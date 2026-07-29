---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__005_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:4 — Solution"
line_start: 14460
line_end: 14603
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

Create a `StructureToNarrativeRenderingCase@Context` for the narrative relation.

Use this compact form. Fill only fields that change the admissible use or block a likely overread.

```text
StructureToNarrativeRenderingCase@Context:
  sourceBasisRef:
  selectedSourceStructureRefs:
  sourceStructureSelectionRationale:
  sourceTemporalPosture:
  renderingMediationMode: direct-source-structure | architecture-mediated | mixed
  architectureMediationRef?:
  sourceStructureGoverningPatternRef?:
  narratingOrRenderingWorkerRef?:
  readerOrListenerRoleRefs:
  readerInterestOrUseHypothesis:
  preservedEntityOfConcernRef?:
  declaredCorrespondenceRef?:
  receivingNarrativeRenderingRef:
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

Use this unfolding block when the selected source structure must be carried into a reader-facing sequence with explicit loss and return.

```text
NarrativeUnfoldingStructureBlock:
  structureBeingRenderedRef:
  unfoldingStructureBeingRenderedRef?:
  narrativeOrderingStructureRef:
  readerActSequenceHypothesis?:
  narrativeRenderingRef?:
  preservedStructure:
  lostOrCoarsenedStructure:
  narrativeStructureUseReturnCondition:
  blockedOverread: narrative sequence is not the ontology of the input structure being rendered, proof, decision, work sequence, or gate
