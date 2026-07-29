---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__006_archetypal-grounding.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:5 — Archetypal Grounding"
line_start: 14603
line_end: 14658
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

### A.6.3.NAR:5 - Archetypal Grounding

Tell: `A.6.3.NAR` is the pattern for making an ordered narrative path from selected source structure while keeping the source-basis relation inspectable. It is not a pattern for writing a better story in general.

#### A.6.3.NAR:5.1 - Scientific mechanism narrative

A chemistry paper has calculations, candidate mechanisms, failed synthesis attempts, and an unresolved tension between theory and experiment. The narrative uses discovery order: failed attempts, structural clue, revised mechanism, new experiment, remaining uncertainty.

The NAR case records selected source structures `calculation set`, `mechanism candidates`, `experiment attempts`, and `unresolved tension`. It records preserved structure `candidate mechanism and failed-attempt relation`, foregrounded structure `discovery sequence`, lost structure `full calculation detail`, and source-basis return condition `return to the named calculation source basis before using the narrative for mechanism proof`.

This is not only conservative retextualization because ordering and tension carry the use. It is not proof because the narrative does not replace evidence.

#### A.6.3.NAR:5.2 - Architecture trade-off narrative

An architecture team explains why one candidate structure was selected. The source includes module structure, data custody, placement constraints, architecture characteristics, and rejected candidates.

The rendering mediation mode is architecture-mediated and prospective when the team is still choosing a future structure; it is retrospective when the team is reverse-engineering why an existing holon has the structure it has. The narrative follows tension order: current pain, candidate split, characteristic trade-off, rejected alternatives, selected structure, remaining residual. The NAR case records what structure the story preserves and which hidden structures remain non-admissible for implementation decisions until the architecture description, decision record, or synthesis governing pattern is reopened.

#### A.6.3.NAR:5.2.1 - Architecture narrative repair after source change

Later, one rejected candidate gains a new measurement basis and a placement constraint changes. The old narrative still tells a coherent tension story, but it no longer preserves the live candidate set. The repair is local: lower the old narrative to historical orientation, reopen the NAR case, replace the selected-source-structure refs and ordering rationale, and add a new source-basis or governing-pattern return condition pointing to the updated architecture description, decision record, or synthesis governing pattern.

The captured and lost structures move to `C.33`: old rejected-candidate relation preserved as history, new candidate-set relation captured, and obsolete measurement basis marked lost for current decision use. `C.34` may carry only the weakened correspondence that remains between the old narrative and the updated source. Implementation or decision use stays non-admissible until the architecture description, decision record, or synthesis governing pattern is repaired.

#### A.6.3.NAR:5.2.2 - Live unfolding event narrative

A commentator narrates a football match while the source event is still unfolding. The rendering mediation mode is direct source-structure and live. The selected source structures include score state, possession changes, tactical shape, player roles, momentum, and uncertainty about what the next play means.

The NAR case records that the narrative can orient the listener during the event, but later analysis, statistics, rule disputes, injury reports, or official results require return to the event record, official result publication, or governing evidence pattern. Live commentary may use tension and prediction, but it cannot treat provisional interpretation as settled event evidence.

#### A.6.3.NAR:5.3 - FPF seminar-route boundary

A team tests whether a future seminar series can explain FPF. The narrative rendering may use `A.6.3.NAR` to declare how FPF selected source structures are ordered for learners: EntityOfConcern discipline, problem frames, pattern use, relation records, source-basis return, framework authoring, and improvement loops.

The probe evaluates whether NAR supports an external seminar-route publication carrier for declared teaching use. It is not a narrative-rendering quality result, not evidence that FPF is correct, and not permission to place seminar outlines, slides, scripts, or exercises inside Core pattern bodies.

The actual seminar outline, slides, exercises, and script are not part of this pattern. They belong in a separate test-run publication carrier or teaching publication carrier. This pattern governs only the structure-to-sequence relation used by that carrier.

#### A.6.3.NAR:5.4 - Franchise-continuation storycraft probe boundary

A storycraft team tests whether a continuation-style narrative for a well-known space-opera franchise can preserve admitted source structures without becoming a fan-service list or an unauthorized publication plan. The source basis is the admitted canon or local source pack. The selected source structures may include continuity constraints, premise, theme, character-agency treatment, causal plot structure, viewpoint, stakes, and source-basis return refs.

`A.6.3.NAR` governs only the structure-to-sequence relation: which selected source structures are ordered into the proposed narrative path, which are foregrounded, which are lost or deferred, and when the worker must return to the named source pack. Storycraft vocabulary, canon classification, generation method, rights or publication permission, and full narrative-quality evaluation stay outside Core. Use `G.2` for the canon or source-pack claim, domain narrative and evaluation patterns plus direct FPF governing patterns for agency, responsibility, and declared-use rendering-quality claims, `C.35` when generated drafts are used, and publication or rights governing patterns when publication is live.

#### A.6.3.NAR:5.5 - Homotopy-theory explanation probe boundary

A teacher turns a graph-heavy mathematical source publication into a sequential explanation of homotopy theory. The selected source structures may include definitions, dependency order, examples, counterexamples, theorem prerequisites, proof-status boundaries, and return to formal statements. The narrative order may be didactic dependency order rather than historical discovery order or proof order.

`A.6.3.NAR` records the chosen sequence rule and visible loss: which mathematical structures remain reconstructible, which proof details or generalizations are deferred, and when the learner must return to formal mathematical statements. It does not certify the mathematical proof, replace the formal text, or turn analogy recall into understanding. Use mathematical-lens, proof, `G.2` source-use, evidence, publication, and teaching-evaluation governing patterns when those claims are live.

#### A.6.3.NAR:5.6 - Automated event-graph narrative

An LLM or NLG system receives an event graph, agent goals, constraints, and a domain schema, then proposes a story scene.

NAR records the relation only after source-basis admission and generated-output admission have done their work. The case names source plan, selected event relations, ordering rule, preserved event constraints, coarsened or hallucinated structure, and source-basis return condition. Generated fluency does not make the narrative authoritative; generated-output admission remains with `C.35`, source-pack claims with `G.2`, and evidence or assurance with their direct governing patterns.

