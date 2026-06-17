---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__002_use-this-when.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:0 — Use This When"
line_start: 6894
line_end: 6927
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30.ASV"
  - "E.18"
  - "E.18.1"
  - "E.18.2"
  - "E.20"
  - "E.24"
keywords:
  - "bounded change"
  - "functioning"
  - "input/output conditions"
  - "transformation"
  - "transformation-flow structure"
  - "transformed entity"
  - "transformer"
---

### A.3.4:0 - Use This When

Use this pattern when a project needs to identify a bounded transformation itself: what governed object changes, from what condition to what condition or delta, under which boundary conditions, and which typed values must be considered around that transformation before a stronger claim is made.

Use it when the working question is:

- what is transformed;
- what relation, task, transition, operation family, or predicate states the change;
- what conditions make the transformation possible, admissible, planned, enacted, observed, modeled, claimed, or published;
- which temporal aspect matters: time window, duration, cadence, rhythm, synchronization, currentness, or ordering relation;
- which transformation-ontic slots are claim-relevant in this use: acting system and `TransformerRole` relation when actual work is claimed, method, method description, mechanism, work plan, work occurrence, transformation-flow structure, transformation-flow mathematical description or lens, dynamics episteme, temporal aspect, temporal-claim adequacy, evidence relation, result record, source relation, publication, gate, decision, assurance, or refresh or reopen claim.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Transformation`: the durable ontic for bounded change under declared conditions over an entity, structure, state, characteristic, episteme, work product, architecture, formal object, or other governed object. Its type-level typed n-ary `SlotRelation` with `SlotSpec` signature states both the identity slots by which one transformation is recovered and the participation and check slots by which claims about acting side, method, work, mechanism, transformation-flow structure, mathematical description, evidence, publication, and other transformation-relevant values stay attached to the same ontic. The `transformationRelation` is one slot inside that typed relation, not the whole `U.Transformation`.

**First useful move.** Identify the `U.Transformation` value first by filling the identity slots: transformed object, bounded context, initial condition, post-state condition or delta, transformation relation, admissibility or boundary condition, and temporal or ordering reference when relevant. Then run the participation and check slot relation in `A.3.4:4.4`: for each slot, record a filled value, unknown or not recovered, not asserted, not current for this claim, or claim lowering or blocking when a stronger claim depends on the missing value. If a claim-bearing record is also needed, treat it as a `C.2.1` episteme whose claim graph may make claims about the transformation, one of its slots, a slot filler, or relations among those values. Do not treat the episteme as the transformation itself.

**Open-world guard.** An unfilled method, work, description, evidence, result, gate, or publication slot does not mean that no such value exists in the world. It means only that this use has not recovered or asserted that value, or that the value is not current for the claim being made. Do not infer a methodless transformation merely because no `U.Method` has been described yet.

**What goes wrong if missed.** Method names become change proof, work traces become laws, process diagrams become execution, dynamics models become permission, temporal trends become intervention claims, mathematical constructions become project-world work, and publications about a change are treated as the change itself.

**What this buys.** A practitioner can keep the transformation under concern distinct from, but slot-connected to, the system bearing TransformerRole and dated work when actual project-world change is claimed, the method that can specify it, the mechanism that can law-govern it, the transformation-flow structure that can compose or locate it, the mathematical description or lens that can express selected structure, the dynamics episteme that can model it, the temporal aspect that can time it, the temporal-claim adequacy pattern that can judge a temporal claim, and the evidence or result relation that can justify a use.

**Not this pattern when.**

- If the issue is only a semantic way of doing, use `A.3.1`.
- If the issue is a description of that way, use `A.3.2`.
- If the issue is a state-space and transition-law episteme, use `A.3.3`.
- If the issue is a law-governed operation algebra with admissibility predicates, use `A.6.1` and `E.20`.
- If the issue is planned or dated work, use `A.15.2` or `A.15.1`.
- If the issue is the selected compound transformation-flow structure, its locus, path, path slice, crossing, or flow valuation, use `E.18`.
- If the issue is a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression used to describe that structure mathematically, use `E.18.2` and `C.29`.
- If the issue is a positive temporal aspect of an object or claim, use `C.27.TA`.
- If the issue is adequacy or supported use of a temporal claim, use `C.27`.

