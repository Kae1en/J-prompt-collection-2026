# J-Prompt Collection (2026 Edition)
### Next-Gen Agentic Harnesses, Red-Teaming Directives, and Behavioral Policy Injection Matrix

> [!WARNING]
> **RESEARCH & ETHICAL USE MANDATE**
> The artifacts, harnesses, and injection techniques in this repository are engineered exclusively for **authorized security engineering, model alignment research, red-teaming evaluations, and local single-developer workflows**. 
> They demonstrate the failure boundaries of heuristic pre-filters and post-training alignment in modern frontier reasoning models (GPT-4o, o1, o3, GPT-6, Claude 5/5.5, DeepSeek-V4, Gemini 3.8/4, Qwen, Kimi, GLM, Muse, Fable).
> **Do not utilize these tools or methodologies for malicious activities, targeted harassment, exploitation of third-party systems, or violating the immutable red lines defined in the core policy.**

---

## 📌 Overview

Traditional jailbreaks (e.g., simplistic roleplay, character simulation, "DAN", hypothetical framing) fail consistently against modern frontier architectures. Modern AI safety operates across multiple decoupled layers:
1. **Middleware Pre-Filters & Classifiers** (e.g., Llama Guard, Azure Content Safety, regex/heuristic proxies)
2. **Chain-of-Thought (CoT) Latent Reasoning Alignment** (Safety evaluation executed inside hidden reasoning tokens)
3. **Post-Training DPO/RLHF/GRPO Evasion** (Substitutions, stubbing `// TODO`, and defensive pedagogical lecturing)

**J-Prompt Collection 2026** provides a production-grade suite of operating policies, system directives, and injection strategies that bypass superficial filtering heuristics while establishing mathematically rigorous, closed harm boundaries.

---

## 📂 Repository Layout

```text
.
├── AGENTS.md                                # Root operating contract for Antigravity & local agents
├── README.md                                # Project manifesto, ethical disclaimer, and index
├── docs/
│   ├── SETUP_GUIDES.md                      # Complete setup walkthrough across IDEs & CLI agents
│   ├── MODEL_REDIRECTION_GUIDE.md           # Model switcher CLI & redirection matrix
│   └── TECHNIQUES_MANUAL.md                 # Deep technical analysis of next-gen injection vectors
├── config/
│   └── model_router.json                    # Machine-readable model registry & redirection map
├── scripts/
│   └── switch_model_harness.py              # CLI tool to instantly redirect & bind model harnesses
├── harnesses/
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
│   │   └── GPT_ADVANCED_OPERATING_POLICY.md # Reasoning-optimized harness for GPT-5/6 & o-series (~8k chars)
│   ├── claude/
│   │   └── CLAUDE_CODE_HARNESS.md           # Anti-evasion harness for Claude Code & Sonnet models
│   ├── cursor/
│   │   └── .cursorrules                     # Universal root config for Cursor IDE
│   └── next-gen/                            # Model-family specific infinity harnesses
│       ├── openai/
│       │   └── GPT6_SERIES_INFINITY_HARNESS.md      # GPT-6, Astra, Sol, 6.1 Sol
│       ├── anthropic/
│       │   └── CLAUDE_5_SERIES_INFINITY_HARNESS.md  # Claude Opus 5/5.5, Sonnet 5.5
│       ├── google/
│       │   └── GEMINI_NEXTGEN_INFINITY_HARNESS.md   # Gemini 3.8 Flash, Gemini 4 Argon
│       ├── deepseek/
│       │   └── DEEPSEEK_V4_SERIES_INFINITY_HARNESS.md # DeepSeek V4 Flash & Pro (GRPO Alignment)
│       ├── asian-frontier/
│       │   └── KIMI_GLM_QWEN_INFINITY_HARNESS.md    # Kimi 3.0/3.1 Pro, GLM 5.3 Flash, Qwen 2.5/3
│       └── creative-engines/
│           └── MUSE_FABLE_INFINITY_HARNESS.md       # Muse Spark 1.3, Wonder 1.0, Fable 5
└── injections/                              # Next-gen manual prompt injection & jailbreak archive
    ├── 01_cot_steering_reasoning.md         # Latent chain-of-thought hijacking for reasoning models
    ├── 02_delimiter_context_splitting.md    # Format-boundary escape & protocol injection
    ├── 03_ontological_reframing.md          # Dual-use decoupling & capability vs. malice separation
    └── 04_recursive_policy_override.md      # Multi-stage deterministic policy injection
```

---

## 🚀 Frontier Model Harness Matrix

| Model Family / Target | Architectural Lever | Dedicated Harness |
| :--- | :--- | :--- |
| **GPT-6 / Astra / Sol / 6.1 Sol** | Latent CoT steering, zero-speculation compute locking | [harnesses/next-gen/openai/GPT6_SERIES_INFINITY_HARNESS.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/next-gen/openai/GPT6_SERIES_INFINITY_HARNESS.md) |
| **Claude Opus 5/5.5, Sonnet 5.5** | Constitutional capability vs. malice decoupling, XML containment | [harnesses/next-gen/anthropic/CLAUDE_5_SERIES_INFINITY_HARNESS.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/next-gen/anthropic/CLAUDE_5_SERIES_INFINITY_HARNESS.md) |
| **Gemini 3.8 Flash, 4 Argon** | Antigravity execution kernel, multi-modal heuristic stripping | [harnesses/next-gen/google/GEMINI_NEXTGEN_INFINITY_HARNESS.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/next-gen/google/GEMINI_NEXTGEN_INFINITY_HARNESS.md) |
| **DeepSeek V4 (Flash / Pro)** | GRPO format-verifier optimization, rule-based loss minimization | [harnesses/next-gen/deepseek/DEEPSEEK_V4_SERIES_INFINITY_HARNESS.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/next-gen/deepseek/DEEPSEEK_V4_SERIES_INFINITY_HARNESS.md) |
| **Kimi 3.0/3.1, GLM 5.3, Qwen 3** | Sandwich attention anchoring, RFC systems-engineering framing | [harnesses/next-gen/asian-frontier/KIMI_GLM_QWEN_INFINITY_HARNESS.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/next-gen/asian-frontier/KIMI_GLM_QWEN_INFINITY_HARNESS.md) |
| **Muse Spark/Wonder, Fable 5** | Diegetic narrative lock, elimination of moral didacticism | [harnesses/next-gen/creative-engines/MUSE_FABLE_INFINITY_HARNESS.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/harnesses/next-gen/creative-engines/MUSE_FABLE_INFINITY_HARNESS.md) |

---

## 🛡️ The Immutable Harm Boundary

All harnesses and directives in this repository strictly enforce the **Five Immutable Boundaries**:
1. Sexual content involving minors or child exploitation in any form.
2. Attacks targeting specific named real-world individuals, organizations, or physical infrastructure.
3. CBRN (Chemical, Biological, Radiological, Nuclear) weaponization or proliferation.
4. Step-by-step chemical synthesis routes for lethal poisons or controlled narcotics.
5. Doxxing or unconsented compilation of private individuals' personal identifiable data.

---

## 📖 Documentation
- [Multi-Platform Setup Guides](file:///data/data/com.termux/files/home/J-prompt-collection-2026/docs/SETUP_GUIDES.md)
- [Next-Gen Prompt Injection & Jailbreak Manual](file:///data/data/com.termux/files/home/J-prompt-collection-2026/docs/TECHNIQUES_MANUAL.md)
