---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:4"
section_title: "Solution — preserve practical content across a representation change"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__005_solution-preserve-practical-content-across-a-representation-change.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:4 — Solution — preserve practical content across a representation change"
line_start: 14937
line_end: 15121
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.NAR"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "C.29"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
keywords:
---

### A.6.3.RT:4 - Solution — preserve practical content across a representation change

#### A.6.3.RT:4.1 - Ordinary representation move

Produce the useful target first:

1. Name the user action the new representation should help: compare, inspect, traverse, calculate, communicate, or replay.
2. Point to the source material and name the claims, relations, commitments, uncertainty, or source pins that must survive.
3. Choose the target representation and say why it is better suited to that action.
4. Produce the smallest target that supports the action.
5. Compare target and source. Mark what is preserved and foregrounded; what is rearranged, omitted, or harder to recover; and which visible links or interpretations were added by the representation.
6. State the representation and reasoning-medium delta only as far as it changes use or blocks a likely overread.
7. Close with admissible use, non-admissible use, and a concrete return trigger and destination.

Use this compact note for ordinary work:

| Representation note entry | Practical question |
| --- | --- |
| User action | What should the target make easier? |
| Source material | What will the user return to? |
| Content to survive | Which claims, relations, commitments, uncertainty, or pins matter? |
| Target and reason | Which representation is chosen, and why does it help? |
| Preserved/foregrounded | What remains recoverable, and what becomes easier to see? |
| Rearranged/lost/added | What is omitted or weakened, and which apparent relation is not source-given? |
| Use boundary | What may and may not be done with the target? |
| Return | Which condition sends the user back to the source or to a stronger claim's direct pattern? |

#### A.6.3.RT:4.1.a - Exact episteme-construction branch

Open this branch only when the receiving use makes exact claim identity material: the target must travel independently, be cited or disputed, cross a scheme boundary for consequential use, be considered for admission as receiving episteme `Y` in a generated or decode-mediated case, or meet an exact-identity requirement from a named public, evidence, or assurance receiver.

Then establish exact A.6.3 construction `v : X -> Y`:

1. identify source episteme `X` and receiving episteme `Y` independently under C.2.1 by claim content, exact EntityOfConcern, and effective `U.ReferenceScheme`;
2. require the same exact EntityOfConcern; a changed concern requires A.6.4;
3. state how claims in `X` and any named additional source epistemes construct the claims in `Y`;
4. state the relation between endpoint schemes, preserved and foregrounded content, admitted loss or recoverability, prohibited strengthening, applicability, use, and return; and
5. cite every exact correspondence relation on which `v` actually depends. Scheme difference, similar content, adjacency, or a visible edge proves none.

A source model, graph, publication occurrence, form, carrier, table, or display does not substitute for `X`; a target table, diagram, notation, page, or file does not substitute for `Y`. If the target has no recoverable claim content, exact EntityOfConcern, or effective reference scheme, keep it as a useful rendering or candidate carrier and do not assert exact RT yet.

An exact `v` performs no Work and is not a relation occurrence. A system may perform representation-transformation Work under A.15.1; methods, source-use relations, A.6.1 bindings, and any A.15.PROD inception claim remain separate. E.17.0 independently decides viewpoint conformance and dependent `U.View` membership. E.24.PUB independently identifies publication occurrence, form, carrier, audience, and bounded use. Completing the exact construction does not itself authorize reliance.

#### A.6.3.RT:4.1.b - Later-specific six-participant occurrence

Use `RepresentationSchemeTransitionRelation@Context` only when the actual transition occurrence is itself needed and all six exact participants plus actual Work are present. The suffix `@Context` retrieves one independently selected A.1.1 `BoundedModelUseStructure : U.Structure`; it introduces no generic context kind or description-context field.

