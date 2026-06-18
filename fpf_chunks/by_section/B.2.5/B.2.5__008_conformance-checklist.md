---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__008_conformance-checklist.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:7 — Conformance Checklist"
line_start: 32212
line_end: 32223
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3"
  - "A.3.4"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-B2.5-1 | A conforming use names supervised holon refs and the supervisor role/transformer refs. | Prevents ghost coordination. |
| CC-B2.5-2 | A conforming use names the shared medium or publication/interaction channel that carries observations, reports, signals, constraints, or influence. | Makes the loop inspectable. |
| CC-B2.5-3 | A conforming use names both observation/report and influence/constraint sides or explicitly says the loop is not closed. | Separates closed feedback loops from one-way commands. |
| CC-B2.5-4 | A conforming use keeps structural composition, supervisory relation, and interaction/publication network distinct. | Prevents layer/part category errors. |
| CC-B2.5-5 | Stability, safety, timing, causal, evidence, assurance, gate, and mathematical-lens claims are assigned to their governing patterns. | Prevents loop-as-proof overread. |
| CC-B2.5-6 | Episteme examples name the acting systems or practices that perform review, revision, publication, or use. | Prevents episteme-agent overread. |
| CC-B2.5-7 | If a control-structure view is being claimed, the control-structure-view claim is governed by `C.30.LCA`. | Keeps relation-level feedback claims and view-level architecture claims aligned. |

