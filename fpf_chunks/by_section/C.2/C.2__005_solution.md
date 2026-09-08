---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__005_solution.md"
commit_sha: "e2457cb64712832c1652450aaa143636078c85b1"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:4 — Solution"
line_start: 41863
line_end: 41904
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
* **Reliability R.** Warrant for this exact claim and receiving use. Litmus: *what supports this conclusion, under which assumptions, and what limits it?* **R-claims MUST bind to their actual formal or empirical support.** A numerical R requires the B.3/C.2.2 meaning, scale, and model; otherwise retain separate support and a bounded reasoned conclusion. A proof under axioms needs no empirical score, and F cannot be substituted for R. Relevance windows and B.3.4 currentness rules apply where the relied-on support consumes them.

 **Congruence Level (CL), pairwise ladder.**
 `CL‑0` **Opposed/Disjoint** (contrastive; no substitution); `CL‑1` **Comparable / Naming‑only** (label similarity; no substitution); `CL‑2` **Translatable / RoleAssignment‑eligible** (structure‑preserving mapping in a declared fragment with **stated loss**; theorems may transport); `CL‑3` **Near‑identity / Type‑structure‑safe** (invariants match; type‑structure substitution allowed). *CL is a characteristic of a relation between two epistemes; it is not a fourth member of the F–G–R assurance tuple and it is not a characteristic space of its own.* **Norm:** substitution is permitted only if plane‑preserving and **CL ≥ 2**; substituting **type‑structure** requires **CL = 3**.

**Constitution and neighboring relations.** State F, G, and R for one exact claim of one C.2.1 episteme. Its exact claim content, EntityOfConcern, and effective `U.ReferenceScheme` identify the episteme through `EpistemeConstitutionRelation`. F characterizes the claim's form; G is the separate `U.ClaimScope`; R relies on exact evaluation, evidence-use, and assurance relations. Empirical grounding and edition remain separate C.2.1 relations. Viewpoint selection and view conformance remain under E.17.0; notation and other representation structure remain under C.29/A.6.3.RT; publication occurrence, form, and carrier remain under E.17/E.24.PUB. Multiple notations are allowed only when their exact representation or notation relation is explicit and any declared loss is applied to R rather than hidden in an omnibus episteme field.

#### C.2:4.2 - Four Δ‑moves (epistemic motion)

* **ΔF — Formalise.** Rewrite for stricter calculi/grammars; raise proof obligations.
* **ΔG — Generalise / Specialise.** Widen or narrow the **claim scope** (assumptions & scope). Changes to decomposition granularity are an **orthogonal view** and do not change **G** unless they alter the envelope.
* **ΔR — Calibrate / Validate.** Revise warrant through support that actually bears on the claim: proof or reasoning, calibration, severe tests, or monitoring as applicable. State what the contribution changes. A formalization alone is ΔF, not an R increase; choosing new inquiry is a separate decision.
* **ΔCL — Congrue.** Establish and record the sameness relation between **two** epistemes (ladder 0→3).
  Moves compose into **paths**. A CL chain minimum retains only the ordered congruence meaning justified by the relation family; it is not a numerical reliability loss.

#### C.2:4.3 - Composition (Γ_epist) and propagation

Let **Γ_epist** compose exact epistemes `{Eᵢ}` for one declared claim and use. B.1.3 supplies the synthesis/compilation Method; B.3 and C.2.2 govern warrant and scale discipline.

* **R (Reliability).** First distinguish indispensable premises, alternative sufficient arguments, complementary evidence, different scope slices, and counterevidence. Identify duplicated data and shared assumptions or bias. A numerical fold requires warranted input meanings, compatible scales, dependencies, and a receiving model. Neither series nor parallel syntax supplies a default minimum or maximum, and there is no universal cap at the best support line. Where no common model is justified, retain separate contributions and limitations in a bounded reasoned synthesis.
* **F (Formality).** `F(Γ) = minᵢ F(Eᵢ)` over the essential formal constituents of the claim. This is an ordinal formality statement, not an R calculation. Raise F by the actual ΔF move; neither an axiomatic mode nor a `line=formal` tag converts F into empirical warrant.
* **G (ClaimScope).** Required premises compose only on their overlapping scope. Distinct supported slices may form `SpanUnion({G_path})` under A.2.6 and C.2.2's type-before-scope rule; retain their support separately and drop unsupported regions. A new source does not by itself generalise the claim. Scope change remains an explicit ΔG± move.
* **CL (Congruence).** Keep each traversed mapping and the ordered meaning of its declared CL visible. A chain minimum is usable where that relation's congruence rule justifies it. A notation, scope-translation, kind, plane, source-local, model-use, or evidence-reuse relation contributes only its own warranted loss. A numerical Φ needs its receiving model; a monotone table or clipped output does not supply one.

For example, two necessary independent conditions with probabilities 0.9 each have conjunction probability 0.81, not minimum 0.9. Conversely, a limited complementary source need not reduce the support already available. A credible contrary result changes the affected conclusion. A theorem A ⇒ P remains valid as a formal result while evidence violating A can defeat its use as assurance of an actual system.

Γ remains defined on holons and respects the core's identity and boundary discipline. Its support account establishes neither a new action permission nor the worth of acquiring further evidence.

#### C.2:4.4 - What **must not** be conflated (normative guards)

* **Representation structure ≠ carrier.** Files, PDFs, or repositories are **carriers** outside the episteme; they never count as parts of `U.Episteme` (**see C.2.1 EP‑1; CC‑EPI‑2/3**).
* **Epistemes do not act.** Only **systems** perform Work. Epistemes carry claim content and can participate in constitution, grounding, edition, description, evidence-use, reliance, viewing, representation, and publication relations under their direct patterns.
* **CL is not a score.** It is a **qualitative ladder** of preservation classes; do not average it.

