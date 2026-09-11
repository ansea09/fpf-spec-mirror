---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__005_solution.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:4 — Solution"
line_start: 19368
line_end: 19537
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

Apply relation-declaration slot discipline only after the direct relation and its relation-participant meanings have been recovered. Give every relation-participant meaning needed by the current typed use one complete `SlotSpec` in the `RelationSignature`. Let the direct-relation definition supply the obtaining predicate and occurrence-identity rule. Follow the `A.6.REL` minimum-current-object rule: a later use adds only its current object and the direct relation to an already recoverable object rather than restating the complete relation-object architecture.

#### A.6.5:4.0 - Ontological status of the discipline

Relation-declaration slot discipline is a rule set, not a durable U-kind. This pattern reuses `RelationSignature`, `SlotSpec`, `SlotKind`, `ValueKind`, and `RefKind` from the existing signature and relation vocabulary; it introduces no U-kind. A.6.5 constrains one `SlotSpec` declaration belonging to one exact `RelationSignature`. Operation argument and result declarations remain under `A.6.1`; mathematical operands and their order remain representation elements; use `C.29` when that representation is used as a declared mathematical lens.

A.15.3 may cite one exact SlotSpec as the target of a planned participant designation inside a `U.WorkPlan`. That citation does not fill the SlotSpec, extend SlotSpec to another description family, make the planned designation an actual participant, or make the direct relation obtain. Planned operation arguments and results instead cite their exact A.6.1 declarations. Only a declaration-local participant specification inside one exact `RelationSignature` is a SlotSpec. Method-description, plan, work, evaluation, card, schema, and record fields retain the kinds and declaration rules supplied by their defining patterns. A field that receives relation semantics follows the applicable declaration or representation correspondence route in §4.2; the field, SlotSpec, designation, and actual participant remain distinct.

#### A.6.5:4.1 - Keep pattern scope exact

| Object or claim | Defining or constraining content | What A.6.5 contributes |
|---|---|---|
| Direct relation kind, relation-participant meanings, and relation obtaining predicate | the direct-relation definition | no replacement; A.6.5 supplies the SlotSpec discipline for a compatible `RelationSignature` |
| Relation occurrence and identity | the direct-relation definition and `A.6.REL` | exact participant ValueKinds; refMode applies only to relation-participant designations in an assertion or relation-occurrence description episteme |
| `RelationSignature` declaration | `A.6.0` defines the containing signature | complete `SlotSpec` declarations inside its vocabulary item |
| Assertion that a predicate obtains | `C.2.1` defines assertion content; the direct claim pattern defines that claim family | no new assertion kind; the assertion can name exact relation participants |
| Local derived kind of participants | `C.3` and `C.3.1` define the kind, subkind, and continuity questions; `C.3.2` supplies its KindSignature, membership judgment, and optional extension | when a `RelationSignature` is needed, its SlotSpec uses the declared participant ValueKind while the SlotKind remains local to that declaration |
| Planned participant designation | `A.15.2` and `A.15.3` define the planned claim | one exact SlotSpec may be cited as the target of a planned filling; A.6.5 contributes only the declaration-local SlotKind, ValueKind, and refMode discipline and establishes neither the plan claim nor actual participation |

None of these objects gets its identity or truth condition from A.6.5. A.6.5 supplies the participant-declaration and designation-typing discipline at their shared boundary.

#### A.6.5:4.2 - Declare one complete SlotSpec for each relation-participant meaning needed by typed reuse

The following code block is a compact representation of a declaration. Its assignment mark, angle brackets, order, and alternatives are notation elements.

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

**SlotKind** is the declaration-local kind by which one exact `RelationSignature` distinguishes one relation-participant meaning. `HolderSystemSlot` and `AssignedSystemRoleKindSlot` are different SlotKinds inside the `InspectionShiftAssignment` declaration even when a receiving assertion designates the holder by reference and the assigned system-role kind by value. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit correspondence to the declared SlotSpec; use C.29 when that correspondence is part of a declared mathematical-lens use. Neither route makes the field a SlotSpec or the designation an actual participant. A mathematical operand or numbered argument belongs to its mathematical representation, not to the relation declaration.

**ValueKind** is the exact world-side kind admitted for the actual participant corresponding to the declared participant meaning. Recover it from the accepted declaration that defines that kind. The declaration may settle a durable U-kind, a current C.3 kind, a Concept-Set entry, or an imported sort whose bridge states the corresponding FPF kind. If one proposed ValueKind hides several kinds for which the predicate has different meaning, recover their real common kind or split the relation kind. A prose list of alternatives does neither.

