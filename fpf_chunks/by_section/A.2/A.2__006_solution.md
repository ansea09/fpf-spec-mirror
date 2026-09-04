---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "System-Role Kinds and Assignments"
section_id: "A.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__006_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.2 — System-Role Kinds and Assignments"
  - "A.2:4 — Solution"
line_start: 3063
line_end: 3200
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10.ROLE"
  - "F.4-F.6"
keywords:
  - "U.SystemRoleAssignment"
  - "ambiguous role wording"
  - "assignment"
  - "holder System"
  - "local System classification"
  - "system-role kind"
  - "work-facing contribution"
---

### A.2:4 - Solution

Use an exact local `U.Kind` when `U.System` candidates need one stable, assignable, work-facing membership distinction. Recover the kind through the candidate domain, operative condition, useful member/non-member boundary, and continuity rule. Keep practice or source provenance as a locator and comparison cue. Give a live technical name the `SystemRole` head, such as `ReviewerSystemRole` or `CoolingCirculatorSystemRole`. Do not introduce `U.SystemRole`; the concrete value is already a local `U.Kind` under C.3.

Then keep four moves separate:

1. identify the local system-role kind;
2. declare or select the `KindSignature` edition used for membership;
3. evaluate one system, kind, signature edition, and slice under C.3.2;
4. add a directly declared `U.SystemRoleAssignment` species and occurrence only when an assignment actually obtains.

Capability, assignment state, method admission, performed Work, responsibility, commitment, permission, authority, evidence, reliance, and publication remain direct neighboring claims.

#### A.2:4.1 - Recognize a System-Role Kind

A local kind is a system-role kind only when all of these conditions hold:

1. its candidate `ValueKind` is `U.System`;
2. its operative membership condition states the stable, assignable, work-facing contribution and uses directly governed candidate features;
3. at least one intended member and one relevant non-member or boundary case make the distinction testable;
4. its continuity rule says which changes preserve that distinction and which require another kind; and
5. its `KindSignature` does not treat a label, taxonomy row, description, assignment record, classification judgment, extension row, or proposed `U.SubkindOf` edge as the feature by form.

The kind asks what continuing distinction classifies candidate systems. A particular C.3.2 judgment asks whether one system satisfies the current signature now. Practice or source provenance shows where to inspect the definition; it neither creates nor splits the kind.
`CoolingPumpKind` is not thereby a system-role kind. Its identity can be a physical or functional pump distinction rather than an assignable work-facing contribution. `ShortAssignmentKind`, if declared to classify assignment occurrences by duration, is also not a system-role kind because its candidates are assignments rather than systems.

#### A.2:4.2 - Evaluate Membership without a Circular Shortcut

Each membership clause names the candidate feature's subject pattern, predicate or governed feature, applicability, dependencies, and slice. The classification has four explicit inputs:

```text
J(candidateSystem, systemRoleKind, kindSignatureEdition, contextSlice)
  -> true | false | unknown
```

An assignment may be one feature only when the local `KindSignature` explicitly uses that independently obtaining assignment predicate. There is no family-wide rule that assignment means membership. The judgment being computed, a broader-kind judgment, an extension row, or the proposed `U.SubkindOf` occurrence cannot be a premise of the same judgment.

Missing a required feature or dependency yields `unknown`, not `false`. Evidence supports a claim about the governed feature; it does not create that feature or the membership result.

Every `U.SubkindOf` proposal evaluates the aligned narrower and broader signatures independently for the same candidate and slice. Admit the order only when the C.3.1 monotonicity condition holds. The edge records an already established implication; it never produces either classification judgment.

#### A.2:4.3 - Keep Kind Identity, Declaration, and Extension Separate

The system-role kind is not its `KindSignature`, taxonomy episteme, reference scheme, classification judgment, or `KindExtension`. Same-kind continuity across declaration editions requires the C.3.1 comparison of candidate domain, operative membership distinction, member/non-member boundary, and continuity rule. A compatible criterion or scheme edition can preserve the kind while later judgments cite the edition actually used. A changed source or practice triggers that comparison but does not decide it.

