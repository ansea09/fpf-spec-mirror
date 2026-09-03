---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__005_solution.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:4 — Solution"
line_start: 15373
line_end: 15543
dependencies:
  - "A.10"
  - "A.22.CGUS"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "B.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "D.1"
  - "D.5"
  - "E.11"
  - "E.17"
  - "E.17.0"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.24.PUB"
  - "E.6"
  - "F.19"
  - "G.11"
  - "G.2"
keywords:
---

### A.6.3.NAR:4 - Solution

Produce the ordinary useful result first:

1. Name the reader or listener and the practical use: what must become understandable, reconstructible, predictable, or discussable.
2. Point to the source material and select only the structures needed for that use. Say why those structures matter.
3. State temporal posture or mediation only when it changes the ordering or the trust boundary.
4. Choose an ordering and connective account: event, causal, discovery, didactic, tension, traversal, or another explicit rule.
5. Draft the smallest narrative that lets the reader follow that path. For technical prose, use F.19 for sentence-level repair.
6. Compare the draft back to the source material. Record what it preserves and foregrounds, what it omits or weakens, and which connective or interpretive statements are not source claims.
7. State the admissible narrative use and the return condition. Name when exact source material must be restored, or state the stronger claim-specific question and apply the pattern whose Solution answers it. Use F.19:4's plausible-reader test for any optional non-admissible use.

Use this compact note for ordinary work. Fill only entries that affect use or block a likely overread:

| Narrative note entry | Practical question |
| --- | --- |
| Reader/listener and use | Who needs the narrative, and what should it enable? |
| Source material | What exact page, episteme, graph, model, record, or source pack will the author return to? |
| Selected structures and rationale | Which relations, events, mechanisms, dependencies, conflicts, or alternatives matter, and why these? |
| Ordering and connective account | Why does this path help the reader, and which links are explanatory additions rather than source claims? |
| Preserved and foregrounded | What can the reader still recover, and what receives extra attention? |
| Omitted, weakened, or unsupported | What is deferred, lost, rearranged, or newly suggested without source support? |
| Use boundary | What use does this narrative support, and within which limits? |
| Return or stronger question | When must the reader restore exact source material, or what stronger claim-specific question must be answered before the use continues? |

#### A.6.3.NAR:4.0.1 - Exact construction branch

Open this branch only when the receiving use makes exact identity material: the narrative must travel independently or be cited; an exact interpretation is disputed; a material cross-scheme reuse is consequential; generated-output admission requires claim-level identity; consequential reliance is current; or another named public, evidence, or assurance receiver explicitly requires exact identity. Public distribution by itself is not such a requirement. Apply E.24.PUB separately when an actual publication occurrence, form, carrier, audience, or bounded publication use is current.

Then establish exact A.6.3 construction `n : X -> Y`:

1. identify source episteme `X` and receiving narrative episteme `Y` independently under C.2.1 by claim content, exact EntityOfConcern, and effective `U.ReferenceScheme`;
2. require the same exact EntityOfConcern; a narrative about another concern requires A.6.4;
3. state how exact claims in `X` and any named additional source epistemes construct the sequential claim content of `Y`;
4. state the endpoint scheme relation, ordering rule, preserved and foregrounded content, admitted loss, prohibited strengthening, applicability, and return; and
5. cite every exact correspondence relation on which the construction actually depends and test it under its direct predicate.

Recover `X` as the exact source episteme whose claim content and EntityOfConcern supply the narrative source, and recover `Y` as the exact receiving narrative episteme. Treat input models and publications according to their source claims and keep forms and carriers in their direct roles. If the receiving item lacks recoverable claim content, an exact EntityOfConcern, or an effective reference scheme, keep it as candidate prose or a carrier and stop before asserting exact NAR.

Use the fuller local record when the trigger above is present. It is not a new U-kind, relation signature, identity record, or universal checklist:

