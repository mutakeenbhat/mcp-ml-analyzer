import ast
import json
from pathlib import Path
from typing import Dict, Any, List

# Input + output JSON paths (same folder as this script)
INPUT_JSON = Path("mcp_analysis_output_classes_resolved.json")
OUTPUT_JSON = Path("mcp_analysis_output_with_syscalls.json")
SYSCALL_SUMMARY_JSON = Path("syscall_report.json")


# ------------- AST-based syscall scanner -------------

class SyscallVisitor(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.filesystem: List[str] = []
        self.network: List[str] = []
        self.subprocess: List[str] = []
        self.env: List[str] = []
        self.other: List[str] = []

    def _add(self, category: str, detail: str):
        lst = getattr(self, category)
        if detail not in lst:
            lst.append(detail)

    def visit_Call(self, node: ast.Call):
        # Function name as string, if we can get it
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            # like module.func or obj.method
            attr_parts = []
            cur = node.func
            while isinstance(cur, ast.Attribute):
                attr_parts.append(cur.attr)
                cur = cur.value
            if isinstance(cur, ast.Name):
                attr_parts.append(cur.id)
            func_name = ".".join(reversed(attr_parts))  # e.g. os.path.join or httpx.post

        fname_lower = func_name.lower()

        # --- filesystem patterns ---
        fs_funcs = {
            "open",
            "pathlib.path.open",
            "pathlib.path.read_text",
            "pathlib.path.write_text",
            "os.remove",
            "os.unlink",
            "os.mkdir",
            "os.makedirs",
            "os.rmdir",
            "shutil.copy",
            "shutil.move",
            "shutil.rmtree",
        }
        if any(fname_lower == f or fname_lower.endswith("." + f.split(".")[-1]) for f in fs_funcs):
            self._add("filesystem", func_name)

        # --- network patterns ---
        net_keywords = ["requests.", "httpx.", "aiohttp.", "socket.", "websockets.", "urllib."]
        if any(k in fname_lower for k in net_keywords):
            self._add("network", func_name)

        # Also crude: if function name is "get", "post", "put", "delete" and module looks HTTP-ish
        if isinstance(node.func, ast.Attribute):
            base = node.func.value
            if isinstance(base, ast.Name):
                base_name = base.id.lower()
                if base_name in ("client", "session", "http", "httpclient"):
                    if node.func.attr.lower() in ("get", "post", "put", "delete", "request"):
                        self._add("network", f"{base_name}.{node.func.attr}")

        # --- subprocess / shell ---
        if fname_lower.startswith("subprocess."):
            self._add("subprocess", func_name)
        if fname_lower in ("os.system", "os.popen"):
            self._add("subprocess", func_name)

        # --- environment variables ---
        if fname_lower in ("os.getenv",):
            self._add("env", func_name)

        # Check for environ[...] usage: os.environ["KEY"]
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "environ":
                self._add("env", "environ access")

        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript):
        # Detect os.environ["KEY"]
        target = node.value
        if isinstance(target, ast.Attribute):
            if (
                isinstance(target.value, ast.Name)
                and target.value.id == "os"
                and target.attr == "environ"
            ):
                self._add("env", "os.environ[...]")
        self.generic_visit(node)


def scan_file(path: Path) -> Dict[str, Any]:
    src = path.read_text(encoding="utf-8", errors="ignore")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {}
    visitor = SyscallVisitor(str(path))
    visitor.visit(tree)
    return {
        "filesystem": visitor.filesystem,
        "network": visitor.network,
        "subprocess": visitor.subprocess,
        "env": visitor.env,
        "other": visitor.other,
    }


# ------------- Main integration logic -------------

def build_syscall_index(repo_path: Path) -> Dict[str, Dict[str, Any]]:
    """
    Return a mapping: file_path -> {filesystem: [...], network: [...], subprocess: [...], env: [...], other: [...]}
    """
    index: Dict[str, Dict[str, Any]] = {}
    py_files = list(repo_path.rglob("*.py"))
    for f in py_files:
        result = scan_file(f)
        if any(result.values()):
            index[str(f)] = result
    return index


def severity_from_syscalls(info: Dict[str, List[str]]) -> str:
    """
    Simple heuristic severity rating.
    """
    if info["subprocess"]:
        return "high"
    if info["network"] and info["filesystem"]:
        return "medium-high"
    if info["network"] or info["filesystem"] or info["env"]:
        return "medium"
    return "low"


def main():
    # Ask user for repo path
    repo_input = input("Enter path to repository folder (python-sdk): ").strip()
    repo_path = Path(repo_input)
    if not repo_path.exists():
        raise FileNotFoundError(f"Repo path does not exist: {repo_path}")

    if not INPUT_JSON.exists():
        raise FileNotFoundError(f"{INPUT_JSON} not found in current folder.")

    print(f"Scanning repo for syscalls: {repo_path}")
    syscall_index = build_syscall_index(repo_path)
    print(f"Python files with syscalls found: {len(syscall_index)}")

    # Load existing MCP report
    report = json.loads(INPUT_JSON.read_text(encoding="utf-8"))
    tools = report.get("tools", [])

    # Attach syscall info to tools based on predicted_filename
    for tool in tools:
        fname = tool.get("predicted_filename", "")
        sysinfo: Dict[str, Any] = {
            "filesystem": [],
            "network": [],
            "subprocess": [],
            "env": [],
            "severity": "low",
        }
        if fname:
            # exact match first
            if fname in syscall_index:
                info = syscall_index[fname]
            else:
                # try basename match
                matches = [
                    v for k, v in syscall_index.items()
                    if Path(k).name == Path(fname).name
                ]
                info = matches[0] if matches else None
            if info:
                sysinfo["filesystem"] = info["filesystem"]
                sysinfo["network"] = info["network"]
                sysinfo["subprocess"] = info["subprocess"]
                sysinfo["env"] = info["env"]
                sysinfo["severity"] = severity_from_syscalls(info)
        tool["syscalls"] = sysinfo

    # Save extended MCP report
    OUTPUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Updated MCP report with syscalls written to: {OUTPUT_JSON}")

    # Also write a standalone syscall summary for all files
    summary = []
    for path_str, info in syscall_index.items():
        summary.append(
            {
                "file": path_str,
                "filesystem": info["filesystem"],
                "network": info["network"],
                "subprocess": info["subprocess"],
                "env": info["env"],
                "severity": severity_from_syscalls(info),
            }
        )
    SYSCALL_SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Standalone syscall summary written to: {SYSCALL_SUMMARY_JSON}")


if __name__ == "__main__":
    main()
