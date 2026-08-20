---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__006_solution.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:4 — Solution"
line_start: 33121
line_end: 33261
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:4 - Solution

`SelectorMechanism` is the canonical **selection kernel** for CHR and for selector specializations. It provides:

* a stable mechanism boundary for `select`,
* a stable SlotKind field set (via the CHR lexicon),
* a minimum law set that preserves set‑valued semantics and forbids hidden thresholds and hidden scalarization,
* a tri‑state admissibility guard that is fail‑closed under missing admissibility or evidence,
* a replay basis that separates effective occurrence bindings, the selected-set result, and supporting evidence from reusable selector semantics;
* an explicit selection-use boundary that keeps candidate universe, the finite upstream comparison-application basis and required coverage, the derived token union, selection conditions, scope, predicate basis, plane, and window distinct; and
* output discipline: `SelectionSlot` contains only the selected candidate set, while eligibility, evidence use, provenance, currentness, result epistemes, and publications remain separate.

Method semantics and SoTA algorithm families do not live inside the kernel: they connect via `G.2` SoTA packs and wiring modules, and via admissible specializations `⊑` and `⊑⁺` that obey the specialisation-chain discipline (`A.6.1:4.2.1`).

#### A.19.SelectorMechanism:4.1 - Mechanism.Intension — normative core

Archetypal Grounding — **Mechanism.Intension** (normative).

* **Declaration boundary:** this A.6.1 intension declares `Select` and `SelectEligibility`; it does not bind project-specific pins or create selection scope, dated work, an actual operation application, gate decision, selected-set episteme, evidence use, provenance path, currentness relation, or publication relation. Each neighboring object or relation uses its direct governor.
* **Canonicality note:** this is the canonical `U.Mechanism.Intension` for `SelectorMechanism.IntensionRef` and is intended to be cited by CHR suite publications and by any wiring layers; other mentions are **Tell + Cite** only.

* **IntensionHeader:** `id = SelectorMechanism`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `SelectorMechanism.IntensionRef` designates this `U.Mechanism` episteme as the canonical suite member named in `A.19.CHR:4.2`; it is not the `EntityOfConcernRef` of the declared operation family.

* **Tell.** Universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Purpose:** universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Imports:** `A.6.1:4.2.1 (specialisation relation chains)`, `A.6.5 (slot discipline; SlotIndex as projection)`, `A.19.CN (CN‑Spec governance card)`, `C.22 (TaskSignature as a policy-reference artifact when used)`, `G.5 (selector conformance and default selection policy)`, `G.0 (CG‑Spec admissibility and evidence gates)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **EntityOfConcernRef:** the selection operation family declared by `Select` and `SelectEligibility` in this section.

* **Effective `U.ReferenceScheme`:** the CHR suite reference scheme in which the A.19.CHR SlotKind lexicon, CN-Spec, CG-Spec, and any current TaskSignature tokens are interpreted.

* **Direct signature components:**

  * **SubjectKind:** `Selection`.
  * **RangedValueKind:** pair of values `<admitted candidate set, relation or poset token set over the same candidate universe>`.
  * **ResultKind:** `U.Set` of selected candidate values.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** selection ranges over one admitted candidate set and the exact union of justified relation or poset tokens from a finite basis of binary CPM applications whose pair endpoints lie in that candidate set and whose coverage satisfies the explicit selection conditions, all in one exact `U.ClaimScope`; selected `U.ContextSlice` values are members of that scope under A.2.6 and do not create duplicate membership.

  These are direct A.6.0 declaration components. They do not form another selector-content container, and they do not absorb candidate admission, comparison work, dated selection work, result, evidence-provenance, or replay relations.
* **SlotIndex:** derived projection from `SlotSpecs` (and any guard‑only SlotSpecs) per slot discipline; uses `A.19.CHR:4.2.1` SlotKind tokens; has no independent semantics.

  * `CandidateSetSlot : ⟨ValueKind = U.Set (candidates), refMode = ByValue⟩`.
  * `ComparisonResultSlot : ⟨ValueKind = U.Set (relation or poset tokens), refMode = ByValue⟩`.
  * `CriteriaSlot : ⟨ValueKind = U.Set (selection criteria or clauses, including explicit tie‑breakers; **acceptance thresholds are not criteria** and remain governed by the cited acceptance declarations and applied only via `SelectEligibility`), refMode = ByValue⟩`.
  * `TaskSignatureSlot? : ⟨ValueKind = TaskSignature, refMode = TaskSignatureRef⟩` optional; when present, SHOULD be the single policy-default slot or ref for selector defaults (e.g., `PortfolioMode` or dominance regime), but it does not replace `CNSpecSlot` or `CGSpecSlot` governing spec refs.
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`.
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`.
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` optional override; otherwise the effective evidence policy is `CGSpecSlot.MinimalEvidence`.
  * `SelectionSlot : ⟨ValueKind = U.Set (selected set), refMode = ByValue⟩`.

