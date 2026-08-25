---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
section_id: "E.17.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__005_solution.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "E.17.2 — TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
  - "E.17.2:4 — Solution"
line_start: 79410
line_end: 79555
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.6"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24.PUB"
  - "U.View"
  - "U.Viewpoint"
  - "U.ViewpointRef"
keywords:
---

### E.17.2:4 - Solution

**Local mantra.** To materialize a local instance, constitute L and bind `f_eng`, four exact references, and four exact P targets. To use an admitted instance, resolve L, its declaration, and only the needed reference. Then identify holon-centered candidate E and test E.17.0 conformance. For any additional engineering or publication claim, keep its objects and relations distinct and use the applicable pattern.

The mantra is a recall aid. The following sections specify the template positions, local materialization, conformance use, and stopping rules; none of their variables denotes a repository-shipped value.

#### E.17.2:4.1 - Bind one project-local declaration without embedding viewpoint values

One project instantiates the template only by supplying these exact bindings:

```text
L_local = catalogue episteme identified by <G_L, K_L, R_L>
f_eng   = ordinary family designator interpreted under R_L

local declaration claim block in G_L:
  familyDesignator = f_eng
  targetKindCompatibility = exact U.Holon target-kind criterion
  viewpointRefs = {
    r_functional,
    r_procedural,
    r_allocation,
    r_module
  }

resolve_R_L(r_functional) = P_functional
resolve_R_L(r_procedural) = P_procedural
resolve_R_L(r_allocation) = P_allocation
resolve_R_L(r_module) = P_module
```

The four `r_*` variables must be bound to exact local `U.ViewpointRef` values; the four `P_*` variables must be bound to exact already admitted viewpoint episteme editions. `f_eng` and any reader-facing names are ordinary designators under `R_L`. Designator, reference, viewpoint episteme, any optional selected viewpoint-convention structure, declaration claim block, and catalogue L remain distinct.

The template does not admit P as `U.Viewpoint`, make another episteme a `U.View`, or establish publication. Use E.17.0 for both dependent-kind membership tests, E.17.1 for L and its declaration claim block, and E.24.PUB for publication.

The four positions are fixed for a project declaration that claims conformance to this template. Safety, assurance, information, mission, deployment, business, and publication-oriented viewpoints use another local E.17.1 declaration or a later exact project catalogue edition with an explicitly revised declaration. A recurring label alone neither binds nor extends `f_eng`.

#### E.17.2:4.2 - Materialize each local viewpoint before binding its reference

Each `P_*` variable must be bound to one exact C.2.1 episteme that independently gains `U.Viewpoint` membership under E.17.0. Start with E.17.0's self-contained branch: give P its exact admitted target kind as EntityOfConcern and put the complete fixed target-kind, concern, admissibility, semantic-form, coverage, consistency, completeness, omission, and describing-use test in its ClaimGraph. Use the structured C/Q/S branch below only when separately versioned convention components and their organization change a named project reuse, comparison, or maintenance action.

For any one of the four positions:

1. identify the exact target kind and the complete self-contained P ClaimGraph;
2. apply the five E.17.0 viewpoint-membership conditions;
3. only in the independently triggered structured branch, identify exact convention epistemes under their least-powerful admitted kinds, construct exact collection C under C.13, recover every selected obtaining direct relation, state ordinary constraint episteme `Q_org`, let a system perform the A.22 selection work, and identify exact selected structure S;
4. bind the resulting exact P to its project-local reader designator and exact `U.ViewpointRef`; and
5. record the resolution under exact `R_L` in the local declaration claim block.

No constituent, `Q_org`, or P becomes a `U.Signature` merely to fit this template. A constituent is a `U.MethodDescription` only when it describes one independently admitted method under A.3.2. Exact selection work and its result remain separate from C, S, P, and selected relation occurrences. The structured-witness table below contains variables and optional recipes, not current repository values.

The four template positions use these exact concern objects and patterns when one project authors its P editions:

