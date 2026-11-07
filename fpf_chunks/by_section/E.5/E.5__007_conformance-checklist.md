---
chunk_kind: "child"
pattern_id: "E.5"
pattern_title: "Four Guard‑Rails of FPF"
section_id: "E.5:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5/E.5__007_conformance-checklist.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "E.5 — Four Guard‑Rails of FPF"
  - "E.5:6 — Conformance Checklist"
line_start: 96378
line_end: 96389
dependencies:
  - "E.2"
  - "E.3"
  - "E.5.1"
  - "E.5.2"
  - "E.5.3"
  - "E.5.4"
keywords:
---

### E.5:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑GR.1** | A Core pattern **SHALL** name the guard-rails whose interpretation, realization or interaction changes its design or use, and explain that relation. | Makes material rule interactions recoverable. |
| **CC‑GR.2** | Core, Tooling and Pedagogy respect GR-1 through GR-4 at their own layer: implementation and runnable teaching remain in their sources; necessary subject-defining syntax follows E.5.1 and interpretation/mapping follows E.5.2. | Preserves both portability and applicable concrete-subject rules. |
| **CC‑GR.3** | A change to a guard-rail's governing meaning **REQUIRES** an E.9 Design-Rationale Record stating the reason and Pillar impact under the E.3 precedence model. | Grounds a changed constitutional obligation while preserving E.9's ordinary editorial branch. |
| **CC‑GR.4** | The aggregate of guard‑rail rules **MUST** remain internally consistent and acyclic; no guard‑rail may override another without explicit precedence edges. | Preserves deterministic governance. |
| **CC‑GR.5** | Every Core pattern **MUST** make its primary EntityOfConcern or primary relation recoverable at first mention. Declare **CHR:ReferencePlane** (`world | concept | episteme`) when the defining rule or receiving use requires that distinction. | Preserves the intended referent and any plane-dependent interpretation. |

*All CC‑GR duties are **conceptual**. Any automated checks are **informative only** and live in Tooling/Pedagogy.*

