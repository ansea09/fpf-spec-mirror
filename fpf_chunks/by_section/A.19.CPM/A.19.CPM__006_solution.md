---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__006_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:4 — Solution"
line_start: 32831
line_end: 32954
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass"
---

### A.19.CPM:4 - Solution

CPM is specified as a canonical `U.Mechanism.Intension` whose core commitments are:

* **Comparator admissibility is declared and gated** (`CG-Spec.ComparatorSet`, and `CG-Spec.SCP` when numeric operations are involved; scale admissibility via CSLC).
* **Results are set‑valued relation or poset tokens**; partial orders remain partial; no silent scalarization or totalization.
* **Admissibility is tri‑state and fail‑closed** on missing admissibility and evidence; unknown never coerces into a fabricated outcome.
* **Comparison remains distinct from selection**; CPM produces relation outcomes; `SelectorMechanism` consumes them.

This pattern defines (governing-pattern, wiring‑friendly):
1. a **stable mechanism boundary** for admissible comparison: `Compare(...) → ComparisonResultSlot` plus a tri‑state `CompareEligibility` guard;
2. a **stable SlotKind field set** (by suite lexicon tokens) that downstream selection and Part‑G wiring can rely on without SlotKind drift;
3. an **admissibility and evidence responsibility split**: admissibility is gated by `CG-Spec` (and CSLC), while admission and comparability relations are cited from `CN-Spec`;
4. a minimal **replay basis**: dated comparison work, the effective refs and editions bound in the actual `Compare` operation application, its `ComparisonResultSlot` binding, and the A.10 evidence-provenance path needed to replay the comparison;
5. explicit **planned-filling separation**: `SlotFillingsPlanItem` rows carry planned edition and policy fillings; dated comparison `U.Work` remains the occurrence, the actual operation application carries argument and result bindings, and A.10 supplies the evidence-provenance path;
6. an explicit **comparison-use boundary**: claim scope, selected A.2.6 context slices, optional A.19 predicate, reference plane, and evaluation window are occurrence bindings, not generic context, comparator content, output fields, or an optional model-use structure.

#### A.19.CPM:4.1 - Mechanism.Intension (canonical; normative)

This is the canonical `U.Mechanism.Intension` for `CPM.IntensionRef`. It is intended to be cited by CHR suite publications and by any wiring layers.

* **Declaration boundary:** this A.6.1 mechanism intension declares `Compare` and `CompareEligibility`; it does not publish telemetry or create dated work, an actual operation application, comparison scope, result episteme, evidence use, provenance path, currentness relation, or publication relation. Each neighboring object or relation uses its direct governor.
  * **Planned slot fillings:** this intension does not fill project-specific slots for editions, policy ids, bridge ids, or similar pins. Planned fillers live in `SlotFillingsPlanItem` rows (A.15.3 plus `A.19.CHR:4.7.2`); dated comparison `U.Work` binds effective values as occurrence parameters.

* **IntensionHeader:** `id = CPM`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `CPM.IntensionRef` designates this `U.Mechanism` episteme as the canonical suite member named in `A.19.CHR:4.2`; it is not the `EntityOfConcernRef` of the declared operation family.

* **SignatureManifest (optional; importability):** if a CPM publication is intended for reuse beyond the CHR suite, author SHOULD publish a `SignatureManifest` that records (i) the declared `Compare` stage‑op signature, (ii) the SlotKind field set (by lexicon tokens), and (iii) the explicit set‑valued output commitment (no silent scalarization or totalization).

* **Tell.** Lawful comparison producing **set‑valued** parity or poset outcomes (not a single scalar).

* **Purpose:** admissible comparison producing **set‑valued** parity or poset outcomes (not a single scalar).

* **Imports:** `G.0 (CG‑Spec.ComparatorSet, CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `A.19.CN (comparability and admission declarations)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **EntityOfConcernRef:** the comparison operation family declared by `Compare` and `CompareEligibility` in this section.

* **Effective `U.ReferenceScheme`:** the CHR suite reference scheme in which the A.19.CHR SlotKind lexicon, CN-Spec, CG-Spec, and ComparatorSpec tokens are interpreted.

