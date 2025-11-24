<<<<<<< HEAD
import os
import sys
import json
import tempfile
import shutil
import zipfile
import subprocess

from language_detector import detect_languages
from ts_js_extractor import analyze_ts_js_repo
from rust_extractor import analyze_rust_repo
from go_extractor import analyze_go_repo
from java_extractor import analyze_java_repo


# ============================================================
# 1. Resolve input (Git URL / ZIP / Folder)
# ============================================================
def resolve_repo_path(user_input: str):
    """
    Accepts:
      - GitHub/GitLab URL
      - ZIP file path
      - Local folder path
    Returns a local folder path ready for analysis, or None if invalid.
    """
    user_input = user_input.strip()

    # A) Git URL (GitHub / GitLab)
    if user_input.startswith("http://") or user_input.startswith("https://"):
        print(f"[INFO] Validating repository URL: {user_input}")
        # Validate access with ls-remote
        try:
            subprocess.run(
                ["git", "ls-remote", user_input],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            print(f"[ERROR] Cannot access repo (ls-remote failed): {user_input}")
            return None

        temp_dir = tempfile.mkdtemp(prefix="mcp_git_")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", user_input, temp_dir],
                check=True,
            )
            print(f"[INFO] Repository cloned to: {temp_dir}")
            return temp_dir
        except Exception as e:
            print("[ERROR] Git clone failed:", e)
            shutil.rmtree(temp_dir, ignore_errors=True)
            return None

    # B) ZIP file
    if user_input.lower().endswith(".zip"):
        if not os.path.exists(user_input):
            print("[ERROR] ZIP file not found:", user_input)
            return None

        temp_dir = tempfile.mkdtemp(prefix="mcp_zip_")
        try:
            with zipfile.ZipFile(user_input, "r") as zf:
                zf.extractall(temp_dir)
            items = os.listdir(temp_dir)
            if len(items) == 1:
                inner = os.path.join(temp_dir, items[0])
                if os.path.isdir(inner):
                    return inner
            return temp_dir
        except Exception as e:
            print("[ERROR] ZIP extraction failed:", e)
            shutil.rmtree(temp_dir, ignore_errors=True)
            return None

    # C) Local folder
    if os.path.isdir(user_input):
        return user_input

    print("[ERROR] Invalid input path.")
    return None


# ============================================================
# 2. Output folder helpers
# ============================================================
def get_repo_name(user_input: str) -> str:
    """Derive a repo name for outputs/ folder."""
    s = user_input.strip().rstrip("/").replace("\\", "/")
    if s.startswith("http://") or s.startswith("https://"):
        name = s.split("/")[-1]
        if name.endswith(".git"):
            name = name[:-4]
        return name or "repo"
    # local path or zip
    base = os.path.basename(s)
    if base.endswith(".zip"):
        base = base[:-4]
    return base or "repo"


def prepare_output_folder(repo_name: str) -> str:
    out_dir = os.path.join("outputs", repo_name)
    os.makedirs(out_dir, exist_ok=True)
    print(f"[INFO] Output directory: {out_dir}")
    return out_dir


# ============================================================
# 3. Main analyzer pipeline
# ============================================================
def run_python_pipeline(repo_path: str) -> str | None:
    """
    Full Python MCP pipeline:
      schema_extractor_v3.py  (static analysis + classes)
      sync_payload_schemas.py
      syscall_scanner_v4.py
      generate_readable_report.py
      ml_refiner.py  (optional; may be heavy)

    Returns path to final JSON (mcp_analysis_output_final_ml.json or mcp_analysis_output_final.json),
    or None if something went wrong.
    """
    try:
        # 1) Schema extractor
        print("\n[PYTHON] Running schema_extractor_v3.py ...")
        proc = subprocess.run(
            ["python", "schema_extractor_v3.py"],
            input=(repo_path + "\n").encode(),
            text=False,
            check=True,
        )
    except Exception as e:
        print("[ERROR] schema_extractor_v3.py failed:", e)
        return None

    try:
        # 2) Sync payload schemas
        print("[PYTHON] Running sync_payload_schemas.py ...")
        subprocess.run(["python", "sync_payload_schemas.py"], check=True)
    except Exception as e:
        print("[WARN] sync_payload_schemas.py failed:", e)

    try:
        # 3) Syscall scanner
        print("[PYTHON] Running syscall_scanner_v4.py ...")
        subprocess.run(
            ["python", "syscall_scanner_v4.py"],
            input=(repo_path + "\n").encode(),
            text=False,
            check=True,
        )
    except Exception as e:
        print("[WARN] syscall_scanner_v4.py failed:", e)

    try:
        # 4) Human-readable markdown report
        print("[PYTHON] Running generate_readable_report.py ...")
        subprocess.run(["python", "generate_readable_report.py"], check=True)
    except Exception as e:
        print("[WARN] generate_readable_report.py failed:", e)

    try:
        # 5) ML refinement (optional; don't crash if it fails)
        print("[PYTHON/ML] Running ml_refiner.py (optional; may be slow) ...")
        subprocess.run(["python", "ml_refiner.py"], check=False)
    except Exception as e:
        print("[WARN] ml_refiner.py failed:", e)

    # Prefer ML-refined JSON if present
    ml_json = "mcp_analysis_output_final_ml.json"
    base_json = "mcp_analysis_output_final.json"

    if os.path.exists(ml_json):
        return ml_json
    if os.path.exists(base_json):
        return base_json

    print("[ERROR] No final JSON produced by Python pipeline.")
    return None


