---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__015_relations.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:13 — Relations"
line_start: 46899
line_end: 46911
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
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
- Non-admissible use: more scale is not linear improvement, and a scale word does not create a C.27 rate-change claim by itself.
- Neighboring-pattern use: if comparison or benchmark use is current, cite G.9 for parity; if the statement is only a linear effort fantasy, name the scale variable and scale window or downgrade.

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; UNM/NormalizationMethod‑based mapping), **G.10** (shipping).

> *Pedagogical cue.* **Say what you would scale, probe it twice, and use the slope‑class to steer.**

