---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__006_solution.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:4 — Solution"
line_start: 7718
line_end: 7897
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

`U.Transformation` is the FPF ontic for one actual bounded change. Identify one occurrence from the smallest subject-side basis that distinguishes it:

1. **Changed referent.** Identify the exact entity, structure, episteme, characteristic-bearing referent, or formal object under its direct pattern.
2. **Extent and boundary.** State the exact temporal extent of the change, including only gaps admitted by its continuity rule, or the exact ordering boundary in a declared formal substrate.
3. **Boundary conditions.** State the conditions that delimit this change from adjacent persistence, work, or change occurrences.
4. **Actual change facts.** Recover exact characteristic-state facts and obtaining direct relations before, during, and after the boundary. These facts, not a verbal change label, establish what changed.
5. **Continuity or reidentification.** When internal variation, interruption, or composition can occur, state the governed rule under which this remains one transformation.

Here, **one** means one occurrence at the resolution, referent, extent, and boundary required by the current use. It does not mean elementary, atomic, indivisible, or partless. Later refinement or a future governed constructive-part claim can coexist with the present identification. Sampling or temporal subdivision alone establishes neither constructive transformation parthood nor absence of transformation parts.

Generic, possible, desired, intended, planned, predicted, modeled, asserted, and published change claims remain claim content of epistemes, methods, work plans, dynamics models, publications, or other use-side objects under their direct patterns. They identify no actual `U.Transformation` until the subject-side occurrence basis obtains. A formal transformation can be actual relative to an admitted formal substrate; its formula or proof term remains a C.29 representation of the independently recovered formal change.

**Mint vs reuse.** A.3.4 reuses the already admitted root U-kind and public name `U.Transformation` from E.24.UK. It introduces no additional U-kind: `componentTransformation` and `compositeTransformation` are local participant meanings for already individuated occurrences. `TransformationPartOfRelation` remains a provisional designator for a blocked derived relation-kind candidate; it has no admitted occurrence or `RelationSignature`, and durable name selection through F.18 opens only after E.24/E.24.UK admission. A.3.4 mints only the local well-formedness-constraint identifier `WF-A34-TPD-1`; that identifier is not an ontic, relation kind, declaration member, or occurrence.

#### A.3.4:4.2 - First-use transformation basis

Use these questions as a recognition aid, not as fields of a transformation record:

| Question | Exact object to recover | Stop condition |
| --- | --- | --- |
| What changed? | one exact governed referent | stop if only a label, file, diagram, or desired object is available |
| Across which boundary? | temporal extent or formal ordering boundary | stop if before and after are merely two unrelated observations |
| What actual facts differ? | direct relation occurrences and characteristic-state facts | stop if the only basis is a method, plan, trace, formula, or assertion |
| What delimits one occurrence? | boundary conditions and continuity or reidentification rule | split or leave identity unresolved when the rule does not cover the gap |
| Which later claim relies on this change? | exact receiving work or decision and its direct relation | add no neighboring object that the receiving use does not depend on |

**Worked first use.** For a reactor cooling loop, identify the exact loop state as the changed referent, the thermal-power step and stabilization interval as the temporal boundary, the measured temperature-profile facts before and after the boundary, and the operating conditions that delimit the episode. The revised operating method, control-law episteme, dated adjustment work, measurements, safety assessment, and release decision remain separate objects. None alone is the transformation.

##### A.3.4:4.2.1 - Ground proposed components and the whole-configuration change independently

Use `componentTransformation` and `compositeTransformation` only as participant meanings for exact already individuated `U.Transformation` occurrences. They are not additional U-kinds or fields of a composite record.

Identify every proposed component transformation and the proposed whole-configuration transformation independently through A.3.4:4.1. A sampled point, arbitrary subinterval, method step, work part, flow node, graph edge, trace segment, formula term, before-and-after image, shared changed referent, or temporal inclusion establishes neither transformation parthood nor that the selected transformation has no parts.

The neighboring general patterns do not silently supply the missing bridge. `A.22` can identify a selected structure whose relation organization changes; `C.27.TA` can identify temporal aspects; `A.14` and `C.13` govern structural mereology and a `Γ_m` construction trace. None of those results by itself states that one actual change contributes to another actual change, that several changed referents constitute the changed referent of another transformation, or that several transformations compose one transformation. A `Γ_m.sum` of entity parts establishes structural extensional identity under C.13; it does not make the resulting whole an actual bounded change or make changes of its inputs parts of that change.

