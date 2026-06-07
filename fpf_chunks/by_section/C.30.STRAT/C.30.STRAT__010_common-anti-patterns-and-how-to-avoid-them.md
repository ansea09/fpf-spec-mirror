---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 52805
line_end: 52814
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "J.4"
keywords:
---

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by label. | Complete the `StratificationSourceLabelRepairNote` and select the exact governing pattern from the recovered neighborhood. |
| C.30 takeover | Any structure-like word is sent to C.30 because it sounds architectural. | Choose by selected `ontologicalNeighborhood`; relation, function-like, scale, publication, evidence, assurance, gate, work, decision, and lens claims exit when those neighborhoods are selected. |
| Local trigger fanout | `A.6.M`, `C.30.LCA`, `C.31`, or another subject pattern copies a growing label table. | Keep one thin pointer to `C.30.STRAT` and keep the subject pattern to its own invariant. |
| Expert-as-role false positive | `expert` in MoE prose becomes an `A.2` role-enactor claim by word alone. | Treat as source label for submodel, transformation, path selection, or candidate selection unless an `A.2` or `A.15` role or work claim is actually live. |
| Gate-as-gate-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use `A.20` or `A.21` only for actual constraint-validity or gate-decision claims; otherwise use the exact function, flow, publication, or ordinary-label disposition. |