**RefKind** is the kind of reference used when a named-use assertion or relation-occurrence description episteme carries a relation-participant designation by reference. A system applying the declared resolution Method obtains a participant of the declared ValueKind as referent. `U.EntityRef`, `U.HolonRef`, `U.EpistemeRef`, and `U.StructureRef` are examples only where their exact RefKind declarations and admission predicates apply. The shorthand `byRef` is usable in a compact local sketch only when the exact RefKind is declared next to that sketch; it is not a complete `refMode` by itself.

**ByValue** means that an assertion or relation-occurrence description episteme carries a value as its relation-participant designation. **By reference** means that it carries a reference value of the declared RefKind as that designation. In both cases, the designation denotes the world-side actual participant. The reference value retains its RefKind, its referent retains the declared ValueKind, the SlotSpec remains declaration content, and the relation occurrence retains its direct identity.

**Naming and source-token repair.** Use `...Slot` only for one declaration-local SlotKind inside one exact `RelationSignature`. Use `...Ref` only for an admitted RefKind or for a reference value or designator of that kind; never use it for the actual participant or the SlotKind. Keep the participant's ValueKind name free of both suffixes. Thus `HolderSystemSlot` is the SlotKind, `U.System` is the participant ValueKind, and `Robot_7_Ref : U.EntityRef` is a reference designation whose referent is `Robot_7 : U.System`. If a source token such as `holder` conflates those objects, split them rather than cosmetically renaming the token. A concrete source field keeps its source name and is related to the SlotSpec identified by `HolderSystemSlot` only through an explicit declaration or representation correspondence.

#### A.6.5:4.3 - Apply the well-formedness constraints



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

A6.5-S5 DirectPredicateDefinition:
  the identified direct-relation definition states the predicate,
  applicability, and any relation occurrence-identity rule.

A6.5-S6 NoHiddenUnion:
  one ValueKind does not hide participant kinds for which the direct
  predicate has different semantics. Recover one real common ValueKind or split the relation kind.

A6.5-S7 RepresentationBoundary:
  a representation or publication form does not become the
  world-side participant or relation occurrence by form.
```

A system performing typed substitution keeps the SlotSpec fixed, resolves any reference under its declared scheme, and checks the designated actual participant against the exact ValueKind; the designation must still satisfy the declared refMode and, when applicable, RefKind. A system performing retargeting changes a reference value in an assertion or description while preserving SlotKind, ValueKind, and RefKind. Neither designation operation by itself changes a world-side participant or makes the direct predicate true. The identified direct-relation definition supplies that predicate and identity rule; the current case must supply the relevant facts or constituting history. A system applies the direct obtaining test to those facts or constituting history, and a claim-bearing episteme records affirmative or negative polarity. Only when an explicit reliance judgment is current does `A.10` or the receiving evaluation separately record supported, refuted, or unresolved reliance. Type compatibility and assertion form do not by themselves establish obtaining or occurrence identity. Evidence supporting the case conclusion and any constitutive contribution are governed separately by the relevant evidence and direct-relation rules.

#### A.6.5:4.4 - Distinguish predicate grammar from holonhood and agency

A relation predicate is often written as a verb phrase: a system **is assigned to** a system-role kind, a part **belongs to** a whole, one claim **supports** another, or one occurrence **results from** Work. The grammatical verb only helps express the predicate. It does not settle the ontological kind of what the expression denotes.

Use the following definitions for that distinction:

- `A.15.1` and `A.3.1` supply the constructive assembly, composition, identity, and meta-holon-transition conditions that admit `U.Work` and `U.Method` as holon kinds. `U.Transformation` is instead a root U-kind under `A.3.4` for one independently grounded actual bounded change. Verb-shaped wording proves neither classification.
- One context-local system-role kind is admitted under `C.3` and described through `A.2`; it is neither a holon nor an assignment. An admitted `U.System` participates as holder in an assignment occurrence whose species is declared under `U.SystemRoleAssignment`.
- `U.Relation` is an individuable obtaining relation occurrence under `A.6.REL`. A SlotSpec does not give it constructive parthood or meta-holon transition and does not admit it as a holon.
- Only an admitted `U.System` acts. A system may be classified by an exact local system-role kind and may participate as holder in an obtaining `U.SystemRoleAssignment`; neither the kind nor the assignment acts. Work is performed, a Method is applied in Work, and a transformation occurs or is carried out.

When one word could denote a relation predicate or a holon occurrence, first ground the participants and ask what obtaining or occurrence identity rule the receiving claim needs. Then find its definition. Do not decide by part of speech.

Predicate grammar also decides neither claim polarity nor reliance. An ordinary relational assertion states affirmative or negative polarity for the exact direct predicate; a forecast, scenario, counterfactual, permission, or other claim family retains the rules that define that claim family. Only when an explicit reliance judgment is current for the declared use does `A.10` or the receiving evaluation separately state supported, refuted, or unresolved reliance. Those claim-side distinctions do not by themselves make the world-side relation obtain; any constitutive effect follows the direct relation's rule.

#### A.6.5:4.4a - Keep ordinary predicate parameters outside SlotSpec

A reusable predicate definition may be an ordinary A.6.0 `U.Signature` without being a `RelationSignature`. Its semantic parameters are not SlotSpecs unless an independently admitted direct relation kind has world-side participant meanings that a typed receiver must reuse. In particular, the `dependentContent` and `baseContent` parameters of `RuleContentBasisFindingDefinition@R7` are `U.ClaimGraph` values in a predicate declaration. They do not name relation participants, `SlotKind`s, occurrence positions, or a new relation kind.

A C.2.1 assertion of `derivedUsingRuleContent` or `evaluatedAgainstRuleContent` designates those exact values and its exact derivation or criterion-selection claim. A record or formula may represent the parameters; use C.29 when that representation is used as a declared mathematical lens. Table shape does not turn the parameters into SlotSpecs. If later work proposes a relation kind, it must independently pass A.6.RCD and E.24/E.24.UK with participant meanings, obtaining, applicability, and occurrence identity; the predicate declaration supplies none by implication.

#### A.6.5:4.5 - Use progressive elaboration

Start with the lightest object that supports the named engineering use. The branch diagram maps three independent receiving-use thresholds that share one recovered direct relation; none is a prerequisite for either of the others:

```text
readable assertion of the recovered direct relation
  +-- reusable RelationSignature with SlotSpecs, when several uses need the same participant typing
  +-- explicit occurrence individuation, when a named claim or direct relation relies on occurrence identity
      +-- relation-occurrence description episteme, when a receiving episteme describes the occurrence
      +-- stable relation-occurrence reference, when a receiving episteme contains a designation of it
  +-- local C.3 kind with an extent rule under C.3.2, when membership, substitution, quantification, or subkind use is current
