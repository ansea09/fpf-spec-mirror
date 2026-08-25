---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:5"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__007_worked-examples.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:5 — Worked examples"
line_start: 28817
line_end: 28852
dependencies:
  - "A.10"
  - "A.16"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.P"
  - "C.27"
  - "C.29"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.8"
  - "E.9.DA"
  - "F.18"
keywords:
---

### A.19.SPR:5 - Worked examples

Each example starts with the smallest useful final wording. The second paragraph adds detail only for a machine-readable, replayed, or high-consequence use.

#### A.19.SPR:5.1 - Physical-system state

**Before:** “Pump 37 is in a good operating state.”

**After:** “Pump 37 satisfies `InspectionOperatingCondition`: its coolant temperature is 72 °C, within the 60–80 °C band, and its discharge pressure is 315 kPa, above the 300 kPa minimum.”

For a relied-on inspection decision, also name the reading time, measurement basis, condition edition, and the event that requires another check. Do not add those fields to a casual status sentence that no decision consumes.

#### A.19.SPR:5.2 - Work-entry readiness is not gate passage

**Before:** “Release 12 is ready.”

**After:** “At 10:00, the A.15.5 check found that `PlanItem-Deploy-12` satisfied its release-entry criterion and was ready for work entry until 10:30; recheck if a required input changes. No A.21 gate decision has yet been made.”

When another use must replay the check, add the exact WorkPlan, criterion, checking Work, input facts, result episteme, and reliance window. Add an A.21 sentence only if a distinct `OperationalGate(profile)` actually consumes declared checks and publishes its own decision.

#### A.19.SPR:5.3 - Source currentness

**Before:** “The source posture is good.”

**After:** “This review uses edition E7 as the accepted decision source. Recheck that use if the edition or the reviewed question changes.”

For automation or consequential reliance, also name the exact source-use relation, currentness result, use window, and the claim that must be reconsidered. The short sentence does not turn the source into evidence, assurance, gate passage, or FPF doctrine.

#### A.19.SPR:5.4 - Other direct repairs

- **Evidence.** Replace “evidence status incomplete” with “The current evidence path does not yet support reliance on claim C; obtain the missing calibration record and check again.” Add exact evidence and currentness references only when the receiving decision needs them.
- **Publication.** Replace “publication posture allows decision input” with “This publication exposes candidate input X for the decision; the decision rule still evaluates X.” Publication does not decide or assure by itself.
- **Mathematical lens.** Keep `LensUseAdmissibilityValue` in C.29 when its possible values and intended lens use are defined. State the practical result in ordinary words; the field does not establish evidence, assurance, release, or source authority.
- **Temporal claim.** Keep `dynClaimPosture` in C.27 when its values and temporal use are defined. Say which temporal claim is usable and for what purpose; the field does not upgrade its evidence or authority.
- **Project-side state.** Put review, dispatch, release, admission, or source-control status in the project record that carries it. A pattern may mention only the user-facing boundary needed for its own subject.

