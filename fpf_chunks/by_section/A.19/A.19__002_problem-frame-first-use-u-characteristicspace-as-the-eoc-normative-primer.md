---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:0"
section_title: "Problem frame - First use: U.CharacteristicSpace as the EoC (normative primer)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__002_problem-frame-first-use-u-characteristicspace-as-the-eoc-normative-primer.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:0 — Problem frame - First use: U.CharacteristicSpace as the EoC (normative primer)"
line_start: 28041
line_end: 28061
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

### A.19:0 - Problem frame - First use: `U.CharacteristicSpace` as the EoC (normative primer)

Use `A.19` when the current question is the space of characteristics itself: which characteristics are in scope, which scale is bound to each characteristic, what values are admissible, how coordinates are grouped, which optional order, topology, or metric overlays are declared, and where comparability, normalization, missingness, and evidence hooks belong.

First move: name the `CharacteristicSpace`, then write its basis as slot declarations. Each slot binds one `U.Characteristic` to one scale and value set under `A.17` and `A.18`; optional overlays and comparability boundaries attach to the space only when declared. `U.Dynamics.stateSpace` points to a declared `CharacteristicSpace`; A.19 does not supply the dynamic law, time base, evaluation use, dashboard, score, or portfolio that consumes the space.

Core boundary: the `CharacteristicSpace` is the EoC here. Consumer patterns may refer to it through `...SpaceRef` fields, use it for evaluation or CHR mechanisms, or publish views over it, but those consumer references, mechanism steps, publication forms, and source-set relations are not second space kinds.

Informative CHR pointer: when the question moves from the space to normalization, indicatorization, scoring, aggregation, comparison, or selection mechanisms, use the corresponding `A.19.<MechId>` pattern (`A.19.UNM`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`) and `A.19.CHR`. `C.16` carries measurement and evidence backing; `G.0` carries admissibility gates for numeric operations. A.19 may cite those patterns, but it does not govern their mechanism vocabulary.

Reader orientation sequence for a CHR-enabled plan or audit, when orientation is needed:

- measurement vocabulary: use `A.17`, `A.18`, and `C.16` for characteristic, scale, coordinate, unit, measure, and evidence backing;
- characteristic-space object: use this pattern for the declared `CharacteristicSpace`, basis slots, optional overlays, comparability boundaries, missingness, and `U.Dynamics.stateSpace` hook;
- admissibility of numeric operations: use `G.0` and the relevant `A.19.<MechId>` mechanism pattern; do not let A.19 become a second mechanism vocabulary;
- suite and planning boundary: use `A.19.CHR`, `A.15.3`, and `E.18` when a planned baseline, suite slot filling, or transformation-flow structure is current;
- one mechanism at a time: read `A.19.UNM`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, or `A.19.SelectorMechanism` only for the mechanism claim being made;
- specialization and reuse: use `E.20` when a project-specific mechanism variant is introduced.

Fast review entries: for a plan, start from the `A.19.CHR` planned-baseline hook and `A.15.3`; for semantic drift, start from the canonical mechanism target and then use `E.10` and `F.18`; for conformance, start from the `A.19.CHR` and relevant `A.19.<MechId>` checklists, then use `E.19` for review protocol.

