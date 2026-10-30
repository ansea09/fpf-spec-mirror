---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:5"
section_title: "Archetypal Grounding - Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__006_archetypal-grounding-worked-slices.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:5 — Archetypal Grounding - Worked Slices"
line_start: 30955
line_end: 30992
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.2.8.PER"
  - "A.20"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.18"
  - "E.18.1"
  - "E.24"
keywords:
  - "WIP and flow policy"
  - "blocked readiness overread"
  - "commitment disposition"
  - "full-kit condition"
  - "launch gate"
  - "planned slot fillings"
  - "prospective permission inputs"
  - "readiness before work entry"
  - "resource-readiness refs"
  - "retrospective exercise evidence"
  - "work-entry readiness"
---

### A.15.5:5 - Archetypal Grounding - Worked Slices

The following constructed cases stipulate their project facts and illustrate the separate readiness, occurrence and reliance questions.

#### A.15.5:5.1 - Fixture deformation test

**Situation.** An accepted cooling-fixture ProblemCard has been carried through E.18.1 into `WorkPlan-LAB-043 : U.WorkPlan`; that P2W carry-through creates neither readiness nor target Work. Its `PlanItem-TEST-043` designates possible future performance `planned-fixture-deformation-test-043`, classifies the intended work as fixture-deformation testing under the plan's current scheme, selects `FixtureDeformationTestMethod-E2 : U.Method`, and relies on `FixtureDeformationTestProcedure-E5 : U.MethodDescription` with that admitted Method as its exact EntityOfConcern and substantive setup-limit claims under A.3.2. The plan records specimen and instrument choices labeled `SFI-043`. To use them as A.15.3 planned-filling rows, recover the selected declaration, its members and their actual-use conditions; until those are recovered, retain the ordinary plan choices and leave their declaration-local filling interpretation unresolved. The plan also records planned resource reservation `FixtureBayReservation-043` and intended performer-system and `FixtureTestTechnicianSystemRole` conditions. These choices remain content of this WorkPlan.

`FixtureTestEntryCriterion-E2` requires, for the proposed 09:00–09:30 UTC start window on 2026-07-27, a resolved specimen identity, heat-flow invariant claim, boundary-condition plan, sensor-calibration result, selected fixture-drawing edition, resource-availability claim, and fixture-test-technician assignment, all current for this use. The assignment basis is explicit once: `FixtureTestTechnicianAssignment` is a directly declared `U.SystemRoleAssignment` species. It defines the holder and assigned-kind positions, uses `FixtureTestSystemRoleKindDomain`, requires `FixtureTestTechnicianSystemRole`, and applies to this laboratory test. Its obtaining occurrence `FixtureTestTechnicianAssignment-043` has `FixtureTechnicianSystem-043` as holder and covers the proposed start window. `SFI-043` preserves the planned specimen and instrument choices; their actual preparation or use needs its own facts. The calibration result, its A.10 evidence path and currentness result, and the E.17 drawing-edition publication use remain separate inputs. The criterion explicitly treats known expiry or a recorded unresolved required-input status as failure and returns `notReady`. If the input or its status cannot be determined and no such failure is established, return `unknown`. A change to a consumed input, assignment coverage, resource availability or start window reopens the affected readiness conclusion; unchanged applicable input results remain reusable.

`LabMetrologySystem-2` and `LabOperationsCoordinatorSystem-1` are independently admitted Systems. For this constructed case, `CalibrationCheckingSystemRole` requires condition-sensitive calibration checking, and `ReadinessCheckingSystemRole` requires selection of readiness/preparation actions against the entry criterion; the stipulated observations support both classifications for this checking scope and window. The directly declared `LabMetrologyAssignment` and `LabOperationsCoordinationAssignment` species establish their holder/kind meanings, and case facts make `RA-LabMetrology-2-E7` and `RA-LabOperationsCoordinator-1-E4` obtain for those Systems and local kinds throughout 08:40–08:50 UTC on 2026-07-27.

The performance history identifies candidate occurrences `CalibrationCurrentnessCheck-043` during 08:40–08:45 and `FixtureEntryReadinessCheck-043` during 08:46–08:50 on that date, following `CalibrationCurrentnessCheckMethod-E1` and `FixtureEntryReadinessEvaluationMethod-E2` respectively. For each complete candidate, this constructed case stipulates the independently established A.1:4.2 construction. The local `LabCheckingWorkOccursWithinService@LAB043` declaration requires the complete checking occurrence to lie within admitted `LabQualityServiceSystem-043`'s declared calibration/readiness-checking boundary throughout its checking interval; the stipulated performance histories satisfy that condition. Together with each performer's established A.13 basis, these premises admit both candidates under A.15.1. Their typed `enactsMethod` and containing-System relations then obtain on those same grounds. Their separate F.6 attributions use the same obtaining assignments and the case's Work-assignment facts. Neither is the intended fixture test.

