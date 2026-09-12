---
chunk_kind: "child"
pattern_id: "C.2.8"
pattern_title: "U.ExtractableStructuralInformation"
section_id: "C.2.8:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.8/C.2.8__005_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.2.8 — U.ExtractableStructuralInformation"
  - "C.2.8:4 — Solution"
line_start: 45924
line_end: 46013
dependencies:
  - "A.17"
  - "A.18"
  - "A.6.3.NAR"
  - "C.16"
  - "C.2.1"
  - "C.2.4"
  - "C.29"
  - "C.33"
  - "E.17.EFP"
keywords:
  - "bounded observer"
  - "description comparison"
  - "epiplexity"
  - "extractable structure"
  - "reader preparation"
  - "reading budget"
  - "structural information"
---

### C.2.8:4 - Solution

#### C.2.8:4.1 - Recover the structural question

Begin with the reader's needed understanding or action. Select the structure that matters to it: for example, a distinction between two alternatives, the dependency that orders two actions, or the reason a design choice changes under a new condition. A study of structural information may instead select a structure family for that research question. Selection need not assign task utility.

Identify the account and form being used. State only the conditions that could change the comparison: relevant concepts and notation the reader can use, available inference or inspection operations, accessible sources and help, and the effort or computation budget. A qualification or course title may locate evidence of preparation; it does not specify the usable knowledge by itself.

Then recover or estimate the selected structure and compare it with the relevant source or correctness criterion. Retain what each expression contributes, what remains missing and what a source return or prerequisite supplies. Reuse a sufficient current result. A new reading trial is useful when its possible outcomes could change the explanation or receiving decision.

Stop when that structural comparison answers the current question. If the selected structure or correctness basis is unresolved, return that gap before assigning an amount. If the practical question is whether a proposed change is worthwhile, use C.11.CRC and C.11 with extraction effort and task value stated separately.

#### C.2.8:4.2 - Characteristic and arity

**Tech name:** `U.ExtractableStructuralInformation`. **Plain name:** structure this reader or observer can extract. `ESI` is an abbreviation after the full name has been introduced.

This is an A.17 `U.RelationCharacteristic`, with arity three over the ordered tuple:

```text
(expressed episteme E, expressing publication form P, reader or observer O)
```

Its aspect is the amount of selected structure correctly extractable from E through P by O under stated comparison conditions. The characteristic is a dependent characteristic, not a root U-kind.

E retains its C.2.1 identity. P is the entity expressing that episteme in the applicable E.24.PUB publication-form relation and retains the more specific kind supplied by its form pattern. O is the specified human or computational observer. An estimate about a reader class states the relevant preparation and variation among its members; it does not treat the class as another individual reader.

Where exact notation helps, write `ESI_C(E, P, O)`. C fixes the selected structure, correctness criterion, relevant prior knowledge, usable operations, available assistance and tools, access conditions, budget and any other qualification that changes interpretation. These conditions qualify the characteristic of the tuple; they are not an additional bearer or a universal record kind.

Changing only expression can retain E. Adding, omitting or changing substantive claims can identify another episteme; use C.2.1 and the applicable source-to-target rule for that claim. In an explanation use, E.17.EFP's first screen distinguishes those branches when the difference matters. A comparison of forms alone holds the expressed claims constant.

The presentation carrier belongs in the access conditions when rendering, resolution, searchability or availability affects extraction. Changing access can change the qualified result while E and P remain the same. Attribute that difference to the changed access conditions. Ordinary references to a page, diagram or file are sufficient when they identify the required account and expression without ambiguity.

#### C.2.8:4.3 - Correct recovery and the expression's contribution

Correct recovery preserves the selected relation's participants, predicate, polarity, modality and action-changing conditions under the declared source or criterion. State the unit of structure only as precisely as the comparison needs. A qualitative result can name additional and missing dependencies directly; a count must also define its granularity.

Repeated expression of the same relation does not add structural amount merely by increasing words, boxes or arrows. A count of edges in a representation needs a correspondence to the selected semantic relations before it can count those relations.

Keep two questions distinct when the source contains a false or unsupported claim. A reader may correctly recover that the account asserts that claim. Establishing the claim about the described world requires its subject and evidence criteria. For recovery of warranted source structure, an unsupported relation does not count as a correct member. Recovering the assertion and endorsing its content are different results.

Prior knowledge may supply vocabulary, notation and inference used to decode the expression. A reader who independently corrects false text from memory has supplied a correction; the text does not receive credit for that corrected relation. When attribution matters, preserve the initial response and identify actual assistance and source returns before interpreting the observed difference. An explanation can expose already familiar structure: ESI is not restricted to newly learned information.

