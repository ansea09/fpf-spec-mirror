---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__005_solution.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:4 — Solution"
line_start: 41803
line_end: 41843
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

### C.2:4 - Solution

#### C.2:4.1 - Coordinates, constitution, and neighboring relations

**KD‑CAL characteristics (single‑episteme, point‑values).**

* **Formality F.** From free prose to **machine‑checkable proof/specification**. Litmus: *would a machine reject it if wrong?*
* **Claim scope (G), a set‑valued applicability over `U.ContextSlice`, with ∩/SpanUnion/translate algebra; CL penalties apply to R, not to F/G.** Litmus: *how wide is the declared scope, and under what minimal assumptions does the claim hold?*
* **Reliability R.** From untested idea to **continuously validated claim**. Litmus: *where is the last successful severe test?* **R‑claims MUST bind to evidence and declare relevance windows; stale bindings degrade R or require waiver per ESG policy.**

 **Congruence Level (CL), pairwise ladder.**
 `CL‑0` **Opposed/Disjoint** (contrastive; no substitution); `CL‑1` **Comparable / Naming‑only** (label similarity; no substitution); `CL‑2` **Translatable / RoleAssignment‑eligible** (structure‑preserving mapping in a declared fragment with **stated loss**; theorems may transport); `CL‑3` **Near‑identity / Type‑structure‑safe** (invariants match; type‑structure substitution allowed). *CL is a characteristic of a relation between two epistemes; it is not a fourth member of the F–G–R assurance tuple and it is not a characteristic space of its own.* **Norm:** substitution is permitted only if plane‑preserving and **CL ≥ 2**; substituting **type‑structure** requires **CL = 3**.

**Constitution and neighboring relations.** State F, G, and R for one exact claim of one C.2.1 episteme. Its exact claim content, EntityOfConcern, and effective `U.ReferenceScheme` identify the episteme through `EpistemeConstitutionRelation`. F characterizes the claim's form; G is the separate `U.ClaimScope`; R relies on exact evaluation, evidence-use, and assurance relations. Empirical grounding and edition remain separate C.2.1 relations. Viewpoint selection and view conformance remain under E.17.0; notation and other representation structure remain under C.29/A.6.3.RT; publication occurrence, form, and carrier remain under E.17/E.24.PUB. Multiple notations are allowed only when their exact representation or notation relation is explicit and any declared loss is applied to R rather than hidden in an omnibus episteme field.

#### C.2:4.2 - Four Δ‑moves (epistemic motion)

* **ΔF — Formalise.** Rewrite for stricter calculi/grammars; raise proof obligations.
* **ΔG — Generalise / Specialise.** Widen or narrow the **claim scope** (assumptions & scope). Changes to decomposition granularity are an **orthogonal view** and do not change **G** unless they alter the envelope.
* **ΔR — Calibrate / Validate.** Strengthen severe tests or add live monitoring; update evidence bindings.
* **ΔCL — Congrue.** Establish and record the sameness relation between **two** epistemes (ladder 0→3).
  Moves compose into **paths**; CL along a path is the **minimum** of its links.

#### C.2:4.3 - Composition (Γ\_epist) and propagation

Let **Γ\_epist** combine epistemes `{Eᵢ}` into a composite episteme **Γ** that makes a joint claim (*AND‑style*) or exposes an interface (*series composition*). KD‑CAL imposes **safe defaults**:

* **R (Reliability).** Along any justification **path** `P`, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`** (weakest‑link with congruence penalty). For **series** composition (claims needed conjunctively), the path‑wise weakest‑link applies; for **parallel** support (independent lines to the *same* claim), use **`R(Γ) = max_P R_eff(P)`** (annotate independence); never exceed the best attested line. A traversed notation, scope-translation, kind, plane, source-local, model-use, or evidence-reuse relation contributes to `CL_min(P)` only through the loss rule it actually declares.

* **F (Formality).** `F(Γ) = minᵢ F(Eᵢ)` (monotone non‑increasing along used paths). To raise **F**, apply **ΔF** to the weakest parts.
* **G (ClaimScope).** On any dependency **path**, take the **intersection** of claim scopes (the **narrowest overlapping scope**). Across **independent support paths to the same claim**, set **`G(Γ) = SpanUnion({G_path})` constrained by support** (drop unsupported regions). Widening/narrowing the scope is an explicit **ΔG±** operation.
* **CL (Congruence).** For a chain of mappings `E₀ ~ E₁ ~ … ~ Eₖ`, the **path congruence** is `min CL(Eⱼ,Eⱼ₊₁)`. Passing through a **NotationBridge** sets CL to the bridge’s declared level; the **Φ(CL)** penalty is applied in the **R** fold for any path that traverses it.

These rules keep Γ aligned with the **holonic kernel**: Γ is only defined on holons and respects identity/boundary discipline from the core.

#### C.2:4.4 - What **must not** be conflated (normative guards)

* **Representation structure ≠ carrier.** Files, PDFs, or repositories are **carriers** outside the episteme; they never count as parts of `U.Episteme` (**see C.2.1 EP‑1; CC‑EPI‑2/3**).
* **Epistemes do not act.** Only **systems** perform Work. Epistemes carry claim content and can participate in constitution, grounding, edition, description, evidence-use, reliance, viewing, representation, and publication relations under their direct patterns.
* **CL is not a score.** It is a **qualitative ladder** of preservation classes; do not average it.

