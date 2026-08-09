---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__005_solution.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:4 — Solution"
line_start: 18977
line_end: 19143
dependencies:
  - "A.15.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.24.UK"
keywords:
---

### A.6.5:4 - Solution

Apply relation-declaration slot discipline only after the direct relation and its relation-participant meanings have been recovered. Give every relation-participant meaning needed by the current typed use one complete `SlotSpec` in the `RelationSignature`, leave relation obtaining and occurrence identity with the direct governing pattern, and follow the `A.6.REL` minimum-current-object rule: a later use adds only its current object and the direct relation to an already recoverable object rather than restating the complete relation-object architecture.

#### A.6.5:4.0 - Ontological status of the discipline

Relation-declaration slot discipline is a rule set, not a durable U-kind. This pattern reuses `RelationSignature`, `SlotSpec`, `SlotKind`, `ValueKind`, and `RefKind` from the existing signature and relation vocabulary; it introduces no U-kind. The notation `U.RelationSlotDiscipline` is not admitted: it has no separate instances, identity rule, grounding rule, constructive assembly, or ontic settlement. The governed object in this pattern is one `SlotSpec` declaration belonging to one exact `RelationSignature`. Operation argument and result declarations remain under `A.6.1`; mathematical operands and their order remain representation elements under `C.29`.

A.15.3 may cite one exact SlotSpec as the target of a planned participant designation inside a `U.WorkPlan`. That citation does not fill the SlotSpec, extend SlotSpec to another description family, make the planned designation an actual participant, or make the direct relation obtain. Planned operation arguments and results instead cite their exact A.6.1 declarations. No method-description, plan, work, evaluation, card, schema, or record field becomes a SlotSpec. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant.

#### A.6.5:4.1 - Keep pattern scope exact

| Governed object | Governing pattern | What A.6.5 contributes |
|---|---|---|
| Direct relation kind, relation-participant meanings, and relation obtaining predicate | the direct relation pattern | no replacement; a compatible `RelationSignature` contains corresponding SlotSpecs governed by A.6.5 |
| Relation occurrence and identity | the direct relation pattern with `A.6.REL` | exact participant ValueKinds; refMode applies only to relation-participant designations in an assertion or relation-occurrence description episteme |
| `RelationSignature` declaration | `A.6.0` | complete `SlotSpec` declarations inside its vocabulary item |
| Assertion that a predicate obtains | `C.2.1` and the direct claim pattern | no new assertion kind; the assertion can name exact relation participants |
| Local derived kind of participants | `C.3` and `C.3.1` | a local kind whose extent rule selects actual participants corresponding to one declared relation-participant meaning; the SlotKind remains declaration-local |
| Planned participant designation | `A.15.2` and `A.15.3` | one exact SlotSpec may be cited as the target of a planned filling; A.6.5 contributes only the declaration-local SlotKind, ValueKind, and refMode discipline and establishes neither the plan claim nor actual participation |

None of these objects gets its identity or truth condition from A.6.5. A.6.5 governs typing discipline at their shared boundary.

#### A.6.5:4.2 - Declare one complete SlotSpec for each relation-participant meaning needed by typed reuse

The following code block is a compact representation of a declaration under `C.29`. Its assignment mark, angle brackets, order, and alternatives are notation elements; the prose below states their FPF meaning.

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

**SlotKind** is the declaration-local kind by which one exact `RelationSignature` distinguishes one relation-participant meaning. `HolderSystemSlot` and `RoleTaxonomyEpistemeSlot` are different SlotKinds inside the `U.RoleAssignment` declaration even when receiving assertions carry both designations by reference. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant. A mathematical operand or numbered argument belongs to its mathematical representation, not to the relation declaration.

**ValueKind** is the exact world-side kind admitted for the actual participant corresponding to the declared participant meaning. Recover it from an accepted kind declaration under its governing pattern. That declaration may settle a durable U-kind, a current C.3 kind, a Concept-Set entry, or an imported sort whose bridge states the corresponding FPF kind. If one proposed ValueKind hides several kinds for which the predicate has different meaning, recover their real common kind or split the relation kind. A prose list of alternatives does neither.

