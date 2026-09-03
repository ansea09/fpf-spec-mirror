---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.SystemRoleAssignment - Contextual System-Role Assignment"
section_id: "A.2.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__006_solution.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.2.1 — U.SystemRoleAssignment - Contextual System-Role Assignment"
  - "A.2.1:4 — Solution"
line_start: 3478
line_end: 3611
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.3.3"
  - "F.6"
  - "F.9"
keywords:
  - "assignment predicate"
  - "direct assignment species"
  - "holder System"
  - "identity"
  - "maximal interval"
  - "performedUnderAssignment"
  - "system-role kind"
---

### A.2.1:4 - Solution

Declare each assignment relation species directly under `U.SystemRoleAssignment`. Do not give the family one universal participant signature. Every admitted species declares:

- `HolderSystemSlot : U.System`;
- one declaration-local `AssignedSystemRoleKindSlot` whose `ValueKind` is the exact local system-role-kind domain used by that species;
- its direct assignment predicate and applicability;
- every additional actual participant that changes the predicate or occurrence identity; and
- its occurrence-identity rule.

The `HolderSystemSlot` and `AssignedSystemRoleKindSlot` names are declaration-local SlotKinds. Their spelling does not create global slots. Their complete A.6.5 SlotSpecs state ValueKind, refMode, participant meaning, multiplicity, and any constraints.

#### A.2.1:4.1 - Simple Direct Species

A simple species has only the two common participants:

```text
JournalReviewAssignmentRelation <: U.SystemRoleAssignment

RelationSignature:
  HolderSystemSlot: U.System, U.EntityRef
  AssignedSystemRoleKindSlot: JournalReviewSystemRoleKindDomain, ByValue

predicate:
  the admitted holder is selected to supply the contribution denoted by
  the assigned system-role kind under JournalReview assignment conditions

applicability:
  JournalReview-2026 assignment episodes
```

`JournalReviewSystemRoleKindDomain` is the exact local C.3 domain defined by A.2. `CoolingPumpKind`, `ShortAssignmentKind`, and arbitrary local kinds cannot fill this species' assigned-kind slot merely because each is a `U.Kind`.

#### A.2.1:4.2 - A Stronger Species Retains Its Real Participants

When an appointment, organizational position, installation locus, or work commission changes the predicate or occurrence identity, the domain species declares that participant. For example, conditional on a domain pattern already admitting `ProjectReviewCommission` and its appointment predicate:

```text
ProjectReviewAppointmentAssignment <: U.SystemRoleAssignment

RelationSignature:
  HolderSystemSlot: U.System, U.EntityRef
  AssignedSystemRoleKindSlot: ProjectReviewSystemRoleKindDomain, ByValue
  ReviewCommissionSlot: ProjectReviewCommission, U.EntityRef

predicate:
  the holder is appointed under the identified commission to supply the
  contribution denoted by the assigned system-role kind
```

The commission is a participant because this admitted species makes it one. A decision episteme, roster row, or evidence item about the appointment is not thereby the commission or another participant.

If no current pattern admits the proposed participant kind or direct predicate, return `A.6.RCD missing-governor` for that specialized assignment. Do not hide the gap in an optional field.

#### A.2.1:4.3 - Occurrence Identity

An occurrence of a declared species begins when that species' direct predicate starts obtaining for fixed participant values. It continues over the maximal uninterrupted predicate-true interval. It ends when a participant changes or the predicate ceases to obtain. A later resumption is another occurrence even when every participant value is the same.

A context field ending in `...SystemRoleAssignmentRef` uses `U.RelationRef constrained to U.SystemRoleAssignment` and resolves to the exact occurrence while keeping its declared species recoverable.

An assignment assertion or occurrence description can state `assignmentInterval` with a temporal reference, start, end or explicit open end, and continuity claim. Closing an open interval later refines the same description when world-side obtaining was uninterrupted. Missing evidence yields `unknown`; it does not split the occurrence. A demonstrated non-assignment interval ends it.

Keep ordinary interval content here. When a positive temporal aspect itself becomes a relied-on object—its temporal reference, validity or currentness window, duration, cadence, rhythm, or interval structure—use `C.27.TA` for that aspect and keep the assignment occurrence separate. Use `C.27` only for the different question of whether a temporal claim is adequate.

Taxonomy, scheme, `KindSignature`, assertion, interval description, and selected publication form can be cited when they matter to interpretation or evidence. Only the species' declared participants and predicate determine world-side occurrence identity.

#### A.2.1:4.4 - One Strong Occurrence, Not a Generic Duplicate

If Alice has overlapping `Commission-A` and `Commission-B`, then `ReviewAssignment-A` and `ReviewAssignment-B` are two `ProjectReviewAppointmentAssignment` occurrences even when holder and `ReviewerSystemRole` match. Their commission participants and predicates distinguish them.

“Alice is the reviewer” is a readable existential projection over any qualifying occurrence. It is not a third assignment occurrence. Do not create a generic two-participant assignment beside either appointment simply to support that sentence or F.6.

Every admitted species supplies the common projection:

