---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__006_solution.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:4 — Solution"
line_start: 35150
line_end: 35246
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:4 - Solution

Resolve the indicator policy against the exact characteristic-space basis and return the selected positions with their Characteristic, Scale and original relative order. Keep their values unchanged. If the policy is absent or an action-changing match remains unresolved, apply the declared abstain behavior. An evidence-gated policy also needs its CG-Spec and effective MinimalEvidence.

Use the operation and guard declarations below for eligibility and actual bindings. Audit keeps the selected editions and the bearer, scope/window, evidence basis and intended use needed for replay. A receiving use adds relation references only for relations it actually relies on. Gate decisions, publication and telemetry follow their own patterns; methods for choosing indicators can be supplied through G.2 and extension declarations.

#### A.19.UINDM:4.1 - Operation declaration (normative)

`UINDM.IntensionRef` cites the exact A.6.1 U.Mechanism declaration episteme presented here. CHR selects that declaration and its edition; its indicatorize stage resolves to the local Indicatorize operation. A changed basis-selection law or eligibility rule requires explicit selection of the changed declaration, while another realizer of the same declaration changes no suite member.

* **Scope note:** A.6.1 governs this declaration's operations, arguments, results, application identities and laws. An A.15.2 plan can select its editions; typed filling under A.15.3 is needed only for an independently declared receiving position. Actual application bindings are governed below. Indicatorization returns S; its guard and audit remain separate from GateDecision/GateLog.
* **IntensionHeader:** `id = UINDM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `UINDM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Policy‑bound indicatorization: select an indicator subset over an existing `U.CharacteristicSpace` under `CN‑Spec.indicator_policy`.
* **Purpose:** freeze a policy‑bound indicator subset early so downstream CHR mechanisms can assume a declared indicator profile (or explicitly `degrade/abstain`) rather than silently “choosing indicators” inside scoring/comparison/selection.
* **Imports:** `A.19.CN (CN‑Spec.indicator_policy)`, `A.6.1 (operation declarations and actual bindings)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`, and (when evidence‑gated) `G.0 (CG‑Spec.MinimalEvidence)`.
* **SubjectBlock:**

  * **SubjectKind:** `U.CharacteristicSpace`, supplied by CharacteristicSpaceSlot.
  * **RangedValueKind:** declaration-local basis positions of that space. Indicatorize selects from them; IndicatorizeEligibility assesses their selection under the policy.
  * **SliceBasis:** the declared `U.ClaimScope` and its selected `U.ContextSlice` members, together with the qualification window and intended use.
  * **Input qualification:** indicatorization ranges over the declared characteristic-space basis `CNSpecSlot.cs_basis` (within `CNSpecSlot.chart`) for the exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use; it never enlarges that basis.
  * Result kinds are declared per operation: a finite basis-position subset and a separate guard judgment.
**Operation-local declarations**

Each argument row declares the same meaning separately for Indicatorize and IndicatorizeEligibility. References identify one exact value and edition under the declaration's effective reference scheme. Cardinalities below are for Indicatorize; the guard can assess a proposal with a missing required argument, which then has no binding and yields abstain.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | CharacteristicSpaceSlot | U.CharacteristicSpace whose exact basis I supplies the candidate positions, their Characteristic and Scale | CharacteristicSpaceRef; 1 |
| Argument | CNSpecSlot | CN-Spec used to delimit that basis and the bearer, scope/slices, qualification window and intended use | CNSpecRef; 1 |
| Argument | IndicatorChoicePolicySlot | IndicatorChoicePolicy whose rules select positions in I and govern unresolved choices and evidence failure | IndicatorChoicePolicyRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying evidence conditions when the selected policy is evidence-gated | CGSpecRef; 0..1, required for evidence-gated use |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used instead of CGSpecSlot.MinimalEvidence when supplied in evidence-gated use | MinimalEvidenceRef; 0..1 |
| Indicatorize result | IndicatorSetSlot | Finite subset S of the exact space declaration's basis-position set I | ByValue; 1 on an admitted resolved selection, 0 on abstain |
| IndicatorizeEligibility result | GuardDecision | Policy-governed eligibility judgment: pass, degrade or abstain | ByValue; 1 on completed evaluation |

