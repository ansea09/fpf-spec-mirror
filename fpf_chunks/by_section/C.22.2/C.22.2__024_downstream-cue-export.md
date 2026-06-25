---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:23"
section_title: "Downstream Cue Export"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__024_downstream-cue-export.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:23 — Downstream Cue Export"
line_start: 47216
line_end: 47230
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:23 - Downstream Cue Export

`ProblemCard@Context` exports problem-side material, not a claim over downstream use.

The compact export fields are:

- problem signal and context grounding;
- EntityOfConcern and scope cut when they change the move;
- improvement check or acceptance probe;
- readiness disposition: reviewable-only, `P2W-ready`, no-work or `abstainOrNoChange`, refresh, retire, archive, or governing-pattern application cue;
- source-set or representation relation reference when current;
- problem-formulation follow-up reason and validation boundary when P2W relies on the card.

For P2W carry-through, use `E.18.1` with the accepted problem-side material and the current relation named by the card. For selector-facing readiness and candidate `TaskSignature` relation, use `C.22`. For selected-set or search cues, use `G.5` only when that relation is current. For work need, use the A.15 family only after work planning, work-entry readiness, performed work, or work-relevant source restoration is current; `A.15.5` carries `WorkEntryReadiness@Context` when the downstream question is whether intended work is ready enough to enter the work boundary. For any other claim being made, apply the pattern that governs it; do not treat the whole card as carrying that claim.

