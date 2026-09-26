---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__006_solution.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:4 — Solution"
line_start: 36512
line_end: 36663
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.1"
  - "A.6.5"
  - "C.22"
  - "E.18"
  - "G.0"
  - "G.5"
keywords:
  - "ComparisonResultSlot"
  - "SelectEligibility"
  - "SelectorMechanism"
  - "explicit criteria"
  - "finite basis of binary CPM applications"
  - "pass/degrade/abstain"
  - "required comparison coverage"
  - "selected candidate set"
  - "selection kernel"
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

Method semantics and SoTA algorithm families do not live inside the kernel: they connect via `G.2` SoTA packs and wiring modules, and via explicitly declared specializations subject to the local restrictions in CC‑A19SelectorMechanism‑10. A claimed refinement, conservative extension or equivalence uses its own comparison test in `A.6.1 §4.8`; the labels `⊑` and `⊑⁺` do not supply that test.

#### A.19.SelectorMechanism:4.1 - Operation declaration — normative core

* **Declaration boundary:** this A.6.1 intension declares `Select` and `SelectEligibility`; it does not bind project-specific pins or create selection scope, dated work, an actual operation application, gate decision, selected-set episteme, evidence use, provenance path, currentness relation, or publication relation. Each neighboring object or relation uses its direct governor.
* **Declaration identity:** SelectorMechanism.IntensionRef cites this exact A.6.1 U.Mechanism episteme. The CHR select stage resolves to its local Select operation. A changed argument, selection law or guard requires explicit selection of the changed declaration; another realizer of the same declaration changes no suite member.

* **IntensionHeader:** `id = SelectorMechanism`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `SelectorMechanism.IntensionRef` designates this `U.Mechanism` episteme as the canonical suite member named in `A.19.CHR:4.2`; it is not the `EntityOfConcernRef` of the declared operation family.

