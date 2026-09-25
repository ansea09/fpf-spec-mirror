---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:8"
section_title: "Composite Capability"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__009_composite-capability.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:8 — Composite Capability"
line_start: 4327
line_end: 4343
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

### A.2.2:8 - Composite Capability

A composite system may have a capability that none of its parts has alone. Treat the composite as the holder.

```text
CapabilityStatement:
  holder: Cell_3
  canDo: place 12 PCB per minute
  envelope: feeder, vision, head, controller, and operator conditions
  measures: placement tolerance, throughput, fault rate
  actualCondition: the claimed component configuration and calibration state
  qualificationPolicy: rely on the supporting assessment only within its declared validity
  dependencyNotes: feeder and vision subsystem conditions
```

The claim is about `Cell_3`. Justify its attained bounds under the stated component and coordination conditions; component claims alone do not establish the composite's ability. A changed dependency can reopen that claim even while each component retains its own qualified ability.