An old role taxonomy or scheme can help recover the candidate domain, membership distinction, boundary probes, continuity rule, or provenance of the current definition. Its label or identifier does not decide sameness. A selected `BoundedModelUseStructure` can qualify one receiving interpretation when that independently established organization matters; it is designated in the receiving assertion or use and is stored neither on the kind nor as an optional participant of a generic assignment or kind relation. A genuinely structure-dependent relation species instead declares the structure as a required participant, uses the stronger predicate, and states the resulting occurrence-identity law.

Use `A.1.1` before citing that structure. Select `BoundedModelUseStructure` only when exact model applicability, actual model use in assigned Work, fixed-content expression coherence, exact applied constraints, and one named selection-use frame jointly change the receiving decision. If the direct kind, relation, assertion, or Bridge already answers the question, stop there; neither a model-use label nor a wish for more background selects the structure.

#### A.2:4.4 - Admit Only Exact System-Role-Kind Domains

`U.Kind` is too broad as the assigned-kind participant domain of an assignment species. Each bounded system-role vocabulary declares one local domain whose candidates are local kinds satisfying the recognition conditions above. For example:

```text
JournalReviewSystemRoleKindDomain : U.Kind
  definitionProvenance: JournalReview-2026 (comparison cue only)
  candidateValueKind: U.Kind
  criterion:
    the candidate kind has U.System candidates, a stable assignable
    work-facing membership condition, useful boundary probes, and
    a continuity rule recovered under C.3
```
A direct assignment species uses that local domain as the `ValueKind` of its declaration-local `AssignedSystemRoleKindSlot`. The slot therefore rejects `CoolingPumpKind`, `ShortAssignmentKind`, and arbitrary local kinds. This is local C.3 typed use, not admission of `U.Kind` as a durable public root.

#### A.2:4.5 - Assignment Boundary

`A.2.1` defines the `U.SystemRoleAssignment` family. The family contains directly declared relation species rather than one permissive universal signature. Every species declares:

- `HolderSystemSlot : U.System`;
- a declaration-local `AssignedSystemRoleKindSlot` whose `ValueKind` is one exact local system-role-kind domain;
- any additional real participants needed to distinguish that species; and
- its own obtaining predicate, applicability, and occurrence-identity rule.

A simple species can declare only the holder and assigned-kind participant meanings. A stronger appointment, authorization, or work arrangement can declare another participant meaning when its actual value changes occurrence identity. The specialized occurrence itself remains a `U.SystemRoleAssignment`; do not keep a second generic occurrence beside it merely for projection.

An assignment occurrence begins when its predicate starts obtaining for the fixed participants, continues over the maximal uninterrupted predicate-true interval, and ends when a participant changes or the predicate ceases to obtain. A taxonomy episteme, reference scheme, `KindSignature`, assertion, or interval description can interpret or describe the claim without becoming another world-side participant.

Assignment does not prove classification unless the kind's signature uses that independently obtaining relation as a feature. Classification does not create an assignment. Neither one proves capability, agency, responsibility, authority, commitment, permission, functioning, method enactment, or performed Work.

#### A.2:4.6 - Relations around the Kind and Assignment

| Current claim | Subject pattern | Kept distinct |
| --- | --- | --- |
| Local kind, declaration, classification, and extension | `C.3`, `C.3.1`, `C.3.2` | system-role kind, `KindSignature`, four-input judgment, optional extension, and kind-continuity decision |
| System-role assignment | `A.2.1`, `A.6.5`, `A.6.REL` | direct species, exact participants, predicate, applicability, and uninterrupted occurrence identity |
| Assignment state | `A.2.5` | exact assignment occurrence, `SystemRoleAssignmentStatePredicate`, `SystemRoleAssignmentStateRelation` occurrence, and its maximal truth interval; target evaluation window, assertion polarity, evidence, and reliance remain separate |
| Capability | `A.2.2` | holder, capability instance, envelope, measures, currentness, and fit predicate |
| Relations among system-role kinds | `A.2.7`, `C.3.1` | exact kind participants and substitution, incompatibility, bundle, or monotonic qualification relation |
| Description and naming | `F.4`, `F.5`, `F.18` | kind, `SystemRoleKindDescription`, names, and publication or access carrier |
| Method and Work | `A.3`, `A.13`, `A.15.1`, `F.6` | Method and MethodDescription; exact actual performer recovered through A.13; independently admitted Work occurrence; assignment and F.6 attribution only when precise assignment-bound attribution is expressly consumed |
| Responsibility, commitment, permission, or authority | direct domain pattern, `A.2.8`, `A.2.8.PER`, or `missing-governor` | actual bearer, exact relation participants, predicate, and instituting or permission basis |
| Evidence, reliance, or publication | `A.10`, `A.15.4`, `B.3`, `C.2.1`, `E.17`, `F.10` | episteme, evidenced claim, reliance, provenance, currentness, and publication relation |

