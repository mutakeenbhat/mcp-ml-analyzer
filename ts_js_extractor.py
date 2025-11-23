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
