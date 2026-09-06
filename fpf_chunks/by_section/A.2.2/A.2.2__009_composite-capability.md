---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:8"
section_title: "Composite Capability"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__009_composite-capability.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:8 — Composite Capability"
line_start: 4044
line_end: 4059
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:8 - Composite Capability

A composite system may have a capability that none of its parts has alone. Treat the composite as the holder.

```text
ConcreteCapabilityInstance:
  holder: Cell_3
  canDo: place 12 PCB per minute
  envelope: feeder, vision, head, controller, and operator conditions
  measures: placement tolerance, throughput, fault rate
  qualificationWindow: current configuration and calibration window
  dependencyNotes: feeder and vision subsystem conditions
```

The concrete capability instance is asserted for `Cell_3`, not for every part. Dependencies may be named, but the bounded capability claim is about the composite holder.

