---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__004_solution.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:3 — Solution"
line_start: 39954
line_end: 39995
dependencies:
  - "A.10"
  - "B.3"
  - "B.3.4"
  - "B.3.5"
  - "C.28"
keywords:
  - "assurance profile"
  - "conceptual correspondence"
  - "constructive support"
  - "empirical validation"
  - "use-qualified assurance"
  - "verification"
---

### B.3.3:3 - Solution

Use B.3 to identify the target claim and receiving assurance use. Determine which uncertainty or possible failure matters to that use, then examine the support that bears on it. State the supported or narrowed conclusion and the limitations that change reliance. A result need not carry an `AssuranceLevel`.

#### B.3.3:3.1 - Assurance subtypes answer different questions

| Subtype | Code | Question answered | Contribution and boundary |
| --- | --- | --- | --- |
| Concept-Bridge Assurance | CBA | Do the load-bearing terms and participants correspond across the descriptions being used? | Compare the relevant meanings, referents and conditions through B.5.3 when movement across vocabularies can change the argument. A discovered or repaired mismatch can change the assurance conclusion. Performing a comparison does not itself improve a relation's congruence. |
| Verification Assurance | VA | Does the claimed consequence follow under the stated specification and assumptions? | Inspect the proof, logical argument or applicable construction. The result supports that consequence under those premises; it does not establish that a running system satisfies its environmental assumptions. |
| Validation Assurance | LA | Does the empirical basis support the claimed performance in the receiving conditions? | Examine relevance, coverage, measurement quality, limitations and contrary results. A simulation supports a claim about its modelled conditions; transfer to an actual system needs the applicable model-to-world warrant. |

Select the contributions needed by the claim, rather than demanding all three types for every judgement. A mathematical consequence may need a proof and no field trial. An engineering performance claim may have sufficient empirical support without an additional formal proof. A safety-related claim needs the actual protective argument and required evidence; neither `FV ≥ threshold` nor `EV > 0` establishes that adequacy by itself.

Terms such as `FV`, `EV` or `CL` can be used only with the bearer, scale and interpretation the receiving argument consumes, as in B.3. A field called `verifiedBy` or `validatedBy` identifies a support relation to inspect, not a positive judgement by its mere presence.

#### B.3.3:3.2 - Use a level only through its justified profile

A domain may define an assurance profile or ordered levels when a recurring receiving decision benefits from that comparison. Its definition states the claim class and use, relevant conditions, meaning of each level, evidence rules, threshold basis and reconsideration conditions. Keep the measure and its scale explicit where a threshold is used. Establish the ordering from these meanings; the numerals in `L0–L2` supply no ordering of trust across unlike uses.

Publish `AssuranceLevel` only with the applicable profile and a result showing why the target meets its criteria. The legacy names `Unsubstantiated`, `Substantiated` and `Axiomatic` do not supply default criteria. In particular, an axiomatic or constructive justification concerns a particular consequence or construction, not a universally higher assurance state than empirical support. A conjecture's origin in abduction likewise does not assign it `L0`.

Examine whether a demanded threshold or evidence requirement protects the relevant quantity well enough to justify its cost, delay and displaced work. Keep that judgement distinct from the conditions presently binding the action. A recommendation to amend a requirement does not change it or confer amendment authority.

For a one-off receiving use, stop with the sufficient qualified assurance result. Do not create a profile, fill unused level fields or explain the omission of a level solely to complete this pattern.

#### B.3.3:3.3 - Preserve scope and inspect the actual grounding

Keep a design-time `MethodDescription` claim separate from a claim about performed `Work` or its `Trace`. Cite evidence with the appropriate conditions and scope. Evidence for a parent claim covers a child claim only through an argument establishing that coverage; a declaration of inheritance is insufficient.

State structural claims as readable Working-Model relations. When a publication choice or current requirement elects B.3.5's CT2R-LOG profile, follow its relation-specific grounding: structural parthood uses the applicable C.13 `sum` or `slice` construction trace; collection belonging uses the collection's `set` trace. These elected branches declare `validationMode=axiomatic`. Other permitted relation claims retain their applicable logical or empirical support. A level label alone does not elect this profile.

A grounding account and the author's `validationMode` are inputs to inspect. Neither creates the relation, makes an empirical premise true, nor decides its currentness. Assurance publications remain downstream of the Working-Model surface under E.14.

#### B.3.3:3.4 - Worked case: a useful empirical result and an irrelevant fresh test

A team is deciding whether a converter can be used for non-safety-critical measurements within a declared temperature and input range. In this example, the receiving task's justified tolerance is 2%. Calibration results covering that range, an adequate measurement-error account and applicable operating observations support error below that tolerance. The team can return “supported for this measurement use within the stated range,” with its actual limitations. A formal proof of unrelated program properties is unnecessary.

Now replace that basis with a newly passed boot test and a glossary mapping. These establish startup behaviour and the intended term correspondences, not measurement accuracy. The same requested measurement use remains unsupported. Neither fresh evidence nor one link of each required type repairs the missing performance basis.

If the recipient instead needs a mathematical invariant, inspect the proof under its assumptions. If the application introduces a protective function or a different operating range, reopen the affected assurance question under its own threshold and evidence rules. The earlier limited result remains an account of what it supported.