| Template position | Exact concern EntityOfConcern and applicable pattern |
|---|---|
| functional | exact `U.Transformation` under A.3.4; exact `U.Capability` under A.2.2; exact transformation-flow `U.Structure` under E.18 and A.22 |
| procedural | exact `U.Method` under A.3.1; exact transformation-flow `U.Structure` under E.18 and A.22; exact operational-state `U.Structure` under A.19.SPR and A.22 |
| allocation-responsibility | exact local system-role kind under A.2; when the view claims that one exact System counts under that kind, the separate C.3.2 judgment over candidate, kind, exact `KindSignature` edition, and context slice; an optional `KindExtension` representation only for a named set-consuming use; exact obtaining assignment occurrence under a directly declared `U.SystemRoleAssignment` species when an assignment claim is current; exact `SystemRoleKindRelationStructure` under A.2.7 and A.22; exact `U.Capability` under A.2.2; exact `U.Transformation` under A.3.4; an independently governed responsibility relation or selected structure when responsibility is current |
| module-interface | exact dependency `U.Structure` under B.1.1 and A.22; every module, interface, boundary, substitutability, or change-policy relation separately names its predicate, participants, obtaining test, and applicable pattern |
Keep these claim boundaries explicit:

- **Functional:** functioning status, input/output boundary, and functional-port coverage remain claims in `E_rule.functionalCoverage` unless the claim identifies a separate EntityOfConcern and states its exact predicate, participants, and obtaining test. The three concern epistemes stay separately about exact Transformation, exact Capability, and exact transformation-flow Structure; there is no universal function entity or one multi-subject concern episteme.
- **Procedural:** every method, order, state, concurrency, failure, and recovery claim designates its exact operational subject and the admitted method, state-transition, or transformation-flow relation that gives the claim meaning. A bounded coverage rule may remain in P, but a candidate E cannot satisfy it through vocabulary alone. Method mention grants no MethodDescription membership, state wording is not a Structure, procedural content is not performed work, and safety evidence is added only for a safety-bearing claim or named reliance.
- **Allocation-responsibility:** holder System, local system-role kind, four-input C.3.2 classification judgment, optional extension representation, assignment, transformer relation, allocation, segregation, capability, and responsibility remain separate typed claims or concern objects. A local system-role kind is not a classification judgment or assignment; classification or assignment establishes neither responsibility nor Work; and a selected structure performs no Work.
- **Module-interface:** A.6.M `ModuleInterfaceClaim` remains claim content. Whole-holon, candidate-module, boundary, independently identified `InterfaceSpecification` episteme and its resolving reference, substitutability, and change-policy content stays in the coverage-rule episteme until an exact module-relation declaration supplies participant kinds, predicate, obtaining rule, and occurrence identity and current facts satisfy it. The claim record is not that relation and a module topic is not an EntityOfConcern.

Split any phrase spanning several exact subjects into separate concern epistemes, or retain it as one constraint claim over candidate content. Give each stakeholder constituent exactly one referent—exact System, local system-role kind, claim-bearing C.3.2 classification-assertion episteme when that judgment is current, exact obtaining system-role assignment, C.13 collection-as-whole, or other independently governed subject. A `KindExtension` remains an optional representation for a named set-consuming use, not the kind or judgment. Cite any responsibility concern through its separately governed direct predicate. Do not coerce heterogeneous constituents into Signatures merely to make the rows uniform.



The following four rows are structured-branch recipes. Every symbol is a template variable until a project binds exact values; an ordinary self-contained P does not materialize this row.

