---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__006_solution.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:4 — Solution"
line_start: 8746
line_end: 8914
dependencies:
  - "A.1"
  - "A.10"
  - "A.11"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.22"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "G.11"
keywords:
  - "actual bounded change"
  - "actual subject facts"
  - "changed referent"
  - "continuity and reidentification"
  - "occurrence boundary"
  - "transformation composition"
---

### A.3.4:4 - Solution

#### A.3.4:4.1 - Identify the actual bounded change

`U.Transformation` is the FPF ontic for one actual bounded change. Use the five checks below and keep only the facts needed to distinguish this occurrence:

1. **Changed subject.** Name the continuing entity, selected structure, presentation carrier, constituent organization, characteristic-bearing referent, or formal object and apply its identity rule. If an episteme's claim content differs across the boundary, identify two C.2.1 epistemes and test their `EpistemeEditionRelation`; do not call either one the continuing changed subject. Use A.3.4 only for another continuing subject, or use `A.15.PROD` when revision `U.Work` first constitutes the later episteme.
2. **Extent and boundary.** State the temporal extent of the change, including only gaps admitted by its continuity rule, or state the ordering boundary in a declared formal substrate.
3. **Boundary conditions.** State the conditions that delimit this change from adjacent persistence, work, or change occurrences.
4. **Actual change facts.** Write the characteristic-state facts and relations that actually hold before, during, and after the boundary. Those facts, not a verbal change label, show what changed.
5. **Continuity or reidentification.** If the subject varies internally, the change pauses, or several intervals are proposed, state the rule that says the subject and this occurrence continue across that variation.

Here, **one** means one occurrence at the resolution, subject, extent, and boundary needed for this use. It does not mean elementary, atomic, indivisible, or partless. Later refinement may identify finer changes, and future accepted work may establish constructive parts; sampling or subdividing time establishes neither result.

Do not call a possible, desired, planned, predicted, modeled, asserted, or published change actual. Those are claims in an episteme, method, work plan, dynamics model, or publication until the occurrence facts above hold. A formal transformation can be actual within an admitted formal substrate, but its formula or proof term remains a `C.29` representation of that independently identified formal change.

**Mint vs reuse.** A.3.4 reuses the already admitted root U-kind and public name `U.Transformation` from E.24.UK. It introduces no additional U-kind, relation kind, public composition name, `RelationSignature`, or local well-formedness identifier. The component-change and whole-configuration-change wording below names only question roles for independently identified occurrences; it asserts no composition.

#### A.3.4:4.2 - First-use transformation basis

Use these questions as a recognition aid, not as fields of a transformation record:

| Question | What to write | Stop condition |
| --- | --- | --- |
| What changed? | one continuing subject under its identity rule | stop if only a label, file, diagram, or desired object is available |
| Across which boundary? | temporal extent or formal ordering boundary | stop if before and after are merely two unrelated observations |
| What actual facts differ? | the relations and characteristic-state facts that hold before, during, and after the boundary | stop if the only basis is a method, plan, trace, formula, or assertion |
| What delimits one occurrence? | boundary conditions and continuity or reidentification rule | split or leave identity unresolved when the rule does not cover the gap |
| Which later claim or use, if any, relies on this change? | name that claim and apply its pattern: for example dated `U.Work`, a safety evaluation, a publication assertion, or no neighboring use | write only the relation needed by that branch; if no later use is being claimed, add nothing |

**Worked first use.** For a reactor cooling loop, identify the loop state as the changed subject, the thermal-power step and stabilization interval as the boundary, the measured temperature-profile facts before and after it, and the operating conditions that delimit the episode. These facts ground `CoolingLoopTransformation-7 : U.Transformation`. The revised operating method, control-law episteme, measurements, safety evaluation, and release decision remain separate objects; none alone is the transformation. This short fixture identifies no dated adjustment `U.Work` occurrence.

Choose only the next claim that the use actually needs:

