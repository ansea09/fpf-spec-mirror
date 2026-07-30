---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__006_solution.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:4 — Solution"
line_start: 3066
line_end: 3165
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:4 - Solution

State the direct assignment in readable prose first. When another claim needs reusable participant typing or occurrence identity, use the `RelationSignature` for `U.RoleAssignment` governed here and declared through `A.6.0` and `A.6.5`. The signature is an episteme about the relation kind; it is not the world-side assignment occurrence. Its SlotSpecs are:

| SlotKind | ValueKind | refMode | Meaning in `U.RoleAssignment` |
| --- | --- | --- | --- |
| `HolderSystemSlot` | `U.System` | `U.EntityRef` | A reference resolving to the admitted system that holds the role. |
| `RoleValueSlot` | `U.Role` | `ByValue` | The enactment-facing role value. |
| `RoleTaxonomyEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` | A reference resolving to the exact role-taxonomy episteme used for interpretation. |
| `EffectiveReferenceSchemeSlot` | `U.ReferenceScheme` | `ByValue` | The reference-scheme value effective for this assignment. |


The four SlotSpecs declare all participant meanings of generic `U.RoleAssignment`. No SlotSpec is declared for the occurrence's temporal extent or for a selected model-use structure used only to qualify a receiving interpretation.

`AssignmentInterval` is a local content ValueKind for an assignment assertion or relation-occurrence description, not a U-kind and not the ValueKind of a relation-participant SlotSpec. An `assignmentInterval` field states the currently known temporal extent through a temporal reference, a start boundary, an end boundary or explicit open end, and the continuity claim used to recognize one uninterrupted assignment episode. The world-side occurrence has that temporal extent under its direct identity rule. The field describes the extent and does not make the relation obtain. A shift label is sufficient only when those temporal facts can be resolved. `C.27.TA` governs fuller temporal-aspect description when the temporal reference or interval itself becomes a relied-on object.

`U.RoleAssignment` obtains when the admitted system holds the role value, interpreted by the named role-taxonomy episteme under the effective reference scheme, throughout one continuous assignment episode. An assignment assertion is a `U.Episteme` claiming that this relation obtains. A roster entry or configuration line may express that assertion, and a publication may expose it; evidence may support relying on it. None of those epistemic or representation-side objects makes the world-side relation obtain merely by existing.

#### A.2.1:4.1 - Relation-Occurrence Identity

Do not replace the identity rule with a tuple key. One generic `U.RoleAssignment` occurrence begins when the assignment predicate starts obtaining for one fixed holder system, role value, role-taxonomy episteme, and effective reference scheme. It continues while that predicate obtains without interruption for those same four actual participants. It ends when the predicate ceases to obtain or one of those participants changes. A later resumption starts another occurrence.

An assignment assertion or occurrence description may carry an `AssignmentInterval` stating the currently known temporal extent of that occurrence. `[start, open]` can designate the current episode before its end is known. Recording the end boundary later refines the description of the same occurrence when obtaining was continuous. A gap in available evidence remains `unknown` and does not by itself split the occurrence. A demonstrated period of non-assignment ends the occurrence; a later resumption begins another. Two descriptions refer to the same occurrence only when they resolve to the same four participants and to temporal information belonging to that one uninterrupted period.

A selected model-use structure does not enter generic assignment identity. A genuinely structure-dependent relation species requires its own direct pattern, a required identity-bearing structure participant, a stronger predicate, and an explicit occurrence-identity rule.

#### A.2.1:4.2 - Filling the Declared Slots

Resolve `HolderSystemSlot` through `U.EntityRef` and check that its referent is an admitted `U.System`. Embed `RoleValueSlot` and `EffectiveReferenceSchemeSlot` by value. Resolve `RoleTaxonomyEpistemeSlot` through `U.EpistemeRef` to the exact episteme edition used for interpretation. If a receiving assertion or work use depends on a selected `BoundedModelUseStructure`, designate that structure in the receiving episteme or use relation under its direct governor.

Those four required designations correspond to the actual participants under the declared participant meanings. State the currently known temporal extent separately as `assignmentInterval` in the assertion or occurrence description. Assignment decision, responsibility, evidence, provenance, installation work, role state, capability, performed work, selected model-use structure, and publication remain separate objects or relation occurrences under their own governing patterns.

#### A.2.1:4.3 - Well-Formedness Predicates

