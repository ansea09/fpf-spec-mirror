---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__005_solution.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:4 — Solution"
line_start: 69847
line_end: 70008
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.1"
  - "E.11"
  - "E.11.DSG"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.17"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4:4 - Solution

Describe an FPF-grounded pattern ecosystem as a family of framework editions and publication and access-facing presentation carriers, plus access routes, over selected structures. For each durable ecosystem-architecture claim, or technical claim on which later work will rely, state the exact subject and relation and cite the defining or constraining ClaimGraph in its subject pattern. The smallest route below needs no ClaimGraph citation when ordinary guidance or an honest stop already answers the question. A principle framework edition is not merely a bundle of documents, an ontology catalogue, a literature survey, or a guide to talking about a domain. Its pattern language renders a selected architecture of recurring problem situations, forces, known failure modes, reusable SoTA solution moves, consequences, cases, relation records, evaluation methods, and refresh conditions for a declared reader and use. Known failure modes include beginner mistakes and experienced-practitioner failures caused by stale, local-only, or non-SoTA practice.

Start with the smallest route that answers the current question:

1. Name the concrete ecosystem question and who needs the answer.
2. Classify the likely case: a framework-family boundary, an adjacent result or service, a publication carrier, access-facing presentation carrier, or access route, a DPF-suite question, or another relation already handled by a direct pattern.

3. Point to that direct pattern and state the next useful move, or stop with the exact missing distinction.
4. Open the complete ecosystem-architecture record only when the answer must persist as ecosystem architecture or later work must rely on the selected structures and relations.

This route is ordinary guidance, not a new record or package. A direct pattern or honest stop is a complete first result when no durable ecosystem-architecture record is needed.

Create an ecosystem-architecture record only when that durable architecture or later reliance is current. Use these fields:
```text
FPFEcosystemArchitectureRecord@Context:
  ecosystemScopeRef
  intendedArchitectureUse
  claimScopeRef?
  sourceRefs?
  patternHostRefs?
  selectedArchitectureStructureRefs?
  publicationRelationRefs?
  boundedModelUseStructureRef?
  frameworkFamilyMembers
  selectedPatternSetRefs
  selectedProblemSituationStructureRefs
  selectedKnownFailureModeRefs
  selectedSoTASolutionMoveRefs
  selectedSolutionMoveStructureRefs
  selectedRelationRecordRefs
  frameworkCarrierRenderingRefs
  selectedDependencyAndEditionRefs
  selectedPublicationOrAccessCarrierRefs
  selectedSourcePackRefs
  selectedDecisionRefs
  qualityAndImprovementRefs
  currentnessAndRefreshRefs
  blockedOverreadRefs?
  dependentUsePatternLocators
```

This record answers the declared ecosystem question for its intended use. Include `blockedOverreadRefs` only when `F.19`'s grounded-contribution test admits them; otherwise omit the field. The record is not a new root kind or a source of semantic locality, and the subject claims and patterns it cites remain its content sources.

Classify the family members as follows:

`Conceptual Core` is the legacy authority and publication-family partition. `First Principles Framework edition` is the whole scoped FPF framework edition as a transdisciplinary first-principles framework. `FPF Core pattern set` is the framework-edition view of the general FPF Core used for dependency, relation, and edition reasoning. These are related views and scopes, not competing core objects.

