r"""
schema_extractor_v3.py

Usage:
    python schema_extractor_v3.py
"""


import os
import json
import re
import ast
from pathlib import Path
from typing import Dict, Any, Optional, List


INPUT_JSON = Path("mcp_analysis_output_synced.json")
OUTPUT_JSON = Path("mcp_analysis_output_classes_resolved.json")


# ---------- basic helpers ----------

def read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def ann_to_str(node: Optional[ast.AST]) -> str:
    """Convert an annotation AST node into a readable string."""
    if node is None:
        return ""
    try:
        if hasattr(ast, "unparse"):
            return ast.unparse(node)
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        if isinstance(node, ast.Subscript):
            base = ann_to_str(node.value)
            inner = ann_to_str(node.slice)
            return f"{base}[{inner}]"
    except Exception:
        pass
    return ""


def primitive_from_str(s: str) -> Dict[str, Any]:
    """Map simple type strings to primitive JSON-schema types."""
    s = s.strip()
    low = s.lower()
    if low in ("str", "string"):
        return {"type": "string"}
    if low in ("int", "integer"):
        return {"type": "integer"}
    if low in ("float", "number"):
        return {"type": "number"}
    if low in ("bool", "boolean"):
        return {"type": "boolean"}

    # list[...] pattern
    m_list = re.match(r"(?:list|List)\[(.+)\]", s)
    if m_list:
        inner = m_list.group(1).strip()
        inner_schema = primitive_from_str(inner)
        return {"type": "array", "items": inner_schema}

    # dict[...] pattern -> generic object
    m_dict = re.match(r"(?:dict|Dict)\[(.+)\]", s)
    if m_dict:
        return {"type": "object", "additionalProperties": {"type": "string", "guessed": True}}

    # default: custom type
    return {"type": "object", "title": s}


# ---------- registry builder ----------

