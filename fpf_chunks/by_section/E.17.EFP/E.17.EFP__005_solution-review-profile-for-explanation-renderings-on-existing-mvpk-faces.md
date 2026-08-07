---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:4"
section_title: "Solution — review profile for explanation renderings on existing MVPK faces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__005_solution-review-profile-for-explanation-renderings-on-existing-mvpk-faces.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:4 — Solution — review profile for explanation renderings on existing MVPK faces"
line_start: 81104
line_end: 81342
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

### E.17.EFP:4 - Solution — review profile for explanation renderings on existing MVPK faces

#### E.17.EFP:4.1 - Informal definition

> `ExplanationFaithfulnessProfile` is a review profile for the explanation use of publication forms or representations of exact claim-bearing epistemes on existing MVPK faces. E.17 supplies face discipline; E.17.0 supplies viewpoint/view conformance only when `U.View` membership is material.
>
> It does not create a new face family, episteme, or source relation. C.2.1 first identifies the exact episteme expressed by the text; E.24.PUB or A.6.3.RT identifies its form or representation; and, when the ClaimGraph changes, the applicable source-to-target pattern defines the relation and its obtaining test. EFP then states the bounded explanation use of that already identified object.

#### E.17.EFP:4.1.a - Profile, episteme, and published-form distinction

`ExplanationFaithfulnessProfile` is a **review profile**. Its cases concern passive publication forms or representations of an exact `U.Episteme`; the profile itself does not act, decide, publish, constitute an episteme, or make a source-to-target relation obtain.

The distinction is executable: same source ClaimGraph means a form or representation of that source edition; changed claim content means another target episteme under C.2.1 plus an exact source-to-target relation shown to obtain under its applicable test. An EFP class applies only after that branch and cannot legalize a hidden claim change.

#### E.17.EFP:4.1.b - How to read this profile

This profile does not decide whether a claim is true or which claim-bearing object exists. It starts after C.2.1 identity and any required source-to-target relation are recoverable, then qualifies the explanation use of one publication form or representation.

- `Faithfulness` names the review question for that explanation use, not a pass verdict or an episteme-identity rule.
- Class names are bounded-use labels for a form or representation, not merit labels and not source-to-target relations.
- Use E.17 for face discipline and E.24.PUB for publication occurrence and form.
- A changed ClaimGraph identifies another episteme even when the prose remains explanatory, didactic, reconstructive, or speculative.
- A causal or counterfactual addition requires a separate hypothesis episteme under B.5.2 before any publication form can receive an EFP use label.

#### E.17.EFP:4.1.c - Local working vocabulary

This profile uses a small local vocabulary for review.

- **Source episteme and publication occurrence** = the exact source `U.Episteme` edition and, when material, the exact E.24.PUB `EpistemePublicationRelation` occurrence through which it is available. Neither is an MVPK face, form, carrier, or arbitrary physical item.
- **Current claim-bearing episteme** = the source edition when the text expresses the same ClaimGraph, or an exact target episteme when claim content changed and an obtaining source-to-target relation has been established under its direct pattern.
- **Published explanation form** = one publication form or representation of that current claim-bearing episteme on one existing face.
- **Class assignment** = the explanation-use class assigned to that published form on that face.
- **Bundle-local class difference** = a case where two forms in one bundle carry different bounded explanation uses.

These are review aids, not new kinds or relation types. EFP neither creates the current episteme nor substitutes for C.2.1, E.24.PUB, A.6.3, B.5.2, or another direct source-to-target pattern.

#### E.17.EFP:4.2 - Core profile fields

The ontic first screen is performed once, not copied into a metadata record for every note. Most published forms whose identity branch is already recoverable need only the compact explanation-use note:

| Core field | Question |
| --- | --- |
| `explanationClass` | Which local profile value is assigned to this one rendering? |
| source reference | Which exact episteme's ClaimGraph does the text express: the source edition itself or an exact target already connected by an obtaining source-to-target relation? Which source locator is sufficient to reopen that decision, and which E.24.PUB occurrence matters only when availability is load-bearing? |
| bounded explanation-reader use | What can the explanation reader do with this explanation now: understand, navigate, inspect, teach, or prepare review? |
| blocked downstream use | What wider claim or effect is not carried by the explanation? |
| reopen or boundary condition | What source change, dispute, use escalation, missing source relation, or neighboring-pattern boundary condition ends this profile use? |

