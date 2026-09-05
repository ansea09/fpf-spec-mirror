---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__006_solution.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:4 — Solution"
line_start: 23837
line_end: 23928
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.2.7"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
keywords:
---

### A.12:4 - Solution

Use A.12 as a thin acting-side pattern.

#### A.12:4.1 - Acting-Side Externalization

For a change-bearing claim, recover this relation frame before relying on self-action wording:

```text
ActingSideExternalization@Context:
  changedSubjectRef: one exact continuing referent identified by the identity rule that defines that referent
  actingEntityRef: exact U.Entity proposed for the acting side
  actingSystemRef?: U.System, fill only after actingEntityRef satisfies the complete A.1 U.System criterion
  a1RecognitionDispositionOrBlockerRef?: required while actingSystemRef is unfilled
  actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, only when one exact obtaining work-facing assignment is current
  actingSideParticipationRef?: one exact obtaining relation occurrence satisfying the predicate and participant meanings that define the participation, causal, or interaction claim
  transformationRef?: U.Transformation, fill only when A.3.4 identifies a bounded change of changedSubjectRef
  methodRef?
  methodDescriptionRef?
  workPlanRef?
  workOccurrenceRef?
  holonBoundaryCrossingRelationRef?: one exact obtaining relation occurrence satisfying the predicate, applicability, and identity rules that define the crossing relation
  evidenceRelationRefs?
  strongerOwnerRefs:
```

The exact entity in `actingEntityRef` and the exact referent in `changedSubjectRef` are distinct participants in the current change-bearing claim. `changedSubjectRef` is a question-local position, not a U-kind or union ValueKind: its value keeps its independently admitted kind and the identity rule that defines that referent. A presentation carrier does not become a `U.Holon` by filling the position, and a transformation reference is filled only when the practitioner applies A.3.4's change test to that same continuing referent. Before A.1 recognition, the exact disposition or blocker remains explicit and `actingSystemRef` stays unfilled. After recognition, `actingSystemRef` identifies that same acting-side entity under `U.System`; it does not introduce another actor. The participants may be parts of a larger holon and may be tightly coupled, but the acting position is not the changed position for that claim.

`ActingSideExternalization@Context` is a relation frame, not a U-kind, acting-system kind, record that acts, or evidence that change occurred. For each neighboring claim it names the exact subject and actual participants and may cite the pattern or rule that defines, constrains, or tests its direct predicate. Neither A.12 frame has a generic context, scope, or qualifier position. First ask what the qualifier changes. If it changes claim content, EntityOfConcern, or the effective reference scheme, C.2.1 identifies another episteme. If it selects whether one exact `U.ContextSlice` belongs to the set-valued applicability boundary of a claim, A.2.6 defines the exact `U.ClaimScope` and membership evaluation. Select a `BoundedModelUseStructure` under A.1.1 only when the named decision use depends on the joint organization of one model edition's applicability, actual use in assigned Work, fixed-content expression coherence, exact applied constraints, and a complete selection-use frame. Otherwise state the exact condition, value, or relation as a claim and apply or cite the rule that defines or tests it. Recover an exact defining or constraining ClaimGraph only when its identity materially changes interpretation, comparison, migration, conflict, publication, or reuse. Do not copy a claim phrase or nearby participants into an A.12 field, and do not invent one umbrella qualifier object.

Use:

- `A.3.4` when `transformationRef` becomes current;
- `A.15` and `A.15.1` when method, work plan, work occurrence, or work success becomes current;
- `A.2.1` when an exact assignment occurrence becomes current, and `A.2.7` only when a relation among exact local system-role kinds becomes current;
- `A.10` when evidence or source independence becomes current;
- `A.1`, `A.14`, and `C.13` when holon identity, part-whole, or constructive grounding becomes current.

#### A.12:4.2 - Reflexive Split

For "self-" claims, do not accept the self-action wording directly. Recover one larger holon and two exact entity parts or subsystems inside it:

```text
ReflexiveSplit@Context:
  containingHolonRef: exact U.Holon
  actingPartOrSubsystemRef: exact U.Entity
  changedPartOrSubsystemRef: exact U.Entity
  holonDelimitationRelationRefs?: exact obtaining parthood relations to containingHolonRef
  holonBoundaryCrossingRelationRef?: one exact obtaining relation satisfying the predicate, applicability, and identity rules that define the crossing relation
  actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, only when one exact obtaining work-facing assignment is current
  transformationRef?
  methodRef?
  workOccurrenceRef?
  evidenceRelationRefs?
```

`ReflexiveSplit@Context` carries no system-recognition position. Its two part-or-subsystem fields identify exact entities, not phases, assignments, relation occurrences, or generic structures. Each filled entity position needs an independently obtaining parthood or subsystem relation to `containingHolonRef` under A.14 and the direct part-relation specialization.

When the acting-position entity must also be evaluated as a system, use a companion `ActingSideExternalization@Context`: its `actingEntityRef` identifies that exact `U.Entity`; its disposition or blocker remains explicit before recognition; and its optional `actingSystemRef` may identify the same entity only after A.1 recognition. Do not insert `actingSystemRef` or an A.1 disposition into `ReflexiveSplit@Context`.

A temporal phase, system-role assignment, parthood occurrence, software-module description, or selected structure remains a separate object under the identity and relation rules that define it. A software component fills a part-or-subsystem field only when it is itself the exact entity and its direct part relation obtains. If a source supplies only unlike positions such as phases or assignments, state those direct relations and do not force them into this frame.

The minimal rule is:

```text
actingPartOrSubsystemRef != changedPartOrSubsystemRef
```

for the current change-bearing claim.

#### A.12:4.3 - Episteme And Publication Cases

An episteme does not act by itself. If a source says "the document updates itself", first recover the exact acting entity and decide which one of these different changed-object readings is current:

- **Carrier-change reading.** One exact publication file, representation carrier, or source-record carrier continues through a separately grounded change under its direct carrier identity rule. It may fill `changedSubjectRef` as that exact carrier, not as a `U.Holon` merely by carrier form; use A.3.4 only when the bounded change of that same referent is independently admitted.
- **Episteme-edition reading.** Changed claim content identifies another episteme, with the predecessor, successor, and exact edition relation governed separately. Do not call it transformation of one unchanged episteme.
- **Relation-occurrence reading.** One exact episteme-related direct relation—for example constitution, empirical grounding, edition, reference, or publication use—obtains when its actual participants satisfy its direct predicate. Its direct identity and change rules determine whether that occurrence continues, ceases, or is replaced. Use C.2.1 for episteme identity and edition distinctions and E.17 or E.24.PUB for publication use. The relation occurrence does not fill `changedSubjectRef`; if an actual change is also claimed, identify its continuing subject and A.3.4 facts separately.

Choose one reading before filling a singular field; never use a carrier, episteme, and relation occurrence as interchangeable values. Name the acting entity under `U.System` only after A.1 recognition, and fill a work-facing assignment only when one exact `U.SystemRoleAssignment` obtains. Use `C.2.1`, `E.17`, `E.17.2`, and the patterns for source use, publication use, carriers, editions, and evidence when those objects or relations are current. A.12 only prevents the sentence from assigning agency to the episteme.

#### A.12:4.4 - No Containing-Whole Inference From Interaction

A system changing another holon does not thereby become its part or the larger whole containing it. A manufacturing, teaching, measurement, repair, control, telemetry, or source-use case may contain separately governed boundary-crossing, transformation, work, evidence, or publication-use claims; none is a part-whole claim merely by wording, and A.12 makes none of them obtain.

Use A.14 or the rule defining the exact part-whole predicate only when parthood is independently admitted.

#### A.12:4.5 - No Self-Evidence Shortcut

A.12 separates the acting side; it does not make the acting side's own output sufficient evidence for success, safety, adequacy, or authorization.

When evidence matters, use A.10's evidence and source-use relations; use B.3 when an assurance conclusion is also claimed. The evidence relation may use an observer system, measurement setup, independent source, audit record, or accepted stronger relation. A.12 only blocks the overread that acting and evidence are the same by default.

