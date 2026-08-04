---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:7"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__009_worked-cases.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:7 — Worked Cases"
line_start: 90768
line_end: 90797
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

`PumpInspectorRoleDescription` is a C.2.1 episteme whose EntityOfConcern is `PumpInspectorRole`, whose effective scheme is `Plant-A-Maintenance-Scheme`, and whose ClaimGraph names `PlantMaintenanceRoles-2026` as the governing role-taxonomy episteme. Its recognition explanation says that the role is used for inspecting pump condition before maintenance work is admitted. It names maintenance-technician, inspection-robot, or service-team `U.System` kinds as eligible holder kinds only when each exact system kind and any current holder entity are independently admitted; the description itself admits neither a system nor an assignment.

Its role invariants say that the role concerns pump-condition inspection, does not itself perform repair, and requires a current assignment before work attribution. It references pump-inspection capability conditions or the inspection method only when a receiving work claim needs them. Its non-role boundary states that an inspection report is an episteme used through direct evaluation, evidence, source, or publication relations, not a role holder.

The description makes `PumpInspectorRole` recognizable. It does not say that Robot-7 holds the role, can inspect, followed the method, or performed work. Those claims go to `A.2.1`, `A.2.2`, `A.15`, and the direct evaluation or evidence patterns.

#### F.4:7.2 - Reviewer Role and Review Report

`ReviewerRole` under `PatternReviewRoles-2026` and `Pattern-Review-Scheme` may have a role-description episteme with invariants about checking a pattern against declared scales. A review report produced by a reviewer is an episteme used as evidence or source for a pattern-quality claim. The report is not the role holder and does not hold an evidence role.

Use:

- `A.2` for `ReviewerRole`;
- `F.4` for the role-description episteme;
- `A.2.1` for Alice's exact `ReviewerRole` assignment under that taxonomy and scheme;
- `A.15.1` for the review work occurrence;
- `A.10`, `B.3`, `G.6`, or a direct evidence-use pattern for the review report as evidence.

#### F.4:7.3 - Standard Used as a Specification or Source

The sentence `Standard S has the architecture-standard role in this work` is unsafe if it makes the standard episteme a role holder. Repair it by naming the direct relation: the exact edition of Standard S is used as a specification, external rule, premise, or source for named claims in the receiving work. Only an admitted `U.System` can hold a work-facing role. The standard may constrain or support a claim through its direct episteme-use relation.

#### F.4:7.4 - Access Role Is Not Automatically Work-Facing Role

RBAC `role` often names a permission grouping. If the current claim is permission or access standing, use the status, policy, or deontic governing pattern. Do not describe it as `U.Role` unless the role taxonomy and effective scheme explicitly introduce a work-facing role value and the holder, assignment, method, and work claims are current.

