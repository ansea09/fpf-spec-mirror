---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:9"
section_title: "Work-to-aggregation interface"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__011_work-to-aggregation-interface.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:9 — Work-to-aggregation interface"
line_start: 25423
line_end: 25456
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:9 - Work-to-aggregation interface

`A.15.1` makes the occurrence-side inputs recoverable without storing them in the occurrence: a separate assertion or description episteme designates exact Work individuals or work parts and states their temporal extents and the separately obtaining resource-use relations selected for aggregation. `B.1.4` identifies the temporal-aggregation claim and result; `B.1.6` identifies the resource-aggregation claim, ledger, and result. Neither becomes a Work field.

#### A.15.1:9.1 - Temporal aggregation return

For utilization, lead time, cycle time, phase coverage, or another temporal roll-up, use `B.1.4`. Name the exact work refs, carrier or aggregation concern, time window, coverage and non-overlap conditions, aggregation policy, and admissible use there. Union, convex hull, and optional `Gamma_time` notation are properties of that recovered temporal aggregation, not fields or identity invariants of a Work occurrence.

When the exact `B.1.4` result selects the Work-interval profile, retain these use-specific choices:

* **Union of intervals** for utilization or availability: preserve every covered instant and do not count overlap twice.
* **Convex hull** `[min t_start, max t_end]` for lead time or cycle time: preserve elapsed span from first start to last end, including gaps.
* **Declared algebraic behavior:** for either exact set-based policy, duplicate input is idempotent, input order is irrelevant, and adding intervals cannot shrink the union or hull. If another policy lacks those properties, name it rather than borrowing the union/hull result.

Never switch union and hull silently between KPIs. The formulas above profile a recovered B.1.4 aggregation over Work intervals; the selected B.1.4 claim, not A.15.1, states the temporal result.

#### A.15.1:9.2 - Resource aggregation return

For a total or ledger over performed resource-use facts, use `B.1.6`. Name the exact work refs, typed resource-accounting basis, units, measurement or evidence refs, holon delimitation, time window, overlap or deduplication policy, aggregation rule, and admissible use there. Additivity, allocation, traceability, the aggregate ledger, and optional `Gamma_work` notation belong to that recovered resource-aggregation claim, not to Work-occurrence identity.

**Filled heterogeneous BuildOps route.** Published case-local specification `BuildOpsResourceUseRelations-v12` declares `BuildWorkUsesResource@BuildOps-v12(work, resource, amount, unit, extent)` with participant order `<work, resource, amount, unit, extent>`. Its test requires the named Work actually to occupy or consume the named resource during that extent, with the amount measured in the named unit. Separate case facts state that `ReleaseBinary12_BuildWork_2026-07-21T0900_0912` occupied `BuildPoolCPU_A` for `24` `runner-core-minute` during `09:00-09:12`, and consumed `0.84` `kWh` of `GridElectricity_BuildZone3` within `BuildService_A_Delimitation-v12` during the same extent. Those facts make relation occurrences `BuildRunUsedCPU_12` and `BuildRunUsedElectricity_12` obtain with those exact participant tuples. `BuildRunnerAllocationEvidence_12` and `BuildZone3EnergyMeasurement_12` support the facts; neither record is the resource use, and neither relation is a field of the Work.

B.1.6 result `BuildResourceAggregation_12 : WorkResourceAggregation@Context` names concern `Build12MeasuredResourceUse`, bounded context `BuildOps-v12`, that exact Work, and the two relation occurrences. It uses typed basis `BuildComputeAndElectricityBasis-v12`, measures `BuildRunnerCoreMinuteMeasure_12` and `BuildZone3KWhMeasure_12`, evidence refs `BuildRunnerAllocationEvidence_12` and `BuildZone3EnergyMeasurement_12`, holon delimitation `BuildService_A_Delimitation-v12`, and window `09:00-09:12`. Policy `BuildResourceRelationDedup-v12` counts each exact relation occurrence once across repeated evidence or a parent/child view. Rule `BuildTypedResourceVectorSum-v12` adds only entries of the same resource type and unit. Ledger `BuildResourceLedger_12` contributes `<BuildRunUsedCPU_12, 24 runner-core-minute>` and `<BuildRunUsedElectricity_12, 0.84 kWh>` and returns `Build12MeasuredResourceVector = <24 runner-core-minute, 0.84 kWh>` without summing or converting its unlike components. Its admissible use is the measured resource-disclosure input for Build 12; it proves no Work identity, production result, efficiency, cost, sustainability verdict, or acceptance.

When an exact `B.1.6` aggregation must allocate shared or overlapping resource use, retain these non-default policy examples:

* **Parent attribution:** book a declared shared fixed value once at the parent and independently measured variable values at children.
* **Pro rata by wall time:** divide a declared shared value by relative durations only when that driver is admissible for the resource basis.
* **Driver based:** allocate by a measured driver such as CPU share, weight, or priority and state the exact allocation rule that uses it.

Whichever policy is selected, add only disjoint or explicitly deduplicated values and keep every aggregate figure traceable to its contributing Work refs and evidence. A policy label alone establishes neither allocation nor ledger value.

A Work publication or KPI may cite either result through the exact E.17 publication-use relation that projects it. It may not recreate an unselected operator, infer an aggregate from parthood, or turn an aggregation record into a Work occurrence.