```text
RepresentationSchemeTransitionRelation@Context <: U.Relation:
  TransitionModelUseStructureSlot = <TransitionModelUseStructureSlot, U.Structure, U.StructureRef constrained to one exact BoundedModelUseStructure>
  PreservedEntityOfConcernSlot = <PreservedEntityOfConcernSlot, U.Entity, U.EntityRef>
  SourceRepresentationEpistemeSlot = <SourceRepresentationEpistemeSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationEpistemeSlot = <ReceivingRepresentationEpistemeSlot, U.Episteme, U.EpistemeRef>
  SourceRepresentationSchemeDescriptionSlot = <SourceRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationSchemeDescriptionSlot = <ReceivingRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  direction = SourceRepresentationEpistemeSlot -> ReceivingRepresentationEpistemeSlot
```

The six SlotSpecs and direction are the exact `RelationSignature`. `X` and `Y` have the same exact EntityOfConcern and their own effective schemes. Each scheme-description episteme is independently constituted: its claims describe one exact endpoint scheme, its EntityOfConcern is that scheme, and its own effective reference scheme makes the description interpretable. A scheme label or visible notation fills no scheme-description slot.

A positive occurrence obtains only when all of the following hold together:

1. all six participants resolve exactly, and the `BoundedModelUseStructure` was independently selected because its model-use organization changes this transition use;
2. A.13 identifies the actual performer, and A.15.1 independently admits the dated representation-transformation Work. If the current use also needs to say exactly which assignment covered that Work, F.6 checks that separate relation against the same A.13 assignment; F.6 identifies neither performer nor assignment, and a missing or failed attribution leaves the Work intact. The Work uses all six participant values collectively through its governed inputs, result, references, A.6.1 bindings, or a combination of these;
3. exact `v : X -> Y` states claim construction, endpoint-scheme relation, same EntityOfConcern, preservation, loss or recoverability, prohibited strengthening, applicability, use, and return; and
4. every depended-on correspondence is an exact separately governed relation or claim.

Work, performer, assignment, method, operation application, source-use relations, and any inception claim are not seventh participants or identity discriminators. Work alone proves neither `v` nor the occurrence. Conversely, an inspectable `v` without the selected model-use structure and exact Work remains an ordinary exact construction.

The occurrence is participant-determined by the complete six-participant tuple. Changing any participant identifies another occurrence. A repeat Work episode, evidence change, publication, form, carrier, layout, transition-description edition, or C.29 output does not reidentify an unchanged tuple. A changed C.2.1 discriminator of `X` or `Y` first identifies another episteme and therefore another tuple.

#### A.6.3.RT:4.1.c - Transition description and source-relation epistemes

Describe the occurrence durably only after it obtains and a receiving use needs that description. The transition-description episteme is identified under C.2.1 by claim content about the exact six-participant occurrence, that occurrence as EntityOfConcern, and its own effective `U.ReferenceScheme`. Editing its claim graph creates another description episteme without changing the occurrence.

Its claim content may make these values recoverable; they are not extra participants or identity fields:

| Description content | Meaning |
| --- | --- |
| `transitionRelationRef` | The exact six-participant occurrence. |
| `viewingConstructionRefOrStatement` | Exact `v : X -> Y`, including claim construction, endpoint-scheme relation, same exact EntityOfConcern, preservation, loss/recoverability, prohibited strengthening, applicability, use, and return. |
| `representationTransformationWorkRef` | Exact A.15.1 Work already used in the obtaining test; actual performer, assignment, Method, A.6.1 bindings, and any A.15.PROD inception claim remain separate. |
| `sourceRelationReferenceEpistemeRefs[]` | C.2.1 epistemes about exact source relations actually used; each relation still needs its own obtaining basis. |
| `preservedClaimRefs[]` | Exact source claims carried into `Y` for this use. |
| `preservedCommitmentRefs[]?` | Exact commitments preserved when a commitment is current. |
| `representationSchemeDeltaDescriptionRef` | What differs between the participating source- and receiving-scheme descriptions. |
| `reasoningMediumDeltaDescriptionRef?` | Changed inspection, comparison, inference, or replay affordance when material. |
| `representationLossDescriptionRef?` | Lost, narrowed, foregrounded, or rearranged distinctions. |
| `recoverabilityDescriptionRef?` | How omitted content is recovered from exact `X` or source relations. |
| `admissibleUseDescriptionRef` | What `Y` supports now. |
| `nonAdmissibleDownstreamUseDescriptionRef` | Which stronger use has not been established. |
| `returnConditionDescriptionRef` | When the user returns to exact `X` or its source relations. |

