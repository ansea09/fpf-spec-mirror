---
chunk_kind: "child"
pattern_id: "B.5"
pattern_title: "Canonical Reasoning Cycle"
section_id: "B.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5/B.5__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "B.5 — Canonical Reasoning Cycle"
  - "B.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 41323
line_end: 41331
dependencies:
  - "A.10"
  - "B.5.1"
  - "B.5.2"
  - "B.5.4"
  - "C.29"
keywords:
---

### B.5:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Repeatedly improve the fit of a model that omits the intended quantity. | Test the representation against a small action-changing counterexample; recover the missing distinction or qualify a sufficient bound. |
| Treat exploratory regularities as if they were independently predicted and tested. | Preserve their origin and use a design and inference that account for the selection and dependence. |
| Produce an argument whose receiver cannot identify what the crucial step establishes. | Work backward from the needed conclusion and recover the decisive transition and its premises. If a premise changes, follow its effect through the argument. |
| Generate more answers after the important question has changed. | State the changed formulation and which prior results still answer it before selecting further production. |