```text
holderSystem(RA : U.SystemRoleAssignment) = RA.HolderSystemSlot
assignedSystemRoleKind(RA) = RA.AssignedSystemRoleKindSlot
```

The projection does not erase additional participants or assert that another occurrence exists.

#### A.2.1:4.5 - Assignment and Classification Are Independent

A C.3.2 judgment classifies one system under one local system-role kind for one signature edition and slice. An assignment occurrence relates participants under its species predicate. Either can be current without the other.

An assignment can be one membership feature only when the exact local `KindSignature` explicitly cites that independently obtaining predicate. `RoboticsAssignment-1` alone makes neither `RoboticsEngineerSystemRole` nor `EngineerSystemRole` true. A later `U.SubkindOf` result records monotonic implication among independently evaluated judgments; it creates no broader assignment.

#### A.2.1:4.6 - Demand-Driven Materialization

Ordinary use can stop at:

```text
During Shift-17, Robot-7 is assigned as inspector under
MaintenanceInspectionAssignment.
```

Expose an occurrence identifier only when a receiver must distinguish episodes, cite the assignment as a participant, compare assertions, or preserve provenance. If a required participant or the predicate cannot be recovered, lower the claim or return the exact missing governor. Never insert a dummy value or broaden the assigned-kind domain.

#### A.2.1:4.7 - Direct Neighboring Relations

| Current question | Direct exit | Why it stays separate |
| --- | --- | --- |
| Does the holder count under the system-role kind? | `A.2`, `C.3.2` | Classification is a four-input judgment, not assignment obtaining. |
| Can the holder do the Work? | `A.2.2` capability and fit | Assignment does not create ability. |
| Does the assignment satisfy a state predicate? | `A.2.5` | State has its own predicate, relation occurrence, and truth interval. |
| Which Method admits or organizes the Work? | `A.3`, `A.15` | Method and MethodDescription do not assign a holder. |
| Was Work performed under this assignment? | `A.13`, `A.15.1`, `F.6` | Use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. Because this question explicitly asks under which assignment the Work was performed, F.6 then checks that separate relation against the assignment already used by A.13. |
| Does a decision or installation help constitute this species? | the direct domain relation and species predicate | It matters only when the admitted species says so; an episteme is not a generic participant. |
| Is the holder responsible, committed, permitted, authorized, or able to access something? | the admitted direct domain predicate, `A.2.8`, `A.2.8.PER`, or `missing-governor` | Evaluate the claim about the holder using the direct predicate and its declared participants. The assignment can supply an applicability ground where specified. |
| What supports use of the assignment claim? | evidence, reliance, provenance, source-use, or publication pattern | Support concerns the assertion; it does not make the relation obtain. |
| Does a model-use structure change this receiving interpretation? | `A.1.1` plus the receiving assertion or use | It is not an optional participant of the assignment family. |

Assignment-establishing world-side relations and epistemic support are not interchangeable. A constituting decision or installation occurrence affects a species only when its direct predicate says so. Evidence can support relying on the assertion without constituting the assignment.

#### A.2.1:4.8 - Performed-Work Attribution

F.6 retains one direct attribution with a comparison-only projection:

```text
performedUnderAssignment(W : U.Work, RA : U.SystemRoleAssignment)
attributedPerformerSystem(W, RA) := RA.HolderSystemSlot
```

A.13 first identifies the actual performer `S`, and A.15.1 independently admits `W : U.Work` from its performance history, enacted Method, temporal extent, and containing-System relation. F.6 is needed only for a **precise assignment-bound attribution**—when the current use must also say exactly under which assignment `W` was performed. It then establishes `performedUnderAssignment(W, RA)` against the same assignment already used by A.13 and requires `S = attributedPerformerSystem(W, RA) = RA.HolderSystemSlot`. The projection exposes the assignment holder only for comparison with `S`; it identifies neither assignment nor performer, and a missing or failed F.6 check leaves the Work intact.

`SystemRoleAssignmentSlot` in F.6 accepts any admitted assignment species because its `ValueKind` is the family `U.SystemRoleAssignment`. It is not a union of a generic relation and stronger non-assignment values. `ReviewWork-A` can be attributed to `ReviewAssignment-A`, and `ReviewWork-B` to `ReviewAssignment-B`, without creating generic duplicates.
Assignment does not prove that Work occurred. Work does not alter assignment identity. For source wording such as `RoleEnactment`, first use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. If the current use also needs to say exactly under which assignment the Work was performed, add that assignment and the separate F.6 `performedUnderAssignment` check. Do not create a duplicate run-time kind or occurrence.

#### A.2.1:4.9 - Source Context Shorthand

`Holder#Role:Context@Window` is source notation, not the assignment ontology. Apply E.10.ROLE to recover the system-role kind or another meaning. Recover the object denoted by `Context` and its direct relation separately. It can be an actual system or Work locus, a claim scope, or a selected `BoundedModelUseStructure`; these have different kinds and uses.

If one assignment species genuinely depends on a structure or locus, its direct pattern declares that participant and stronger identity law. Otherwise keep the recovered object in the receiving assertion or use; never invent a generic context participant.