```text
StructureToNarrativeRenderingCase:
  sourceEpistemeRef: X
  receivingNarrativeEpistemeRef: Y
  viewingConstructionRefOrStatement: n : X -> Y
  additionalSourceEpistemeRefs?:
  exactCorrespondenceRelationRefs?:
  selectedSourceStructureRefs:
  sourceStructureSelectionRationale:
  sourceTemporalPosture?:
  renderingMediationMode?: direct-source-claims | architecture-mediated | mixed
  architectureMediationEpistemeRef?:
  sourceStructureDefinitionClaimEpistemeRefs?:
  sourceStructureConstraintClaimEpistemeRefs?:
  narrativeConstructionWorkRef?:
  narratingOrRenderingSystemRef?: U.EntityRef resolving to an admitted U.System
  narratingOrRenderingSystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
  narratingOrRenderingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment
  readerOrListenerSystemRefs[]?: U.EntityRef values resolving to admitted systems
  readerOrListenerSystemRoleKindRefs[]?: U.KindRef values resolving to exact local system-role kinds
  readerOrListenerSystemRoleAssignmentRefs[]?: U.RelationRef values constrained to U.SystemRoleAssignment
  readerInterestOrUseHypothesis:
  intendedReaderOrListenerUse:
  orderingRationaleOrTraversalRule:
  preservedStructure:
  foregroundedStructure:
  coarsenedOrLostStructure:
  unsupportedStrengtheningBlocked:
  epiplexityOrStructuralInformationRef?:
  recoverabilityClassOrSourceBasisReturnCondition:
  eventModelSupport?:
  engagementOrMotivationClaim?:
  admissibleUse:
  nonAdmissibleDownstreamUse?:
  strongerClaimQuestionsAndActions[]?:
```

`selectedSourceStructureRefs` identifies the selected structures. A PatternID mentioned in `sourceStructureSelectionRationale` or surrounding prose only locates the content used to recognize or test them; it is not another structure reference. Include `sourceStructureDefinitionClaimEpistemeRefs` or `sourceStructureConstraintClaimEpistemeRefs` only when the exact identity of one or more definition or constraint claims changes reconstruction, comparison, dispute, or reliance. Both lists may be present and each resolves only to claim-bearing C.2.1 epistemes of the named kind.

Resolve `X` and `Y` to their complete C.2.1 identities and use this record only for the construction account. When actual production history matters, recover each precise performer's A.13 core and independently admit dated narrative-construction Work under A.15.1; add F.6 afterward only when precise assignment-bound attribution is current. `readerInterestOrUseHypothesis` remains the working hypothesis. Include each optional System, system-role-kind, or assignment reference only when its exact referent and direct claim obtain independently. Connect source epistemes, parameters, methods, tools, and `Y` through exact direct relations or A.6.1 bindings. If the Work first constitutes `Y` and that inception claim matters, use A.15.PROD to test that separate local claim.

`nonAdmissibleDownstreamUse?`, also named `groundedNonAdmissibleDownstreamUse?`, is one optional explanatory field governed by F.19:4's plausible-reader test.

Publication remains separate. E.24.PUB identifies any occurrence that makes selected episteme `Y` available to an audience and bounded use through a publication form and `U.PresentationCarrier`. C.2.1 identifies `Y`, A.6.3 governs the construction `n`, and E.17.0 independently decides whether `Y` has `U.View` membership.

Use this optional unfolding block when an independently identified selected structure must be carried into a reader-facing sequence with explicit loss and return:

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
  narrativeStructureUseReturnCondition: return to exact source episteme X, then through its designation relations to the selected source structure when an omitted branch or exact order matters; apply the relevant pattern for any stronger claim
  blockedOverread?: optional explanatory guard under F.19:4's plausible-reader test