def run_full_analysis(repo_path: str, output_dir: str):
    """Detect language, route to correct extractor, and save per-repo output."""

    if not repo_path:
        print("[ERROR] Repo path is invalid; aborting.")
        return

    print("\n[STEP 1] Detecting languages...")
    langs = detect_languages(repo_path)
    print("Detected languages:", langs)

    dominant = max(langs, key=langs.get) if langs else None
    print("Dominant language:", dominant)

    final_report: dict = {
        "language": dominant or "unknown",
        "transport": {"type": "unknown", "confidence": 0.0, "evidence": []},
        "tools": [],
        "run_template": {"command": "unknown", "confidence": 0.0},
    }

    try:
        # ----------------------------------------------------
        # PYTHON PATH (full static + ML pipeline)
        # ----------------------------------------------------
        if dominant == "python":
            final_json_path = run_python_pipeline(repo_path)
            if final_json_path and os.path.exists(final_json_path):
                with open(final_json_path, "r", encoding="utf-8") as f:
                    final_report = json.load(f)
            else:
                print("[WARN] Python pipeline did not produce a final JSON.")
                final_report["tools"] = []

        # ----------------------------------------------------
        # TYPESCRIPT / JAVASCRIPT PATH
        # ----------------------------------------------------
        elif dominant in ("typescript", "javascript"):
            print("\n[TS/JS] Running ts_js_extractor ...")
            tools = analyze_ts_js_repo(repo_path) or []
            final_report.update(
                {
                    "language": dominant,
                    "transport": {
                        "type": "http",
                        "confidence": 0.4,
                        "evidence": [],
                    },
                    "tools": tools,
                    "run_template": {
                        "command": "node server.js",
                        "confidence": 0.4,
                    },
                }
            )

        # ----------------------------------------------------
        # RUST PATH
        # ----------------------------------------------------
        elif dominant == "rust":
            print("\n[RUST] Running rust_extractor ...")
            tools = analyze_rust_repo(repo_path) or []
            final_report.update(
                {
                    "language": "rust",
                    "transport": {
                        "type": "http",
                        "confidence": 0.4,
                        "evidence": [],
                    },
                    "tools": tools,
                    "run_template": {
                        "command": "cargo run",
                        "confidence": 0.4,
                    },
                }
            )

        # ----------------------------------------------------
        # GO PATH
        # ----------------------------------------------------
        elif dominant == "go":
            print("\n[GO] Running go_extractor ...")
            tools = analyze_go_repo(repo_path) or []
            final_report.update(
                {
                    "language": "go",
                    "transport": {
                        "type": "http",
                        "confidence": 0.4,
                        "evidence": [],
                    },
                    "tools": tools,
                    "run_template": {
                        "command": "go run main.go",
                        "confidence": 0.4,
                    },
                }
            )

        # ----------------------------------------------------
        # JAVA PATH
        # ----------------------------------------------------
        elif dominant == "java":
            print("\n[JAVA] Running java_extractor ...")
            tools = analyze_java_repo(repo_path) or []
            final_report.update(
                {
                    "language": "java",
                    "transport": {
                        "type": "http",
                        "confidence": 0.4,
                        "evidence": [],
                    },
                    "tools": tools,
                    "run_template": {
                        "command": "mvn spring-boot:run",
                        "confidence": 0.4,
                    },
                }
            )

        else:
            print("[WARN] No supported dominant language; leaving tools empty.")

        # ----------------------------------------------------
        # Optional: copy syscall_report.json into output_dir
        # (Python pipeline writes it; other languages may too)
        # ----------------------------------------------------
        syscall_path = "syscall_report.json"
        if os.path.exists(syscall_path):
            shutil.copy(syscall_path, os.path.join(output_dir, "syscall_report.json"))

        # If Python pipeline generated markdown, copy it too
        md_path = "mcp_final_report_readable.md"
        if os.path.exists(md_path):
            shutil.copy(md_path, os.path.join(output_dir, "mcp_final_report_readable.md"))

        # ----------------------------------------------------
        # FINAL: Save per-repo JSON only if tools exist
        # ----------------------------------------------------
        tools = final_report.get("tools", [])
        if tools and len(tools) > 0:
            out_json = os.path.join(output_dir, "mcp_analysis_output_final.json")
            with open(out_json, "w", encoding="utf-8") as f:
                json.dump(final_report, f, indent=2)
            print(f"[SUCCESS] Final JSON saved: {out_json}")
        else:
            skip_log = os.path.join(output_dir, "skip.log")
            with open(skip_log, "w", encoding="utf-8") as f:
                f.write("No MCP tools found; JSON not saved.\n")
            print(
                "[SKIP] No MCP tools detected for this repo; see skip.log in output folder."
            )

    except Exception as e:
        err_path = os.path.join(output_dir, "analyzer_error.log")
        with open(err_path, "w", encoding="utf-8") as ef:
            ef.write(f"Error during analysis:\n{e}\n")
        print("[ERROR] Analysis failed; see analyzer_error.log for details.")


