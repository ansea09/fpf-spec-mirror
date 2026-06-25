---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__001_intro.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:intro — Intro"
line_start: 36165
line_end: 36170
dependencies:
  - "A.1"
  - "A.10"
  - "B.3"
  - "C.2.1"
  - "U.Episteme"
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

**Scope & exports.** A substrate‑neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their motion and equivalence. Exports: (i) three **point‑characteristics**—**Formality F**, **ClaimScope G**, **Reliability R**—that locate a single episteme; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ‑moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; (v) propagation laws for CL through mappings and notation bridges. KD‑CAL is typed by `U.EpistemeSlotRelation` and never confuses `ClaimGraph`, `EntityOfConcernSlot`, `GroundingHolonSlot`, `Viewpoint`, `View`, `ReferenceScheme`, notation, publication form, or carrier. All F–G–R computations are **context‑local**; Cross‑context traversals **require** an explicit **Bridge** with **CL** and apply the **B.3** congruence penalty **Φ(CL)** to **R**.  // Contexts ≡ U.BoundedContext; substitution is plane‑preserving only.

**Formality F** is the rigor characteristic defined **normatively in C.2.3**. All KD‑CAL computations and guards **SHALL** use `U.Formality` (F0…F9) as specified there; **no parallel “mode” ladders** are allowed.