```text
RA-1 HolderAdmission:
  the U.EntityRef filling HolderSystemSlot resolves to an admitted U.System.

RA-2 RoleInterpretation:
  the U.Role filling RoleValueSlot is interpreted through the exact
  taxonomy episteme and effective reference-scheme fillings.

RA-3 AssignmentEpisode:
  the assignment predicate obtains without interruption for the four required
  actual participants; any assignmentInterval states the currently known
  temporal extent in an assertion or occurrence description.
RA-4 NoAssignmentOverread:
  the assignment occurrence alone does not establish capability,
  role state, method admission, performed work, responsibility,
  authorization, evidence sufficiency, or publication currentness.

RA-5 InterpretationQualification:
  any selected model-use structure is designated by the receiving assertion
  or work use, not as a participant of generic U.RoleAssignment.
```

An evidence gap makes the assignment claim unknown or unrecovered; it does not demonstrate that the assignment predicate failed. A demonstrated non-assignment interval, by contrast, ends the current occurrence.

#### A.2.1:4.4 - Demand-Driven Materialization

Ordinary use can stop at a readable direct assertion:

```text
During Shift-17, Robot-7 holds InspectorRole as interpreted by
MaintenanceRoles-2026 under Maintenance-Scheme-A.
```

Expose the relation occurrence explicitly only when a receiving claim needs to refer to it, distinguish it from another episode, or use it as a participant. If any required participant filling or the continuity of the assignment episode cannot be recovered, keep the assertion reduced or lower the receiving claim. Do not insert a dummy filling or put a value of another kind into a declared slot.

#### A.2.1:4.5 - Direct Neighboring Relations

| Current question | Direct exit | Why it stays separate |
| --- | --- | --- |
| Is the holder able to do the work? | `A.2.2` capability and capability-fit relation | Assignment does not create ability. |
| Is the assignment in an enactable state now? | `A.2.5` role-state relation | State predicate, evidence, and state window differ from assignment identity. |
| Which method admits this role? | `A.3.1`, `A.3.2`, `A.15` | Method and method-description claims do not assign a holder. |
| Was work performed under the assignment? | `A.15.1`, `F.6` | `U.Work` is a dated occurrence and has its own identity. |
| What helps constitute a specialized assignment? | direct decision, installation, responsibility, or commitment relation | It is constitutive only when the specialized assignment ontology says so. |
| What supports knowledge or use of the assignment claim? | direct evidence, reliance, or provenance relation | It refers to the assignment occurrence or assertion without making the world-side relation obtain. |
| Does a DDD organization change this receiving interpretation? | `A.1.1` plus the receiving assertion or work-use pattern | The receiving episteme or use may designate the selected structure; generic `U.RoleAssignment` gains no optional participant. |

A constituting decision, installation relation, or another assignment-establishing occurrence can help make a specialized assignment relation obtain only when that direct ontology says so. Evidence, reliance, and provenance relations instead support knowledge or use of the assignment claim. Do not use epistemic support as the world-side constituting condition by default.

#### A.2.1:4.6 - Performed-Work Attribution

When dated work is performed under role holding, name the admitted holder System, exact Work, and exact assignment directly:

```text
Robot-7 performed InspectionWork-17 under RoleAssignment-17.
performedUnderAssignment(InspectionWork-17, RoleAssignment-17)
```

`Robot-7` is the admitted System in `RoleAssignment-17.HolderSystemSlot`. `A.15.1` governs `InspectionWork-17`; `A.2.1` governs `RoleAssignment-17`; `F.6` owns the attribution relation. The assignment does not prove that work occurred, and the work occurrence does not alter assignment identity.

If source wording says `RoleEnactment`, recover the dated `U.Work` occurrence, exact `U.RoleAssignment`, admitted holder System, and direct `performedUnderAssignment(W, RA)` relation. Do not introduce a second run-time U-kind or relation occurrence beside work and assignment.

#### A.2.1:4.7 - Legacy Context Shorthand

`Holder#Role:Context@Window` is source notation, not the assignment ontology. `Context` is an untyped source label here. Recover the exact referent, its kind, and the direct relation that makes it relevant. If it denotes an independently selected `BoundedModelUseStructure` that changes a receiving interpretation, designate that structure in the receiving assertion or work use. Otherwise keep the recovered referent in its own direct relation; never invent a generic context or model-use participant for `U.RoleAssignment`.