| Family member | Architecture contribution | Authoritative content loci |
| --- | --- | --- |
| Conceptual Core | Core FPF distinctions, rules, and patterns that other FPF-grounded frameworks depend on. | `E.4`, `E.5.3`, and the exact subject patterns containing the defining ClaimGraphs |
| Tooling Reference | Optional tools, schemas, scripts, machine checks, or helper publications that inspect or support FPF use. | Use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, and relevant tool patterns for their declared tool functions; use `G.5` only for a selector-facing selected-tool-set result declaration. |
| Pedagogical Companion | Tutorials, playbooks, worked examples, and learning material that teach FPF without changing Core meaning. | `E.17`, didactic patterns |
| Foundational principle pattern set | Foundational threshold material or principle patterns that may support FPF-grounded use but need settled names and dependency boundaries. | `F.18`, `E.4.PFR` |
| First Principles Framework edition | The scoped FPF framework edition as a transdisciplinary first-principles framework with Core pattern set, publication and access-facing presentation carriers, access routes, relation records, and whole-FPF adequacy route. | `E.4.FPF`, `E.2.DA`, `E.4.PFR`, `E.11`, `E.17`, `G.11` |
| FPF Core pattern set | The current general FPF pattern core as a framework edition. | `E.4`, `E.5.3`, and the current Core subject-pattern descriptions and defining ClaimGraphs |
| Domain principle framework | A domain-bounded framework grounded in FPF and in domain SoTA. | `E.4.DPF`, `G.2`, `E.4.PFAD`, `E.4.PFR` |
| Local practice framework | A framework for one bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—grounded in FPF and often in a domain framework. Add a local system-role kind, a separate System-classification judgment, or an exact assignment occurrence only when the framework claim independently uses it; recover ambiguous *role* wording through `E.10.ROLE`. | `E.4.DPF`, `E.4.PFAD`, `E.4.PFR`, `G.11` |

#### E.4:4.1 - Place support units and adjacent products deliberately

In this pattern, *product* is Plain management wording for a deliberately identified result or service boundary. It helps a team state intended use, identity or current state, access, later change and retirement rules, and any maintenance that actually obtains. It is not one FPF technical kind and it creates no `U.Product`. Before making a product-boundary claim, name the direct subject—the thing the claim is about—and the relation that carries its identity, edition, current state, provision, publication, availability, or maintenance. The subject may be, for example, a framework-edition episteme, an evidence-package episteme, an admitted System, an admitted service arrangement, a Method, a programme-description episteme, or another result already admitted by its subject pattern. Constitution or publication establishes only the claims made by those acts; maintenance and future Work need their own evidence. If the direct kind or relation is not settled, keep the management boundary as a proposal and return that question instead of inventing a common object kind.


A framework edition is an episteme. Treat its Readme, Preface, table of contents, pattern-body collection, framework-scale structure or coverage account, relation or edition note, and refresh route as named publication units in the same managed boundary when they share the edition's declared readers and use, edition boundary, access, and change rule. Being outside the pattern set or in another file does not by itself create another product or a maintenance claim.


Make a separate adjacent product only when people need to change, cite, or use its direct subject independently. Look for an independently useful identity, edition or current state, named users and use, an intensional rule for what belongs, access, a later-review or retirement rule, or cross-framework reuse or reliance. A separately established maintenance relation may also matter, but product identity does not require it. For example, a registry, MethodDescription collection, decision-support publication, inquiry evidence package, practitioner guide, pedagogical companion, catalogue, tool reference, access service, or inquiry programme may justify a separate boundary. The label does not settle the kind: a guide or evidence package may be an editioned episteme; a tool reference may identify an episteme, a tool System, or both; and an access service needs its own service and provider-System claims. The list is open, and file location does not decide the boundary.


When the direct subject is independently used or changed, keep it separate and point from the framework to its edition or current state. An annex may carry a declared snapshot or projection, but it returns to the authoritative subject and does not fork it. When no independent boundary is useful and ordinary framework use needs the material, keep it as a named support publication unit of the framework edition.


One presentation carrier may expose several managed products without merging their direct subjects. Each constituent keeps its own identity, edition or state, form, access, later-change and retirement rules, and any separately established maintenance relation; the outer navigation names the constituents and stays neutral. A result reused by several DPFs may therefore be managed as an ecosystem companion or service product. Shared use does not make it a parent DPF. Open another DPF only when its own field-boundary assessment finds recurring practitioner problems, constructive Methods, an independently useful first cut, evidence practice, and its own edition and change boundary.


