---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 73192
line_end: 73206
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
  - "F.19"
keywords:
---

### E.8.ECSPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Score-sheet pattern.** | The pattern is mostly a table of values. | Move evaluated object kind, use, first evaluation use, FPF-publication boundary, and practical consequence into recognition text before the table. |
| **Checklist-as-solution.** | Users are told only what must be checked. | Put the actual evaluation method and record shape in `Solution`; let checklist rows verify it. |
| **Publication-form/content collapse.** | The FPF pattern is treated as the evaluated object being evaluated or evaluation result. | State that the pattern is a publication form for the `CharacteristicSpace`; the evaluated object and evaluation result are separate. |
| **Positive-only case bank.** | Every example passes. | Add below-floor and outside-declared-object-kind boundary cases. |
| **Related-pattern authority theft.** | The pattern claims authority over evidence, assurance, release, measurement, naming, or improvement. | Use the applicable pattern to define, constrain, or test each such claim; keep only the evaluation claim here. |
| **Rubric promotion.** | A local rubric becomes an FPF pattern because it was useful once. | Keep it local unless durable FPF reuse and evaluated-object scope are established and every outside claim names the applicable pattern and its contribution. |
| **Frozen evaluation publication form.** | The evaluated EntityOfConcern kind, use, use of a cited source, source adoption/adaptation/rejection decision, or coordinate meanings change, but the pattern keeps the old values as if still current. | Reopen `A.19.ECS` for the evaluation EntityOfConcern and state whether earlier evaluation results remain comparable, need a bridge, or must be retired. |
| **Report-shaped evaluation pattern.** | The pattern publishes coordinate names but leaves the returned result as a narrative, score list, or two-column table. | Add a result-form block: coordinate, value, short rationale, evidence basis, and coordinate-specific payload where needed. |
| **Pattern-quality report as evaluation pattern.** | `E.21` status, all-`4` or all-`5` posture, corpus projection, retrieval evidence, README, ToC, E.11, and I.2 alignment, monolith parity, landing readiness, or author or reviewer turn correspondence appears anywhere in the pattern as if it were the evaluation method. | Move that evidence to the quality, review, projection, or release carrier and keep the pattern body focused on the evaluation for the declared evaluated object kind. |
| **Apparatus-overwrapped publication form.** | The evaluation relation is written through ambiguous role, carrier, locus, flow, status, or package words that add no evaluated object kind, coordinate meaning, evidence rule, user-facing action, or exact flow position. | Apply `F.19`; if remaining content still hides a word, head, or use, apply `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines the affected object or relation. |

