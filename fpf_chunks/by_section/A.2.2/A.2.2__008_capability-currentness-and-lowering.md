---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:7"
section_title: "Capability Currentness and Lowering"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__008_capability-currentness-and-lowering.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:7 — Capability Currentness and Lowering"
line_start: 3514
line_end: 3528
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

### A.2.2:7 - Capability Currentness and Lowering

Lower or reopen a capability instance, or lower reliance on a statement about it, when any of these changes:

- the holder system changes composition, version, calibration, staffing, training state, toolchain, or environment;
- the envelope no longer covers the intended work slice;
- measures no longer meet the required threshold;
- the qualification window expires or becomes contested;
- evidence, source-use, test, audit, or simulation relations become stale or are reclassified, lowering the support or currentness assessment rather than becoming the capability;
- the method or method description changes the required capability threshold;
- the role assignment or role state changes, causing a work-admission claim to fail even though capability remains true;
- a composite holder changes dependency conditions.

Repair the smallest object that changed. A stale calibration window lowers the capability currentness assessment and may lower reliance on the capability instance; it does not rewrite the role value. A failed role assignment lowers work admission; it does not by itself lower the holder's measured ability. A stale report lowers a statement or evidence relation before it lowers the capability instance itself.