**RefKind** is the kind of reference used when a receiving assertion or relation-occurrence description episteme carries a relation-participant designation by reference. A system applying the governed resolution method obtains a participant of the declared ValueKind as referent. `U.EntityRef`, `U.HolonRef`, `U.EpistemeRef`, and `U.StructureRef` are examples only where their direct patterns admit them. The shorthand `byRef` is usable in a compact local sketch only when the exact RefKind is declared next to that sketch; it is not a complete `refMode` by itself.

**ByValue** means that an assertion or relation-occurrence description episteme carries a value as its relation-participant designation. **By reference** means that it carries a reference value of the declared RefKind as that designation. In both cases, the designation denotes the world-side actual participant. The reference value retains its RefKind, its referent retains the declared ValueKind, the SlotSpec remains declaration content, and the relation occurrence retains its direct identity.

**Naming and source-token repair.** Use `...Slot` only for one declaration-local SlotKind inside one exact `RelationSignature`. Use `...Ref` only for an admitted RefKind or for a governed reference value or designator of that kind; never use it for the actual participant or the SlotKind. Keep the participant's ValueKind name free of both suffixes. Thus `HolderSystemSlot` is the SlotKind, `U.System` is the participant ValueKind, and `Robot_7_Ref : U.EntityRef` is a reference designation whose referent is `Robot_7 : U.System`. If a source token such as `holder` conflates those objects, split them rather than cosmetically renaming the token. A concrete source field keeps its source name and is related to `HolderSystemSlot` only through an explicit declaration or C.29 correspondence.

#### A.6.5:4.3 - Apply the well-formedness constraints

The following labelled block represents seven rules for reviewing a declaration episteme. The labels and indentation are presentation elements, not SlotSpecs, relation participants, or work occurrences.

```text
A6.5-S1 CompleteSlotSpec:
  every relation-participant meaning needed by reusable typed use has one SlotSpec
  with exactly one SlotKind, one ValueKind, and one refMode.

A6.5-S2 LocalSlotKind:
  SlotKind is interpreted only inside the exact RelationSignature that
  contains the corresponding SlotSpec.

A6.5-S3 ExactParticipantKind:
  each actual participant corresponding to the declared relation-participant meaning
  has the declared ValueKind; each receiving-episteme designation denotes such a participant.
  A C.3 kind ordered by an explicit U.SubkindOf relation may narrow
  that range only when typed membership or substitution is current.

A6.5-S4 HonestReference:
  when refMode is a RefKind, the receiving assertion or description carries
  a reference of that RefKind whose resolution denotes a participant
  of the declared ValueKind. The relation itself does not store it.

A6.5-S5 DirectPredicateGovernance:
  the direct governing pattern contains statements of the relation predicate,
  applicability, and any relation occurrence-identity rule.

A6.5-S6 NoHiddenUnion:
  one ValueKind does not hide participant kinds for which the direct
  predicate has different semantics. Recover one real common ValueKind or split the relation kind.

A6.5-S7 RepresentationBoundary:
  a representation or publication form does not become the
  world-side participant or relation occurrence by form.
```

A system performing typed substitution keeps the SlotSpec fixed and checks a proposed relation-participant designation against the exact ValueKind. A system performing retargeting changes a reference value in an assertion or description while preserving SlotKind, ValueKind, and RefKind. Neither operation changes a world-side participant or makes the direct predicate true. The direct owner defines that predicate and identity rule; the current case must supply the relevant facts or constituting history. A system evaluates those facts by the direct method, and a claim-bearing episteme records affirmative or negative polarity. Only when an explicit reliance judgment is current does `A.10` or the receiving evaluation separately record supported, refuted, or unresolved reliance. Type compatibility, assertion polarity, evidence, and reliance establish neither obtaining nor occurrence identity.

#### A.6.5:4.4 - Distinguish predicate grammar from holonhood and agency

A relation predicate is often written as a verb phrase: a system **holds** a role, a part **belongs to** a whole, one claim **supports** another, or one occurrence **results from** work. The grammatical verb only helps express the predicate. It does not settle the ontological kind of what the expression denotes.

Use the direct patterns for that settlement:

