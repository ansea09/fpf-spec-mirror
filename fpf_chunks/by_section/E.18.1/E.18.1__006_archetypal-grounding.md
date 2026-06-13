---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "Principles-to-Work Carry-Through"
section_id: "E.18.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__006_archetypal-grounding.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "E.18.1 — Principles-to-Work Carry-Through"
  - "E.18.1:5 — Archetypal Grounding"
line_start: 68181
line_end: 68262
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.22.2"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.19"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
  - "P2W"
  - "accepted ProblemCard@Context"
  - "carry-through record"
  - "evaluation refresh"
  - "formal substrate"
  - "mechanism realization"
  - "method-family selection"
  - "principles-to-work"
  - "work planning"
---

### E.18.1:5 - Archetypal Grounding

`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, accepted problem-side material may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same material may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W move asks one question in both cases: which FPF kind or relation can carry the next claim being made?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision authority. |
| Show with P2W | The team writes a carry-through record, separates method comparison from `A.15.2 U.WorkPlan` and plan-item records, records dated `U.Work`, and unpacks result records. | The team writes a carry-through record, separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. P2W records the carried distinction, recovers mathematical-lens use and `U.Signature(profile=FormalSubstrate)` declaration only if needed, and stops before method selection until comparator, measurement, and selected-set relations are named.

2. **Planning from selected enough method.** A method family is selected enough for planning. P2W carries the planning relation; the plan records planned constraints, planned fillers, evidence-reference pins, and freshness requests.

3. **Performed work after planning.** A dated work occurrence has appeared. P2W carries the performed-work relation and records which gate, release, provenance, or launch-value relation is separate from the occurrence.

4. **Result interpretation without generic result.** A source says the work result proves that the approach worked. P2W unpacks artifact, telemetry, measurement, evidence, acceptance, quality-evaluation, refresh, and role-enactability candidates before any one of them guides the next move.

5. **Functional explanatory order.** A source diagram places `U.Signature(profile=FormalSubstrate)`, principle frame, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. P2W uses the diagram to classify applications while keeping material time and performed-work chronology with their own patterns.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. P2W first splits the phrase: module-interface relation (`A.6.M`), flow or throughput relation (`E.18` or `A.6.F` when function use is being claimed), WorkPlan constraint (`A.15.2`), dated `U.Work` occurrence (`A.15.1`), evidence or gate claim (`A.10`, `G.6`, `A.20`, or `A.21`), or architecture and structural-view claim (`C.30` family). The carry-through record writes only the relation that changes the P2W move being made and leaves the other readings as stopped cues.

7. **Result measurement returns to planning.** A performed `U.Work` occurrence produced telemetry and an artifact. Later measurement shows that the planned module-interface constraint was interpreted against the wrong reference plane. P2W splits measurement, reference-plane repair, source restoration, refresh, planning revision, and method-comparison claims. If the original `ProblemCard@Context` no longer states the right problem, the problem-side correction returns to the problem-side pattern.

#### E.18.1:5.2 - Additional worked situations

| Situation | P2W move | What changes |
|---|---|---|
| First-minute use | A practitioner has only an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." Fill `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, and `RecoveredFPFKindOrRelation` or `StopCondition`. | The next action becomes a `C.29` and `A.6.0` application, not method selection or evidence writing. |
| Diagram and approval note in the same source | The same source contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the distinction carried from the problem-side result. | Diagram, evidence-looking material, and gate-looking material are separated by relation recovery; the P2W record keeps only the carried distinction and next relation. |
| Principle story without accepted problem-side material | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the material remains a reduced-use cue until `C.22.2` or the problem-side pattern named by value accepts problem-side material. |
| Acceptance label hides wrong measurement | A dashboard shows a green acceptance label, but the measurement used the wrong reference plane. | Acceptance color does not guide the next move; P2W returns to measurement, normalization, source restoration, planning, and method comparison. |
| Changed unit after source restoration | Later source restoration changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated `U.Work` occurrence is cited, not rewritten. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | P2W uses `C.29` for mathematical-lens use and `A.6.0` for `U.Signature(profile=FormalSubstrate)`, names preserved and lost structure, and prevents the lens from settling empirical truth or work authorization. |
| FPF relation law changes after a P2W record | A governing FPF pattern changes the boundary for architecture-description, evidence, or source-restoration use. Fill the replay and currentness check: changed law, still-carried distinction, no-longer-carried cue, smallest reopened application, and next move. | The earlier carry-through record is replayed rather than trusted by age; only the affected architecture-description, evidence, source-restoration, or P2W field changes. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, flow relation, dated `U.Work` occurrence, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the P2W move being made is written; the remaining readings stop as named cues until their governed relations are being made. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side material. | The mathematical phrase lowers to a reduced-use cue; P2W does not open method selection, evidence, gate, or `A.15.2` planning from mathematical prestige alone. |
| Result source becomes stale | A result-looking source is later replaced by a fresher source with a different artifact reference and measurement reference. | P2W uses `A.15.4`-style source restoration before result carry-through; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for coupled development and application flows