Accordingly, one independently grounded change of an exact selected configuration may be retained as a configuration transformation under A.3.4:4.1. It is not thereby a composite transformation, and separately grounded mounting, wiring, or connection transformations are not thereby its components. Ground a composite transformation only after exact direct contribution and transformed-referent relations, their temporal and boundary compatibility governors, and one applicable subject composition and reidentification rule are all recoverable. If any of that basis is missing, retain the independently identified transformations and stop before composition or parthood.

A composition-grounded whole-level characteristic is not constitutive of composite-transformation identity. It becomes an additional A.1 recognition component only after the same exact composite is independently grounded under the preceding rule. Without that characteristic or the modal larger-assembly component, retain the grounded composite and stop only before A.1 classification; without the composition basis itself, stop earlier and assert no composite.

##### A.3.4:4.2.2 - Keep `TransformationPartOfRelation` at candidate status

`TransformationPartOfRelation(componentTransformation, compositeTransformation)` is a designator for a proposed derived relation-kind candidate, not an admitted FPF relation kind. A.3.4 supplies the subject-side question and a proposed settlement, but neither this pattern nor a predicate-shaped phrase admits the kind. Until one exact E.24/E.24.UK admission result is available, do not assert `TransformationPartOfRelation` occurrences and do not publish an A.6.0 `RelationSignature` for this candidate.

The present one-off transformation-parthood use does not pass A.6.RCD disposition 2. No exact direct pattern supplies actual-change contribution to another actual change or constitution of the whole changed referent by component changed referents; no exact temporal or boundary compatibility predicate and no subject composition rule or substrate are selected. A C.2.1 episteme may identify that blocked claim and its missing basis, but it may not assert a positive local compound transformation-parthood claim.

The proposed derived-kind settlement is therefore conditional and blocked:

| Settlement component | Candidate rule or current stop |
| --- | --- |
| component participant | one exact independently individuated `componentTransformation : U.Transformation` |
| composite participant | one exact independently individuated `compositeTransformation : U.Transformation`, available only after the composition basis in 4.2.1 is governed |
| proposed obtaining | if admitted later, the component's governed actual change contributes to the composite's actual change under exact named base facts; exact temporal, boundary, and transformed-referent compatibility predicates hold; and one selected composition and reidentification rule admits that contribution |
| proposed occurrence identity | one exact reusable definition states the proposed identity and recurrence semantics, including whether the same participant pair under another composition rule, substrate, or base-definition edition is the same occurrence; `A.6.REL` governs that occurrence-identity question, while `E.24` / `E.24.UK` decides only whether to admit the candidate kind against the settled definition |
| current disposition | missing-governor and missing-substrate blocker; no positive local compound transformation-parthood claim, classified occurrence, reusable definition, or admitted kind |
| admission stop | no reusable predicate-definition episteme has one truthful exact C.2.1 `EntityOfConcern`; no exact base-relation kinds and direct patterns govern actual-change contribution or changed-referent constitution; temporal and boundary compatibility governors, selected derivation substrate, base-definition dependencies, one occurrence-consuming receiver, occurrence identity, and an E.24/E.24.UK admission result are absent |
| failure boundary | temporal inclusion, co-occurrence, a shared referent, adjacency in a flow, a list of effects, an unresolved claim, or the candidate designator establishes neither composition, admission, nor an occurrence |

**Well-formedness constraint `WF-A34-TPD-1` — usable future transformation-parthood definition.** A future reusable predicate-definition episteme is usable here only when it names one truthful exact C.2.1 `EntityOfConcern`, the exact base-relation claims and direct governing patterns, derivation under a selected substrate, polarity, scope, time, applicability, dependencies and editions, positive and discriminating cases, the admissible receiving use, and a proposed occurrence-identity law governed by `A.6.REL`. When stable occurrence semantics are required, A.6.RCD routes the proposed settlement to E.24/E.24.UK and A.11; E.24/E.24.UK decides admission, while A.6.REL retains occurrence-identity authority. The definition remains distinct from the candidate kind and every occurrence. Until that basis exists, ordinary work retains the independently identified transformations and the exact blocker.

##### A.3.4:4.2.3 - Apply A.1 only to a governed composite transformation

