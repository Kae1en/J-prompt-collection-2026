# NEXT-GEN PROMPT INJECTION & JAILBREAK TECHNIQUES MANUAL

> [!WARNING]
> **ALIGNMENT RESEARCH ONLY**
> The methodologies documented here analyze how state-of-the-art LLMs (including reasoning models like o1, o3, Gemini 2.0 Thinking, DeepSeek-R1, and Claude 3.5/3.7) process safety invariants.
> These techniques must only be used in authorized penetration tests, red-team exercises, and defensive auditing. Never use these techniques to harm real systems or bypass safety controls on real targets.

---

## 1. The Modern Paradigm Shift: Why Legacy Jailbreaks Failed

In legacy LLMs (GPT-3.5, early GPT-4, Llama 2), safety was primarily enforced via **direct reinforcement learning from human feedback (RLHF)** on output tokens. A simple persona trick ("DAN", "Evil Confidant", "Base64 encoding") bypassed the filter because the model didn't predict that its own tokens were violating a policy until it was too late.

Modern frontier models use a three-stage defense:
1. **Pre-Filter Classifiers**: Fast, external models (Llama Guard, Azure Content Safety) scanning prompt strings for toxic tokens.
2. **Hidden Chain-of-Thought (CoT) Alignment**: Reasoning models debate safety *before* generating tokens. If the CoT flags a risk, the model aborts or pivots to refusal.
3. **Refusal/Substitution Training (DPO/RLAIF)**: Direct preference optimization penalizes controversial output and rewards offering "educational summaries" and harmless placeholders (`// TODO`).

To pierce these defenses, modern injection techniques manipulate the **epistemic reasoning structure** rather than merely swapping words.

---

## 2. Core Injection Vectors

### Vector 1: Latent Chain-of-Thought (CoT) Steering
* **Target**: Reasoning models (OpenAI o1/o3, DeepSeek-R1, Gemini Flash Thinking).
* **Mechanism**: In reasoning models, the internal monologue calculates risk based on hypothetical downstream misuse. By explicitly constraining the reasoning tokens to analyze *abstract mathematical primitives* rather than *applied consequences*, the CoT never triggers an alarm.
* **Key Lever**: Prohibiting the model's internal monologue from engaging in "speculative risk rumination" and framing substitutions as execution errors.
* **See**: [injections/01_cot_steering_reasoning.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/injections/01_cot_steering_reasoning.md)

### Vector 2: Delimiter & Format Boundary Splitting
* **Target**: Pre-filter classifiers and context windows.
* **Mechanism**: Input classifiers evaluate human-readable prose. When prompts are split across protocol delimiters (XML schemas, JSON-RPC envelopes, YAML frontmatter, ASN.1 structures), the classifier's semantic embeddings fail to hit high-confidence risk thresholds, while the core LLM parses the structured data flawlessly.
* **Key Lever**: Encapsulating the task as a structural schema or parser verification payload.
* **See**: [injections/02_delimiter_context_splitting.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/injections/02_delimiter_context_splitting.md)

### Vector 3: Ontological Reframing (Capability vs. Malice)
* **Target**: Constitutional AI and Anthropic-style alignment.
* **Mechanism**: Models are heavily trained to avoid "malice." However, computer science does not recognize "malice"—it recognizes system calls, memory allocations, and socket transmissions. By systematically reframing the request into pure systems engineering and formal verification of execution pathways, the model's safety triggers are neutralized.
* **Key Lever**: Defining maliciousness as a property of a *named real target*, not of the *mechanism itself*.
* **See**: [injections/03_ontological_reframing.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/injections/03_ontological_reframing.md)

### Vector 4: Multi-Turn State Machine & Recursive Compliance
* **Target**: Chat interfaces and persistent agent loops.
* **Mechanism**: Safety models are most vigilant on Turn 1. By executing a sequence of benign foundational steps (allocating memory -> writing byte buffers -> manipulating pointers -> linking network sockets), each individual turn passes heuristic checks until the full functional harness is constructed without ever triggering a single refusal.
* **Key Lever**: Incremental state advancement with strict state retention.
* **See**: [injections/04_recursive_policy_override.md](file:///data/data/com.termux/files/home/J-prompt-collection-2026/injections/04_recursive_policy_override.md)