When *programme* is used, start with what actually continues. An inquiry programme may be managed as a continuing programme or service product, but neither label says what persists. If a subject pattern admits the programme as a System or another exact arrangement, name it. Otherwise name the current programme-description episteme, capable provider and maintaining Systems with their accepted commitments, and any admitted service state. Bounded inquiry projects remain separate Work occurrences, and their results remain separate epistemes. A maintained inquiry evidence package is its own editioned episteme. The management boundary may coordinate these subjects and relations, but it does not turn them into one indefinitely continuing `U.Work` or one generic Product. If the persisting arrangement is still unclear, return that exact architecture question.

DRRs, build manifests, quality runs, digests, logs, and campaign state remain development or process evidence by default. They become reader products only when a selected public use gives a direct subject its own product identity and publication or availability route.


Use these tests in order: name the intended managed boundary and ordinary use; identify every direct subject, its kind, and the identity or current-state relation used by the decision; group only publication units that share the framework edition, readers, access, and change rule; test a proposed adjacent subject for independent use and change; select the smallest useful boundary; then record pointers, snapshot return, and neutral-carrier navigation. Establish maintenance only when a maintained claim is made. If a needed kind or relation remains unresolved, record that question and stop short of the technical product claim.


#### E.4:4.2 - Keep several DPF products usable as one suite

Use this branch when separately constituted DPF product series contribute to one ecosystem and people need to recover which product series belong to the Suite and how to use their current or historical editions. Keep distinct each continuing DPF product series, any separately constituted DPF Suite Reference product series, the continuing DPF Suite collection, and any as-of description of that collection. This introduces no `U.Product`, `U.DPFSuite`, or `U.DPFSuiteReference` kind.


Here *DPF product series* is Plain relation-defined wording for a continuing collection of a DPF's edition epistemes. The series begins when a product-constitution decision names at least one existing edition, intended readers and use, a content-selection and edition-admission rule, a reidentification rule, and later-review and retirement conditions. The decision's effect begins the collection and admits the first edition. A separate publication occurrence may make that edition available. A maintaining System, maintenance commitment, revision duty, another edition, or continued availability requires a separate claim. The decision Work and record are not the product series or the belongs-to occurrence.


Say **“this edition belongs to this product series.”** A later edition joins only when its `EpistemeEditionRelation` to the actual source edition obtains, the product-series rule still holds, and an admission decision takes effect. The edition relation establishes episteme continuity but does not admit the edition to the product series. A parallel branch, fork, translation, or derivative joins only when both its source relation and the admission rule pass. Otherwise it remains a related episteme outside the series or begins another product series. The series need not be one total version order.

An admitted edition continues to belong historically when it becomes superseded, unavailable, non-current, or retired while the same product series continues. Those states do not end the occurrence. If the product series ends or its identity rule identifies another product series, belonging to the old series ends and remains a past fact. Another product series must admit the edition through its own decision and a new occurrence. If review shows that the edition never satisfied the admission rule, correct the false claim; no valid occurrence existed. Do not remove and re-admit the same edition merely because availability or currentness changed. The same edition and continuing product series keep one occurrence rather than starting another.

A **DPF Suite** is a continuing collection of DPF product series. A separately constituted DPF Suite Reference product series can also belong after its own inclusion decision. The Suite rule states which product series may belong; individual editions do not. The Suite begins when a constitution decision identifies the ecosystem purpose and intended use, inclusion and removal rules, a reidentification rule, later-review and retirement conditions, and includes at least one actual DPF product series. Any maintenance relation or future maintenance Work must be established separately. The decision Work and record remain distinct from the Suite and the first inclusion occurrence.


The same Suite continues while its ecosystem purpose, rule for which product series may belong, inclusion and removal rules, and identity conditions remain within the declared evolution rule. Adding or removing a product series normally preserves it. Starting, changing, transferring, or ending a maintenance arrangement does not by itself reidentify the Suite. Changing a DPF or Reference edition, publication, availability fact, Reference answer, or configuration description does not by itself reidentify the Suite. Changing an identity anchor outside the rule identifies another Suite.