* **OperationAlgebra** suite stage = `select`, per `A.19.CHR:4.5`; canonical stage op = `Select`

  * `Select(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, TaskSignatureSlot?, MinimalEvidenceSlot?) → SelectionSlot`.

  For an actual n-candidate use, the `ComparisonResultSlot` argument is the exact set-union of justified tokens from the finite basis members' own CPM output bindings. It carries no application reference, pair, eligibility value, scope, or replay metadata; those remain separate selection-use bindings. A CPM `abstain` with no output binding contributes no token.

* **Selection-use bindings for each actual application** (required A.6.1 occurrence arguments; not CHR SlotKinds and not another container kind):

  * one finite by-value comparison-application basis whose every member identifies an exact actual binary CPM `Compare` application, its exact left/right pair, realized `GuardDecision`, and its own `ComparisonResultSlot` binding when one was produced;
  * the finite set of required binary comparisons derived from the candidate universe, `CriteriaSlot`, and effective selector policy, including pair direction or comparator distinction when it changes the selection condition; every required comparison is discharged by an exact basis member, and every candidate excluded under `degrade` is named by the bound failure behavior;
  * a trace from every token in the Selector's `ComparisonResultSlot` argument to the basis member output binding that produced it; no missing pair, empty output, or `abstain` may be converted into a relation token;
  * one exact `U.ClaimScope` for the candidate universe and selection use;
  * selected `U.ContextSlice` members under A.2.6, without copying membership;
  * the same by-value A.19 `CharacteristicSpacePredicate` basis used by the relevant basis members or an explicit `none` when no predicate governs the use;
  * effective `U.ReferenceScheme` and reference plane;
  * explicit selection-evaluation point or interval; and
  * effective selection conditions: the by-value `CriteriaSlot`, current selector policy and defaults, and explicit failure behavior for `degrade`.

  The comparison-application basis is an occurrence binding and replay projection, not a new U-kind, SlotKind, relation, result container, batch CPM application, generic context input, model-use-structure field, or replay record. Acceptance and admission predicates remain with their direct declarations. Evidence use retains its own A.2.4 claim scope and relevance window.

