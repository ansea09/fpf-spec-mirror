---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:9"
section_title: "Archetypal Grounding — Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__010_archetypal-grounding-worked-cases.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:9 — Archetypal Grounding — Worked Cases"
line_start: 42363
line_end: 42413
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

### C.2.1:9 - Archetypal Grounding — Worked Cases

These cases ground the pattern in practice; only a case that names an obtaining `EpistemeEmpiricalGroundingRelation` asserts empirical grounding.

#### C.2.1:9.1 - Physical engineering

A pump-maintenance specification has a claim graph about exact pump `P` under a reference scheme that resolves part names, states, units, and measurement procedures. Those three participants identify the episteme. For test bench `B`, exact covered claim subgraph `C_B` contains the discharge-pressure-tolerance and leakage claims. Its claim-to-world mapping names the direct pressure-measurement and leakage-inspection relations involving `B`; a maintenance-interval claim outside `C_B` is not grounded by those measurements. The grounding relation over `(E,B)`, with `covered=C_B`, continues for the maximal interval during which every required mapping obtains. If that coverage continues while an evidence archive or inspection-work log becomes unavailable, only a separately governed support, warrant, confidence, or evidence-use assertion may change. A publication occurrence makes the episteme available through a rendered checklist form borne by an exact carrier. For each maintenance or inspection Work recorded by checklist marks, use A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently. If the checklist account must also identify the assignment under which that Work was performed, check that relation separately through F.6. A separately current assertion that `P` satisfies the constructive `U.System` criterion is another episteme about `P`; renaming or republishing the governing FPF pattern does not change `P` or create its systemhood.

The classification assertion changes only when its own claim content or reference scheme changes. Pump continuity is judged instead under the `A.1` reidentification rule; a changed or unchanged assertion does not establish that continuity.

#### C.2.1:9.2 - Medicine

A diagnostic model concerns one patient-state entity or one admitted patient cohort under a scheme that defines observations, measurements, and diagnostic interpretations. For each precise clinical Work claim, use A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently. If the clinical account must also identify the assignment under which the Work was performed, check that relation separately through F.6. The assignment neither participates in nor performs the Work, and a failed check leaves Work intact. Neither the Systems nor assignments are absorbed into the model's EntityOfConcern. Each `EpistemeEmpiricalGroundingRelation` identifies the exact covered diagnostic-claim subgraph, grounding holon, mapping to the required current observation, measurement, or test relations, and maximal continuous interval of complete coverage; it grounds no unlisted claim. If a threshold revision changes claim content or the effective reference scheme, that changed discriminator identifies another episteme; moving the unchanged model to another screen changes only the exact publication or representation object that actually changed.

#### C.2.1:9.3 - Competence claims, teaching Work, and learner-facing views

When claim-bearing *learning*, *teaching*, *taught*, or *learned* wording still hides the changed subject or returned result, use `E.10.LRN` first and return each recovered claim to its direct pattern. A curriculum model concerns an exact competence structure under a scheme that relates exact assessment or performance evidence to competence claims. Teaching, coaching, practice-support, assessment, and learner inquiry may designate different Methods or dated Work occurrences. Recover those objects separately; none is the competence structure or the holder's capability. “Was taught” foregrounds an intervention received, while “learned to perform X” ordinarily foregrounds a capability claim and leaves teacher, self-directed inquiry, practice, tools, peers, and environment underdetermined. One exact admitted course-cohort holon or one exact admitted learning-environment holon may participate in a separate grounding occurrence without becoming the competence structure.

A learner-facing episteme is a `U.View` when it conforms to an exact learner-facing viewpoint under `E.17.0`. If it was constructed from the source curriculum-model episteme, use `A.6.3` to state that separate viewing relation. For lesson-session or receiving-episteme authoring or construction Work, use A.13 to identify each actual performer and A.15.1 to admit each dated occurrence independently. If an account must also identify the assignment under which that Work was performed, check it separately through F.6. A lesson, public construction, recalled text, score, or observed performance has only the result established by its direct result pattern. If a later claim relies on that result, use `A.10` separately to classify the named bounded reliance; none of those items by itself establishes authorship, capability, transfer, or retention. None is required merely to identify the learner-facing episteme from its claims, exact subject, and effective scheme.

#### C.2.1:9.4 - Episteme about an episteme

Simulation model `M` is one episteme. Review `R` concerns `M`, so the EntityOfConcern in `R` is the episteme `M`, not the physical system modeled by `M`. Claims in either episteme may cite separately governed evidence-use relations concerning the simulated or physical system. Publishing `R` does not revise `M`.

A theory episteme is recognized through its claim-bearing constitution and whole-level inferential characteristics. A textbook publication can make one edition of that theory available, but the publication occurrence, form, and carrier are not constituents of the theory and do not establish its holonhood.

#### C.2.1:9.5 - Edition succession

Episteme `E1` is the exact source used to produce candidate edition `E2`. The applicable continuity policy says that the EntityOfConcern remains the same, specified core claims must remain traceable, listed claims may be corrected, and a translation into another reference scheme counts as a derivative rather than an edition. The current case identifies the preserved core claims, deliberately corrected claims, unchanged EntityOfConcern, and source-to-revision use. Those facts satisfy the policy, so the positive `EpistemeEditionRelation(E1,E2)` assertion is available.

