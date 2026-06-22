---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:4"
section_title: "Solution — review profile for explanation renderings on existing MVPK faces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__005_solution-review-profile-for-explanation-renderings-on-existing-mvpk-faces.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:4 — Solution — review profile for explanation renderings on existing MVPK faces"
line_start: 68835
line_end: 69068
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CSC"
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

> `ExplanationFaithfulnessProfile` is a review profile governed by `E.17.0` and `E.17` for explanation-facing renderings over already available claims, traces, and pins on existing MVPK faces.
>
> It does not create a new face family. It states how an explanation relates to its source `U.Episteme` or source `U.EpistemePublication`, what kind of augmentation is bounded, which evidence binding remains source-bounded, and which existing faces can carry the rendering.

#### E.17.EFP:4.1.a - Profile, case, and published rendering distinction

`ExplanationFaithfulnessProfile` is a **review profile** governed by `E.17.0` and `E.17`. Concrete explanation-facing renderings are passive published renderings or reviewed cases classified under this profile; the profile itself does not act, decide, or publish.

This distinction matters because the profile governs **how** a rendering is related to its source and reviewed. It does not turn every explanatory paragraph into a giant standalone record, and it does not replace MVPK face governance with a second semantic track.

#### E.17.EFP:4.1.b - How to read this profile

This profile does not decide whether a claim is true. It says how an explanation rendering relates to already available source `U.Episteme` or source `U.EpistemePublication`, source pins, traces, and provenance references, and which bounded use that rendering carries.
- `Faithfulness` names the review question for the rendering, not a pass verdict for every class.
- Class names are source-relation and bounded-use labels, not merit labels or proof that all classes are faithful in the same sense.
- Faces stay governed by `E.17`; the profile only constrains what sort of explanation is bounded on them.
- If a rendering begins to add new semantic commitments, it has left this profile even if the prose still looks explanatory.
- It helps a publication-side reviewer state one published rendering's relation to the already pinned source `U.Episteme` or source `U.EpistemePublication`.

#### E.17.EFP:4.1.c - Local working vocabulary

This profile uses a small local vocabulary for review.
- **Source `U.Episteme` or source `U.EpistemePublication`** = the already pinned source `U.Episteme` or source `U.EpistemePublication`, source claims, traces, notes, pins, or provenance references that the explanation rendering depends on. This is not the MVPK face, not the SCR/RSCR carrier, and not an arbitrary carrier or physical item.
- **Rendering** = one published explanation-facing text on one existing face.
- **Class assignment** = the explanation-class assigned to that rendering on that face.
- **Bundle-local class difference** = a case where two renderings in one bundle carry under bounded use different explanation classes.

These are review aids, not new governance kinds. Faces remain governed by `E.17`; this profile only qualifies explanation behaviour on those faces.

#### E.17.EFP:4.2 - Core profile fields

Most renderings reviewed under this profile need only the compact review note:

| Core field | Question |
| --- | --- |
| `explanationClass` | Which local profile value is assigned to this one rendering? |
| source reference | Which already available source `U.Episteme` or source `U.EpistemePublication`, pins, trace, or provenance reference does the rendering depend on? |
| bounded explanation-reader use | What can the explanation reader do with this explanation now: understand, navigate, inspect, teach, or prepare review? |
| blocked downstream use | What wider claim or effect is not carried by the explanation? |
| reopen or boundary condition | What source change, dispute, use escalation, missing source relation, or neighboring-pattern boundary condition ends this profile use? |

The fuller field vocabulary below opens only when ambiguity or load-bearing use is present: different classes across faces, source linkage dispute, connective reconstruction, reader-fit dispute, interaction or statefulness, derivative rendering, cross-context reuse, cited reliance, work or reliance, evidence, gate, engineering justification, bridge, or coarsening boundary.

- `profilePlacementRef = profile governed by E.17 and E.17.0`;
- `governingPatternRef = E.17 and E.17.0`;
- `sourcePublicationOrRecordForm`;
- `targetPublicationOrRecordForm`;
- `changeTargetRef`;
- `entityOfConcernPolicy = preserve` for explanation renderings over the same underlying source `U.Episteme` or source `U.EpistemePublication`;
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
- `upstreamGoverningPatternRef?`, `upstreamAuthoritySourceRef?`, `downstreamGoverningPatternRef?`, and `downstreamAuthoritySourceRef?`;
- `boundedFaces`;
- `publication-face kind value` when `publication face/form` or `interop publication form` discipline is present;
- `publicNamePolicy`;
- `explanationSourceRelationClass` using the shared `E.17:5.1b` vocabulary when source pointer, source availability or retrieval, source use, source faithfulness, claim-source relation, contradiction, omission, claim widening, added linkage, independent verification, bounded use, forbidden downstream use, or reopen trigger could diverge;
- no generic source-relation field; source relation is recorded through `explanationSourceRelationClass`;
- `augmentationRelation`;
- `addedLinkPolicy` when `SourceLinkedExplanationReconstruction` adds bounded connective prose;
- `targetUserModel?` when reader-fit materially shapes the rendering;
- `interactionMode?` when the explanation is more than one static explanatory paragraph;
- `contrastiveQuestion?` when the rendering is answering a specific user-facing contrast or why-question;
- `boundedReaderUse?` when downstream use is bounded by intended reader and task;
- `overreadRisk?` when overinterpretation pressure is part of the review load;
- `evidenceRelation`;
- `noNewBoundaryClaims = true` on explanation faces;
- `compositionRule`;
- `reopenCondition`.

