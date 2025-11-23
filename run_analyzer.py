import sys
from analyzer import analyze_repo

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_analyzer.py <repo_zip>")
        exit()

    analyze_repo(sys.argv[1])