def build_class_registry(repo: Path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Scan all .py files and build a registry:

    registry[name] = [
        {
            "path": file path,
            "kind": "class" | "pydantic",
            "properties": {field: schema},
            "required": [fields]
        },
        ...
    ]
    """
    registry: Dict[str, List[Dict[str, Any]]] = {}

    py_files = list(repo.rglob("*.py"))
    for f in py_files:
        src = read_text_safe(f)
        if not src:
            continue
        try:
            tree = ast.parse(src)
        except Exception:
            continue

        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue

            cls_name = node.name

            # detect kind (pydantic BaseModel vs normal)
            bases = []
            for b in node.bases:
                if isinstance(b, ast.Name):
                    bases.append(b.id)
                elif isinstance(b, ast.Attribute):
                    bases.append(b.attr)
            kind = "class"
            if "BaseModel" in bases or "pydantic.BaseModel" in bases:
                kind = "pydantic"

            props: Dict[str, Any] = {}
            required: List[str] = []

            # collect annotated attributes
            for stmt in node.body:
                if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                    field_name = stmt.target.id
                    ann_str = ann_to_str(stmt.annotation)
                    schema = primitive_from_str(ann_str)
                    props[field_name] = schema
                    # simple rule: if no default -> required
                    has_default = stmt.value is not None
                    if not has_default:
                        required.append(field_name)

            if props:
                registry.setdefault(cls_name, []).append(
                    {
                        "path": str(f),
                        "kind": kind,
                        "properties": props,
                        "required": required,
                    }
                )

    return registry


# ---------- schema resolvers ----------

def resolve_literal_title(title: str) -> Optional[Dict[str, Any]]:
    """
    Handle titles like "Literal['image']" or "Literal['user', 'assistant']".
    """
    if not title.startswith("Literal"):
        return None

    # Extract things inside Literal[...]
    m = re.match(r"Literal\[(.+)\]", title)
    if not m:
        return None

    inner = m.group(1)
    # find '...' or "..."
    values = re.findall(r"'([^']*)'|\"([^\"]*)\"", inner)
    enums: List[str] = []
    for a, b in values:
        if a:
            enums.append(a)
        elif b:
            enums.append(b)

    if not enums:
        return None

    return {"type": "string", "enum": enums}


def resolve_union_title(title: str, registry: Dict[str, List[Dict[str, Any]]]) -> Optional[Dict[str, Any]]:
    """
    Handle titles like "TextResourceContents | BlobResourceContents".
    We build a oneOf if we can resolve the components.
    """
    if "|" not in title:
        return None

    parts = [p.strip() for p in title.split("|")]
    one_of: List[Dict[str, Any]] = []
    for p in parts:
        if not p:
            continue
        entries = registry.get(p)
        if not entries:
            # unknown type; bail out if nothing resolved
            continue
        entry = entries[0]
        schema: Dict[str, Any] = {
            "type": "object",
            "properties": entry.get("properties", {}),
        }
        if entry.get("required"):
            schema["required"] = entry["required"]
        one_of.append(schema)

    if not one_of:
        return None

    return {"oneOf": one_of}


def expand_class_title(title: str, registry: Dict[str, List[Dict[str, Any]]]) -> Optional[Dict[str, Any]]:
    """
    Try to expand a single class name like "WeatherData" into full schema.
    """
    entries = registry.get(title)
    if not entries:
        return None

    entry = entries[0]  # pick first match
    schema: Dict[str, Any] = {
        "type": "object",
        "properties": entry.get("properties", {}),
    }
    if entry.get("required"):
        schema["required"] = entry["required"]
    return schema


def refine_schema(schema: Any, registry: Dict[str, List[Dict[str, Any]]]) -> Any:
    """
    Recursively refine a schema object by resolving titles, Literals, unions, etc.
    """
    if not isinstance(schema, dict):
        return schema

    # Handle Literal[...] titles
    title = schema.get("title")
    if isinstance(title, str):
        lit = resolve_literal_title(title)
        if lit is not None:
            return lit

        union = resolve_union_title(title, registry)
        if union is not None:
            # keep type "object" and add oneOf, or just return union
            return union

        # Plain class title => expand if we know it
        expanded = expand_class_title(title, registry)
        if expanded is not None:
            # If existing schema has additional stuff, we could merge.
            # For now we just return expanded.
            return expanded

    # If this is an array, refine items
    if schema.get("type") == "array" and "items" in schema:
        schema["items"] = refine_schema(schema["items"], registry)
        return schema

    # If this is an object with properties, refine each property
    if schema.get("type") == "object":
        props = schema.get("properties")
        if isinstance(props, dict):
            for key, val in list(props.items()):
                props[key] = refine_schema(val, registry)
        # additionalProperties might also hold nested types
        if "additionalProperties" in schema:
            schema["additionalProperties"] = refine_schema(schema["additionalProperties"], registry)
        return schema

    return schema


# ---------- main processing ----------

def process_report(repo_path: str):
    repo = Path(repo_path)
    if not repo.exists():
        raise FileNotFoundError(f"Repo path does not exist: {repo_path}")

    if not INPUT_JSON.exists():
        raise FileNotFoundError(f"{INPUT_JSON} not found. Make sure this file is in the current folder.")

    print(f"Building class & Pydantic registry from repo: {repo}")
    registry = build_class_registry(repo)
    print(f"  Classes found: {len(registry)}")

    report = json.loads(INPUT_JSON.read_text(encoding="utf-8"))

    tools = report.get("tools", [])
    improved = 0

    for tool in tools:
        # refine input_schema
        if "input_schema" in tool:
            tool["input_schema"] = refine_schema(tool["input_schema"], registry)

        # refine output_schema
        if "output_schema" in tool:
            tool["output_schema"] = refine_schema(tool["output_schema"], registry)

        # refine payload_shape to stay in sync
        payload = tool.get("payload_shape", {})
        if "request" in payload and "input_schema" in tool:
            request_props = tool["input_schema"].get("properties", {})
            payload["request"] = request_props
        if "response" in payload and "output_schema" in tool:
            payload["response"] = tool["output_schema"]
        tool["payload_shape"] = payload

        improved += 1
        # bump confidence a bit
        conf = tool.get("confidence", 0.7)
        tool["confidence"] = float(min(0.98, conf + 0.04))

    OUTPUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Done. Tools processed: {improved}")
    print(f"Output written to: {OUTPUT_JSON}")


if __name__ == "__main__":
    repo = input("Enter path to repository folder (extracted python-sdk, not the zip): ").strip()
    process_report(repo)
