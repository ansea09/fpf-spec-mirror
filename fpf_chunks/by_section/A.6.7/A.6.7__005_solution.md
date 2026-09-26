---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__005_solution.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:4 — Solution"
line_start: 21551
line_end: 21800
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

### A.6.7:4 - Solution

Declare the members and their shared conditions in a `MechSuiteDescription`:

#### A.6.7:4.1 `MechSuiteDescription` (data model)

`MechSuiteDescription` declares:

1. **Suite identifier:** a stable identifier for downstream citation.
2. **Membership:** a finite set of distinct mechanism declarations.
3. **Suite obligations:** shared invariants that every member (and any permitted composition of members) must respect.
4. **Suite spec pins:** required citations/pins to governing spec refs and other “anchor” references.
5. **Suite protocols:** allowed pipelines of use (permitted ordering and optional steps), expressed at the descriptive level.
6. **Suite audit obligations:** required audit/pin visibility for downstream uses (UTS/Path pins, crossing pins, guard pins), expressed as required anchors (not run-time values).
7. **Notes:** didactic boundaries and anti-pattern warnings.

A minimal canonical form:

```
MechSuiteId := Identifier  // PascalCase; stable citation handle. Versioning MAY be carried externally.

SuiteObligation := declared suite-level obligation
// Canonical reusable names (not exhaustive):
//   bridge_only_crossings,
//   two_bridge_rule_for_described_entity_change,
//   transport_declarative_only,
//   penalties_route_to_r_eff_only,
//   guard_decision_tristate(pass|degrade|abstain),
//   unknown_never_coerces_to_pass,
//   gate_decision_separation,
//   guard_lexeme_reservations,
//   cg_spec_cite_required_for_numeric_ops,
//   no_silent_scalarisation_of_partial_orders,
//   no_silent_totalisation,
//   no_thresholds_in_suite_core,
//   crossing_visibility_required,
//   planned_slot_filling_in_work_planning_only,
//   finalize_launch_values_in_work_enactment_only,
//   implementation_export_discipline_when_cited

SuiteObligations := { SuiteObligation[*] } // clause set; duplicates-free.

MechSuiteDescription := ⟨
  mech_suite_id: MechSuiteId ,
  mechanisms: MechanismDeclarationRef[+] ,     // references to exact member declarations
  suite_obligations: SuiteObligations ,
  suite_spec_pins: SuiteSpecPins ,
  suite_protocols?: SuiteProtocol[*] ,
  suite_audit_obligations?: SuiteAuditObligations ,
  suite_notes?: DidacticNotes
⟩
```

**Norms.**

* **Suite identifier.**
  `mech_suite_id` MUST be present and stable: it is the citation handle for downstream planning and `U.Work.Audit`.

**Well-formedness constraints (admissibility; non-deontic).**

* **WF‑MS‑1 (Membership set semantics).** `mechanisms` resolves to pairwise distinct A.6.1 declaration epistemes under C.2.1 identity; field order carries no semantics. Two citations of the same declaration are one member.
* **WF‑MS‑2 (Protocol closure and resolution).** Every `ProtocolStep.mechanism` resolves to one member declaration at its selected edition, and `step.operation` resolves to one operation designator in that declaration. The selected operation supplies its arguments, results, laws and admission conditions. A stage label or unqualified family name is insufficient.
* **WF‑MS‑3 (Suite ≠ Pack).** `MechSuiteDescription` does not carry shipping/publication payloads; use the applicable shipping or publication pattern for those results.
* **WF‑MS‑4 (Suite ≠ Mechanism).** `MechSuiteDescription` contains no `OperationAlgebra`/`LawSet`/execution semantics and is not admissible where a `U.Mechanism.*` node is required.

* **Membership is by exact declaration (order-free).**
  `mechanisms` MUST denote a duplicates-free set of distinct `U.Mechanism` members. Membership order has no semantics; any intended ordering is expressed only in `suite_protocols`. A suite is defined by selected operation declarations and suite protocols.

