---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:23"
section_title: "Downstream Cue Export"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__024_downstream-cue-export.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:23 — Downstream Cue Export"
line_start: 44704
line_end: 44718
dependencies:
  - "A.10"
  - "A.15"
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
  - "E.10"
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
- readiness disposition: reviewable-only, `P2W-ready`, no-work or `abstain/no-change`, refresh, retire, archive, or exact-pattern application cue;
- source-set or representation relation reference when live;
- problem-formulation next-move reason and validation boundary when P2W relies on the card.

For P2W carry-through, use `E.18.1` with the accepted problem-side material and the live relation named by the card. For selector-facing readiness and candidate `TaskSignature` relation, use `C.22`. For selected-set or search cues, use `G.5` only when that relation is live. For work need, use the A.15 family only after work planning, performed work, or work-relevant source restoration is live. For any other live claim, apply the exact pattern that governs it; do not treat the whole card as carrying that claim.