For this constructed case, the laboratory defines two local evaluation-result predicates. `calibrationExpiryReported(W, X, T)` holds when W's actual performer compares calibration result X's governing validity end with T, determines that it is no later than T, and completes that check by reporting `expired`. `fixtureReadinessReturned(W, R)` holds when W's actual performer evaluates the named plan item and proposed start window under `FixtureTestEntryCriterion-E2`, using the identified input facts, and completes that check by reporting R as its readiness verdict. Each claim concerns one terminal report in one checking episode; a recheck is another episode.

The constructed history stipulates that the calibration result's validity ended at 08:30 UTC on 2026-07-27. During `CalibrationCurrentnessCheck-043`, `LabMetrologySystem-2` makes that comparison and reports `expired` at 08:45. During `FixtureEntryReadinessCheck-043`, `LabOperationsCoordinatorSystem-1` evaluates `PlanItem-TEST-043` in `WorkPlan-LAB-043` for the proposed 09:00–09:30 start window. It uses the established calibration expiry and the recorded unresolved drawing-edition status, applies the criterion's explicit failure rule, and reports `notReady` at 08:50.

The C.2.1 episteme `FixtureTestEntryReadinessResult-E1`, whose exact EntityOfConcern is `WorkPlan-LAB-043`, reports that readiness verdict and its grounds for `PlanItem-TEST-043`: the calibration result is expired and the fixture-drawing edition remains unresolved. Its stop is `do not start planned-fixture-deformation-test-043`; its return condition is `obtain a current calibration result, select the drawing edition, and rerun the readiness check`. The preparation and checking Work occurred; the target test did not. No A.21 gate decision or A.2.8.PER permission result follows from this readiness result.

**What changes in practice.** The team withholds the target test and prepares the current calibration and selected drawing. After those inputs are available, it reapplies the criterion and reuses other unchanged applicable grounds. Any assignment of that preparation has its own allocation basis; the readiness result itself supplies no duty or target Work.

#### A.15.5:5.2 - Documentation Repair Probe

Situation: an assisting agent can run a reversible documentation probe to find source-currentness gaps.

Use A.15.5 for the probe only if its work-entry decision needs a readiness criterion; an ordinary sufficient reversible probe needs no automatic formal plan or readiness result. When that branch is selected, apply the criterion to the probe's WorkPlan and return the bounded value. If the account later claims the performed probe as a dated Work, recover its A.13 core and independent A.15.1 admission, adding F.6 only for precise attribution. A target-repair readiness question is then evaluated separately; the probe plan, readiness, actual occurrence and target-repair result establish different claims.

#### A.15.5:5.3 - Release screen with separate readiness, gate, and permission windows

At 10:00 UTC on 2026-07-27, the evaluator applies `ReleaseEntryCriterion-E3` to `ReleasePlan-E7` and `PlanItem-Deploy-12`. The result says `ready` for reliance only in `[10:00, 10:30)` and requires recheck when a consumed source, resource, assignment, permission or gate input changes. All times below use UTC on that date.

At `10:05`, the current A.21 application of profile `Release-Core-E4` consumes that readiness result through one identified `GateCheckApplicationResult`, cited by its `GateCheckRef`, among the complete effective check set. The gate returns a `GateDecisionResult` with `decisionValue=pass` for `[10:05, 10:20)`; `DecisionLogRef=ReleaseGateLog-12` cites the separate log recording that result. That gate result is not the readiness result and does not institute permission.

Separately, exact A.2.8.PER `GrantedPermissionRelation@Context` occurrence `DeployGrant-12` covers the named beneficiary and deployment action for `[09:00, 11:00)`. `DeployNonProhibitionFinding-E2` reports `nonProhibited` from its named current frame, explicitly complete for this use, in evaluation window `[10:00, 10:15)`; it is not the grant. A `PermissionNormConflictFinding@Context`, if an incompatible current norm is established over the same content and window, would be a third permission-side input and an unresolved disposition would stop the use. A policy that requires readiness, gate passage, a current grant, and the frame-relative non-prohibition result may rely on those distinct inputs at `10:10`; it must re-evaluate the relevant branch when any window ends or a conflict appears. None of them proves that deployment Work occurred. A.15.1 identifies that Work only after its dated occurrence basis obtains.

If a dashboard shows green but the readiness result or its reliance window, the current A.21 profile application and gate result, or the required permission value and qualification window cannot be recovered, keep the display at source finding under A.15.4. Recover the gate result directly or through `ReleaseGateLog-12`; loss of the log alone need not block reliance on a fully recoverable result. Open the A.10 evidence-provenance and currentness question when that basis for a consumed claim is unresolved.