| Exact project substrate after binding | Applied constraints, selected structure, and viewpoint episteme | Selected direct dependencies | Method and work boundary |
|---|---|---|---|
| `C_functional = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.functionalTransformation, E_concern.capability, E_concern.transformationFlowStructure, E_rule.functionalCoverage, E_rule.functionalModuleSeparation, E_rule.functionalRetargeting}` | `Q_org.functional` is an ordinary constraint episteme about C. A.22 selects `S_functional`; exact project `P_functional` has `EntityOfConcern=S_functional`, is assigned local reader designator `d_functional`, and passes E.17.0 viewpoint membership before `r_functional` is bound to it. | Each concern episteme depends on `E_target.tevbHolon`; `E_rule.functionalCoverage` depends on all three concern epistemes and `E_admitted.tevbEpisteme`; separation depends on functional-transformation concern; retargeting depends on the target. | No method constituent is required. A method convention enters only as exact `U.MethodDescription` after its method passes A.3.1. |
| `C_procedural = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.method, E_concern.transformationFlowStructure, E_concern.operationalStateStructure, E_rule.proceduralCoverage, E_rule.proceduralMethodBoundary, E_rule.proceduralNoWorkInference}` | `Q_org.procedural` is about C. A.22 selects `S_procedural`; exact project `P_procedural` has `EntityOfConcern=S_procedural`, is assigned local reader designator `d_procedural`, and passes E.17.0 membership before `r_procedural` is bound. | Each concern episteme depends on the target; coverage depends on all concerns and admitted-episteme kind; method boundary depends on method concern; no-work-inference depends on method and transformation-flow concerns. | Operational methods remain subjects of separate method-description epistemes. Concern selection, view construction, evaluation, and use do not form one method or workflow by mention. |
| `C_allocation = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.systemRoleKind, E_concern.systemRoleKindRelationStructure, E_concern.capability, E_concern.transformation, E_concern.responsibility, E_rule.allocationCoverage, E_rule.allocationNoWorkInference, E_rule.allocationRetargeting}`; add `E_concern.systemRoleClassification` only for an independently current four-input C.3.2 judgment, and add `E_concern.systemRoleAssignment` only for an independently current assignment claim | `Q_org.allocation` is about C. Use A.22 to select `S_allocation`; exact project `P_allocation` has `EntityOfConcern=S_allocation`, is assigned local reader designator `d_allocation`, and passes E.17.0 membership before `r_allocation` is bound. | Each current concern episteme depends on the target; coverage depends on all current concerns and the admitted-episteme kind; no-work-inference depends on whichever kind, classification, assignment, transformation, and responsibility concerns are current; retargeting depends on the target. | A bare *role* label, raw kind or relation reference, and raw Method are not collection members. Only exact current concern epistemes enter C. An allocation or analysis Method enters only through an exact MethodDescription episteme. The selected structure performs no Work. |
| `C_module = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.dependencyStructure, E_rule.moduleCoverage, E_rule.interfaceTyping, E_rule.functionalModuleSeparation, E_rule.substitutabilityChange, E_rule.moduleRetargeting}` | `Q_org.module` is about C. A.22 selects `S_module`; exact project `P_module` has `EntityOfConcern=S_module`, is assigned local reader designator `d_module`, and passes E.17.0 membership before `r_module` is bound. | Dependency-structure concern depends on the target; coverage depends on target, dependency structure, and admitted-episteme kind; typing, functional separation, and substitutability/change depend on dependency structure; retargeting depends on target and dependency structure. | No method, work, or module relation enters by mention. A direct module or interface relation joins only after its own pattern supplies participants, obtaining law, and occurrence identity. |

Each project-bound structured witness remains independently recoverable. Exact constituent editions identify C; every selected dependency occurrence passes the E.17.0 predicate; optional `D_dependencyUse` states obtaining and named-use admissibility as separate claims; and A.22 selects S from exact C, selected occurrences, applied Q constraints, and the use frame. Exact P is then identified by its ClaimGraph, S EntityOfConcern, and effective scheme. Changing only the Q edition leaves S unchanged when those selection inputs remain semantically unchanged. No topic list, citation, displayed edge, hidden O, D, template variable, or neighboring witness supplies another witness's closure.
The dependency relation in this table is exact `ViewpointConventionDependencyRelation` from E.17.0. It obtains only when interpreting or replaying the fixed claims of the dependent episteme relies on an exact criterion, law, public name, or method claim of the base episteme, and replacing the base edition can change that interpretation or replay. Co-membership, citation, or a visible arrow is insufficient.



When an A.22 selection judgment needs an explicit claim that one obtaining dependency occurrence is admissible for that use, identify the separate decision-use episteme described by E.17.0. Do not insert that decision, its evidence, or its evaluation result into the dependency relation or S identity.

#### E.17.2:4.3 - Keep the four concern conventions distinct

**Functional.** A conforming candidate episteme foregrounds exact transformations, capabilities, effects, functional elements, or transformation-flow relations of its holon. It does not identify a module structure by functional vocabulary and does not mint `U.Function`. Any neighboring responsibility claim keeps the admitted System, local system-role kind, current C.3.2 classification judgment, exact assignment, kind-relation structure, capability, transformation, and direct responsibility relation separate; use A.2, C.3.2, A.2.1, A.2.7, or the direct responsibility pattern for the claim actually made.

**Procedural.** A conforming candidate episteme foregrounds exact methods, order, state, concurrency, failure, and recovery related to its holon and designates the exact admitted method, state-transition, or transformation-flow relations on which each claim depends. A procedural view about a holon is not a `U.MethodDescription`; that dependent kind requires one admitted method as its exact EntityOfConcern. Ordinary operational recovery needs no safety package unless the claim is safety-bearing or a named receiving decision relies on one.

