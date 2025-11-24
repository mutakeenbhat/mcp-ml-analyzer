<<<<<<< HEAD
# go_extractor.py
import os
import re
from pathlib import Path
from typing import List, Dict, Any

GO_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"\bos\.Open\(", "os.Open"),
        (r"\bioutil\.ReadFile\(", "ioutil.ReadFile"),
        (r"\bos\.Create\(", "os.Create"),
    ],
    "network": [
        (r"\bhttp\.Get\(", "http.Get"),
        (r"\bhttp\.Post\(", "http.Post"),
        (r"\bnet/http\b", "net/http"),
    ],
    "subprocess": [
        (r"\bexec\.Command\(", "exec.Command"),
    ],
    "env": [
        (r"\bos\.Getenv\(", "os.Getenv"),
    ],
}

def detect_syscalls_go(code: str) -> Dict[str, List[str]]:
    result = {"filesystem": [], "network": [], "subprocess": [], "env": []}
    for category, patterns in GO_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                if label not in result[category]:
                    result[category].append(label)
    return result

def extract_exported_functions_go(code: str):
    """
    Detect exported functions like:
      func Ping(...) ...
    where the function name starts with a capital letter.
    """
    funcs = []
    matches = re.findall(r"func\s+([A-Z]\w*)\s*\((.*?)\)", code, re.DOTALL)
    for name, args in matches:
        funcs.append({"name": name, "args": args})
    return funcs

def simple_schema_from_go_args(arg_str: str) -> Dict[str, Any]:
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "ctx context.Context" or "id int"
        parts = arg.split()
        if len(parts) >= 2:
            name = parts[0]
            go_type = parts[1]
        else:
            name = arg
            go_type = "interface{}"

        if go_type in ["string"]:
            json_type = "string"
        elif go_type in ["int", "int64", "float32", "float64"]:
            json_type = "number"
        elif go_type in ["bool"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_go_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    tools: List[Dict[str, Any]] = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith(".go"):
                continue

            full_path = Path(root) / fname
            try:
                code = full_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            funcs = extract_exported_functions_go(code)
            if not funcs:
                continue

            syscalls = detect_syscalls_go(code)

            for fn in funcs:
                name = fn["name"]
                args = fn["args"]
                input_schema = simple_schema_from_go_args(args)
                output_schema = {"type": "object"}

                tools.append({
                    "name": name,
                    "description": f"Exported Go function from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": f"func {name}({args}) ...",
                    "explanation": f"Extracted from exported Go function in {fname}",
                    "syscalls": syscalls,
                    "confidence": 0.35,
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to Go repository: ").strip()
    go_tools = analyze_go_repo(repo)
    import json
    print(json.dumps(go_tools, indent=2))
=======
# go_extractor.py
import os
import re
from pathlib import Path
from typing import List, Dict, Any

GO_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"\bos\.Open\(", "os.Open"),
        (r"\bioutil\.ReadFile\(", "ioutil.ReadFile"),
        (r"\bos\.Create\(", "os.Create"),
    ],
    "network": [
        (r"\bhttp\.Get\(", "http.Get"),
        (r"\bhttp\.Post\(", "http.Post"),
        (r"\bnet/http\b", "net/http"),
    ],
    "subprocess": [
        (r"\bexec\.Command\(", "exec.Command"),
    ],
    "env": [
        (r"\bos\.Getenv\(", "os.Getenv"),
    ],
}

def detect_syscalls_go(code: str) -> Dict[str, List[str]]:
    result = {"filesystem": [], "network": [], "subprocess": [], "env": []}
    for category, patterns in GO_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                if label not in result[category]:
                    result[category].append(label)
    return result

def extract_exported_functions_go(code: str):
    """
    Detect exported functions like:
      func Ping(...) ...
    where the function name starts with a capital letter.
    """
    funcs = []
    matches = re.findall(r"func\s+([A-Z]\w*)\s*\((.*?)\)", code, re.DOTALL)
    for name, args in matches:
        funcs.append({"name": name, "args": args})
    return funcs

def simple_schema_from_go_args(arg_str: str) -> Dict[str, Any]:
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "ctx context.Context" or "id int"
        parts = arg.split()
        if len(parts) >= 2:
            name = parts[0]
            go_type = parts[1]
        else:
            name = arg
            go_type = "interface{}"

        if go_type in ["string"]:
            json_type = "string"
        elif go_type in ["int", "int64", "float32", "float64"]:
            json_type = "number"
        elif go_type in ["bool"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_go_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    tools: List[Dict[str, Any]] = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith(".go"):
                continue

            full_path = Path(root) / fname
            try:
                code = full_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            funcs = extract_exported_functions_go(code)
            if not funcs:
                continue

            syscalls = detect_syscalls_go(code)

            for fn in funcs:
                name = fn["name"]
                args = fn["args"]
                input_schema = simple_schema_from_go_args(args)
                output_schema = {"type": "object"}

                tools.append({
                    "name": name,
                    "description": f"Exported Go function from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": f"func {name}({args}) ...",
                    "explanation": f"Extracted from exported Go function in {fname}",
                    "syscalls": syscalls,
                    "confidence": 0.35,
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to Go repository: ").strip()
    go_tools = analyze_go_repo(repo)
    import json
    print(json.dumps(go_tools, indent=2))
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
