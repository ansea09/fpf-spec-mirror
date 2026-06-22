---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__006_solution.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:4 — Solution"
line_start: 76616
line_end: 76742
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:4 - Solution

Use F.6 as a local check over candidate assignment and optional work attribution.

```text
RoleAssignmentAttributionCheck:
  CandidateRoleDescriptionRef:
  CandidateHolderRef:
  CandidateRoleValueRef:
  BoundedContextRef:
  AssignmentWindowDisposition:
  HolderAdmissionDisposition:
  RoleStateAdmissionRef:
  CapabilityRequirementRef:
  MethodOrMethodDescriptionRef:
  WorkOccurrenceRef:
  PerformedByRelation:
  AssignmentJustificationRef:
  EvidenceOrSourceUseRefs:
  BridgeRef:
  NotCarried:
  Result:
```

This check is not a new root kind. It is an application relation over values governed elsewhere. `A.2.1` governs `U.RoleAssignment`; `A.15.1` governs the `U.Work` occurrence; `F.10`, `A.10`, `B.3`, `E.17`, `E.10.D2`, and direct governing patterns govern status, evidence, assurance, publication, and source-use relations.

#### F.6:4.1 - Slot Meanings

| Slot | Admitted value | Meaning |
| --- | --- | --- |
| `CandidateRoleDescriptionRef` | `F.4` role-description episteme or local role gloss | The description that makes the role recognizable. It is not the role value and not the assignment. |
| `CandidateHolderRef` | `U.System` or acting holon admitted by `A.2.1` | The candidate holder that may bear the role. Epistemes are not admitted here merely because they are used as evidence, source, standard, requirement, publication, or status bearer. |
| `CandidateRoleValueRef` | `U.Role` governed by `A.2` | The work-facing role value being assigned. |
| `BoundedContextRef` | `U.BoundedContext` | The local context that gives the role value meaning. |
| `AssignmentWindowDisposition` | filled, inherited, unknown, not asserted, or not current for this claim | Whether assignment currentness is recovered well enough for the claim being made. |
| `HolderAdmissionDisposition` | admitted, not admitted, lowered, or blocked with reason | Whether the holder kind and local predicates admit the assignment. |
| `RoleStateAdmissionRef` | `A.2.5` state assertion or absence disposition when current | Whether role state or enactable-state admission matters for current work. |
| `CapabilityRequirementRef` | `A.2.2` capability relation when current | Required ability or operating envelope; not proved by role name. |
| `MethodOrMethodDescriptionRef` | `A.3.1`, `A.3.2`, or `A.15` reference when current | The method or method-description claim that the role assignment may serve. |
| `WorkOccurrenceRef` | `U.Work` governed by `A.15.1` when current | The performed work occurrence being attributed. Missing work means no performed-work attribution claim is made. |
| `PerformedByRelation` | `Work.performedBy = RoleAssignment` or `RoleEnactmentFact` | The direct relation or named fact that links work to the assignment. |
| `AssignmentJustificationRef` | source, speech act, gate, decision, policy, evidence, or provenance relation governed by its direct pattern | Why the assignment claim is admitted or relied upon, when current. |
| `EvidenceOrSourceUseRefs` | direct evidence, source, status, publication, assurance, or requirement-use relation refs | Direct non-F.6 uses that may justify, challenge, or qualify the assignment or work claim. They do not become role assignments. |
| `BridgeRef` | `F.9` bridge when cross-context reuse is current | Cross-context explanation or substitution claim; not local assignment identity. |
| `NotCarried` | stronger claim not made by this check | Examples: status truth, gate passage, method validity, capability proof, work occurrence, evidence sufficiency, cross-context substitution. |
| `Result` | `assignmentAdmitted`, `assignmentBlocked`, `workAttributionAdmitted`, `workAttributionBlocked`, `claimGovernedOutsideF6`, or `claimLowered` | The local check result. |

#### F.6:4.2 - The Check Sequence

Use these questions in order. They are judgement questions, not a `U.WorkPlan`, registry procedure, or tool protocol.

