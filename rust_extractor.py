<<<<<<< HEAD
# rust_extractor.py — Upgraded Rust MCP Extractor
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

# ---------------------------------------
# 1. Syscall detection patterns
# ---------------------------------------
RUST_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"std::fs", "std::fs"),
        (r"tokio::fs", "tokio::fs"),
    ],
    "network": [
        (r"reqwest::", "reqwest"),
        (r"ureq::", "ureq"),
        (r"hyper::", "hyper"),
    ],
    "subprocess": [
        (r"std::process", "std::process"),
        (r"tokio::process", "tokio::process"),
        (r"Command::new", "Command::new"),
    ],
}

def detect_syscalls(code: str) -> Dict[str, List[str]]:
    result = {key: [] for key in RUST_SYSCALL_PATTERNS}
    for category, patterns in RUST_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                result[category].append(label)
    return result


# --------------------------------------------------------
# 2. Infer JSON schema from Rust types
# --------------------------------------------------------
def rust_type_to_json(t: str) -> str:
    t = t.strip()

    if t.startswith("&str") or t == "String":
        return "string"
    if t in ("i32", "i64", "u32", "u64", "f32", "f64", "usize", "isize"):
        return "number"
    if t == "bool":
        return "boolean"
    if t.endswith("Vec") or t.startswith("Vec<") or t.endswith("]"):
        return "array"

    return "object"


def parse_structs(code: str) -> Dict[str, Dict[str, Any]]:
    structs = {}
    pattern = r"struct\s+(\w+)\s*\{([^}]+)\}"
    for name, body in re.findall(pattern, code, re.DOTALL):
        fields = {}
        for line in body.split("\n"):
            line = line.strip().rstrip(",")
            if ":" not in line:
                continue
            fname, ftype = line.split(":", 1)
            fields[fname.strip()] = {"type": rust_type_to_json(ftype)}
        structs[name] = {"type": "object", "properties": fields}
    return structs


# --------------------------------------------------------
# 3. Extract Rust functions
# --------------------------------------------------------
FN_REGEX = re.compile(
    r"pub\s+(?:async\s+)?fn\s+(\w+)\s*\(([^)]*)\)\s*(?:->\s*([^{]+))?\s*\{",
    re.DOTALL
)

def extract_functions(code: str) -> List[Dict[str, Any]]:
    fns = []

    for match in FN_REGEX.finditer(code):
        name, args, ret = match.groups()

        inputs = {}
        if args.strip():
            parts = args.split(",")
            for p in parts:
                p = p.strip()
                if ":" in p:
                    aname, atype = p.split(":", 1)
                    inputs[aname.strip()] = {"type": rust_type_to_json(atype)}
                else:
                    inputs[p] = {"type": "object"}

        output_schema = {"type": rust_type_to_json(ret or "object")}

        fns.append({
            "name": name,
            "input_schema": {
                "type": "object",
                "properties": inputs
            },
            "output_schema": output_schema
        })

    return fns


# --------------------------------------------------------
# 4. Main Rust repo analyzer
# --------------------------------------------------------
def analyze_rust_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    extracted_tools = []

    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in ("target", ".git")]

        for fname in files:
            if not fname.endswith(".rs"):
                continue

            full_path = Path(root) / fname
            code = full_path.read_text(encoding="utf-8", errors="ignore")
            rel = str(full_path.relative_to(repo))

            structs = parse_structs(code)
            syscalls = detect_syscalls(code)
            functions = extract_functions(code)

            for f in functions:
                extracted_tools.append({
                    "name": f["name"],
                    "description": f"Rust function '{f['name']}' in {rel}",
                    "input_schema": f["input_schema"],
                    "output_schema": f["output_schema"],
                    "payload_shape": {
                        "request": f["input_schema"],
                        "response": f["output_schema"]
                    },
                    "predicted_code_snippet": f"pub fn {f['name']}(...) {{ ... }}",
                    "explanation": f"Detected Rust function in {rel}",
                    "syscalls": syscalls,
                    "confidence": 0.65
                })

    return extracted_tools


if __name__ == "__main__":
    path = input("Enter Rust repo path: ").strip()
    tools = analyze_rust_repo(path)
    print(json.dumps(tools, indent=2))
=======
# rust_extractor.py
import os
import re
from pathlib import Path
from typing import List, Dict, Any

RUST_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"std::fs::", "std::fs"),
        (r"fs::File", "fs::File"),
    ],
    "network": [
        (r"reqwest::", "reqwest"),
        (r"hyper::", "hyper"),
    ],
    "subprocess": [
        (r"std::process::Command", "std::process::Command"),
    ],
    "env": [
        (r"std::env::var", "std::env::var"),
    ],
}

def detect_syscalls_rust(code: str) -> Dict[str, List[str]]:
    result = {"filesystem": [], "network": [], "subprocess": [], "env": []}
    for category, patterns in RUST_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                if label not in result[category]:
                    result[category].append(label)
    return result

def extract_pub_functions(code: str):
    """
    Detect pub fn functions:
      pub fn name(args...) {
    """
    funcs = []
    matches = re.findall(r"pub\s+fn\s+(\w+)\s*\((.*?)\)", code, re.DOTALL)
    for name, args in matches:
        funcs.append({"name": name, "args": args})
    return funcs

def simple_schema_from_rust_args(arg_str: str) -> Dict[str, Any]:
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "name: String" or "id: i32"
        parts = arg.split(":")
        if len(parts) == 2:
            name = parts[0].strip()
            rust_type = parts[1].strip()
        else:
            name = arg
            rust_type = "&str"

        if rust_type in ["String", "&str"]:
            json_type = "string"
        elif rust_type in ["i32", "i64", "u32", "u64", "f32", "f64"]:
            json_type = "number"
        elif rust_type in ["bool"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_rust_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    tools: List[Dict[str, Any]] = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith(".rs"):
                continue

            full_path = Path(root) / fname
            try:
                code = full_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            funcs = extract_pub_functions(code)
            if not funcs:
                continue

            syscalls = detect_syscalls_rust(code)

            for fn in funcs:
                name = fn["name"]
                args = fn["args"]
                input_schema = simple_schema_from_rust_args(args)
                output_schema = {"type": "object"}

                tools.append({
                    "name": name,
                    "description": f"Public Rust function from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": f"pub fn {name}({args}) {{ ... }}",
                    "explanation": f"Extracted from public Rust function in {fname}",
                    "syscalls": syscalls,
                    "confidence": 0.3,
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to Rust repository: ").strip()
    rust_tools = analyze_rust_repo(repo)
    import json
    print(json.dumps(rust_tools, indent=2))
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