The fuller field vocabulary below opens only when ambiguity or load-bearing use is present: different classes across faces, source linkage dispute, connective reconstruction, reader-fit dispute, interaction or statefulness, derivative rendering, cross-context reuse, cited reliance, work or reliance, evidence, gate, engineering justification, bridge, or coarsening boundary.

- `faceRuleRef = E.17` and `viewpointConformanceRuleRef = E.17.0`;
- `sourcePublicationOrRecordForm`;
- `targetPublicationOrRecordForm`;
- `changeTargetRef`;
- `entityOfConcernPolicy = preserve` for explanation renderings over the same underlying source `U.Episteme` edition;
- `boundedContextPolicy`;
- `viewpointPolicy`;
- `referenceSchemePolicy`;
- `representationSchemePolicy`;
- `groundingPolicy`;
- `referencePlanePolicy`;
- `claimPolicy`;
- `claimScopePolicy`;
- `publicationScopePolicy`;
- `reliabilityTransportPolicy`;
- `pinningPolicy`;
- `provenancePolicy`;
- `lossProfile`;
- `claimContinuityClass`;
- `microtheoryContinuityClass`;
- `onticContinuityClass`;
- `bridgeRequirement`;
- `worldContactPolicy`;
- `evidencePolicy`;
- `gatePolicy`;
- `workCrossing`;
- `sourceRelationRuleRef?`, `upstreamAuthoritySourceRef?`, `downstreamUseRuleRef?`, and `downstreamAuthoritySourceRef?`;
- `boundedFaces`;
- `publication-face kind value` when `publication face/form` or `interop publication form` discipline is present;
- `publicNamePolicy`;
- `explanationSourceRelationClass` using the shared `E.17:5.1b` vocabulary when source pointer, source availability or retrieval, source use, source faithfulness, claim-source relation, contradiction, omission, claim widening, added linkage, independent verification, bounded use, forbidden downstream use, or reopen trigger could diverge;
- no generic source-relation field; source relation is recorded through `explanationSourceRelationClass`;
- `augmentationRelation`;
- `addedLinkPolicy` when a non-obvious `SourceLinkedExplanationReconstruction` connective points to an actual derivation from the source claims or to an exact relation occurrence that those source claims already report and whose obtaining is independently established;
- `targetUserModel?` when reader-fit materially shapes the rendering;
- `interactionMode?` when the explanation is more than one static explanatory paragraph;
- `contrastiveQuestion?` when the rendering is answering a specific user-facing contrast or why-question;
- `boundedReaderUse?` when downstream use is bounded by intended reader and task;
- `overreadRisk?` when overinterpretation pressure is part of the review load;
- `evidenceRelation?` only when a named operative claim or receiving reliance actually consumes an A.10 evidence/provenance path;
- `noNewBoundaryClaims = true` on explanation faces;
- `compositionRule`;
- `reopenCondition`.