1. **Role meaning recovered?** Does the role label point to a `U.Role` in one bounded context, usually through `F.4` and `A.2`?
2. **Holder admitted?** Is the candidate holder a system or acting holon admitted by `A.2.1` and by the local role description?
3. **Context and window adequate?** Is the bounded context explicit, and is the assignment window filled, inherited, unknown, not asserted, or not current for the claim?
4. **Related prerequisites current?** Does this use need role state, capability, method, method description, work plan, evidence, gate, decision, or source-currentness?
5. **Work occurrence current?** Is there a `U.Work` occurrence to attribute? If not, stop at assignment admission or blocker.
6. **Performed-by relation admissible?** Can the work occurrence cite the assignment by `Work.performedBy = RoleAssignment` or `RoleEnactmentFact`?
7. **Claim governed outside F.6?** If the current claim is status, evidence, source, publication, requirement, assurance, bridge, method, capability, or gate use, apply the direct governing pattern and do not encode that claim as role assignment.

#### F.6:4.3 - Assignment Result vs Work-Attribution Result

Keep two local results separate.

```text
AssignmentAdmission:
  CandidateHolderRef bears CandidateRoleValueRef in BoundedContextRef
  with AssignmentWindowDisposition and HolderAdmissionDisposition.
```

```text
PerformedWorkAttribution:
  WorkOccurrenceRef performedBy RoleAssignmentRef
  with RoleEnactmentFact only when a named fact is useful.
```

An assignment admission does not prove that work happened. A performed-work attribution does not prove that the method was valid, the capability was sufficient, the evidence is adequate, or the gate passed. Those claims use their governing patterns.

#### F.6:4.4 - `RoleEnactmentFact`

Use `RoleEnactmentFact` only as a name for the derived fact that a work occurrence was performed under a role assignment.

```text
RoleEnactmentFact:
  workOccurrence: U.Work
  performedBy: U.RoleAssignment
  methodTrace?: U.Method or U.MethodDescription reference when current
  window?: inherited from work occurrence or role assignment when current
```

Do not write `U.RoleEnactment` as a durable root kind. If a log, table, database row, or publication stores a role-enactment entry, treat it as a record of this fact unless a direct governing pattern admits record-as-value for that use.

#### F.6:4.5 - Status and Evidence Claims Governed Outside F.6

Status and evidence claims often sit next to role assignment. They do not become role assignment.

| Source sentence | F.6 result | Direct governing pattern |
| --- | --- | --- |
| "The standard plays the normative role for this method." | `claimGovernedOutsideF6`; no role assignment holder recovered. | standard-use, requirement-use, source-use, or `E.10.D2` |
| "The report has evidence role for claim C." | `claimGovernedOutsideF6`; evidence-use relation around an episteme. | `A.10`, `B.3`, or direct evidence-use pattern |
| "The dashboard says the service is ready." | `claimGovernedOutsideF6`; status-use, display, or source question. | `F.10`, `E.17`, gate or assurance pattern when current |
| "Alice reviewed report R as ReviewerRole." | candidate assignment plus work attribution may be current. | `A.2.1`, `A.15.1`, and F.6 check |
| "RBAC admin role allows access." | access or policy term first; work-facing role assignment only if actual work attribution is also current. | direct access, policy, status, or source-use pattern |

#### F.6:4.6 - Compact Notation and Shortcut Boundary

`Holder#Role:Context@Window` is allowed as a compact reading aid after the typed relation is recoverable.

Baseline relation:

```text
RoleAssignment:
  HolderSlot:
  RoleValueSlot:
  BoundedContextSlot:
  AssignmentWindowSlot:
```

Compact notation:

```text
Holder#Role:Context@Window
```

The compact notation saves reader effort in examples, tables, and short work records. It weakens the representation by hiding SlotSpec names and any current assignment justification, role state, capability, method, evidence, source, or provenance relation. Therefore it is admitted only for local reading, examples, and compact citations after the typed slots are either filled, inherited, or explicitly not current for the claim.

Do not use the compact notation as proof of assignment, proof of performed work, proof of capability, proof of method validity, proof of status, or proof of gate passage. If reliance-bearing use depends on any hidden slot, unfold the notation to the typed relation or lower the claim.