These fields inherit the `E.17:5.1e` local-field rule. They classify one explanation-facing rendering for review; they do not create `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, authority reference, publication face, or project-side FPF kind and reference named by value unless another governing FPF pattern explicitly instantiates that object. The `explanationClass` value is a local source-relation and bounded-use profile value, not `ExplanationKind`, not `U.Kind`, not `EvidenceKind`, not `FaceKind`, and not a truth certificate.

Where explanation crosses from source rendering into new claim production, hidden bridge work, gate-bearing semantics, world-changing claim or effect, or a source relation with declared source-loss mode, the profile no longer suffices and the case leaves this profile.

#### E.17.EFP:4.2.a - Working-model first

Ordinary reviewed renderings do not need to restate every field from scratch. When the governing MVPK face, pinned source `U.Episteme` or source `U.EpistemePublication`, and already published provenance references already fix a field honestly, the rendering can inherit that condition by explicit reference.

A source-bearing review record becomes necessary when:
- explanation class differs across faces in the same publication bundle;
- the rendering relies on bounded connective prose that is not obvious from the source wording alone;
- didactic or speculative wording creates a real risk of policy, assurance, or gate misuse;
- source linkage, provenance, or reliability transport would otherwise become unclear;
- the rendering is a fork, adaptation, translation, generated explanation, tutorial, access-format conversion, or another derivative publication that can be mistaken for the source itself.

When one rendering needs its own narrower bounded claim or effect line, blocked downstream claim or effect line, or source-bearing reopen rule because distinctions were deliberately coarsened for reader fit, the issue is no longer only explanation class. Do not keep that case here as if it were merely one more helpful rendering style; apply `A.6.3.CSC Controlled Semantic Coarsening`.

#### E.17.EFP:4.2.b - What a publication-side reviewer checks first

A publication-side reviewer usually starts with four questions:
1. What exactly is the source `U.Episteme` or source `U.EpistemePublication` for this rendering?
2. Which explanation class is being claimed for this rendering on this face?
3. Are the pins, provenance references, and evidence relation visible enough for that class?
4. Has the rendering quietly begun to add new semantic commitments, new face-like behaviour, derivative-source replacement, or a deliberately coarsened source rendering that needs `A.6.3.CSC`?

If these questions are answered clearly, the rendering often remains lightweight. If they are not, a fuller face-by-face review record is usually warranted.

#### E.17.EFP:4.2.c - Interpretant-side block

This profile still governs explanation renderings on existing faces, not full interactive explanation systems.

However, when reader-help, onboarding, or contrastive explanation is doing real work, the rendering also makes visible:
- who the rendering is fit for (`targetUserModel`);
- whether the interaction is static, guided, contrastive, or another bounded mode (`interactionMode`);
- what question the rendering is helping answer (`contrastiveQuestion`);
- what interpretation or use remains bounded (`boundedReaderUse`);
- and what downstream claim or effect would be wrongful (`overreadRisk`).

These fields do not create a new governing source relation. Their current role is narrower: stop explanation prose from pretending that every rendering is audience-neutral, and make misuse boundaries explicit when reader-fit is part of the explanation case. `boundedReaderUse` is a local reader-fit field under `boundedUse`; it is not permission, evidence relation, or authority.

#### E.17.EFP:4.3 - Explanation class set

The explanation-class set used in this profile is:
- `SourcePinnedExplanation`
- `SourceLinkedExplanationReconstruction`
- `DidacticRetelling`
- `SpeculativeRetelling`

In field form, the local assignment is `explanationClass = SourcePinnedExplanation | SourceLinkedExplanationReconstruction | DidacticRetelling | SpeculativeRetelling`.

Class assignment is a source-relation and bounded-use classification. `SourcePinnedExplanation` is source-bound rendering, `SourceLinkedExplanationReconstruction` is bounded reconstruction with explicit added-link policy, `DidacticRetelling` is teaching and onboarding help, and `SpeculativeRetelling` is exploratory help. The last two classes do not assert the same kind of source faithfulness as `SourcePinnedExplanation`; they state the limits under which reader help remains bounded.

Safe next action by class:

| Class | Safe next action |
| --- | --- |
| `SourcePinnedExplanation` | source inspection, bounded restatement, and source navigation. |
| `SourceLinkedExplanationReconstruction` | bounded explanation with explicit `addedLinkPolicy`. |
| `DidacticRetelling` | onboarding or teaching only; return to source for reliance. |
| `SpeculativeRetelling` | exploratory discussion only; no evidence, work, gate, assurance, or release reliance. |

These classes are publication-behaviour labels for one rendering on one existing face. They are not `U.Kind` values, not MVPK faces, and not semantic merit grades. They state how the explanation relates to the source, how much augmentation is tolerated, what reliability transport is still honest, and which faces remain bounded-use.

Class assignment is per published rendering on a face, not one blanket label for a whole multi-face bundle. If a `PlainView` rendering stays source-pinned while a `TechCard` rendering adds bounded connective prose, the bundle needs an explicit class difference.

#### E.17.EFP:4.3.a - Ordinary class-selection guidance

A practical classification order is:
- start with `SourcePinnedExplanation` if the rendering stays close to the source wording and keeps direct pins visible;
- choose `SourceLinkedExplanationReconstruction` when bounded connective prose is added but source linkage remains explicit;
- choose `DidacticRetelling` when reader-help dominates and some phrasing is intentionally more pedagogical than canonical;
- choose `SpeculativeRetelling` only when the rendering openly goes beyond source-backed explanation and remains confined to exploratory or didactic use.

The profile is not used to make a rendering sound more respectable than its actual source relation warrants.

Do not keep one narrower-use rendering with declared source-loss mode inside explanation just because the prose is reader-friendly. If the rendering needs its own forbidden-use line and reopen rule to stay honest, explanation is no longer the primary question; use `A.6.3.CSC Controlled Semantic Coarsening`.

#### E.17.EFP:4.3.b - `SourceLinkedExplanationReconstruction` added-link policy

When a rendering claims `SourceLinkedExplanationReconstruction`, publish a compact `addedLinkPolicy` whenever the connective move is not already explicit in the source wording.

Minimum source-link load:
- `addedLinkKind` — what bounded connective move is being added;
- `sourceReferenceSet` — which pinned claims, traces, or notes carry that move;
- `boundednessReason` — why the added link does not become an unsupported relation theory, modality lift, causal claim, bridge-comparison load, or policy-bearing interpretation;
- `forbiddenLinkClass` — which unsupported connective move is explicitly excluded;
- `reopenTrigger` — what would force downgrade, source-bearing return, or source-bearing review.

Working rule:
- if `addedLinkPolicy` cannot be stated plainly, the rendering drops to a more restricted explanation class, uses a more restricted MVPK face or named `publication-face kind` value, or leaves `E.17.EFP`;
- `SourceLinkedExplanationReconstruction` does not hide new relation theory, bridge equivalence, design-scope generalization, or policy-bearing guidance inside "bounded" connective prose.

#### E.17.EFP:4.4 - Working bounded-use matrix

| Class | Source relation | Augmentation relation | Evidence relation | Usually bounded faces | Usually bounded `publication face/form` or `interop publication form` use | Usually forbidden uses |
|---|---|---|---|---|---|---|
| `SourcePinnedExplanation` | rendering | omission-only | trace-bound | `PlainView`, `TechCard` | `publication face/form`; `interop publication form` only when the governing face source explicitly permits source-pinned, structure-preserving export without added semantics | `AssuranceLane` or gate-bearing claim or effect if required pins or evidence are absent |
| `SourceLinkedExplanationReconstruction` | reconstruction | bounded link-addition | trace-backed | `PlainView`, `TechCard` | `publication face/form` on bounded explanatory use | `InteropCard` or `AssuranceLane` unless governing face policy explicitly allows it with source linkage kept visible |
| `DidacticRetelling` | reconstruction | omission + didactic addition | trace-backed for domain facts; trace-free only for analogy, scaffolding, or reader orientation | `PlainView` | `publication face/form` on didactic or onboarding use only | `TechCard`, `InteropCard`, `AssuranceLane`, or policy-bearing use when it could be mistaken for canonical semantics |
| `SpeculativeRetelling` | speculation | link-addition or counterfactual augmentation | trace-free or low trace backing | `PlainView` | `publication face/form` on clearly marked exploratory or didactic use only | `TechCard`, `InteropCard`, `AssuranceLane`, gate-adjacent, or policy-bearing use |

`ExplanationFaithfulnessProfile` ordinarily stays on `publication face/form`. Any appearance on `interop publication form` remains source-pinned and structure-preserving, and does not smuggle explanation-specific semantics into interop publication. Didactic or speculative restrictions are use-profile restrictions over existing faces, not new face kinds.

Source-pinned explanation on `AssuranceLane`-facing publication is exceptional rather than ordinary. Unless the governing face source explicitly permits that use with visible evidence carriers, source pins, and no added semantics, reviewers treat `AssuranceLane`-facing explanation rendering as blocked.

`DidacticRetelling` and trace-free reader help are illustrative or analogical scaffolding only. Trace-free didactic material can carry analogy, scaffolding, or reader orientation, but any domain fact inside didactic prose needs either to be source-pinned or explicitly downgraded to non-canonical reader aid. It does not carry causal claims, policy claims, reliability claims, or canonical `TechCard` semantics. If didactic content appears near technical content, mark it as a boxed or otherwise clearly separated non-canonical reader aid rather than letting it merge into the technical source.

Every concrete explanation rendering also publishes the source claim IDs, pins, trace refs, or equivalent provenance references that justify its class on that face. If those anchors cannot be made visible on the chosen MVPK face or named `publication-face kind` value, the rendering drops to a more restricted explanation class, uses a more restricted use profile, or leaves the face.

When reader-help, onboarding, or contrastive explanation is part of the case, the rendering also publishes or inherits its `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedReaderUse`, and `overreadRisk` so that user-fit does not quietly become policy guidance, assurance guidance, or gate-bearing guidance.

#### E.17.EFP:4.5 - Shared explanation rule set

##### E.17.EFP:4.5.a. Preservation rule
Explanation-facing renderings under this profile preserve the same underlying EntityOfConcern line, bounded context, and source-pinned `U.Episteme` or source `U.EpistemePublication`. Viewpoint, reference scheme, representation scheme, grounding, and reference-plane handling stay explicit rather than being left to prose. `SourcePinnedExplanation` and `SourceLinkedExplanationReconstruction` are expected to remain claim-conservative; `DidacticRetelling` can omit or simplify source claims but stays source-linked; `SpeculativeRetelling` can widen explanatory language only when kept clearly off canonical faces and off gate-bearing claim or effect.

##### E.17.EFP:4.5.b. Loss and reliability rule
A rendering assigned to one of these explanation classes declares what is omitted, reordered, simplified, or newly connected. Reliability transport can stay source-bounded or be explicitly downgraded, but it is never silently widened by more persuasive prose. Didactic and speculative renderings also state forbidden downstream uses whenever omissions, declared source-loss modes, or trace-free additions occur.

When reader-fit is part of the explanation case, `boundedReaderUse` and `overreadRisk` are explicit enough that a didactic or contrastive rendering cannot be mistaken for assurance, policy, or gate-bearing guidance.

##### E.17.EFP:4.5.c. Downstream-use and boundary rule
This profile stays explanation-facing and episteme-facing. It does not govern bridge stance, retargeting, action selection, executable docking, gate-bearing claim or effect, assurance, engineering justification, or work enactment. If a case starts carrying one bounded comparative review case, rival interpretations, bridge-mediated comparison load, world consequences, work or reliance consequences, gate consequences, assurance, or engineering justification, apply the neighboring FPF pattern and name the project-side FPF kind and reference named by value that governs that claim or effect (`E.17.ID.CR`, `F.9.1`, `B.5.2`, `A.6.4`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`).

