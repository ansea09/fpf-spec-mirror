---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__007_archetypal-grounding-parallel-domains.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:6 — Archetypal grounding (parallel domains)"
line_start: 25109
line_end: 25147
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.2.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.32.P2S"
  - "E.17"
  - "E.24"
  - "E.24.UK"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "PlanItem content"
  - "horizon"
  - "intended-work episteme"
  - "no actuality by plan"
  - "performer and capability conditions"
  - "positive or governed-negative local fulfilment assertion"
  - "possible future performance"
  - "present EntityOfConcern"
  - "reusable predicate semantics"
  - "variance"
---

### A.15.2:6 - Archetypal grounding (parallel domains)

#### A.15.2:6.1 - Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025-08-12-E3 : U.WorkPlan` is one C.2.1 episteme. Its present `EntityOfConcern` is exact existing system `OR-Service-System-12 : U.System`; its effective reference scheme is `HospitalORPlanningScheme-E4`; its horizon is `2025-08-12T00:00:00+03:00/2025-08-13T00:00:00+03:00`. Proposed case performances remain ClaimGraph designators and are not dated Work occurrences.
* **One `PlanItem`:** `Case_1_Appendectomy` coordinates proposed performance `PlannedAppendectomy-Case1` through the following exact content.

| PlanItem concern | Filled value |
|---|---|
| target method | `LaparoscopicAppendectomyMethod-E2 : U.Method` |
| planned window | `2025-08-12T09:00:00+03:00/2025-08-12T10:30:00+03:00` |
| intended performer and role conditions | one holder satisfying `SurgeonRole` and `AppendectomyLeadCapability-v3`; one holder satisfying `AnesthetistRole` and `ORAnesthesiaCapability-v2`; these are intended conditions, not role assignments |
| budget and reservations | 90 minutes of `OR-3`, one `SterileKit-A17`, and consumables budget `ORCase1-Consumables-B3` |
| dependency | positive `PreOpClearance-Case1-E2` claim must be current before the planned window starts |
| acceptance target | `procedureCompleteBy10:30`, compared under B.1.4 against the exact Work extent after Work occurs |
| baseline | exact C.2.1 episteme `OR-DayBaseline-2025-08-05-E1` |

* **Later Work:** A.15.1 independently identifies `AppendectomyWork-2025-08-12-Case1 : U.Work` with `workContinuityPolicyRef = SingleProcedureFromAnesthesiaStartToHandover-E1` and temporal extent `2025-08-12T09:04:00+03:00/2025-08-12T10:21:00+03:00`. F.6 `performedUnderAssignment` obtains for `RA-Surgeon-DrK-2025-08-12` and `RA-Anesthetist-DrM-2025-08-12`; A.15.1 `enactsMethod` obtains for `LaparoscopicAppendectomyMethod-E2`; B.1.4 supplies the exact within-window comparison. The plan created none of those facts.
* **Named one-case policy:** `ORCase1FulfilmentPolicy-E2` is one exact C.2.1 episteme about exact plan episteme `OR_DayPlan_2025-08-12-E3`, interpreted under `HospitalORPlanningScheme-E4`. Its ClaimGraph is limited to item `Case_1_Appendectomy` and states positive polarity only when the identified Work enacts the target Method, both required `performedUnderAssignment` relations obtain, and its extent lies inside the planned window. It uses only those four facts for this local conclusion, does not travel to another plan episteme, and admits no fulfilment relation kind.
* **Visible result:** C.2.1 assertion episteme `OR-DayPlan-Case1-Fulfilment-Assertion-E1` has `OR_DayPlan_2025-08-12-E3` as its exact `EntityOfConcern`; its ClaimGraph names `AppendectomyWork-2025-08-12-Case1`, item `Case_1_Appendectomy`, policy `ORCase1FulfilmentPolicy-E2`, the four supporting facts, and positive polarity. The result says that this Work satisfies this plan item under that policy. It does not rewrite the plan and does not assert a universal relation.
* **Nearest false shortcut:** a theatre log row carrying key `Case_1_Appendectomy` and start time `09:04` establishes neither `performedUnderAssignment` nor `enactsMethod`. Without those independently obtaining facts the local conclusion returns `missing-information`; matching labels and times produce neither negative polarity nor fulfilment.
* **Edition boundary:** `OR_DayPlan_2025-08-12-E3` is the first plan episteme used for this day, so this case has no `EpistemeEditionRelation` and needs no change note. If planners later change its ClaimGraph but establish no edition predicate, C.2.1 identifies a new, non-continuing plan episteme. Reusing the day-plan label or adding a `Rev-4` note cannot turn that replacement into a continuation; a later policy must name whichever exact plan it judges.

