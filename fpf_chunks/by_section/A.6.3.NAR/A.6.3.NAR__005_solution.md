---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__005_solution.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:4 — Solution"
line_start: 14921
line_end: 15078
dependencies:
  - "A.16.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.11"
  - "E.17"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.6"
  - "G.11"
  - "G.2"
keywords:
---

### A.6.3.NAR:4 - Solution

First establish exact A.6.3 construction `n : X -> Y`:

1. identify exact source episteme `X` and receiving narrative episteme `Y` independently by claim content, EntityOfConcern, and effective `U.ReferenceScheme`;
2. require the same exact EntityOfConcern; changed concern exits to A.6.4;
3. state how exact claims in `X` and any named additional source epistemes construct the sequential claim content of `Y`;
4. state how the endpoint effective schemes relate, the exact ordering rule, preserved content, foregrounded content, admitted loss, prohibited strengthening, and applicability;
5. cite every exact governed correspondence relation used by the construction; a graph edge, architecture view, source-set row, publication, or similar content does not make one obtain.

If the supposed receiving item has no recoverable claim content, exact EntityOfConcern, or effective reference scheme, it is candidate prose, a publication form, or a carrier—not `Y`; stop before asserting NAR. A valid `n` constructs a candidate episteme but does not make `Y` a `U.View`. E.17.0 conformance decides that separately.

Create a `StructureToNarrativeRenderingCase` only after this boundary passes. The case is local review content, not a new U-kind, relation signature, or identity record:

```text
StructureToNarrativeRenderingCase:
  sourceEpistemeRef: X
  receivingNarrativeEpistemeRef: Y
  viewingConstructionRefOrStatement: n : X -> Y
  additionalSourceEpistemeRefs?:
  exactCorrespondenceRelationRefs?:
  selectedSourceStructureRefs:
  sourceStructureSelectionRationale:
  sourceTemporalPosture:
  renderingMediationMode: direct-source-claims | architecture-mediated | mixed
  architectureMediationEpistemeRef?:
  sourceStructureGoverningPatternRef?:
  narrativeConstructionWorkRef?:
  narratingOrRenderingSystemAndRoleRef?:
  readerOrListenerRoleRefs:
  readerInterestOrUseHypothesis:
  intendedReaderOrListenerUse:
  orderingRationaleOrTraversalRule:
  preservedStructure:
  foregroundedStructure:
  coarsenedOrLostStructure:
  epiplexityOrStructuralInformationRef?:
  recoverabilityClassOrSourceBasisReturnCondition:
  eventModelSupport?:
  engagementOrMotivationClaim?:
  admissibleUse:
  nonAdmissibleDownstreamUse:
  neighboringPatternExits:
```

The references to `X` and `Y` resolve to their complete C.2.1 identities; the case does not add identity slots. `narrativeConstructionWorkRef` is present only when actual history matters. A system performs that dated Work under A.15.1; the morphism does not. Source epistemes, parameters, methods, tools, and `Y` participate through exact direct relations or A.6.1 bindings. If the Work first constitutes `Y` and inception matters, A.15.PROD governs that separate claim.

Publication remains separate. E.24.PUB identifies any occurrence that makes exact selected episteme `Y` available to a declared audience and bounded use through an exact publication form and `U.PresentationCarrier`. The publication occurrence, form, carrier, audience, and readable sequence neither constitute `Y` nor establish `n`.

Use this unfolding block when selected source structure must be carried into a reader-facing sequence with explicit loss and return:

```text
NarrativeUnfoldingStructureBlock:
  sourceEpistemeRef: X
  structureBeingRenderedRef:
  unfoldingStructureBeingRenderedRef?:
  narrativeOrderingStructureRef:
  readerActSequenceHypothesis?:
  receivingNarrativeEpistemeRef: Y
  preservedStructure:
  lostOrCoarsenedStructure:
  narrativeStructureUseReturnCondition:
  blockedOverread: narrative sequence is not X, its selected structure, proof, decision, work sequence, publication, or gate
```

`structureBeingRenderedRef` names an independently governed structure designated by `X`; it does not replace `X`. `narrativeOrderingStructureRef` names the ordering rule or selected sequence structure used for reader understanding. `receivingNarrativeEpistemeRef` names `Y`, not its form or carrier. These are different positions.

`NarrativeUnfoldingStructureBlock` is a local A.22.CGUS `U.Structure` specialization block only when that direct pattern's admission and identity tests pass. It is not a root U-kind, workflow, proof, architecture decision, evidence record, publication permission, or automatic description of every NAR case. Use `unfoldingStructureBeingRenderedRef` only when the exact source structure is itself a constraint-governed unfolding structure.