Interpretant-side fields do not weaken that boundary rule. They only bound reader use; they do not authorize unsupported downstream guidance.

If a coarsened explanation-like rendering needs narrower bounded claim or effect, blocked downstream claim or effect, and source-bearing reopen to remain honest, the case is governed by `A.6.3.CSC Controlled Semantic Coarsening` rather than staying in ordinary explanation-use discipline.

##### E.17.EFP:4.5.d. Composition and reopen rule
Repeated `SourcePinnedExplanation` over the same pinned source can be idempotent. `SourceLinkedExplanationReconstruction` and `DidacticRetelling` are order-sensitive and reopens when the source claim set, pins, provenance, or face-use assumptions change. `SpeculativeRetelling` reopens whenever source binding becomes available or whenever the rendering starts to look like a canonical explanation rather than a clearly bounded exploratory retelling.

#### E.17.EFP:4.6 - Hard boundary rules

A rendering reviewed under this profile keeps the following explicit:
- it does **not** create a second face family;
- it does **not** turn faces into a second semantic rule track;
- it does **not** license new A.6.B boundary claims on explanation faces: law claims, use-boundary claims, deontic or commitment claims, and effect or evidence claims;
- it does **not** replace bridge discipline, retargeting discipline, or world or gate boundary discipline;
- it does **not** let `publication face/form` and `interop publication form` collapse into one undifferentiated explanation channel.

If explanation text starts carrying new semantic commitments instead of rendering or licensed explanation over existing ones, the case leaves this profile.

