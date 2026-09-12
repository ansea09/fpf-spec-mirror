---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__006_solution.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:4 — Solution"
line_start: 24021
line_end: 24122
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

Separate the acting participant from the subject claimed to change. Add the precise claims needed to explain the case.

#### A.12:4.1 - Acting-Side Externalization

When a precise change-bearing account is needed, use the following frame to distinguish the participants and the claims you are making. It is not a required form for an ordinary acting-side explanation. Fill a neighboring-claim position only when that claim is needed and its own admission conditions hold:

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

Identify `actingEntityRef` and `changedSubjectRef` as distinct participants in the claim. `changedSubjectRef` is a question-local position, not a U-kind or union ValueKind: its value retains its independently admitted kind and identity rule. A presentation carrier does not become a `U.Holon` by filling it. Fill `transformationRef` only when A.3.4 establishes a bounded change of that same continuing referent.

Before calling the acting entity a `U.System`, apply the complete A.1 criterion. Until recognition is established, retain the entity and its `recognized | rejected | unknown` disposition or blocker, and leave `actingSystemRef` unfilled. Once recognized, that position names the same entity under `U.System`, not another actor. Tight coupling or membership in a larger holon does not merge the acting and changed positions.

`ActingSideExternalization@Context` describes the relation frame; it does not define a U-kind or establish that a change occurred. Each neighboring claim has its own participants and defining or testing rule. Neither A.12 frame has a generic context, scope or qualifier position. Ask what the proposed qualifier changes:

- If claim content, EntityOfConcern or the effective reference scheme changes, C.2.1 identifies another episteme.
- If the question is whether a `U.ContextSlice` belongs to a claim’s set-valued applicability boundary, use A.2.6’s `U.ClaimScope` and membership evaluation.
- Select A.1.1’s `BoundedModelUseStructure` only when the decision depends jointly on one model edition’s applicability, actual use in assigned Work, fixed-content expression coherence, applied constraints and complete selection-use frame.

For another condition, state the condition or relation and apply its defining or testing rule. A pattern citation is usually enough to locate that rule. Recover its identity-bearing defining or constraining ClaimGraph only when the graph’s identity changes interpretation, comparison, migration, conflict, publication or reuse. A claim phrase or nearby participant does not fill an A.12 field unless it satisfies that field’s meaning.

Use:

- `A.3.4` when `transformationRef` becomes current;
- `A.15` and `A.15.1` when method, work plan, work occurrence or work success is claimed; for an actual Work occurrence, follow the performer/admission/attribution order below;
- `A.2.1` when an exact assignment occurrence becomes current, and `A.2.7` only when a relation among exact local system-role kinds becomes current;
- `A.10` when evidence or source independence becomes current;
- `A.1`, `A.14`, and `C.13` when holon identity, part-whole, or constructive grounding becomes current.

For a dated Work claim, first establish each actual performer’s A.13 core: an admitted System, a local agential system-role kind and criterion it satisfies, an obtaining assignment, and the scope, situation and window the use needs, supported by evidence. Add an agency-characteristic profile only for a consumed Grade/autonomy/profile claim, a characteristic-dependent local criterion, or an assurance use that requires it. Then admit the occurrence independently under A.15.1 from its performance history, enacted Method, temporal extent and obtaining containing-System relation. Only if precise assignment-bound attribution is also claimed does F.6 relate that admitted Work to the same obtaining assignment. A Work-only account stops after admission.

#### A.12:4.2 - Reflexive Split

Use Reflexive Split when the acting and changed participants are two distinct entity parts or subsystems of one containing holon, with an independently obtaining part relation for each. Establish those premises before using this frame; the word "self-" alone does not establish them. If the source supports another reading, keep that acting-side or relation account and leave any unsupported internal-parts claim open.

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

If a source says "the document updates itself", identify the acting participant and decide which changed-object reading the claim needs:

- **Carrier-change reading.** One exact publication file, representation carrier, or source-record carrier continues through a separately grounded change under its direct carrier identity rule. It may fill `changedSubjectRef` as that exact carrier, not as a `U.Holon` merely by carrier form; use A.3.4 only when the bounded change of that same referent is independently admitted.
- **Episteme-edition reading.** Changed claim content identifies another episteme, with the predecessor, successor, and exact edition relation governed separately. Do not call it transformation of one unchanged episteme.
- **Relation-occurrence reading.** One exact episteme-related direct relation—for example constitution, empirical grounding, edition, reference, or publication use—obtains when its actual participants satisfy its direct predicate. Its direct identity and change rules determine whether that occurrence continues, ceases, or is replaced. Use C.2.1 for episteme identity and edition distinctions and E.17 or E.24.PUB for publication use. The relation occurrence does not fill `changedSubjectRef`; if an actual change is also claimed, identify its continuing subject and A.3.4 facts separately.

Choose the reading before filling a singular field; carriers, epistemes and relation occurrences are not interchangeable values. Call the acting entity a `U.System` only after A.1 recognition, and fill a work-facing assignment only when that `U.SystemRoleAssignment` obtains. Use C.2.1 for episteme identity, E.17/E.17.2 for publication relations and E.24.PUB for the publication-form boundary when those claims are needed.

#### A.12:4.4 - No Containing-Whole Inference From Interaction

Treat the interaction and part-whole claims separately. A system changing another holon does not thereby become its part or the larger whole containing it.

For a part-whole claim, use A.14 or the rule defining the exact part-whole predicate to test parthood independently of the interaction claim.

#### A.12:4.5 - No Self-Evidence Shortcut

A producer’s output does not automatically establish a claim of success, safety, adequacy or authorization. State the claim you need to support, then use A.10 to identify its evidence and provenance. The producer’s output may contribute when that evidence relation supports the claim.

Use B.3 when a separate assurance conclusion is requested. Introduce an observer, measurement setup or independent source only when its contribution matters to the evidence account.

