---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:7"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__009_worked-cases.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:7 — Worked Cases"
line_start: 81877
line_end: 81926
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:7 - Worked Cases

#### F.4:7.1 - Pump Inspector Role

```text
RoleDescription:
  DescribedRoleSlot: PumpInspectorRole
  BoundedContextSlot: PlantMaintenance_2026
  HolderAdmissionSlot: maintenance technician, inspection robot, or service team admitted as acting holon by the maintenance context
  RecognitionTextSlot: the role used for inspecting pump condition before maintenance work is admitted
  RoleInvariantSetSlot:
    - concerns inspection of pump condition in PlantMaintenance_2026
    - does not perform repair work by itself
    - requires current assignment before work attribution
  CapabilityRequirementRefs: PumpInspectionCapability when the work claim depends on ability
  MethodRequirementRefs: PumpInspectionMethodDescription when the work claim depends on method
  NonRoleUseBoundarySlot: inspection report is evidence use, not a role holder
```

The description makes `PumpInspectorRole` recognizable. It does not say that Robot-7 holds the role, can inspect, followed the method, or performed work. Those claims go to `A.2.1`, `A.2.2`, `A.15`, and evidence patterns.

#### F.4:7.2 - Reviewer Role and Review Report

`ReviewerRole` in `PatternReview_2026` may have a role description with invariants about checking a pattern against declared scales. A review report produced by a reviewer is an episteme used as evidence or source for a pattern-quality claim. The report is not the role holder and does not hold an evidence role.

Use:

- `A.2` for `ReviewerRole`;
- `F.4` for the role-description episteme;
- `A.2.1` for `Alice#ReviewerRole:PatternReview_2026@Window`;
- `A.15.1` for the review work occurrence;
- `A.10`, `B.3`, `G.6`, or a direct evidence-use pattern for the review report as evidence.

#### F.4:7.3 - Standard Used as Requirement Source

The sentence "ISO 42010 has the architecture-standard role in this work" is unsafe if it makes the standard a role holder.

Repair it as:

```text
ISO/IEC/IEEE 42010 is used as a standard-use or requirement-use episteme
for architecture-description claims in this bounded context.
```

Only a system or acting holon can hold a work-facing role. The standard may constrain, evidence, or source a claim through direct episteme-use relations.

#### F.4:7.4 - Access Role Is Not Automatically Work-Facing Role

RBAC "role" often names a permission grouping. If the current claim is permission or access standing, use the status, policy, or deontic governing pattern. Do not describe it as `U.Role` unless the bounded context explicitly introduces a work-facing role value and the holder, assignment, method, and work claims are current.