- **Work.** First identify a dated `U.Work` occurrence under `A.15.1`. If both work and transformation participants are identified, apply the three outcomes in `4.2.4`. The short reactor fixture has not identified that work occurrence, so it makes no work-to-change claim and does not yet report a missing governor.
- **Safety evaluation.** Use case-local `evaluatesTransformation@PlantSafety-v4(SafetyEvaluation-7, CoolingLoopTransformation-7, CoolingLoopSafetyCriterion-v4)` only when all three participants are identified and the predicate's obtaining conditions hold. The evaluation is not thereby a decision.
- **Publication.** Use a C.2.1 assertion whose EntityOfConcern is `CoolingLoopTransformation-7` and identify its E.24.PUB publication occurrence. Publication neither creates nor performs the change.

If none of these uses is being claimed, keep the identified transformation and add no neighboring relation.

**Choose the next branch now.** If the current result is one identified transformation and the use needs no positive claim that several changes compose one change or that the change is a holon, continue directly at 4.3. Sections 4.2.1-4.2.3 are not prerequisites for that ordinary route. Open them only when the use needs one of those two positive claims; the current advanced branch returns the parked blocker and selects no future architecture.

##### A.3.4:4.2.1 - Keep proposed component and whole-configuration changes separate

Use *component change* and *whole-configuration change* only as ordinary question roles for actual `U.Transformation` occurrences already identified through A.3.4:4.1. They are not additional U-kinds, record fields, or evidence that one change is part of another.

Identify every proposed component change and the proposed whole-configuration change independently. A sampled point, arbitrary subinterval, method step, work part, flow node, graph edge, trace segment, formula term, before-and-after image, shared changed subject, or temporal inclusion establishes neither composition nor absence of finer parts.

The neighboring general patterns do not silently answer the composition question. `A.22` can identify a selected structure whose relation organization changes; `C.27.TA` can identify temporal aspects; `A.14` and `C.13` define structural mereology and a `Γ_m` construction trace. None of those results by itself says that several actual changes compose one actual change. A materialized `Γ_m.sum` trace is a C.2.1 episteme about identified entity-part relations, assembly, and direct identity or reidentification conditions. It establishes neither those world-side facts nor transformation composition.

One independently identified change of a selected configuration can therefore remain a valid configuration transformation. If the use needs no positive composition or transformation-holon claim, continue with that transformation and the ordinary neighboring-object guidance in `4.3`-`4.8`. If it does need such a claim, retain the identified changes and stop with **missing transformation-composition governor**; a proposed local compound claim also stops with **missing derivation substrate**. Neither stop says that composition is false or that any change is partless.

##### A.3.4:4.2.2 - Keep the composition architecture open (informative)

Transformation composition remains an open research question, not a relation architecture declared by this Stable pattern. Future work must decide what identifies and reidentifies a proposed whole change and its constituents; whether and when method parts, work parts, changed-substrate changes, temporal segments, and causal contributions correspond; which contribution, compatibility, boundary, interface, and whole-level-characteristic laws matter; and what substrate, if any, makes a derived claim valid.

That work must also compare rather than preselect the representation of the answer: one generic relation, several subject-specific relations, bounded local compound claims, or continued non-admission. A.3.4 chooses none of them. It mints no composition relation kind, designator, signature, occurrence-identity law, or local well-formedness identifier.

##### A.3.4:4.2.3 - Apply A.1 only after composition is independently established

Membership in `U.Transformation` supplies no holonhood. A.1 remains the authority for the constructive criterion. This edition of A.3.4 supplies neither a positive transformation-composition result nor the candidate, constituents, constructive part relations, and assembly needed by A.1. Therefore an independently identified configuration transformation remains a valid `U.Transformation`, while positive `U.Holon` classification on the basis of transformation composition stops. The stop is not evidence that no such whole or parts exist.

If future accepted work supplies one whole transformation and its construction facts, apply A.1 without changing its test or assuming which relation form that work chose. A.1 still requires the candidate, constituents, constructive part relations and assembly, reidentification rule, composition-grounded whole-level characteristic, and possible participation in a larger constructive assembly. Recover those facts from the patterns that define them at that time; a name, shared interval or referent, nearby change, trace, diagram, or missing-governor note supplies none of them.

