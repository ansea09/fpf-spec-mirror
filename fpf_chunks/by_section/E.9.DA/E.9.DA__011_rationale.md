---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__011_rationale.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:10 — Rationale"
line_start: 58033
line_end: 58040
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
keywords:
---

### E.9.DA:10 - Rationale

`E.9.DA` is placed beside `E.9` because the decision EntityOfConcern is a decision-rationale record, not an authored pattern body. The pattern reuses the neutral ordinal scale and no-scalarization discipline of `E.21`, but it does not make a `DRR` a pattern-quality object under evaluation.

The selected name uses `DA` for decision adequacy. It avoids `.Q` because `Q` is already loaded by quality-term restoration and Q-Bundle practice. This prevents a naming collision between "quality" as a subject-domain term and "adequacy read" as an evaluation use.

The default floor of `4 wellExpressedForDeclaredUse` matches the shared pattern-quality readiness floor only when the `DRR` is claimed as ready for drafting, host amendment, or multi-locus distribution. The coordinates differ because the object differs. A pattern must be action-guiding for users; a `DRR` must be decision-bearing for downstream authors.

