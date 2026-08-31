---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:13"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__015_archetypal-grounding-worked-cases.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:13 — Archetypal Grounding - worked cases"
line_start: 97393
line_end: 97453
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:13 - Archetypal Grounding - worked cases

#### F.15:13.1 - Activity and task under two run schemes

The slice resolves `activity` under `PROVORunScheme-2026` and `task` under `IEC61131RunScheme-2026` as two exact F.17 SchemeSenseCells. A named comparison use is current.

F.15 result:

* SCR-F15-S3 checks each exact triple; shared run-language does not merge them.
* SCR-F15-S12 requires an obtaining F.9 occurrence before the comparison uses a semantic relation. Its Card is optional and its bounded-use claim is separate.
* Any F.17 row must pass its own gate. It may contain the exact cells needed by the row use; table shape does not create the row.
* An `ExecutionSystemRoleKindDescription` remains an F.4 episteme about one exact local `ExecutionSystemRole` under one scheme; it does not describe both cells, assign a system, or prove work.
* If a later `task` sense becomes cyclic while the `activity` sense remains non-periodic, RSCR-F15-E4 and E9 compare exact later cells and Bridge candidates; evidence may change the use claim or reliance without silently rewriting the prior Bridge.

Suppose `CheckRun-17` is dated assessment `U.Work`, `CheckMethod-17` is its semantic `U.Method`, `CheckInterval-17` is the Work interval, and `HarnessSystem-17` is the containing System. `Evaluator-17` is the admitted `U.System` that performs the Work using that Method during `CheckInterval-17`. First recover Evaluator-17's A.13 core for this action, including declared assignment species `EvaluatorAssignmentSpecies-17` and one obtaining occurrence `EvaluatorAssignment-17` with every required participant value, Evaluator-17 as holder, and interval coverage. A.15.1 then independently admits `CheckRun-17` from its performance history, enacted Method, interval, and containing-System relation. Because this example also claims performance under `EvaluatorAssignment-17`, F.6 afterward links the already admitted Work to that same assignment.

`ApplySCR-S12-17` is the exact A.6.1 rule application and bindings. `BridgeRuleResult-17` is a separate C.2.1 result claim; `WitnessTrace-17` and its A.10 path are separate again. `UnificationConformanceRecord-17` merely cites those admitted refs. Publishing the record requires its own E.24.PUB occurrence, form, and carrier.

#### F.15:13.2 - Service availability across service and observation schemes

The slice contains one service-management status value/use and one uptime-observation claim under different effective schemes, plus exact cells only for the naming use that addresses them.

F.15 result:

* SCR-F15-S14 requires F.10 for the status family/value, target, scope, window, source condition, and intended use, or the exact defining or testing rule for the current status claim.
* A named cross-local comparison must pass SCR-F15-S12 and S13; the row or shared `availability` label does not create the Bridge.
* Observation evidence and A.10 reliance are not the status value, comparison result, assurance claim, or F.15 result.
* Use B.3 only when its assurance claim or material-reliance threshold is current; the slice establishes no assurance by inclusion.

#### F.15:13.3 - Rename a SystemRoleKindDescription without changing the described kind

`IncidentReviewerSystemRoleKindDescription@t0` and `ServiceIncidentReviewerSystemRoleKindDescription@t1` describe the same exact `IncidentReviewerSystemRole` only if F.4's candidate domain, operative membership condition, intended member/non-member boundary, continuity rule, current `KindSignature`, effective scheme, and description claims support that continuity. A changed source, practice, or name alone decides neither sameness nor difference.

F.15 result:

* RSCR-F15-E7 compares the two exact description epistemes and the described local system-role kind.
* RSCR-F15-E8 permits F.13/F.18 alias or rename treatment only for expression change with value, scheme, sense, and use preserved.
* F.18 updates the NameCard; F.17 updates a public row only if that row use is current and its gate passes.
* If the described system-role kind or description claim changed, F.4 and the naming patterns create the corresponding new objects; F.15 does not declare continuity.

#### F.15:13.4 - Partial Bridge later claimed as equivalence

An exact `Partial-overlap` Bridge once obtained between an OWL subclass sense and an FCA order-edge sense. A later formal result claims equivalence inside one constrained fragment.

F.15 result:

* RSCR-F15-E9 keeps the prior occurrence fixed and identifies the exact later endpoint/profile candidate.
* RSCR-F15-E10 requires the Equivalence predicate and dependencies to be true for a separately identified occurrence; new witnesses or `CL` do not suffice.
* The constrained-fragment substitution is a separate bounded-use claim with its own rule, tolerance, polarity, and reliance.
* C.29 governs the mathematical-lens claim; F.15 checks that no description, Card, or result label silently strengthens the relation.

#### F.15:13.5 - Peak-hours status proposal

A team proposes `PeakHoursAvailabilityStatus` as a new family because one existing status is used in another time window.

F.15 result:

* SCR-F15-S14 fails if F.10 or the applicable status rule shows only a changed window or use.
* RSCR-F15-E11 compares the exact family/value, target, scope, window, source condition, and use rather than the suffix.
* Use F.10 or the applicable status pattern for the status claim; F.14/F.8/F.18 block a new durable name until a distinct governed value is independently recovered.

