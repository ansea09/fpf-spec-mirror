---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:8"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__008_conformance-checklist-normative.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:8 — Conformance Checklist (normative)"
line_start: 15508
line_end: 15554
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:8 - Conformance Checklist (normative)

**CC‑A.6.4‑1 - EFEM species and EntityOfConcernChangeMode.**
Any pattern that claims to define `U.EpistemicRetargeting` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `entityOfConcernChangeMode = retarget`,
* and state the EntityOfConcern kind pair, invariant, and any grounding, scheme, scope, operating condition, describing-use viewpoint, or representation relation that constrains its applicability.

**CC-A.6.4-2 - Value-and-relation read/change discipline.**
Each species of EpistemicRetargeting **MUST**:
* list the C.2.1 values it reads or changes: at least EntityOfConcern, claim content, and effective ReferenceScheme;
* state that the exact EntityOfConcern changes and whether claim content, effective ReferenceScheme, or separately identified edition or metadata values also change;
* state explicitly how grounding behaves and, separately, how any viewpoint selected for a named describing use is preserved or changed,
* use A.6.5 SlotSpecs only when an exact reusable relation declaration is current, keeping those SlotKinds local to that `RelationSignature`.

**CC‑A.6.4‑3 - Bridge & invariant declaration.**
Each species SHALL:
* identify the relevant `KindBridge` species (and, where applicable, plane Bridges),
* declare the invariant(s) it preserves (in KD‑CAL/LOG‑CAL terms),
* sketch how invariant preservation is checked or approximated (e.g. through proofs, tests, or statistical guarantees).

**CC‑A.6.4‑4 - SquareLaw‑retargeting witnesses.**
Retargeting species that interact with `E.18` transformation-flow structures or other graph-level transformation structures **MUST**:
* describe the commutative squares (or more general diagrams) that express “evaluate then retarget = retarget then evaluate” up to equivalence,
* identify the corresponding SquareLaw‑retargeting witnesses and how they are represented as epistemes.

**CC-A.6.4-5 - Description-episteme and describing-use behaviour.**
For retargetings over `...Description` or `...Spec` epistemes:
* X and Y MUST each be identified through their exact C.2.1 claim content, EntityOfConcern, and effective scheme;
* the EntityOfConcern MUST change consistently with the declared `KindBridge`;
* every material change to grounding, effective scheme, claim scope, model-use structure, operating condition, or specification-use basis MUST be stated separately;
* when a named describing use selects a viewpoint, the source and receiving selections MUST be preserved or changed explicitly through exact references resolving exact P editions; any catalogue-family restriction bounds eligible references but does not replace the retargeting witness; and
* an F.9 Bridge is required only for an actual relation between distinct local senses. No generic context reference or universal context bridge is introduced.
**CC‑A.6.4‑6 - Separation from Viewing and Mechanisms.**
* Any species that leaves `entityOfConcernRef` unchanged is **not** a conformant EpistemicRetargeting; it belongs to `U.EpistemicViewing` (A.6.3) or another EFEM species.
* Any species that performs measurement, actuation, or another world-side effect is not an EpistemicRetargeting. Identify a mechanism and its application through A.6.1 and E.20, dated Work through A.15.1, and an actual changed referent through A.3.4 whenever those claims are current.

**CC-A.6.4-7 - Retargeting witness and reopen discipline.**
For every FPF-governed retargeting use, the source EntityOfConcern, receiving EntityOfConcern, `KindBridge`, invariant, preserved commitments, withdrawn or new commitments, admissible predicate changes, admissibility value, retargeting witness, and source-bearing reopen condition are recoverable. If bridge or invariant witnessing is insufficient for the intended use, the case records source-bearing reopen, bridge-only comparison, controlled coarsening, report-only use, exploratory use, or named neighboring-pattern handoff.

**CC-A.6.4-8 - Neighboring-pattern handoff.**
Retargeting wording carries no work authority, evidence force, assurance force, gate passage, abductive selection, temporal adequacy, dynamics law, control relation, bridge substitution, or transformation-flow path currentness unless the pattern that defines or constrains that claim and the project-side FPF kind or reference are named by value.

**CC-A.6.4-9 - StructuralReinterpretation boundary.**
When `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is used, the graph, path, constraint, and gate relations stay with `E.18`, `A.20`, or `A.21`. A.6.4 defines the retargeting conditions used for `StructuralReinterpretation`; it is not proof of `entityOfConcernRef` continuity and not an `E.18`-local retargeting kind.

