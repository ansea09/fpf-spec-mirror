---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite: Shared Rules for Characterization and Selection"
section_id: "A.19.CHR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__007_conformance-checklist.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.19.CHR — CHRMechanismSuite: Shared Rules for Characterization and Selection"
  - "A.19.CHR:7 — Conformance Checklist"
line_start: 34473
line_end: 34574
dependencies:
  - "A.15.2"
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "A.6.7"
  - "A.6.RCD"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.19"
  - "G.0"
  - "G.10"
  - "G.5"
keywords:
  - "Bridge-only transport"
  - "CG-Spec"
  - "CHR suite"
  - "CN-Spec"
  - "P2W seam"
  - "SlotFillingsPlanItem"
  - "admissibility gate"
  - "characterization core"
  - "crossing visibility"
  - "no hidden scalarization"
  - "no hidden thresholds"
  - "penalties→R_eff"
  - "planned baseline"
  - "set-return selection"
  - "suite obligations"
  - "tri-state guard decision"
---

### A.19.CHR:7 - Conformance Checklist

A CHR mechanism-suite publication set is conformant to **A.19.CHR** iff all applicable items below hold. Existing claim references resolve through §4.3.7.

#### A.19.CHR:7.1 - Suite object checks

**CC‑A67CHR‑1 (Correct kind and level).**
A conforming `CHRMechanismSuiteDescription` SHALL be a `MechSuiteDescription` instance and SHALL NOT be encoded as a `MechFamilyDescription`.

**CC‑A67CHR‑1a (Stable citation handle).**
A conforming `CHRMechanismSuiteDescription` SHALL include a stable `mech_suite_id` suitable for downstream planning and `U.Work.Audit` citation.

**CC‑A67CHR‑2 (Canonical membership).**
A conforming `CHRMechanismSuiteDescription` SHALL enumerate exactly the six CHR mechanisms (UNM, UINDM, USCM, ULSAM, CPM, SelectorMechanism) as `MechanismDeclarationRef`s.

**CC‑A67CHR‑2a (Membership set semantics).**
A conforming `CHRMechanismSuiteDescription.mechanisms` SHALL be duplicates-free and SHALL NOT treat order as semantic (WF‑MS‑1).

**CC‑A67CHR‑2b (No dangling IntensionRefs).**
Each member reference resolves to one exact declaration edition under §4.2.2, and each used operation resolves within that declaration. A stub without the contract is insufficient for use.

**CC‑A67CHR‑3 (Governing spec refs are pins, not copies).**
A conforming `CHRMechanismSuiteDescription` SHALL cite `CN‑Spec` and `CG‑Spec` as required spec refs and SHALL NOT duplicate them as “shadow specs”.

**CC‑A67CHR‑3a (Planned-baseline requirement is pinned).**
A conforming suite cites the exact WorkPlan and baseline locator that will hold its selected editions and references. A.15.3 typed filling is conditional on independently declared positions.

**CC‑A67CHR‑4 (Crossing discipline is complete).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include, at minimum:
`bridge_only_crossings`,
`two_bridge_rule_for_described_entity_change`,
`transport_declarative_only`,
`penalties_route_to_r_eff_only`,
`guard_decision_tristate(pass|degrade|abstain)`,
`unknown_never_coerces_to_pass`,
`gate_decision_separation`,
`guard_lexeme_reservations`,
`cg_spec_cite_required_for_numeric_ops`,
`no_silent_scalarisation_of_partial_orders`,
`no_silent_totalisation`,
`no_thresholds_in_suite_core`,
`crossing_visibility_required`,
`planned_slot_filling_in_work_planning_only`,
`finalize_launch_values_in_work_enactment_only`,
`implementation_export_discipline_when_cited`.

**CC‑A67CHR‑5 (Guard/gate separation).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL:
1) enforce tri‑state guard decisions (`pass|degrade|abstain`),
2) enforce `unknown_never_coerces_to_pass`,
3) enforce guard–gate separation (no `GateDecision` / `DecisionLog` at mechanism/suite level; `block` remains gate‑only), and
4) enforce guard lexeme reservations (`USM.CompareGuard` / `USM.LaunchGuard` are gate-level pins; mechanism predicates use `…Admissibility/…Eligibility`).

