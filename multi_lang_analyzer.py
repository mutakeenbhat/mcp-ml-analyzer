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
