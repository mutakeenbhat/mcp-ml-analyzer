# schema_extractor_v2.py
# Improved resolver for python repos (static AST heuristics).
# Usage: python schema_extractor_v2.py
# When prompted, enter the path to the extracted repo folder (not the zip).

import os, json, re, ast
from pathlib import Path
from typing import Dict, Any, Optional

# ------- Helpers -------
def read_text_safe(p: Path) -> str:
    try:
        return p.read_text(encoding="utf8", errors="ignore")
    except Exception:
        return ""

def ann_to_simple_str(node: Optional[ast.AST]) -> str:
    """Return a readable string for an annotation node (best-effort)."""
    if node is None:
        return ""
    try:
        # ast.unparse available in Python 3.9+; fallback to manual parsing
        if hasattr(ast, "unparse"):
            return ast.unparse(node)
        else:
            # fallback: try Name and Subscript
            if isinstance(node, ast.Name):
                return node.id
            if isinstance(node, ast.Subscript):
                base = node.value.id if isinstance(node.value, ast.Name) else ""
                slice_s = ann_to_simple_str(node.slice)
                return f"{base}[{slice_s}]"
    except Exception:
        pass
    return ""

def infer_primitive_from_str(s: str) -> Dict[str,Any]:
    s = s.strip()
    s_lower = s.lower()
    if s_lower in ("str","string"):
        return {"type":"string"}
    if s_lower in ("int","integer"):
        return {"type":"integer"}
    if s_lower in ("float","number"):
        return {"type":"number"}
    if s_lower in ("bool","boolean"):
        return {"type":"boolean"}
    # list[...] detection
    m = re.match(r"list\[(.+)\]", s, flags=re.I)
    if m:
        inner = m.group(1).strip()
        inner_schema = infer_primitive_from_str(inner)
        return {"type":"array", "items": inner_schema}
    # dict[...] detection
    m2 = re.match(r"dict\[(.+?),(.+)\]", s, flags=re.I)
    if m2:
        return {"type":"object", "additionalProperties": {"type":"string", "guessed": True}}
    # fallback: custom class name
    return {"type":"object", "title": s}

# ------- Build registry (scan files for class defs & pydantic models) -------
def build_registry(repo: Path):
    registry = {
        "by_name": {},      # short name -> {path, properties, required, kind}
        "by_fullpath": {}   # file path -> ast.Module (not stored, but track)
    }
    py_files = list(repo.rglob("*.py"))
    for f in py_files:
        src = read_text_safe(f)
        try:
            tree = ast.parse(src)
        except Exception:
            continue
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                clsname = node.name
                props = {}
                required = []
                # find annotated class attributes (AnnAssign)
                for stmt in node.body:
                    if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                        aname = stmt.target.id
                        ann_str = ann_to_simple_str(stmt.annotation) if stmt.annotation else ""
                        schema = infer_primitive_from_str(ann_str)
                        props[aname] = schema
                        required.append(aname)
                # detect BaseModel inheritance (pydantic)
                bases = [ (b.id if isinstance(b, ast.Name) else (getattr(b,'attr','') or "")) for b in node.bases ]
                kind = "class"
                if "BaseModel" in bases or "pydantic.BaseModel" in bases:
                    kind = "pydantic"
                registry["by_name"].setdefault(clsname, []).append({
                    "path": str(f),
                    "properties": props,
                    "required": required,
                    "kind": kind
                })
    return registry