For each argument, its **bindingPredicate** holds when this application actually uses that resolved value in the stated role: the space supplies I, the CN-Spec delimits the use, the choice policy supplies the selection or eligibility rule, and any evidence arguments supply the effective evidence condition. An unused evidence reference in a non-evidence-gated use creates no binding. For the guard, each required argument has cardinality 0..1 so that missing inputs can be assessed; absent inputs cannot be counted as actual bindings.

The **IndicatorSetSlot bindingPredicate** holds when that Indicatorize application returns S after applying the bound policy to the bound basis under the admitted use; the laws below govern S. The **GuardDecision bindingPredicate** holds when that IndicatorizeEligibility application returns the judgment determined by its stated predicates. A compatible set or guard value copied into an audit entry establishes neither return. A.6.1 identifies each binding by the exact application, local declaration, value and continuous binding extent; input extents are within the selection/evaluation episode and result binding begins at return.

**SlotIndex (derived projection).** The argument/result designators, ValueKinds, designation modes and cardinalities in the table are its sole source. Their historical Slot names support CHR lookup; A.6.5 relation SlotSpecs do not define operation arguments.

* **OperationAlgebra** (suite stage = `indicatorize`, per `A.19.CHR:4.5`; canonical stage‑op = `Indicatorize`):

  * `Indicatorize(CharacteristicSpaceSlot, CNSpecSlot, IndicatorChoicePolicySlot, CGSpecSlot?, MinimalEvidenceSlot?) → IndicatorSetSlot`; the exact space declaration supplies I and each position's Characteristic, Scale and meaning. Resolve any policy stated by Characteristic criteria to positions before returning S. If several positions match, apply the declared choice or all-matches rule; without a resolving rule, return the policy's unresolved/abstain disposition rather than select an arbitrary position.
**ApplicationPredicate.** Indicatorize obtains when a selection episode actually resolves the bound policy against the bound space's basis positions for the CN-Spec use and determines S. It proceeds on pass, or on degrade only when that policy permits a degraded selection; abstain yields no S. IndicatorizeEligibility obtains when a separate evaluation episode assesses those inputs under the eligibility predicates and determines its GuardDecision. A planned choice or a passing guard is not an Indicatorize episode.

**ApplicationIdentityRule.** Each operation's occurrence is one selection or eligibility-evaluation invocation at its calculation locus, starting when it takes up its arguments and ending at return or termination. Two references to that same episode identify one application. Taking up the same values and policy for a second calculation identifies another, even when both return the same S or judgment. Replacing the input basis or policy for a fresh calculation likewise begins another application; a mere copied result begins none.

**ApplicationExtentRule.** Indicatorize extends from taking up the basis/policy for selection through return of S or termination without S; IndicatorizeEligibility extends from taking up the proposal for assessment through judgment or termination. An unfinished episode has an open extent and no unreturned result binding. These are the actual calculation extents, which can differ from the selected data window. An invocation reference designates that episode only when its identity is established; no U.Work claim follows from ordinary selection or projection mathematics.

For example, select Celsius temperature twice from CS7 under the same policy in §5.4. Each completed selection returns {i1}, but the two operand-to-return episodes and their result bindings are distinct. An audit record copied from the first episode can describe its result; it cannot establish a result binding for the second without the second return. Re-reading the first record also creates no new selection application.

* **LawSet** (CHR‑lawful indicatorization):

  1. **Selection‑only:** `Indicatorize` MUST NOT alter units, scales, and polarities; it only selects a subset (no implicit `UNM`).
  2. **Declared-basis restriction:** return `S⊆I` for the exact A.19 basis identified by the space and CN-Spec editions. The projection `x|_S` retains the selected positions' original relative order, Characteristic, Scale and meaning. Re-resolve the policy after a basis change; naked indices from the preceding declaration do not identify positions in the new one.
  3. **No implicit NCV⇒indicator:** measurability/NCV is not sufficient; indicators exist only via `IndicatorChoicePolicySlot` (cites `A.19.CN` `indicator_policy`).
  4. **Edition-determinism for the declared use:** for fixed editions of all **ByRef** inputs (`CharacteristicSpaceRef`, `CNSpecRef`, `IndicatorChoicePolicyRef`, and—when evidence-gated—`CGSpecRef` plus optional `MinimalEvidenceRef`) and fixed bearer, claim scope and selected slices, qualification window, evidence basis, and intended use, the `IndicatorSetSlot` result is stable.
  5. **No silent evidence coercion:** if evidence is insufficient/unknown under the chosen policy, the result MUST NOT be “silently emptied” nor silently treated as “pass”; use tri‑state guards.
* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):

  * `IndicatorizeEligibility(CharacteristicSpaceSlot, CNSpecSlot, IndicatorChoicePolicySlot, CGSpecSlot?, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CNSpecSlot.indicator_policy` is present, (ii) `IndicatorChoicePolicySlot` matches that policy reference and edition, (iii) `CharacteristicSpaceSlot` matches the declared characteristic-space basis, and (iv) that policy's eligibility conditions hold for the exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use.
  * If the chosen `IndicatorChoicePolicy` is evidence‑gated:
    (i) `CGSpecSlot` MUST be present,
    (ii) define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`,
    and (iii) insufficient/unknown evidence MUST yield `degrade` or `abstain` per the **effective** failure‑behavior policy (never a silent `pass`).
  * If the chosen `IndicatorChoicePolicy` is **not** evidence‑gated, absence of `MinimalEvidenceSlot` MUST NOT affect eligibility; no accidental “always‑evidence‑gated” behavior is permitted.
* **Applicability:**
  * Intended to be used before any scoring/comparison/selection that assumes an indicator profile, while remaining a distinct step (no hidden indicatorization inside downstream mechanisms).
  * Reuse for another bearer, source-local meaning, scope and window, evidence basis, reference plane, or intended use requires a new eligibility decision. Cite an F.9 Bridge, kind relation, or plane relation only when the new use actually relies on it.
  * Pin‑binding note: choosing concrete policy editions/pins is a planned baseline concern (P2W); UINDM only consumes those refs and records the effective ones in `Audit`.
* **Relation boundary:** indicatorization creates no transfer relation. When a receiving use relies on an obtaining F.9 Bridge, kind relation, or plane relation, cite it with direction, preserved or lost meaning, and receiving use; supported penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default (no implicit “latest”).
* **PlaneRegime:** the indicator set keeps the reference plane declared by the characteristic-space and CN-Spec editions; UINDM introduces no plane shift.
  When a receiving conclusion depends on a relation between different planes, cite that exact plane relation, its direction and loss, and keep its use separate from the indicator set.
* **Audit:**

  * MUST record: `CharacteristicSpaceRef.edition`, `CNSpecRef.edition`, `IndicatorChoicePolicyRef.edition`, exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use.
  * When evidence‑gated, MUST record: `CGSpecRef.edition` and effective MinimalEvidence (`MinimalEvidenceRef` when provided; otherwise `CGSpecSlot.MinimalEvidence`).
  * SHOULD record: the realized `GuardDecision` (`pass|degrade|abstain`) and, when non‑`pass`, the policy‑bound failure behavior reference that justified it.
  * SHOULD record: a stable description of `IndicatorSetSlot` (or an id reference to a **citable** indicator-set publication unit), plus any F.9 Bridge, kind relation, or plane relation only when the result or receiving use actually relies on it.

#### A.19.UINDM:4.2 - Interpretation notes (informative)

* **IndicatorSet selects basis positions.** A Characteristic reference can match several positions with different Scales. S identifies the selected positions in the exact space declaration; each resolves uniquely through that basis. Obtain or reuse their values under the corresponding measurement/evaluation rule and retain the position and Scale in the profile. UINDM computes no measurement or conversion.

* **Subspace views are derived, not mandatory.** If a project needs an explicit subspace view, treat it as a derived support view `CS|_S`, with `S = IndicatorSetSlot` over the exact base `CS = CharacteristicSpaceSlot`. Restrict its ordered basis and any state `x|_S` to S without reordering the retained positions. Do not add a new mandatory output to the kernel signature; model a first-class subspace support view via `⊑⁺` only when it is genuinely needed.

* **Justification is optional and externalized.** The CHR SlotKind lexicon includes `JustificationSlot`, but the canonical UINDM intension does not require it.
  If a project needs a first‑class justification output, treat it as an **extension** (`⊑⁺`) rather than by mutating the base `Indicatorize` signature,
  and model the justification as a justification `U.Episteme` (e.g., `JustificationSlot : ⟨ValueKind = U.Episteme, refMode = U.EpistemeRef⟩`).

* **Evidence-gated indicatorization is explicit.** Evidence gating is activated only by the chosen `IndicatorChoicePolicy`. In that case `CGSpecSlot` is required and the effective MinimalEvidence is explicit: use `MinimalEvidenceSlot` when supplied, otherwise `CGSpecSlot.MinimalEvidence`. The override remains optional.