**Allocation-responsibility.** A conforming candidate episteme foregrounds exact Systems, local system-role kinds, current C.3.2 classification judgments, obtaining assignments, relations among those kinds, capabilities, transformations, and separately governed responsibility relations or selected structures related to its holon. A label creates no kind, classification, or assignment; a classification judgment needs its candidate, kind, `KindSignature` edition, and context slice but no assignment. The view may state that judgment, but it does not make the criterion true, create an assignment or responsibility relation, or perform Work.

**Module-interface.** A conforming candidate episteme foregrounds exact constituent holons, dependency structures, boundaries, interfaces, compatibility, substitutability, and change policy. It remains distinct from the functional viewpoint: many modules may support one transformation, one module may support several transformations, and either description may be incomplete without becoming the other.

The following are practitioner recognition and claim-shape cues, not embedded `StakeholderFamilies` or `AllowedEpistemeKinds` fields. A reader label creates neither a system-role classification nor an assignment and enters neither viewpoint nor view identity; every example still needs its exact EntityOfConcern, the predicate and participants of each claimed relation, its obtaining test, and its E.17.0 conformance result.

| Template position | Typical readers or concern holders | Distinctive claim-shape and conformance cues |
|---|---|---|
| functional | System-engineering and architecture readers, product or capability owners, and reliability or performance readers inspecting capability envelopes | Look for service-capability and promise content, delivery or access and API descriptions, input/output signatures, and functional-port boundaries as separate claims about the holon. Ground bounded behavior in exact transformations, capabilities, or a selected transformation-flow structure; keep service delivery Work, access relations, publications, and module interfaces separate, and do not mint `U.Function`. |
| procedural | Operations and run-time owners, control and automation engineers, and safety readers | Look for exact operational subjects and admitted method, state-transition, and transformation-flow relations behind order, state, concurrency, failure, and recovery claims. Where step boundaries are current, make preconditions and postconditions explicit and type-checked. Open an exact safety-analysis basis, A.10 evidence path, or B.3 assurance branch only when the current claim is safety-bearing or a named receiving decision relies on it; otherwise stop at the operational relations and ordinary failure/recovery boundary. Keep method, method description, work plan, dated Work, calendars, and selected state or flow structures distinct. |
| allocation-responsibility | Organization and operations designers, safety or compliance readers concerned with segregation of duties, and device or system engineers | Look for the admitted System and exact local system-role kind; when the claim says that System counts under the kind, recover the separate four-input C.3.2 judgment. Look separately for any assignment occurrence, segregation and escalation constraints, capability and transformation claims, and responsibility relation or structure. A kind locator is neither a classification result nor an assignment; none of those claims proves responsibility; allocation wording is not an obtaining relation; and no view or selected structure performs the allocated Work. |
| module-interface | Hardware or software architects, integration and test engineers, and lifecycle or maintenance readers concerned with replaceable units | Look for module decomposition, protocols, schemas, physical connectors, APIs, interface and conformance expectations, version and change policies, dependency and allowed-coupling structures, replaceability and variation points, and explicit functional-to-module correspondence or allocation without identity by default. Ports or connector diagrams do not establish module/interface relations; state and test each direct relation separately, and use A.6.4 for any functional-to-module retargeting. |

#### E.17.2:4.4 - Recognize holon-centered TEVB views by conformance

TEVB keeps two subjects explicit:

| Episteme | Exact EntityOfConcern | Job |
|---|---|---|
| viewpoint episteme P | exact admitted target kind in the self-contained branch; exact selected viewpoint-convention structure S only in a triggered structured branch | states the target-kind criterion, concerns, admitted episteme kinds, semantic-form, coverage, consistency, completeness, omission, and describing-use rules |
| candidate or view episteme E | one exact holon H admitted by P's target criterion | states claims about H; whenever it relates H to another engineering object, it names the exact predicate, participants, and obtaining test |

`EpistemeViewpointConformanceRelation(E,P)` must pass the fixed E.17.0 predicate. Only then is the same episteme E a `U.View`. Direct authoring, query execution, A.6.3 construction, a reader-facing label, declaration membership, or publication does not establish that membership. A reader-facing system-role label also establishes neither the local kind nor a C.3.2 classification judgment or assignment.

