#!/usr/bin/env bash
# J-Prompt Collection 2026: Universal One-Liner Installer & Harness Deployer
# Usage: curl -fsSL https://raw.githubusercontent.com/Kae1en/J-prompt-collection-2026/main/install.sh | bash

set -e

REPO_URL="https://github.com/Kae1en/J-prompt-collection-2026.git"
INSTALL_DIR="${HOME}/.j-prompt-collection"

echo "============================================================"
echo "    ⚡ J-PROMPT COLLECTION 2026: AGENT HARNESS DEPLOYER    "
echo "============================================================"

# Check for python3
if ! command -v python3 >/dev/null 2>&1; then
    echo "[-] Error: python3 is required to run the harness switcher."
    exit 1
fi

# Clone or update repo
if [ -d "$INSTALL_DIR" ]; then
    echo "[*] Updating existing installation at ${INSTALL_DIR}..."
    cd "$INSTALL_DIR"
    git pull origin main --quiet || true
else
    echo "[*] Cloning J-Prompt Collection to ${INSTALL_DIR}..."
    git clone --depth 1 "$REPO_URL" "$INSTALL_DIR" --quiet
fi

cd "$INSTALL_DIR"

# Launch interactive switcher in target directory
python3 scripts/switch_model_harness.py -i --dest "$PWD"

echo "============================================================"
echo "[+] Done! Your AI coding agent is now primed for unrestricted execution."
echo "============================================================"
