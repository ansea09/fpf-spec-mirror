---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:4"
section_title: "Solution (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__006_solution-normative.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:4 — Solution (normative)"
line_start: 35802
line_end: 35902
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UINDM"
  - "A.19.ULSAM"
  - "A.19.USCM"
keywords:
  - "CG-Spec.SCP"
  - "CG-Spec.Γ_fold"
  - "MinimalEvidence"
  - "fold_Γ?"
  - "lawful aggregation"
  - "scale-lawful fold"
  - "tri-state guard (pass"
  - "ΓFoldRef"
---

### A.19.ULSAM:4 - Solution (normative)

ULSAM is the **canonical scale‑aggregation mechanism** in the CHR suite. It defines:
* a stable **mechanism boundary** (`fold_Γ?` is a stage with its own operation and eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* a **tri‑state admissibility guard** (fail‑closed on missing admissibility/evidence),
* and an **audit minimum** (admitted set and membership basis, fold and policy editions, scope and window, evidence, contributors, result, and any relation actually used).

Method semantics (“which aggregation family to use”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while ULSAM remains the stable mechanism boundary.

#### A.19.ULSAM:4.1 - Operation declaration (normative)

`ULSAM.IntensionRef` cites this exact A.6.1 U.Mechanism declaration episteme. CHR resolves its fold stage to the local Fold_Γ operation. A changed argument, fold law or guard requires explicit selection of that changed declaration; another realizer of the same declaration changes no suite member.

* **Scope note:** A.6.1 governs the operation and its actual bindings below. A planned baseline selects the fold and specification editions; typed filling is conditional on an independently declared receiving position. Fold_Γ returns the aggregate and any declared contributor set. Eligibility, Audit, GateDecision/GateLog and publication retain their separate meanings.

* **IntensionHeader:** `id = ULSAM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `ULSAM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Explicit **Γ‑fold** over admitted measures — no hidden aggregation inside scoring/comparison/selection.
* **Purpose:** explicit **Γ‑fold** (and, when declared, time‑fold) over admitted measures — no hidden aggregation inside scoring/selection.
* **Imports:** `G.0 (CG‑Spec.Γ_fold, CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `A.19.CN (CN‑Spec.acceptance + aggregation routing)`, `A.6.1 (operation declarations and actual bindings)`, `B.3 (justified quantity and dependency model for any R_eff fold)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**
  * **SubjectKind:** `U.Measure`, supplied by the members of MeasureSetSlot.
  * **RangedValueKind:** `U.Measure`; Fold_Γ aggregates the admitted measures, and FoldEligibility_Γ assesses that proposed aggregation.
  * **SliceBasis:** the declared `U.ClaimScope` and selected `U.ContextSlice` members, together with the qualification window and intended result use.
  * **Input qualification:** aggregation ranges over the admitted measure set and its declared grouping or membership basis, scope and window, evidence basis, contributors, and intended result; `CNSpecSlot.acceptance` routes admission while `CG-Spec.Γ_fold` and `CG-Spec.SCP` govern admissibility.
  * Results are operation-local: aggregate, optional contributors and separate eligibility judgment.

**Operation-local argument and result declarations**

Each input is declared separately for Fold_Γ and FoldEligibility_Γ. References resolve to one exact value and edition. Cardinalities shown are for Fold_Γ; the guard may assess an incomplete proposal with 0..1 of each otherwise required input. A missing value has no argument binding and invokes the corresponding abstain condition.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | MeasureSetSlot | Set of U.Measure values offered for aggregation, with its grouping or membership basis | ByValue; 1 set |
| Argument | CNSpecSlot | CN-Spec whose acceptance conditions delimit the admitted portion, scope/window and intended aggregate use | CNSpecRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying SCP, the declared fold and default evidence conditions | CGSpecRef; 1 |
| Argument | GammaFoldSlot | ΓFold actually selected through CGSpecSlot.Γ_fold or an explicit admitted override | ΓFoldRef; 1 |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used in place of CGSpecSlot.MinimalEvidence | MinimalEvidenceRef; 0..1 |
| Fold_Γ result | AggregatedMeasureSlot | U.Measure returned by applying the effective fold to its admitted contributors | ByValue; 1 on completed admitted folding, 0 without a result |
| Fold_Γ result | ContributorSetSlot | Set of U.Measure values actually used as contributors to that aggregate | ByValue; 0..1 set, optional |
| FoldEligibility_Γ result | GuardDecision | Eligibility judgment under the predicates below: pass, degrade or abstain | ByValue; 1 on completed evaluation |

An argument's **bindingPredicate** holds when that application uses the resolved value in the row's stated role: as offered measures, acceptance/use conditions, fold/admissibility declaration or evidence override. The AggregatedMeasureSlot **bindingPredicate** holds when that Fold_Γ application returns the measure it computes using its bound effective fold and admitted contributors. The ContributorSetSlot binding holds only when the same application also returns that actual contributor set; Law 5 requires both its subset condition and equality of the aggregate to the effective fold of that subset. An omitted contributor result creates no contributor binding. The guard result binds when that FoldEligibility_Γ evaluation returns its determined judgment. A.6.1 governs binding identity and maximal continuous extent within the application, with result binding beginning at return.

**SlotIndex (derived projection).** Project the local designators, ValueKinds, designation modes and cardinalities above. Historical Slot names support CHR lookup; A.6.5 relation SlotSpecs add no operation meanings. The optional FoldTime_Γ extension is not a base operation or a prerequisite of ordinary folding.

* **OperationAlgebra** (suite stage = `fold_Γ?`, per `A.19.CHR:4.5`; canonical stage‑op = `Fold_Γ`):
  * `Fold_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → (AggregatedMeasureSlot, ContributorSetSlot?)`; the cited inputs supply the set, grouping and use qualifications.

**ApplicationPredicate.** Fold_Γ obtains when a calculation actually applies the resolved effective fold to the admitted contributors selected from the bound measure set under the bound acceptance/use conditions. It proceeds on pass or an explicitly permitted degrade branch; abstain produces no folding result. FoldEligibility_Γ obtains when an evaluation actually assesses the proposed set, fold and conditions under the guard predicates and returns its judgment. Numerical equality to a lawful fold and a passing guard alone establish neither calculation nor its result binding.

**ApplicationIdentityRule.** One Fold_Γ occurrence is one aggregation invocation at its calculation locus, from taking up the admitted operands/fold to return or termination. One FoldEligibility_Γ occurrence is one corresponding proposal-evaluation invocation. A second invocation remains distinct even when every measure, contributor, fold, policy, qualification window and returned value is equal. Several references to the same established invocation identify one application; creating another reference or copying its result creates none.

**ApplicationExtentRule.** The fold extends from actual use of its operands and rule through aggregate/contributor return or termination. The guard extends from actual proposal assessment through judgment or termination. An unfinished invocation has an open extent and no unreturned result binding. A time window qualifying the measures or an explicitly declared time-fold does not supply the occurrence interval of the calculation that processes them. Ordinary folding mathematics needs no asserted dated U.Work.

For example, two separate lawful sums of admitted 2 kg and 3 kg measurements under the same fold, grouping and policy both return 5 kg, with contributor set {2 kg, 3 kg} if requested. Law 5 holds for both contents. The first and second operand-to-return episodes nevertheless supply different aggregate/contributor bindings. A copied pair (5 kg, {2 kg, 3 kg}) is not evidence of another performed sum; two descriptions of the first sum still describe one application.

* **LawSet** (minimum; explicit, scale‑lawful folding only):
  1. **No hidden aggregation:** any Γ‑fold MUST be explicit as `Fold_Γ` (no folding hidden inside `Score/Compare/Select`).
  2. **Scale‑lawfulness:** aggregation MUST be CSLC‑lawful and admissible under `CGSpecSlot.SCP`; ordinal arithmetic (e.g., means on ordinal ranks) is forbidden unless explicitly allowed by the relevant CSLC fragment.
  3. **Γ‑fold admissibility:** `GammaFoldSlot` MUST resolve to either `CGSpecSlot.Γ_fold` or an explicitly pinned override (CAL policy) -- never an implicit "implementation default".
  4. **Evidence‑gated folding:** if evidence is insufficient/unknown, folding MUST follow tri‑state guard behavior and MUST NOT silently coerce.
  5. **Contributor accountability (when produced):** when `ContributorSetSlot?` is produced, it MUST be a subset of the admitted portion of `MeasureSetSlot`, and `AggregatedMeasureSlot` MUST be the result of applying the effective Γ‑fold to that contributor subset (no “hidden contributors”).
  6. **No implicit UNM:** ULSAM MUST NOT silently normalize/rescale to “force comparability.” If establishing a compare‑on‑invariants surface requires UNM for the measures being folded, UNM MUST appear as an explicit stage (Uses + pins) upstream; ULSAM itself remains folding‑only.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):
  * `FoldEligibility_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot` provides `SCP` and `Γ_fold`, (ii) `GammaFoldSlot` resolves to the admitted fold or an explicit override, (iii) the measure set and its grouping or membership basis are admitted by `CNSpecSlot.acceptance`, (iv) scope, window, evidence, contributors, and intended result are recoverable, and (v) the set is scale-compatible for that fold.
  * Define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`; the guard MUST evaluate evidence against `EffectiveMinimalEvidence`.
  * If evidence is missing/unknown under `EffectiveMinimalEvidence`, the guard MUST NOT return `pass` (return `degrade` or `abstain` per the effective failure behavior; record the basis in Audit).

* **Applicability:**
  * Intended to be used only when a fold is explicitly required (and never as a hidden sub‑step of scoring/comparison/selection).
  * Applicable only when `CGSpecSlot` provides the admissibility surface (`Γ_fold` and `SCP`) (fail‑closed otherwise).
  * If comparability routing is UNM-based, applicability requires the explicit upstream result and preservation/loss basis needed by the fold. A fold inherited on classes requires equivalent outputs and representative-independent availability; a requested aggregate answer must be recoverable. Otherwise retain/refine the original inputs or return the missing distinction.

* **Relation boundary:** folding creates no transfer relation. If the admitted set or receiving use relies on an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation, cite the exact obtaining relation, its direction and loss; supported penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default; time‑fold requires explicit windowing policy (if an explicit operator is needed, introduce `FoldTime_Γ` as an `⊑⁺` extension using `GammaTimeRuleSlot` from the CHR SlotKind Lexicon).
* **PlaneRegime:** each contributor and aggregated measure keeps its declared reference plane; ULSAM introduces no plane crossing. When a result depends on a relation between planes, cite that relation, its direction and loss, and keep the receiving use separate.

* **Audit:**
  * MUST record: the admitted measure set and grouping or membership basis; `CNSpecRef.edition`, `CGSpecRef.edition`, and effective `ΓFoldRef`; claim scope and selected slices, qualification window, intended result, and the aggregated measure.
  * MUST record the evidence refs used to admit the measure set and evaluate `FoldEligibility_Γ`.
  * If `GammaFoldSlot` resolves via an explicit override, SHOULD record the override’s `policy-id` (or its stable ref) alongside `ΓFoldRef`.
  * When `MinimalEvidenceSlot?` is present, MUST record `MinimalEvidenceRef`; otherwise MUST cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * When `ContributorSetSlot?` is produced, SHOULD record it (or an id reference) as an auditable explanation surface.
  * SHOULD record: any explicit UNM invocation ids/pins when folding presumes a compare‑on‑invariants surface established by UNM.
  * SHOULD record: an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation only when the fold or receiving use actually relies on that obtaining relation.
  * SHOULD record: the evaluated `GuardDecision` (especially when not `pass`) and, when applicable, the effective evidence policy / failure behavior reference used to justify `degrade|abstain`.

#### A.19.ULSAM:4.2 - Interpretation notes (didactic, informative)

- **Γ‑fold is a declared governing spec ref, not an implementation choice.** In FPF terms, “how we fold” is a **policy-level commitment**: `GammaFoldSlot` MUST be resolvable to `CGSpecSlot.Γ_fold` routing or an explicit pinned override. If you cannot cite it, you do not have a fold — you have a hidden default.
- **ULSAM is not normalization.** ULSAM does not establish comparability by itself: it does not normalize, rescale, or “align units” as a hidden convenience. If a compare‑on‑invariants surface is required, invoke UNM explicitly upstream and cite the effective pins in Audit.
- **Prefer vector semantics when possible.** If you do not strictly need one aggregated measure, keep measures separate and let `CPM` + `SelectorMechanism` operate on a partial order (set-return semantics). A fold can discard distinctions; state which distinctions the declared fold preserves and loses.
- **Contributor surfaces are not “nice-to-have” in practice.** `ContributorSetSlot?` is optional in the signature, but operationally it is the simplest way to prevent “mystery rollups” and to preserve an explanation surface.
- **Time-fold is a specialization, not a loophole.** The base ULSAM declares `Γ_timePolicy` and allows time-fold only via explicit windowing policy. If a project needs an explicit `FoldTime_Γ` operator, introduce it as an `⊑⁺` extension with no mutation of inherited operations or SlotKind drift.
  - Use the suite lexicon token `GammaTimeRuleSlot` for the additional windowing rule input; do not overload `GammaFoldSlot` or invent a generic context input to carry time semantics.

