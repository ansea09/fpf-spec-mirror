---
chunk_kind: "child"
pattern_id: "C.26.1"
pattern_title: "Probe-Coupled Boundary Interaction"
section_id: "C.26.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.1/C.26.1__002_problem-frame.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.26.1 — Probe-Coupled Boundary Interaction"
  - "C.26.1:1 — Problem frame"
line_start: 66007
line_end: 66026
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.6"
  - "A.6.B"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.26"
  - "C.26.2"
  - "C.26.3"
  - "F.9"
keywords:
  - "API read"
  - "bridge result"
  - "dashboard as instrument"
  - "evidence window"
  - "export loss"
  - "passive read"
  - "probe-coupled boundary"
  - "survey"
  - "workshop as state-changing interaction"
---

### C.26.1:1 - Problem frame

Use this pattern when a boundary read, meeting, metric, API read, dashboard, workshop, survey or message is used as evidence of state, and a possible effect of that interaction on the reported state could change the decision. Recover which state the output actually supports before deciding whether the read is passive, probe-coupled, or unresolved.

The useful move is to recover what the interaction read, what it changed and which state its output can support. That ordinary result can finish the use. Add QL only under the separate C.26 activation test.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, platform lead, domain modeler, or manager judging a boundary read, workshop, dashboard, metric, API read, or bridge result. |
| Boundary interaction under concern | A boundary interaction being used as evidence, export, comparison, or decision input. |
| Boundary-interaction decision use | Establish which state and time the output supports, correct a false passive-read or lossless-transfer inference, and redesign or use a neighboring method when needed. |
| Outside work | Ordinary message passing, causal intervention, API semantics or Bridge loss whose output interpretation is already adequate for the receiving use. |
| What changes in practice | The team traces how and when the output was produced and retains only the state claim that the procedure and evidence support. |

Plain glosses:
- `passive read`: treating a workshop, metric, dashboard, API read, survey, or message as if it only reports state.
- `probe-coupled`: the read/export/intervention participates in the represented state enough to change the lawful decision.
- `coupling channel`: the concrete workshop, metric, message, API, dashboard, meeting, bridge, or event stream through which the effect travels.
- `export loss`: what the carried output cannot faithfully carry into another context or decision.