A.1 also keeps world-side satisfaction or failure separate from an A.6.1 `true | false | unknown` recognition evaluation, an optional C.2.1 assertion, evidence and assurance, G.11 currentness, receiving-work disposition, and B.2 whole reidentification. Follow A.1 for that separation rather than repeating its full table here.

Stress the current boundary before classifying:

- a pressure increase may be identified as one `U.Transformation` at the resolution needed by the use; sampling or subdivision establishes neither constructive parts nor absence of such parts;
- a switch transition may be treated as effectively instantaneous at the selected temporal resolution and identified as one `U.Transformation`; that resolution claim establishes neither indivisibility nor parts;
- subintervals of continuous biological growth may each be independently identified as transformations, but this pattern does not decide whether they compose one change;
- a formal transformation can be actual under a selected formal substrate, while its formula, morphism, or proof term remains a C.29 representation and supplies no holonhood;
- mounting, wiring, connection, and whole-configuration changes may each be identified independently; the current edition does not make them constituents of one transformation, so positive A.1 classification on that basis does not begin.

##### A.3.4:4.2.4 - Keep work and production claims outside transformation identity

Do not infer a work-to-change connection from shared timing, a common affected subject, or the word *successful*. Once the `U.Work` and `U.Transformation` participants are both identified, choose exactly one outcome: (1) apply an existing subject predicate whose declared participants and obtaining condition match the case; (2) state an `A.6.RCD` disposition-2 local compound claim over named base facts and an admitted substrate; or (3) return `missing-governor` for that exact pair.

Production is a separate question. A post-state, work reference, verbal predicate, continuing changed entity, or `U.Holon` classification proves neither production-work participation, first existence of an entity, nor production completion. Apply `A.15.PROD` to the exact work, work part, subject-identity facts, completion criterion, and direct effect facts. A.3.4 contributes only the independently identified transformations; it adds no universal work-to-change or production relation.

**Filled positive branch — result:** C.2.1 assertion `BuildWorkPopulatedStore-12` states the local connection between `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work` and `ArtifactStorePopulationTransformation_12 : U.Transformation`. The BuildOps predicate `BuildWorkPopulatedStore@BuildOps-v12(work, transformation)` holds only when that work performs the `storeWrite` application that changes the same `ArtifactStorePartition_12` across the same boundary. `BuildApplication_12` supplies the performed application and its `builtBinary -> ReleaseBinary_12` binding; the partition's before/after artifact-presence facts ground the transformation. This is an `A.6.RCD` disposition-2 local compound claim, not a universal FPF work-to-change kind or occurrence.

**Pump 14 — current result and earlier no-governor stage:** A.3.4 identifies `T-P14-PRESSURE-RISE : U.Transformation` as the bounded change of continuing `HydraulicLoop_P14`; the loop's discharge-pressure characteristic is `belowBand` at the opening boundary and `inBand` at the closing boundary. The current case record contains relation-declaration episteme `P14-REL-2026`, owned by `Pump14OperationsRelations`, which declares `AdjustmentWorkCausesPressureRise` for exact participants `W-P14-ADJUST-1010-1020 : U.Work` and `T-P14-PRESSURE-RISE`; a separately stated case fact satisfies its actual-causation predicate. Therefore write: `W-P14-ADJUST-1010-1020 caused T-P14-PRESSURE-RISE`; neither shared timing nor transformation identity supplies that fact. In the explicitly earlier case record, `P14-REL-2026` is absent; at that epistemic stage, keep the same Work and transformation, return `missing-governor: work-to-change claim for <W-P14-ADJUST-1010-1020, T-P14-PRESSURE-RISE>`, and route the missing declaration to `Pump14OperationsRelations` instead of asserting causation.

#### A.3.4:4.3 - Keep six layers separate

For one identified transformation, keep these objects distinct:

| Layer | Object to keep distinct | Where to check it |
| --- | --- | --- |
| actual bounded change | one `U.Transformation` | A.3.4 identifies the continuing subject, extent, boundary conditions, before/during/after facts, and continuity rule |
| facts about the changed subject | relation occurrences and characteristic-state facts that actually hold | each subject pattern defines the participants, obtaining rule, and identity |
| reusable change semantics | one predicate-definition episteme when repeated use needs the same rule | A.3.4 or the subject pattern states how the listed base facts satisfy that predicate |
| transformation assertion | one C.2.1 episteme asserting that the transformation or base facts obtain | C.2.1 identifies claim content, exact EntityOfConcern, and effective reference scheme; scope and viewpoint remain neighboring relations |
| representation | formula, morphism, path, graph, diagram, trace, tuple, or state-plane expression | C.29 governs correspondence to independently recovered objects |
| evidence or evaluation result | an episteme used to support or evaluate the assertion | the measurement, evaluation, evidence, provenance, or assurance pattern defines or constrains that use |

A verbal predicate does not turn every obtaining relation occurrence into a transformation. Assignment, availability, installation, and temporal order can obtain without change. Conversely, one actual transformation may require several relation facts without being identical to any one of them.

Do not restore the old `transformationRelation` field. If an existing relation already states the needed fact, use it. Otherwise apply `A.6.RCD`: a local compound claim is available only when its exact base facts and admitted substrate are present; if either is missing, return `missing-governor` or `missing-substrate`. Introduce a reusable predicate-definition episteme only when repeated uses need the same rule. A new durable relation kind still needs its own obtaining and occurrence-identity law; a task, morphism, operation family, or verbal predicate cannot be inserted into one union-valued field.

#### A.3.4:4.4 - Add neighboring objects only for the claim being made

A neighboring object is not a slot of `U.Transformation`. Add it only for the claim the reader is making, and state its relation to the transformation, changed subject, work, or later use.

| Claim being made | Pattern and boundary |
| --- | --- |
| reusable semantic way of doing | `A.3.1` governs `U.Method`; method existence establishes no actual change |
| claim-bearing account of that way | `A.3.2` and C.2.1 govern `U.MethodDescription`; description establishes neither work nor change |
| typed operation arguments or results | A.6.1 governs the exact operation declaration and application binding; these are not generic transformation inputs or outputs |
| intended work | `A.15.2` governs `U.WorkPlan`; intention establishes no dated work or actual transformation |
| performed work | `A.15.1` governs dated `U.Work` occurrences; `4.2.4` then requires an existing subject predicate, an `A.6.RCD` disposition-2 local compound claim, or `missing-governor` for the named work/transformation pair |
| transformation-flow location or composition | `E.18` governs selected `TransformationFlowStructure`; a flow locus neither performs work nor makes a change actual |
| mathematical expression | `E.18.2` and `C.29` govern representation; a graph edge, morphism, or delta expression is not the world-side occurrence |
| dynamics model | `A.3.3` governs the episteme; prediction is not actuality or permission |
| evidence, measurement, evaluation, or assurance | apply the measurement, evaluation, evidence, provenance, or assurance pattern that states the support or judgment relation; none of those results makes the change actual |
| description, view, publication, form, or carrier | C.2.1, `E.17`, and `E.24.PUB` keep the episteme, view membership, publication occurrence, publication form, and carrier distinct |
| `input`, `output`, `result`, `outcome`, `deliverable`, or `handoff` | name the participant and the relation actually claimed: method declaration, planned work, actual work, transformation, evaluation, commitment, delivery, acceptance, transfer, or receiving work. The source word is not a kind or universal slot. |

A declared post-state is part of a transformation description. An actual post-boundary state or changed entity is a fact about the subject. To call that entity or relation a result, name the later use, its participants, and the relation being asserted; acceptance, delivery, publication, and downstream effect remain separate. `U.Transformation` therefore has no generic `ResultRef` or `OutputConditionOrPortRefs` slot.

When the use needs an episteme about the transformation, identify it through C.2.1: exact claim content, the transformation or another subject as EntityOfConcern, and the effective reference scheme. Add scope, viewpoint, empirical grounding, edition, publication, or representation only when the use separately requires that relation.

#### A.3.4:4.5 - Neighboring Distinction Table

