import os
import json
import zipfile
from ml_inference import MCPMLModels

ml = MCPMLModels()

# ------------------------------------------------------------
# Utility
# ------------------------------------------------------------

def read_all_texts(repo_path):
    combined = ""
    file_map = {}

    for root, dirs, files in os.walk(repo_path):
        for f in files:
            if f.endswith((".py", ".js", ".ts", ".json")):
                path = os.path.join(root, f)
                try:
                    txt = open(path, "r", encoding="utf-8", errors="ignore").read()
                    file_map[path] = txt
                    combined += txt + "\n"
                except:
                    pass

    return combined, file_map


def extract_zip(zip_path):
    repo_name = os.path.splitext(os.path.basename(zip_path))[0]
    extract_root = os.path.join("repos", repo_name)

    os.makedirs("repos", exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_root)

    items = os.listdir(extract_root)
    if len(items) == 1:
        nested = os.path.join(extract_root, items[0])
        if os.path.isdir(nested):
            return repo_name, nested

    return repo_name, extract_root

# ------------------------------------------------------------
# MCP Transport (ML + Rules Hybrid)
# ------------------------------------------------------------

def detect_transport(text):
    ml_pred = ml.predict_transport(text)

    evidence = [f"ML classifier predicted: {ml_pred}"]

    # hybrid boosting
    rules = {
        "stdio": ["sys.stdin", "sys.stdout", "input(", "process.stdin"],
        "http": [".get(", ".post(", "fetch(", "axios", "flask", "router."],
        "websocket": ["WebSocket(", "ws.on", "socket.on", "send("],
        "sse": ["text/event-stream", "EventSource", "res.write('data", "stream.write("]
    }

    for ttype, patterns in rules.items():
        for p in patterns:
            if p in text:
                evidence.append(f"Rule match: '{p}' → {ttype}")
                if ttype != ml_pred:  
                    ml_pred = ttype  

    return {
        "type": ml_pred,
        "confidence": 0.85,
        "evidence": evidence
    }

# ------------------------------------------------------------
# MCP Tools Detector (ML + pattern matching)
# ------------------------------------------------------------

def detect_tools(file_map, repo_path):
    results = []

    patterns = ["class", "tool", "@tool", "execute_tool", "ToolResponse"]

    for path, txt in file_map.items():
        ml_label = ml.predict_tool(txt)

        evidence = []
        if ml_label == "is_tool":
            evidence.append("ML classified: is_tool")

        for p in patterns:
            if p in txt:
                evidence.append(f"Rule matched: {p}")

        if evidence:
            results.append({
                "file": os.path.relpath(path, repo_path),
                "confidence": 0.80,
                "evidence": evidence
            })

    return results

# ------------------------------------------------------------
# MCP Schema detector
# ------------------------------------------------------------

def detect_schemas(file_map, repo_path):
    results = []

    for path, txt in file_map.items():
        if not path.endswith(".json"):
            continue

        label = ml.predict_schema(txt)
        if label == "schema":
            results.append({
                "file": os.path.relpath(path, repo_path),
                "confidence": 0.90,
                "evidence": ["ML schema classifier predicted: schema"]
            })

    return results

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def analyze_repo(zip_path):
    repo_name, repo_path = extract_zip(zip_path)

    combined_text, file_map = read_all_texts(repo_path)

    transport = detect_transport(combined_text)
    tools = detect_tools(file_map, repo_path)
    schemas = detect_schemas(file_map, repo_path)

    final_report = {
        "repository": repo_name,
        "file_count": len(file_map),
        "transport": transport,
        "tools": tools,
        "schemas": schemas
    }

    os.makedirs("outputs", exist_ok=True)
    out = f"outputs/{repo_name}_mcp_ml_report.json"

    with open(out, "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=4)

    print("\n🎉 Report saved to:", out)
    return final_report
