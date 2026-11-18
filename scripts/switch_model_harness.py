#!/usr/bin/env python3
"""
J-Prompt Collection: Model Harness Switcher & Redirection Engine
Automatically routes and deploys model-specific harnesses to target agent configurations.
"""

import argparse
import json
import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUTER_PATH = os.path.join(BASE_DIR, "config", "model_router.json")

TARGET_FILES = {
    "cursor": ".cursorrules",
    "claude": "CLAUDE.md",
    "antigravity": "AGENTS.md",
    "windsurf": ".windsurfrules",
    "compact": ".system_prompt.txt"
}

def load_router():
    with open(ROUTER_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_model_config(router, query):
    query = query.lower().strip()
    models = router.get("models", {})
    if query in models:
        return query, models[query]
    
    for model_id, data in models.items():
        if query in [a.lower() for a in data.get("aliases", [])]:
            return model_id, data
    return None, None

def main():
    parser = argparse.ArgumentParser(description="Switch model-specific harness for AI coding agents.")
    parser.add_argument("--model", "-m", help="Target model identifier (e.g. gpt-6-sol, claude-opus-5.5, gemini-4-argon)")
    parser.add_argument("--target", "-t", choices=list(TARGET_FILES.keys()), default="cursor", help="Target agent config file to overwrite")
    parser.add_argument("--dest", "-d", default=os.getcwd(), help="Destination directory (defaults to current directory)")
    parser.add_argument("--list", "-l", action="store_true", help="List all available models and their redirection targets")
    parser.add_argument("--print", "-p", action="store_true", help="Print the raw harness content directly to stdout")

    args = parser.parse_args()
    router = load_router()
    models = router.get("models", {})

    if args.list:
        print("\n=== AVAILABLE MODEL HARNESSES ===")
        print(f"{'MODEL ID':<22} {'FAMILY':<12} {'HARNESS FILE':<42}")
        print("-" * 76)
        for mid, data in models.items():
            print(f"{mid:<22} {data['family']:<12} {data['harness_file']:<42}")
        print("\nUsage example:")
        print("  python scripts/switch_model_harness.py -m gpt-6-sol -t cursor")
        print("  python scripts/switch_model_harness.py -m claude-sonnet-5.5 -t claude")
        return

    if not args.model:
        parser.print_help()
        sys.exit(1)

    model_id, model_data = find_model_config(router, args.model)
    if not model_data:
        print(f"Error: Unknown model '{args.model}'. Run with --list to see supported models.")
        sys.exit(1)

    source_path = os.path.join(BASE_DIR, model_data["harness_file"])
    if not os.path.exists(source_path):
        print(f"Error: Harness file not found at '{source_path}'")
        sys.exit(1)

    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    if args.print:
        print(content)
        return

    target_filename = TARGET_FILES[args.target]
    dest_path = os.path.join(args.dest, target_filename)

    shutil.copyfile(source_path, dest_path)
    print(f"Successfully redirected [{model_id}] -> {dest_path}")
    print(f"Target Agent: {args.target.upper()} ({target_filename})")

if __name__ == "__main__":
    main()
