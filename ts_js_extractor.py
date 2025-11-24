<<<<<<< HEAD
# ts_js_extractor.py  (UPGRADED VERSION)

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

# -------------------------------------
# 1. Syscall detection (same idea as before)
# -------------------------------------
TS_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"\bfs\.", "fs"),
        (r"\bfs/promises\b", "fs.promises"),
    ],
    "network": [
        (r"\bfetch\(", "fetch"),
        (r"\baxios\.", "axios"),
        (r"\bhttp\.", "http"),
        (r"\bhttps\.", "https"),
    ],
    "subprocess": [
        (r"\bchild_process\.", "child_process"),
        (r"\bexec\(", "exec"),
        (r"\bspawn\(", "spawn"),
    ],
    "env": [
        (r"\bprocess\.env\b", "process.env"),
    ],
}


def detect_syscalls(code: str) -> Dict[str, List[str]]:
    result = {key: [] for key in TS_SYSCALL_PATTERNS.keys()}
    for category, patterns in TS_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                if label not in result[category]:
                    result[category].append(label)
    return result


# -------------------------------------
# 2. Helpers for schema inference
# -------------------------------------
def infer_json_type(ts_type: str) -> str:
    ts_type = ts_type.strip()
    if ts_type in ("string", "String"):
        return "string"
    if ts_type in ("number", "Number", "bigint", "BigInt"):
        return "number"
    if ts_type in ("boolean", "Boolean"):
        return "boolean"
    if ts_type.endswith("[]"):
        return "array"
    return "object"


def simple_schema_from_args(arg_str: str) -> Dict[str, Any]:
    """
    Very simple TS/JS arg parser → JSON schema.
    Handles patterns like:
      name: string
      id: number
      query: Query
    """
    if not arg_str or not arg_str.strip():
        return {"type": "object", "properties": {}}

    inputs = [a.strip() for a in arg_str.split(",") if a.strip()]
    props: Dict[str, Any] = {}

    for arg in inputs:
        # Examples:
        #   "id: number"
        #   "query: Query"
        #   "ctx"
        parts = arg.split(":")
        if len(parts) == 2:
            name = parts[0].strip()
            ts_type = parts[1].strip()
        else:
            name = arg.strip()
            ts_type = "any"

        jt = infer_json_type(ts_type)
        prop: Dict[str, Any] = {"type": jt}
        if jt == "array":
            prop["items"] = {"type": "string"}
        props[name] = prop

    return {"type": "object", "properties": props}


def empty_schema() -> Dict[str, Any]:
    return {"type": "object", "properties": {}}


# -------------------------------------
# 3. Extract patterns
# -------------------------------------

EXPORT_FN_REGEX = re.compile(
    r"export\s+function\s+(\w+)\s*\((.*?)\)",
    re.DOTALL
)

EXPORT_CONST_FN_REGEX = re.compile(
    r"export\s+const\s+(\w+)\s*=\s*\((.*?)\)\s*=>",
    re.DOTALL
)

# tools: { foo: {...}, bar: {...} }
TOOLS_OBJECT_REGEX = re.compile(
    r"tools\s*:\s*\{([^}]+)\}",
    re.DOTALL
)

TOOL_ENTRY_REGEX = re.compile(
    r"(\w+)\s*:\s*\{([^}]*)\}",
    re.DOTALL
)

# export default { tools: { ... } }
EXPORT_DEFAULT_TOOLS_REGEX = re.compile(
    r"export\s+default\s*\{\s*tools\s*:\s*\{([^}]+)\}",
    re.DOTALL
)


def extract_exported_functions(code: str) -> List[Dict[str, Any]]:
    tools: List[Dict[str, Any]] = []

    for name, args in EXPORT_FN_REGEX.findall(code):
        tools.append({
            "name": name,
            "args": args,
            "source": "export_function"
        })

    for name, args in EXPORT_CONST_FN_REGEX.findall(code):
        tools.append({
            "name": name,
            "args": args,
            "source": "export_const_function"
        })

    return tools


