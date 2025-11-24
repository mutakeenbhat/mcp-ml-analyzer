<<<<<<< HEAD
# java_extractor.py
import os
import re
from pathlib import Path
from typing import List, Dict, Any

JAVA_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"\bFileInputStream\b", "FileInputStream"),
        (r"\bFiles\.", "Files.*"),
    ],
    "network": [
        (r"\bHttpURLConnection\b", "HttpURLConnection"),
        (r"\bHttpClient\b", "HttpClient"),
    ],
    "subprocess": [
        (r"\bProcessBuilder\b", "ProcessBuilder"),
        (r"Runtime\.getRuntime\(\)\.exec", "Runtime.exec"),
    ],
    "env": [
        (r"System\.getenv\(", "System.getenv"),
    ],
}

def detect_syscalls_java(code: str) -> Dict[str, List[str]]:
    result = {"filesystem": [], "network": [], "subprocess": [], "env": []}
    for category, patterns in JAVA_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                if label not in result[category]:
                    result[category].append(label)
    return result

def extract_public_methods(code: str):
    """
    Very rough detection of public methods:
      public ReturnType methodName(args) {
    """
    methods = []
    matches = re.findall(
        r"public\s+[\w<>]+\s+(\w+)\s*\((.*?)\)\s*\{", code, re.DOTALL
    )
    for name, args in matches:
        methods.append({"name": name, "args": args})
    return methods

def simple_schema_from_java_args(arg_str: str) -> Dict[str, Any]:
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "String name" or "int id"
        parts = arg.split()
        if len(parts) >= 2:
            java_type = parts[0]
            name = parts[1]
        else:
            name = arg
            java_type = "Object"

        if java_type in ["String"]:
            json_type = "string"
        elif java_type in ["int", "long", "float", "double"]:
            json_type = "number"
        elif java_type in ["boolean"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_java_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    tools: List[Dict[str, Any]] = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith(".java"):
                continue

            full_path = Path(root) / fname
            try:
                code = full_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            methods = extract_public_methods(code)
            if not methods:
                continue

            syscalls = detect_syscalls_java(code)

            for m in methods:
                name = m["name"]
                args = m["args"]
                input_schema = simple_schema_from_java_args(args)
                output_schema = {"type": "object"}

                tools.append({
                    "name": name,
                    "description": f"Public Java method from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": f"public ... {name}({args}) {{ ... }}",
                    "explanation": f"Extracted from public Java method in {fname}",
                    "syscalls": syscalls,
                    "confidence": 0.3,
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to Java repository: ").strip()
    java_tools = analyze_java_repo(repo)
    import json
    print(json.dumps(java_tools, indent=2))
=======
# java_extractor.py
import os
import re
from pathlib import Path
from typing import List, Dict, Any

JAVA_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"\bFileInputStream\b", "FileInputStream"),
        (r"\bFiles\.", "Files.*"),
    ],
    "network": [
        (r"\bHttpURLConnection\b", "HttpURLConnection"),
        (r"\bHttpClient\b", "HttpClient"),
    ],
    "subprocess": [
        (r"\bProcessBuilder\b", "ProcessBuilder"),
        (r"Runtime\.getRuntime\(\)\.exec", "Runtime.exec"),
    ],
    "env": [
        (r"System\.getenv\(", "System.getenv"),
    ],
}

def detect_syscalls_java(code: str) -> Dict[str, List[str]]:
    result = {"filesystem": [], "network": [], "subprocess": [], "env": []}
    for category, patterns in JAVA_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                if label not in result[category]:
                    result[category].append(label)
    return result

def extract_public_methods(code: str):
    """
    Very rough detection of public methods:
      public ReturnType methodName(args) {
    """
    methods = []
    matches = re.findall(
        r"public\s+[\w<>]+\s+(\w+)\s*\((.*?)\)\s*\{", code, re.DOTALL
    )
    for name, args in matches:
        methods.append({"name": name, "args": args})
    return methods

def simple_schema_from_java_args(arg_str: str) -> Dict[str, Any]:
    if not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props = {}
    for arg in inputs:
        # Example: "String name" or "int id"
        parts = arg.split()
        if len(parts) >= 2:
            java_type = parts[0]
            name = parts[1]
        else:
            name = arg
            java_type = "Object"

        if java_type in ["String"]:
            json_type = "string"
        elif java_type in ["int", "long", "float", "double"]:
            json_type = "number"
        elif java_type in ["boolean"]:
            json_type = "boolean"
        else:
            json_type = "object"

        props[name] = {"type": json_type}

    return {"type": "object", "properties": props}

def analyze_java_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    tools: List[Dict[str, Any]] = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith(".java"):
                continue

            full_path = Path(root) / fname
            try:
                code = full_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            methods = extract_public_methods(code)
            if not methods:
                continue

            syscalls = detect_syscalls_java(code)

            for m in methods:
                name = m["name"]
                args = m["args"]
                input_schema = simple_schema_from_java_args(args)
                output_schema = {"type": "object"}

                tools.append({
                    "name": name,
                    "description": f"Public Java method from {fname}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": f"public ... {name}({args}) {{ ... }}",
                    "explanation": f"Extracted from public Java method in {fname}",
                    "syscalls": syscalls,
                    "confidence": 0.3,
                })

    return tools

if __name__ == "__main__":
    repo = input("Enter path to Java repository: ").strip()
    java_tools = analyze_java_repo(repo)
    import json
    print(json.dumps(java_tools, indent=2))
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
