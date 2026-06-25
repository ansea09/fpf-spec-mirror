---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:8"
section_title: "Integration with Role-State Relation and Dynamics (Normative and Clarifying)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__011_integration-with-role-state-relation-and-dynamics-normative-and-clarifying.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:8 — Integration with Role-State Relation and Dynamics (Normative and Clarifying)"
line_start: 43043
line_end: 43054
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:8 - Integration with Role-State Relation and Dynamics (Normative and Clarifying)

#### C.16:8.1 - `RoleStateRelation@BoundedContext` touch-points

MM‑CHR **supplies recognisers** used in **State Checklists**. A checklist criterion **may** refer to a measure (e.g., “Cohesion ≥ T on ordinal ladder”), but the **state itself remains the EntityOfConcern of the checklist**; the checklist is its **description**, and a **StateAssertion** is an evidence‑backed verdict over a Window. No lifecycle language is implied. When a graph or state-machine lens is used, it describes the role-state relation; it is not the relation in life.

**Rule RSR‑M1.** When a checklist cites a measure, it **SHALL** do so by **Characteristic + Scale semantics** (and unit if applicable), not by colloquial aliases; Tech and Formal registers apply. **Rule RSR‑M2.** Thresholds in checklists **MUST** respect the scale type (no ratio talk on interval scales; no arithmetic on ordinal ladders).

#### C.16:8.2 - Dynamics & CharacteristicSpace

`U.Dynamics.stateSpace` is a **CharacteristicSpace**—a named set of Characteristics with units and topology. MM‑CHR provides the **measurement side** of that space; patterns specify the **transition law**. Architectural or epistemic **dynamics** are then *trajectories in the declared CharacteristicSpace*. **No** procedural or storage commitments are implied.

