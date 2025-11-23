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
