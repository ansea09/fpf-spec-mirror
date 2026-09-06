---
chunk_kind: "child"
pattern_id: "C.26.1"
pattern_title: "Probe-Coupled Boundary Interaction"
section_id: "C.26.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.1/C.26.1__002_problem-frame.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.26.1 — Probe-Coupled Boundary Interaction"
  - "C.26.1:1 — Problem frame"
line_start: 54743
line_end: 54762
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

Use this pattern when a boundary read, meeting, metric, API read, dashboard, workshop, survey, split, bridge, or message is being used as if it merely revealed or transferred state, but the probe or interaction changes the represented state enough to alter the architecture decision.

This is the main everyday entry into the QL cluster. It is useful because many teams already know how to talk about boundaries, interfaces, metrics, and workshops. The missing move is to notice when the act of reading or crossing the boundary participates in the state being read.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, platform lead, domain modeler, or manager judging a boundary read, workshop, dashboard, metric, API read, or bridge result. |
| Boundary interaction under concern | A boundary interaction being used as evidence, export, comparison, or decision input. |
| Boundary-interaction decision use | Replace false passive-read wording or unjustified lossless boundary-to-decision inference with a probe-coupled boundary decision and reroute where needed. |
| Outside work | Ordinary message passing, ordinary causal intervention, ordinary API semantics, bridge loss alone, and generic relation-token minting. |
| What changes in practice | The team records what the probe changed before using its output as architecture evidence. |

Plain glosses:
- `passive read`: treating a workshop, metric, dashboard, API read, survey, or message as if it only reports state.
- `probe-coupled`: the read/export/intervention participates in the represented state enough to change the lawful decision.
- `coupling channel`: the concrete workshop, metric, message, API, dashboard, meeting, bridge, or event stream through which the effect travels.
- `export loss`: what the carried output cannot faithfully carry into another context or decision.

