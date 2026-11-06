---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "Repair State and Status Wording"
section_id: "A.19.SPR:5"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__007_worked-examples.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "A.19.SPR — Repair State and Status Wording"
  - "A.19.SPR:5 — Worked examples"
line_start: 35444
line_end: 35479
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

Each example starts with wording for the stated use; §4 determines which further details are needed.

#### A.19.SPR:5.1 - Physical-system state

**Before:** “Pump 37 is in a good operating state.”

**After:** “Pump 37 satisfies `InspectionOperatingCondition`: its coolant temperature is 72 °C, within the 60–80 °C band, and its discharge pressure is 315 kPa, above the 300 kPa minimum.”

For a relied-on inspection decision, make the measurement basis and applicable condition recoverable. Add the reading time, exact condition edition and recheck condition when the decision depends on them.

#### A.19.SPR:5.2 - Work-entry readiness is not gate passage

**Before:** “Release 12 is ready.”

**After:** “At 10:00, the A.15.5 check found that `PlanItem-Deploy-12` satisfied its release-entry criterion and was ready for work entry until 10:30; recheck if a required input changes.”

For replay, make the plan item, criterion, input facts, result and reliance window recoverable. Identify a separate result episteme or checking Work only when that identity matters; a claimed Work needs its A.13 basis and independent A.15.1 admission, with F.6 only for precise assignment-bound attribution. The work-entry finding alone establishes no gate passage. Use A.21 for a distinct `OperationalGate(profile)` that consumes declared checks and publishes its own decision.

#### A.19.SPR:5.3 - Source use and currentness

**Before:** “The source posture is good.”

**After:** “This review uses edition E7 for decision question Q. Reconsider that choice if the question or the source content needed to answer it changes.”

When the decision relies on a claim from E7, assess that claim’s currentness under B.3.4 using the premises and time limits that matter to this use. Preserve exact source and result identities when the receiving operation depends on them.

#### A.19.SPR:5.4 - Other direct repairs

- **Evidence.** Replace “evidence status incomplete” with “Reliance on claim C remains unestablished because the needed calibration basis is missing; obtain the missing calibration basis and check again.” Add exact evidence and currentness references only when the receiving decision needs them.
- **Publication.** Replace “publication posture allows decision input” with “This publication exposes candidate input X for the decision; the decision rule still evaluates X.”
- **Mathematical lens.** Keep `LensUseBoundaryValue` in C.29 when its possible values and intended lens use are defined. State what the value permits for the intended lens use under C.29.
- **Temporal claim.** For a C.27 classification, name the temporal claim and its Dyn0, Dyn1 or Dyn2 reading. State the supported use; add the intervention account only when the claim is intervention-sensitive.
- **Project-side state.** Keep current framework-development status in its project record. Retain reusable guidance and worked examples that help the reader handle project status in the pattern’s stated practice.