* **Tell.** Universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Purpose:** universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Imports:** `A.6.1:4.8 (exact declaration comparisons)`, `A.6.1 (operation-local declarations and bindings)`, `A.19.CN (CN‑Spec governance card)`, `C.22 (TaskSignature as a policy-reference artifact when used)`, `G.5 (selector conformance and default selection policy)`, `G.0 (CG‑Spec admissibility and evidence gates)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **EntityOfConcernRef:** the selection operation family declared by `Select` and `SelectEligibility` in this section.

* **Effective `U.ReferenceScheme`:** the CHR suite reference scheme in which the A.19.CHR SlotKind lexicon, CN-Spec, CG-Spec, and any current TaskSignature tokens are interpreted.

* **Direct signature components:**

  * **SubjectKind:** `Selection`.
  * **RangedValueKind:** pair of values `<admitted candidate set, relation or poset token set over the same candidate universe>`.
  * Results are operation-local: the selected candidate set and the separate guard judgment.
  * Input qualification: selection ranges over one admitted candidate set and the exact union of justified relation or poset tokens from a finite basis of binary CPM applications whose pair endpoints lie in that candidate set and whose coverage satisfies the explicit selection conditions, all in one exact `U.ClaimScope`; selected `U.ContextSlice` values are members of that scope under A.2.6 and do not create duplicate membership.

  These are direct A.6.0 declaration components. They do not form another selector-content container, and they do not absorb candidate admission, comparison work, dated selection work, result, evidence-provenance, or replay relations.
**Operation-local argument and result declarations**

Each argument below is declared separately for Select and SelectEligibility, except the realized eligibility argument of Select itself. ByValue carries the stated value; a named Ref or ByRef resolves one exact value and edition. Cardinality is per application. The guard can assess an incomplete proposal with 0..1 of each required argument; missing inputs have no binding and prevent pass.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | CandidateSetSlot | Set of admitted candidate values, each retaining its governing kind and identity | ByValue; 1 set |
| Argument | ComparisonResultSlot | Set of relation/poset tokens, exactly the union of the comparisonBasis members' own returned values | ByValue; 1 set |
| Argument | CriteriaSlot | Set of selection clauses and explicit tie-breakers used to determine the selected set; acceptance thresholds remain in their own declarations | ByValue; 1 set |
| Argument | TaskSignatureSlot | TaskSignature supplying selector policy defaults when used; it does not replace CN-Spec or CG-Spec | TaskSignatureRef; 0..1 |
| Argument | CNSpecSlot | CN-Spec supplying admission/acceptance and candidate-use conditions | CNSpecRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying selector admissibility and default evidence conditions | CGSpecRef; 1 |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used instead of CGSpecSlot.MinimalEvidence | MinimalEvidenceRef; 0..1 |
| Argument | comparisonBasis | Finite set of exact binary CPM Compare application references, each with its left/right pair, realized eligibility and own output binding or explicit absence | ByValue set; 1 |
| Argument | requiredComparisons | Finite set of required binary comparisons derived from the candidates, criteria and effective policy, including direction/comparator distinctions that affect selection | ByValue set; 1 |
| Argument | tokenProvenance | Mapping from every consumed token to at least one exact producing CPM output binding in comparisonBasis | ByValue; 1 mapping |
| Argument | claimScope | U.ClaimScope delimiting candidate universe and selection use | ByRef; 1 |
| Argument | selectedSlices | Set of selected U.ContextSlice members of claimScope under A.2.6 | ByValue set of exact references; 1 set |
| Argument | characteristicPredicate | A.19 CharacteristicSpacePredicate basis shared as required with the relevant CPM members | ByValue; 0..1, explicitly absent when none governs the use |
| Argument | referenceScheme | Effective U.ReferenceScheme used to interpret the selection | ByRef; 1 |
| Argument | referencePlane | CHR:ReferencePlane value qualifying selection | ByValue; 1 |
| Argument | evaluationTime | Selection-evaluation point or interval in the declared time basis | ByValue; 1 |
| Argument | selectorPolicy | Effective selection policy and resolved defaults, including exact candidate-level failure behavior when degrade is used | ByRef to the declared policy; 1, resolved through TaskSignature when it supplies that policy |
| Select argument | eligibility | GuardDecision actually determined by SelectEligibility for these same proposal arguments, used to admit this selection | ByValue; 1, with its exact producing guard-result binding recoverable |
| Select result | SelectionSlot | Set of candidate values selected under those criteria and policy | ByValue; 1 set on completed admitted selection, 0 on abstain |
| SelectEligibility result | GuardDecision | Judgment determined by the eligibility predicates: pass, degrade or abstain | ByValue; 1 on completed evaluation |

For each argument row, its **bindingPredicate** holds when that application actually uses the resolved value for its stated purpose: candidates supply the selection universe, criteria/policy supply the choice rule, specifications/evidence requirements govern admission, and the basis, coverage and provenance supply the comparisons on which the choice relies. Scope, slices, predicate, scheme, plane and time bind only when they qualify that application. A nearby policy or copied comparison record does not supply those bindings.

The **SelectionSlot bindingPredicate** holds when that Select application returns the candidate subset determined by its bound criteria/policy from the justified comparison basis, under its declared pass/degrade conditions. The **GuardDecision bindingPredicate** holds when that SelectEligibility application returns its assessed judgment. An equal selected set or guard value stored elsewhere is insufficient. A.6.1 governs each binding's identity and continuous extent within the application; result binding begins at its actual return.

**SlotIndex (derived projection).** Project the designators, ValueKinds, designation and cardinalities above. Historical Slot names support CHR lookup. The other local names declare operation arguments, not new U-kinds or CHR SlotKinds; A.6.5 relation SlotSpecs supply none of their semantics.

**OperationAlgebra.** The select stage resolves to Select with the declared candidate/token, criteria/specification and selection-use arguments, returning SelectionSlot. SelectEligibility evaluates that proposal under the guard below. ComparisonResultSlot contains only the exact token union; application references, coverage, scope and provenance remain separate arguments. A CPM abstain with no output contributes no token. Every required comparison must be discharged by an exact basis member; degraded selection names excluded candidates under the bound failure behavior and retains complete coverage for its reduced use.

**ApplicationPredicate.** Select obtains when a selection act actually applies the bound criteria and effective policy to the candidate universe using the bound justified CPM outputs and use restrictions, with pass or an explicitly permitted degrade outcome under SelectEligibility. It returns the resulting set; on abstain no Select act proceeds. SelectEligibility obtains when an evaluation actually checks that proposal's coverage, provenance, admission and evidence conditions and returns the corresponding judgment. A valid proposal or an equal saved selected set does not establish that selection act.

**ApplicationIdentityRule.** One application is one selection invocation or guard-evaluation invocation at its calculation locus, from taking up its declared arguments until return or termination. References to that same episode reidentify it. Two independently begun invocations remain distinct even when the complete CPM basis, criteria, policies, qualification window and results are equal. Law 6 additionally makes a changed binding a new selection application; a completed prior application cannot acquire the replacement basis or result.

**ApplicationExtentRule.** Select extends from actual use of its candidates, CPM basis and choice rules through selected-set return or termination; SelectEligibility extends from proposal assessment through judgment or termination. An unfinished invocation has an open extent and no unreturned result binding. The selection-evaluation window qualifies the use and does not determine these actual calculation intervals. A trace designates an established episode; ordinary set-selection mathematics asserts no dated U.Work.

For example, use the admitted incomparable supplier pair from A.19.CPM §4.1 and the declared criterion “retain every nondominated candidate.” With complete required coverage and the exact CPM token binding, two separately performed selections can each return {A,B}. Their Select occurrences and result bindings differ even when they reuse the same CPM producer application. A copied {A,B} without a corresponding selection return establishes no fresh binding. A copied comparison token whose producing CPM return is unestablished fails tokenProvenance and causes abstain; it cannot enter the basis merely because its text matches.

* **LawSet** (minimum): the selection kernel is set-returning and policy-bound

  1. **Set‑returning by default:** a conformant `Select` MUST return a declared selected set by default. It MUST NOT silently collapse partial orders or incomparabilities to a single winner; if a singleton outcome is required, it MUST be an explicit criterion (or a declared upstream total order).
  2. **No hidden thresholds or constants:** a conformant publication MUST NOT smuggle thresholds, weights, dominance rules, or tie‑breakers. Selection‑level commitments MUST be explicit in `CriteriaSlot` and, where needed, in explicit policy defaults exposed through `TaskSignatureSlot`. Admissibility and acceptance thresholds are applied only via `SelectEligibility` using `CNSpecSlot.acceptance` and the effective evidence policy (`MinimalEvidenceSlot?` or `CGSpecSlot.MinimalEvidence`).
  3. **No hidden scalarization or token aggregation by assertion:** a conformant publication MUST consume `ComparisonResultSlot` as the exact union of the finite basis members' justified set-valued or partial outputs. Every consumed token MUST be traceable to at least one exact producing CPM application. Scalar summaries or relation tokens inferred from a missing pair, empty output, `degrade`, or `abstain` are forbidden; scalar summaries, if produced at all, are report-only unless explicitly promoted by policy outside suite closure.
  4. **Evidence gating is explicit:** when selection depends on evidence, it MUST cite either `MinimalEvidenceSlot` or the effective `CGSpecSlot.MinimalEvidence` policy and evaluate selection with the tri-state predicate. Candidate-level ineligibility handling MUST be explicit in current criteria or upstream results and bound by the actual selection application; the kernel MUST NOT invent evidence thresholds.
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
  * A selection across reference schemes or planes follows the relations the case actually needs. When it relates two exact F.17 `SchemeSenseCell` values from different semantic contexts, test the F.9 `BridgePredicateProfile` and cite the Bridge only when its direct predicate obtains; state suitability for the named selection use in a separate C.2.1 claim. If that predicate is false or unresolved and the semantic crossing is required by the selection conditions, `SelectEligibility` cannot be `pass`; follow the already declared explicit `degrade` policy when applicable, otherwise `abstain`. When the selection crosses exact ReferencePlanes, cite the applicable plane relation and policy. If both facts are current, state both under their own predicates. A cell or plane difference alone establishes neither relation, and one branch never fabricates the other. Neither relation supplies candidate universe, comparison-application basis or coverage, relation tokens, selection conditions, scope, predicate, or time.

* **Neighboring semantic-Bridge, bounded-use, and reference-plane relations:**

  When candidates or comparison tokens require interpretation across different semantic contexts, resolve the two exact F.17 `SchemeSenseCell` endpoints and test one F.9 `BridgePredicateProfile`. For an obtaining Bridge, state its exact endpoints and profile separately. State suitability for the named selection use in a C.2.1 assertion whose EntityOfConcern is that Bridge and whose ClaimGraph designates `<u,d,r,t>` and polarity. Include `CL` or an observed-loss note only when the receiving use consumes it; permitted loss remains `t` in the bounded-use claim. For a ReferencePlane crossing, cite the applicable plane relation and policy separately. Open A.10 only when bounded reliance is current and B.3 only when an actual named assurance claim is current. If that assurance argument consumes a locally declared `R_eff` calculation, cite its applicable domain model and calculation; neither the Bridge nor `CL` creates a penalty. Adding or changing any of these neighboring objects does not by itself change the selector declaration.

* **Neighboring dated work, operation application, result binding, and evidence relations:**

  The identified Select application binds the candidate set, finite comparison basis, required coverage, token union, selection-use arguments, policies and returned SelectionSlot. If the account also asserts dated selection U.Work, A.15.1 independently admits that performance; neither its identity nor extent is automatically that of one Select application. When the account asserts them or the receiving use consumes them, A.2.4 governs evidence use with its own claim scope and relevance window, A.10 governs reliance and provenance, and G.11 governs source or assertion-edition currentness. A durable selected-set episteme, when needed, is governed by C.2.1, and any current entity-identity inception claim by A.15.PROD. No universal work-result, comparison-result, or selection-result relation is presumed. To replay the selection, recover:

  * the candidate set and required binary comparisons; for every basis member, the exact CPM application, pair, realized `GuardDecision`, and its own output binding or explicit absence; and the trace from every consumed token to its producing member;
  * one `U.ClaimScope`, selected A.2.6 context slices, A.19 predicate basis, effective reference scheme and plane, and evaluation point or interval shared as required by the selection conditions;
  * `CNSpecRef.edition`, `CGSpecRef.edition`, and `TaskSignatureRef.edition` when TaskSignature is used;
  * the effective MinimalEvidence policy, either the explicit override or `CGSpecSlot.MinimalEvidence`;
  * the Selector's realized `GuardDecision` and, for `degrade` or `abstain`, the current failure-behavior policy;
  * the candidate-set value and exact derived union bound to the Selector's `ComparisonResultSlot` argument;
  * the effective criteria and selector-default refs; and
  * the selected-set result; any current obtaining F.9 Bridge and its separate C.2.1 bounded-use claim; any optional `CL` or observed-loss note actually consumed; and any applicable ReferencePlane relation and policy. Recover A.10 reliance or B.3 assurance only when the selection use actually consumes it.

  These neighboring objects support replay. The finite basis is a binding of the actual selection application, and none of them is selector-declaration content or a generic result container.

#### A.19.SelectorMechanism:4.2 - Boundary and layering rules

0. **Selection conditions are explicit values, not a new object kind.** The actual application binds `CriteriaSlot` plus effective selector-policy refs, defaults, and `degrade` failure behavior. Acceptance and admission predicates remain separate. `SelectionSlot` contains only the resulting candidate set; eligibility, conditions, scope, evidence, and replay metadata stay outside it.

1. **Selection consumes a traceable finite basis of upstream CHR products; it does not invent them.** Any indicator-derived scoring or comparison input retains its exact A.19 basis and the UINDM positions selected under that declaration. A changed basis requires the affected upstream position resolution and result again; the selector cannot carry old naked indices into the new declaration. The actual use binds exact binary CPM applications separately and supplies `ComparisonResultSlot` only as the union of their justified outputs. The kernel MUST NOT perform normalization (UNM), indicatorization (UINDM), scoring (USCM), folding (ULSAM), comparison (CPM), batch-result fabrication, or missing-pair completion inside `Select`. If a scalar “overall score” is desired, it must be declared upstream as an admissible scoring or comparator choice, not invented inside selection.

2. **Threshold discipline (acceptance is not selection).** Acceptance and admission thresholds are not selection criteria: they remain in their governing declarations and are applied only through `SelectEligibility`. Selection-level tie-breakers, `PortfolioMode`, and selected-set constraints may exist, but they MUST be explicit in current criteria or policy refs and bound by the actual selection application, never hidden as unnamed constants.

3. **Report‑only summaries inside suite closure.** Any scalar summaries, illumination metrics, or auxiliary “why not chosen” telemetry are report‑only unless explicitly promoted by policy, and MUST NOT be used as hidden dominance rules (`A.19.CHR:4.3.3`).
   Publishing and telemetry remain outside suite closure and are handled by established publication forms such as `G.10` or `PTM`, not as hidden tails inside selection.

4. **Specializations are explicit and disciplined.** A proposed specialization of `SelectorMechanism` must retain these local restrictions:

   * SlotKind invariance for inherited operations,
   * no new mandatory inputs to inherited `Select`,
   * added capabilities appear as explicitly declared new operations or additional results under the local `⊑⁺` notation.

   For the exact refinement, conservative-extension or equivalence claim, apply its own `A.6.1 §4.8` test, preserving the applicable operation, application and binding meanings. CC‑A19SelectorMechanism‑10 retains the exact predicate, endpoint facts and A.6.RCD gap branch.

5. **Planned use and actual binding.** An A.15.2 baseline selects TaskSignature, CG-Spec and evidence-policy editions. A.15.3 supplies planned filling only for an independently declared receiving position. Actual Select arguments and returns are established under this declaration; the planned values remain available for a separately governed comparison with what occurred.

---

