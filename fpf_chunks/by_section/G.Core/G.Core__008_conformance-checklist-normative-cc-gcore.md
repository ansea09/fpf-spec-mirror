---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:7"
section_title: "Conformance checklist (normative) — CC‑GCORE"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__008_conformance-checklist-normative-cc-gcore.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:7 — Conformance checklist (normative) — CC‑GCORE"
line_start: 90996
line_end: 91021
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:7 - Conformance checklist (normative) — **CC‑GCORE**

Conformance items are authoring obligations and are enforced transitively by `CC‑Gx‑CoreRef` in every `G.x`.

| ConformanceId        | Statement |
| -------------------- | --------- |
| **CC‑GCORE‑DEL‑1**   | A conforming `G.Core` SHALL be delegation-first: if a norm is already governed by `A.6.7`, `A.15.3`, `A.19`, `G.0`, `A.19.CHR`, or a relevant Part E pattern, `G.Core` cites that governing definition rather than duplicating semantics. |
| **CC‑GCORE‑CN‑CG‑1** | Any pattern in Part G that builds on `G.Core` SHALL cite `CN‑Spec` and `CG‑Spec` as the only spec-legality surfaces and SHALL NOT introduce shadow specs (incl. complying with `SuiteObligations.transport_declarative_only` and `SuiteObligations.cg_spec_cite_required_for_numeric_ops`). |
| **CC‑GCORE‑OBL‑1**   | A conforming `G.Core` SHALL treat the obligation vocabulary in `A.6.7:4.2` as the canonical naming surface for Part‑G‑wide obligations and SHALL NOT introduce competing obligation names for the same norms. |
| **CC‑GCORE‑CROSS‑1** | A Part‑G pattern that introduces or consumes crossings SHALL enforce `SuiteObligations.bridge_only_crossings` and `SuiteObligations.crossing_visibility_required` (CrossingBundle per E.18); SHALL prohibit implicit crossings; SHALL treat `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL/CrossingBundle registries and UTS rows for crossing artefacts) as `RSCRTriggerKindId.CrossingBundleEdit` (and, when an edition pin is involved, also `RSCRTriggerKindId.EditionPinChange` per multi‑cause discipline); and SHALL cite `SuiteObligations.two_bridge_rule_for_described_entity_change` through its canonical governing definition. |
| **CC‑GCORE‑GUARD‑1** | A Part‑G pattern SHALL treat `GuardDecision := {pass|degrade|abstain}` as the only admissibility/eligibility decision domain (`SuiteObligations.guard_decision_tristate(pass|degrade|abstain)`); `unknown` SHALL NOT silently coerce to `pass` (`SuiteObligations.unknown_never_coerces_to_pass`); “sandbox/probe‑only” SHALL be expressed via SoS‑LOG branch pins (policy/FailureBehavior) (see `C.23`), not as an extra decision value. |
| **CC‑GCORE‑PEN‑1**   | A Part‑G pattern SHALL route penalties/assurance loss to the **R lane (`R_eff`) only** (`SuiteObligations.penalties_route_to_r_eff_only`) and SHALL preserve **F/G invariants** under penalties (penalties do not alter legality/invariant lanes). |
| **CC‑GCORE‑SET‑1**   | A Part‑G pattern SHALL preserve set-return semantics for partial orders and SHALL prohibit silent scalarization/totalization (`SuiteObligations.no_silent_scalarisation_of_partial_orders`, `SuiteObligations.no_silent_totalisation`); any scalar summary SHALL be report-only unless declared as a admissible comparator surface. |
| **CC‑GCORE‑SKP‑1**   | A Part‑G pattern SHALL preserve the suite/kit/pack distinction (A.19.CHR) and SHALL keep shipping concerns governed by their canonical governing patterns (e.g., G.10) rather than embedding shipping semantics into unrelated kits or core invariants. |
| **CC‑GCORE‑P2W‑1**   | A Part‑G pattern that uses planned baselines SHALL anchor them via `SlotFillingsPlanItem` in WorkPlanning (`SuiteObligations.planned_slot_filling_in_work_planning_only`) and SHALL finalize launch values only in WorkEnactment (`SuiteObligations.finalize_launch_values_in_work_enactment_only`); gate decisions remain separated per `SuiteObligations.gate_decision_separation`. |
| **CC‑GCORE‑LINK‑1**  | Every conforming `G.x` SHALL satisfy `G.Core:4.2` by providing a `G.x:<n> - G.Core linkage (normative)` section containing a `GCoreLinkageManifest` (incl. either `CoreConformanceProfileIds` or `CoreConformanceIds`, either `RSCRTriggerSetIds` or `RSCRTriggerKindIds`, and either `CorePinSetIds` or `CorePinsRequired` (or both)). Nil‑elision is permitted for `∅` fields. |
| **CC‑GCORE‑LINK‑2**  | Every conforming `G.x` SHALL include `CC‑Gx‑CoreRef` as the first checklist item; it SHALL make mandatory the effective `CoreConformanceIds` (including expansions of any `CoreConformanceProfileIds`) declared in the linkage manifest. |
| **CC‑GCORE‑UTS‑1**   | If a Part‑G pattern mints, deprecates, or evolves any public identifier, it SHALL publish/update the corresponding UTS entries and cite them via `UTSRowId` pins, delegating UTS semantics (twin labels, alias/deprecation discipline, edition pins) to its canonical governing definition `F.17 (UTS)`. |
| **CC‑GCORE‑ID‑1**    | When deduplicating, existing public CC ids in `G.x` SHALL NOT be deleted/renamed; they SHALL become delegation items to relevant `CC‑GCORE‑…` items. |
| **CC‑GCORE‑ID‑2**    | Public id continuity applies beyond CC item ids: `UTSRowId` rows, `RSCRTriggerAliasId` tokens (e.g., `T0…T7`), deprecation notices, and edition bumps SHALL preserve prior ids and express drift via alias/deprecation/edition evolution (never by reusing/redefining an old id). When downstream behaviour can change, the change SHALL emit a canonical `RSCRTriggerKindId` (e.g., `TokenizationOrNameChange`, `EditionPinChange`). |
| **CC‑GCORE‑TRIG‑1**  | A conforming `G.Core` SHALL define the canonical `RSCRTriggerKindId` catalogue and SHALL be its single writer. |
| **CC‑GCORE‑TRIG‑2**  | Any `G.x` that uses local trigger tokens SHALL provide (or cite) a `TriggerAliasMap` mapping each alias to canonical `RSCRTriggerKindId`. |
| **CC‑GCORE‑TRIG‑3**  | Any artefact that records RSCR/SCR/refresh reasons SHALL record canonical `RSCRTriggerKindId` (aliases may be recorded as labels only). |
| **CC‑GCORE‑TRIG‑4**  | A conforming `G.Core` SHALL keep `TriggerAliasMap.*` consistent with the governing patterns’ deprecated trigger alias catalogues (e.g., `G.11:T*`). Any change to an alias mapping SHALL be treated as refresh‑sensitive; at minimum it SHALL be recorded/emitted as `RSCRTriggerKindId.TokenizationOrNameChange` (and, if the mapped trigger kinds change, the corresponding canonical kinds apply as well). |
| **CC‑GCORE‑DEF‑1**  | A conforming `G.Core` SHALL maintain a Default Governing Definition Index for Part‑G defaults, ensuring each `DefaultId.*` names exactly one governing definition (a CC item or a policy id). All other patterns SHALL cite the governing definition and SHALL NOT state competing defaults. Any governing-definition change MUST be recorded as `RSCRTriggerKindId.DefaultGoverningDefinitionChange`. |

