---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:5"
section_title: "Archetypal Grounding - Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__006_archetypal-grounding-worked-slices.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:5 — Archetypal Grounding - Worked Slices"
line_start: 26194
line_end: 26223
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

#### A.15.5:5.1 - Fixture deformation test

**Situation.** An accepted cooling-fixture ProblemCard has been carried through E.18.1 into `WorkPlan-LAB-043 : U.WorkPlan`; that P2W carry-through creates neither readiness nor target Work. Its `PlanItem-TEST-043` designates possible future performance `planned-fixture-deformation-test-043`, classifies the intended work as fixture-deformation testing under the plan's current scheme, selects `FixtureDeformationTestMethod-E2 : U.Method`, and relies on `FixtureDeformationTestProcedure-E5 : U.MethodDescription` only for the setup limits stated in that edition. The plan also carries specimen and instrument choices through `SlotFillingsPlanItem-SFI-043`, planned resource reservation `FixtureBayReservation-043`, and intended technician-role conditions. None is target test Work.

`FixtureTestEntryCriterion-E2` requires, for the proposed start window, a resolved specimen identity, current heat-flow invariant claim, current boundary-condition plan, current sensor-calibration result, selected fixture-drawing edition, resource-availability claim, and an obtaining technician assignment that will cover the intended window. The A.15.3 rows preserve only the planned specimen and instrument choices; the calibration result, its A.10 evidence-provenance path and separate currentness result, and the E.17 drawing-edition publication use remain separately governed inputs. The criterion returns `notReady` when an explicitly required input is determined expired or unresolved; unavailable facts return `unknown`. Any input revision, assignment gap, resource loss, or start-window change ends reliance and requires recheck.

`CalibrationCurrentnessCheck-043 : U.Work` was performed by `LabMetrologySystem-2 : U.System` under obtaining `RA-LabMetrology-2-E7`, enacted `CalibrationCurrentnessCheckMethod-E1`, and determined that the cited sensor-calibration result expired before the proposed start. Separately, `FixtureEntryReadinessCheck-043 : U.Work` was performed by `LabOperationsCoordinatorSystem-1 : U.System` under obtaining `RA-LabOperationsCoordinator-1-E4`, enacted `FixtureEntryReadinessEvaluationMethod-E2`, and applied the criterion to the exact plan inputs.

The C.2.1 episteme `FixtureTestEntryReadinessResult-E1`, whose exact EntityOfConcern is `WorkPlan-LAB-043`, states `notReady` for `PlanItem-TEST-043`: the calibration result is expired and the fixture-drawing edition remains unresolved. Its stop is `do not start planned-fixture-deformation-test-043`; its return condition is `obtain a current calibration result, select the drawing edition, and rerun the readiness check`. The preparation and checking Work occurred; the target test did not. No A.21 gate decision or A.2.8.PER permission result follows from this readiness result.

**What changes in practice.** The team stops the target test, assigns the two named preparation moves, and reruns the exact criterion after their inputs are current; it neither turns the existing plan into performed Work nor asks a gate or permission label to stand in for the missing facts.

#### A.15.5:5.2 - Documentation Repair Probe

Situation: an assisting agent can run a reversible documentation probe to find source-currentness gaps.

For the probe itself, apply one exact readiness criterion to its WorkPlan and PlanItem and return the local readiness value with its relied-on inputs, window, and recheck condition. If the probe is actually run, identify that dated occurrence as `U.Work` under `A.15.1`, with its performer system, obtaining role assignment, enacted method, extent, and actual bindings; then run a separate readiness check for the target repair. The probe plan, probe readiness result, performed probe, and target-repair readiness result are four distinct claims.

#### A.15.5:5.3 - Release screen with separate readiness, gate, and permission windows

At `10:00`, `ReleaseReadinessCheck-12 : U.Work` evaluates `ReleasePlan-E7`, `PlanItem-Deploy-12`, and `ReleaseEntryCriterion-E3`. The persisted result says `ready` for reliance only in `[10:00, 10:30)` and requires recheck after any source, resource, assignment, permission, or gate-input change.

At `10:05`, exact A.21 `OperationalGate(Release-Core-E4)` consumes that readiness result as one declared `GateCheckRef` among its current check set and publishes `GateDecision=pass` with `DecisionLogRef=ReleaseGateLog-12` for `[10:05, 10:20)`. That gate result is not the readiness result and does not institute permission.

Separately, exact A.2.8.PER `GrantedPermissionRelation@Context` occurrence `DeployGrant-12` covers the named beneficiary and deployment action for `[09:00, 11:00)`. `DeployNonProhibitionFinding-E2` reports `nonProhibited` from its named current frame, explicitly complete for this use, in evaluation window `[10:00, 10:15)`; it is not the grant. A `PermissionNormConflictFinding@Context`, if an incompatible current norm is established over the same content and window, would be a third permission-side input and an unresolved disposition would stop the use. A policy that requires readiness, gate passage, a current grant, and the frame-relative non-prohibition result may rely on those distinct inputs at `10:10`; it must re-evaluate the relevant branch when any window ends or a conflict appears. None of them proves that deployment Work occurred. A.15.1 identifies that Work only after its dated occurrence basis obtains.

If a dashboard shows green but the exact readiness result or its reliance window, the current `OperationalGate(profile)` and `DecisionLogRef`, or the required permission value and qualification window cannot be recovered, the display remains a cue, an appearance-based reliance question, or a prompt to open the exact A.10 evidence-provenance and applicable currentness question for the claim being relied on. It is not readiness, evidence sufficiency, gate passage, authorization, or performed work by appearance.