These fields inherit the `E.17:5.1e` local-field rule. They classify one explanation-facing rendering for review; they do not create `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, authority reference, publication face, or project-side FPF kind and reference named by value unless another FPF pattern explicitly defines or instantiates that object. The `explanationClass` value is a local source-relation and bounded-use profile value, not `ExplanationKind`, not `U.Kind`, not `EvidenceKind`, not `FaceKind`, and not a truth certificate.

When claim content changes, pause EFP until the practitioner uses C.2.1 to identify the target episteme and the applicable source-to-target pattern to identify and test the relation. EFP may then qualify a publication form of that target only when explanation use remains a distinct question; it never substitutes for that relation or its obtaining test.

#### E.17.EFP:4.2.a - Working-model first

Ordinary published forms do not restate every field or replay the ontic decision. When their exact claim-bearing episteme, MVPK face, any material E.24.PUB occurrence, and already published source references make the branch recoverable, the compact note inherits those conditions by reference.

A source-bearing review record becomes necessary when:
- explanation class differs across faces in the same publication bundle;
- the rendering relies on bounded connective prose that is not obvious from the source wording alone;
- didactic or speculative wording creates a real risk of policy, assurance, or gate misuse;
- source linkage, provenance, or reliability transport would otherwise become unclear;
- the rendering is a fork, adaptation, translation, generated explanation, tutorial, access-format conversion, or another derivative publication that can be mistaken for the source publication, source relation, or source episteme itself.

When one rendering needs its own narrower bounded claim or effect line, blocked downstream claim or effect line, or source-bearing reopen rule because distinctions were deliberately coarsened for reader fit, the issue is no longer only explanation class. Do not keep that case here as if it were merely one more helpful rendering style; apply `A.6.3.CSC Controlled Semantic Coarsening`.

#### E.17.EFP:4.2.b - What a publication-side reviewer checks first

A publication-side reviewer starts with five questions:

1. Does the text express the exact source ClaimGraph, or a different target ClaimGraph?
2. If it differs, which exact target episteme does the text express, and which obtaining source-to-target relation connects it to the source?
3. Which E.24.PUB form or A.6.3.RT representation expresses that exact episteme?
4. Which explanation-use class is claimed for that form, and what reader action changes because of it?
5. Has the form begun carrying another unsupported claim, relation, reliance, or deliberately coarsened use that must return to its direct pattern?
Questions 1–3 are prerequisites: if the exact episteme, form, or required source-to-target relation is unavailable, leave EFP and repair that object or relation under its direct pattern. If they are recoverable and the class distinction changes the next action, the compact note is complete. Open a fuller face-by-face record only when one of the ambiguity or load-bearing triggers in section 4.2 consumes additional fields.

#### E.17.EFP:4.2.c - Interpretant-side block

This profile classifies explanation use on existing faces; it does not describe full interactive explanation systems.

When reader fit materially changes the explanation class, bounded use, blocked use, or reopen condition, make only the distinction needed for that change. A familiar audience and static note may need no separate reader-model field. A contrastive or interactive case may need one or more of `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedReaderUse`, or `overreadRisk`.

These names are optional prompts, not a five-field publication block. They create no source relation, permission, evidence relation, or authority; they only expose the reader-fit difference that changes the present use.

#### E.17.EFP:4.3 - Explanation class set

The explanation-class set used in this profile is:

- `SourcePinnedExplanation`
- `SourceLinkedExplanationReconstruction`
- `DidacticRetelling`
- `SpeculativeRetelling`

In field form, the local assignment is `explanationClass = SourcePinnedExplanation | SourceLinkedExplanationReconstruction | DidacticRetelling | SpeculativeRetelling`.

Class assignment follows, and never replaces, the ontic first screen.

- `SourcePinnedExplanation` qualifies a form or representation that expresses the source edition's same ClaimGraph.
- `SourceLinkedExplanationReconstruction` qualifies a non-obvious connective only when it remains in the same source ClaimGraph because a stated derivation from exact source claims recovers it, or because the source ClaimGraph already reports an exact relation occurrence whose obtaining is independently established under its defining pattern. An independently true relation that the source does not claim belongs to another target ClaimGraph.
- `DidacticRetelling` qualifies teaching or onboarding use. It may qualify a form of the source when claim content is unchanged, or a form of an exact target connected under `A.6.3.CR`, `A.6.3.CSC`, or another applicable source-to-target pattern when pedagogy changed the ClaimGraph.
- `SpeculativeRetelling` qualifies only the bounded exploratory use of a form of a separately constituted hypothesis episteme, normally produced under `B.5.2`. It is not a speculative form of the original source ClaimGraph.

These values are not `U.Kind` values, MVPK faces, semantic merit grades, source-to-target relations, or episteme identities. They state how the published form may be used after those objects and relations have been recovered.

Class assignment is per published form on a face, not one blanket label for a whole multi-face bundle. If a `PlainView` form stays source-pinned while a `TechCard` form expresses a separately related target episteme, the bundle names both exact epistemes and the class difference.

#### E.17.EFP:4.3.a - Ordinary class-selection guidance

A practical order is:

1. compare the text's claim content with the exact source ClaimGraph;
2. if it differs, constitute the exact target episteme and recover the obtaining source-to-target relation under its direct pattern;
3. identify the publication form or representation of the resulting exact episteme;
4. assign an EFP class only if a bounded explanation-use distinction still changes the reader's next action.

Then use `SourcePinnedExplanation` for same-ClaimGraph source explanation; `SourceLinkedExplanationReconstruction` for an already justified connective explanation; `DidacticRetelling` for bounded teaching use of the identified source or target; and `SpeculativeRetelling` only for a separately constituted hypothesis episteme. If the target identity or relation is missing, downgrade or stop rather than making the rendering sound more respectable through a class label.

Do not keep one narrower-use target with declared source-loss mode inside explanation merely because the prose is reader-friendly. When its narrower bounded claim or effect, blocked downstream use, and source-bearing return are primary, use `A.6.3.CSC Controlled Semantic Coarsening`; EFP may qualify a later publication form only if explanation use remains a separate live question.

#### E.17.EFP:4.3.b - Entailed connective and `addedLinkPolicy`

Harmless connective wording adds no proposition: conjunction markers, pronoun recovery, and sentence order can simply make an already explicit source statement readable. No `addedLinkPolicy` is needed for that case.

`SourceLinkedExplanationReconstruction` applies to a less obvious connective only when one of two bases is recoverable:

1. the exact source claims plus their effective reference scheme make the connective a consequence under a stated derivation; or
2. the exact source claims already report the relation occurrence, and that occurrence independently obtains under its defining pattern.

When that basis is material but not visible in the prose, a compact `addedLinkPolicy` points to it:

- `addedLinkKind` — the connective being exposed;
- `sourceReferenceSet` — the exact source claims used;
- `effectiveSchemeOrRuleRefs` — the designation, interpretation, ordering, or inference rules used by the derivation;
- `derivationOrRelationRef` — the inspectable derivation or the exact relation occurrence already reported by the source claims and independently shown to obtain;
- `claimContentResult = source-recoverable` — confirmation that the connective introduces no unsupported target claim;
- `reopenTrigger` — a source, scheme, rule, context, or relation change that invalidates the basis.

The policy is an index to the basis, not evidence that the basis exists. `boundednessReason`, a forbidden-link note, or author intent may help delimit use, but none substitutes for `derivationOrRelationRef`.

If neither a derivation from the exact source claims nor an exact source-reported relation occurrence that independently obtains can be recovered, the connective is another claim. Constitute its exact target episteme under C.2.1 and apply the direct relation, bridge, comparison, or B.5.2 hypothesis pattern that fits the new claim. If that result is unavailable, remove the connective or leave EFP; a downgrade label cannot make it source-linked.

#### E.17.EFP:4.4 - Working bounded-use matrix

| Class | Claim/source relation | Augmentation boundary | Usually bounded faces | Usually bounded publication-form use | Usually forbidden uses |
|---|---|---|---|---|---|
| `SourcePinnedExplanation` | form or representation of the source edition's same ClaimGraph | no claim-level augmentation | `PlainView`, `TechCard` | source inspection, navigation, or bounded restatement | an assurance, gate, evidence, or work claim not separately established |
| `SourceLinkedExplanationReconstruction` | same source ClaimGraph with a connective recovered by a stated derivation from source claims, or by an exact relation occurrence already reported there and independently shown to obtain | no new relation by class label | `PlainView`, `TechCard` | bounded explanation while the exact derivation or source-reported relation remains recoverable | use for which the source, scheme, derivation, source relation claim, or obtaining basis is unavailable |
| `DidacticRetelling` | form of the source when ClaimGraph is unchanged, otherwise form of an exact target connected under A.6.3 or another applicable pattern | pedagogy does not hide target identity or relation | `PlainView` | didactic or onboarding use | policy, assurance, gate, or source-replacement use |
| `SpeculativeRetelling` | form of a separately constituted B.5.2 hypothesis episteme | causal or counterfactual claim belongs to the hypothesis ClaimGraph | `PlainView` | clearly marked exploratory use | evidence, assurance, gate, release, or policy use |

This matrix assigns no evidence relation. An ordinary EFP result needs no A.10 path. Exact evidence, trace, pin, or provenance details open only when a named claim, dispute, derivative transformation, or receiving reliance consumes them and its applicable pattern or project record requires them.

`ExplanationFaithfulnessProfile` ordinarily stays on `publication face/form`. Any appearance on `interop publication form` remains source-pinned and structure-preserving, and does not smuggle explanation-specific semantics into interop publication. Didactic or speculative restrictions are use-profile restrictions over existing faces, not new face kinds.

Source-pinned explanation on `AssuranceLane`-facing publication is exceptional rather than ordinary. Unless the exact face or source policy permits that use with visible evidence carriers, source pins, and no added semantics, reviewers treat `AssuranceLane`-facing explanation rendering as blocked.

`DidacticRetelling` may carry analogy, scaffolding, or reader orientation without asserting a domain fact. Every domain claim it does express belongs either to the exact source ClaimGraph or to an identified target episteme with an obtaining source-to-target relation. Marking prose non-canonical or trace-free does not erase claim content, create its episteme, or establish that relation. When such analogy or scaffolding sits beside technical content, box or otherwise visibly separate it so readers do not merge it into the technical source; that cue limits likely use but does not establish episteme identity or a source relation.

The compact ordinary result needs only a source locator sufficient to reopen the exact source or target decision. Publish exact claim IDs, pins, trace paths, provenance details, or an A.10 evidence relation only when a named claim, dispute, derivative transformation, or receiving reliance consumes them. A reopenable locator is not automatically an evidence path.

When a reader-fit difference changes the bounded or blocked use, state only the relevant audience, interaction, question, use, or overread distinction. Do not publish or inherit all five reader-model fields for ordinary reader help.

#### E.17.EFP:4.5 - Shared explanation rule set

##### E.17.EFP:4.5.a. Preservation rule
Every published explanation form under this profile expresses one exact episteme edition. It stays a form or representation of the source edition only while it expresses the same ClaimGraph under the same C.2.1 identity; otherwise it expresses an exact target episteme connected by an obtaining source-to-target relation. E.24.PUB publication occurrence remains separate, and the EFP class changes neither identity nor relation.

##### E.17.EFP:4.5.b. Loss and reliability rule
A published form states material omission, reordering, simplification, or connection. When any such move changes claim content, the loss belongs to the exact target episteme and its obtaining source-to-target relation under A.6.3 or another applicable pattern, not to an EFP label. Reliability is never silently widened by more persuasive prose.

When a concrete reader-fit difference is load-bearing, expose only enough of its bounded use or overread risk to prevent the actual didactic or contrastive form from being mistaken for assurance, policy, or gate guidance.

##### E.17.EFP:4.5.c. Downstream-use and boundary rule
This profile stays explanation-facing and episteme-facing. It does not decide bridge stance, retargeting, action selection, executable docking, gate-bearing claims or effects, assurance, engineering justification, or work enactment. If a case starts carrying one bounded comparative review case, rival interpretations, bridge-mediated comparison load, world consequences, work or reliance consequences, gate consequences, assurance, or engineering justification, apply the neighboring FPF pattern, then name the project-side object or record that carries the claim or effect and its FPF kind (`E.17.ID.CR`, `F.9.1`, `B.5.2`, `A.6.4`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`).

