---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "P2W Problem-to-Work Carry-Through"
section_id: "E.18.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__006_archetypal-grounding.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.18.1 — P2W Problem-to-Work Carry-Through"
  - "E.18.1:5 — Archetypal Grounding"
line_start: 83967
line_end: 84065
dependencies:
  - "A.15"
  - "A.15.PROD"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.29"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.18"
  - "E.18.3"
  - "F.17"
  - "F.18"
  - "F.8"
  - "F.9"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
keywords:
---

### E.18.1:5 - Archetypal Grounding

#### E.18.1:5.0 - Seal-failure carry-through

A maintenance team has an accepted `ProblemCard@Context` for recurrent seal failure. It records the operating conditions, the distinction between thermal deformation and material degradation, and the observations that would challenge that distinction. The team uses E.18.1 because diagnostic-method selection, repair planning, dated repair work, interpretation of the post-repair measurements, and return after a changed diagnosis all depend on preserving these accepted problem-side distinctions.

E.11.PUA may help the team inspect and apply one diagnostic-pattern candidate inside this flow. Its result might be one fit finding or one diagnostic method-selection input. That smaller result does not replace the accepted problem material, the repair plan, the repair work, or the later interpretation and return relations.


`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, an accepted problem-side record may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same record may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W application asks one question in both cases: which FPF kind or relation can carry the next claim being made?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision claim. |
| Show with P2W | The team carries one accepted claim, separates method comparison from `A.15.2 U.WorkPlan` and plan-item records, records references to dated `U.Work` occurrences while keeping those records as separate epistemes, and unpacks result relations; it writes a compact note only when replay matters. | The team separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. The practitioner preserves that claim, applies `C.29` for the mathematical-lens question, and carries the returned lens-use value or stop. A separate formal-declaration question opens under `A.6.0` and returns its own declaration result or stop; method selection waits for its own relation and participants.

2. **Planning from selected enough method.** A method family is selected enough for planning. The practitioner applies `A.15.2`; any compact P2W note cites the planning result returned there and the problem-side claim it preserves. The WorkPlan retains its own content and authority.

3. **Performed work after planning; filled positive connection.** **Readable result:** the named build `U.Work` occurrence populated the named artifact-store partition; that occurrence and the store change are connected by the declared BuildOps predicate, not by timing or the word *build*. `A.15.1` grounds `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work`. `A.3.4` separately grounds `ArtifactStorePopulationTransformation_12 : U.Transformation` as the 09:00-09:12 change of `ArtifactStorePartition_12` from no stored `ReleaseBinary_12` to stored `ReleaseBinary_12` under `BuildOpsStoreScheme-v12`. Predicate-definition episteme `BuildWorkPopulatedStore@BuildOps-v12(work, transformation)` holds only when that `U.Work` occurrence performs the governed `storeWrite` application that changes the same partition. `BuildApplication_12` supplies that performed application and its `builtBinary -> ReleaseBinary_12` binding, so C.2.1 assertion `BuildWorkPopulatedStore-12` carries the positive local work-to-change claim under `A.6.RCD` disposition 2. P2W keeps the work occurrence, transformation, and assertion separate. If the predicate or one required base fact is absent, this connection stops instead of becoming a universal work-to-change kind.

4. **Result interpretation without generic result.** The sentence *the work result proves the approach worked* does not yet name a result. Ask what can actually be asserted. `A.6.P.WMR` may return a direct subject claim, an `A.6.1` application binding, a local `A.15.PROD` or `A.6.RCD` claim, or a bounded non-assertability result. P2W carries only the returned item. `factually unsupported` and `missing-information` stop an unsupported or underinformed claim; `missing-governor` identifies the absent predicate for the stated participants and use. None becomes a generic result or production value.

5. **Functional explanatory order.** A source diagram places formal declaration, principle framing, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. The diagram helps recognize candidate continuations, but P2W carries only values returned by their direct patterns; the display order supplies no sequence or authority.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. The practitioner opens separate `A.6.M` module-interface and `E.18` transformation-flow questions. Planning, work, evidence, gate, function, and architecture cues remain stopped until their relations are asserted. Conversational P2W use or the compact note carries only the direct-pattern result that changes the present decision.

7. **Result measurement returns to planning.** A source says one `U.Work` occurrence produced telemetry and an artifact. First use `A.6.P.WMR` to separate the artifact binding, telemetry claim, and any production or unsupported claim; P2W carries those results on separate continuations. If later `C.16` measurement changes the reference plane used by planning, reapply `C.16` and `G.11`, then reopen only the planning, method-comparison, or problem-side continuation that used that plane. The earlier dated `U.Work` occurrence is not rewritten.

8. **Pump 14 pressure adjustment; governed continuation after an earlier stop.** **Readable result:** the current case record supports `W-P14-ADJUST-1010-1020 caused T-P14-PRESSURE-RISE` under `AdjustmentWorkCausesPressureRise`; P2W carries that returned result rather than inferring it from timing. Exact basis: `PumpTeam-14 : U.System` performs `W-P14-ADJUST-1010-1020 : U.Work` under assignment `RA-P14-ADJUST`, enacts `SetPointAdjustment@PlantOps-v3`, and works in `PumpStation-14` from 10:10 to 10:20 under `A.15.1`. Independently, `A.3.4` returns `T-P14-PRESSURE-RISE : U.Transformation` as the bounded change of continuing `HydraulicLoop_P14`, whose discharge-pressure characteristic changes from `belowBand` to `inBand` over the same interval. Relation-declaration episteme `P14-REL-2026`, owned by `Pump14OperationsRelations`, declares `AdjustmentWorkCausesPressureRise` for those exact participants, and a separate case fact satisfies its actual-causation predicate. In the explicitly earlier case record, `P14-REL-2026` is absent; at that epistemic stage, keep the Work and transformation separate, return `missing-governor: work-to-change claim for <W-P14-ADJUST-1010-1020, T-P14-PRESSURE-RISE>`, and route the missing declaration to `Pump14OperationsRelations`. The separate claim that `PC-P14-PRESSURE` guided `WP-P14-2026-07-15` remains `missing-governor` under A.6.P.WMR; neither the problem claim nor shared timing causes the Work. Later measurement and decision uses remain separate; no production or transformation-composition question opens.


#### E.18.1:5.2 - Additional worked situations

| Situation | P2W application | What changes |
|---|---|---|
| First-minute use | A practitioner has an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." State the accepted card, carried claim, decision or use needing the answer, and next practical question in conversation. Add a compact note only when another person or later action must replay the path. Then name one direct pattern and the result it must return, or state the stop. | Apply `C.29` to the preserved structure, lost structure, payoff, declared use, and stop condition. A later formal-substrate declaration under `A.6.0` is separate; neither continuation selects a method or writes evidence. |
| Diagram and approval note in the same source publication or source-use record | The same source publication contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the claim carried from the accepted problem card. | Diagram cue, evidence-looking cue, and gate-looking cue are separated by relation recovery; conversational use or the compact note keeps only the carried claim and current direct relation. |
| Principle story without accepted problem-side record | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the source remains a reduced-use cue until `C.22.2` or the problem-side pattern named by value accepts a problem-side record. |
| Acceptance claim with and without a governor | For `Fixture-42`, the project-local `ThermalTestAcceptanceRelations` owner governs `acceptedForThermalTest(Fixture-42, CriterionSet-T7, Campaign-T7)`. `CriterionSet-T7` requires leak rate at most `0.5 mL/min` and mounting offset at most `0.2 mm`; current measurements are `0.3 mL/min` and `0.1 mm`, so that predicate is true and P2W carries the exact positive claim. In the earlier dashboard record, only a green `accepted` label exists, the offset was measured from the wrong reference plane, and no acceptance predicate or governor is current. | Apply the direct governor in the positive case. In the earlier case, repair the measurement and return `A.6.RCD missing-governor` for the attempted acceptance claim; the label establishes no acceptance, and `C.25` is not a universal acceptance owner. |
| Changed unit after source-currentness repair | Later source-currentness repair changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated `U.Work` occurrence is cited, not rewritten. |
| Clinical differential carried into care planning | An accepted problem card distinguishes an adverse treatment effect from progression of the underlying condition. Diagnostic-method choice, care planning, performed clinical work, and outcome interpretation all depend on retaining that distinction. | The practitioner applies the clinical DPF and direct work, evidence, and measurement patterns. The problem-side claim does not grant permission to treat; a changed observation reopens the diagnostic continuation before any dependent plan, permission, or work-entry relation. |
| Learning difficulty carried into teaching and assessment | An accepted problem card distinguishes missing recall from a wrong conceptual model. Teaching-method selection, session planning, performed teaching work, and later assessment depend on that distinction. | The selected educational method and A.15 work relations keep their own values. A lesson plan or completed session does not prove changed learner capability; an assessment that challenges the distinction reopens the smallest method or problem continuation. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | The practitioner applies `C.29` for mathematical-lens use. Apply `A.6.0` separately only when the signature's subject, ranged value, and `FormalSubstrate` profile can be named; otherwise keep the signature wording as a stopped cue. P2W preserves the accepted claim across those continuations without settling empirical truth or granting permission to start work. |
| FPF relation rule changes after a P2W use | Reapply that relation's direct pattern and `A.6.REL`. If its result changed and a later continuation relied on it, record the changed result, what still follows, what no longer follows, and the smallest continuation to reopen. | The earlier use is replayed rather than trusted by age; only the changed relation and dependent continuation reopen. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, `E.18` transformation-flow relation, a dated `U.Work` occurrence, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the P2W application being made is written; the remaining readings stop as named cues until their relations and participants are stated. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side record. | The mathematical phrase lowers to a reduced-use cue; P2W does not justify method selection, evidence, gate, or `A.15.2` planning from mathematical prestige alone. |
| Result source-use relation becomes stale | A result-looking source-use relation or publication cue is later replaced by a fresher source-use relation with a different artifact reference and measurement reference. | The practitioner applies `A.15.4` appearance-based reliance repair before continuing P2W; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for transformation-flow structures and networks

These pilots are grounding checks, not source terminology to import. Before using one, decide which of three ontic cases is current: several valuations or path slices of one exact TFS; one parent-relative internal `SubflowRef`; or an E.18.NET network of independently identified TFS or nested-network members connected by exact already-obtaining cross-boundary relations. A diagram, common product, display order, shared Work or source wording decides none of them.

For one TFS, every valuation resolves to the same structure boundary and internal `U.Transfer` occurrences. For a network, every member retains its own boundary, Work, actual transformations, valuations and leaf-local position binding or `DesignRunTag`; exact cross-flow occurrences retain their direct governors, signatures, participant order and endpoint bindings. Membership is acyclic; directly governed feedback may cycle. Use a pilot to check the carried object's exact member-local position, the direct relation that crosses a boundary when one exists, and the smallest reopened member or continuation.

| Pilot | P2W use being made | What it tests |
|---|---|---|
| Coffee service TFS | Accepted `ProblemCard@Context PC-COFFEE-SERVICE-17` keeps the service-temperature and throughput problem visible while each next claim opens separately: `C.29` returns `CoffeeHeatMassBalanceLensUse-17`; `A.6.0` returns `CoffeeFormalSubstrateSignature-v3` only for its declared subject and ranged value; `A.6.1` returns `CoffeeBrewHeatTransferMechanism-v2` and exact application bindings; `A.19.UNM` returns `CoffeeTemperatureNormalization-v4`; `A.3.1` returns `CoffeeBrewMethod-v5`; `A.15.2` returns `CoffeeShiftPlan-17`; `A.15.1` returns dated `CoffeeBrewWork-17-0815`; `C.16` returns the temperature and throughput measurements; and `G.11` reopens only a continuation relying on the changed source, normalization, Method or measurement. Treat them as positions or continuations of one TFS only while every use resolves to that same exact selected structure and internal transfers. | A signature supplies no mechanism or Method; a plan supplies no Work; telemetry supplies no measurement result until `C.16` applies it; another valuation or slice does not mint another TFS; refresh changes only the relation that relied on the changed value. |
| Compiler design and run | Compiler preparation/build, later compiler use, release assurance and product operation retain independently identified TFS values when their boundaries, Work or change cadence differ. Release-assurance use, launch-gate use, reproducible-build currentness and `G.11` source-currentness remain separate claims. Select an E.18.NET network only after the exact source-use, production/inception, operation-application, evaluation or other cross-member occurrences and endpoint bindings independently obtain. | No collapse of build, run and product Work; no giant flow; no universal `produces`/`uses` edge; local `DesignRunTag`; and no transformation, production, gate or currentness result from a build arrow or intended realization. |
| TAMP and MPC robotics | Method selection and `A.15.2` planning may be revised under a declared progress or budget condition before performed Work. That planning/replanning cycle may be one TFS valuation or path-slice family when the exact structure identity is shared; separately selected development, controller-execution and evaluation flows require E.18.NET and exact cross-member relations. | Branching and cycles without a fixed work procedure; no launch decision or performed Work before dated Work occurs; and feedback cycles do not make membership cyclic. |
| AutoML and QD | Method selection returns a Pareto, QD, front or archive set under comparator and descriptor editions. If generation, evaluation and deployment are independently selected flows, relate them only through exact direct occurrences in E.18.NET. A changed descriptor, comparator or retained-set relation reopens only the dependent selection or publication continuation. | Set-return discipline, comparator currentness, no hidden scalarization, retained-set refresh, and no evaluation label used as a universal edge. |
| Freshness or physical-transport case | Work planning and performed Work depend on freshness windows, transport relations, units, reference planes and source-currentness. A detailed internal route remains a `SubflowRef`; independent transport and use flows require a network. | No implicit `latest`, no unbridged unit or plane comparison, exact member boundary, and smallest affected refresh. |
| Integration under module-interface constraints | After assembly, a result phrase may mean role-enactability under module-interface constraints, evidence, gate, architecture, function or Work relation. | Result carry-through is not artifact-only or telemetry-only; module-interface and integration wording is accepted only after recovering the exact direct relation. |
| Tool-product-use network | One member contains exact dated tool-building Work, actual substrate changes and only the A.15.PROD production/inception/completion claims that are current; another member uses the admitted tool through an exact operation-application or subject-use occurrence. In the concrete chain, a later member may use that tool to make a chair and another may use the chair as context for writing a text, but every production, use and context relation must obtain under its direct owner. | The same carried object may occupy a run-result, design-side input, tool, context or constraint position in different members without changing kind. Exact source/use/production relations connect members; a design tag, result label or adjacency does not. |
| FPF pattern development and use network | One member carries exact drafting or repair Work and episteme-edition changes; quality evaluation, publication projection, admitted publication, later application to another EntityOfConcern and use-found evaluation remain separately governed values or members when independently selected. An evaluation member may return a defect through exact source-use, evaluation and change relations to the smallest affected development continuation. | Development, publication, application and evaluation remain separate; evidence stays outside practitioner prose; repair changes the exact development object through its direct owner, not by treating the publication as acting or every edit as production. |

#### E.18.1:5.4 - Filled P2W carry-through notes

Use these as replayable filled examples, not as a second schema beside the compact note in `4.1`.

**Cooling-loop mathematical-lens continuation.**

| Compact note field | Filled value |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-COOL-017`, accepted for a cooling-loop stabilization problem. |
| Carried problem-card claim | The observed deformation is not one more tuning defect; the later method-comparison use relies on preserving the conserved heat-flow structure. |
| Receiving use | Determine the mathematical-lens result needed before any formal-substrate declaration or method comparison. |
| Next practical question | Which structure is preserved, which is lost, and where does the heat-flow lens stop? |
| Direct governing pattern | `C.29` Mathematical Lens Use. |
| Result written and use it answers | A C.29 local lens-use result naming target phenomenon, candidate mathematical object, preserved structure, lost structure, payoff, declared use, and stop condition. |
| Local stop | Method comparison waits until comparator, measurement, and candidate-set relations are named. A later `A.6.0` signature declaration is a separate continuation. |

**Port-throughput continuation split.**

| Compact note field | Filled value |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-PORT-008`, accepted for an integration-throughput problem. |
| Carried problem-card claim | The port-throughput constraint affects integration, but the source phrase does not decide which module-interface, transformation-flow, planning, work, evidence, gate, or architecture relation is current. |
| Receiving use | Make the current module-interface and transformation-flow relations inspectable without inferring readiness. |
| Next practical question | Which exact relation is being written now? |
| Continuation 1 | Apply `A.6.M` and write the exact module-interface relation for the port contract. |
| Continuation 2 | Apply `E.18` and write the exact transformation-flow relation that uses that interface. |
| Stopped cues | Apply `A.15.2` only if a planning constraint is actually being written. Evidence, gate, and architecture cues remain stopped until their direct relations are current. |
| Local stop | No readiness result, granted permission, performed-work claim, evidence verdict, or gate decision follows from the port phrase by itself. |