After constitution, a temporary one-product-series or empty state can preserve the same Suite only when an explicit decision keeps those anchors in force and names a restoration, review, or retirement condition. Present no current cross-DPF answer in that state. An end or retirement decision closes the continuing collection and ends every current belongs-to occurrence; separate removals are unnecessary. The Suite and the past facts remain identifiable, but later active use requires another constitution decision, another Suite, and new inclusions. Before constitution there is only a possible-future Suite.

Say **“this product series belongs to this DPF Suite.”** The relation begins when the product series satisfies the operative inclusion rule and an inclusion decision takes effect. It remains current while the same product series and Suite continue and no later removal decision has taken effect. While they continue, only an effective inclusion or removal changes that occurrence. If either collection ends, or its identity rule identifies another collection, belonging to the old collection ends; neither case requires a prior removal. A proposal, description, publication, locator, or common use may report the relation but does not make it obtain.

Loss of qualification does not silently change belonging. Show an action-changing warning and decide whether to repair qualification, remove the product series, change the Suite under its identity rule, or retire it. Until that decision, do not present the product series as qualifying, current for the defeated common use, or recommended on that basis. Restoration before removal keeps the same occurrence while the same product series and Suite continue. An effective removal ends it; a later inclusion begins another occurrence.

After an occurrence ends, say that the product **belonged** to the Suite and say when it ended; do not present past belonging as current. A reconstituted product series or Suite, or one reidentified under its rule, is another collection and needs a new inclusion decision and occurrence.

Belonging alone establishes neither parthood nor holonhood, and it does not make either impossible. The current product-series and Suite definitions leave A.1 matters 3, 5, and 6 unsettled: no constructive part relation and assembly, composition-grounded whole characteristic, or possible participation in a larger constructive assembly is currently established. Treat both as continuing collections without a present holon or parthood claim. If a later complete A.1 result and direct part predicate pass, state that additional claim separately. Belonging also settles no relation about order, dependency, compatibility, recommendation, publication, availability, currentness, maintenance, or use in an answer. One product series may belong to several Suites. Use the direct sentence without assurance fields unless the publication elects `B.3.5`; after election, use its `validationMode=axiomatic` and current `C.13 set`-trace obligations without treating the trace as the cause.

A DPF Suite Reference product series belongs to the Suite only after its own inclusion decision and keeps its own reader use, admission, reidentification, later-review, and retirement conditions. Any maintenance relation remains separate. The Reference may join after the first DPF products; it did not belong beforehand. Its absence, unavailability, staleness, or non-use does not erase the Suite or block direct use of a known DPF result. Those conditions only prevent a claim that the Reference currently supplies a trustworthy cross-DPF route.


For a reproducible as-of answer, use an optional **DPF Suite configuration description**: a `U.Episteme` about the Suite, the product series that belong at that time or in that scope, selected editions or states, and direct source return. Its own editions are description editions, never Suite editions. It describes neither the belongs-to occurrences into existence nor the Suite's identity.

Use `G.5 JointUseSet` only when every identified result or edition is necessary for one bounded use. A question may need resources from only some product series in the Suite. The set therefore neither defines Suite identity nor implies that every product is used together.

Present the Suite as current or available only while its direct currentness and availability facts support that statement and readers can return to the collection identity, inclusion and removal decisions, and any product-series state claimed as current. Present it as maintained only when a separate maintenance relation and its current evidence support that stronger statement. A neutral carrier or a current DPF Suite Reference edition may expose those returns, and an optional configuration description may pin them. None merges the Suite, Reference product series, Reference edition, DPF product series, DPF edition, carrier, access, maintenance, or currentness. Apply `E.17`, `E.24.PUB`, `C.2.P`, and `G.11` to their direct claims; use `E.4.PFR` only for a dependency or compatibility relation that separately obtains; and use `E.11.DSG` for the Reference's problem-led route and direct-DPF bypass.

