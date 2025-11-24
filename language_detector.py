<<<<<<< HEAD
# language_detector.py
import os
from pathlib import Path
from collections import Counter
from typing import Dict

# Map file extensions to language names
EXT_TO_LANG = {
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
    ".go": "go",
    ".java": "java",
    ".rs": "rust",
}

def detect_languages(repo_path: str) -> Dict[str, int]:
    """
    Walk the repo and count files by language based on extension.
    Returns a dict like: {"python": 15, "typescript": 8}
    """
    root = Path(repo_path)
    counts: Counter = Counter()

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            lang = EXT_TO_LANG.get(ext)
            if lang:
                counts[lang] += 1

    return dict(counts)

def dominant_language(lang_counts):
    if not lang_counts:
        return "unknown"

    # Priority order
    priority = ["typescript", "javascript", "python", "go", "java", "rust"]

    # If any priority language exists, return the highest priority one
    for lang in priority:
        if lang in lang_counts:
            return lang

    # Otherwise fall back to count-based
    return max(lang_counts.items(), key=lambda kv: kv[1])[0]

if __name__ == "__main__":
    repo = input("Enter path to repository folder (or extracted ZIP): ").strip()
    counts = detect_languages(repo)
    dom = dominant_language(counts)
    print("Language counts:", counts)
    print("Dominant language:", dom)
=======
# language_detector.py
import os
from pathlib import Path
from collections import Counter
from typing import Dict

# Map file extensions to language names
EXT_TO_LANG = {
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
    ".go": "go",
    ".java": "java",
    ".rs": "rust",
}

def detect_languages(repo_path: str) -> Dict[str, int]:
    """
    Walk the repo and count files by language based on extension.
    Returns a dict like: {"python": 15, "typescript": 8}
    """
    root = Path(repo_path)
    counts: Counter = Counter()

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            lang = EXT_TO_LANG.get(ext)
            if lang:
                counts[lang] += 1

    return dict(counts)

def dominant_language(lang_counts):
    if not lang_counts:
        return "unknown"

    # Priority order
    priority = ["typescript", "javascript", "python", "go", "java", "rust"]

    # If any priority language exists, return the highest priority one
    for lang in priority:
        if lang in lang_counts:
            return lang

    # Otherwise fall back to count-based
    return max(lang_counts.items(), key=lambda kv: kv[1])[0]

if __name__ == "__main__":
    repo = input("Enter path to repository folder (or extracted ZIP): ").strip()
    counts = detect_languages(repo)
    dom = dominant_language(counts)
    print("Language counts:", counts)
    print("Dominant language:", dom)
>>>>>>> cf7ae0a987a9d04a3898ae77f6d6d3b763d6de30