**Declaration reference and edition selection.** `MechanismDeclarationRef` is a reference to an independently identified A.6.1 `U.Mechanism` episteme, not a new kind. Resolve it under the effective reference scheme to its content and EntityOfConcern. The published edition used for that resolution must be explicit or uniquely determined by the cited suite baseline. When several editions qualify, state a selection condition that yields one before using a protocol step; otherwise return the unresolved alternatives. There is no implicit latest.

Changing declaration content, EntityOfConcern or effective reference scheme follows A.6.1/C.2.1 identity. Changing a carrier, layout or citation alone can leave the member unchanged. A changed guard or argument selects a different declaration contract and requires the affected protocol bindings to be checked again. A claim that two declarations concern the same operation family needs that subject's own identity rule; suite membership does not establish it. Distinct declaration contracts can be selected without inventing a universal operation-family kind.

* **No substitution by `MechFamilyDescription`.**
  A suite MUST NOT be encoded as a `MechFamilyDescription`.
  If desired, a suite MAY additionally **cite** `MechFamilyDescription` / `MechInstanceDescription` for particular members (e.g., “preferred realization for this context”), but such citations do not redefine membership.

* **No “Pack” meaning.**
  A suite MUST NOT be named or treated as a publication pack. `Pack` remains reserved for publication/shipping bundling (e.g., G.10).

* **No mechanism semantics in the suite.**
  A suite is a **Description**, not a mechanism: it does not define `OperationAlgebra` and does not absorb gate logic.

#### A.6.7:4.2 SuiteObligations (canonical obligation vocabulary)

`MechSuiteDescription` MAY declare any obligations. The canonical names in §4.1 support reuse across Part G and admissibility-gated characterization stacks; they are not an exhaustive inventory.

`SuiteObligations` SHOULD be written as an explicit, duplicates-free clause set. Select applicable clauses from the canonical vocabulary in §4.1 and state any additional obligations explicitly. The requirements below remain applicable under their stated conditions.

**Obligation meanings (normative).**

1. **`bridge_only_crossings`.**
   For an actual semantic correspondence between distinct recovered local senses, recover the F.17 endpoints and an obtaining F.9 Bridge, then the bounded-use and reliance claims required for this use. A suite creates none of those facts. A changed entity, reference scheme, plane or notation alone establishes no semantic crossing under A.6.4.

   1.1. **`two_bridge_rule_for_described_entity_change`.**

   * When both an F.9 semantic correspondence and a C.3.3 kind correspondence are claimed, establish each under its direct rule. Any separately claimed plane relation keeps its own governor. Changing the EntityOfConcern alone creates neither relation. Retain the separate use conditions and applicable penalty policy; do not invent a second Bridge from the change label.

   1.2. **`transport_declarative_only`.**
   * Well-formedness constraint: suite obligations do not introduce any additional graph edge kind beyond E.18 `U.Transfer` and do not embed CL/Φ/Ψ/Φ_plane tables. Any transport-related obligation is expressed only as referenced pins/anchors whose realization is mediated by E.18 / gate surfaces.

2. **`penalties_route_to_r_eff_only`.**
   Well-formedness constraint: CL/Φ/Ψ/Φ_plane penalties associated with crossing discipline route to `R/R_eff` only; suites do not define transport penalties that alter `F/G`.

3. **`guard_decision_tristate(pass|degrade|abstain)` and `unknown_never_coerces_to_pass`.**
   Well-formedness constraint: admissibility/eligibility outcomes use a tri-state guard result `GuardDecision := {pass|degrade|abstain}`. Unknown/insufficient evidence is not coerced to `pass`; it resolves to `{degrade|abstain}` under declared failure behavior (e.g., probe-only as a SoS‑LOG branch id, not as a new decision value).

4. **`gate_decision_separation`.**
   Well-formedness constraint: suites do not define or use `GateDecision` values (including `block`) as part of mechanism/suite semantics. Gate-level outcomes and `DecisionLog` remain on `OperationalGate(profile)`.

5. **`guard_lexeme_reservations`.**
   Well-formedness constraint: `USM.CompareGuard` and `USM.LaunchGuard` denote gate-owned guard events/pins; member mechanisms and suite protocols use `…Admissibility` / `…Eligibility` for guard predicates, not the reserved gate lexemes.