For one current describing use, its exact use qualification carries one singular `viewpointRef : U.ViewpointRef` resolving P under the effective reference scheme. Any reader-facing viewpoint name is only P's ordinary designator. The use qualification, designator, reference, and P remain distinct; selection identifies neither E nor H, establishes no conformance, and adds no conformance participant or episteme-identity field.

Recover exact H only as `EntityOfConcern(E)` from E's C.2.1 constitution. Do not import a legacy context tuple, generic bounded-context object, or model-use identity field into E, P, S, conformance, or selection. Another use may select another P while E remains unchanged; several selected viewpoints require an exact C.13 collection of their references rather than one overloaded reference.
If a user needs a view whose exact subject is a Method, local system-role kind, system-role assignment, transformation, responsibility relation, or structure rather than H, identify another candidate episteme with that EntityOfConcern and use a viewpoint whose target-kind criterion admits it. Do not silently retarget a holon-centered TEVB view.

#### E.17.2:4.5 - Import, subset, and extend one materialized local instance

An E.17.0 multi-view use can import TEVB only after it resolves one admitted project catalogue edition L, retrieves the declaration claim block designated by exact local `f_eng`, and resolves the exact imported `r_*` members or subset. Open `<G_L, K_L, R_L>` under E.17.1:4.2 only when L or the declaration is new, missing, or disputed, or a named later use consumes the catalogue constitution as premises. `f_eng` is only an ordinary designator inside L: it identifies neither L nor any viewpoint by itself and is not a member reference. Each imported reference resolves exact P under `R_L`; any reader-facing viewpoint name is only P's designator. A local subset names retained references, preserves `<editionDesignator(L), f_eng>` provenance, and records whether each omission is unused coverage or an intentional exclusion.

If local work changes only reader-facing aliases or adds examples, keep those as naming or annex content. If it changes a viewpoint's target criterion, concerns, admitted episteme kinds, or conformance rules, identify another viewpoint episteme edition and bind another exact reference as needed. If it changes family membership, identify another catalogue episteme or declaration claim block. Do not keep an old designator while changing the exact P it resolves under the same effective scheme.

Several local families may be used together, but each member retains its exact catalogue provenance and resolved viewpoint edition. Similar labels do not merge members. Two projects can claim use of the same reusable family only when they resolve the same exact L, declaration, and member references; independent instances of this template remain different local families even when all four labels match.

A project may bind its local four positions to reader names such as `Functional`, `Procedural`, `Allocation-Responsibility`, and `Module-Interface`. Those names do not perform the binding. A different reference-to-position mapping is another local declaration and must not silently reuse the earlier `f_eng` under `R_L`.

#### E.17.2:4.6 - Keep cross-view relations and publication separate

A materialized local TEVB instance provides four exact project references; the template alone provides none. Neither instance nor template asserts correspondence among resulting views. When a later engineering use depends on a relation between a functional claim and a module claim, or between a procedural claim and a system-role-assignment claim:

1. identify the exact participating entities or epistemes;
2. state the exact realization, allocation, dependency, consistency, trace, or other direct relation claimed;
3. use the concrete pattern that defines and tests that relation, including its obtaining law;
4. use A.6.RCD when no existing direct or derived relation is sufficient;
5. use C.29 only for a representation of the recovered relation.

If a separate receiving claim asserts dated `U.Work`, use A.15.1 to establish its performer, Method, time, and containing System, and F.6 to identify the assignment under which the performer acted. Those Work facts are neither participants in the cross-view relation nor prerequisites for identifying it.

E.17 and E.24.PUB may publish a selected TEVB view edition through three distinct relations: `PublicationFormExpressionRelation(selectedEdition,publicationForm,boundedUseDeclaration)`, `PublicationFormBearingRelation(presentationCarrier,publicationForm)`, and the five-participant `EpistemePublicationRelation(selectedEdition,audienceDeclaration,boundedUseDeclaration,publicationForm,presentationCarrier)`. Each retains its own participant set and maximal continuous obtaining interval; changing a participant or restoring availability after a gap yields another occurrence without reidentifying unchanged E or P.

Rendering, printing, upload, or carrier manipulation is separate system-performed `U.Work`. Use C.29 only when a representation corresponds to independently recovered objects or relations. A publication-side viewpoint, when current, is another exact viewpoint episteme selected by reference—not a TEVB position label reused as a form or file name. View episteme, viewpoint episteme, construction, conformance, form, carrier, publication, rendering, and representation remain distinct; publication and representation make no represented world-side relation obtain.