Interpretant-side fields do not weaken that boundary rule. They only bound reader use; they do not authorize unsupported downstream guidance.

If a coarsened explanation-like rendering needs a narrower bounded claim or effect, blocked downstream use, and source-bearing reopen to remain honest, apply `A.6.3.CSC Controlled Semantic Coarsening` rather than keeping the case in ordinary explanation-use discipline.

##### E.17.EFP:4.5.d. Composition and reopen rule
Repeated `SourcePinnedExplanation` over forms of the same exact source edition can be idempotent. Any changed ClaimGraph reopens C.2.1 identity and the source-to-target relation before class review. Didactic target forms reopen when their target edition, relation, or use changes; speculative forms reopen when their B.5.2 hypothesis edition, prompt relation, or exploratory use changes.

#### E.17.EFP:4.6 - Hard boundary rules

A rendering reviewed under this profile keeps the following explicit:
- it does **not** create a second face family;
- it does **not** turn faces into a second semantic rule track;
- it does **not** license new A.6.B boundary claims on explanation faces: law claims, use-boundary claims, deontic or commitment claims, and effect or evidence claims;
- it does **not** replace bridge discipline, retargeting discipline, or world or gate boundary discipline;
- it does **not** let `publication face/form` and `interop publication form` collapse into one undifferentiated explanation channel.

If explanation text carries a changed ClaimGraph, stop class review, identify the exact target episteme and make the direct source-to-target relation obtain. Resume EFP only for a publication form of that target when bounded explanation use remains separately material.

