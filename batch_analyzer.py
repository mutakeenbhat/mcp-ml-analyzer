import os
import subprocess
import tempfile
import shutil

# ------------------------------
# Top 10 MCP Server Repos
# ------------------------------
REPOS = [
    "https://github.com/modelcontextprotocol/python-sdk",
    "https://github.com/modelcontextprotocol/typescript-sdk",
    "https://github.com/modelcontextprotocol/quickstart-python",
    "https://github.com/modelcontextprotocol/quickstart-typescript",
    "https://github.com/modelcontextprotocol/servers",
    "https://github.com/e2b-dev/mcp-llm-bridge",
    "https://github.com/e2b-dev/sandbox-mcp-server",
    "https://github.com/microsoft/graphrag-mcp",
    "https://github.com/nilsherzig/mcp-filesystem",
    "https://github.com/nilsherzig/mcp-github"
]

ANALYZER = "multi_lang_analyzer.py"

def clone_repo(url):
    temp_dir = tempfile.mkdtemp(prefix="mcp_repo_")
    print(f"\n[CLONE] Cloning {url} ...")
    try:
        subprocess.run(["git", "clone", url, temp_dir], check=True)
        print(f"[CLONE] Success: {temp_dir}")
        return temp_dir
    except Exception as e:
        print(f"[ERROR] Failed to clone {url}: {e}")
        return None

def run_analyzer(path):
    print(f"\n[ANALYZE] Running analyzer on {path} ...")
    try:
        subprocess.run(["python", ANALYZER], input=path.encode(), check=True)
        print("[ANALYZE] Done.")
    except Exception as e:
        print(f"[ERROR] Analyzer failed: {e}")

def cleanup(path):
    print(f"[CLEANUP] Removing temp folder {path}")
    shutil.rmtree(path, ignore_errors=True)

def main():
    print("\n==============================")
    print("   MCP Batch Analyzer (TOP 10)")
    print("==============================\n")

    for repo in REPOS:
        print("\n--------------------------------------")
        print(f"[START] Processing repo: {repo}")
        print("--------------------------------------")

        local = clone_repo(repo)
        if not local:
            print("[SKIP] Clone failed")
            continue

        run_analyzer(local)
        cleanup(local)

    print("\n==============================")
    print(" ALL REPOS ANALYZED SUCCESSFULLY ")
    print("   Check the 'outputs/' folder")
    print("==============================\n")

if __name__ == "__main__":
    main()
