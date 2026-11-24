---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__004_solution.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:3 — Solution"
line_start: 47235
line_end: 47282
dependencies:
  - "A.10"
  - "B.3"
  - "B.3.4"
  - "B.3.5"
  - "C.28"
keywords:
---

### B.3.3:3 - Solution

Use B.3 to identify the target claim and receiving use. Ask what could make the proposed conclusion fail. Follow that possibility to the correspondence, inference or observation that can resolve it. A single applicable argument can settle the use. For a decision requiring several contributions, check that their subjects, conditions and conclusions fit together. A result can be given without an `AssuranceLevel`.

#### B.3.3:3.1 - Assurance subtypes answer different questions

| Subtype | Code | Question answered | Contribution and boundary |
| --- | --- | --- | --- |
| Concept-Bridge Assurance | CBA | Do the load-bearing terms and participants correspond across the descriptions being used? | Compare the relevant meanings, referents and conditions through B.5.3 when movement across vocabularies can change the argument. A discovered or repaired mismatch can change the assurance conclusion. Performing a comparison does not itself improve a relation's congruence. |
| Verification Assurance | VA | Does the claimed consequence follow under the stated specification and assumptions? | Inspect the proof, logical argument or applicable construction. The result supports that consequence under those premises; it does not establish that a running system satisfies its environmental assumptions. |
| Validation Assurance | LA | Does the empirical basis support the claimed performance in the receiving conditions? | Examine relevance, coverage, measurement quality, limitations and contrary results. A simulation supports a claim about its modelled conditions; transfer to a system needs the applicable model-to-world warrant. |

Select the contributions needed by the claim, rather than demanding all three types for every judgement. A mathematical consequence may need a proof and no field trial. An engineering performance claim may have sufficient empirical support without an additional formal proof. A safety-related claim needs the protective argument and required evidence; neither `FV ≥ threshold` nor `EV > 0` establishes that adequacy.

Terms such as `FV`, `EV` or `CL` can be used only with the bearer, scale and interpretation the receiving argument consumes, as in B.3. A field called `verifiedBy` or `validatedBy` identifies a support relation to inspect, not a positive judgement by its presence.

#### B.3.3:3.2 - Use a level only through its justified profile

A domain may define an assurance profile or ordered levels when a recurring receiving decision benefits from that comparison. Its definition states the claim class and use, conditions, meaning of any levels used, evidence rules, the basis for any thresholds, and reconsideration conditions. State the measure and its scale where a threshold is used.

To design such a profile, take the actions its recipients must distinguish and work back to what would justify each. Hold the apparent level fixed and change the subject, the part tested or the conditions of operation. Would the same level now warrant a different action? Retain the difference in the criteria or limit their applicability. Select the grounds for meeting each criterion, including alternative sufficient arguments where the decision permits them. Ask which cases the proposed rule could accept despite a missing condition and which sufficiently supported cases it would exclude. A general argument can settle either question. Adjust the rule to the intended use or retain an exclusion required by that use.

Where levels are ordered, establish the ordering their meanings promise. If one level is said to support every use allowed by another, establish that implication across the applicable conditions. A narrower operating range with better accuracy need not contain a wider range with looser accuracy. State what each qualifies when the uses differ.

To assign or endorse an assurance level on its merits, apply the profile and show how the evidence meets its criteria. To report the level an authority actually assigned, identify the decision, the designation or profile it used and its scope. An error in applying the criteria can change what the assignment warrants while the historical fact of assignment remains established. The legacy names `Unsubstantiated`, `Substantiated` and `Axiomatic` do not supply default criteria. In particular, an axiomatic or constructive justification concerns a consequence or construction, not a universally higher assurance state than empirical support. A conjecture's origin in abduction likewise does not assign it `L0`.

Examine whether a demanded threshold or evidence requirement protects the relevant quantity well enough to justify its cost, delay and displaced work. Keep that judgement distinct from the conditions binding the action. A recommendation to amend a requirement does not change it or confer amendment authority.

For a one-off receiving use, stop with the sufficient qualified assurance result. Do not create a profile, fill unused level fields or explain the omission of a level solely to complete this pattern.

#### B.3.3:3.3 - Preserve scope and inspect the grounding

A claim about a design-time `MethodDescription` and one about performed `Work` or its `Trace` have different subjects. For an inference across composition scales, identify the relation the receiving claim uses. A condition established for every operating mode applies to a specified mode within that range. A rate for the whole constrains its parts to the extent their sizes and overlap permit. If passing and failing exhaust the outcomes on this criterion and at most two of 100 distinct readings failed, at least eight of any ten of those readings passed. Conversely, two groups of ten can each report nine passes yet share the same nine passing readings and have different failures. Their combined set then has nine passes among eleven readings. Establish the coverage and common conditions needed for the conclusion in the chosen direction.

State structural claims as readable Working-Model relations. When a publication choice or current requirement elects B.3.5's CT2R-LOG profile, follow its relation-specific grounding: structural parthood uses the applicable C.13 `sum` or `slice` construction trace; collection belonging uses the collection's `set` trace. These elected branches declare `validationMode=axiomatic`. Other permitted relation claims retain their applicable logical or empirical support. A level label alone does not elect this profile.

A grounding account and the author's `validationMode` are inputs to inspect. Neither creates the relation, makes an empirical premise true, nor decides its currentness. Assurance publications remain downstream of the Working-Model surface under E.14.

#### B.3.3:3.4 - Worked case: a useful empirical result and an irrelevant fresh test

A team is deciding whether a converter can be used for non-safety-critical measurements within a declared temperature and input range. In this example, the receiving task's justified tolerance is 2%. Calibration results covering that range, an adequate measurement-error account and applicable operating observations support error below that tolerance. The team can return “supported for this measurement use within the stated range,” with its limitations. A formal proof of unrelated program properties is unnecessary.

Now replace that basis with a newly passed boot test and a glossary mapping. These establish startup behaviour and the intended term correspondences, not measurement accuracy. The same requested measurement use remains unsupported. Neither fresh evidence nor one link of each required type repairs the missing performance basis.

If the recipient instead needs a mathematical invariant, inspect the proof under its assumptions. If the application introduces a protective function or a different operating range, reopen the affected assurance question under its threshold and evidence rules. The earlier limited result remains an account of what it supported.

To design a profile for later converter assignments, recover what each recipient uses the measurement to decide. An offset that stays the same in two readings cancels in their difference. The same offset can decide whether an absolute limit has been crossed. Develop criteria for the quantity being accepted and the operating conditions that could change its error. Applying the existing 2% criterion remains sufficient for the original assignment when its grounds still hold.