* **LawSet** (minimum): the selection kernel is set-returning and policy-bound

  1. **Set‑returning by default:** a conformant `Select` MUST return a declared selected set by default. It MUST NOT silently collapse partial orders or incomparabilities to a single winner; if a singleton outcome is required, it MUST be an explicit criterion (or a declared upstream total order).
  2. **No hidden thresholds or constants:** a conformant publication MUST NOT smuggle thresholds, weights, dominance rules, or tie‑breakers. Selection‑level commitments MUST be explicit in `CriteriaSlot` and, where needed, in explicit policy defaults exposed through `TaskSignatureSlot`. Admissibility and acceptance thresholds are applied only via `SelectEligibility` using `CNSpecSlot.acceptance` and the effective evidence policy (`MinimalEvidenceSlot?` or `CGSpecSlot.MinimalEvidence`).
  3. **No hidden scalarization or token aggregation by assertion:** a conformant publication MUST consume `ComparisonResultSlot` as the exact union of the finite basis members' justified set-valued or partial outputs. Every consumed token MUST be traceable to at least one exact producing CPM application. Scalar summaries or relation tokens inferred from a missing pair, empty output, `degrade`, or `abstain` are forbidden; scalar summaries, if produced at all, are report-only unless explicitly promoted by policy outside suite closure.
  4. **Evidence gating is explicit:** when selection depends on evidence, it MUST cite either `MinimalEvidenceSlot` or the effective `CGSpecSlot.MinimalEvidence` policy and evaluate selection with the tri-state predicate. Candidate-level ineligibility handling MUST be explicit in current criteria or upstream results and recorded by the dated selection occurrence; the kernel MUST NOT invent evidence thresholds.
  5. **No competing defaults:** effective `PortfolioMode`, dominance regime, and other defaults come from declared policy refs and are bound by the actual application.
  6. **No silent boundary change:** `Select` does not silently change candidate universe, comparison-application basis membership, required comparison coverage, any member's pair, eligibility or output binding, selection conditions, A.19 predicate basis, claim scope, selected context slices, reference scheme or plane, or evaluation window. A changed binding is another selection application and may require new binary comparisons.
  7. **Guard-output separation:** `GuardDecision` is not a selected-set member. On `abstain`, no `SelectionSlot` value is fabricated. A `degrade` eligibility value permits a reduced set only under the explicitly bound failure behavior and criteria.

* **AdmissibilityConditions** (tri-state guard; fail-closed on missing admissibility, comparison coverage, token provenance, or evidence)

  * `SelectEligibility(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, TaskSignatureSlot?, MinimalEvidenceSlot?; selection-use bindings) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) every basis member's exact pair lies inside `CandidateSetSlot`; (ii) the basis covers every binary comparison required by the candidate universe and explicit selection conditions; (iii) every consumed relation token traces to a member's own output binding; (iv) explicit selection conditions and tie-breakers; (v) compatible A.19 predicate basis, claim scope, selected A.2.6 context slices, reference plane, and evaluation window across the basis and selection; (vi) coherent CN-Spec and CG-Spec editions; and (vii) satisfied admission, acceptance, and effective MinimalEvidence predicates under their direct owners.
  * If `MinimalEvidenceSlot` is absent, `SelectEligibility` MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` by explicit rule, and missing or unknown evidence MUST NOT yield `pass`.
  * A basis member with `GuardDecision = degrade` may support a reduced set only when a current selector policy names the exact candidate-level failure behavior and the remaining basis still covers the comparisons required for that reduced use. The actual selection application binds that policy and its own realized eligibility value.
  * A missing required comparison, untraceable token, or required basis member with `GuardDecision = abstain` makes `SelectEligibility = abstain`; selection does not proceed and no selected-set output is created.

* **Applicability:**

  * Intended for the CHR `select` stage after the required finite set of admissible binary comparisons and produces a selected-set value. Selection remains distinct from comparison, acceptance, gate decision, publication, and telemetry.
  * Applicable only when `CNSpecSlot`, `CGSpecSlot`, explicit criteria, the effective evidence policy, and a finite comparison-application basis with complete required coverage and token provenance are current for the candidate universe. Missing declarations or coverage fail closed.
  * Inside the CHR suite, `A.19.CHR:4.5` alone determines stage ordering and optionality.
  * Every actual selection binds one exact `U.ClaimScope`, selected A.2.6 `U.ContextSlice` members, the finite basis of exact binary CPM applications and their pair, eligibility, and output bindings, the derived token union, A.19 predicate basis, effective reference plane, selection conditions, and explicit evaluation point or interval. There is no implicit latest value and no default window inherited from the predicate or comparison label.
  * Cross-reference-scheme or cross-plane use requires an explicit F.9 Bridge. The Bridge does not supply candidate universe, comparison-application basis or coverage, relation tokens, selection conditions, scope, predicate, or time.

* **Neighboring bridge relation:**

  When candidates or comparison tokens require interpretation across reference schemes or planes, state the F.9 bridge relation separately. Name its exact endpoints, preserved and lost selection meaning, applicable use, CL value, and any `R_eff` penalty. Adding or changing that bridge does not by itself change the selector declaration.