# ============================================================
# 4. Main entry
# ============================================================
if __name__ == "__main__":
    user_input = input("Enter repository URL, ZIP path, or folder: ").strip()

    repo_path = resolve_repo_path(user_input)
    if not repo_path:
        sys.exit(1)

    repo_name = get_repo_name(user_input)
    output_dir = prepare_output_folder(repo_name)

    run_full_analysis(repo_path, output_dir)

    # Clean up temp cloned/extracted repos
    if repo_path.startswith(tempfile.gettempdir()):
        shutil.rmtree(repo_path, ignore_errors=True)
=======
# multi_lang_analyzer.py
import json
import subprocess
from pathlib import Path

from language_detector import detect_languages, dominant_language
from ts_js_extractor import analyze_ts_js_repo
from go_extractor import analyze_go_repo
from java_extractor import analyze_java_repo
from rust_extractor import analyze_rust_repo

THIS_DIR = Path(__file__).parent

def run_python_pipeline(repo_path: str):
    """
    Runs your existing Python-only pipeline:
      1) schema_extractor_v3.py
      2) sync_payload_schemas.py
      3) syscall_scanner_v4.py
      4) generate_readable_report.py

    Assumes those scripts are in the same folder as this file.
    """
    print("\n[PYTHON] Running schema_extractor_v3.py...")
    subprocess.run(
        ["python", "schema_extractor_v3.py"],
        cwd=THIS_DIR,
        check=True,
        input=(repo_path + "\n").encode(),  # for input() inside the script
    )

    print("\n[PYTHON] Running sync_payload_schemas.py...")
    subprocess.run(
        ["python", "sync_payload_schemas.py"],
        cwd=THIS_DIR,
        check=True,
    )

    print("\n[PYTHON] Running syscall_scanner_v4.py...")
    subprocess.run(
        ["python", "syscall_scanner_v4.py"],
        cwd=THIS_DIR,
        check=True,
        input=(repo_path + "\n").encode(),  # for input() inside the script
    )

    print("\n[PYTHON] Running generate_readable_report.py...")
    subprocess.run(
        ["python", "generate_readable_report.py"],
        cwd=THIS_DIR,
        check=True,
    )

    print("\n[PYTHON] Done. Your final JSON is: mcp_analysis_output_final.json")
    print("Readable report: mcp_final_report_readable.md\n")

def build_non_python_report(language: str, tools):
    """
    Build a minimal MCP JSON report for non-Python languages.
    """
    if language in ("typescript", "javascript"):
        transport_type = "http"
        run_cmd = "node server.js"
    elif language == "go":
        transport_type = "http"
        run_cmd = "go run main.go"
    elif language == "java":
        transport_type = "http"
        run_cmd = "java Main"
    elif language == "rust":
        transport_type = "http"
        run_cmd = "cargo run"
    else:
        transport_type = "stdio"
        run_cmd = "server"

    report = {
        "language": language,
        "transport": {
            "type": transport_type,
            "confidence": 0.3,
            "evidence": [],
        },
        "tools": tools,
        "run_template": {
            "command": run_cmd,
            "confidence": 0.3,
        },
    }

    out_path = THIS_DIR / "mcp_analysis_output_final.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"\n[{language.upper()}] JSON report written to: {out_path}\n")

def main():
    repo_path = input("Enter path to repository folder or extracted ZIP: ").strip()
    if not repo_path:
        print("No path given.")
        return
    if not Path(repo_path).exists():
        print("Path does not exist:", repo_path)
        return

    lang_counts = detect_languages(repo_path)
    dom_lang = dominant_language(lang_counts)

    print("\nDetected languages:", lang_counts)
    print("Dominant language:", dom_lang)

    if dom_lang == "python":
        run_python_pipeline(repo_path)

    elif dom_lang in ("typescript", "javascript"):
        print("\n[INFO] Running basic TypeScript/JavaScript extractor...")
        tools = analyze_ts_js_repo(repo_path)
        build_non_python_report(dom_lang, tools)

    elif dom_lang == "go":
        print("\n[INFO] Running basic Go extractor...")
        tools = analyze_go_repo(repo_path)
        build_non_python_report(dom_lang, tools)

    elif dom_lang == "java":
        print("\n[INFO] Running basic Java extractor...")
        tools = analyze_java_repo(repo_path)
        build_non_python_report(dom_lang, tools)

    elif dom_lang == "rust":
        print("\n[INFO] Running basic Rust extractor...")
        tools = analyze_rust_repo(repo_path)
        build_non_python_report(dom_lang, tools)

    else:
        print(f"\nLanguage '{dom_lang}' is not yet supported.\n")

if __name__ == "__main__":
    main()
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
