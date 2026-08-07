---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:6"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__007_worked-cases.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:6 — Worked Cases"
line_start: 3472
line_end: 3513
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:6 - Worked Cases

#### A.2.2:6.1 - Manufacturing Cell

`RobotArm_A` is the admitted holder in one exact assignment occurrence with `WelderRole`, `FactoryProductionRoles-2026`, and `Factory-Line-B-Role-Scheme`; the assignment's actual extent follows uninterrupted obtaining for those four fixed participants. A separate work or system-locus relation may place intended or performed welding at `AssemblyLine_2026` when that relation obtains. The assignment says only that the holder system holds that role under the named taxonomy and scheme during its extent; it proves neither permission, ability, action, nor performed work.

The capability instance is separate; a statement or record may describe it:

```text
ConcreteCapabilityInstance:
  holder: RobotArm_A
  canDo: Weld_MIG_v3 seam family
  envelope: steel grades S235-S355, ambient 18-30 C, argon mix 92-95 percent, torch T-MIG-07
  measures: bead width 6.0 mm plus or minus 0.2 mm, throughput up to 12 seams per minute, defect rate below 0.5 percent
  qualificationWindow: calibration valid through 2026-09-30
  currentnessCondition: calibration and configuration remain inside the qualification window
SupportAndUseReferencesAroundCapability:
  evidenceOrSourceUse: latest welding test report and calibration source relation
```

If a method step requires `WelderRole` and bead width tolerance below 0.2 mm, the role assignment and the capability are both checked. The assignment does not supply the tolerance, and the capability does not assign the robot to the shift.

**Shared boundary case — Robot-7 possesses an inspection algorithm.** `RoleAssignment-17` has four exact participants: admitted holder system `Robot-7`, `InspectorRole`, `MaintenanceRoles-2026`, and `Maintenance-Scheme-A`; its separately described extent covers the candidate inspection interval. `Robot7-TurbineInspectionCapability-2026` is the holder-dependent capability instance for turbine-inspection work within its declared sensor, calibration, input, measure, and qualification bounds. A statement that Robot-7 "possesses inspection algorithm A" does not by itself identify that capability instance, an exact Method, a deployed-software relation, or a method-description episteme. Dispatch the phrase by claim: use A.2.2 only for the bounded ability; A.3.1 for exact `TurbineInspection@Maintenance-2026 : U.Method`; a direct deployed-software or possession relation when that is the actual claim; and A.3.2 for candidate episteme `TurbineInspectionProcedure-v3` only after its exact `EntityOfConcern` resolves to that Method and one substantive claim says how it is done.

Assignment and capability still do not prove execution. If `InspectionWork-17` actually occurs, Robot-7 is the actor and performs it under `RoleAssignment-17` through F.6 `performedUnderAssignment(InspectionWork-17, RoleAssignment-17)`; the Work occurrence separately stands in `enactsMethod(InspectionWork-17, TurbineInspection@Maintenance-2026)`. `InspectorRole`, the capability instance, the possession phrase, the Method, and `TurbineInspectionProcedure-v3` do not act or perform the inspection.

#### A.2.2:6.2 - Software Service as Deployed System

`PlannerService_v4` is a deployed system. It may have capability to generate job-shop schedules for 50-500 jobs and 5-40 machines, with benchmark optimality above 0.95 and latency below 20 ms in `PlantScheduling_2026`.

The algorithm paper and method description are not the capability. The deployed system has the capability only while its version, dependencies, input range, and operational measurements satisfy the declared currentness condition; a benchmark report or model card is support for a statement about that instance.

#### A.2.2:6.3 - Organization or Team

`FinanceDept` can close books for eight legal entities under IFRS with ERP v12, staffing at or above six qualified people, and close duration below five business days. That is a capability of the organizational system.

The monthly-close service promise is a promise content claim. The actual close for March 2026 is performed work. Staff assignments and role states are neighboring role claims. The capability instance keeps the ability of the department visible and measurable; the management report describing it is a statement about that instance.

#### A.2.2:6.4 - Episteme Anti-Case

"ISO 26262 has safety capability" is not a capability statement about a holder-dependent capability instance. The standard is an episteme used as source, requirement, or assurance input. A safety engineering team or toolchain may have a capability to perform safety-case work using that standard within a declared envelope.