**CC‑A67CHR‑6 (No hidden scalarization/totalization).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include explicit bans on silent scalarization of partial orders and silent totalization.

**CC‑A67CHR‑7 (No thresholds in core + single-source defaults).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include `no_thresholds_in_suite_core`.
If any suite protocol relies on defaults (e.g., `PortfolioMode`), the suite description and plan items SHALL cite those defaults from their single declared source (typically a TaskSignature or explicit policy-id), and SHALL NOT introduce competing defaults in the suite.

**CC‑A67CHR‑8 (Protocol explicitness + closure).**
If `suite_protocols` is present, a conforming `CHRMechanismSuiteDescription` SHALL:
1) express any dependence as an explicit protocol step (no hidden invocation of UNM/UINDM/ULSAM inside score/compare/select), and
2) satisfy WF‑MS‑2: every step resolves to one member declaration edition and one operation in that declaration, with no unresolved edition choice.

**CC‑A67CHR‑8a (Canonical protocol is available when protocols are published).**
If `suite_protocols` is present, a conforming `CHRMechanismSuiteDescription` SHALL include at least one protocol equivalent to:
`normalize (UNM) → indicatorize (UINDM) → score (USCM) → fold_Γ? (ULSAM) → compare (CPM) → select (SelectorMechanism)`,
where `fold_Γ` is explicitly optional.
Any publish/telemetry continuation is governed externally (e.g., by G.10 and/or PTM) and MUST NOT be encoded as a `ProtocolStep` inside `suite_protocols` (to preserve WF‑MS‑2 closure).

**CC‑A67CHR‑9 (Packaging separation).**
If protocols include `publish/telemetry`, it is governed by G.10 and/or PTM; the suite does not act as a pack or shipping publication.

#### A.19.CHR:7.2 - Planned baseline checks

**CC‑A67CHR‑10 (Planned baseline exists).** Every P2W path slice using the suite has an A.15.2 WorkPlan baseline with the selected suite and member declaration editions.

**CC‑A67CHR‑10a (Typed filling has its governor).** Use a `CHRMechanismSuiteSlotFillingsPlanItem` only when A.15.3 applies to an independently declared operation argument or relation position. Cite that declaration and position; a suite field is insufficient.

**CC‑A67CHR‑11 (Plan and enactment).** Planned references and values establish no actual binding, launch value, execution witness or gate decision.

**CC‑A67CHR‑11a (Use anchors).** Recover the described entity, bounded context, CG-frame, path slice, publication scope, reference plane when current, and explicit time rule needed for the declared use.

**CC‑A67CHR‑11b (Expected guards).** Expected guard pins belong to `{USM.CompareGuard, USM.LaunchGuard}` and name the responsible gate when later event aggregation requires it.

**CC‑A67CHR‑11c (Spec baseline).** The baseline cites CN-Spec and CG-Spec and their selected editions. Cite the independently declared position separately when either reference is also used as a typed planned argument filling.

**CC‑A67CHR‑12 (Exact edition resolution).** Each used declaration and operation has one governing edition. Multiple applicable editions require a selection condition before use; a source list or implicit latest does not resolve them.

**CC‑A67CHR‑13 (Applicable crossing references).** Expected crossings cite only the relations, policies and bundle anchors their governing rules require; the baseline embeds no CL/Φ tables.

**CC‑A67CHR‑14 (Audit traceability).** Later Work audit can cite the exact WorkPlan and baseline locator and distinguish actual bindings or deviations from planned values.

#### A.19.CHR:7.3 - MVPK face checks (when projected)

**CC‑A67CHR‑15 (Views do not add meaning).**
Any `TechCard(…)` / `PlainView(…)` projection of the plan item does not introduce new assertions beyond the plan item.

**CC‑A67CHR‑16 (Fail-closed pins on claimful faces).**
If a face publishes an edition reference, retain that exact reference. For a comparability or launch claim, also publish every anchor required by the relations, receiving policy and gate actually used; a gate-owned USM pin retains its `GuardOwnerGateSlot`. Missing a required anchor makes that claim nonconformant. A note that only pins a new declaration edition needs no invented BridgeCard, UTS crossing row, CrossingBundle or gate event.

