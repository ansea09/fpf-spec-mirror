---
chunk_kind: "child"
pattern_id: "C.26.1"
pattern_title: "Probe-Coupled Boundary Interaction"
section_id: "C.26.1:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.1/C.26.1__004_forces.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.26.1 — Probe-Coupled Boundary Interaction"
  - "C.26.1:3 — Forces"
line_start: 54771
line_end: 54779
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

### C.26.1:3 - Forces

| Force | Tension |
| --- | --- |
| Boundary discipline vs probe sensitivity | `A.6` and `F.9` already govern boundaries and bridges; this pattern adds only a probe-coupled reading of the state-changing or export-changing interaction. |
| Intervention vs readout | Many actions change the world ordinarily. QL is active only when the action is being used as a read, export, comparison, or optimization of the state it changes. |
| Lean use vs evidence-support class | A working team needs a small card; release, audit, or measurement claims need evidence and measurement-governing patterns or records. |
| Coupling words vs relation tokens | Words such as coupling, interaction, and export can remain local explanatory wording. A reusable name under `F.18` designates an already settled relation; use `A.6.P` when the relation or participants remain unclear. |