* **Neighboring dated work, operation application, result binding, and evidence relations:**

  A dated selection run is `A.15.1 U.Work`. Its actual A.6.1 `Select` application binds the candidate set, finite comparison-application basis, required coverage, derived token union, selection-use arguments, policies, and selected-set `SelectionSlot`. A.2.4 separately governs evidence use with its own claim scope and relevance window; A.10 governs provenance; G.11 governs source or assertion-edition currentness. A durable selected-set episteme, when needed, is governed by C.2.1, and any current entity-identity inception claim by A.15.PROD. No universal work-result, comparison-result, or selection-result relation is presumed. To replay the selection, recover:

  * the candidate set and required binary comparisons; for every basis member, the exact CPM application, pair, realized `GuardDecision`, and its own output binding or explicit absence; and the trace from every consumed token to its producing member;
  * one `U.ClaimScope`, selected A.2.6 context slices, A.19 predicate basis, effective reference scheme and plane, and evaluation point or interval shared as required by the selection conditions;
  * `CNSpecRef.edition`, `CGSpecRef.edition`, and `TaskSignatureRef.edition` when TaskSignature is used;
  * the effective MinimalEvidence policy, either the explicit override or `CGSpecSlot.MinimalEvidence`;
  * the Selector's realized `GuardDecision` and, for `degrade` or `abstain`, the current failure-behavior policy;
  * the candidate-set value and exact derived union bound to the Selector's `ComparisonResultSlot` argument;
  * the effective criteria and selector-default refs; and
  * the selected-set result and any current F.9 bridge, CL, and ReferencePlane refs.

  These neighboring objects support replay. The finite basis is a binding of the actual selection application, and none of them is selector-declaration content or a generic result container.

#### A.19.SelectorMechanism:4.2 - Boundary and layering rules

0. **Selection conditions are explicit values, not a new object kind.** The actual application binds `CriteriaSlot` plus effective selector-policy refs, defaults, and `degrade` failure behavior. Acceptance and admission predicates remain separate. `SelectionSlot` contains only the resulting candidate set; eligibility, conditions, scope, evidence, and replay metadata stay outside it.

1. **Selection consumes a traceable finite basis of upstream CHR products; it does not invent them.** The actual use binds exact binary CPM applications separately and supplies `ComparisonResultSlot` only as the union of their justified outputs. The kernel MUST NOT perform normalization (UNM), indicatorization (UINDM), scoring (USCM), folding (ULSAM), comparison (CPM), batch-result fabrication, or missing-pair completion inside `Select`. If a scalar “overall score” is desired, it must be declared upstream as an admissible scoring or comparator choice, not invented inside selection.

2. **Threshold discipline (acceptance is not selection).** Acceptance and admission thresholds are not selection criteria: they remain in their governing declarations and are applied only through `SelectEligibility`. Selection-level tie-breakers, `PortfolioMode`, and selected-set constraints may exist, but they MUST be explicit in current criteria or policy refs and bound by the dated selection occurrence, never hidden as unnamed constants.

3. **Report‑only summaries inside suite closure.** Any scalar summaries, illumination metrics, or auxiliary “why not chosen” telemetry are report‑only unless explicitly promoted by policy, and MUST NOT be used as hidden dominance rules (`A.19.CHR:4.3.3`).
   Publishing and telemetry remain outside suite closure and are handled by established publication forms such as `G.10` or `PTM`, not as hidden tails inside selection.

4. **Specializations are explicit and disciplined.** Any refinement or extension of `SelectorMechanism` must follow `A.6.1:4.2.1`:

   * SlotKind invariance for inherited operations,
   * no new mandatory inputs to inherited `Select`,
   * added capabilities appear as new operations or as `⊑⁺` extensions.

5. **Planned slot filling is preserved.** Planned fillers for `TaskSignatureRef@edition`, `CGSpecRef@edition`, evidence-policy overrides, and other pins live in `SlotFillingsPlanItem` rows. Dated selection `U.Work` binds effective values as occurrence parameters; its result and evidence-provenance relations make their use replayable without mutating the plan.

---