# ------- Resolve an annotation string to schema by consulting registry -------
def resolve_annotation_schema(ann_str: str, registry) -> Dict[str,Any]:
    ann_str = ann_str.strip()
    # handle Annotated[...] by extracting inner and field args
    if ann_str.startswith("Annotated[") and "Field(" in ann_str:
        # Annotated[inner, Field(...)]
        m = re.match(r"Annotated\[(.+?),\s*Field\((.+?)\)\s*\]", ann_str)
        if m:
            inner = m.group(1).strip()
            field_args = m.group(2)
            sch = resolve_annotation_schema(inner, registry)
            # simple numeric constraints
            mmin = re.search(r"ge\s*=\s*([0-9]+)", field_args)
            mmax = re.search(r"le\s*=\s*([0-9]+)", field_args)
            mlen = re.search(r"max_length\s*=\s*([0-9]+)", field_args)
            if mmin:
                sch["minimum"] = int(mmin.group(1))
            if mmax:
                sch["maximum"] = int(mmax.group(1))
            if mlen:
                sch["max_length"] = int(mlen.group(1))
            return sch
    # list[...] case
    m = re.match(r"list\[(.+)\]", ann_str, flags=re.I)
    if m:
        inner = m.group(1).strip()
        inner_sch = resolve_annotation_schema(inner, registry)
        return {"type":"array", "items": inner_sch}
    # simple primitive
    prim = infer_primitive_from_str(ann_str)
    if prim.get("type") != "object" or ann_str in registry["by_name"]:
        # if primitive or exact name in registry, return prim or mapped custom
        if ann_str in registry["by_name"]:
            # pick first match (conservative)
            entry = registry["by_name"][ann_str][0]
            sch = {"type":"object", "properties": entry["properties"]}
            if entry.get("required"):
                sch["required"] = entry["required"]
            return sch
        return prim
    # fallback
    return prim

# ------- Main analysis -------
def analyze(repo_path: str):
    repo = Path(repo_path)
    if not repo.exists():
        raise FileNotFoundError(repo_path)
    registry = build_registry(repo)
    # load existing report if present
    in_path = Path("mcp_analysis_output.json")
    if not in_path.exists():
        print("mcp_analysis_output.json not found in cwd. Run the prior extractor first.")
        return
    report = json.loads(in_path.read_text(encoding="utf8"))
    updated = 0
    for tool in report.get("tools", []):
        fname = tool.get("predicted_filename","")
        # map file to extracted repo file if relative names used
        if fname and not Path(fname).exists():
            # try to find by basename inside repo
            candidates = list(repo.rglob(os.path.basename(fname)))
            if candidates:
                fname = str(candidates[0])
        # open file and attempt to find function AST
        try:
            if fname and Path(fname).exists():
                src = read_text_safe(Path(fname))
                tree = ast.parse(src)
                func_node = None
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and node.name == tool.get("name"):
                        func_node = node
                        break
                if not func_node:
                    # try finding by snippet
                    snippet = tool.get("predicted_code_snippet","").strip().splitlines()[0] if tool.get("predicted_code_snippet") else ""
                    if snippet:
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                seg = ast.get_source_segment(src, node) or ""
                                if snippet in seg:
                                    func_node = node
                                    break
                if not func_node:
                    continue
                # process args
                props = tool.get("input_schema", {}).get("properties", {})
                reqs = set(tool.get("input_schema", {}).get("required", []))
                total_args = func_node.args.args
                num_defaults = len(func_node.args.defaults)
                for idx, arg in enumerate(total_args):
                    if arg.arg in ("self","cls"): continue
                    ann_str = ann_to_simple_str(arg.annotation) if arg.annotation else ""
                    if not ann_str:
                        continue
                    sch = resolve_annotation_schema(ann_str, registry)
                    props[arg.arg] = sch
                    # required if no default for that arg
                    has_default = idx >= (len(total_args) - num_defaults)
                    if not has_default:
                        reqs.add(arg.arg)
                # update report tool entry
                tool["input_schema"]["properties"] = props
                if reqs:
                    tool["input_schema"]["required"] = sorted(list(reqs))
                # attempt the return type
                ret_ann = func_node.returns
                if ret_ann:
                    ret_str = ann_to_simple_str(ret_ann)
                    ret_sch = resolve_annotation_schema(ret_str, registry)
                    tool["output_schema"] = ret_sch
                updated += 1
                # bump confidence a bit
                tool["confidence"] = min(0.95, tool.get("confidence",0.7) + 0.12)
        except Exception:
            continue
    # write output
    out_path = Path("mcp_analysis_output_v2.json")
    out_path.write_text(json.dumps(report, indent=2), encoding="utf8")
    print(f"Done. Wrote {out_path}. Tools scanned: {len(report.get('tools',[]))}. Updated entries: {updated}")

if __name__ == "__main__":
    repo = input("Enter path to repository folder (extracted, not zip): ").strip()
    analyze(repo)
