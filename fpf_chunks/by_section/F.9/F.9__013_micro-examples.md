---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:11"
section_title: "Micro-examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__013_micro-examples.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:11 — Micro-examples"
line_start: 89738
line_end: 89768
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

### F.9:11 - Micro-examples

1. **Participant versus Agent.**
   Cells: `BPMN:Participant` and `PROV:Agent`.
   Bridge: Partial-overlap, `CL = 2`.
   Loss: participation scope versus attribution scope.
   Admitted use: Naming-only label "actor"; no role assignment.

2. **Process design versus Activity occurrence.**
   Cells: `BPMN:Process` and `PROV:Activity`.
   Bridge: Design-spec-to-run-occurrence, `CL = 2`.
   Loss: model structure versus temporal occurrence.
   Admitted use: Explanation-only.

3. **Observation versus SLO fulfilment.**
   Cells: `SOSA:Observation` and `ITIL:SLO fulfilment`.
   Bridge: Measurement-evidence-for, `CL = 2`.
   Loss: sampling window and target definition.
   Admitted use: Explanation-only; direct evidence or status claim goes to A.10, B.3, F.10, or the local status pattern.

4. **Subtype across OWL and curated taxonomy.**
   Cells: `OWL:SubClassOf` and `TaxonomyX:is-a`.
   Bridge: Equivalence, `CL = 3` only when acyclicity, anti-symmetry, and class-level reasoning match.
   Admitted use: Type-structure row.

5. **Accuracy in metrology versus data quality.**
   Cells: `ISO80000:accuracy` and `ISO25024:accuracy`.
   Bridge: Partial-overlap, `CL = 2`.
   Loss: instrument perspective versus dataset perspective.
   Admitted use: Naming-only row "accuracy"; methods and measurements stay context-local.

