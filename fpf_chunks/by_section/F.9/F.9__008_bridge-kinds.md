---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:6"
section_title: "Bridge kinds"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__008_bridge-kinds.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:6 — Bridge kinds"
line_start: 77665
line_end: 77708
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

### F.9:6 - Bridge kinds

F.9 distinguishes substitution bridges from interpretation bridges.

#### F.9:6.1 - Substitution bridges

These relate `SenseCells` in the same `senseFamily` and may admit bounded substitution of sense.

1. **Equivalence** - near-identity of sense. Symmetric and rare.
   Use: may admit Type-structure rows only when `CL = 3` and invariants match.
   Loss Notes: none or profile-level differences, with the invariant evidence stated.

2. **Narrower-than and Broader-than** - proper inclusion of sense. Directional.
   Use: narrower-to-broader may admit Naming-only and, at `CL >= 2`, role-description naming or other same-family name reuse. Broader-to-narrower is not admitted unless a separate Bridge states it.
   Loss Notes: special cases, enforcement conditions, or local constraints that fail to carry.

3. **Partial-overlap** - non-empty intersection where neither sense includes the other.
   Use: Naming-only at best. It never admits role assignment, performed-work attribution, or Type-structure inference.
   Loss Notes: A-only sense and B-only sense.

4. **Disjoint** - explicit contrast.
   Use: contrastive explanation only.
   Loss Notes: not applicable; the claim is incompatibility.

#### F.9:6.2 - Interpretation bridges

These explain connections across `senseFamily` boundaries. They do not admit substitution or Concept-Set rows beyond local explanation.

5. **Design-spec-to-run-occurrence** - a design sense relates to a run-time occurrence sense.
   Example: `BPMN:Process` to `PROV:Activity`.
   Use: explain design-to-run correspondence.
   Loss Notes: process model versus occurrence, control structure versus temporal extent.

6. **Measurement-evidence-for** - a measurement sense evidences or quantifies another sense.
   Example: `SOSA:Observation` to `ITIL:SLO fulfilment`.
   Use: explain evaluation; direct evidence-use remains with A.10, B.3, E.17, F.10, or the local status pattern.

7. **Policy-constraint-on** - a policy or deontic sense constrains another sense.
   Example: `ODRL:Duty` to service behavior.
   Use: explain a constraint relation; direct policy, gate, or authority claims remain with the governing pattern.

8. **Viewpoint-correspondence** - one view, report, model, dashboard, or viewpoint-bound episteme corresponds to another view over an EntityOfConcern.
   Use: explain cross-view comparison; direct architecture-description, episteme, publication, or source-use claims remain with their governing patterns.