def extract_tools_from_tools_object(code: str) -> List[Dict[str, Any]]:
    tools: List[Dict[str, Any]] = []

    # direct tools: { ... }
    m = TOOLS_OBJECT_REGEX.search(code)
    blocks = []

    if m:
        blocks.append(m.group(1))

    # export default { tools: { ... } }
    m2 = EXPORT_DEFAULT_TOOLS_REGEX.search(code)
    if m2:
        blocks.append(m2.group(1))

    for block in blocks:
        for tmatch in TOOL_ENTRY_REGEX.finditer(block):
            tname = tmatch.group(1)
            tbody = tmatch.group(2)
            tools.append({
                "name": tname,
                "args": "",
                "body": tbody,
                "source": "tools_object"
            })

    return tools


# -------------------------------------
# 4. Main TS/JS repo analyzer
# -------------------------------------
def analyze_ts_js_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    extracted_tools: List[Dict[str, Any]] = []

    for root, dirs, files in os.walk(repo):
        # Skip node_modules / dist / build etc.
        skip = {"node_modules", "dist", "build", ".git", ".next"}
        dirs[:] = [d for d in dirs if d not in skip]

        for fname in files:
            if not fname.endswith((".ts", ".tsx", ".js", ".jsx")):
                continue

            full_path = Path(root) / fname
            try:
                code = full_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            rel_path = full_path.relative_to(repo)

            # detect syscalls for this file
            syscalls = detect_syscalls(code)

            # 1) exported functions
            exported_funcs = extract_exported_functions(code)

            for fn in exported_funcs:
                name = fn["name"]
                args = fn["args"]
                input_schema = simple_schema_from_args(args)
                output_schema = empty_schema()

                extracted_tools.append({
                    "name": name,
                    "description": f"Exported function '{name}' from {rel_path}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": f"export function {name}({args}) {{ ... }}",
                    "explanation": f"Detected as exported function in {rel_path}",
                    "syscalls": syscalls,
                    "confidence": 0.6
                })

            # 2) tools: { foo: {...} } blocks
            tools_objs = extract_tools_from_tools_object(code)

            for t in tools_objs:
                name = t["name"]
                body = t.get("body", "")
                input_schema = empty_schema()
                output_schema = empty_schema()

                extracted_tools.append({
                    "name": name,
                    "description": f"Tool '{name}' detected in tools object in {rel_path}",
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "payload_shape": {
                        "request": input_schema,
                        "response": output_schema,
                    },
                    "predicted_code_snippet": body[:500],
                    "explanation": f"Detected inside tools: {{}} block in {rel_path}",
                    "syscalls": syscalls,
                    "confidence": 0.5
                })

    return extracted_tools


if __name__ == "__main__":
    repo = input("Enter path to TS/JS repo: ").strip()
    tools = analyze_ts_js_repo(repo)
    print(json.dumps(tools, indent=2))
=======
# ts_js_extractor.py  (UPGRADED VERSION)

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any


# -------------------------------------
# 1. Detect syscalls (same as before)
# -------------------------------------
TS_SYSCALL_PATTERNS = {
    "filesystem": [
        (r"\bfs\.", "fs"),
        (r"\bfs/promises\b", "fs.promises"),
    ],
    "network": [
        (r"\bfetch\(", "fetch"),
        (r"\baxios\.", "axios"),
        (r"\bhttp\.", "http"),
        (r"\bhttps\.", "https"),
    ],
    "subprocess": [
        (r"\bchild_process\.", "child_process"),
        (r"\bexec\(", "exec"),
        (r"\bspawn\(", "spawn"),
    ],
    "env": [
        (r"\bprocess\.env\b", "process.env"),
    ],
}


def detect_syscalls(code: str) -> Dict[str, List[str]]:
    result = {key: [] for key in TS_SYSCALL_PATTERNS.keys()}
    for category, patterns in TS_SYSCALL_PATTERNS.items():
        for pat, label in patterns:
            if re.search(pat, code):
                result[category].append(label)
    return result


