---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:8"
section_title: "Composite Capability"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__009_composite-capability.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:8 — Composite Capability"
line_start: 2816
line_end: 2831
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:8 - Composite Capability

A composite system may have a capability that none of its parts has alone. Treat the composite as the holder.

```text
Capability:
  holder: Cell_3
  canDo: place 12 PCB per minute
  envelope: feeder, vision, head, controller, and operator conditions
  measures: placement tolerance, throughput, fault rate
  qualificationWindow: current configuration and calibration window
  dependencyNotes: feeder and vision subsystem conditions
```

The capability belongs to `Cell_3`, not to every part and not to the method description. Dependencies may be named, but the whole-system capability remains a property of the composite holder.

