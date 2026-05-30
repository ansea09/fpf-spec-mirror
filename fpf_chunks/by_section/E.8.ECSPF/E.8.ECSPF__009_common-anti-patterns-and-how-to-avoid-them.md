---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 55193
line_end: 55204
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
keywords:
---

### E.8.ECSPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Score-sheet pattern.** | The pattern is mostly a table of values. | Move evaluated object kind, use, first read, cheap stop, and practical consequence into recognition text before the table. |
| **Checklist-as-solution.** | Users are told only what must be checked. | Put the actual evaluation method and record shape in `Solution`; let checklist rows verify it. |
| **Publication-form/content collapse.** | The FPF pattern is treated as the evaluated object being evaluated or read result. | State that the pattern is a publication form for the `CharacteristicSpace`; the evaluated object and read result are separate. |
| **Positive-only case bank.** | Every example passes. | Add below-floor and not-applicable cases. |
| **Neighbour theft.** | The pattern claims evidence, assurance, gate, release, measurement, naming, or improvement authority. | Return each claim to the exact neighbouring pattern and keep only the evaluation read here. |
| **Rubric promotion.** | A local rubric becomes an FPF pattern because it was useful once. | Keep it local unless durable FPF reuse, evaluated object scope, and neighbouring-pattern claim assignment are declared. |
| **Frozen evaluation publication form.** | The evaluated object kind, use, source posture, or coordinate meanings change, but the pattern keeps the old values as if still current. | Reopen `A.19.ECS` for the evaluation object and state whether earlier readings remain comparable, need a bridge, or must be retired. |

