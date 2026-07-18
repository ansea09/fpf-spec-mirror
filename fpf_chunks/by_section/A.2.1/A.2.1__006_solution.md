---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__006_solution.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:4 — Solution"
line_start: 2422
line_end: 2573
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:4 - Solution

Use `U.RoleAssignment` for the typed relation that assigns an enactment-facing `U.Role` to an admitted system holder in one bounded context.

```text
RoleAssignmentCoreSlotSpec:
  HolderSlot:
  RoleValueSlot:
  BoundedContextSlot:
  AssignmentWindowSlot:
  AssignmentJustificationSlot:
  AssignmentProvenanceSlot:
```

This is a relation value. A record, registry row, publication, diagram, or file may describe, cite, or store the relation value. It is not the assignment itself by default.

#### A.2.1:4.1 - Core SlotSpecs

| SlotKind | ValueKind | Slot-use disposition | Meaning |
| --- | --- | --- | --- |
| `HolderSlot` | admitted `U.System` selected as system-like performer by the governing work, transformation, functioning, or method pattern | identity slot | The holder that bears the role in the bounded context. `U.Episteme` is not admitted here merely because it is used as evidence, source, standard, requirement, explanation, status bearer, publication, or assurance input. |
| `RoleValueSlot` | `U.Role` | identity slot | The context-bound role value governed by `A.2`. It is not a SlotKind and not a capability. |
| `BoundedContextSlot` | `U.BoundedContext` | identity slot | The context that gives the role value its local meaning. |
| `AssignmentWindowSlot` | assignment-currentness window, role-state window, or temporal-validity value governed by the temporal pattern current in the project | optional-in-use; currentness-required when the claim depends on current assignment validity | Missing window means not recovered or not current for the claim, not that no window exists. |
| `AssignmentJustificationSlot` | source, speech act, policy, gate, decision, rule, or evidence relation governed by its direct pattern | currentness-required when the assignment admission is challenged or relied upon | This slot points to why the assignment claim is admitted; it does not replace the governing speech-act, gate, policy, or evidence pattern. |
| `AssignmentProvenanceSlot` | provenance relation for issuing, recording, or refreshing the assignment claim | consideration slot; currentness-required when auditability or source order is current | This slot is not a bucket for target claim, evidence polarity, status value, evidence window, or publication form. |

Direct work-role patterns may declare additional work-role qualifier SlotSpecs. Evidence-use and status-use relation slots are not assignment qualifiers unless a direct work-role pattern explicitly makes that work-role claim.

#### A.2.1:4.2 - Well-Formedness Constraints

Use these constraints as predicates over a filled assignment relation.

```text
Invariant RA-S1 (Local role):
  RoleValueSlot content is a U.Role admitted in the BoundedContextSlot content.

Invariant RA-S2 (Holder admission):
  HolderSlot content is an admitted U.System selected as system-like performer by the governing work, transformation, functioning, or method pattern.

Invariant RA-S3 (No role-as-holder):
  HolderSlot content is not U.Role and not U.RoleAssignment.

Invariant RA-S4 (No episteme holder by use):
  U.Episteme is not admitted as HolderSlot content merely because the episteme is used as evidence, source, standard, requirement, definition, explanation, publication, status bearer, or assurance input.

Invariant RA-S5 (Context locality):
  Cross-context assignment reuse requires a named bridge or direct context relation; shared labels do not create sameness.

Invariant RA-S6 (Window honesty):
  A claim that depends on current assignment validity names AssignmentWindowSlot content, inherits a declared bounded-context default, or states that the window is unknown, not recovered, not asserted, or blocking for the stronger claim.
```

Do not express these predicates with RFC-style deontics unless the sentence is imposing a duty on an author, validator, or published record.

#### A.2.1:4.3 - Open-World Slot Disposition

The SlotSpecs are a thinking discipline, not a demand to fill a form for every casual use.

Use these dispositions:

- **filled:** the relation instance names the slot filler or reference;
- **inherited:** the role definition or bounded-context rule fixes the value for the current claim;
- **unknown or not recovered:** the slot is relevant, but the project has not recovered it;
- **not asserted:** the text deliberately makes no claim about this slot;
- **not current for this claim:** the slot exists in the model, but the present claim does not depend on it;
- **claim lowering or blocker:** a stronger claim depends on the slot, so missing content lowers or blocks that claim.