6. **`cg_spec_cite_required_for_numeric_ops`.**
   Well-formedness constraint: any member operation that performs numeric comparison/aggregation/admissibility-sensitive scoring cites the applicable `CG-Spec` (and relevant subrefs) as spec pins, rather than embedding equivalent local admissibility content.

7. **`no_silent_scalarisation_of_partial_orders` and `no_silent_totalisation`.**
   Well-formedness constraint: if a member mechanism induces a partial order, it preserves set-/relation-valued semantics; it does not silently reduce to a scalar/total order. Any totalization is explicit and policy-bound.

8. **`no_thresholds_in_suite_core`.**
   Well-formedness constraint: suite core does not publish acceptance thresholds (“passing scores” / hidden cutoffs). Thresholds belong to acceptance clauses / task signatures / gate profiles.

9. **`crossing_visibility_required`.**
   Well-formedness constraint: any GateCrossing relevant to suite use publishes a `CrossingBundle` (E.18) and can be cited as an audit anchor.
   Apply E.18 only for an independently selected TransformationFlowStructure and its actual governed crossing; apply A.21 for a current work-entry gate. An edition, entity or notation change alone supplies neither that crossing nor a semantic Bridge.
   Suites may require `CrossingBundleRef` / UTS / Path pins and policy-id pins as anchors, and MUST NOT embed CL/Φ/Ψ/Φ_plane tables.

10. **`planned_slot_filling_in_work_planning_only`.**
    Well-formedness constraint: any planned slot filling used as a baseline for suite use is authored in `WorkPlanning` as a planned baseline (no run-time slot instances; no launch values).

11. **`finalize_launch_values_in_work_enactment_only`.**
   Well-formedness constraint: `FinalizeLaunchValues` (and any witness of actual launch values) occurs only in `U.WorkEnactment`; neither the suite nor any planned-baseline WorkPlanning plan item is a place for launch values.

#### A.6.7:4.3 SuiteSpecPins

A `MechSuiteDescription` MUST be able to declare required spec pins as references, not as duplicated content. Canonically:

```
SuiteSpecPins := ⟨
  required_spec_refs?: {CNSpecRef?, CGSpecRef?, ...},
  required_edition_pins?: EditionPin[*],
  required_policy_id_pins?: PolicyIdPin[*],
  required_planned_baseline_ref?: PlannedBaselineRef?
⟩
```

**Norms.**

* If the suite is admissibility-gated for characterization, `CNSpecRef` and `CGSpecRef` MUST be required (as references/pins).
* Spec pins are citations and anchors. They do not replace the underlying `…Spec` objects.
* A suite may require an edition/reference baseline in ordinary A.15.2 WorkPlan content. Address it through the exact plan and its local content locator; it supplies no launch value or gate decision.
* Use A.15.3 typed planned filling only when an existing declaration member independently supplies the position meaning, designation, cardinality and actual-use predicate. A suite Description field is not a SlotSpec or operation argument merely because a plan names it. Missing planned information can remain unknown in the plan; a missing governor requires recovery or definition of that member before typed filling. Actual launch bindings and any FinalizeLaunchValues witness remain with actual enactment.

#### A.6.7:4.4 SuiteProtocols

A suite MAY describe allowed protocols (pipelines) as descriptive constraints on how suite members are intended to be composed. A `SuiteProtocol` describes the member-operation sequence. Its description:

* MUST name the member mechanisms it uses (explicitly; no “implicit use”),
* MAY mark steps as optional,
* MUST NOT introduce hidden crossings or hidden admissibility steps,
* MUST identify any “publish/telemetry” as an external step of the surrounding protocol, realized through existing publication surfaces (e.g., Part G shipping), rather than as a hidden tail inside a mechanism. This external step is not a `ProtocolStep` in the suite-member sequence.

A canonical shape for the suite-member sequence:

```
SuiteProtocol := ⟨
  steps: [ ProtocolStep₁, …, ProtocolStepₙ ],
  invariants?: ProtocolInvariant[*],
  notes?: DidacticNotes
⟩

ProtocolStep := ⟨
  mechanism: MechanismDeclarationRef, // resolves to the exact selected edition
  operation: declaration-local operationDesignator,
  optionality: {required|optional},
  requires_pins?: PinRef[*]
⟩
```

