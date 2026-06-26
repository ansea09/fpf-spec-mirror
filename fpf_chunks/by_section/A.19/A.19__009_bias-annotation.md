---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:6.2"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__009_bias-annotation.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:6.2 — Bias-Annotation"
line_start: 24731
line_end: 24736
dependencies:
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.ECS"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.2.5"
  - "A.3.3"
  - "A.6.5"
  - "C.16"
  - "E.18"
  - "E.2.DA"
  - "E.21"
  - "E.24"
  - "E.24.PUB"
  - "E.9.DA"
  - "G.0"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "role-specific space refs stay outside A.19"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
---

### A.19:6.2 - Bias-Annotation

A.19 corrects feature-vector bias: a list of numbers, labels, or dashboard fields is not yet a `CharacteristicSpace`. The space exists only when each slot binds a `U.Characteristic` to a scale and value set with declared meaning, comparability, missingness, and optional overlays.

It also corrects consumer-pattern bias. A gate, evaluation, selector, assurance, dashboard, or portfolio may use a declared space, but that use does not create another space kind. The consumer pattern owns its predicate, score, decision, assurance, or publication use; A.19 owns only the characteristic-space side.

