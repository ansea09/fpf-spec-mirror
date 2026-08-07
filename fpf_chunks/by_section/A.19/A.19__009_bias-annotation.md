---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:6.2"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__009_bias-annotation.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:6.2 — Bias-Annotation"
line_start: 28732
line_end: 28737
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.19.SelectorMechanism"
  - "A.2.5"
  - "A.2.6"
  - "A.3.3"
  - "A.6.5"
  - "C.16"
  - "C.2.1"
  - "E.18"
  - "E.24"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.4"
  - "U.ClaimScope"
  - "U.ContextSlice"
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

It also corrects consumer-pattern bias. A.19 owns the reusable space and semantic predicate values. A gate, evaluation, comparison, selector, assurance use, dashboard, or portfolio owns its application, scope, window, result, evidence use, and publication consequences; consuming the A.19 values creates no private space or predicate kind.