Membership in `U.Transformation` supplies no holonhood. A.1 remains the authority for the constructive criterion; the table below maps its components to a transformation case without redefining them. Only an exact governed composite transformation may also be classified as `U.Holon`, and only when that same entity satisfies A.1. This is dual classification of one entity, not a relation occurrence and not admission of `U.Transformation` as a holon kind.

The unresolved transformation-parthood blocker supplies neither composite identity nor the exact admitted part-relation occurrences required by A.1. Positive A.1 classification therefore waits for a governed composite transformation, an admitted direct transformation-parthood kind, exact obtaining occurrences under it, and every other A.1 component. An independently identified configuration transformation may remain a valid `U.Transformation` while this positive classification is blocked.

| A.1 constructive component | Transformation-specific realization | Stop or failure boundary |
| --- | --- | --- |
| exact candidate | one already individuated `compositeTransformation` with exact changed referent, extent, boundary conditions, actual change facts, governed composition basis, and continuity or reidentification rule | a separately identified configuration transformation is not yet a composite by that fact; a task, method, plan, delta formula, trace, relation expression, or picture is not the candidate |
| exact constituents | two or more independently individuated `componentTransformation` occurrences whose exact contribution to this composite is governed | arbitrary time slices, concurrent changes, method steps, work parts, and representation nodes are not constituents |
| constructive part relations and assembly | exact obtaining transformation-parthood occurrences under an admitted direct kind, together with the governed contribution, compatibility, and composition facts | the candidate `TransformationPartOfRelation` name, a missing-governor note, temporal inclusion, common referent, or co-occurrence supplies no admitted occurrence |
| reidentification rule | one exact C.2.1 predicate-definition episteme whose `EntityOfConcern` is the composite transformation and whose claim admits declared constituent and boundary-condition variation while preserving that composite | a tuple, path label, trace, or diagram does not reidentify the actual change |
| composition-grounded whole-level characteristic | at least one exact characteristic of the composite whose value or state is produced or sustained by the declared composition and is not attributable to one component alone | this is an additional A.1 component, not a condition for identifying every transformation; an effect label or list of component effects does not supply it |
| possible participation in a larger constructive assembly | the composite's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed larger-assembly construction method or rule under which it could participate as a constituent while preserving identity | the method-or-rule episteme describes the construction and conditions; it does not create compatibility or possibility |

Whether those world-side facts satisfy or fail A.1 is independent of evidence availability. When a reusable recognition evaluation is current, A.6.1 governs the typed operation and actual bindings; its result is `true`, `false`, or `unknown`. `unknown` reports inability to determine satisfaction because evidence or a dependency is unavailable; it is not a state of the transformation.

An optional C.2.1 classification assertion may record the judgment about the exact composite and the already admitted `U.Holon` kind. The assertion creates none of the composite, components, part relations, reidentification rule, whole-level characteristic, compatibility facts, construction method or rule, larger-assembly possibility, or holonhood. Exact evidence and assurance relations support or warrant its claim content; G.11 governs assertion-edition currentness; receiving work decides whether to rely, decline, defer, or reopen. A.1 satisfaction, failure, or recognition-evaluation uncertainty supplies neither warrant for a B.2 whole-reidentification claim nor grounds for selecting B.2.

Stress the boundary before classifying:

- a pressure increase may be identified as one `U.Transformation` at the resolution needed by the current use; sampling or subdivision establishes neither constructive transformation parts nor absence of such parts;
- a switch transition may be treated as effectively instantaneous at the selected temporal resolution and identified as one `U.Transformation`; that resolution claim establishes neither indivisibility nor constructive parts;
- subintervals of continuous biological growth become component transformations only when each is independently identified; they compose one transformation only under exact direct contribution and compatibility governors plus an applicable composition and reidentification rule;
- a formal transformation can be actual under a selected formal substrate, while its formula, morphism, or proof term remains a C.29 representation and supplies no holonhood;
- mounting, wiring, connection, and whole-configuration changes may each be identified independently; without the exact transformation-composition basis they remain separate, and positive A.1 classification does not begin.

##### A.3.4:4.2.4 - Keep work and production claims outside transformation identity

Exact work may cause, realize, or participate in a transformation only through separately governed work-to-change facts; temporal overlap is insufficient. A post-state, work reference, verbal predicate, changed continuing entity, or classification of a composite transformation as `U.Holon` establishes none of production-work participation, entity-identity inception, or production completion. Recover each such claim from its exact work, work-part, subject-identity, completion-criterion, and direct effect facts under `A.15.PROD` and the direct subject patterns it invokes. A.3.4 contributes the independently identified actual transformations and no universal production relation.

