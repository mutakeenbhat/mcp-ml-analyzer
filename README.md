📘 MCP Repository Analyzer – Final Submission (README.md)

A Multi-Language, ML-Enhanced, Git-Powered MCP Server Analysis Tool
Author: Mutakeen

🚀 Overview

This project is my implementation of a Multi-Language MCP Repository Analyzer, built to read:

GitHub/GitLab URLs

ZIP files

Local folders

…and automatically detect Model Context Protocol (MCP) characteristics.

The analyzer scans entire repositories across different programming languages and outputs a complete MCP JSON report containing:

Transport type

Tools and descriptions

Input & output schemas

Payload shapes

Code snippets

System calls

Run templates

Confidence scores

The design originally only supported ZIP files, but I extended it into a full Git repository analyzer, capable of scanning large curated collections like the Awesome MCP Servers list automatically.

🧠 Motivation

The assignment required building an ML-driven system that:

✔ Reads entire codebases
✔ Supports multiple languages
✔ Works on Git repositories
✔ Produces a single structured JSON output
✔ Extracts MCP features fully
✔ Uses ML to improve predictions
✔ Handles hundreds of repositories in batch mode

My initial solution only worked with ZIP files, which required manually downloading each repository. To solve this, I upgraded the system to:

Support repository URLs

Auto-clone Git repos

Handle hundreds of repos in bulk

Create isolated output folders

Detect languages dynamically

Switch extractors automatically

This made the analyzer scalable, flexible, and entirely automated.

🏗️ Architecture
┌──────────────────────────────┐
│ multi_lang_analyzer.py       │  ← Main unified entry-point
└───────────────┬──────────────┘
                │
     ┌──────────┼─────────────┬───────────────────────────┐
     │          │             │                           │
┌────▼─┐   ┌────▼────┐   ┌────▼────┐                ┌─────▼──────┐
│Python│   │TS / JS  │   │Rust     │                │Go / Java    │
│Extractor││Extractor│   │Extractor│                │Extractors   │
└────┬────┘└────┬─────┘   └────┬────┘                └─────┬──────┘
     │          │             │                            │
     └──────────┴─────────────┴────────────────────────────┘
                       │
                       ▼
                Static Analysis
     (tools, schemas, payloads, syscalls, run template)
                       │
                       ▼
                 ML Refinement Layer (optional)
                       │
                       ▼
            /outputs/<repo_name>/mcp_analysis_output_final.json

🌐 Supported Inputs
✔ GitHub / GitLab URL

Example:

python multi_lang_analyzer.py
https://github.com/modelcontextprotocol/python-sdk

✔ ZIP Files

Example:

python multi_lang_analyzer.py
C:\path\to\repo.zip

✔ Local Folders

Example:

python multi_lang_analyzer.py
C:\project\mcp-server

🧩 Multi-Language Support

The analyzer dynamically detects languages using file inspection.

Supported languages:

Language	                         Extractor
Python	                       schema_extractor_v3.py
TypeScript / JavaScript	      ts_js_extractor.py
Rust	                           rust_extractor.py
Go                               	go_extractor.py
Java                            	java_extractor.py

Each extractor identifies:

MCP tools

Code patterns

Function signatures

Input/output schemas

Payload shapes

System calls

Run commands

Transport hints

🤖 ML Refinement (Optional)

To improve predictions, I built a lightweight ML refinement layer:

Refines schema fields

Enhances descriptions

Infers missing details

Improves confidence scoring

This step is optional and automatically skipped on low-RAM systems.

⚙️ Batch Analyzer: Auto-Awesome MCP Scanner

One major enhancement I built is the automatic scanner for the Awesome MCP Servers list.

Using:

python auto_awesome_analyzer.py


The system:

Downloads the Awesome MCP markdown list

Extracts GitHub URLs

Validates repositories

Authenticates using GitHub PAT

Clones valid repos

Analyzes each repo

Saves each result into its own folder

Generates:

outputs/
    repo_1/
    repo_2/
    repo_3/


This satisfies the assignment requirement of testing the analyzer on a large ecosystem of repos.

📁 Output Format

Each analyzed repository generates a folder:

outputs/<repo-name>/
     mcp_analysis_output_final.json
     mcp_final_report_readable.md
     syscall_report.json


The main JSON file contains:

Transport prediction

Tools (name, description)

Schema objects

Request/response shape

System calls detected

Run template

Confidence scores

▶️ How to Use
1️⃣ Run main analyzer
python multi_lang_analyzer.py


Input can be ZIP / URL / folder.

2️⃣ Run auto batch (Awesome MCP)
python auto_awesome_analyzer.py

3️⃣ Run ML refiner (optional)
python ml_refiner.py

📦 Folder Structure
code/
    multi_lang_analyzer.py
    auto_awesome_analyzer.py
    batch_analyzer.py
    schema_extractor_v3.py
    ts_js_extractor.py
    rust_extractor.py
    go_extractor.py
    java_extractor.py
    language_detector.py
    sync_payload_schemas.py
    syscall_scanner_v4.py
    generate_readable_report.py
    ml_refiner.py

outputs/
    <repo-name>/
        mcp_analysis_output_final.json
        syscall_report.json
        mcp_final_report_readable.md

report/
    Final_MCP_Analyzer_Report.pdf

🎯 Key Improvements I Made

Here is a summary of all enhancements I implemented:

✔ Originally ZIP-only → Now supports Git URLs
✔ Added multi-language support
✔ Added full repo auto-cloning
✔ Added language detection
✔ Added batch analyzer
✔ Added auto-awesome analyzer
✔ Generates separate folders per repo
✔ Added syscall scanning
✔ Added schema syncing
✔ Added ML refinement
✔ Created final PDF report
✔ Cleaned repo & created README

This transformed the project into a complete, production-ready MCP analyzer.

🛠️ Requirements
Python 3.10+
pip install -r requirements.txt


Important:
Do NOT commit .venv/ or outputs/ to Git.

💡 Future Enhancements

Add more ML refinement models

Add streaming analysis

Add Type inference engine for JS/TS

Add UI dashboard for browsing results