#### A.6.7:4.5 SuiteAuditObligations

A suite MAY require that downstream use provide certain audit anchors. These are **requirements**, not run-time values. A suite audit obligation MAY include:

* required `UTS` + `Path` pins,
* required crossing-surface visibility pins for any crossing relevant to suite use,
* required presence of `USM.CompareGuard` and/or `USM.LaunchGuard` **pins** (not gate checks),
* required declaration of guard ownership (e.g., a `GuardOwnerGateSlot` anchor),
* required expression of guard violations as `GuardFail` events aggregated by the guard-owning gate (per `GuardOwnerGateSlot`), not as extra mechanism/suite states,
* required policy-id pins for any degrade/sandbox/probe-only branches (SoS‑LOG branch id anchors).
* required parity/selection-grade pins when applicable (e.g., when suite use claims parity-grade comparison/selection surfaces downstream).

**Norm.** A suite must never publish a `DecisionLog` or `GateDecision`. If the suite requires guard pins, it requires their **presence** as anchors so that the gate-level owner can aggregate `GuardFail`s and decide `degrade|block` per gate profile.

#### A.6.7:4.6 Examples

**Example 1 — compare two offers and retain the nondominated set.** The question is whether either offer can be discarded without accepting a worse cost or quality. This is a stipulated mathematical use; the following specifications and applications are case facts, not empirical measurements or dated Work claims.

**Selected contracts and specifications.** The baseline `OfferChoiceB1` selects `Dcmp = A.19.CPM §4.1` and `Dsel = A.19.SelectorMechanism §4.1`, including their operation-local declarations, application/binding predicates, identity and extent rules, in the same publication edition as this case. These references mean that edition's content, not a later revision. Resolve another publication's references again before reuse. Their effective scheme is the CHR reference scheme declared there.

The case's independently stipulated specification editions are:

| Reference | Content consumed in this use |
| --- | --- |
| `OfferCN@1` | Admits exactly offers A and B with complete cost and quality profiles on `OfferBasis@1`. Comparability is componentwise on those same positions and scales, with no normalization requirement. Both candidates meet acceptance; there is no additional acceptance threshold. |
| `OfferCG@1` | Admits `OfferPareto@1` in ComparatorSet. SCP permits order comparisons on each declared scale and conjunction of those comparisons; it permits no cross-characteristic addition. MinimalEvidence requires both exact profile values and their common basis. |
| `OfferPareto@1` | Lower cost and higher quality are better. X dominates Y iff X is no worse on both positions and strictly better on at least one. Equal profiles return parity; a trade-off returns the pair's incomparability token. No epsilon or tie-breaker applies. |
| `OfferSelection@1` | Select every nondominated candidate. Compare every unordered pair once under OfferPareto@1. No singleton preference or hidden default applies. Missing required comparison, failed evidence or unknown value means abstain; no degrade branch is enabled. |

These definitions are the cited case specifications, outside the suite description. `OfferBasis@1` gives position `cost` the price Characteristic and EUR ratio scale, and position `quality` the declared defect-free proportion Characteristic and a dimensionless ratio scale. The already admitted measure profiles are A=(10 EUR, 0.8), B=(12 EUR, 0.9). Both use these positions, with complete exact stipulated values.

**Filled suite description.** `OfferChoiceSuiteDescription` has `mech_suite_id = OfferChoiceSuite`, membership `{Dcmp, Dsel}`, required spec references `{OfferCN@1, OfferCG@1}`, and required policy/comparator references `{OfferSelection@1, OfferPareto@1}`. Its shared obligations are tri-state eligibility with unknown never passing, explicit numeric admissibility, set-valued comparison/selection without hidden scalarization or totalization, and gate-decision separation. The one protocol contains four required steps:

| Selected member | Operation | Required references |
| --- | --- | --- |
| Dcmp | CompareEligibility | OfferCN@1, OfferCG@1, OfferPareto@1 |
| Dcmp | Compare | the same three references |
| Dsel | SelectEligibility | OfferCN@1, OfferCG@1, OfferSelection@1 |
| Dsel | Select | the same three references |

