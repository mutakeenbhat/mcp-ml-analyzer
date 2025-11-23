import os
import json
import ast
from pathlib import Path
from typing import Dict, Any, Optional, List


# ---------------------------
#   JSON TYPE INFERENCE
# ---------------------------

def map_pyname_to_json(name: str) -> Dict[str, Any]:
    n = name.lower()
    if n in ("str", "string"):
        return {"type": "string"}
    if n in ("int", "integer"):
        return {"type": "integer"}
    if n in ("float",):
        return {"type": "number"}
    if n in ("bool", "boolean"):
        return {"type": "boolean"}
    if n in ("dict", "mapping", "object"):
        return {"type": "object"}
    if n in ("list", "sequence", "array"):
        return {"type": "array", "items": {"type": "string"}}

    return {"type": "string", "guessed": True}


def ann_to_json_type(node: Optional[ast.AST]) -> Dict[str, Any]:
    """Map Python type hints to JSON-schema-like types."""
    if node is None:
        return {"type": "string", "guessed": True}

    if isinstance(node, ast.Name):
        return map_pyname_to_json(node.id)

    if isinstance(node, ast.Attribute):
        return map_pyname_to_json(node.attr)

    if isinstance(node, ast.Subscript):
        base = node.value
        if isinstance(base, ast.Name):
            n = base.id.lower()
            if n in ("list", "typing.list"):
                return {"type": "array", "items": ann_to_json_type(node.slice)}
            if n in ("dict", "typing.dict"):
                return {"type": "object", "additionalProperties": ann_to_json_type(node.slice)}

    return {"type": "string", "guessed": True}


# ---------------------------
#   FUNCTION SCHEMA INFERENCE
# ---------------------------

def infer_schemas_from_function(func: ast.FunctionDef) -> Dict[str, Any]:
    props = {}
    required = []

    arg_list = [a for a in func.args.args if a.arg not in ("self", "cls")]

    defaults = func.args.defaults
    num_defaults = len(defaults)
    non_default_count = len(arg_list) - num_defaults

    for i, arg in enumerate(arg_list):
        name = arg.arg
        ann = arg.annotation

        schema = ann_to_json_type(ann) if ann else {"type": "string", "guessed": True}
        props[name] = schema

        if i < non_default_count:
            required.append(name)

    input_schema = {"type": "object", "properties": props}
    if required:
        input_schema["required"] = required

    # OUTPUT SCHEMA
    if func.returns:
        out_schema = ann_to_json_type(func.returns)
        if out_schema.get("type") != "object":
            out_schema = {"type": out_schema["type"]}
    else:
        out_schema = {"type": "object", "guessed": True}

    return {"input_schema": input_schema, "output_schema": out_schema}


# ---------------------------
#   FILE PARSER
# ---------------------------

def extract_from_python_file(path: Path) -> List[Dict[str, Any]]:
    src = path.read_text(encoding="utf8", errors="ignore")
    tree = ast.parse(src)
    results = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            schema = infer_schemas_from_function(node)

            results.append({
                "name": node.name,
                "predicted_filename": str(path),
                "description": (ast.get_docstring(node) or ""),
                "input_schema": schema["input_schema"],
                "output_schema": schema["output_schema"],
                "predicted_code_snippet": ast.get_source_segment(src, node),
                "payload_shape": {
                    "request": schema["input_schema"]["properties"],
                    "response": schema["output_schema"]
                },
                "confidence": 0.70
            })

    return results


# ---------------------------
#   TRANSPORT DETECTION
# ---------------------------

def detect_transport(repo_path: Path) -> Dict[str, Any]:
    transport = {"type": "stdio", "confidence": 0.3, "evidence": []}

    for file in repo_path.rglob("*.py"):
        code = file.read_text(errors="ignore")
        if "Flask" in code or "@app.route" in code:
            return {
                "type": "http",
                "confidence": 0.9,
                "evidence": [f"Flask usage in {file.name}"]
            }

        if "websocket" in code.lower():
            return {
                "type": "websocket",
                "confidence": 0.85,
                "evidence": [f"websocket pattern found in {file.name}"]
            }

    return transport


# ---------------------------
#   MAIN REPO ANALYZER
# ---------------------------

def analyze_repo(repo_dir: str):
    repo_path = Path(repo_dir)

    tools = []
    for file in repo_path.rglob("*.py"):
        tools.extend(extract_from_python_file(file))

    report = {
        "repo": repo_dir,
        "analysis_time": "2025-11-23",
        "transport": detect_transport(repo_path),
        "tools": tools,
        "run_template": {
            "cmd": "python server.py",
            "confidence": 0.8,
            "evidence": ["default guess, refine later"]
        }
    }

    out_path = Path("mcp_analysis_output.json")
    out_path.write_text(json.dumps(report, indent=2))

    print("\n ✔️ JSON report generated at:")
    print("   mcp_analysis_output.json\n")


# ---------------------------
#   ENTRY POINT
# ---------------------------

if __name__ == "__main__":
    repo = input("Enter path to repository folder: ").strip()
    analyze_repo(repo)
