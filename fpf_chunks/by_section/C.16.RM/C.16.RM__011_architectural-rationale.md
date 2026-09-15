---
chunk_kind: "child"
pattern_id: "C.16.RM"
pattern_title: "Repair a Measurement Model or Arrangement"
section_id: "C.16.RM:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.RM/C.16.RM__011_architectural-rationale.md"
commit_sha: "368bb772285d22b29eaaf20180500f49f1a2c9d7"
heading_path:
  - "C.16.RM — Repair a Measurement Model or Arrangement"
  - "C.16.RM:10 — Architectural Rationale"
line_start: 53285
line_end: 53292
dependencies:
  - "B.5.MPC.R"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.16"
  - "C.16.IR"
  - "C.16.MR"
  - "C.28"
  - "C.29.2"
keywords:
---

### C.16.RM:10 - Architectural Rationale

Measurement joins a subject, an interaction, a mathematical relation and a calculation used to interpret an indication. The same unwanted effect can be addressed by representing it, reducing it in the arrangement or changing how the indication distinguishes the target. Keeping these alternatives together helps avoid repairing the most familiar component merely because it is familiar.

C.16.MR constructs a relation and C.16.IR determines what it resolves. This Method begins when that existing use is inadequate and chooses what to change. B.5.MPC.R supplies the wider repair across physical, mathematical and computational contributions. Here the distinction between subject and instrument, cancellation conditions, loading reduction and reinterpretation of retained observations makes that repair actionable for measurement.

The result can be epistemic, such as a corrected interpretation, or include an actual physical alteration. Its status follows the work performed and the premises available. That distinction permits a useful design calculation before equipment is changed and a useful recomputation after an implementation fault is found.

