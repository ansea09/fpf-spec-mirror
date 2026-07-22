---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:5"
section_title: "Archetypal Grounding - Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__006_archetypal-grounding-worked-slices.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:5 — Archetypal Grounding - Worked Slices"
line_start: 25821
line_end: 25858
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

#### A.15.5:5.1 - Fixture Deformation Work

Situation: a cooling-fixture team plans a deformation test. The ProblemCard is accepted, P2W has carried a heat-flow distinction into a work-planning question, and the team asks whether the test is ready to start.

```text
WorkEntryReadiness@Context:
  WorkEntryConcernRef: cooling-fixture deformation test
  BoundedContextRef: lab test before comparator run
  TargetWorkPlanRef: WorkPlan-LAB-043
  TargetPlanItemRef: PlanItem-TEST-043
  FullKitCondition:
    NeededInputRefs: specimen id, heat-flow invariant note, boundary-condition plan, sensor calibration record or certificate, fixture drawing edition
    KnownInputRefs: specimen id, heat-flow invariant note
    MissingInputRefs: sensor calibration record or certificate, fixture drawing edition
    GoverningPatternForEachMissingValue: A.15.3 for planned calibration-record filler, A.10 when calibration evidence or currentness is claimed, E.17 for drawing publication edition
    PlannedBaselineRef: SlotFillingsPlanItem-SFI-043
    StopOrDegradedUseRule: no launch until calibration and drawing edition are pinned
  CommitmentDisposition: blocked
  LaunchGateRef: LaunchGate-LAB-043
  StopCondition: do not start target test work
```

The readiness result blocks target work entry. It does not say the lab test occurred.

#### A.15.5:5.2 - Documentation Repair Probe

Situation: an assisting agent can run a reversible documentation probe to find source-currentness gaps.

Use `WorkEntryReadiness@Context` only for the readiness of the probe or repair work. If the probe is actually run, record the probe as `U.Work` under `A.15.1` and then recheck readiness for the target repair.

#### A.15.5:5.3 - Release Screen

Situation: a release dashboard shows a green readiness badge.

If the current claim is "the release gate passed", use A.21 and recover `OperationalGate(profile)`, declared checks, aggregate, `GateDecision`, `DecisionLogRef`, scope, currentness, and window. If those fields are not recoverable, the display may be a reliance appearance for `A.15.4`, an evidence question, or a readiness indication. It is not gate passage by appearance.