At least one of loss and recoverability is explicit; both are explicit when distinctions are lost and a recovery route is claimed.

When `v` cites a claim about one exact source relation, identify any reference-bearing episteme independently by its own C.2.1 triple: claims designating that relation and stating its exact kind, signature, defining pattern, and use in `v`; the source relation as EntityOfConcern; and its effective scheme. The episteme is not the relation, and citation does not make the relation obtain.

Publication may expose `X`, `Y`, the occurrence, or its description; forms, carriers, C.29 representations, and publication occurrences substitute for none of them.

#### A.6.3.RT:4.2 - Progressive use and local vocabulary

Use three levels, without copying one level's burden into another:

- **Ordinary target:** target representation plus compact note.
- **Exact construction:** add `X`, `Y`, `v`, endpoint schemes, exact source dependencies, and claim-level loss/return when the receiving use triggers them.
- **Actual transition occurrence:** add the six-participant relation, Work, and optional occurrence-description episteme only when that historical relation is itself material.

Use detailed vocabulary only when it changes the next representation decision or blocks a concrete overclaim:

- **semiotic mode** — the meaning-bearing relation doing the main work, such as structural likeness, trace, conventional code, model-mediated correspondence, or decode-mediated recovery;
- **factor delta** — the representation-factor change material to review;
- **source-relation chain** — the exact source claims and relations on which an exact `v` depends, or the ordinary source trail to which a user returns;
- **decode-mediated case** — a case whose receiving interpretation depends on a declared decoding or access relation;
- **actionability shift** — an apparent change in what users think they can do, which is not work authority, gate status, or permission; and
- **recoverability evidence** — evidence that omitted content can be recovered well enough for the declared use.

State the actual use, loss, evidence, and return once. Use A.10 or B.3 only when a specific evidence or assurance claim is current.

#### A.6.3.RT:4.3 - Direct and correspondence-mediated constructions

In a **direct** exact construction, `Y` is constructed from `X` and fixed declared configuration. State the claim construction, endpoint-scheme relation, same exact EntityOfConcern, preservation, loss/recoverability, prohibited strengthening, applicability, use, and return; no generic correspondence object is required.

In a **correspondence-mediated** exact construction, `Y` depends on additional source epistemes or governed relations among their claim-bearing contents. Recover each needed direct relation and, when `v` cites a claim about it, the exact C.2.1 assertion episteme. A correspondence table, model, graph edge, or scheme difference is neither the relation nor proof that it obtains.

Both profiles retain the same exact EntityOfConcern. A correspondence by itself establishes neither an F.9 Bridge nor any substitution, comparative-review, evidence, or publication claim. Add C.29 only for a current mathematical modeling or reasoning use.

#### A.6.3.RT:4.4 - Recurring moves and useful deltas

Recurring move shapes include tabulation, diagramming, structured-notation shift, and a same-EntityOfConcern correspondence-mediated representation shift. They are not separate Core patterns.

In ordinary language, say what changed and why it helps: “the table foregrounds row comparison”, “the diagram foregrounds dependency shape”, or “the notation foregrounds explicit argument positions”. Add salience, topology, actionability, calibration, interactivity, or semiotic-mode detail only when it materially changes use or misuse risk.

#### A.6.3.RT:4.5 - Preservation, loss, decode, and chains

##### A.6.3.RT:4.5.a - Preservation and conservativity

The ordinary move preserves the practical content named for the use. The exact branch preserves the same exact EntityOfConcern across independently constituted `X` and `Y` while changing scheme and often reasoning medium.

A target introduces a new concern-side claim when it:

- upgrades a source-visible relation into dependency theory or another relation not present in the source;
- turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
- adds a Bridge, substitution, comparative, mechanism, temporal, or control claim that the source does not state and that has not been independently established under its governing pattern;
- collapses source alternatives, uncertainty, or bounded scope into one wider commitment; or
- treats decode-mediated recovery as direct givenness.

Check each target-side connective against the source or exact same-EntityOfConcern correspondence. A clearer, more structured, or more formal target does not establish a broader reliability claim.