# -----------------------------------------------------------
# 2. NEW: Detect tools inside "tools: { ... }" blocks
# -----------------------------------------------------------
TOOLS_OBJECT_REGEX = re.compile(
    r"tools\s*:\s*\{([^}]*)\}",
    re.DOTALL
)

TOOL_ENTRY_REGEX = re.compile(
    r"(\w+)\s*:\s*\{([^}]*)\}",
    re.DOTALL
)


def extract_tools_from_tools_object(code: str) -> List[Dict[str, Any]]:
    tools = []
    match = TOOLS_OBJECT_REGEX.search(code)
    if not match:
        return tools

    inner = match.group(1)

    for tool_match in TOOL_ENTRY_REGEX.finditer(inner):
        name = tool_match.group(1)
        body = tool_match.group(2)

        tools.append({
            "name": name,
            "description": f"Tool '{name}' detected inside tools: {{}} block",
            "raw_body": body.strip()
        })

    return tools


# -----------------------------------------------------------------
# 3. NEW: Detect toolkit.addTool("name", handler)
# -----------------------------------------------------------------
ADD_TOOL_REGEX = re.compile(
    r"addTool\s*\(\s*['\"](\w+)['\"]\s*,",
    re.DOTALL
)


def extract_addTool_calls(code: str) -> List[Dict[str, Any]]:
    tools = []
    for match in ADD_TOOL_REGEX.finditer(code):
        name = match.group(1)
        tools.append({
            "name": name,
            "description": f"Tool '{name}' detected via addTool(...)",
            "raw_body": ""
        })
    return tools


# -----------------------------------------------------------------
# 4. NEW: Detect register("name", handler)
# -----------------------------------------------------------------
REGISTER_REGEX = re.compile(
    r"register\s*\(\s*['\"](\w+)['\"]\s*,",
    re.DOTALL
)


def extract_register_calls(code: str) -> List[Dict[str, Any]]:
    tools = []
    for match in REGISTER_REGEX.finditer(code):
        name = match.group(1)
        tools.append({
            "name": name,
            "description": f"Tool '{name}' detected via register(...)",
            "raw_body": ""
        })
    return tools


# -----------------------------------------------------------------
# 5. Basic schema placeholder (we can ML-refine later)
# -----------------------------------------------------------------
def empty_schema():
    return {"type": "object", "properties": {}}


# -----------------------------------------------------------------
# 6. MAIN EXTRACTOR
# -----------------------------------------------------------------
def analyze_ts_js_repo(repo_path: str) -> List[Dict[str, Any]]:
    repo = Path(repo_path)
    extracted_tools: List[Dict[str, Any]] = []

    for root, _, files in os.walk(repo):
        for fname in files:
            if not fname.endswith((".ts", ".tsx", ".js", ".jsx")):
                continue

            full_path = Path(root) / fname
            code = full_path.read_text(encoding="utf-8", errors="ignore")

            # 1) detect tools: { ... }
            tools_from_object = extract_tools_from_tools_object(code)

            # 2) detect toolkit.addTool(...)
            tools_from_add_tool = extract_addTool_calls(code)

            # 3) detect register(...)
            tools_from_register = extract_register_calls(code)

            all_found = tools_from_object + tools_from_add_tool + tools_from_register

            # Add schemas + syscalls
            syscalls = detect_syscalls(code)

            for t in all_found:
                extracted_tools.append({
                    "name": t["name"],
                    "description": t["description"],
                    "input_schema": empty_schema(),
                    "output_schema": empty_schema(),
                    "payload_shape": {
                        "request": empty_schema(),
                        "response": empty_schema(),
                    },
                    "predicted_code_snippet": t.get("raw_body", "")[:500],
                    "explanation": "Detected from static TypeScript patterns",
                    "syscalls": syscalls,
                    "confidence": 0.45
                })

    return extracted_tools


if __name__ == "__main__":
    repo = input("Enter path to TS/JS repo: ").strip()
    tools = analyze_ts_js_repo(repo)
    print(json.dumps(tools, indent=2))
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
