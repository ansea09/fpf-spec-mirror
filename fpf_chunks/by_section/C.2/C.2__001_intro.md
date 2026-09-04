---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__001_intro.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:intro — Intro"
line_start: 41787
line_end: 41792
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.3.RT"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "U.Episteme"
  - "U.View"
keywords:
  - "ClaimScope"
  - "F-G-R"
  - "Formality"
  - "Reliability"
  - "assurance"
  - "epistemic"
  - "evidence"
  - "knowledge"
  - "provenance"
  - "trust"
---

## C.2 - Epistemic holon composition (KD-CAL)

**Scope & exports.** A substrate-neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their change and equivalence. Exports: (i) three **point-characteristics**—**Formality F**, **ClaimScope G**, **Reliability R**—that locate one exact claim-bearing episteme for a stated use; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ-moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; and (v) propagation laws for CL through mappings and notation relations. C.2.1 identifies an episteme by its exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` under `EpistemeConstitutionRelation`. Empirical grounding and edition are separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; mathematical or diagrammatic representation uses C.29 and A.6.3.RT; publication uses E.17/E.24.PUB; a carrier remains a distinct entity. Every F–G–R computation names the exact claim and its `U.ClaimScope`. If a path changes scope, notation, kind, reference plane, source-local meaning, model-use basis, or evidence basis, it names the actual relation traversed and applies only the loss that relation declares; no generic Context, slot umbrella, or Bridge stands in for those different relations.

**Formality F** is the rigor characteristic defined **normatively in C.2.3**. All KD‑CAL computations and guards **SHALL** use `U.Formality` (F0…F9) as specified there; **no parallel “mode” ladders** are allowed.