Select only the objects needed by the current claim. None of these values is a “part of the role”.

`SystemRoleKindDescription` is an F.4 description episteme whose exact EntityOfConcern is one system-role kind. An episteme about an assignment or a relation among kinds has that assignment or relation as its EntityOfConcern instead.

#### A.2:4.7 - Recover Contribution Wording before Formalizing It

The phrase “the role of X” often means that X contributes to a use. Apply `E.10.ROLE` first. If X is an admitted system and the claim needs a work-facing classification, recover the local system-role kind and C.3.2 judgment; add an assignment only when holding is claimed. Otherwise keep X in its actual kind and name the direct relation or declaration place.

| Ordinary wording | Governed repair |
| --- | --- |
| `RFC 9110 plays a normative role in this design` | Keep the publication as an episteme and state the current external-rule, constraint, source-use, or publication relation selected by the design claim. |
| `this dataset plays the benchmark role` | Keep the dataset as an episteme and state the measurement, evidence, benchmark, source-use, or currentness relation that actually obtains. |
| `this parameter has the control role` | Recover the Method or model parameter, or an A.6.5 participant slot, from the direct declaration. |
| `this interface plays the integration role` | Recover the selected module-interface, port, signature, or protocol relation under its governor. |

Use these recognition probes to identify the relation in the current claim. If no direct relation can yet be named, return the exact `missing-governor` rather than minting a system-role kind.

#### A.2:4.8 - System-Role Vocabularies and Relations among Kinds

A system-role-vocabulary or taxonomy episteme may state local kind names, declarations, and selected relation claims under an effective reference scheme. Each live kind needs the C.3 distinction that lets readers recover it; each judgment cites its actual signature edition. An assignment claim separately requires an obtaining A.2.1 relation.

Use `A.2.7` to state one selected `SystemRoleKindRelationStructure` over exact local system-role kinds and admitted relations among them. A receiving use can cite an assertion about substitution, incompatibility, bundle, qualification, or another residual relation alongside separately stated assignments, state, capability, and Work. Systems and assignments are not participants of the kind-relation structure.

Algebraic, graph, matrix, embedding, or neural representations are mathematical lenses over that selected structure when a project declares the lens use. They neither create the kinds nor make a relation obtain.

| System-role kind | Recognition case | Boundary |
| --- | --- | --- |
| `CoolingCirculatorSystemRole` | A pump supplies a circulation contribution in plant operation. | Capability, assignment, functioning, and performed Work remain separate. |
| `TestArticleSystemRole` | The same pump is selected for qualification use. | The classification or assignment does not change pump identity. |
| `VerifierSystemRole` | A person, team, organization, service, or non-human technical system supplies verification contribution under its local criterion. | A verification report is an episteme, not the classified system. |
| `TransformerSystemRole` | A system is classified for a transformation-facing contribution. | For performed Work, name the performer system. |

#### A.2:4.9 - Reduced Use and Stronger Claims

Ordinary “Alice is reviewer” or “this component plays a control role” wording can remain Plain when no decision, attribution, admission, or reliance depends on another technical distinction. Do not materialize a kind, judgment, or assignment merely to decorate the sentence.

When a stronger claim appears, add only the needed object:

- the local kind and judgment when classification matters;
- the assignment occurrence when who holds what and when matters;
- the direct state, capability, method, Work, responsibility, commitment, permission, evidence, reliance, or publication relation when that relation carries the claim;
- the exact C.3.3 kind relation and, when local meanings differ, F.9 relation needed for cross-local use, without merging the kinds or creating assignments.

The earlier Plain sentence is not evidence for a stronger claim.

