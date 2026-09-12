---
chunk_kind: "child"
pattern_id: "F.0.2"
pattern_title: "Conceptual Synthesis across Source Ontologies"
section_id: "F.0.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.2/F.0.2__006_archetypal-grounding.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "F.0.2 — Conceptual Synthesis across Source Ontologies"
  - "F.0.2:5 — Archetypal Grounding"
line_start: 96235
line_end: 96285
dependencies:
  - "A.2.4"
  - "C.2.1"
  - "E.10.ARCH"
  - "E.4.DPF"
  - "F.0.1"
  - "F.1"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.8"
  - "F.9"
  - "G.11"
  - "G.2"
keywords:
---

### F.0.2:5 - Archetypal Grounding

#### F.0.2:5.1 - Systems Engineering use and system concept

A Systems Engineering DPF author must decide what a practitioner should do when a proposed system concept is internally attractive but its connection to outside use is unclear. The author compares a proposed outside-before-inside instruction with the receiving ontology and an external systems-engineering account:

| Input to the comparison | Claim used in this comparison | Role and limit |
| --- | --- | --- |
| Proposed outside-before-inside instruction | Begin with the system's behavior in its operating environment and only then work inward toward alternative constructions. These linked descriptions remain revisable. | Authoring proposal to test and refine. |
| `FPF 8`, patterns `A.14`, `A.6.F`, and `C.2.1` | Parthood, function or effect claims, function bearing, and the identity of a claim-bearing episteme are separate questions with their own conditions. | Receiving-ontology boundary. |
| [SEBoK v2.14, *Applying the Systems Approach*, permanent revision `78074`](https://sebokwiki.org/w/index.php?title=Applying_the_Systems_Approach&oldid=78074), 18 May 2026, `Application Principles` | Apply activities concurrently with attention to their dependencies. Iterate between needs and candidate solutions. | Comparison for dependency-aware concurrent and iterative work; the sequence is tailored to the problem situation. |



A lexical crosswalk that maps both *using system* and *containing system* to one *parent system* entry erases the use-versus-parthood distinction. The author can then no longer compare changing the project system's construction with changing how an external system uses it.

The comparison concerns **priority within an iterative process**. Starting from an internal construction can narrow the alternatives before the outside behavior and operating conditions are known. Begin with the outside-use question. Once the information needed for a particular design question is explicit, explore construction and feasibility while refining the use account; leave a dependent construction choice open while its decisive use conditions remain unknown.

The author records the **provisional synthesis** branch at local locator `SE-CS-USE-01` with this claim: **“For one Systems Engineering concept decision, first establish the proposed outside behavior, operating conditions and system-of-interest sufficiently to compare internal constructions. Develop and test candidate constructions against that use; refine both accounts as new information arrives, and reopen the use, boundary or construction when realization evidence defeats it. State the subjects and direct relations that change the decision.”** This retains the proposal's outside-before-inside priority, reconciled with dependency-aware concurrent and iterative work.

**Replay the clock choice.** A team begins comparing gear arrangements for a clock. In this constructed case, asking where and how the clock will be used reveals a requirement for millisecond timing beside a rocket engine, with vibration and 30 g acceleration. The next result is an explicit timing-and-environment use hypothesis; the team compares and tests constructions against it before selecting one. Timing accuracy and vibration resistance can be investigated in parallel once their required operating conditions are stated. If feasibility evidence defeats the proposed clock use, revise that use or the system concept and compare again.

A key/lock case changes another premise: investigating the intended change from a locked to an unlocked door shifts the system-of-interest from the key to the lock, with the key treated as a subsystem in that decomposition. Recover the selected boundary before comparing mechanical, electronic or biometric realizations. The retained function stays visible while the construction alternatives change.

In this worked case, the later Systems Engineering DPF content decision cites `SE-CS-USE-01` with this source edition and records `used as proposed`. The applied use-and-system-concept move stays in the Systems Engineering DPF; general claim, parthood and function-bearing rules stay in FPF. Reopen `SE-CS-USE-01` when a source changes the linked action or boundary, a counterexample shows that the proposal cannot guide the decision, or the receiving decision changes its intended use.

#### F.0.2:5.2 - Organization change contrast

An organization-change author compares schools that describe organizational flows and partial organizations through different transformations and coordination structures. The sources support a narrower claim about linked transformation and coordination structures, but not one universal organization-flow kind. The author records a contrast claim, preserves the source-local decompositions, and lets a later DPF content decision choose the narrower contribution.

#### F.0.2:5.3 - Scientific classification inquiry

A cross-disciplinary data framework proposes one shared classification relation between a laboratory ontology and an administrative classification. The available alignment suggests candidate correspondences, but the current edition of a load-bearing clinical source is unavailable. The author records an unresolved-inquiry claim about that bounded comparison, keeps the administrative-only use available, and names inspection of the missing clinical edition as the next source action.

#### F.0.2:5.4 - Cheap anti-case

An engineer consults a handbook and its later edition only to recover the current pump tolerance. The later edition gives the needed claim, and no ontological difference changes the authoring decision. The engineer records direct source reliance and stops without conceptual synthesis.

#### F.0.2:5.5 - Compare causal accounts on one sensor case


An author is deciding whether an explanation may treat inference about a hidden condition and changing an observed output as the same operation. Recover the source-local operations first. [Parr and Pezzulo (2021), Introduction and The Generative Model](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2021.772641/full), describes hidden-state inference together with policy-conditioned transitions and preferred outcomes. [Pearl, Glymour and Jewell's corrected primer, p.55](https://bayes.cs.ucla.edu/PRIMER/mueller-edits-questions-pearl-etal-2016-primer-errata-pages-august2019.pdf), supplies intervention by replacement of a generating mechanism.

Use the [binary load/alarm case in C.28:4.4][fpf-c28-4-4-ref]. Under exact inference from the same stipulated joint distribution, either account obtains a high-load probability of 0.9 after an alarm and 0.1 after an ordinary low reading. In the separately specified intervention model, setting the alarm output low leaves the load mechanism unchanged, so the high-load probability is 0.5.

An active-inference action can be compared with that intervention after its state-transition and observation consequences are specified. An action that changes only the output agrees on this load prediction. An action that initiates cooling requires the later load transition and its time order in both models. Comparing which action to select also needs the objectives or preferences used in selection.

The comparison establishes this contrast: the same joint distribution supplies the stated observational inference, while agreement about an action requires a correspondence between the specified mechanisms.

The receiving explanation decision can adopt this contrast and keep the two questions explicit. Reopen the comparison when the receiving question, source account, inference approximation or action mechanism changes.