Work in this order:

1. Identify exact `X`, exact `Y`, and their C.2.1 identity triples.
2. State `n : X -> Y`, same exact EntityOfConcern, endpoint scheme relation, claim construction, prohibited strengthening, and applicability.
3. Name each selected source structure, exact governor, and any additional source episteme or correspondence relation on which `n` depends.
4. State source temporal posture, source-structure selection rationale, and reader-interest or use hypothesis. If these remain only in intuition, a prompt, or finished prose, keep the output candidate-only.
5. Name direct-source-claims, architecture-mediated, or mixed mediation. Architecture descriptions, views, decisions, selected structures, and telemetry remain separate governed objects.
6. Recover actual narrating Work, system, role assignment, method, and bindings only when that history matters.
7. Choose and state the ordering rationale: event, causal, discovery, didactic, tension, graph traversal, architecture-decision, live-commentary, prospective-scenario, source-publication order, or another exact rule.
8. State preserved, foregrounded, coarsened, and lost structure, plus recoverability and return to exact `X` or governed source relations.
9. If the live question is how much structure was pulled into `Y`, cite the structural-information or epiplexity result rather than answering with fluency. Architecture-relevant use routes to C.33; non-architecture narrative evaluation stays with its domain governor, A.19.ECS, and C.16 as applicable.
10. Add event-model support when events, actions, mechanisms, goals, obstacles, state updates, or change are part of the use.
11. Keep engagement or motivation as a bounded use claim. Route persuasion, harm, affected parties, policy influence, bias, value conflict, evidence, and assurance to D.1–D.5, A.10, or B.3 as applicable.
12. Close with admissible use, non-admissible downstream use, source or governing-pattern return, and neighboring exits.

#### A.6.3.NAR:4.1 - Ordinary and claim-bearing cases

Ordinary cases can stay lightweight after exact `X`, exact `Y`, and `n : X -> Y` are recoverable. An internal explanation, teaching example, or orientation narrative then needs only selected source structure, sequence rule, visible loss, admissible use, and return to exact source episteme or governed source relations.

Claim-bearing cases need the fuller record. A case is claim-bearing when the narrative will be used for design, architecture, policy, safety, public science communication, generated-output admission, cross-context reuse, assurance-facing training, or a disputed interpretation.

#### A.6.3.NAR:4.2 - Same-EntityOfConcern and correspondence-mediated profiles

Every NAR construction is same-EntityOfConcern: exact `X` and `Y` designate the same entity. Similar content or a declared correspondence does not relax this rule. If the narrative concerns another entity, use A.6.4 and state its retargeting relation.

Use the **direct-source-claims** profile when `n` constructs `Y` from exact claims in `X` and fixed configuration. A situation, event stream, domain model, proof dependency field, evidence set, fictional canon, or source pack can contribute only after exact `X` claims about it or exact additional source epistemes and governed relations are named. The raw object, graph, set, or pack is not the source endpoint.

Use the **correspondence-mediated** profile when `n` depends on exact governed relations among `X`, additional exact source epistemes, or their designated structures. Recover each direct correspondence, realization, trace, equivalence, or consistency relation under its owner and cite the exact assertion episteme when the construction uses a claim about that occurrence. A C.34 record is used only when C.34 governs the exact correspondence current for this use; it is not a generic cure for dissimilar endpoints.

#### A.6.3.NAR:4.2.1 - Direct and architecture-mediated routes

In the direct route, the exact source episteme states or designates the source situation, event structure, proof dependencies, canon claims, or source-pack claims that `n` orders. Viewpoint discipline may help, but `X`, `Y`, and `n` remain the central objects.

In the architecture-mediated route, one exact architecture-description, architecture-view, decision, candidate-structure, or telemetry episteme participates as `X` or as an explicitly named additional source episteme. Independently recover any selected A.22 structures, world-side holons, decisions, relations, or telemetry occurrences that its claims designate. The return chain is `Y` to exact source episteme(s), then through their governed designations to exact structures or occurrences when those are current. Each selection, coarsening, abstraction, omission, ordering, and correspondence remains explicit under C.33, C.34, C.32.*, and the direct architecture-description or decision governors. NAR governs only `n`.

In either route, the temporal posture matters. A historical reconstruction, live commentary, prospective project narrative, and fictional continuation can all be narrative epistemes, but they have different source claims, evidence and uncertainty boundaries, order, and return conditions. A system may perform narrative-construction Work; the source or narrative episteme does not act.

#### A.6.3.NAR:4.3 - Ordering rationale

The ordering rationale is not decoration. It is the structure-to-sequence rule.

Common ordering rationales:

| Ordering rationale | Use when |
| --- | --- |
| Event order | The selected source structure is a sequence of happenings or state changes. |
| Causal order | The reader must understand mechanism, dependency, intervention, or consequence. |
| Discovery order | The narrative teaches how a claim, design, or explanation was found. |
| Didactic order | The source basis is reordered so a learner can build prerequisites and reconstruct the selected source structures later. |
| Tension order | The narrative preserves conflicts, trade-offs, obstacles, failed attempts, or unresolved alternatives. |
| Traversal rule | The source basis is a graph, architecture, relation set, or option field and the narrative follows a declared path through it. |

If the source basis only changes carrier form, file format, export layout, OCR extraction, or byte order, this pattern is not open. Carrier serialization alone is not narrative rendering.

#### A.6.3.NAR:4.4 - Event model, viewpoint, and agency

If the narrative asks readers to understand events, actions, mechanisms, or change, state the event-model support. At minimum, name the event or mechanism type, participating holons or agents when present, causal or dependency links, update points, and what the narrative asks the reader to predict or revise.

If viewpoint, narrator, focalized object, protagonist, or agency choices affect understanding, keep them in domain narrative vocabulary unless a direct FPF governing pattern is live. In FPF Core, the reusable claim is simpler: the viewpoint choice foregrounds some selected source structure and hides or weakens another structure for a declared use.

#### A.6.3.NAR:4.5 - Engagement, ethics, and assurance boundary

Engagement is a real use claim, but it is not truth or permission.

When an engagement or motivation claim matters, state:

- intended effect for the declared use;
- selected source structure that may not be distorted for that effect;
- affected reader, listener, group, or decision context when relevant;
- non-admissible uses that would overread the narrative;
- direct governing pattern for ethical, evidence, assurance, or policy claims.

Use `D.1` for ethical value-frame entry, `D.2` through `D.4` for multilevel conflict and decision use, `D.5` for bias, human impact, or ethical assurance, `A.10` for evidence, and `B.3` for assurance. Narrative engagement never grants moral permission by itself.

#### A.6.3.NAR:4.6 - Reopen, lower, and return rule

A NAR case stays admissible only while exact `X`, exact `Y`, `n : X -> Y`, selected source structures, intended use, ordering rationale, loss, and source or governing-pattern return still match the receiving use. When one changes, repair the smallest affected object and its dependent claims before reuse; do not turn NAR into a general narrative monitor.

| Trigger | Required move |
| --- | --- |
| Exact `X`, additional source epistemes, or selected governed structures change | Reidentify the changed episteme when a C.2.1 discriminator changed; restate `n`, preservation, foregrounding, loss, and return. Use C.33 only for architecture-relevant captured/lost structure and G.2 only for source-pack claims; lower use until exact source return is restored. |
| Intended reader or listener use becomes stronger, broader, or more reliance-facing | Lower the narrative to orientation-only use until the case is repaired; route publication or audience-unit claims to `E.17` or `E.17.AUD`, and route evidence, assurance, ethics, or policy force to `A.10`, `B.3`, or `D.1` through `D.5`. |
| Ordering rationale or traversal rule changes | Reopen the ordering field and visible-loss account; use `A.6.3.RT` if the representation scheme changed, `A.6.3.CSC` if the source basis was deliberately coarsened for narrower use, and NAR only when selected source structure is still being ordered into a narrative path. |
| Return to exact `X`, exact governed source relations, or the direct next governor is missing, stale, or unreachable | Lower downstream use and refresh that exact return before reliance-facing use; use G.11 when currentness or freshness is the live defect. |
| Generated output, source-basis plan, schema, or admission result changes | Return to `C.35` for generated-carrier admission and `G.2` for source-pack claims; reopen NAR only after the source-basis-to-narrative relation, captured or lost structure, and correspondence obligations are again explicit. |
| Domain narrative vocabulary, source-pack basis, or relevant narrative, NLG, or cognitive SoTA changes the meaning of a relied-on narrative field | Refresh the domain vocabulary or source-pack basis first; lower any NAR claim that depended on the old vocabulary or source-basis anchor until the field meaning is replayable. |
| Downstream use requires stronger evidence, assurance, ethics, publication, or work authority than the NAR case carries | Keep NAR as a representation relation only; route the stronger claim to `A.10`, `B.3`, `D.1` through `D.5`, `E.17`, or the direct work or decision governing pattern, and mark that downstream use non-admissible until that governing pattern admits the stronger claim. |
| Correspondence or preservation claim weakens after repair | Use `C.34` only for the weakened correspondence that remains; use `C.33` for captured and lost architecture-relevant structures, use the domain evaluation pattern for non-architecture epiplexity, and lower any downstream use that required stronger sameness. |

