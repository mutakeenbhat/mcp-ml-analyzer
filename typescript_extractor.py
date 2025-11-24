<<<<<<< HEAD
# typescript_extractor.py
import os
import re
import json
from pathlib import Path

# Basic syscall patterns for TypeScript / Node.js
SYSCALL_PATTERNS = {
    "filesystem": [r"\bfs\.", r"\bfs/promises\b"],
    "network": [r"\bfetch\(", r"\baxios\.", r"\bhttp\.", r"\bhttps\."],
    "subprocess": [r"\bchild_process\.", r"\bexec\(", r"\bspawn\("],
    "environment": [r"\bprocess\.env"],
}

def detect_syscalls(code: str):
    detected = []
    for syscall_type, patterns in SYSCALL_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, code):
                detected.append(syscall_type)
                break
    return detected

def extract_exported_functions(code: str):
    """
    Detect exported functions like:
    export function ping() {}
    export const add = () => {}
    module.exports = { ping }
    """
    functions = []

    # export function xyz(...)
    export_fn = re.findall(r"export\s+function\s+(\w+)\s*\((.*?)\)", code, re.DOTALL)
    for name, args in export_fn:
        functions.append({"name": name, "args": args})

    # export const xyz = (...)
    export_const = re.findall(r"export\s+const\s+(\w+)\s*=\s*\((.*?)\)", code, re.DOTALL)
    for name, args in export_const:
        functions.append({"name": name, "args": args})

    return functions

def simple_schema_from_args(arg_str: str):
    """
    Very basic schema inference:
    input_schema → {"type": "object", "properties": {...}}
    """
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "count: number" → name=count, type=number
        parts = arg.split(":")
        if len(parts) == 2:
            name = parts[0].strip()
            ts_type = parts[1].strip()
        else:
            name = arg
            ts_type = "any"

        # Convert TS types to JSON types
        if ts_type in ["string"]:
            json_type = "string"
        elif ts_type in ["number"]:
            json_type = "number"
        elif ts_type in ["boolean"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_typescript_repo(repo_path: str):
    repo = Path(repo_path)
    tools = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith((".ts", ".js")):
                continue

            full_path = Path(root) / fname
            code = full_path.read_text(encoding="utf-8", errors="ignore")

            exported = extract_exported_functions(code)
            if not exported:
                continue

            for fn in exported:
                name = fn["name"]
                args = fn["args"]
                input_schema = simple_schema_from_args(args)
                output_schema = {"type": "object"}  # basic placeholder

                syscalls = detect_syscalls(code)

                tools.append({
                    "name": name,
                    "description": f"Tool extracted from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "predicted_code_snippet": f"export function {name}({args}) {{...}}",
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "explanation": f"Extracted from exported function in {fname}",
                    "syscalls": syscalls,
                    "confidence": {
                        "schema": 0.4,
                        "tool": 0.5,
                        "syscalls": 0.6
                    }
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to TypeScript repository: ").strip()
    results = analyze_typescript_repo(repo)
    print(json.dumps(results, indent=2))
=======
# typescript_extractor.py
import os
import re
import json
from pathlib import Path

# Basic syscall patterns for TypeScript / Node.js
SYSCALL_PATTERNS = {
    "filesystem": [r"\bfs\.", r"\bfs/promises\b"],
    "network": [r"\bfetch\(", r"\baxios\.", r"\bhttp\.", r"\bhttps\."],
    "subprocess": [r"\bchild_process\.", r"\bexec\(", r"\bspawn\("],
    "environment": [r"\bprocess\.env"],
}

def detect_syscalls(code: str):
    detected = []
    for syscall_type, patterns in SYSCALL_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, code):
                detected.append(syscall_type)
                break
    return detected

def extract_exported_functions(code: str):
    """
    Detect exported functions like:
    export function ping() {}
    export const add = () => {}
    module.exports = { ping }
    """
    functions = []

    # export function xyz(...)
    export_fn = re.findall(r"export\s+function\s+(\w+)\s*\((.*?)\)", code, re.DOTALL)
    for name, args in export_fn:
        functions.append({"name": name, "args": args})

    # export const xyz = (...)
    export_const = re.findall(r"export\s+const\s+(\w+)\s*=\s*\((.*?)\)", code, re.DOTALL)
    for name, args in export_const:
        functions.append({"name": name, "args": args})

    return functions

def simple_schema_from_args(arg_str: str):
    """
    Very basic schema inference:
    input_schema → {"type": "object", "properties": {...}}
    """
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "count: number" → name=count, type=number
        parts = arg.split(":")
        if len(parts) == 2:
            name = parts[0].strip()
            ts_type = parts[1].strip()
        else:
            name = arg
            ts_type = "any"

        # Convert TS types to JSON types
        if ts_type in ["string"]:
            json_type = "string"
        elif ts_type in ["number"]:
            json_type = "number"
        elif ts_type in ["boolean"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_typescript_repo(repo_path: str):
    repo = Path(repo_path)
    tools = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith((".ts", ".js")):
                continue

            full_path = Path(root) / fname
            code = full_path.read_text(encoding="utf-8", errors="ignore")

            exported = extract_exported_functions(code)
            if not exported:
                continue

            for fn in exported:
                name = fn["name"]
                args = fn["args"]
                input_schema = simple_schema_from_args(args)
                output_schema = {"type": "object"}  # basic placeholder

                syscalls = detect_syscalls(code)

                tools.append({
                    "name": name,
                    "description": f"Tool extracted from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "predicted_code_snippet": f"export function {name}({args}) {{...}}",
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "explanation": f"Extracted from exported function in {fname}",
                    "syscalls": syscalls,
                    "confidence": {
                        "schema": 0.4,
                        "tool": 0.5,
                        "syscalls": 0.6
                    }
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to TypeScript repository: ").strip()
    results = analyze_typescript_repo(repo)
    print(json.dumps(results, indent=2))
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