The protocol invariant requires both members to use the same admitted profiles, scope, slices, scheme, plane and evaluation point, and Select to consume the actual returned Compare binding. The audit obligation is to recover those effective arguments, eligibility judgments and output bindings, including token provenance. There is no public naming, semantic/kind/plane correspondence, flow crossing, gate, implementation export or planned-launch claim in this use, so it requires none of their conditional anchors. The description supplies no operation law or runtime output of its own.

**Application and result.** Outside the description, stipulate one completed application of each of the four selected operations, in the listed order. Each takes up the following arguments and ends at its own return; those four invocation episodes are distinct from the evaluation point they share. `OfferScope@1` delimits the comparison and selection of A and B for this offer question; `{OfferSlice@1}` is its selected A.2.6 context-slice set. Both members bind that scope and set, the CHR reference scheme, the concept reference plane, and evaluation point `2030-01-01T00:00Z` in UTC. No additional CharacteristicSpacePredicate or MinimalEvidence override is used. Normalization has no dependency because OfferCN@1 compares the original matched scales.

The comparator guard uses A as LeftProfileSlot and B as RightProfileSlot, with OfferCN@1, OfferCG@1 and OfferPareto@1, and returns `pass`: both profiles are complete, admitted and scale-compatible. Application `c1` then returns `ComparisonResultSlot = {A ∥ B}`. Its returned binding, not an equal saved token, supplies the selection basis.

The selector guard binds CandidateSetSlot={A,B}, comparisonBasis={c1}, requiredComparisons={(A,B,OfferPareto@1)}, tokenProvenance={A ∥ B ↦ c1's returned binding}, and ComparisonResultSlot={A ∥ B}. CriteriaSlot contains the single clause “retain all nondominated candidates”; selectorPolicy is OfferSelection@1; TaskSignatureSlot is absent because no default is obtained from it. CN, CG and the common use arguments are those above. Coverage is complete and the guard returns `pass`. Select consumes that exact eligibility result and returns `SelectionSlot = {A,B}`. Incomparability is retained; neither offer is silently chosen as the winner.

**Changed condition and stop.** If B's quality is unknown, OfferCG@1's evidence condition fails: CompareEligibility returns `abstain`, no Compare result is fabricated, and the selector has no complete comparison basis. Its guard returns `abstain`, with no Select application or selected-set result. Changing only the selected comparator declaration to an unresolved edition also stops at protocol resolution before calculation. A suite-shaped record cannot cure either missing basis.

The description answers which contracts can be jointly used and under what conditions. The four stipulated applications answer what happened in this case. A gate decision, dated Work account or published result would need its own independently established basis.

**Declaration-change case.** The CHR `normalize` stage resolves to `apply` in a selected UNM declaration edition. Let D1 admit `pass` and policy-supported `degrade`, as A.19.UNM §4.1 does. Suppose a separately proposed D2 changes the operation guard to `pass` only. For the same input whose eligibility is `degrade`, D1 permits the qualified output and D2 does not. Merely pinning both sources or writing `UNM + normalize` cannot decide which contract governs. A step selecting D1 remains on D1; substituting D2 changes the member contract and requires the new guard to pass. These are illustrative edition names, not claims that both editions are published.

Two different realizers of D1 still use one member. UNM and the independently identified UINDM declaration are different members. A differently formatted publication of D1 can preserve the declaration identity. A new declaration about an independently established same family is still a new contract when its content changes; any family-continuity claim remains separate. Thus the protocol can resolve exactly even where family continuity is irrelevant or unresolved.

**Example 2 (non-conformant).** Misusing a family as a suite:

```
CHRMechanismFamily : MechFamilyDescription := { UNM, UINDM, USCM, ... }
```

This is a level error: `MechFamilyDescription` is reserved for realizations of a single mechanism declaration.

**Example 3 (non-conformant).** Turning a suite into a hidden gate:

* The suite declares `GateDecision` values or embeds a `DecisionLog`.
* The suite defines acceptance thresholds (“pass score ≥ 0.7”) as part of suite obligations.
* The suite embeds Φ/CL tables or invents an additional graph edge kind beyond E.18 `U.Transfer`.

All violate the separation between mechanism/suite descriptions and gate-level operational control.

