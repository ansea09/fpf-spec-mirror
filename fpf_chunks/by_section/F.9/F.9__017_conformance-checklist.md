---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:21"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__017_conformance-checklist.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:21 — Conformance Checklist"
line_start: 82005
line_end: 82017
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:21 - Conformance Checklist

A Bridge publication conforms to F.9 iff:

1. **CC-F.9-1 - Well-typed Bridge declaration.** Every Bridge names two `SenseCells` bound to declared contexts and publishes kind, direction when needed, `CL`, Loss Notes, and admitted use.
2. **CC-F.9-2 - Substitution discipline.** Same-family substitution comes only from a substitution Bridge on the same `senseFamily`; Type-structure use requires `CL = 3` plus matched invariants.
3. **CC-F.9-3 - Interpretation embargo.** Interpretation Bridges remain Explanation-only and are not used to justify substitution or Concept-Set rows.
4. **CC-F.9-4 - CL honesty and loss visibility.** `CL <= 2` needs a counter-example or boundary case; `CL = 3` needs invariants; every Bridge has Loss Notes.
5. **CC-F.9-5 - Weakest-link row discipline.** Cross-context rows never claim a broader use or higher row-level `CL` than their Bridges admit.
6. **CC-F.9-6 - Role-boundary discipline.** Role-facing Bridges may inform RoleDescription naming or comparison, but actual `U.RoleAssignment`, required-role satisfaction, and performed-work attribution stay with A.2.1, F.6, and A.15.1.
7. **CC-F.9-7 - Registry-reference discipline.** `BridgeId` and cited policy pins are registry references, not signature-exported semantic symbols.
8. **CC-F.9-8 - Coarsened-note boundary.** A lighter note, summary, or comparison aid is not treated as a Bridge Card until the source-bearing episteme or publication needed for the Bridge Card is reopened and the Bridge is published.

