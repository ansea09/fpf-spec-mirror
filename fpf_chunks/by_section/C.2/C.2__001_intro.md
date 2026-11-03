---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__001_intro.md"
commit_sha: "d73588bdcb52ed173d7b4c1552b2ce199a548c64"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:intro — Intro"
line_start: 50952
line_end: 50963
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
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
  - "Congruence Level"
  - "F-G-R"
  - "Formality"
  - "KD-CAL"
  - "Reliability"
  - "assurance"
  - "epistemic holon composition"
  - "evidence"
  - "knowledge"
  - "provenance"
  - "trust"
---

## C.2 - Epistemic holon composition (KD-CAL)

> **Status:** Stable

**Use this when** you need to combine epistemes for a claim and intended use, or determine what an epistemic change or proposed substitution preserves.

**First useful result.** Identify the claim and intended use, and recover the contributing epistemes or the source and proposed result of the change. Establish the scope, support dependencies and preservation conditions needed for the conclusion. Return the justified synthesis or change assessment, including any unresolved condition. An adequate synthesis need not have a common numerical R. Apply the F–G–R assessment or CL substitution conditions when the receiving operation uses them. If the question is only which episteme is meant, C.2.1 can suffice; identification or publication alone does not require a KD-CAL assessment.

**Scope & exports.** A substrate-neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their change and equivalence. Exports: (i) three distinct **assessment aspects**—**Formality F**, **ClaimScope G**, **Reliability R**—for one exact claim-bearing episteme and stated use; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ-moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; and (v) propagation laws for CL through mappings and notation relations. C.2.1 identifies an episteme by its exact claim content, exact EntityOfConcern, and effective reference scheme under `EpistemeConstitutionRelation`. Empirical grounding and edition are separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; expression construction and scheme changes use A.6.3.RT.OE/A.6.3.RT; use C.29 when a question about choosing, transferring, or relying on a mathematical representation remains unresolved; publication uses E.17/E.24.PUB; a carrier remains a distinct entity. Every F–G–R computation names the exact claim and its `U.ClaimScope`. If a path changes scope, notation, kind, reference plane, source-local meaning, model-use basis, or evidence basis, it names the actual relation traversed and applies only the loss that relation declares.

**Formality F** is the assessment of expression properties governed by **C.2.3**. KD-CAL uses the properties required by the receiving operation, with any local ordered summary explicitly declared. It supplies no universal rank of languages or logics.