#### A.15.2:6.2 - Fab maintenance weekend (asset reservations)

* **WorkPlan:** `Fab_Maintenance_W36` is interpreted under `FabMaintenancePlanningScheme-E3`, has horizon `[2025-09-06T00:00Z, 2025-09-08T00:00Z)`, and concerns already identified `Fab-Production-System-4 : U.System`. `Tool_42` and `Tool_13` remain exact assets named by the PlanItems; they are not an unproved joint EntityOfConcern.
* **`PlanItem` content:** `Tool_42 chamber clean` under `ChamberCleanMethod-E2`; `Tool_13 calibration` under `ToolCalibrationMethod-E1`; the ClaimGraph carries an exact exclusivity constraint with production windows under the named scheduling policy, not a reusable `MutuallyExclusive_pl` relation kind.
* **Reservations:** nitrogen, DI water, metrology window.
* **Later local assertion:** The exact chamber-cleaning Work occurrence is identified independently as an individual admitted under `U.Work`. `FabChamberCleanPlanUsePolicy-E1` asks whether that Work enacted `ChamberCleanMethod-E2`, stayed inside the planned window, and kept nitrogen use within the reserved amount. A.15.1, B.1.4, and B.1.6 establish those three facts. In this transfer probe they all obtain, so a separate C.2.1 assertion about the plan states positive fulfilment, early completion, and nitrogen underrun. A shared item label or reservation row supplies none of those facts.

#### A.15.2:6.3 - Data-center rollout (multi-context plan)

* **WorkPlan:** `DC_Rollout_Phase-2` is interpreted under `DCOperationsPlanningScheme-E5`, has horizon `[2025-09-01T00:00Z, 2025-09-15T00:00Z)`, and concerns already identified `Service-A-Operations-System : U.System`. The Security Audit scheme remains a separate interpretation source used only through the branch below.
* **Interpretation boundary:** Operations uses `DCOperationsPlanningScheme-E5`; Security Audit uses `SecurityAuditScheme-E4`. Their acceptance criteria remain separate; apply the branch in checklist item 7 before proposing any cross-context reuse.
* **Bridge premise:** exact F.17 cells `OperationsReadyCell-E3` and `SecurityAuditPassedCell-E2` participate in F.9 Bridge `OpsAuditReadinessOverlapBridge-E1` under `OpsAuditPartialOverlapProfile-E1`. The Bridge obtains as `partial-overlap`: both senses exclude a known blocking security defect, while Operations readiness also requires rollback rehearsal and live monitoring and the audit sense applies its own security criteria.
* **Rejected verdict transfer:** C.2.1 claim `AuditPassAsOperationsReadyUse-E1` proposes copying `GateDecision=pass` from A.21 gate `SecurityAuditGate-E2` into an A.15.5 work-entry readiness result, from the audit cell to the Operations cell, by identity transfer and with zero tolerance for omitted readiness conditions. The claim is negative because the two senses do not align on rollback rehearsal or monitoring readiness. A.10 evidence-provenance path `OpsAuditTransferEvidencePath-E1` has `RelianceDisposition=pass` for that negative claim, so the team retains the A.21 audit decision and evaluates Operations readiness separately under A.15.5. The obtaining Bridge remains true. A narrower plan use may cite the audit decision as one readiness input; it still cannot transfer the verdict.
* **`PlanItem` content:** `Deploy Service A`, `Pen-test A`; exact dependency and window claims name their predicates and conditions inside the plan ClaimGraph.
* **Later local assertions:** Exact deployment and audit Work occurrences are identified independently as individuals admitted under `U.Work`. Separate operations and audit evaluations apply their own targets and produce separately governed verdicts; plan-use assertions state exact local fulfilment and per-context comparison without adding those actual facts to the plan content or creating one cross-context fulfilment relation.

