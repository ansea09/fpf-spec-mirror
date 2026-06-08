---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__007_archetypal-grounding.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:5 — Archetypal Grounding"
line_start: 9381
line_end: 9395
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.6.0"
  - "C.16"
  - "E.10.D1"
  - "G.10"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:5 - Archetypal Grounding

#### A.6.1:5.1 - **U.Scope (Claim, Work, Publication) — USM as a U.Mechanism instance** (informative example)

* **Imports:** `U.ContextSliceSet`; Part F.9 **Bridge**; **C.2.1 ReferencePlane** (noted for crossings); **C.2.2 F–G–R**; **C.2.3 U.Formality**.
* **BaseType:** `U.ContextSliceSet`.
* **SliceSet:** `U.ContextSliceSet` (addressable `U.ContextSlice`s).
* **SubjectKind:** `U.Scope` with specializations `U.ClaimScope` (G), `U.WorkScope`, and `U.PublicationScope`.
* **OperationAlgebra:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.
* **LawSet:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features or characteristics, validity window, evidence class); **translate** uses declared **Bridges**; **Γ_time** is **mandatory**.
* **AdmissibilityConditions:** deterministic **“Scope covers TargetSlice”**; **fail-closed**; `unknown → {degrade, abstain}` (no implicit `unknown→0` and no implicit `unknown→false`).
* **Transport:** **Bridge-only** with **CL**; penalties are recorded in **`R_eff`**; **F and G** stay invariant; publish UTS notes.
* **Γ_timePolicy:** `point`, `window`, or `policy`; **no implicit “latest.”**
* **PlaneRegime:** *not applicable to scope sets* (scope is set-valued over `ContextSlice`, no value-plane); **CL^plane** not applicable.