```

The branches are independent thresholds; explicit occurrence individuation does not require a `RelationSignature`. The direct-relation definition supplies the obtaining predicate and direct occurrence-identity rule, while current case facts or constituting history must satisfy the predicate before that rule distinguishes an occurrence.

The local-kind branch does not turn every participant qualification into a kind. It is justified only when membership, substitution, quantification, or `U.SubkindOf` reasoning will be performed. C.3.2 supplies the KindSignature, pre-judgment admissibility, membership judgment, and any separately needed extension; a local-kind judgment does not require a RelationSignature or a materialized extension.

#### A.6.5:4.6 - Dispatch the world-side fact, claim, and local kind

| Current reading | Object or claim | Next pattern |
|---|---|---|
| Relevant current-case facts or constituting history satisfy the direct obtaining predicate for these participants | one world-side relation occurrence whose participants retain their own kinds | direct relation pattern for the test and identity rule; the current case for its factual basis; `A.6.REL` only when occurrence identity is consumed |
| A claim-bearing episteme designates the participants under declared SlotSpecs and records affirmative or negative polarity for the direct predicate; evidence and reliance remain separate when used | an assertion episteme about the direct relation; an affirmative assertion may designate an occurrence only after current-case facts or constituting history satisfy the direct predicate and the identity rule has been applied; the assertion states that result; assertion form by itself neither warrants nor constitutes the occurrence, and any constitutive contribution follows the direct relation's rule; forecasts, scenarios, counterfactuals, permissions, and other claim families retain their own defining rules | `C.2.1`, A.6.5, and the direct claim-family definition; add `A.10` or the receiving evaluation only when a reliance judgment is current |
| A typed claim ranges over all actual participants corresponding to one declared participant meaning | local C.3 kind whose extent rule selects those participants | `C.3` and `C.3.1` for kind, subkind, and continuity; `C.3.2` for the KindSignature, admissibility, membership judgment, and optional extension |



Keep the direct relation fact under its relation pattern, the claim under `C.2.1`, and introduce a C.3 local kind only when membership, substitution, quantification, or typed reasoning is current.

The declaration's exact local `ValueKind` constrains the actual participant corresponding to that meaning; when typed quantification is current, a separately defined C.3 local kind and its membership rule supply the reusable classification.

#### A.6.5:4.7 - Read the SlotSpecs of a Direct System-Role-Assignment Species

`A.2.1` defines the `U.SystemRoleAssignment` relation family through directly declared species. The family has no root `RelationSignature` that hides several participant laws. Conditional on an independently defined two-participant `InspectionShiftAssignment` species, a compatible `RelationSignature` declares the following SlotSpecs under A.6.5. Its predicate, applicability, and `InspectorSystemRoleKindDomain` remain supplied by that species' definition, not by the family citation:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `HolderSystemSlot` | `U.System` | `U.EntityRef` | The admitted system that is the holder; a receiving assertion designates it by an entity reference. |
| `AssignedSystemRoleKindSlot` | `InspectorSystemRoleKindDomain` | `ByValue` | The exact local system-role kind assigned under this direct species. |

Every assignment species declares its own participant meanings, predicate, applicability, and occurrence-identity rule. It adds another participant meaning only when its corresponding participant changes the predicate or occurrence identity. A `KindSignature`, system-role-taxonomy episteme, effective reference scheme, bridge, or model-use structure may interpret a receiving assertion or use when needed; it is not another participant merely because it helps interpret the claim.

`assignmentInterval` is not another SlotKind or a ValueKind admitted for a relation participant. It is a local content value in an assignment assertion or relation-occurrence description. The field states the currently known temporal extent of one occurrence, including an explicit open end when the occurrence is current. Under `A.2.1`, an occurrence of one direct species begins when its predicate starts obtaining for all fixed actual participants and continues while it obtains without interruption. Closing an open temporal description refines the same occurrence when continuity holds. A missing-evidence interval remains unknown and establishes neither continuity nor a split. The direct rule ends the occurrence when a participant changes or its predicate ceases to obtain; demonstrated non-assignment supports concluding that it ended. A.2.5 defines assignment-state predicates and direct state relations; the patterns for capability, performed Work, and supporting claims retain their distinct definitions.

#### A.6.5:4.8 - Recover interface and port relations before declaring slots

Keep recognizable source words such as **interface**, **port**, **endpoint**, **API**, and **signature** in the recognition sentence; do not erase them and do not promote them into a generic `U.Interface`. Then use this sequence:

1. Repeat the source sentence so the practitioner can still recognize the situation.
2. Say in ordinary language what connects, crosses, or is transferred between which exact entities.
3. Recover the exact direct relation and its definition. If no current definition supplies the needed participant meanings, predicate, applicability, and identity rule, require `A.6.RSIR` or record one missing-relation result naming the proposed participants, required predicate, and receiving use.
4. Only after the direct relation's definition is recovered, let its `RelationSignature` declare the SlotSpecs for participant meanings actually reused by the receiving typed claim.

**Compact contrast.** In “the evaporator outlet interfaces with the compressor inlet,” keep **interfaces** for recognition. If the intended claim is that refrigerant crosses from one named outlet to one named inlet, name that medium and those two endpoints and recover the exact transfer-relation definition before declaring any slots. If **interface** instead names a diagram boundary, API description, protocol, or publication form, use the definition for that object and use. A catalogue of possible participants closes neither branch; without a definition of the direct relation, stop before a `RelationSignature`.

#### A.6.5:4.9 - Name the operation by the object that changes

| Operation | Exact change | Relevant defining or constraining content |
|---|---|---|
| supply a designation under one SlotSpec in an assertion or description | carry a value or reference that designates the actual participant admitted by that SlotSpec | A.6.5 supplies designation typing; the direct-relation definition supplies the participant meaning and predicate |
| replace a participant designation in an assertion or description | change the designation associated with one SlotSpec while preserving that SlotSpec | resolve the new designation, then let a system apply the direct obtaining test to the relevant facts or constituting history before recording assertion polarity and any separate reliance posture |
| substitute a participant designation in typed reasoning | replace one designation with another while preserving the SlotSpec, resolving any reference under its declared scheme, and checking the designated actual participant against the ValueKind while the designation satisfies refMode and, when applicable, RefKind; designation substitution by itself does not replace a world-side participant or establish predicate truth | A.6.5; C.3/C.3.1 only when a local participant-kind or subkind use is current, and C.3.2 for that kind's membership judgment |
| retarget a reference | replace one reference value in an episteme with another of the same RefKind | the receiving episteme's definition states how it carries the designation; the effective reference scheme supplies the resolution rules and the RefKind declaration constrains the referent range; F.18 enters only when a durable name changes; world-side change is a separate claim |
| resolve a reference | obtain the designated referent from a reference under its reference scheme | the effective reference scheme supplies the resolution rules and the direct RefKind pattern constrains the referent range; F.18 enters only when durable naming is current |
| revise or re-edition a referent | change the referred object or episteme under its own continuity rules | direct object and edition patterns |

`F.18` supplies the rules for durable name designation; participant-designation substitution and reference resolution do not. When a system selects a method at run time, use the definition of that method family or selector; A.6.5 supplies no method-selection operation. Do not rename that choice with the generic slot `binding` metaphor. If early or late timing matters, name which operation in this table is early or late.