If the same Work instead retargets the claims to another EntityOfConcern, translates them under a rule that the policy classifies as a derivative, or reconstructs similar content without using E1 as source, the edition predicate fails even when the Method is named “revision.” Work, Method, provenance, change facts, evaluation, and evidence remain outside the two-participant relation. Later repackaging or publication establishes neither another episteme nor edition continuity.

#### C.2.1:9.6 - Grounded identity across two observations
A morning-observation episteme concerns observed object `M` under one reference scheme; an evening-observation episteme concerns observed object `E` under another. The exact direct identity or reidentification pattern for the observed entity must define the predicate and identity rule. The physically testable trajectory and observations supply the current case facts; they may satisfy or fail that predicate but the pattern itself establishes neither result. A separate identity-assertion episteme states affirmative or negative polarity, and exact evaluation or evidence-use relations make supported, refuted, or unresolved reliance inspectable. Only after positive case facts satisfy the predicate may its identity rule individuate an occurrence for designation. If no current direct governor is recoverable, keep reliance unresolved and return an exact missing-relation blocker naming `M`, `E`, the required predicate and use, and the missing governor. Even after both designations resolve to the same exact entity, the two observation epistemes need not merge: their claim graphs or effective reference schemes can keep their C.2.1 identities different. A shared label or grounding holon alone establishes neither world-side identity nor episteme identity.

#### C.2.1:9.7 - Readable wiring diagram as a proxy

Wiring-model episteme `E1` concerns exact harness `H` under reference scheme `S1`, which resolves connector designators, pin identities, and connection predicates. A system performs exact diagram-redrawing work; any operation application, binding, or declared result position is governed separately by A.6.1. If only layout changes in a C.29 wiring-diagram representation, identify the exact representation transition and preserved connector, pin, and connection correspondence; `E1` remains the same. If instead only an exact publication form, carrier, or rendering changes, identify that E.17/E.24.PUB object and relation; `E1` again remains the same. If a connection claim is omitted or the legend changes the effective reference scheme, the changed claim graph or scheme identifies episteme `E2`. These three branches are settled by the changed object and C.2.1 discriminators; diagram-redrawing work and an A.6.1 result position establish none of them by themselves.

For the `C.29` lens-use statement, the target phenomenon is the connectivity of `H`; the candidate mathematical object is the wiring-diagram representation under its stated diagram scheme; the mapping resolves connector marks and pin marks to the independently identified connectors and pins. A layout-only transition preserves connector identity, pin identity, and connection predicates. An omitted connection loses one predicate, while a changed legend loses the earlier mark-to-connector reference. The diagram remains admissible for maintenance diagnosis only while the connections on which that diagnosis depends are preserved and recoverable; stop that use or return to the source relation structure when they are not. This representation statement does not prove that the diagram is the harness, that visual similarity preserves claims, or that a higher readability score preserves episteme identity.

A readability score can therefore improve while diagnosable connectivity becomes worse. When that score is used as the practical value, apply `E.13`: name the intended diagnostic value, the readability proxy, and what became worse. Use `C.29` and `A.6.3.RT` for the representation transition and its preserved or lost structure; under the C.2.1 identity rule, a changed claim graph or effective reference scheme identifies another episteme.

#### C.2.1:9.8 - Trained or probe-derived representation and tool-using inference

When *learned representation* is load-bearing and its subject is not already explicit, use `E.10.LRN` to separate training Work, trained model edition, system-side phenomenon, probe-training Work, decoded rendering, representation relation, and any later inference or capability claim. For any asserted inference or tool-call Work, use A.13 to identify the actual language-model or tool-using performer and A.15.1 to admit the dated occurrence independently. Add F.6 only if the account must also identify the assignment under which that Work was performed. That Work is not the earlier model-training occurrence or the resulting trained model.

First recover a distributed activation pattern as an exact system-side phenomenon observed during the inference Work. A probe's trained decoder or decoded rendering may represent that phenomenon for a declared use under `C.29` and `A.6.3.RT`; causal influence, decodability, or a readable label does not by itself make the activation pattern or its representation a `U.Episteme`. A probe result or decoded rendering is admitted as an episteme only when recoverable claim content concerns an exact EntityOfConcern under an effective reference scheme. Training loss, probe accuracy, recovered claim content, tool-use success, and deployed-system capability remain different results with different evidence.

Keep the other entities and claims separate through their exact direct relations. A tool-call trace may fill an exact A.6.1 result position or another declared participant position for the call work. If a receiving claim additionally asks when that trace first existed, apply the shared 4.9 boundary; otherwise its result position and work history add no inception claim. If the trace itself carries claims about that work, it may also be identified as another episteme through the C.2.1 triple. An answer entity identified at an exact declared result position and a separately identified evaluation-report episteme can have different kinds and EntitiesOfConcern; neither is a generic work result by wording alone. Tool availability, a successful call, or a high evaluation score establishes neither claim truth nor empirical grounding. When tool integration changes or degrades reasoning, locate the change in the enacted method, inference work, call work, operation binding, representation use, evidence relation, or empirical-grounding occurrence. Reidentify an episteme only when its claim content, EntityOfConcern, or effective reference scheme changed.

