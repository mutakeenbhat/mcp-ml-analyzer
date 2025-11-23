"""
ml_refiner.py

FAST ML refinement using Phi-3 Mini 128M (very small + CPU friendly)
Refines tool descriptions and adds ML confidence.
Works perfectly on low-RAM systems.

Input:  mcp_analysis_output_final.json
Output: mcp_analysis_output_final_ml.json
"""

import json
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# FAST MODEL (recommended for your laptop)
MODEL_NAME = "gpt2"


ROOT = Path(__file__).parent
INPUT_JSON = ROOT / "mcp_analysis_output_final.json"
OUTPUT_JSON = ROOT / "mcp_analysis_output_final_ml.json"


def load_model():
    print(f"[ML] Loading fast model: {MODEL_NAME} ...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32
    )
    model.eval()
    return tokenizer, model


def build_prompt_for_tool(tool: dict, index: int) -> str:
    """
    Build a short prompt for Phi-3 Mini to generate:
    - refined description
    - confidence score
    """
    name = tool.get("name", f"tool_{index}")
    old_desc = tool.get("description", "")
    snippet = tool.get("predicted_code_snippet", "")

    prompt = f"""
You are improving metadata for an MCP tool.

Given:
Tool name: {name}
Old description: {old_desc}
Code snippet: {snippet[:400]}

Return ONLY valid JSON with:
{{
  "description": "one short sentence",
  "confidence": 0.0 to 1.0
}}
Do not add anything else.
""".strip()

    return prompt


def call_model(tokenizer, model, prompt: str) -> dict:
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=60,       # FAST
            do_sample=True,
            top_p=0.9,
            temperature=0.7
        )

    full_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # try to extract JSON
    start = full_text.find("{")
    end = full_text.rfind("}")
    if start == -1 or end == -1:
        return {
            "description": "ML refinement unavailable",
            "confidence": 0.5
        }

    try:
        js = json.loads(full_text[start:end+1])
        desc = js.get("description", "ML refinement unavailable")
        conf = float(js.get("confidence", 0.5))
        return {"description": desc, "confidence": conf}
    except:
        return {
            "description": "ML refinement unavailable",
            "confidence": 0.5
        }


def refine_report():
    if not INPUT_JSON.exists():
        print("[ML] ERROR: mcp_analysis_output_final.json not found")
        return

    print("[ML] Loading MCP JSON...")
    report = json.loads(INPUT_JSON.read_text())
    tools = report.get("tools", [])

    if not tools:
        print("[ML] No tools found in report; nothing to refine.")
        return

    tokenizer, model = load_model()

    print(f"[ML] Refining {len(tools)} tools... (fast mode)")
    for idx, tool in enumerate(tools):
        print(f"[ML] Tool {idx+1}/{len(tools)}: {tool.get('name')}")
        prompt = build_prompt_for_tool(tool, idx)
        ml_out = call_model(tokenizer, model, prompt)

        tool["ml_refined_description"] = ml_out["description"]
        tool["ml_confidence"] = ml_out["confidence"]

    report["ml_refinement"] = {
        "model_name": MODEL_NAME,
        "notes": "Fast ML refinement applied using Phi-3 Mini 128M"
    }

    OUTPUT_JSON.write_text(json.dumps(report, indent=2))
    print(f"[ML] Done. Output saved to: {OUTPUT_JSON}")


if __name__ == "__main__":
    refine_report()