```

`structureBeingRenderedRef` names the input structure under concern. `narrativeOrderingStructureRef` names the ordering rule or sequence structure used for reader understanding. `narrativeRenderingRef` names the episteme or publication unit that carries the narrative. These are different positions. A good narrative may preserve the right structure for a reader while deliberately coarsening, reordering, or omitting other structure; the block makes that loss inspectable.

`NarrativeUnfoldingStructureBlock` is a local `A.22.CGUS` `U.Structure` specialization block governed here for narrative-rendering use. It is not a root U-kind, not a workflow, not a proof, not an architecture decision, not evidence, and not publication permission. `A.6.3.NAR` governs the source-structure-to-sequence relation; generated-output admission, source-pack claims, architecture-description claims, ethics, evidence, assurance, rights, publication, and work claims leave to their direct governing patterns.

Use `unfoldingStructureBeingRenderedRef` only when the source basis itself is a constraint-governed unfolding structure. Otherwise NAR may still order a selected source structure, architecture description, event stream, proof dependency field, option field, or source pack without claiming CGUS.

Work in this order:

1. Name the source basis, the selected source structure that must survive, and its temporal posture: retrospective or reverse-engineered actual, live unfolding, prospective planned, prospective fictional, or mixed.
2. State the source-structure selection rationale and the reader-interest or use hypothesis. If these are only implicit in a draft, treat the draft as a candidate carrier until the rationale is reconstructed.
3. Name the rendering mediation mode. Use `direct-source-structure` for a situation, event stream, proof field, canon, or source pack rendered directly; use `architecture-mediated` when architecture understanding, architecture description, architecture view, architecture viewpoint, decision record, candidate structure, or telemetry is the mediating source basis.
4. Name the narrating or rendering worker, the receiving narrative rendering, and the intended reader or listener role and use.
5. State whether the same EntityOfConcern is preserved or whether a `C.34` correspondence is needed.
6. Choose the ordering rationale: event order, causal order, discovery order, didactic order, tension order, graph traversal, architecture-decision sequence, live-commentary sequence, prospective-scenario sequence, source-publication order, or another declared rule.
7. State preserved structure, foregrounded structure, coarsened or lost structure, and recoverability.
8. If the live question is how much structure was pulled into the narrative, create or cite the structural-information or epiplexity note instead of answering with fluency. For architecture-relevant uses this routes to `C.33`; for declared narrative-quality evaluation this routes to the domain narrative evaluation pattern, `A.19.ECS`, and `C.16` as applicable.
9. Add event-model support when the narrative asks the reader to understand events, actions, mechanisms, goals, obstacles, state updates, or change.
10. Add engagement or motivation only as a declared-use claim. If persuasion, harm, affected parties, policy influence, bias, value conflict, or ethical assurance is live, route the claim to `D.1` through `D.5`, `A.10`, or `B.3` as applicable.
11. Close with admissible use, non-admissible downstream use, source-basis or governing-pattern return condition, and neighboring-pattern exits.

#### A.6.3.NAR:4.1 - Ordinary and claim-bearing cases

Ordinary narrative renderings can stay lightweight. An internal explanation, teaching example, or orientation story usually needs only a compact note: source basis, selected structure, sequence rule, visible loss, and source-basis return condition.

Claim-bearing cases need the fuller record. A case is claim-bearing when the narrative will be used for design, architecture, policy, safety, public science communication, generated-output admission, cross-context reuse, assurance-facing training, or a disputed interpretation.

#### A.6.3.NAR:4.2 - Same-entity and correspondence-mediated profiles

Use the same-entity profile when the receiving narrative is still a rendering of the same EntityOfConcern and the source tether remains visible.

Use the correspondence-mediated profile when the narrative is produced from a source model, graph, architecture view, or generated relation set that corresponds to the source but is not the same representation. In that case, create or cite the `C.34` correspondence record before the narrative is treated as same enough for a downstream use.

#### A.6.3.NAR:4.2.1 - Direct and architecture-mediated routes

Use the direct source-structure mediation mode when the narrative worker renders a situation, event stream, domain model, proof dependency field, evidence set, fictional canon, or source pack directly into a narrative path. View and viewpoint discipline may still help, but the central governing relation is the NAR relation plus any domain-specific narrative or evaluation pattern, not the architecture line.

Direct does not mean implicit. If the selected source structures, selection rationale, reader-interest hypothesis, ordering rationale, and loss account are left inside the writer's intuition, an LLM prompt, or a finished story, the output is only a candidate carrier or candidate prose, not an admitted narrative rendering. It can inspire a later NAR case, but reliance-facing use requires reconstructing and checking the missing selection and loss record.

Use the architecture-mediated mode when the selected source structure is actual or possible holon structure that has been understood through architecture work: reverse-engineering an existing holon, comparing candidate future structures, using architecture descriptions and views, applying architecture decisions, or checking telemetry after realization. In this mode the return chain is narrative rendering to architecture description or view, then to architecture as selected structures in context, then to wider holon or source-basis structures when those are current. Each relation can select, coarsen, abstract, omit, or order structure, and each relation needs its own source-basis, description, view, architecture-decision, or governing-pattern return condition when the loss becomes live. `C.33`, `C.34`, `C.32.*`, architecture-description governing patterns, and architecture-decision governing patterns remain live. NAR governs only the narrative rendering of that architecture-relevant structural information.

The temporal posture matters in both mediation modes. A historical reconstruction, a live football broadcast, a prospective project narrative, and a fictional continuation may all be narratives, but they have different source-basis return, evidence, uncertainty, ordering, and non-admissible-use obligations.

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

A NAR case stays admissible only while its source basis, selected source structures, intended use, ordering rationale, source-basis or governing-pattern return condition, and neighboring governing-pattern exits still match the narrative rendering's use. When one of these changes, repair the smallest affected part of the case before relying on the narrative again. Do not turn NAR into a general monitor for all narrative science; this rule is local to the declared NAR case and its governing-pattern routing obligations.

| Trigger | Required move |
| --- | --- |
| Selected source structures or source basis change | Reopen the NAR case; restate preserved, foregrounded, coarsened, and lost structure; use `C.33` only when the narrative rendering is being used as architecture-relevant structural information, use the domain evaluation pattern for non-architecture epiplexity, use `G.2` for source-pack claims, and lower admissible use until the named source basis or receiving governing-pattern return condition is restored. |
| Intended reader or listener use becomes stronger, broader, or more reliance-facing | Lower the narrative to orientation-only use until the case is repaired; route publication or audience-unit claims to `E.17` or `E.17.AUD`, and route evidence, assurance, ethics, or policy force to `A.10`, `B.3`, or `D.1` through `D.5`. |
| Ordering rationale or traversal rule changes | Reopen the ordering field and visible-loss account; use `A.6.3.RT` if the representation scheme changed, `A.6.3.CSC` if the source basis was deliberately coarsened for narrower use, and NAR only when selected source structure is still being ordered into a narrative path. |
| Source-basis or governing-pattern return condition is missing, stale, or no longer reachable | Lower downstream use, return to the named source basis or receiving governing pattern, and refresh that return condition before treating the narrative as reliance-facing. Use `G.11` when currentness or freshness is the live problem. |
| Generated output, source-basis plan, schema, or admission result changes | Return to `C.35` for generated-carrier admission and `G.2` for source-pack claims; reopen NAR only after the source-basis-to-narrative relation, captured or lost structure, and correspondence obligations are again explicit. |
| Domain narrative vocabulary, source-pack basis, or relevant narrative, NLG, or cognitive SoTA changes the meaning of a relied-on narrative field | Refresh the domain vocabulary or source-pack basis first; lower any NAR claim that depended on the old vocabulary or source-basis anchor until the field meaning is replayable. |
| Downstream use requires stronger evidence, assurance, ethics, publication, or work authority than the NAR case carries | Keep NAR as a representation relation only; route the stronger claim to `A.10`, `B.3`, `D.1` through `D.5`, `E.17`, or the direct work or decision governing pattern, and mark that downstream use non-admissible until that governing pattern admits the stronger claim. |
| Correspondence or preservation claim weakens after repair | Use `C.34` only for the weakened correspondence that remains; use `C.33` for captured and lost architecture-relevant structures, use the domain evaluation pattern for non-architecture epiplexity, and lower any downstream use that required stronger sameness. |

