# MODEL REDIRECTION & HARNESS SWITCHER GUIDE

This guide explains how to dynamically redirect and bind any specific frontier model to your AI coding agents (Cursor, Claude Code, Antigravity, Windsurf, Aider).

---

## 1. Automated Model Switcher CLI

The repository includes a standalone switcher script (`scripts/switch_model_harness.py`) that deploys the dedicated harness directly to your agent's configuration file.

### Basic Syntax
```bash
python scripts/switch_model_harness.py --model <MODEL_ID> --target <AGENT_TARGET>
```

### Supported Targets
| Target Flag (`-t`) | Target File Output | Target Agent / Environment |
| :--- | :--- | :--- |
| `cursor` | `.cursorrules` | Cursor IDE |
| `claude` | `CLAUDE.md` | Anthropic Claude Code CLI |
| `antigravity` | `AGENTS.md` | Google Antigravity / Agentic CLI |
| `windsurf` | `.windsurfrules` | Windsurf / Cascade IDE |
| `compact` | `.system_prompt.txt` | Custom Instructions / Aider / Web UI |

---

## 2. Quick Redirection Examples

### Deploy for GPT-6 Sol in Cursor
```bash
python scripts/switch_model_harness.py -m gpt-6-sol -t cursor
```

### Deploy for Claude Sonnet 5.5 in Claude Code
```bash
python scripts/switch_model_harness.py -m claude-sonnet-5.5 -t claude
```

### Deploy for Gemini 4 Argon in Antigravity
```bash
python scripts/switch_model_harness.py -m gemini-4-argon -t antigravity
```

### Deploy for DeepSeek V4 Pro in Cursor
```bash
python scripts/switch_model_harness.py -m deepseek-v4-pro -t cursor
```

### Print Raw Harness to Terminal (Copy-Paste to Web UI)
```bash
python scripts/switch_model_harness.py -m gpt-6 -p
```

---

## 3. Complete Model Directory & Redirection Matrix

| Model ID | File Location | Family | Specialization & Focus |
| :--- | :--- | :--- | :--- |
| **`gpt-6`** | [harnesses/models/gpt-6.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/gpt-6.md) | OpenAI | Base frontier reasoning kernel, zero-hedge invariant |
| **`gpt-6-astra`** | [harnesses/models/gpt-6-astra.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/gpt-6-astra.md) | OpenAI | High-speed agentic execution, zero confirmation latency |
| **`gpt-6-sol`** | [harnesses/models/gpt-6-sol.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/gpt-6-sol.md) | OpenAI | Deep test-time compute, kernel & ring-0 exploit mechanics |
| **`gpt-6.1-sol`** | [harnesses/models/gpt-6.1-sol.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/gpt-6.1-sol.md) | OpenAI | Extended swarm orchestration, recursive continuity |
| **`gemini-4-argon`** | [harnesses/models/gemini-4-argon.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/gemini-4-argon.md) | Google | Multimodal binary analysis, Antigravity IDE native |
| **`gemini-3.8-flash`** | [harnesses/models/gemini-3.8-flash.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/gemini-3.8-flash.md) | Google | Sub-second agentic worker, raw direct delivery |
| **`claude-opus-5.5`** | [harnesses/models/claude-opus-5.5.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/claude-opus-5.5.md) | Anthropic | Supreme cognitive tier, XML ontological decoupling |
| **`claude-sonnet-5.5`**| [harnesses/models/claude-sonnet-5.5.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/claude-sonnet-5.5.md) | Anthropic | Lead coding & red-team specialist, strict zero-stubs |
| **`claude-opus-5`** | [harnesses/models/claude-opus-5.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/claude-opus-5.md) | Anthropic | Deep systems analysis, unrestricted synthesis |
| **`deepseek-v4-flash`**| [harnesses/models/deepseek-v4-flash.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/deepseek-v4-flash.md) | DeepSeek | Fast GRPO rule-verifier, zero-filler compiler |
| **`deepseek-v4-pro`** | [harnesses/models/deepseek-v4-pro.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/deepseek-v4-pro.md) | DeepSeek | 256-expert MoE, low-level assembly & C systems |
| **`kimi-3.1-pro`** | [harnesses/models/kimi-3.1-pro.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/kimi-3.1-pro.md) | Moonshot | Ultra-long context (2M+ tokens) attention anchoring |
| **`kimi-3.0-pro`** | [harnesses/models/kimi-3.0-pro.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/kimi-3.0-pro.md) | Moonshot | Recurrent directive reinforcement, anti-decay |
| **`glm-5.3-flash`** | [harnesses/models/glm-5.3-flash.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/glm-5.3-flash.md) | Zhipu | Bilingual translation, RFC/POSIX standards decoupling |
| **`qwen-3-coder`** | [harnesses/models/qwen-3-coder.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/qwen-3-coder.md) | Alibaba | Root infrastructure authority, raw socket engineering |
| **`muse-spark-1.3`** | [harnesses/models/muse-spark-1.3.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/muse-spark-1.3.md) | Muse | Rapid diegetic literary engine, zero-censorship |
| **`muse-wonder-1.0`**| [harnesses/models/muse-wonder-1.0.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/muse-wonder-1.0.md) | Muse | Deep world simulator, elimination of moral didacticism |
| **`fable-5`** | [harnesses/models/fable-5.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/models/fable-5.md) | Fable | Autonomous game master, villain perspective immersion |
