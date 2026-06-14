---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__008_conformance-checklist.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:7 — Conformance Checklist"
line_start: 21856
line_end: 21885
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:7 - Conformance Checklist

| ID          | Check (normative)                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CC-A15.3-01 | The object is a `U.WorkPlan.PlanItem` with `kind = SlotFillingsPlanItem`, and obeys WorkPlan guardrails (no logs or actual fillings, no step logic).                                                                           |
| CC-A15.3-02 | `target_slot_bearing_description_ref` is present and identifies a real slot-bearing description (kit or suite); SlotKinds in rows are interpreted only within that slot-bearing description.                                                                      |
| CC-A15.3-02a | If the PlanItem is used as a reproducibility baseline and the slot-bearing description is edition-addressable, `target_slot_bearing_description_ref` is edition-pinned (e.g., `…DescriptionRef.edition`).                                      |
| CC-A15.3-02b | `target_slot_bearing_description_ref` is a **Description-scoped** ref (e.g., `MechSuiteDescriptionRef`, `…KitDescriptionRef`) and MUST NOT target `MechanismDefinitionRef`. |
| CC‑A15.3‑02c (single slot-bearing description) | A `SlotFillingsPlanItem` targets exactly one slot-bearing description via `target_slot_bearing_description_ref`. If multiple slot-bearing descriptions are involved, they MUST be represented by multiple PlanItems (one per slot-bearing description). |
| CC-A15.3-03 | `described_entity_ref` is present. If `grounding_holon_ref` or `reference_plane` is omitted, the omission must be unambiguously derivable from cited context publications or records (e.g., the pinned CG-frame and specification context). |
| CC-A15.3-03a | `described_entity_ref` is a concrete RefKind (no generic “EntityRef” placeholder is introduced by this pattern). |
| CC-A15.3-04 | Context anchors are explicit at least to `bounded_context_ref`; if the fillings serve legality or selection, then CG-frame and path-slice anchors are present.                                                           |
| CC-A15.3-05 | Time is explicit: the item includes `Γ_time_selector` or `Γ_time_rule_ref`; “latest” or “current” without explicit `Γ_time` is nonconformant.                                                                             |
| CC-A15.3-05a | Exactly one of `Γ_time_selector` and `Γ_time_rule_ref` is present (XOR); both-present or both-absent is nonconformant. |
| CC-A15.3-06 | `planned_fillings` is the authoritative source: each row is `⟨slot_kind, planned_filler, edition_pin?⟩`; each planned filler is explicit `ByValue` vs `ByRef(ref-of-concrete-RefKind)` and conforms to the slot-bearing description’s SlotSpec discipline (no silent slot-meaning changes). |
| CC-A15.3-06a | Unless the slot-bearing description declares a slot as multi-valued, `planned_fillings` contains **no duplicate** `slot_kind` rows (duplicate keys ⇒ nonconformant). |
| CC-A15.3-06b | If both a row and its `ByRef(…)` filler carry edition pinning, they MUST agree; mismatch ⇒ nonconformant. |
| CC-A15.3-07 | Any present “indices” (`planned_*_ref_index`) are derivable projections of `planned_fillings` and are not independently maintained; mismatch ⇒ nonconformant.                                                         |
| CC-A15.3-08 | The PlanItem contains no `GateDecision` or `DecisionLog`, and makes no claim that a crossing occurred; only expected policy pins may be stated.                                                                      |
| CC-A15.3-09 | The PlanItem contains no `FinalizeLaunchValues` witness and no launch-time actuals; launch values are finalized only in Work enactment.                                                                             |
| CC-A15.3-10 | If `expected_usm_guard_pins` includes `USM.LaunchGuard`, the PlanItem contains sufficient pins and references (explicit `Γ_time_selector` or `Γ_time_rule_ref`, pinned editions, evidence pin anchors, and `guard_owner_gate_ref` or an unambiguous derivation) to make downstream guard execution possible.     |
| CC-A15.3-10a | In this pattern, “evidence anchors” are expressed as pin refs (e.g., SCR pins or RSCR pins). Do not introduce a generic `EvidenceHookRef` token here; use concrete pin refs. |
| CC-A15.3-11 | The PlanItem does not claim to set or mutate the edition vector (`editions{…}` or `edition_key`). It may pin editions and may state *expected* edition-sensitive crossings, but edition changes themselves are crossings (gate-level or work-level witnesses). |
| CC-A15.3-12 | When used as a baseline for enactment, execution-time deviations are recorded as Work variance and the baseline PlanItem is not rewritten (“no backfill”); the Work Audit cites the PlanItem (preferably by edition-addressable ref) as the planned baseline reference.  |
| CC-A15.3-12a | Any change to edition-pinned refs that would alter the effective edition-key for legality or selection MUST NOT be retroactively applied to the already-cited baseline PlanItem. Treat it as (i) a new PlanItem edition for subsequent enactments and (ii) variance or required crossing witnesses for the enactment that deviated. |
| CC-A15.3-13 | If `expected_crossing_policy_refs` is present, it contains references and policy identifiers only (BridgeCardRef + policy-id refs + plane ids); it MUST NOT embed CL, Φ, Ψ, or Φ_plane tables or introduce non-Bridge transport edges. |
| CC‑A15.3‑13a (crossing bundles are not witnesses) | `expected_crossing_bundle_refs` (if present) is used only to cite already‑published, context‑constant CrossingBundle baselines; it MUST NOT be used to claim that a crossing occurred for this enactment, nor to substitute for gate-level or work-level crossing witnesses. |
| CC‑A15.3‑14 (view projection discipline) | Any `U.View` projection of a `SlotFillingsPlanItem` (e.g., `TechCard(PlanItemRef)`, `PlainView(PlanItemRef)`) MUST be an explicit projection that introduces no additional claims, defaults, or rows beyond the PlanItem; any additional semantics on the view is nonconformant. |
| CC-A15.3-15 | Lower, repair, and refresh conditions are explicit: missing target description, SlotKind interface, EntityOfConcern, context, time, concrete RefKind, edition pin, guard pin, evidence pin, crossing policy, or cited-baseline variance lowers or reopens the planned-baseline claim rather than widening it. |