- `U.Work` and `U.Method` are admitted holon kinds only because their governing patterns supply the required constructive assembly, composition, identity, and meta-holon-transition conditions. `U.Transformation` is instead a root U-kind under `A.3.4` for one independently grounded actual bounded change. Verb-shaped wording proves neither classification.
- `U.Role` is a work-facing role value, not a holon. An admitted `U.System` holds it through `U.RoleAssignment`.
- `U.Relation` is an individuable obtaining relation occurrence under `A.6.REL`. A SlotSpec does not give it constructive parthood or meta-holon transition and does not admit it as a holon.
- Only an admitted `U.System` acts and holds a role. Work is performed, a method is applied in work, and a transformation occurs or is carried out. The relation, method, work, transformation, role, signature, and structure do not become actors because prose gives them an active verb.

When one word could denote a relation predicate or a holon occurrence, first ground the participants and ask what obtaining or occurrence identity rule the receiving claim needs. Then select the direct pattern. Do not decide by part of speech.

Predicate grammar also decides neither claim polarity nor reliance. An ordinary relational assertion states affirmative or negative polarity for the exact direct predicate; a forecast, scenario, counterfactual, permission, or other claim family retains its exact direct governor. Only when an explicit reliance judgment is current for the declared use does `A.10` or the receiving evaluation separately state supported, refuted, or unresolved reliance. None of those claim-side distinctions makes the world-side relation obtain.

#### A.6.5:4.5 - Use progressive elaboration

Start with the lightest object that supports the named engineering use. The branch diagram maps three independent receiving-use thresholds that share one recovered direct relation; none is a prerequisite for either of the others:

```text
readable assertion of the recovered direct relation
  +-- reusable RelationSignature with SlotSpecs, when several uses need the same participant typing
  +-- explicit occurrence individuation, when a named claim or direct relation relies on occurrence identity
      +-- relation-occurrence description episteme, when a receiving episteme describes the occurrence
      +-- stable relation-occurrence reference, when a receiving episteme contains a designation of it
  +-- local C.3 kind with an extent rule, when typed quantification over corresponding participants is current
```

The branch marks are representation edges under `C.29`, not transitions in a drafting process, world-side relations, or work occurrences. They show only which additional object the named use consumes. The diagram does not make a `RelationSignature` prerequisite for explicit occurrence individuation, and it neither makes the direct relation obtain nor supplies occurrence identity. The direct owner defines the obtaining predicate; current case facts or constituting history must satisfy it. The direct occurrence-identity rule governs which occurrence is being distinguished only after that factual condition is met.

The local-kind branch does not turn every participant qualification into a kind. It is justified only when membership, substitution, quantification, or `U.SubkindOf` reasoning will be performed.

#### A.6.5:4.6 - Dispatch the world-side fact, claim, and local kind

| Current reading | Governed object | Next pattern |
|---|---|---|
| Relevant current-case facts or constituting history satisfy the direct obtaining predicate for these participants | one world-side relation occurrence whose participants retain their own kinds | direct relation pattern for the test and identity rule; the current case for its factual basis; `A.6.REL` only when occurrence identity is consumed |
| A claim-bearing episteme designates the participants under declared SlotSpecs and records affirmative or negative polarity for the direct predicate; evidence and reliance remain separate when used | an assertion episteme about the direct relation; an affirmative assertion may designate an occurrence only after current-case facts or constituting history satisfy the direct predicate and the identity rule has been applied; the assertion states but does not warrant or constitute that result; forecasts, scenarios, counterfactuals, permissions, and other claim families retain their exact governors | `C.2.1`, A.6.5, and the direct claim pattern; add `A.10` or the receiving evaluation only when a reliance judgment is current |
| A typed claim ranges over all actual participants corresponding to one declared participant meaning | local C.3 kind whose extent rule selects those participants | `C.3` and `C.3.1` |

These readings do not leave a fourth object called `RelationDefinedQualification`. Do not introduce that name or `E.24.RC`.

They also do not justify a parallel `S-kind` hierarchy for relation-position readings. Keep the direct relation fact under its relation pattern, the claim under `C.2.1`, and introduce a C.3 local kind only when membership, substitution, quantification, or typed reasoning is current.

Do not replace that split with a generic `KindWitnessedFillerSpec` or filler record. The declaration's exact local `ValueKind` types the participant meaning; when typed quantification is current, a separately governed C.3 local kind and its membership rule supply the reusable classification.

#### A.6.5:4.7 - Read the Role-Assignment SlotSpecs