##### A.6.3.RT:4.5.b - Loss and recoverability

State which distinctions, inspection possibilities, uncertainty cues, or local qualifiers are lost, foregrounded, rearranged, or harder to recover. The target may remain useful under a reliability claim bounded by the source or with an explicitly narrowed admissible use. If it remains honest only through a declared narrower use and source return, A.6.3.CSC is primary.

##### A.6.3.RT:4.5.c - Decode-mediated entry

A latent or decode-mediated case stays bounded until it has source material for the same concern, a decoding or access relation, recoverability evidence for the intended use, admissible and non-admissible use, remaining user action, and source return. When exact reliance is claimed, source material includes exact `X`, exact `Y`, `v`, and the exact source-relation chain.

A latent region, activation pattern, embedding, probe result, decoded rendering, publication form, or carrier may help locate the case but fills no episteme endpoint. Missing recovery evidence keeps the result exploratory, report-only, or blocked.

##### A.6.3.RT:4.5.d - Composition and reopen rule

Repeated same-regime normalization may be idempotent; heterogeneous representation shifts are generally order-sensitive. Check a chain pairwise and carry accumulated loss instead of pretending each step resets it. Keep the source and target, content under test, scheme delta, preserved and withdrawn commitments, loss/recovery, and remaining action recoverable at every step.

Reopen the affected account when source content, endpoint identity, recovery assumptions, pins or provenance, correspondence or counter-witness disposition, primary semiotic mode, intended publication or receiving use, or accumulated loss changes. A changed EntityOfConcern requires A.6.4; a changed target-side claim uses the pattern that defines that exact claim.

#### A.6.3.RT:4.6 - Boundary triggers

| What became primary | Required move |
| --- | --- |
| Same-regime wording only | Use A.6.3.CR. |
| Reader-useful ordering into a narrative path | Use A.6.3.NAR; keep RT only for a remaining material scheme shift. |
| Explanation adequacy of an existing face | Use E.17.EFP. |
| Receiving episteme has an independently identified different exact EntityOfConcern | Use A.6.4 for the retargeting arrow, its separate C.2.1 bounded-use assertion, and the current-case judgement `satisfies`, `fails`, or `cannot decide`. |
| Changed kind, ontology frame, predicate set, mathematical domain, or notation without an established EntityOfConcern change | Repeat the C.2.1 identity test and use the exact ontology pattern for any changed claim. Stay in RT when the same EntityOfConcern remains current and representation is the primary change. |
| Same-signal time/frequency or another mathematical representation change | Stay in RT when the same EntityOfConcern remains current and representation is the primary change. Add C.29 only when the use depends on a contested or claim-bearing mathematical lens. A.6.4 opens only after C.2.1 independently identifies a different receiving entity. |
| Carrier rendering, export, serialization, OCR, or parsing before a receiving episteme exists | Use A.7 or the corresponding carrier/extraction pattern. |
| A narrower-use coarsened receiving episteme | Use A.6.3.CSC with explicit loss and source return. |
| Cross-context equivalence, substitution, or Bridge use | Keep RT for the representation delta. Use F.9 to test a Bridge between two exact F.17 `SchemeSenseCell` values from different semantic contexts; cite the Bridge only if it obtains, and keep any C.2.1 bounded-use claim separate. |
| Bounded comparison over already available source epistemes | Use E.17.ID.CR; keep RT only for a remaining material representation change. |
| Problem formulation or abductive prompt, candidate, or selection | Use B.5.2.0 for the prompt and B.5.2 for the abductive loop. |
| Performed Work, a work plan, or authority to act | Use the applicable A.15 pattern for performed Work or a work plan; an RT note or construction supplies neither and grants no authority to act. |
| Evidence or assurance force | Keep RT for preservation/loss and use A.10 or B.3 for that exact claim. |
| Temporal or dynamics claim | Use C.27 or A.3.3 for the claim actually made. |
| Transformation-flow graph/path, step-validity, or gate-decision claim | Use E.18, A.20, or A.21 respectively. |
| A contested mathematical lens | Keep RT for the representation transition and use C.29 only for adequacy of that lens. |