#### A.3.4:4.3 - Keep six layers separate

For one exact transformation, keep these objects distinct:

| Layer | Exact object | Governing responsibility |
| --- | --- | --- |
| actual bounded change | one `U.Transformation` | A.3.4 identifies changed referent, extent, boundary conditions, actual change facts, and continuity |
| exact subject facts | obtaining relation occurrences and characteristic-state facts | each direct subject pattern governs participants, obtaining, and identity |
| reusable change semantics | one predicate-definition episteme when repeated use needs the same rule | A.3.4 or the direct subject pattern states how governed facts satisfy the predicate |
| transformation assertion | one C.2.1 episteme asserting that the transformation or base facts obtain | C.2.1 identifies claim content, exact EntityOfConcern, and effective reference scheme; scope and viewpoint remain neighboring relations |
| representation | formula, morphism, path, graph, diagram, trace, tuple, or state-plane expression | C.29 governs correspondence to independently recovered objects |
| evidence or evaluation result | an episteme used to support or evaluate the assertion | the measurement, evaluation, evidence, provenance, or assurance pattern governs that use |

A verbal predicate does not turn every obtaining relation occurrence into a transformation. Assignment, availability, installation, and temporal order can obtain without change. Conversely, one actual transformation may require several relation facts without being identical to any one of them.

Do not restore the old `transformationRelation` field. First use an already governed direct relation when it expresses the needed fact. Otherwise apply A.6.RCD: only a substrate-admitted compound over exact governed base facts can yield a local relation-bearing claim; if that basis is absent, return the exact missing-governor or missing-substrate blocker. Introduce a reusable predicate-definition episteme only for repeated semantics. A new durable relation kind needs its own obtaining and occurrence-identity law; do not insert a task, morphism, operation family, or predicate into one union-valued field.

#### A.3.4:4.4 - Recover neighboring objects only for the current claim

A neighboring object is not a slot of `U.Transformation`. State its exact relation to the transformation, changed referent, work, or receiving use only when that relation is current.

| Current neighboring claim | Exact owner and boundary |
| --- | --- |
| reusable semantic way of doing | `A.3.1` governs `U.Method`; method existence establishes no actual change |
| claim-bearing account of that way | `A.3.2` and C.2.1 govern `U.MethodDescription`; description establishes neither work nor change |
| typed operation arguments or results | A.6.1 governs the exact operation declaration and application binding; these are not generic transformation inputs or outputs |
| intended work | `A.15.2` governs `U.WorkPlan`; intention establishes no dated work or actual transformation |
| performed work | `A.15.1` governs dated Work occurrences admitted under `U.Work`; exact work-to-change facts are recovered under their direct governor, because temporal coincidence is insufficient |
| transformation-flow location or composition | `E.18` governs selected `TransformationFlowStructure`; a flow locus neither performs work nor makes a change actual |
| mathematical expression | `E.18.2` and `C.29` govern representation; a graph edge, morphism, or delta expression is not the world-side occurrence |
| dynamics model | `A.3.3` governs the episteme; prediction is not actuality or permission |
| evidence, measurement, evaluation, or assurance | the direct measurement, evaluation, evidence, provenance, or assurance pattern governs the exact support or judgment relation |
| description, view, publication, form, or carrier | C.2.1 and E.17/E.24.PUB keep the episteme, view membership, publication occurrence, publication form, and carrier distinct |
| `input`, `output`, `result`, `outcome`, `deliverable`, or `handoff` | recover the exact participant and direct relation to a method declaration, planned work, actual work, transformation, evaluation, commitment, delivery, acceptance, transfer, or receiving work; the word is not a kind or universal slot |

A declared post-state is part of transformation description. An actual post-boundary state or changed entity is a subject-side fact. Treating that entity or relation as a result requires an additional exact receiving-use relation; acceptance, delivery, publication, and downstream effect remain separate. A transformation therefore has no generic `ResultRef` or `OutputConditionOrPortRefs` slot.

When an episteme about the transformation is current, identify it normally through C.2.1: exact claim content, the transformation or another exact subject as EntityOfConcern, and the effective reference scheme. Add claim scope, viewpoint, empirical grounding, edition, publication, or representation only through the direct neighboring relation required by the use.