These pilots are grounding checks, not source terminology to import. They exercise the same common shape: one selected `TransformationFlowStructure` can relate several flow valuations, one flow may develop or select a usable product, another flow may apply it, and an evaluation or refresh flow may return to the smallest affected development or application locus. The selected structure does not merge the flow objects, `DesignRunTag` boundaries, evidence, gates, work occurrences, or the relation position that the carried object fills inside each flow. Use each pilot to check whether the P2W use being made can name the joined flows, the carried object's flow-local relation position, the `DesignRunTag` boundary, and the smallest reopened slice.

| Pilot | P2W use being made | What it tests |
|---|---|---|
| Coffee service STF | An accepted service-quality problem carries heat or mass-balance structure through `U.Signature(profile=FormalSubstrate)`, declaration-stack, mechanism-position, normalization, method-selection, `A.15.2 U.WorkPlan` or plan-item records, dated `U.Work`, telemetry, measurement, and refresh relations. | Positive whole-chain readability, freshness, set-return selection, launch values only in performed work, and relation-local refresh. |
| Compiler design and run | Toolchain construction, compiler use, and product execution are separate applications; design and run changes pass through the gate and work relations being used. | `DesignRunTag`, launch gate, reproducible build currentness and source currentness, and no collapse of build, run, and product work. |
| TAMP and MPC robotics | Method selection and `A.15.2` planning records may be revised under a declared progress or budget condition before performed work. | Branching and cycle use without imposing one mandatory work procedure, and no launch-value binding before performed work. |
| AutoML and QD | Method selection returns a Pareto, QD, front, or archive set under comparator and descriptor editions, not a hidden scalar winner. | Set-return discipline, comparator currentness, no hidden scalarization, and retained-set refresh. |
| Freshness or material-transport case | Work planning and performed work depend on freshness windows, transport relations, units, reference planes, and source-currentness. | No implicit `latest`, no unbridged unit or plane comparison, and smallest affected refresh. |
| Integration under module-interface constraints | After assembly, a result phrase may mean role-enactability under module-interface constraints, evidence, gate, architecture, function, or work relation. | Result carry-through is not artifact-only or telemetry-only; module-interface and integration wording must recover the relation being claimed. |
| Tool-product-use chain | A design-tagged flow makes a tool; a later run or use flow uses the tool to make a chair; another flow uses the chair as context for writing a text. | One selected transformation-flow structure can relate all flows, but the same carried object may fill a run-result position in one flow and a design-side input, tool, context, or constraint position in another. The relation-position shift is explicit, tied to the flow relation and any `DesignRunTag` being used, and does not change the object's kind by wording. |
| FPF pattern-development / self-evolving specification | A development flow creates or repairs a pattern, specification, or process description through drafting, quality evaluation, publication projection, and admitted publication; a later use flow applies that product to its own `EntityOfConcern`; a defect found in use returns to the smallest development slice for repair. | Development, application, and evaluation flows are joined by transfer and return relations while keeping objects and `DesignRunTag` boundaries separate; evaluation records or use-found evidence change the product through edits to the smallest development slice, not by entering the used publication's practitioner-facing prose. |

#### E.18.1:5.4 - Filled P2W output records

Use these as replayable outputs, not as new templates.

```text
P2W output record:
  ProblemCardRef: ProblemCard@Context PC-COOL-017, accepted for a cooling-loop stabilization problem.
  CarriedDistinction: the observed deformation is not one more tuning defect; a conserved heat-flow structure must survive method comparison.
  NextFPFUseQuestion: which formal or mathematical relation is needed before method selection?
  RecoveredFPFKindOrRelation: mathematical-lens use plus `U.Signature(profile=FormalSubstrate)` declaration.
  SelectedApplication: `C.29` for preserved and lost structure; `A.6.0` for the formal-substrate declaration.
  WrittenRecordOrApplication: declare the heat-flow invariant, boundary conditions, excluded deformation factors, and practical payoff for comparator selection.
  LocalStop: method selection waits until comparator, measurement, and selected-set relations are named.
```

```text
P2W output record:
  ProblemCardRef: ProblemCard@Context PC-PORT-008, accepted for an integration-throughput problem.
  CarriedDistinction: the port-throughput phrase may carry module-interface, flow, work-plan, performed-work, evidence, gate, and architecture relations, but only one relation changes this P2W move.
  NextFPFUseQuestion: which relation is being written now?
  RecoveredFPFKindOrRelation: `A.6.M` module-interface relation plus `E.18` flow relation; `A.15.2` planning constraint is written only if the planning record is being made.
  SelectedApplication: `A.6.M` for the port contract; `E.18` for the selected transformation-flow relation; `A.15.2` only for the planned constraint.
  WrittenRecordOrApplication: write the module-interface constraint and flow relation; stop evidence and gate cues until their governing relations are being made.
  LocalStop: no readiness proof or work authorization follows from the port phrase by itself.
```

