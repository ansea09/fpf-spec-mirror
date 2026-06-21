---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__006_solution.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:4 — Solution"
line_start: 20226
line_end: 20313
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.7"
  - "A.3.4"
  - "B.2"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "C.30"
  - "E.17"
keywords:
---

### A.12:4 - Solution

Use A.12 as a thin acting-side pattern.

#### A.12:4.1 - Acting-Side Externalization

For a change-bearing claim, recover this relation frame before relying on self-action wording:

```text
ActingSideExternalization@Context:
  changedHolonRef:
  actingSystemRef: U.System or candidate acting system admitted by direct pattern
  actingRoleAssignmentRef:
  boundedContextRef:
  transformationRef?: U.Transformation
  methodRef?
  methodDescriptionRef?
  workPlanRef?
  workOccurrenceRef?
  holonBoundaryCrossingRelationRef?
  evidenceRelationRefs?
  strongerOwnerRefs:
```

The acting system and the changed holon are distinct slot fillers for the current change-bearing claim. They may be parts of a larger holon, and they may be tightly coupled, but the acting position is not the changed position for that claim.

`ActingSideExternalization@Context` is a relation frame, not a U-kind, acting-system kind, record that acts, or evidence that change occurred. It names which direct owner governs each neighboring claim.

Use:

- `A.3.4` when `transformationRef` becomes current;
- `A.15` and `A.15.1` when method, work plan, work occurrence, or work success becomes current;
- `A.2.1` and `A.2.7` when role assignment or role relation becomes current;
- `A.10` when evidence or source independence becomes current;
- `A.1`, `A.14`, and `C.13` when holon identity, part-whole, or constructive grounding becomes current.

#### A.12:4.2 - Reflexive Split

For "self-" claims, do not accept the self-action wording directly. Recover a larger holon and at least two distinct positions inside it:

```text
ReflexiveSplit@Context:
  containingHolonRef:
  actingPartOrSubsystemRef:
  changedPartOrSubsystemRef:
  boundedContextRef:
  holonDelimitationRelationRefs?
  holonBoundaryCrossingRelationRef?
  actingRoleAssignmentRef?
  transformationRef?
  methodRef?
  workOccurrenceRef?
  evidenceRelationRefs?
```

The split is a modeling move, not a claim that the two positions are always permanent physical modules. They can be stable subsystems, temporal phases, organizational assignments, software components, or another directly governed structure. If the split relies on parthood, use A.14 and C.13. If it relies on role assignment, use A.2.1 and A.2.7. If it relies on temporal phases, use the temporal owner.

The minimal rule is:

```text
actingPartOrSubsystemRef != changedPartOrSubsystemRef
```

for the current change-bearing claim.

#### A.12:4.3 - Episteme And Publication Cases

An episteme does not act by itself. If a source says "the document updates itself", recover the acting system in role and the object that changed:

- a publication file or representation changed;
- a source record changed;
- an episteme slot relation changed;
- a claim relation, reference relation, or publication-use relation changed.

Use `C.2.1`, `E.17`, `E.17.2`, source-use, publication-use, and evidence owners for the episteme or publication side. A.12 only prevents the sentence from assigning agency to the episteme.

#### A.12:4.4 - No Super-Holon Inference

A system changing another holon does not become that holon's super-holon. Manufacturing, teaching, measurement, repair, control, telemetry, or source use can be boundary-crossing, transformation, work, evidence, or publication-use relations without being part-whole relations.

Use part-whole owners only when parthood is independently admitted.

#### A.12:4.5 - No Self-Evidence Shortcut

A.12 separates the acting side; it does not make the acting side's own output sufficient evidence for success, safety, adequacy, or authorization.

When evidence matters, use `A.10` or the direct evidence and assurance owner. The evidence relation may use an observer system, measurement setup, independent source, audit record, or accepted stronger relation. A.12 only blocks the overread that acting and evidence are the same by default.

