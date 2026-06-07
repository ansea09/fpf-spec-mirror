---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR‑NORM)"
section_id: "A.17:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__003_problem.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR‑NORM)"
  - "A.17:2 — Problem"
line_start: 21976
line_end: 21987
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.3"
  - "A.3.3"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.CHR-CAL"
  - "C.KD-CAL"
  - "D.3"
  - "E.10"
  - "U.Dynamics"
  - "U.PromiseContent.acceptanceSpec"
keywords:
  - "attribute"
  - "axis"
  - "characteristic"
  - "dimension"
  - "measurement"
  - "property"
---

### A.17:2 - Problem

When measurement concepts are not kept rigorously distinct, several issues arise:

-   **Polysemy at the anchor.** Teams say “dimension” or “feature” but mean slightly different things, so the very trait being measured is ambiguous.

-   **Arity mistakes.** A relational quality (e.g. similarity between two items) might be treated as if it were an intrinsic property of one item, or vice versa, leading to logical errors.

-   **Expression conflation.** The aspect being measured is often mixed up with its expression – for example, using “scale” or “axis” to mean both the quality _and_ its unit or range. This leads to **unsafe arithmetic** (averaging ordinal ranks, comparing raw numbers from incompatible scales, etc.) because values get interpreted out of context.

In summary, projects lacking a canonical terminology for metrics risk miscommunication and pseudo-quantitative operations. Measurements of physical quantities, architectural attributes, or performance scores end up on **incommensurate rails** due to inconsistent naming and handling.

