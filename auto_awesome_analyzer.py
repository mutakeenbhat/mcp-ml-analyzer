"""
auto_awesome_analyzer.py

Automatically:
1. Downloads the README of
   https://github.com/punkpeye/awesome-mcp-servers
2. Extracts ALL GitHub/GitLab repository links from the list
3. Filters REAL MCP server repos only
4. Clones each repo
5. Runs multi_lang_analyzer.py on each one
6. Saves results into outputs/<repo-name>/
"""

import os
import re
import requests
import subprocess
import tempfile
import shutil
import time

MULTI_ANALYZER = "multi_lang_analyzer.py"

AWESOME_URL = "https://raw.githubusercontent.com/punkpeye/awesome-mcp-servers/main/README.md"


# -----------------------------------------------------
# 1. Download README content
# -----------------------------------------------------
def fetch_readme():
    print("[INFO] Downloading Awesome MCP Servers README...")
    r = requests.get(AWESOME_URL, timeout=15)
    if r.status_code == 200:
        return r.text
    print("[ERROR] Could not download README. Status:", r.status_code)
    return None


# -----------------------------------------------------
# 2. Extract GitHub/GitLab URLs from markdown
# -----------------------------------------------------
def extract_repo_urls(readme_text):
    print("[INFO] Extracting repo URLs from markdown...")

    # Match GitHub or GitLab repos
    pattern = r"(https://github\.com/[A-Za-z0-9_.\-/]+|https://gitlab\.com/[A-Za-z0-9_.\-/]+)"
    urls = re.findall(pattern, readme_text)

    # Clean URLs (remove trailing parentheses or markdown chars)
    cleaned = []
    for u in urls:
        u = u.strip().rstrip(")").rstrip("]")
        cleaned.append(u)

    # Remove duplicates
    cleaned = list(set(cleaned))

    print(f"[INFO] Found {len(cleaned)} raw URLs.")
    return cleaned


# -----------------------------------------------------
# 3. Validate URL using "git ls-remote"
# -----------------------------------------------------
def is_valid_repo(url):
    try:
        subprocess.run(
            ["git", "ls-remote", url],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except:
        return False


# -----------------------------------------------------
# 4. Clone repo to temporary folder
# -----------------------------------------------------
def clone_repo(url):
    print(f"[CLONE] Cloning {url} ...")
    temp_dir = tempfile.mkdtemp(prefix="mcp_auto_")
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", url, temp_dir],
            check=True
        )
        print(f"[CLONE] Success → {temp_dir}")
        return temp_dir
    except Exception as e:
        print(f"[ERROR] Clone failed: {e}")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return None


# -----------------------------------------------------
# 5. Run multi_lang_analyzer.py on local folder
# -----------------------------------------------------
def run_analyzer(path, original_url):
    print(f"\n[ANALYZE] Running analyzer on repo: {original_url}\n")
    try:
        subprocess.run(
            ["python", MULTI_ANALYZER],
            input=(path + "\n").encode(),
            text=False,
            check=False
        )
    except Exception as e:
        print(f"[ERROR] Analyzer crashed: {e}")


# -----------------------------------------------------
# MAIN PIPELINE
# -----------------------------------------------------
def main():
    print("\n=======================================")
    print("   AUTO AWESOME MCP ANALYZER")
    print("=======================================\n")

    readme = fetch_readme()
    if not readme:
        return

    urls = extract_repo_urls(readme)
    print("[INFO] Filtering valid Git repositories...")

    valid_repos = []
    for url in urls:
        if is_valid_repo(url):
            valid_repos.append(url)
        else:
            print(f"[SKIP] Invalid or inaccessible: {url}")

    print(f"\n[INFO] VALID MCP SERVER REPOS FOUND: {len(valid_repos)}\n")

    for repo in valid_repos:
        print("--------------------------------------")
        print(f"[START] Processing repo: {repo}")
        print("--------------------------------------")

        folder = clone_repo(repo)
        if not folder:
            print("[SKIP] Skipping repo due to clone failure.\n")
            continue

        run_analyzer(folder, repo)

        print("[CLEANUP] Removing temp clone folder...\n")
        shutil.rmtree(folder, ignore_errors=True)
        time.sleep(1)

    print("\n=======================================")
    print(" ALL AWESOME-MCP REPOS ANALYZED")
    print(" Check the 'outputs/' folder")
    print("=======================================\n")


if __name__ == "__main__":
    main()