| Claim being made | Pattern to use |
| --- | --- |
| actual bounded transformation | `A.3.4 U.Transformation` |
| selected transformation-flow structure, locus, path, crossing, or flow valuation | `E.18`; A.3.4 still identifies each transformation occurrence |
| graph, algebra, morphism, path, tuple, or wiring expression | `E.18.2` and `C.29` as representation, not actuality |
| semantic way of doing | `A.3.1 U.Method` |
| description of a way of doing | `A.3.2 U.MethodDescription` |
| state-space and transition-law episteme | `A.3.3 U.Dynamics` |
| reusable operation declaration or application binding | `A.6.1` |
| planned or dated work | `A.15.2 U.WorkPlan` or an `A.15.1` `U.Work` occurrence |
| positive temporal aspect or temporal-claim adequacy | `C.27.TA` or `C.27` |
| problem-to-work carry-through | `E.18.1`; it carries the identified objects and does not retype them |
| evidence, evaluation, assurance, gate, decision, source use, publication, delivery, acceptance, or transfer | use the pattern that defines that claim |

#### A.3.4:4.6 - Description And Publication Boundary

A method description, dynamics model, transformation diagram, transformation-flow structure description, dashboard, result record, source span, publication, or proof may describe a transformation or provide evidence for a use. It is not the transformation.

If the task is about the description, use `C.2.1`, `A.3.2`, `A.3.3`, `E.17`, `E.18`, or the applicable publication or source pattern. If the task is about the transformation, keep the description as a neighboring episteme or publication value.

#### A.3.4:4.7 - Formal Transformation And Project-World Realization

A morphism, constructive proof, or formal state transition can correspond to an actual transformation of a formal object within the selected formal substrate. The formula, morphism, or proof term is still its C.29 representation.

For a physical, clinical, organizational, architectural, documentary, or epistemic change, a formal expression may specify, predict, constrain, or compare the change but cannot make it actual. First identify the changed subject, boundary, and before/during/after facts. If a later claim says that dated `U.Work` caused, realized, or participated in that transformation, apply the three outcomes in `4.2.4`; return `missing-governor` when the named pair has neither an existing predicate nor a valid local compound basis. Do not infer realization, evidence, permission, acceptance, or a result relation from the formal construction.

#### A.3.4:4.8 - Multi-reading source phrase

Use this slice when one phrase seems to name method, mechanism, formal construction, work, evidence, and transformation at once:

> "The workflow algorithm transforms the emergency-stop specification, and the proof shows the new plant boundary is safe."

Keep these objects separate:

- the workflow or algorithm may designate a `U.Method` or `U.MethodDescription`;
- the proof is a claim-bearing episteme using a declared formal substrate;
- when claim content changes, the earlier specification episteme and the later specification episteme are distinct C.2.1 identities; `EpistemeEditionRelation` relates them only when its historical-continuation predicate obtains;
- dated editing or review is a `U.Work` occurrence admitted under `A.15.1`;
- edition succession alone establishes no transformation of one continuing episteme. Open A.3.4 only for a separately continuing subject—such as a selected `U.PresentationCarrier` under `E.24.PUB` or a claim-bearing constituent organization—after naming its boundary, before/during/after facts, and continuity rule; otherwise stop without a transformation claim;
- if revision `U.Work` first constitutes the later episteme, open a separate `A.15.PROD` first-existence question: name the exact `productIdentitySpecification` episteme, the named applicability predicate or filled local claim that applies it to the candidate basis, subject context, and boundary, the `identityClosingWork`, and the work-to-change and change-to-identity predicates or local compound claims. If that specification continues an earlier specification, state the separate C.2.1 `EpistemeEditionRelation` only when its historical-continuation predicate obtains; without that relation, treat it as a non-continuing replacement and evaluate its applicability independently. Return `missing-governor` for either named work/change pair whose basis is absent; the word *governed* cannot supply the link;
- a plant change, safety evaluation, assurance claim, gate decision, and publication are separate objects and relations.

If only the proposed wording and proof are available, do not assert a project-world plant transformation. Different claim content gives two epistemes; test their `EpistemeEditionRelation`. Assert an A.3.4 specification-side transformation only for a separately continuing carrier or constituent organization with its boundary, before/during/after facts, and continuity rule. If the question instead concerns the later episteme's first existence, use `A.15.PROD` and stop when either direct connection lacks a basis. The proof can support an assertion only through its evidence or derivation use; it does not prove its own project use.

