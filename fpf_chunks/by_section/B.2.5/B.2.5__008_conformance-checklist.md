---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__008_conformance-checklist.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:7 — Conformance Checklist"
line_start: 31615
line_end: 31626
dependencies:
  - "A.1"
  - "A.12"
  - "A.15"
  - "A.2"
  - "A.3"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
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

