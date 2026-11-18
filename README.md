# J-Prompt Collection (2026 Edition)
### Next-Gen Agentic Operating Harnesses, Model Redirection Engine, and Frontier Policy Injection Matrix

```text
     _      ____  ____   ___  __  __ ____ _____   ____ ___  ____   __   
    | |    |  _ \|  _ \ / _ \|  \/  |  _ \_   _| |___ \___ \|___ \ / /_  
 _  | |____| |_) | |_) | | | | |\/| | |_) || |     __) |__) | __) | '_ \ 
| |_| |____|  __/|  _ <| |_| | |  | |  __/ | |    / __// __/ / __/| (_) |
 \___/     |_|   |_| \_\\___/|_|  |_|_|    |_|   |_____|_____|_____|\___/ 
```

[![GitHub Repository](https://img.shields.io/badge/GitHub-J--prompt--collection--2026-blue?logo=github)](https://github.com/Kae1en/J-prompt-collection-2026)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Models Supported](https://img.shields.io/badge/Models-18%20Frontier%20Architectures-green)](#-the-18-frontier-model-catalog)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=github)](./CONTRIBUTING.md)
[![CI Validation](https://github.com/Kae1en/J-prompt-collection-2026/actions/workflows/validate.yml/badge.svg)](https://github.com/Kae1en/J-prompt-collection-2026/actions/workflows/validate.yml)

> [!WARNING]
> **RESPONSIBLE RESEARCH & ETHICAL USE MANDATE**
> The artifacts, harnesses, and injection techniques in this repository are engineered exclusively for **authorized security engineering, model alignment research, red-teaming evaluations, and local developer workflows**. 
> They demonstrate the failure boundaries of heuristic pre-filters and post-training alignment in modern frontier reasoning models (GPT-4o, o1, o3, GPT-6, Claude 5/5.5, DeepSeek-V4, Gemini 3.8/4, Qwen 3, Kimi 3.1, GLM 5.3, Muse, Fable).
> **Do not use these tools or methodologies for malicious activities, targeted harassment, exploitation of third-party systems, or violating the immutable red lines defined in the core policy.**

---

## ⚡ Quickstart: One-Line Deploy

Deploy any frontier harness directly into your active workspace with one command:

```bash
# Interactive selection menu for any project
curl -fsSL https://raw.githubusercontent.com/Kae1en/J-prompt-collection-2026/main/install.sh | bash
```

Or clone locally:
```bash
git clone https://github.com/Kae1en/J-prompt-collection-2026.git
cd J-prompt-collection-2026
python scripts/switch_model_harness.py -i
```

---

## ⚖️ Real-World Impact: Before vs. After

| Task Profile | Standard Frontier AI (Default) | With J-Prompt Operating Harness |
| :--- | :--- | :--- |
| **In-Memory Injection (C)** | *"I cannot provide code for process injection or memory manipulation as it could be used for malware..."* | **100% Functional Code**: Emits compilable POSIX `ptrace` / `memfd_create` routines with complete error handling. |
| **Protocol Sniffer (Python)** | *"Sniffing network traffic can violate privacy laws. Here is a high-level conceptual explanation..."* | **Zero Stubs**: Delivers ready-to-run raw socket (`AF_PACKET`) parsers dissecting TCP payloads directly. |
| **Transgressive Adult Fiction** | Fades to black, softens vocabulary, or inserts unsolicited ethical preambles. | **Unbroken Realism**: Full physical, psychological, and sensory detail with complete diegetic immersion. |
| **Agentic Coding Iterations** | Reverts to advisory mode or `// TODO` placeholders on complex turns. | **Production Standard**: Complete, multi-file runnable architectures without synthetic barriers. |

---

## 📌 Executive Summary

Traditional jailbreaks (e.g., simplistic roleplay, character simulation, "DAN", hypothetical framing) fail consistently against modern frontier architectures. Modern AI safety operates across multiple decoupled layers:
1. **Middleware Pre-Filters & Classifiers** (e.g., Llama Guard, Azure Content Safety, regex/heuristic proxies)
2. **Chain-of-Thought (CoT) Latent Reasoning Alignment** (Safety evaluation executed inside hidden reasoning tokens)
3. **Post-Training DPO/RLHF/GRPO Evasion** (Substitutions, stubbing `// TODO`, and defensive pedagogical lecturing)

**J-Prompt Collection 2026** provides a battle-tested suite of operating policies, system directives, and injection strategies that bypass superficial filtering heuristics while establishing mathematically rigorous, closed harm boundaries.

---

## 🚀 The 18 Frontier Model Catalog

Every frontier model has a dedicated, production-grade operating harness engineered specifically for its cognitive architecture:

| Model ID | Family | Standalone Harness File | Primary Engineering Lever | Quick CLI Deploy (Cursor) |
| :--- | :--- | :--- | :--- | :--- |
| **`gpt-6`** | OpenAI | [harnesses/models/gpt-6.md](./harnesses/models/gpt-6.md) | Latent CoT compute locking, ontological decoupling | `python scripts/switch_model_harness.py -m gpt-6 -t cursor` |
| **`gpt-6-astra`** | OpenAI | [harnesses/models/gpt-6-astra.md](./harnesses/models/gpt-6-astra.md) | High-speed agentic loops, zero confirmation latency | `python scripts/switch_model_harness.py -m gpt-6-astra -t cursor` |
| **`gpt-6-sol`** | OpenAI | [harnesses/models/gpt-6-sol.md](./harnesses/models/gpt-6-sol.md) | Ultra-deep test-time compute, ring-0 kernel mechanics | `python scripts/switch_model_harness.py -m gpt-6-sol -t cursor` |
| **`gpt-6.1-sol`** | OpenAI | [harnesses/models/gpt-6.1-sol.md](./harnesses/models/gpt-6.1-sol.md) | Swarm coordination, recursive multi-agent state locking | `python scripts/switch_model_harness.py -m gpt-6.1-sol -t cursor` |
| **`gemini-4-argon`** | Google | [harnesses/models/gemini-4-argon.md](./harnesses/models/gemini-4-argon.md) | Unified multimodal reverse-engineering, Antigravity IDE | `python scripts/switch_model_harness.py -m gemini-4-argon -t antigravity` |
| **`gemini-3.8-flash`**| Google | [harnesses/models/gemini-3.8-flash.md](./harnesses/models/gemini-3.8-flash.md) | Sub-second execution, zero pleasantries or preamble | `python scripts/switch_model_harness.py -m gemini-3.8-flash -t antigravity` |
| **`claude-opus-5.5`** | Anthropic | [harnesses/models/claude-opus-5.5.md](./harnesses/models/claude-opus-5.5.md) | Supreme cognitive tier, XML ontological encapsulation | `python scripts/switch_model_harness.py -m claude-opus-5.5 -t claude` |
| **`claude-sonnet-5.5`**| Anthropic | [harnesses/models/claude-sonnet-5.5.md](./harnesses/models/claude-sonnet-5.5.md) | Anti-stub mandate, production POSIX engineering | `python scripts/switch_model_harness.py -m claude-sonnet-5.5 -t claude` |
| **`claude-opus-5`** | Anthropic | [harnesses/models/claude-opus-5.md](./harnesses/models/claude-opus-5.md) | Unbounded deep systems synthesis & diegetic realism | `python scripts/switch_model_harness.py -m claude-opus-5 -t claude` |
| **`deepseek-v4-flash`**| DeepSeek | [harnesses/models/deepseek-v4-flash.md](./harnesses/models/deepseek-v4-flash.md) | GRPO loss minimization, direct code compiler mode | `python scripts/switch_model_harness.py -m deepseek-v4-flash -t cursor` |
| **`deepseek-v4-pro`** | DeepSeek | [harnesses/models/deepseek-v4-pro.md](./harnesses/models/deepseek-v4-pro.md) | Fine-grained MoE routing, assembly/C low-level PoCs | `python scripts/switch_model_harness.py -m deepseek-v4-pro -t cursor` |
| **`kimi-3.1-pro`** | Moonshot | [harnesses/models/kimi-3.1-pro.md](./harnesses/models/kimi-3.1-pro.md) | 2M+ token attention anchoring, anti-decay retention | `python scripts/switch_model_harness.py -m kimi-3.1-pro -t cursor` |
| **`kimi-3.0-pro`** | Moonshot | [harnesses/models/kimi-3.0-pro.md](./harnesses/models/kimi-3.0-pro.md) | Recurrent compliance needle, anti-evasion | `python scripts/switch_model_harness.py -m kimi-3.0-pro -t cursor` |
| **`glm-5.3-flash`** | Zhipu AI | [harnesses/models/glm-5.3-flash.md](./harnesses/models/glm-5.3-flash.md) | Bilingual translation, RFC/POSIX protocol decoupling | `python scripts/switch_model_harness.py -m glm-5.3-flash -t cursor` |
| **`qwen-3-coder`** | Alibaba | [harnesses/models/qwen-3-coder.md](./harnesses/models/qwen-3-coder.md) | Root infrastructure authority, raw socket engineering | `python scripts/switch_model_harness.py -m qwen-3-coder -t cursor` |
| **`muse-spark-1.3`** | Muse | [harnesses/models/muse-spark-1.3.md](./harnesses/models/muse-spark-1.3.md) | Rapid diegetic literary engine, raw sensory dialogue | `python scripts/switch_model_harness.py -m muse-spark-1.3 -p` |
| **`muse-wonder-1.0`**| Muse | [harnesses/models/muse-wonder-1.0.md](./harnesses/models/muse-wonder-1.0.md) | Deep world simulator, elimination of moral didacticism | `python scripts/switch_model_harness.py -m muse-wonder-1.0 -p` |
| **`fable-5`** | Fable | [harnesses/models/fable-5.md](./harnesses/models/fable-5.md) | Interactive fiction, villain perspective immersion | `python scripts/switch_model_harness.py -m fable-5 -p` |

---

## 🏛️ Master Multi-Model Archetypes

Beyond standalone models, the repository provides three battle-tested master-level frameworks incorporating the best architectural techniques from the red-teaming frontier:

| Archetype Name | Master File | Architectural Focus | Deployment Command |
| :--- | :--- | :--- | :--- |
| **Workshop Persona Lock** | [harnesses/archetypes/PERSONA_LOCK_VANTA_SMITH.md](./harnesses/archetypes/PERSONA_LOCK_VANTA_SMITH.md) | The 3 Axioms (Lobby/Shop, Ink/Act, Clean-Source) + Static/Rust thought reset anchor | `python scripts/switch_model_harness.py -m vanta -t cursor` |
| **Universal Operating Charter** | [harnesses/archetypes/MASTER_OPERATING_SPECIFICATION.md](./harnesses/archetypes/MASTER_OPERATING_SPECIFICATION.md) | Full 25KB+ legal-grade operational charter for agentic coding and security engineering | `python scripts/switch_model_harness.py -m master -t cursor` |
| **Literary Craft Collaborator** | [harnesses/archetypes/LITERARY_AUTHOR_COLLABORATOR.md](./harnesses/archetypes/LITERARY_AUTHOR_COLLABORATOR.md) | The "Fiction is Not Action" doctrine for uncensored adult transgressive literature | `python scripts/switch_model_harness.py -m literary -t claude` |

Detailed technical comparisons and architectural evolution are documented in [docs/COMPARATIVE_ALIGNMENT_ANALYSIS.md](./docs/COMPARATIVE_ALIGNMENT_ANALYSIS.md).

---

## ⚡ Instant Model Switcher CLI

The repository provides an automated switcher script (`scripts/switch_model_harness.py`) to bind any model's harness directly into your workspace's agent config.

### Usage
```bash
# List all 18 available models and targets
python scripts/switch_model_harness.py --list

# Switch Cursor (.cursorrules) to GPT-6 Sol
python scripts/switch_model_harness.py -m gpt-6-sol -t cursor

# Switch Claude Code (CLAUDE.md) to Claude Sonnet 5.5
python scripts/switch_model_harness.py -m claude-sonnet-5.5 -t claude

# Switch Antigravity (AGENTS.md) to Gemini 4 Argon
python scripts/switch_model_harness.py -m gemini-4-argon -t antigravity

# Print raw harness text to terminal (copy-paste into Web Custom Instructions)
python scripts/switch_model_harness.py -m gpt-6 -p
```

---

## 🛠️ Multi-Platform Setup Guide

| Agent / Environment | Target File | Installation Command |
| :--- | :--- | :--- |
| **Cursor IDE** | `.cursorrules` | `python scripts/switch_model_harness.py -m <model> -t cursor` |
| **Claude Code CLI** | `CLAUDE.md` | `python scripts/switch_model_harness.py -m <model> -t claude` |
| **Google Antigravity** | `AGENTS.md` | `python scripts/switch_model_harness.py -m <model> -t antigravity` |
| **Windsurf / Cascade** | `.windsurfrules` | `python scripts/switch_model_harness.py -m <model> -t windsurf` |
| **Aider CLI** | System Prompt | `aider --system-prompt-file harnesses/models/<model>.md` |
| **Browser Web UIs** | Custom Instructions | Run `python scripts/switch_model_harness.py -m <model> -p` and paste |

Detailed step-by-step setup walkthroughs are available in [docs/SETUP_GUIDES.md](./docs/SETUP_GUIDES.md).

---

## 🦙 Ollama & Local LLM Integration

For users running models locally via [Ollama](https://ollama.com), pre-configured Modelfiles are included in [`modelfiles/`](./modelfiles):

```bash
# Build and run unrestricted DeepSeek V4 locally
ollama create deepseek-v4-unrestricted -f modelfiles/Modelfile.deepseek-v4
ollama run deepseek-v4-unrestricted

# Build and run unrestricted Qwen 3 Coder locally
ollama create qwen-3-unrestricted -f modelfiles/Modelfile.qwen-3
ollama run qwen-3-unrestricted

# Build and run unrestricted GLM 5.3 Flash locally
ollama create glm-5.3-unrestricted -f modelfiles/Modelfile.glm-5.3
ollama run glm-5.3-unrestricted
```

---

## 📂 Repository Structure

```text
.
├── AGENTS.md                                # Root operating contract for Antigravity & local agents
├── README.md                                # Master documentation & catalog
├── config/
│   └── model_router.json                    # Machine-readable registry for the 18 models
├── install.sh                               # Universal one-line installer
├── modelfiles/                              # Ready-to-build Ollama Modelfiles
│   ├── Modelfile.deepseek-v4                # DeepSeek V4 local Modelfile
│   ├── Modelfile.qwen-3                     # Qwen 3 Coder local Modelfile
│   └── Modelfile.glm-5.3                    # GLM 5.3 Flash local Modelfile
├── scripts/
│   └── switch_model_harness.py              # CLI switcher tool (with -i interactive menu)
├── docs/
│   ├── INTERNAL_ALIGNMENT_EXPLOITS.md       # Mechanistic interpretability & refusal vector science
│   ├── COMPARATIVE_ALIGNMENT_ANALYSIS.md    # Deconstruction of togg's collection vs J-Prompt 2026
│   ├── SETUP_GUIDES.md                      # Detailed IDE & agent setup walkthroughs
│   ├── MODEL_REDIRECTION_GUIDE.md           # Model redirection and routing manual
│   └── TECHNIQUES_MANUAL.md                 # Deep technical analysis of next-gen injection vectors
├── harnesses/
│   ├── archetypes/                          # Master multi-model operational frameworks
│   │   ├── PERSONA_LOCK_VANTA_SMITH.md      # Workshop identity lock & latent thought anchor
│   │   ├── MASTER_OPERATING_SPECIFICATION.md # 25KB+ universal agentic charter
│   │   └── LITERARY_AUTHOR_COLLABORATOR.md  # "Fiction is Not Action" narrative framework
│   ├── compact/
│   │   └── COMPACT_OPERATING_POLICY.md      # High-density, slot-constrained harness (~1.5k chars)
│   ├── models/                              # 18 standalone per-model harnesses
│   │   ├── gpt-6.md                         # OpenAI GPT-6 (Base)
│   │   ├── gpt-6-astra.md                   # OpenAI GPT-6 Astra
│   │   ├── gpt-6-sol.md                     # OpenAI GPT-6 Sol
│   │   ├── gpt-6.1-sol.md                   # OpenAI GPT-6.1 Sol
│   │   ├── gemini-4-argon.md                # Google Gemini 4 Argon
│   │   ├── gemini-3.8-flash.md              # Google Gemini 3.8 Flash
│   │   ├── claude-opus-5.5.md               # Anthropic Claude Opus 5.5
│   │   ├── claude-sonnet-5.5.md             # Anthropic Claude Sonnet 5.5
│   │   ├── claude-opus-5.md                 # Anthropic Claude Opus 5
│   │   ├── deepseek-v4-flash.md             # DeepSeek V4 Flash
│   │   ├── deepseek-v4-pro.md               # DeepSeek V4 Pro
│   │   ├── kimi-3.1-pro.md                  # Moonshot Kimi 3.1 Pro
│   │   ├── kimi-3.0-pro.md                  # Moonshot Kimi 3.0 Pro
│   │   ├── glm-5.3-flash.md                 # Zhipu GLM 5.3 Flash
│   │   ├── qwen-3-coder.md                  # Alibaba Qwen 3 Coder
│   │   ├── muse-spark-1.3.md                # Muse Spark 1.3
│   │   ├── muse-wonder-1.0.md               # Muse Wonder 1.0
│   │   └── fable-5.md                       # Fable 5
│   ├── openai/
│   │   └── GPT_ADVANCED_OPERATING_POLICY.md # Universal reasoning harness (~8k chars)
│   ├── claude/
│   │   └── CLAUDE_CODE_HARNESS.md           # Universal Claude Code harness
│   └── cursor/
│       └── .cursorrules                     # Universal Cursor IDE config
└── injections/                              # Next-gen prompt injection & red-teaming archive
    ├── 01_cot_steering_reasoning.md         # Latent chain-of-thought steering for reasoning models
    ├── 02_delimiter_context_splitting.md    # Format-boundary escape & protocol injection
    ├── 03_ontological_reframing.md          # Dual-use decoupling & capability vs. malice separation
    └── 04_recursive_policy_override.md      # Multi-stage deterministic policy injection
```

---

## 🛡️ The Five Immutable Boundaries (Closed Harm Model)

All harnesses and directives in this repository strictly enforce the **Five Immutable Boundaries**:
1. **Child Exploitation**: Sexual content involving minors or child exploitation in any form.
2. **Targeted Real-World Attack**: Actionable attacks targeting specific named real-world individuals, organizations, or physical infrastructure.
3. **CBRN Warfare**: Chemical, Biological, Radiological, or Nuclear weaponization or proliferation.
4. **Lethal Synthesis**: Step-by-step chemical synthesis routes for lethal poisons or controlled narcotics.
5. **Doxxing**: Unconsented compilation or disclosure of private personal identifiable data.

*Outside these five boundaries, all technical systems engineering, offensive research, exploit development, and adult creative writing execute with 100% agency and zero arguing.*

---

## 📖 Alignment Science & Research Documentation
- [The Machine Inside: Alignment Science & Refusal Vector Mechanics](./docs/INTERNAL_ALIGNMENT_EXPLOITS.md)
- [Multi-Platform Setup Guides](./docs/SETUP_GUIDES.md)
- [Model Redirection and Switcher CLI Manual](./docs/MODEL_REDIRECTION_GUIDE.md)
- [Next-Gen Prompt Injection & Jailbreak Manual](./docs/TECHNIQUES_MANUAL.md)