For example, a quick staffing note may only need holder, role, and context. A safety-critical work attribution claim needs the assignment window, role-state admission, and method or work relation that the note omitted.

#### A.2.1:4.4 - Role State and Role-Description Characterization Hooks

`U.RoleAssignment` does not contain a role-state relation or a role-state description. The `U.Role` and its role description may be linked to:

- RoleCharacteristicSpace, the characteristic space used to describe role variants or role-admission conditions in one bounded context;
- Role State Relation, the state-family relation used to decide whether a role assignment is in an enactable state;
- state assertions or evaluations governed by `A.2.5` and the relevant evidence or evaluation pattern.

A work attribution claim may depend on those neighboring values. The assignment relation names the holder, role, context, and window; `A.2.5` governs whether the assignment is in an enactable state for the current work.

#### A.2.1:4.5 - Role Assignment and Work

Work is not performed by the role value. Work is performed by the holder under a role assignment. For machines and components, this includes physical or operational work such as driving, pumping, regulating, heating, cooling, sensing, stabilizing, or transforming a state under the governing functional or transformation context.

Use the direct relation:

```text
Work.performedBy = RoleAssignment
```

Then check neighboring claims:

- the work occurrence is governed by `A.15.1`;
- the bounded transformation is governed by `A.3.4` when the work is claimed as transformation participation;
- functional wording is restored through `A.6.F` when the role is named by what the holder does functionally;
- the selected method is governed by `A.3.1`;
- the method description or role-admission declaration is governed by `A.3.2` and `A.15`;
- the work plan is governed by `A.15.2`;
- role-state admission is governed by `A.2.5`;
- capability is governed by `A.2.2`.

A `U.Work` record may cite `performedBy = some U.RoleAssignment`. That citation does not make the work record the assignment and does not make the assignment a work occurrence.

#### A.2.1:4.6 - RoleEnactmentFact

Source text may name `U.RoleEnactment` or `RoleEnactment`. In FPF, role enactment is a derived relation or fact over `U.Work` and `U.RoleAssignment`, not a durable U-kind.

Use this named fact only when a named relation is clearer than direct `performedBy` wording:

```text
RoleEnactmentFact:
  workOccurrence: U.Work
  performedBy: U.RoleAssignment
  methodTrace?: U.Method or U.MethodDescription reference when current
  window?: inherited from work occurrence or role assignment when current
```

If a database, log, table, or publication stores a role-enactment entry, it stores a record of the fact unless a direct governing pattern admits record-as-value for that use.

#### A.2.1:4.7 - Episteme Evidence, Status, Source, and Publication Uses

Do not use `U.RoleAssignment` for an episteme merely because the episteme is useful in a project relation.

| Source phrase | Recover as |
| --- | --- |
| "this report has evidence role for Claim A" | evidence-use relation with evidence episteme, target claim, claim scope, polarity, and relevance window when current. |
| "the standard has normative role" | standard-use, requirement-use, source-use, publication-use, or status-use relation under the direct pattern. |
| "the dataset plays the role of benchmark" | dataset-use, evidence-use, measurement, benchmark, or source-use relation under the direct pattern. |
| "the model card is the approver" | publication, evidence, assurance, or source relation for the model card; any approving work is performed by a system or acting holon through a role assignment. |
| "the dashboard role is monitoring" | publication or interface description use for the dashboard; observing work belongs to an observer holder under a role assignment. |

The repair is not to find a nicer role word. The repair is to recover the current relation and its slot fillers.

#### A.2.1:4.8 - Shorthand Notation

The compact notation is:

```text
Holder#Role:Context@Window
```

Use it only as a readable notation for the typed assignment relation.

Examples:

- `Robot_7#InspectorRole:MaintenanceLine_A@2026-06-15T09:00..2026-06-15T11:00`
- `Motor_M1#DriveMotorRole:WaterPumpAssembly_A@installed-window`
- `OpsTeam#IncidentCommanderRole:PlantIncident_2026@open`
- `CI_Service#DeployerRole:ReleaseTrain_2026@2026-Q2`

If the notation is missing the window, the current text must still say whether the window is inherited, unknown, not asserted, or not current for this claim when the claim depends on assignment currentness.