#### C.2.8:4.4 - Positive direction and scale choice

More selected structure correctly extractable under comparable conditions is the positive direction of ESI. If one result includes every correctly recoverable selected relation of another and adds selected relations, it has the positive structural direction. If each exposes something the other does not, retain that trade-off unless a justified scale resolves it.

A scale can be ordinal, a count, a fraction, a nonnegative structural weighting or a bit estimate. Its meaning and method must fit the declared use. A fraction has a fixed denominator; a weighted amount has an explicit structural interpretation. Changing the selected structure, granularity, denominator or weights changes the comparison basis. A task-utility weighting defines a separate score rather than silently becoming structural amount.

An ordered ESI scale declares the positive direction under A.17/A.18. A numeric comparison uses only operations legal for that scale. C.16 supplies the measurement chain when a measurement is claimed: the tuple and measurand, scale, method and model, obtained result and relevant uncertainty. Qualitative comparisons and conditional design estimates remain available without a validated human bit estimator.

A missing observation, unspecified denominator or unresolved criterion is missing basis for a value. It is not an observed zero. A zero has meaning only under a defined scale and a result that supports it.

#### C.2.8:4.5 - Reading results, estimates and robustness

A design walkthrough, an actual reading and a formal-model estimate can concern the same characteristic. State which grounds the assertion and the conditions at which it applies.

An observed response establishes the structure recovered in that trial and can ground an estimate of what is extractable. One success does not establish a maximum or reliability for a population; one failure does not establish impossibility. A computational procedure can support an exact bounded result when its operation and selected structure make that result derivable.

Repeat or perturb a reading when the receiving use needs a claim about robustness or transfer. Preserve the first response before giving a changed condition or further help. Success under the new condition strengthens the corresponding changed-condition claim; it does not add structure to the original result by itself.

For a cold-reader check, obtain the instruction from the publication, its declared prerequisites and the knowledge presupposed for the intended reader. The task may supply case facts. If it supplies the missing explanation of the instruction, the response shows use of that added explanation. Use F.19 to repair the publication before claiming that the publication itself supplied the action.

Absence of human validation restricts empirical claims about people. It does not restrict ESI to computational observers or prevent a conditional author estimate about a human reading situation.

#### C.2.8:4.6 - Relation to epiplexity and MDL

A formal structural-information estimate is useful when a mathematical model can represent the selected account, observer and extraction question. Use C.29 for that correspondence and its preserved and lost structure.

Finzi et al.'s computational epiplexity selects a time-bounded probabilistic program by a two-part coding criterion:

```text
P* = argmin over P in P_T of ( |P| + E[-log2 P(X)] )
S_T(X) = |P*|
H_T(X) = E[-log2 P*(X)]
```

Ties select the shorter program. The model term describes structural information; the residual is time-bounded entropy. Conditional versions allow side information, and practical estimators have their own assumptions. The execution bound and the effort of finding or estimating a model are distinct costs. [Finzi et al., v2, §3–4](https://arxiv.org/pdf/2601.03220v2)

For an ESI estimate, explain how the episteme and expression map to X, how the model class represents the observer's available operations, and which selected structure the model term estimates. State how prior knowledge is represented. Conditional model description given side information need not count all familiar structure a reader can recover.

Use epiplexity as a formal specialization where that correspondence holds. Otherwise it motivates the structural-information question without supplying its value. Total code length, text length and arbitrary model size are not interchangeable ESI measures. Ordinary description comparisons may use an adequate domain method without a coding model.

#### C.2.8:4.7 - Articulation, effort and useful change

C.2.4 `U.ArticulationExplicitness` orders progression from a cue to explicit branch-appropriate meaning and stable receiving use. ESI compares the selected structure extractable by an observer under a budget. Two complete descriptions at the same AE level can have different ESI; a reader's difficulty alone does not establish that the semantic branch was left unarticulated.

Measure or compare extraction effort separately. Two expressions may expose the same structure at different cost. Additional selected structure may also be irrelevant to the next task or displace more valuable work. C.11.CRC/C.11 make the marginal choice using the structural result, cost, protected results and receiving value. The chosen result may be the current sufficient explanation.

Use the method appropriate to the proposed change: C.37 for selecting representations, A.6.3.NAR for narrative ordering and source carry-through, or the applicable domain description or instructional method. ESI states the aspect being compared; it does not prescribe adding a diagram, example or lesson.