```

`structureBeingRenderedRef`, `narrativeOrderingStructureRef`, and any receiving narrative episteme occupy different positions. Use `unfoldingStructureBeingRenderedRef` only when the source structure is itself a constraint-governed unfolding structure. Treat the block as an A.22.CGUS `U.Structure` specialization only when CGUS admission and identity tests pass; ordinary NAR does not require it. `returnCondition` names the same value as `narrativeStructureUseReturnCondition`, not a second return rule.

#### A.6.3.NAR:4.1 - Ordinary and reliance-facing cases

An internal explanation, teaching example, orientation narrative, or early team account normally closes with the compact note and a source comparison. Its first useful result is the narrative itself, not an exactness form.

Move progressively. Add temporal posture, event-model support, mediation, viewpoint, engagement, or worker history only when each distinction changes the use or blocks a likely error. Open the exact construction branch only at its declared trigger. A reliance-facing case then carries forward the ordinary narrative and note; it does not replace them with a dossier.

#### A.6.3.NAR:4.2 - Exact same-EntityOfConcern and correspondence-mediated profiles

This subsection applies only after the exact branch is open. Exact NAR is same-EntityOfConcern: `X` and `Y` designate the same exact concern even when their effective reference schemes differ. Similar content or a declared correspondence does not relax this rule. If the receiving narrative concerns another entity, use A.6.4 and state the retargeting relation there.

Use the **direct-source-claims** profile when `n` constructs `Y` from claims in `X` and fixed configuration. A situation, event stream, domain model, proof-dependency field, evidence set, fictional canon, or source pack can contribute only through claims in `X` or through named additional source epistemes and exact relation occurrences. The raw object, graph, set, or pack is not the source endpoint.

Use the **correspondence-mediated** profile when `n` depends on exact relations among `X`, additional source epistemes, or their designated structures. Recover each correspondence, realization, trace, equivalence, or consistency relation by applying the pattern that defines its predicate, and cite the assertion episteme when the construction uses a claim about that occurrence. Use a C.34 record only when C.34's correspondence test fits the current use; it is not a generic cure for dissimilar endpoints.

#### A.6.3.NAR:4.2.1 - Direct and architecture-mediated routes

In the direct route, the exact source episteme states or designates the source situation, event structure, proof dependencies, canon claims, or source-pack claims that `n` orders. Viewpoint discipline may help, but `X`, `Y`, and `n` remain the central objects.

In the architecture-mediated route, one exact architecture-description, architecture-view, decision, candidate-structure, or telemetry episteme participates as `X` or as an explicitly named additional source episteme. Independently recover any selected A.22 structures, world-side holons, decisions, relations, or telemetry occurrences that its claims designate. The return chain is `Y` to exact source episteme(s), then through their exact designation relations to exact structures or occurrences when those are current. Keep every selection, coarsening, abstraction, omission, ordering, and correspondence explicit by using the applicable `C.32.*`, C.33, C.34, architecture-description, or decision test. NAR defines only `n`'s source-to-narrative construction, preservation, loss, and return boundary.

In either route, the temporal posture matters. A historical reconstruction, live commentary, prospective project narrative, and fictional continuation can all be narrative epistemes, but they have different source claims, evidence and uncertainty boundaries, order, and return conditions. A system may perform narrative-construction Work; recover its identity only when actual production history matters.

#### A.6.3.NAR:4.3 - Ordering rationale

The ordering rationale is not decoration. It is the structure-to-sequence rule.

Common ordering rationales:

| Ordering rationale | Use when |
| --- | --- |
| Event order | The selected source structure is a sequence of happenings or state changes. |
| Causal order | The reader must understand mechanism, dependency, intervention, or consequence. |
| Discovery order | The narrative teaches how a claim, design, or explanation was found. |
| Didactic order | The source material is reordered so a learner can build prerequisites and reconstruct the selected source structures later. |
| Tension order | The narrative preserves conflicts, trade-offs, obstacles, failed attempts, or unresolved alternatives. |
| Traversal rule | The source material presents a graph, architecture, relation set, or option field and the narrative follows a declared path through it. |

If the source material only changes carrier form, file format, export layout, OCR extraction, or byte order, this pattern is not open. Carrier serialization alone is not narrative rendering.

#### A.6.3.NAR:4.4 - Event model, viewpoint, and agency

If the narrative asks readers to understand events, actions, mechanisms, or change, state enough event-model support to preserve the relevant happening or mechanism type, participants, causal or dependency links, update points, and what the reader is expected to predict or revise.

If viewpoint, narrator, focalized object, protagonist, or agency choices affect understanding, keep their detailed vocabulary in the narrative domain. In FPF Core the reusable check is simpler: which selected source structure does the viewpoint foreground, hide, or weaken for this declared use? Invoke another FPF pattern only for a specific stronger claim that pattern actually defines.

#### A.6.3.NAR:4.5 - Engagement, ethics, and assurance boundary

Engagement is a real use claim. When engagement or motivation matters, state the intended effect, the source structure that may not be distorted for that effect, the affected reader or decision context, and the return condition. Use F.19:4's plausible-reader test for any optional explanatory guard.

Use `D.1` for ethical value-frame entry, `D.2` through `D.4` for multilevel conflict and decision use, `D.5` for bias, human impact, or ethical assurance, `A.10` for evidence, and `B.3` for assurance. Apply only the patterns needed by the current claim.

#### A.6.3.NAR:4.6 - Reopen, lower, and return rule

An ordinary narrative remains fit while its source material, selected structures, reader use, ordering/connective account, loss statement, and return still match the actual use. An exact case additionally depends on the current identities of `X` and `Y`, the construction `n`, its source relations, and every exact qualification used by the receiving claim. Repair the smallest affected account and its dependent claims; do not turn NAR into a general narrative monitor.

| Trigger | Required move |
| --- | --- |
| Source material or selected structures change | Recompare the narrative with the changed source, revise ordering, preservation, loss, unsupported additions, and return, and lower use until the useful path is honest again. |
| An exact discriminator of `X`, `Y`, an additional source episteme, or a depended-on relation changes | Reidentify only the changed exact object; restate the affected part of `n`, preservation, loss, and return. Use C.33 only for architecture-relevant captured/lost structure and G.2 only for source-pack claims. |
| Intended reader or listener use becomes stronger, broader, or more reliance-facing | Lower the existing narrative to its supported use. Open the exact branch only if the changed receiver now makes claim identity material, and add only the identity, source-chain, evidence, assurance, ethics, publication, or policy account that receiver requires; otherwise revise the ordinary note and stop there. |
| Ordering rationale or connective account changes | Reopen the ordering and visible-loss account. Use RT as well when a material representation-scheme shift remains after narrative ordering is accounted for; use CSC when a narrower-use coarsened episteme is primary. |
| Exact source material is missing, stale, or unreachable, or a stronger claim still lacks its claim-specific result | Lower downstream use. Restore access to the exact source material; when the stronger claim is current, apply the pattern whose Solution answers that question and keep the claim unresolved until its result is available. Use G.11 when currentness or freshness is the live defect. |
| Generated output, source-pack plan, schema, or admission result changes | Use C.35 for generated-carrier admission and G.2 for source-pack claims; reopen NAR only for the affected source-to-narrative relation, loss, and return. |
| Domain narrative vocabulary or relevant narrative, NLG, or cognitive SoTA changes a relied-on field | Refresh that domain basis and replay the affected use; do not enlarge Core vocabulary merely to mirror the domain source. |
| Downstream use requires evidence, assurance, ethics, publication, policy, decision, or work authority that NAR does not supply | Keep NAR as the narrative construction account and state the stronger claim under `A.10`, `B.3`, `D.1`–`D.5`, `E.24.PUB`, or the exact pattern that defines the needed decision or Work relation. |
| A correspondence or preservation claim weakens | Use C.34 only for the correspondence that remains; use C.33 for captured/lost architecture-relevant structures and the domain evaluation pattern for other narrative epiplexity. Lower uses that required stronger sameness. |

