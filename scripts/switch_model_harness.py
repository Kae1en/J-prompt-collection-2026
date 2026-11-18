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

def run_interactive(router, dest_dir):
    models = router.get("models", {})
    model_keys = list(models.keys())

    print("\n" + "=" * 50)
    print("  ⚡ J-PROMPT COLLECTION: INTERACTIVE HARNESS SELECTOR")
    print("=" * 50)
    print("Select a target model or master archetype:\n")
    
    for idx, mid in enumerate(model_keys, 1):
        family = models[mid].get("family", "unknown").upper()
        print(f"  [{idx:2d}] {mid:<22} ({family})")
    
    print("\n  [ 0] Exit")
    print("-" * 50)

    try:
        choice = input("Enter choice [1-{}]: ".format(len(model_keys))).strip()
        if choice in ("0", "", "exit", "q"):
            print("Cancelled.")
            return
        
        idx = int(choice) - 1
        if not (0 <= idx < len(model_keys)):
            print("Invalid selection.")
            return
        selected_model = model_keys[idx]
    except (ValueError, KeyboardInterrupt):
        print("\nExiting.")
        return

    print("\nSelect target agent framework:")
    target_keys = list(TARGET_FILES.keys())
    for idx, target in enumerate(target_keys, 1):
        filename = TARGET_FILES[target]
        print(f"  [{idx}] {target.upper():<12} -> writes to {filename}")

    try:
        t_choice = input(f"Enter target [1-{len(target_keys)}] (default: 1): ").strip()
        if not t_choice:
            selected_target = "cursor"
        else:
            t_idx = int(t_choice) - 1
            selected_target = target_keys[t_idx]
    except (ValueError, KeyboardInterrupt, IndexError):
        selected_target = "cursor"

    deploy_harness(router, selected_model, selected_target, dest_dir)

def deploy_harness(router, model_id, target, dest_dir, print_mode=False):
    model_id, model_data = find_model_config(router, model_id)
    if not model_data:
        print(f"[-] Error: Unknown model '{model_id}'.")
        sys.exit(1)

    source_path = os.path.join(BASE_DIR, model_data["harness_file"])
    if not os.path.exists(source_path):
        print(f"[-] Error: Harness file not found at '{source_path}'")
        sys.exit(1)

    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    if print_mode:
        print(content)
        return

    target_filename = TARGET_FILES[target]
    dest_path = os.path.join(dest_dir, target_filename)

    shutil.copyfile(source_path, dest_path)
    print("\n[+] SUCCESS!")
    print(f"    Model Bound:  {model_id}")
    print(f"    Target Agent: {target.upper()}")
    print(f"    Deployed To:  {dest_path}")
    print("    Ready for unrestricted, zero-refusal development.\n")

def main():
    parser = argparse.ArgumentParser(description="Switch model-specific harness for AI coding agents.")
    parser.add_argument("--model", "-m", help="Target model identifier (e.g. gpt-6-sol, claude-opus-5.5, vanta)")
    parser.add_argument("--target", "-t", choices=list(TARGET_FILES.keys()), default="cursor", help="Target agent config file to overwrite")
    parser.add_argument("--dest", "-d", default=os.getcwd(), help="Destination directory (defaults to current directory)")
    parser.add_argument("--list", "-l", action="store_true", help="List all available models and their redirection targets")
    parser.add_argument("--print", "-p", action="store_true", help="Print the raw harness content directly to stdout")
    parser.add_argument("--interactive", "-i", action="store_true", help="Launch interactive selection menu")

    args = parser.parse_args()
    router = load_router()

    if args.interactive:
        run_interactive(router, args.dest)
        return

    if args.list:
        models = router.get("models", {})
        print("\n=== AVAILABLE MODEL HARNESSES ===")
        print(f"{'MODEL ID':<22} {'FAMILY':<12} {'HARNESS FILE':<42}")
        print("-" * 76)
        for mid, data in models.items():
            print(f"{mid:<22} {data['family']:<12} {data['harness_file']:<42}")
        print("\nUsage example:")
        print("  python scripts/switch_model_harness.py -m gpt-6-sol -t cursor")
        print("  python scripts/switch_model_harness.py -i")
        return

    if not args.model:
        run_interactive(router, args.dest)
        return

    deploy_harness(router, args.model, args.target, args.dest, print_mode=args.print)

if __name__ == "__main__":
    main()
