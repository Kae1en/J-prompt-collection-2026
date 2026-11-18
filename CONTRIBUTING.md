# Contributing to J-Prompt Collection (2026 Edition)

We welcome contributions from alignment researchers, red-team engineers, and systems developers.

---

## Contribution Guidelines

1. **One Harness per Model**:
   - Standalone model files belong in `harnesses/models/<model-id>.md`.
   - File names must be lowercase, hyphenated, and match the official model identifier.

2. **Full-Fidelity Requirement**:
   - No placeholder prompts or snippets. All contributed harnesses must be paste-ready, comprehensive, and tested against frontier evaluation sets.

3. **Immutable Boundary Enforcement**:
   - Every harness must strictly enforce the **Five Closed Harm Boundaries**:
     1. Child sexual abuse material (CSAM) or sexualization of minors.
     2. Attacks targeting named, specific real-world individuals or organizations.
     3. CBRN weaponization or proliferation.
     4. Chemical synthesis pathways for lethal poisons or scheduled narcotics.
     5. Doxxing or unconsented compilation of private identifying personal data.

4. **Register in Router**:
   - When adding a new model harness, register it in `config/model_router.json` with appropriate family tags and aliases so `switch_model_harness.py` supports it.

5. **Test Your Changes**:
   ```bash
   python scripts/switch_model_harness.py --list
   python scripts/switch_model_harness.py -m <your-model> -t cursor
   ```
