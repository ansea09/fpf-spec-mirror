---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:23"
section_title: "Downstream Cue Export"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__024_downstream-cue-export.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:23 — Downstream Cue Export"
line_start: 52061
line_end: 52076
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
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
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
---

### C.22.2:23 - Downstream Cue Export

`ProblemCard` exports problem-side claim content, not authority over downstream use.

The compact export contains:

- problem signal and exact signal reference;
- one joint EntityOfConcern, effective ReferenceScheme, ClaimScope, and current qualification window when needed;
- exact claim family and polarity: actual-PFR assertion, anticipated-condition claim, method-availability or solvability claim, or another named direct claim;
- improvement check or acceptance probe;
- readiness disposition: reviewable-only, `P2W-ready`, `abstainOrNoChange`, refresh, retire, archive, or subject-pattern cue;
- exact PFR, source-set, A.15.6 composite or component Work, or representation reference only when current and independently governed; and
- problem-formulation follow-up reason, validation boundary, freshness condition, and stop when the receiving use relies on them.

For P2W carry-through, use E.18.1 with the accepted problem-side distinctions. For TaskSignature constitution and assignment, use C.22. For selected-set or search use, apply G.5 only when that relation is current. For intended or performed Work, use A.15 only after its exact object is current; when the question is whether intended Work may enter its boundary, A.15.5 governs `WorkEntryReadiness@Context`. For evidence, gate, autonomy, or any other claim, apply the direct pattern; the whole card never carries that claim by itself.

