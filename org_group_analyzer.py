"""
org_group_analyzer.py

High-level wrapper around multi_lang_analyzer.py

- If user gives a single repo URL (GitHub or GitLab) → analyze that one repo.
- If user gives a GitHub org URL → fetch all repos via GitHub API and analyze each.
- If user gives a GitLab group URL → fetch all projects via GitLab API and analyze each.
- If user gives a ZIP or local folder → just analyze once.

This script does NOT hard-code any URLs.
"""

import os
import sys
import subprocess
import tempfile
import shutil
import time
from urllib.parse import urlparse, quote
import requests

MULTI_ANALYZER = "multi_lang_analyzer.py"

# Optional: tokens for private / big orgs (set these in your environment if needed)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)
GITLAB_TOKEN = os.environ.get("GITLAB_TOKEN", None)


# -------------------------------------------------------
# 1. Helpers to detect what kind of URL we have
# -------------------------------------------------------
def classify_url(url: str):
    """
    Returns one of:
      ("github", "org", <org_name>)
      ("github", "repo", <full_repo_url>)
      ("gitlab", "group", <group_path>)
      ("gitlab", "repo", <full_repo_url>)
      ("other", "url", <url>)
    """
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path_parts = [p for p in parsed.path.strip("/").split("/") if p]

    # GitHub
    if "github.com" in host:
        if len(path_parts) == 1:
            # https://github.com/org
            return ("github", "org", path_parts[0])
        elif len(path_parts) >= 2:
            # https://github.com/org/repo or deeper
            return ("github", "repo", url)

    # GitLab
    if "gitlab.com" in host:
        # Very simple heuristic:
        #  - 1 path segment → treat as group
        #  - >=2 segments → treat as repo
        if len(path_parts) == 1:
            # https://gitlab.com/group
            group_path = path_parts[0]
            return ("gitlab", "group", group_path)
        elif len(path_parts) >= 2:
            # https://gitlab.com/group/project (or nested)
            return ("gitlab", "repo", url)

    return ("other", "url", url)


# -------------------------------------------------------
# 2. Query GitHub API for org repos
# -------------------------------------------------------
def fetch_github_org_repos(org_name: str):
    """
    Returns a list of repo HTML URLs for the given GitHub org.
    Only public repos if no token is provided.
    """
    print(f"[INFO] Fetching repos for GitHub org: {org_name}")
    api_url = f"https://api.github.com/orgs/{org_name}/repos?per_page=50"

    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    try:
        resp = requests.get(api_url, headers=headers, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        urls = [repo["html_url"] for repo in data]
        print(f"[INFO] Found {len(urls)} repos in GitHub org '{org_name}'.")
        return urls
    except Exception as e:
        print("[ERROR] Failed to fetch GitHub org repos:", e)
        return []


# -------------------------------------------------------
# 3. Query GitLab API for group projects
# -------------------------------------------------------
def fetch_gitlab_group_repos(group_path: str):
    """
    Returns a list of repo URLs for a GitLab group.
    group_path is like 'mygroup' or 'mygroup/subgroup'
    """
    print(f"[INFO] Fetching projects for GitLab group: {group_path}")

    # GitLab expects full path url-encoded (slashes encoded as %2F)
    encoded_group = quote(group_path, safe="")
    api_url = f"https://gitlab.com/api/v4/groups/{encoded_group}/projects?per_page=50"

    headers = {}
    if GITLAB_TOKEN:
        headers["PRIVATE-TOKEN"] = GITLAB_TOKEN

    try:
        resp = requests.get(api_url, headers=headers, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        # Use web_url or http_url_to_repo; both are cloneable usually
        urls = [proj.get("http_url_to_repo") or proj.get("web_url") for proj in data]
        urls = [u for u in urls if u]  # filter None
        print(f"[INFO] Found {len(urls)} repos in GitLab group '{group_path}'.")
        return urls
    except Exception as e:
        print("[ERROR] Failed to fetch GitLab group projects:", e)
        return []


# -------------------------------------------------------
# 4. Run the existing multi_lang_analyzer.py
# -------------------------------------------------------
def run_single_analysis(input_value: str):
    """
    Calls multi_lang_analyzer.py and passes input_value (URL/zip/folder)
    into its stdin (because it uses input()).
    """
    print(f"\n[ANALYZE] Starting analysis for: {input_value}\n")
    try:
        # Note: we pass the input via stdin; multi_lang_analyzer uses input() to read it
        proc = subprocess.run(
            ["python", MULTI_ANALYZER],
            input=(input_value + "\n").encode(),
            text=False,
            check=False
        )
        if proc.returncode == 0:
            print(f"[ANALYZE] Finished: {input_value}\n")
        else:
            print(f"[WARN] Analyzer exited with code {proc.returncode} for: {input_value}\n")
    except Exception as e:
        print(f"[ERROR] Analyzer crashed on {input_value}: {e}\n")


# -------------------------------------------------------
# 5. Main logic
# -------------------------------------------------------
def main():
    user_input = input("Enter GitHub/GitLab ORG/GROUP URL, single repo URL, ZIP, or local folder: ").strip()

    # Non-URL case → treat it as zip or folder and just analyze once
    if not user_input.startswith("http://") and not user_input.startswith("https://"):
        print("[INFO] Treating input as ZIP or local folder.")
        run_single_analysis(user_input)
        return

    # URL case → classify
    kind, subtype, value = classify_url(user_input)
    print(f"[DEBUG] Classified as: kind={kind}, subtype={subtype}, value={value}")

    # -------------------------
    # GitHub org → many repos
    # -------------------------
    if kind == "github" and subtype == "org":
        repos = fetch_github_org_repos(value)
        if not repos:
            print("[WARN] No repos found or API call failed.")
            return

        for repo_url in repos:
            run_single_analysis(repo_url)
            time.sleep(1)

    # -------------------------
    # GitHub single repo
    # -------------------------
    elif kind == "github" and subtype == "repo":
        run_single_analysis(value)

    # -------------------------
    # GitLab group → many repos
    # -------------------------
    elif kind == "gitlab" and subtype == "group":
        repos = fetch_gitlab_group_repos(value)
        if not repos:
            print("[WARN] No repos found or API call failed.")
            return

        for repo_url in repos:
            run_single_analysis(repo_url)
            time.sleep(1)

    # -------------------------
    # GitLab single repo
    # -------------------------
    elif kind == "gitlab" and subtype == "repo":
        run_single_analysis(value)

    # Other URLs → just pass directly
    else:
        print("[INFO] Unrecognized URL type; passing directly to analyzer once.")
        run_single_analysis(user_input)


if __name__ == "__main__":
    main()