#### A.3.4:4.5 - Neighboring Distinction Table

| Current claim | Governing pattern |
| --- | --- |
| actual bounded transformation | `A.3.4 U.Transformation` |
| selected transformation-flow structure, locus, path, crossing, or flow valuation | `E.18`; A.3.4 still governs each exact transformation occurrence |
| graph, algebra, morphism, path, tuple, or wiring expression | `E.18.2` and `C.29` as representation, not actuality |
| semantic way of doing | `A.3.1 U.Method` |
| description of a way of doing | `A.3.2 U.MethodDescription` |
| state-space and transition-law episteme | `A.3.3 U.Dynamics` |
| reusable operation declaration or application binding | `A.6.1` |
| planned or dated work | `A.15.2 U.WorkPlan` or an `A.15.1` Work occurrence admitted under `U.Work` |
| positive temporal aspect or temporal-claim adequacy | `C.27.TA` or `C.27` |
| problem-to-work carry-through | `E.18.1`; it carries exact objects and does not retype them |
| evidence, evaluation, assurance, gate, decision, source use, publication, delivery, acceptance, or transfer | the direct pattern governing that exact claim |

#### A.3.4:4.6 - Description And Publication Boundary

A method description, dynamics model, transformation diagram, transformation-flow structure description, dashboard, result record, source span, publication, or proof may describe a transformation or provide evidence for a use. It is not the transformation.

If the description itself is under concern, use `C.2.1`, `A.3.2`, `A.3.3`, `E.17`, `E.18`, or the direct publication or source pattern. If the transformation is under concern, keep the description as a neighboring episteme or publication value.

#### A.3.4:4.7 - Formal Transformation And Project-World Realization

A morphism, constructive proof, or formal state transition can correspond to an actual transformation of a governed formal object under the selected formal substrate. The formula, morphism, or proof term is still its C.29 representation.

For a physical, clinical, organizational, architectural, documentary, or epistemic change, a formal expression may specify, predict, constrain, or compare the transformation. Project-world actuality additionally needs the exact changed referent, boundary, subject facts, and, when work is claimed, dated work plus governed work-to-change facts. Do not infer realization, evidence, permission, acceptance, or a result relation from the formal construction.

#### A.3.4:4.8 - Multi-reading source phrase

Use this slice when one phrase seems to name method, mechanism, formal construction, work, evidence, and transformation at once:

> "The workflow algorithm transforms the emergency-stop specification, and the proof shows the new plant boundary is safe."

Recover separate objects:

- the workflow or algorithm may designate a `U.Method` or `U.MethodDescription`;
- the proof is a claim-bearing episteme using a declared formal substrate;
- when claim content changes, the earlier specification episteme and the later specification episteme are distinct C.2.1 identities; `EpistemeEditionRelation` relates them only when its historical-continuation predicate obtains;
- dated editing or review is a Work individual admitted under `U.Work`;
- edition succession alone establishes no actual transformation of one continuing episteme. An A.3.4 specification-side transformation requires one exact already-existing continuing referent governed under its direct pattern—such as a selected `U.PresentationCarrier` under E.24.PUB or a separately governed claim-bearing constituent organization—plus the exact boundary, actual before/during/after facts, and continuity or reidentification rule; if that basis is absent, stop without the transformation claim;
- when revision work first constitutes the later episteme, treat that first existence as a separate A.15.PROD entity-identity-inception question. Require the exact `productIdentitySpecificationEdition`, its direct subject-governed applicability basis, exact `identityClosingWork`, governed work-to-change and change-to-identity links, and the earliest satisfying boundary; otherwise return the exact missing-governor or missing-basis blocker;
- a plant change, safety evaluation, assurance claim, gate decision, and publication are separate objects and relations.

If only the proposed wording and proof are available, do not assert a project-world plant transformation. When the specification claims differ, identify the earlier and later epistemes separately and test the exact `EpistemeEditionRelation`; distinct episteme succession is not an actual transformation of one episteme. Assert an A.3.4 specification-side transformation only for a separately governed continuing referent with the required boundary, facts, and continuity basis. If the receiving use instead asks when revision work first constituted the later episteme, route that claim separately through A.15.PROD and stop when its direct basis is absent. The proof can support an exact assertion only through its direct evidence or derivation use; it does not prove its own project use.

