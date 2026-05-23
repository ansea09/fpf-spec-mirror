---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:20"
section_title: "Conformance Checklist (CC-F.9)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__022_conformance-checklist-cc-f-9.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:20 — Conformance Checklist (CC-F.9)"
line_start: 64598
line_end: 64619
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
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

### F.9:20 - Conformance Checklist (CC-F.9)

A Bridge publication conforms to F.9 iff:

1. **CC-F.9-1 - Well-typed Bridge declaration.**
   Every Bridge names two SenseCells bound to declared Contexts and publishes kind, direction (if needed), `CL`, Loss Notes, and Bridge-supported use.
2. **CC-F.9-2 - Substitution discipline.**
   Any substitution or row support comes only from a Substitution Bridge on the same `senseFamily`; Role Assignment & Enactment-level substitution requires `CL >= 2`, and Type-structure substitution requires `CL = 3` plus matched invariants.
3. **CC-F.9-3 - Interpretation embargo.**
   Interpretation Bridges remain explanation-only and are not used to justify substitution or Concept-Set rows.
4. **CC-F.9-4 - CL honesty and loss visibility.**
   Bridges with `CL <= 2` publish a counter-example or explicit boundary case; Bridges with `CL = 3` publish the invariants that justify the higher-scope use; all Bridges publish Loss Notes.
5. **CC-F.9-5 - Weakest-link row discipline.**
   Cross-context rows never claim a broader scope or higher row-level `CL` than the participating Bridges support.
6. **CC-F.9-6 - Overlay non-collapse.**
   If a `F.9.1` Bridge Stance Overlay is used, it remains an annotation and does not replace bridge kind, direction, `CL`, or Loss Notes.
7. **CC-F.9-7 - Registry-reference discipline.**
   `BridgeId` and cited policy pins are treated as registry references, not as signature-exported semantic symbols.

8. **CC-F.9-8 - Coarsened cross-context note is not treated as a Bridge Card.**
   If bridge-bearing reuse begins from a lighter note, summary, or comparison aid, the source-bearing episteme or source publication needed for bridge support is reopened and a full Bridge Card is published before any equivalence, substitution, `Naming-only` row, interoperability, or other row support is claimed.