`A.2.1` directly governs `U.RoleAssignment`. Its direct pattern states the predicate, obtaining condition, and occurrence-identity rule. A compatible `RelationSignature` declares the following SlotSpecs under A.6.5:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `HolderSystemSlot` | `U.System` | `U.EntityRef` | A reference whose referent is the admitted system that holds the role. |
| `RoleValueSlot` | `U.Role` | `ByValue` | The enactment-facing role value. |
| `RoleTaxonomyEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` | A reference to the exact role-taxonomy episteme used for interpretation. |
| `EffectiveReferenceSchemeSlot` | `U.ReferenceScheme` | `ByValue` | The reference-scheme value effective for the assignment. |


The four required SlotSpecs declare all participant meanings of generic `U.RoleAssignment`. A selected model-use structure that changes one receiving interpretation is designated in that receiving assertion or use, not in this generic `RelationSignature`.

`AssignmentInterval` is not another SlotKind or a ValueKind admitted for a relation participant. It is a local content value in an assignment assertion or relation-occurrence description. The field name `assignmentInterval` states the currently known temporal extent of one occurrence, including an explicit open end when the occurrence is current. Under `A.2.1`, one generic occurrence begins when the assignment predicate starts obtaining for fixed holder, role value, taxonomy episteme, and reference scheme, and continues while it obtains without interruption. Closing an open temporal description refines the same occurrence when continuity holds. A missing-evidence interval remains unknown; only demonstrated non-assignment ends that occurrence. Role state, capability, performed work, and every supporting claim remain under their direct governing patterns.

#### A.6.5:4.8 - Recover interface and port relations before declaring slots

Keep recognizable source words such as **interface**, **port**, **endpoint**, **API**, and **signature** in the recognition sentence; do not erase them and do not promote them into a generic `U.Interface`. Then use this sequence:

1. Repeat the source sentence so the practitioner can still recognize the situation.
2. Say in ordinary language what connects, crosses, or is transferred between which exact entities.
3. Recover the exact direct relation and its owner. If no current owner supplies the needed participant meanings, predicate, applicability, and identity rule, return to `A.6.RSIR` or record one missing-governor result naming the proposed participants, required predicate, and receiving use.
4. Only after that relation closes, let its `RelationSignature` declare the SlotSpecs for participant meanings actually reused by the receiving typed claim.

**Compact contrast.** In “the evaporator outlet interfaces with the compressor inlet,” keep **interfaces** for recognition. If the intended claim is that refrigerant crosses from one named outlet to one named inlet, name that medium and those two endpoints and recover the exact transfer-relation owner before declaring any slots. If **interface** instead names a diagram boundary, API description, protocol, or publication form, keep that object under its own governor. A catalogue of possible participants closes neither branch; without a direct relation owner, stop before a `RelationSignature`.

#### A.6.5:4.9 - Name the operation by the object that changes

| Operation | Exact change | Governing boundary |
|---|---|---|
| supply a designation under one SlotSpec in an assertion or description | carry a value or reference that designates the actual participant admitted by that SlotSpec | A.6.5 governs designation typing; the direct relation pattern governs the participant meaning and predicate |
| replace a participant designation in an assertion or description | change the designation associated with one SlotSpec while preserving that SlotSpec | resolve the new designation, then let a system evaluate the direct predicate by its governing method before recording assertion polarity and any separately governed reliance posture |
| substitute a participant designation in typed reasoning | replace one designation with another while preserving the SlotSpec and testing ValueKind compatibility; this operation does not replace a world-side participant or establish predicate truth | A.6.5, with C.3 only when the reasoning quantifies over a local participant kind |
| retarget a reference | replace one reference value in an episteme with another of the same RefKind | the receiving episteme's direct pattern governs its changed designation; the effective reference scheme supplies the resolution rules and the direct RefKind pattern constrains the referent range; F.18 enters only when a durable name changes; world-side change is a separate claim |
| resolve a reference | obtain the designated referent from a reference under its reference scheme | the effective reference scheme supplies the resolution rules and the direct RefKind pattern constrains the referent range; F.18 enters only when durable naming is current |
| revise or re-edition a referent | change the referred object or episteme under its own continuity rules | direct object and edition patterns |

Durable name designation is governed by F.18, not by participant-designation substitution or reference resolution. When a system selects a method at run time, use the pattern governing that method family or selector; A.6.5 supplies no method-selection operation. Do not rename that choice with the generic slot `binding` metaphor. If early or late timing matters, name which operation in this table is early or late.