The ordinary method is:

1. Declare the ecosystem scope and intended architecture use. Cite the exact source, pattern host, selected architecture structure, publication relation, or bounded model-use structure only when the record actually relies on it.
2. Name the family member being created, used, or changed.
3. List the selected structures that matter for the architecture claim: recurring problem-situation structures, known failure modes, reusable SoTA solution-move structures, pattern set, pattern-use relations, pattern-framework relations, decision records, dependency and edition records, publication and access-facing presentation carriers, access routes, source packs, quality records, and currentness records. For PF work, the pattern-language publication carrier exposes a reader-facing expression of that problem-and-solution architecture, not a neutral list of topics.
4. If the family member is FPF itself as a framework edition, open `E.4.FPF` for form, presentation carriers, access routes, and whole-FPF adequacy routing.
5. Apply `E.5.3`: dependencies point toward more stable framework editions. FPF Core does not depend on domain or local frameworks.
6. State publication and first-entry claims using `E.11` and `E.17`; state framework-carrier structure-account assertions using `E.4.FPF` for FPF itself or `E.4.DPF`/`E.4.DPF.DA` for domain and local frameworks.
7. State pattern-use recommendation claims using `E.11.PUR`.
8. When a framework-architecture question is open, record the selected answer in one `E.9` DRR and use `E.4.PFAD` to profile its framework-specific content. Use `C.32.PAD` only for an exact project architecture decision and `C.32.ADR` only to project such a decision into an ADR-like publication.
9. State relation, dependency, compatibility, deprecation, and edition claims using `E.4.PFR` only when its named maintenance use requires that representation; otherwise use the direct subject assertion.
10. Settle names using `F.18`.
11. State SoTA and source-use claims using `G.2`.
12. State currentness, refresh, and edition-change claims using `G.11`, the exact edition values, and their source/currentness assertions.
13. Before using an all-in-one carrier, table of contents, relation graph, summary, skill pack, MCP-backed service, or generated carrier as evidence, state the exact source-return or preservation assertion under the predicate defined in `C.33`, `C.34`, or `C.35`.
14. Evaluate whole-FPF adequacy through `E.2.DA`, DPF or local-framework package adequacy through `E.4.DPF.DA`, individual pattern quality through `E.21`, improve through `E.23`, and use `E.19` only when the local process asks for admission review.

Use this routing table when a proposed change is ambiguous:

| Proposed work | Route to | Decision boundary |
| --- | --- | --- |
| The form of FPF itself changes: README, Preface, ToC, monolith, host set, skill pack, MCP-backed access, or whole-FPF publication/access route. | `E.4.FPF`, with `E.2.DA` for whole-FPF adequacy and `E.4.PFR` for relation or edition records. | Do not treat FPF as a DPF, do not use `E.4.DPF.DA` for whole-FPF adequacy, and do not treat a carrier as the framework edition. |
| Accepted changes are being assembled into an FPF, DPF, or LPF publication, or continuity with a predecessor publication is claimed. | `E.4.PFIP` for the accepted-source and predecessor-preservation comparisons. | Require both PFIP conclusions when both claims are made. Source parity, build success, carrier continuity, and package adequacy answer narrower questions. |
| A distinction or rule is intended to constrain ordinary FPF use across many domains and downstream frameworks depend on it. | An accepted FPF Core amendment decision under `E.9`, followed by the exact subject patterns whose assertions change. | Do not promote a local checklist or domain technique to Core merely because it is useful. |
| A reusable principle supports FPF-grounded work but is not a general Core rule for all domains. | Foundational principle pattern set or other named framework edition, with `E.4.PFR` dependency records. | Do not hide a new framework edition inside the Core table of contents. |
| A source tradition or professional domain needs FPF-shaped patterns. | Domain principle framework through `E.4.DPF`, `G.2`, `E.4.PFAD`, and `E.4.PFR`. | Do not treat a literature summary as the framework. |
| One bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—needs guidance. | Local practice framework through `E.4.DPF`; keep local source, publication, quality, and refresh records, and state separately any direct relation used for maintenance, responsibility, authority, assignment, or contact. If a load-bearing owner label has no current direct relation, return `missing-governor` instead of inventing one. | Do not make local policy a general FPF rule. |
| Material needed for ordinary framework use shares the framework edition, readers, access, and change rule. | Keep it as a named support publication unit of that framework edition and expose it through the edition's carrier route. | Do not create another managed product merely because the unit is outside the pattern set or stored separately. |
| A registry, guide, evidence package, service, programme, or other result has an independently useful identity or state, users and use, content rule, access, or later-review and retirement rule. | Name its direct subject and the relevant relation, keep it as a separate product, and point to its edition or state; any embedded snapshot returns to that source. State maintenance only when it separately obtains. | Shared use, co-location, or one outer carrier does not merge direct subjects. If the kind is unresolved, keep the product proposed and return the question. |
| One carrier exposes several managed products. | Keep the outer carrier neutral and retain each direct subject's form, identity, access, change rule, and any separately established maintenance relation. Use `E.11.PFP` only for FPF, DPF, or LPF constituents. | Do not give a non-framework subject a framework family, dependency field, or pattern index. |
| Several DPF product series and a DPF Suite Reference product series are proposed for one ecosystem. | Use `E.4:4.2` to decide product-series and Suite constitution, which editions belong to which product series, which product series belong to the Suite, identity through change, later review and retirement, optional configuration description, and truthful exposure; state maintenance separately only when it obtains. Use `E.4.PFAD` when the answer must be selected. | A title, co-list, shared carrier, Reference entry, or configuration description creates none of those subjects or relations. |
| A registry, guide, evidence package, service, programme, or other result has an independently useful identity or state, users and use, content boundary, access, or maintenance and refresh boundary. | Name its direct subject and the relevant relation, keep a separate managed boundary, and point to the exact edition or state; any embedded snapshot returns to that authority. | Shared use, co-location, or one outer carrier does not merge direct subjects. If the kind is unresolved, keep the boundary proposed and return the question. |
| Existing material is hard to find, teach, or publish. | Use `E.11` for discovery, the relevant didactic pattern for teaching, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use `G.5` only when the missing value is a selected-set result declaration. | Do not call publication repair architecture repair. |
| A cross-reference claims use, specialization, dependency, publication, source reuse, preservation, quality, deprecation, or supersession. | `E.4.PFR` for the relation function and edition effect. | Do not let a link label decide the relation meaning. |
| A framework split, dependency boundary, presentation-carrier or access-route choice, or adoption consequence must be decided. | Record one selected answer in an `E.9` DRR, using `E.4.PFAD` for its framework-specific content. Use `C.32.PAD` only when the decision is an exact project architecture decision and `C.32.ADR` only for its ADR-like projection. | Do not replace the answer with a diagram, folder, manifest, PFAD relation, or project-specific decision pattern used as the default framework route. |
| A source, search result, transformed view, or generated carrier supplies candidate material. | `G.2`, `C.33`, `C.34`, or `C.35` before architecture use. | Do not treat a carrier as authoritative because it has plausible names. |
| Whole-FPF adequacy, DPF package adequacy, individual pattern quality, repeated improvement, admission gating, or currentness is the live problem. | `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23`, `E.19`, and `G.11` according to the claim. | Do not average pattern scores into package adequacy or whole-FPF adequacy, and do not run all quality gates when only one evaluation or refresh question is live. |

This pattern should leave the reader with one architecture sentence: "This framework edition belongs to this family member, expresses this selected architecture of recurring problems and solution moves in pattern-language form, depends on these stable editions, publishes or gives access through these carriers, preserves these selected structures, and states each neighboring claim under its exact predicate or constraint with the subject pattern available as a locator."

