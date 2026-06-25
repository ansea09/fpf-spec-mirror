---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:7"
section_title: "Capability Currentness and Lowering"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__008_capability-currentness-and-lowering.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:7 — Capability Currentness and Lowering"
line_start: 2765
line_end: 2779
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

### A.2.2:7 - Capability Currentness and Lowering

Lower or reopen a capability claim when any of these changes:

- the holder system changes composition, version, calibration, staffing, training state, toolchain, or environment;
- the envelope no longer covers the intended work slice;
- measures no longer meet the required threshold;
- the qualification window expires or becomes contested;
- evidence, source-use, test, audit, or simulation relations become stale or are reclassified;
- the method or method description changes the required capability threshold;
- the role assignment or role state changes, causing a work-admission claim to fail even though capability remains true;
- a composite holder changes dependency conditions.

Repair the smallest value that changed. A stale calibration window lowers the capability claim; it does not rewrite the role value. A failed role assignment lowers work admission; it does not by itself lower the holder's measured ability.