* **Direct signature components:**

  * **SubjectKind:** `Comparison`.
  * **RangedValueKind:** CHR-typed profile values in a CG-Frame (see `CG-Spec.ComparatorSet`).
  * **ResultKind:** `U.Set` of relation or poset tokens; the comparison result is set-valued by default.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** comparison ranges over admitted left and right profiles in one exact `U.ClaimScope`; selected `U.ContextSlice` values are members of that scope under A.2.6 and do not create a duplicate membership relation.

  These are direct A.6.0 declaration components. They do not form an additional comparison-content container, and they do not absorb comparator admission, evaluation, evidence-use, or replay relations.

* **SlotIndex** (derived projection from `SlotSpecs` and guard SlotSpecs; uses `A.19.CHR:4.2.1` SlotKind tokens; no independent semantics):

  * `LeftProfileSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `RightProfileSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`,
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`,
  * `ComparatorSpecSlot : ⟨ValueKind = ComparatorSpec, refMode = ComparatorSpecRef⟩`,
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` (optional override; otherwise cite `CGSpecSlot.MinimalEvidence`),
  * `ComparisonResultSlot : ⟨ValueKind = U.Set (relation or poset tokens), refMode = ByValue⟩`.

* **OperationAlgebra** (suite stage = `compare`, per `A.19.CHR:4.5`; canonical stage‑op = `Compare`):

  * `Compare(LeftProfileSlot, RightProfileSlot, CNSpecSlot, CGSpecSlot, ComparatorSpecSlot, MinimalEvidenceSlot?) → ComparisonResultSlot`.

* **Comparison-use bindings for each actual application** (required A.6.1 occurrence arguments; not CHR SlotKinds and not another container kind):

  * exact `U.ClaimScope` for the admitted profile pair and comparison claim;
  * selected `U.ContextSlice` members of that scope under A.2.6, without copying its membership relation;
  * optional by-value A.19 `CharacteristicSpacePredicate`, explicitly absent when comparison does not depend on one;
  * effective `U.ReferenceScheme` and reference plane; and
  * explicit comparison-evaluation point or interval.

  Together the profile pair and these bindings delimit the comparison scope. They do not form another U-kind, generic context input, model-use-structure field, or replay record. The comparator remains the separately declared `ComparatorSpecSlot`; evidence use retains its own A.2.4 claim scope and relevance window.

* **LawSet** (minimum; set-valued comparison, no hidden scalarization):

  1. **ComparatorSet gate:** `ComparatorSpecSlot` MUST be an element of `CGSpecSlot.ComparatorSet` (admissibility gate; cite `G.0`).
  2. **Set‑valued semantics:** `ComparisonResultSlot` is set‑valued (parity or poset tokens); partial orders remain partial — no silent totalization or scalarization.
  3. **CSLC+SCP admissibility:** any numeric ops implied by the comparator MUST be admissible under `CGSpecSlot.SCP` and CSLC-admissible (cite `G.0` + `A.18`).
  4. **Unknown is not coerced:** missing or unknown evidence MUST NOT be mapped to a comparison outcome; use tri‑state guards.
  5. **No hidden thresholds or tie-breakers:** any thresholds, epsilons, priority orders, or tie-break logic MUST live in the declared `ComparatorSpecSlot`, or in `CNSpecSlot.acceptance` as explicit acceptance clauses, and be edition-pinned for replay; CPM MUST NOT smuggle constants.
  6. **No implicit UNM:** CPM does not normalize or align internally. Normalization-based comparability requires already-normalized inputs plus exact upstream normalization refs; otherwise eligibility is `degrade` or `abstain`.
  7. **No silent boundary change:** a `Compare` application does not silently change its profile pair, `U.ClaimScope`, selected context slices, optional A.19 predicate, comparator, reference scheme or plane, or evaluation window. A changed binding is a different application and requires a newly evaluated outcome.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility and evidence):

  * `CompareEligibility(LeftProfileSlot, RightProfileSlot, CNSpecSlot, CGSpecSlot, ComparatorSpecSlot, MinimalEvidenceSlot?; comparison-use bindings) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) comparator admission; (ii) scale-admissible operations; (iii) admitted and comparable profiles under the exact claim scope and selected A.2.6 context slices; (iv) an explicit evaluation point or interval and reference plane; (v) the same by-value A.19 predicate when one is used; and (vi) satisfaction of the effective MinimalEvidence policy.
  * If `CNSpecSlot.comparability` is normalization‑based (compare‑on‑invariants), `pass` additionally requires that the inputs are already in the required invariant and normalization regime; CPM MUST NOT “make them comparable” by silent normalization.
  * If `MinimalEvidenceSlot` is absent, the guard MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` (by explicit rule), and MUST NOT return `pass` when evidence is missing or unknown **or** fails the effective MinimalEvidence gate.

* **Applicability:**

  * Intended for the CHR stage `compare`: it may follow indicatorization or scoring and optional folding when those stages are present, and it precedes selection wherever selection occurs. It remains distinct from selection.
  * Applicable only when `CGSpecSlot` supplies the current admissibility and evidence-policy declarations. Missing declarations fail closed.
  * Inside the CHR suite, `A.19.CHR:4.5` alone determines stage ordering and optionality; CPM does not infer order from `mechanisms[]`.
  * Every actual comparison binds one exact `U.ClaimScope`, selected A.2.6 `U.ContextSlice` members, optional A.19 predicate, effective reference plane, and explicit evaluation point or interval. There is no implicit latest value and no default window inherited from the predicate.
  * Cross-reference-scheme or cross-plane use requires an explicit F.9 Bridge. The Bridge does not supply claim scope, selected slices, predicate, comparator, or evaluation time.

* **Neighboring bridge relation:**

  When the two profiles require interpretation across reference schemes or planes, state the F.9 bridge relation separately. Name its exact endpoints, preserved and lost comparison meaning, applicable use, CL value, and any `R_eff` penalty. Adding or changing that bridge does not by itself change the CPM declaration.

* **Neighboring dated work, operation application, result binding, and evidence relations:**

  A dated comparison run is `A.15.1 U.Work`. Its actual A.6.1 `Compare` application binds the profile pair, comparator, comparison-use arguments, policies, and set-valued `ComparisonResultSlot`. A.2.4 separately governs evidence use with its own evidence claim scope and relevance window; A.10 governs provenance; G.11 governs source or assertion-edition currentness. A durable result episteme, when needed, is governed by C.2.1, and any current entity-identity inception claim by A.15.PROD. No universal work-result or comparison-result relation is presumed. To replay the comparison, recover:

  * the two profile values or exact upstream refs, one `U.ClaimScope`, selected A.2.6 context slices, optional A.19 predicate, effective reference scheme and plane, and evaluation point or interval;
  * `CNSpecRef.edition`, `CGSpecRef.edition`, and the effective `ComparatorSpecRef`;
  * the effective MinimalEvidence policy, either the explicit override or `CGSpecSlot.MinimalEvidence`;
  * the realized `GuardDecision` and, for `degrade` or `abstain`, any current downstream-handling policy;
  * the effective upstream normalization dependency, or the explicit absence that caused degradation or abstention;
  * the comparison result and any bridge, CL, and ReferencePlane refs used by this occurrence.

  Use G.9 when a parity or benchmark use requires a stable run package and report record. These neighboring records support replay; none is CPM declaration content.

#### A.19.CPM:4.2 - Interpretation notes — informative

* **The output is a value, not a replay container.** The by-value set bound to `ComparisonResultSlot` contains relation or poset tokens only. Comparator, scope, predicate, plane, window, eligibility, evidence use, provenance, and currentness remain separate bindings or relations.
* **Set-valued output is the default, not a loophole.** “Set‑valued” means CPM preserves incomparability, ties, and partiality as first‑class outcomes; it does not authorize silent post‑processing into a scalar or a single winner.
* **Total orders are allowed only if declared by the comparator.** If a `ComparatorSpec` defines a total order, CPM still outputs a (singleton) set of relation tokens; the totalization is a property of the declared comparator, not an implicit kernel default.
* **Normalization is not smuggled into comparison.** If `CN‑Spec.comparability` declares normalization‑based invariants for comparison, that dependence must be represented explicitly via the suite protocol and, where needed, explicit Uses contours (CPM consumes admitted profiles; it does not silently normalize them).
* **Thresholds and tie-breakers are never kernel constants.** If thresholds exist, they belong to explicit policies or specs such as `ComparatorSpec` and `AcceptanceClauses`, are edition-pinned, and are recorded by the dated comparison occurrence for replay.

