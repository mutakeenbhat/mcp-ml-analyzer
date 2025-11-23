"""
generate_readable_report.py
Auto-detects mcp_analysis_output_final.json anywhere in the project folder.
Generates mcp_final_report_readable.md.
"""

import json
from pathlib import Path

OUTPUT = Path("mcp_final_report_readable.md")

def find_final_json():
    """Search for mcp_analysis_output_final.json anywhere under the project folder."""
    project_dir = Path(".").resolve()
    candidates = list(project_dir.rglob("mcp_analysis_output_final.json"))
    if not candidates:
        raise FileNotFoundError("Could not find mcp_analysis_output_final.json anywhere in the project folder.")
    return candidates[0]

def indent_block(text, level=4):
    pad = " " * level
    return "\n".join(pad + line for line in text.splitlines())

def write_header(fp, title, level=1):
    fp.write(f"{'#' * level} {title}\n\n")

def generate_report():
    json_path = find_final_json()
    print(f"Found MCP final JSON at: {json_path}")

    data = json.loads(json_path.read_text(encoding="utf-8"))

    with OUTPUT.open("w", encoding="utf-8") as fp:
        write_header(fp, "MCP Repository Analyzer — Final Report")

        # Transport
        write_header(fp, "Transport Inference", 2)
        transport = data.get("transport", {})
        fp.write(f"- **Type:** {transport.get('type')}\n")
        fp.write(f"- **Confidence:** {transport.get('confidence')}\n\n")

        # Tools
        tools = data.get("tools", [])
        write_header(fp, f"Tools Overview ({len(tools)} tools)", 2)

        for t in tools:
            name = t.get("name", "unknown")
            fp.write(f"### 🛠️ Tool: **{name}**\n")
            fp.write(f"- **File:** `{t.get('predicted_filename', '?')}`\n")
            fp.write(f"- **Confidence:** {t.get('confidence')}\n\n")

            # Input Schema
            fp.write("#### Input Schema\n")
            fp.write("```json\n")
            fp.write(json.dumps(t.get("input_schema", {}), indent=2))
            fp.write("\n```\n\n")

            # Output Schema
            fp.write("#### Output Schema\n")
            fp.write("```json\n")
            fp.write(json.dumps(t.get("output_schema", {}), indent=2))
            fp.write("\n```\n\n")

            # Payload
            fp.write("#### Payload Shape\n")
            fp.write("```json\n")
            fp.write(json.dumps(t.get("payload_shape", {}), indent=2))
            fp.write("\n```\n\n")

            # Syscalls
            sc = t.get("syscalls", {})
            fp.write("#### Syscalls\n")
            fp.write(f"- Filesystem: {sc.get('filesystem',[])}\n")
            fp.write(f"- Network: {sc.get('network',[])}\n")
            fp.write(f"- Subprocess: {sc.get('subprocess',[])}\n")
            fp.write(f"- Env: {sc.get('env',[])}\n")
            fp.write(f"- Severity: **{sc.get('severity')}**\n\n")

            # Run Template
            fp.write("#### Run Template\n")
            fp.write("```json\n")
            fp.write(json.dumps(t.get("run_template", {}), indent=2))
            fp.write("\n```\n\n")

            # Evidence summary
            fp.write("#### Evidence Summary (Short)\n")
            ev = t.get("evidence", [])
            for e in ev[:3]:
                fp.write(f"- {e.get('type')} — `{e.get('file','')}`\n")
            if len(ev) > 3:
                fp.write(f"- (+{len(ev)-3} more entries)\n")
            fp.write("\n---\n\n")

        # Evidence pack metadata
        write_header(fp, "Evidence Pack (Metadata)", 2)
        fp.write("```json\n")
        fp.write(json.dumps(data.get("evidence_pack", {}), indent=2))
        fp.write("\n```\n\n")

    print(f"Report generated: {OUTPUT}")

if __name__ == "__main__":
    generate_report()
