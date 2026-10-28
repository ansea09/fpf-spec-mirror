---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__006_archetypal-grounding.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:5 — Archetypal Grounding"
line_start: 19418
line_end: 19475
dependencies:
  - "A.10"
  - "A.22.CGUS"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "B.3"
  - "C.2.8"
  - "C.29"
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

### A.6.3.NAR:5 - Archetypal Grounding

Tell: NAR turns selected source structure into a reader-useful sequence while keeping ordering, loss, unsupported strengthening, and source return visible. It is not a general story-writing pattern.

#### A.6.3.NAR:5.1 - Scientific mechanism narrative

A chemistry paper has calculations, candidate mechanisms, failed synthesis attempts and unresolved tension between theory and experiment. If the sources establish the discovery history, an internal explanation can follow it: failed attempts, structural clue, revised mechanism, new experiment, remaining uncertainty. Its note identifies the preserved claims and deferred calculations; any connective added to explain the sequence is distinguished from a source assertion. A mechanism-proof question returns to the calculations and experiment record.

When a receiving use needs exact preservation of this account, identify source episteme `ChemistryMechanism-X` and narrative episteme `ChemistryDiscovery-Y` about the same reaction case. `DiscoveryNarrativization : X -> Y` states the selection, scheme relation, discovery order, preserved and lost claims, any grounded proof-use exclusion, and source return. The calculation files express source content; the paper form and carrier express the narrative. Their file labels alone identify neither episteme.

#### A.6.3.NAR:5.2 - Architecture trade-off narrative

An architecture team needs to explain a candidate selection. It can order the account by the binding constraint, compared alternatives, decision and remaining trade-off. Preserve the decision's stated basis rather than inventing the sequence by which the team discovered it.

**Source fixture.** `For project system S, data must be processed at Plant P. Under the same workload W, candidate C1 processes at P with a measured median latency of 40 ms; C2 processes at regional site R outside P with a measured median latency of 30 ms. Decision D selects C1 because the placement constraint is mandatory. D does not authorize implementation.`

**Narrative.** `Decision D selects C1 because it processes S's data at Plant P, as the mandatory placement constraint requires. C2 processes at regional site R outside P, which would violate the mandatory placement constraint. Under W, its measured median latency was 30 ms, 10 ms lower than C1's 40 ms. D does not authorize implementation.`

**Comparison.** The narrative foregrounds the constraint before the performance trade-off. It preserves both candidates, sites, workload, measured characteristic and decision basis; the 10 ms difference follows from the two comparable medians. It asserts no discovery history or actual implementation. This short fixture omits no source claim. For a changed workload or placement rule, return to the measurement and decision basis before carrying the selection forward.

When the receiver needs exact claim identity, `ArchitectureTradeoff-X` and `ArchitectureRationale-Y` concern the same project system, and `ArchitectureRationaleNarrativization : X -> Y` states the construction and return. Independently identified A.22 candidate structures are designated by the source claims. The posture is prospective during choice and retrospective when recounting the decision; publication, decision, synthesis and performed Work remain separate.

##### A.6.3.NAR:5.2.1 - Architecture narrative repair after source change

Later, a rejected candidate gains a new measurement basis and a placement constraint changes. The old story remains coherent but no longer preserves the live candidate set. Lower it to historical orientation, update the selected structures and ordering, state the changed loss and residual, and restore return to the current architecture description or decision material. In an exact case, reidentify only source epistemes whose C.2.1 identity changed, and restate the affected construction `n` under A.6.3.

C.33 carries captured and lost architecture-relevant structures: preserve the old rejected-candidate relation as history, capture the new candidate-set relation, and mark the obsolete measurement basis lost for current decision use. C.34 carries only a correspondence that actually remains. Implementation or decision use stays non-admissible until the exact architecture claim, decision result, or synthesis result and any required use relation are current.

#### A.6.3.NAR:5.2.2 - Live unfolding event narrative

A commentator narrates a football match while it unfolds. The ordinary narrative selects score state, possession changes, tactical shape, player roles and positions, momentum, and uncertainty, then uses event and tension order for live orientation. Here *player roles* is ordinary football language for tactical contribution and behaviour—such as pressing, covering, marking, playmaking, or providing width—not an asserted FPF system-role kind or assignment. The narrative does not turn provisional interpretation into settled event evidence.

Later analysis, statistics, rule disputes, injuries or official-result use returns to the event record and official sources. When replay or dispute depends on exact claim identity, identify event-record episteme `MatchState-X`, commentary episteme `LiveNarrative-Y` and their construction `LiveNarrativization`. The match is the concern, source claims describe its events, and audio expresses the narrative through its form and carrier.

#### A.6.3.NAR:5.3 - FPF seminar-route boundary

A team orders selected FPF claims for learners: EntityOfConcern discipline, problem frames, pattern use, relation records, source return, framework authoring, and improvement loops. The first result is a teachable route whose note records prerequisite order, deferred detail, reconstruction tasks, and return to exact FPF passages.

Teaching these claims does not establish that FPF is correct. A separate E.24.PUB occurrence may make a selected narrative episteme available through a teaching form and carrier; publication neither constitutes the narrative episteme nor establishes the NAR construction.

#### A.6.3.NAR:5.4 - Franchise-continuation storycraft boundary

A storycraft team develops a proposed continuation using canon constraints, premise, theme, character agency, causal plot structure, viewpoint and stakes. The new events come from that story construction. NAR then orders the proposed events and relevant canon claims into a readable account, making selection, foregrounding, loss and source return explicit.

For an exact same-entity continuity account, identify the source episteme describing the proposed continuation and any additional canon-source epistemes, then identify `ContinuationNarrative-Y` about that same continuation. The construction states how its assertions follow from those sources. Canon alone does not supply newly invented events. Canon classification, story generation, rights, publication and narrative-quality evaluation remain separately governed. G.2 applies to SoTA source-pack synthesis and C.35 to generated results intended to inform architecturing, only when those uses are current.

#### A.6.3.NAR:5.5 - Homotopy-theory explanation boundary

A teacher turns graph-heavy mathematical material into a didactic sequence of definitions, dependencies, examples, counterexamples, theorem prerequisites, and proof-status boundaries. The ordinary note records which structures a learner can reconstruct, which proof details or generalizations are deferred, and when to return to formal statements. Recalling an analogy alone does not establish a proof or recovery of the mathematical structure being taught.

When a mathematical use needs exact preservation, identify `HomotopySource-X` and `HomotopyNarrative-Y` about the same mathematical EntityOfConcern and state the construction, ordering and loss. Mathematical-lens, proof, source-use, publication and teaching-evaluation claims retain their applicable tests.

#### A.6.3.NAR:5.6 - Automated event-graph narrative

An LLM or NLG system uses source claims designating an event graph, agent goals, constraints, and a domain schema, then performs generation Work and proposes the resulting story-scene carrier. The first inspection compares the proposed sequence with the selected event relations, marks preserved constraints, omissions, and hallucinated connective claims, and limits use to candidate review.

Generated prose is not an admitted narrative episteme merely because it is fluent. Use C.35 when the generated result is intended to inform architecturing; it tests that exact result's next architecture use. If reliance-facing use later opens exact NAR, independently identify `EventPlan-X` and `StoryScene-Y`, then state `EventNarrativization : EventPlan-X -> StoryScene-Y`, the additional source dependencies, loss, prohibited strengthening, and return. The graph and schema are not `X`; the system's generation Work, evidence, assurance, and publication remain separate.

