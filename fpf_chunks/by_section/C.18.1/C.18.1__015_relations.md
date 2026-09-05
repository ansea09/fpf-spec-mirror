---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__015_relations.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:13 — Relations"
line_start: 50262
line_end: 50274
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "G.10"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DoE (design‑of‑experiments)"
  - "Scale Variables (S)"
  - "ScaleWindow"
  - "UNM/NormalizationMethod‑based mapping"
  - "compute‑elasticity"
  - "data‑elasticity"
  - "diminishing returns"
  - "exponent class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

### C.18.1:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim that more review capacity, tool calls, tokens, data, model capacity, parallelism, freedom of action, sprints, or another declared scale variable changes rate, learning, recovery, throughput, stabilization, or improvement.
- This pattern keeps: scale variable, scale window, scale probes, and elasticity value.
- Non-admissible use: more scale does not by itself establish linear improvement, and a scale word does not create a C.27 rate-change claim by itself.
- Neighboring-pattern use: if comparison or benchmark use is current, cite G.9 for parity; if linear improvement is merely assumed, name the scale variable and scale window or state the improvement claim as an assumption.

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; UNM/NormalizationMethod‑based mapping), **G.10** (shipping).

> *Pedagogical cue.* **Say what you would scale, probe at least two scale points, and use the slope‑class to steer.**

