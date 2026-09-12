---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:4"
section_title: "Solution - selected answer"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__006_solution-selected-answer.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:4 — Solution - selected answer"
line_start: 59192
line_end: 59838
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "B.5.MPC"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18.1"
  - "C.19.1"
  - "C.2.P"
  - "C.26"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "C.31.ASAP"
  - "C.39"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "F.19"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
---

### C.29:4 - Solution - selected answer

#### C.29:4.1 - Construct and test the correspondence

1. **State the working question.** Name the quantity, relation, distinction or possibility that would change the next action. Recover the intended use and the precision or range it needs.
2. **Choose a concrete mathematical object.** Specify its elements, variables, relations, operations and constraints. Use the least costly adequate local theory or construction. A family name is a discovery cue; if no object is yet available, keep a candidate and name the next observation or construction.
3. **Establish the correspondence.** Say what each relevant element or operation represents and in what direction the inference is used. Distinguish an analogy, a fitted representation, a simulation and an exact structure-preserving map. State the assumptions, scale and context that the correspondence requires.
4. **Determine what the correspondence preserves, omits or introduces.** Identify the structure on which the intended result relies and any omitted distinction that could change it. Establish the preservation claimed for the needed operations. If the receiving domain adds objects or operations, determine which of their results answer the source question. C.29.1 constructs these comparisons, including cases with no loss of source distinctions and cases where a receiving solution has no source counterpart.
5. **Do the mathematical work.** Calculate, derive, construct or demonstrate the obstruction. For a missing computational formulation or procedure, use C.29.2; for an unsettled connection to an executing system, use C.29.3. Return the result through the correspondence to the working question. A statement that a queue “exposes bottlenecks” is not yet the bottleneck calculation.
6. **Choose the resulting action and its limit.** Use the result within its assumptions, collect a discriminating observation, compare a relevant rival, narrow the question or reject the representation. Test the material loss and changed premises. When another person or later use needs the account, retain the smallest sufficient record under :4.4.

##### C.29:4.1.1 - Transfer the result through the operations

A source operation or result is available, and you need to use it through another representation. Use **C.29.1 - Mathematical Result Transfer** to recover the operation and its permissions, compare performing then mapping with mapping then performing, and test whether choosing another represented source case changes the answer.

Its Solution constructs a transferable consequence, a justified bound or a specific repair of the correspondence. It also separates a receiving operation that gives a useful relaxation from one whose result can be realized as a source action. The reservation and route-cost entries in :7.1–:7.2 lead to its worked constructions.

##### C.29:4.1.2 - Construct a computation for the question

The needed answer is identified, but the available representation and operations do not yet explain how to obtain it. Use **C.29.2 - Computational Formulation** to select the distinctions retained in computational state, construct a procedure or solver formulation, establish the claimed result and estimate the cost that matters to its use.

Its Solution starts from either a question or available computational means. Worked cases develop an interpreter, a bounded root calculation, a memory-limited quantum-state representation, two questions about the same circuit, and a probability estimate. The result is a usable computation under stated conditions or the missing construction that prevents it.

##### C.29:4.1.3 - Realize the computation and read its result

A computation is available, but how a concrete system performs it is unsettled. Use **C.29.3 - Computational Realization** to connect input preparation, system actions and result interpretation, then compare the required result with the interpreted execution. For a design calculation, the comparison uses the supplied system model; a claim about an actual run uses its observations.

The result is a conditional realization, an interpreted result or a located failure in preparation, operation or readout. Digital, analog, stochastic and manual arrangements can enter through the same question. Its robot, analog addition and admission-card cases show repairs of range, scale and shared-state conditions. B.5.MPC coordinates these results with the physical account, mathematical construction and receiving action.

#### C.29:4.2 - Mathematical Lens Use Principle

A mathematical lens is useful for a stated question when its correspondence preserves the structure needed for an actual consequence and makes the material losses explicit. A proof under mathematical assumptions establishes that consequence inside the model. Reliance on the phenomenon additionally requires the correspondence and application conditions to hold; prediction and other model-bearing uses require their validation under :4.5a.

Plain phrases such as “what survives transfer” can guide recognition. For a used result, make the actual correspondence, preserved structure, loss and stopping condition recoverable. Include a blocked overread only when it passes F.19's plausible-reader test.

#### C.29:4.2a - When mathematicalization pays

Introduce a representation when it changes what can be derived, compared, observed, constructed or ruled out for the working question. An adequate ordinary calculation may already supply the answer. If no useful consequence or next inquiry follows, keep ordinary prose or the domain result; no C.29 output is required.

#### C.29:4.2b - Discover a candidate from the working cue

Choose the row that fits the problem, or use a closer domain construction. The menu is informative; when a listed construction is used, its named mathematical elements and conditions must be supplied. The shared test is :4.1, not membership in this list.

| Working cue | Candidate structure and first mathematical work | Conditions that can change the use |
| --- | --- | --- |
| Waiting, backlog, throughput | Queue or flow network: identify stations, routing, arrivals, service and waiting; derive a capacity bound or waiting relation. | Check discipline, batching, rework, finite buffers and station availability before applying the result. |
| State change, trajectory, stabilization or control | State space, Markov model, ODE or control model: name state, transition law and constraints; add an observation map when the receiving use needs it. | A.3.3 supplies dynamics semantics; C.27.TA and C.27 apply to the temporal aspect and temporal-use claim being made. |
| Conditional independence or computational-boundary cue | Probabilistic graph, Markov blanket or active-inference model: state variables, conditional-independence assumptions, observation/action partition and model boundary. | Recover a separately claimed physical interface, component or agency condition through its direct pattern. |
| Dependency, interface, composition or change of algebra | Graph, hypergraph, category, operad, optic or semiring: state edge/slot meanings, objects, morphisms, identities, interface conditions and composition laws; test the required composition or transform. | Classical, tropical, Fourier–Laplace or Legendre transforms can change the retained law. F.9 supplies cross-context semantic correspondence when needed. |
| Local-to-global flow or balance | Boundary operator, exterior derivative, divergence or Stokes-like construction: name domain, boundary, field/form/flow, local operator, boundary conditions and source or conservation balance. | The chosen domain law and regularity assumptions must support the global inference. |
| Local rule with no global extension | Cohomology, closed/exact distinction or another obstruction: identify the cycle/cocycle, equivalence class, local closure and failed global witness. | Use the obstruction to delimit this transfer; the failure does not select the rival model or identify a cause. |
| Sameness under transformations | Group action, symmetry, invariant or equivariant representation: identify transformations, action on variables and preserved quantity; derive a conservation link only under its theorem's assumptions. | State coordinate details and distinctions lost; a physical conservation claim needs its domain basis. |
| Extremum, trade-off, potential or dual view | Variational, Lagrangian/Hamiltonian, action, energy, free-energy, loss, value or entropy functional; constrained optimization or Legendre/convex duality. Name variation space, constraints, boundary conditions and stationarity/extremum or dual transform. | A system's actually following that extremum is a separate dynamics or causal question. |
| Similarity, distribution shift, population or shape movement | Metric, topology, order, embedding, coupling or optimal transport: define neighborhood/distance or transport plan, conserved mass and cost; calculate the comparison. | State what is transported and lost. C.16 supplies a used measurement/comparability construction; a policy effect or fairness claim needs its own argument. |
| Scale transition, coarse behavior, universality or knee | Coarse-graining, RG or fixed-point view: name scale variable/window, coarse-graining rule, fixed point or attractor, basin/regularity assumptions and invariant or exponent. | Return to the microdescription when an omitted distinction matters. C.18.1, C.19.1 and C.31.ASAP supply the separately claimed scale-law, method preference and architecture preference results. |
| Self-reference or a universal evaluator | Diagonal, self-application or fixed-point construction: specify encoding, evaluator/self-map, tested universal claim and exact obstruction. | A recursive-looking loop alone does not establish a no-go result. |
| Uncertainty, missing observation or next sample | Probability/information measure, Bayesian workflow, BED/OED, active learning or Bayesian optimization: state variables, priors/likelihood, utility or information criterion, design/acquisition variable and estimation method. | Check prior-data conflict, predictive mismatch, estimation cost, uncertainty and robustness to model/noise error; use the result within its validation boundary. |
| Recoverable structure under a resource bound | MDL, epiplexity or another code/measure: name source episteme/trace, observer, admissible model/coding scheme and execution bound; distinguish selected structure from residual description. | Apply the correspondence and observation/postulate boundary in :4.2c; return to source when the discarded structure matters. |
| Learning update, curvature or optimization trajectory | Information geometry or a learning-dynamics model: specify update variables, metric/noise relation and the property being calculated. | Establish the mapping to the particular learning process before using the result beyond the formal model. |
| Nonlinear dynamics needing a tractable observable | Koopman/operator, DMD or system-identification construction: select observables, operator and approximation; derive the forecast or diagnostic consequence. | Finite closure and predictive/control validity need checking; A.3.3 and C.27 supply the actual dynamics and temporal-use conditions. |
| Learned scientific representation or surrogate solver | Neural operator, latent representation, embedding or world model: specify function/state/field mapping, observation map, training or simulation regime and resolution policy. | Apply :4.5a's learned-lens and validation conditions, including generalization scope and approximation loss. |
| Intervention, policy effect or counterfactual | SCM, causal graph or micro-to-macro causal abstraction: specify assignment/intervention, outcome and preserved or approximated intervention/counterfactual structure. | C.28 supplies identification and causal-use justification; an associative graph or latent manifold may not answer this question. |
| Probe, order or context effect with incompatible frames | Quantum-like or contextual-probability model: identify the contextual obstruction that still changes inference or action after the ordinary subject patterns. | Apply C.26's adequacy conditions. A physical quantum claim additionally needs the relevant physics and observations. |
| Storage, computational or realizability limit | Count actual represented objects and operations; apply a resource bound or constructive/impossibility argument. | Recompute for the actual alternative representation. A valid rejection of one implementation does not yet supply a feasible replacement. |

For a first candidate, compare with ordinary prose, direct observation or the accepted domain model before a broader survey. When the question is a tradition-scale source synthesis, use G.2; C.29 needs only the candidate or rival relevant to this working question.

#### C.29:4.2c - Bounded-observer structural-information lens

Use this subcase when a mathematical lens estimates, compresses, codes, compares, or otherwise exposes how much selected structure a bounded observer can recover from a description, relation trace, generated graph, model, or reusable-structure accounting result. Typical examples include MDL-like two-part codes, epiplexity-style extracted-structure estimates, compression-complexity comparisons, and information-functionals over relation graphs.

`C.2.8` defines extractable structural information for the episteme, expressing form and observer under stated conditions. When this lens output is used to estimate that characteristic, state how its mathematical objects, admissible models, selected structure and resource bound correspond to those conditions. A comparison that uses an adequate domain method directly needs no mathematical lens.

For an epiplexity estimate, distinguish the selected model's description length from the residual data description, the model-execution bound from estimation effort, and conditional model information from all familiar structure a reader can recover. Use the existing source, mapping, preserved/lost-structure and stop fields to state the correspondence. The formal model and its application conditions are explained in `C.2.8:4.6`; a numerical measurement claim also uses `C.16`.

Minimum record:

```text
MathLensUse.StructuralInformationLensUse@Context:
  TargetPhenomenon:
  SourceEpistemeOrTraceRef:
  BoundedObserverRef or observerBoundary:
  CandidateMathObject:
  LensMappingMode:
  PreservedStructure:
  LostStructure:
  VisiblePayoff:
  ObservationBoundary?:
  PostulateBoundary?:
  SourceReturnCondition?:
  LensUseBoundaryValue:
  declaredLensUse:
  StopCondition:
  blockedLensOverread?:
```

When the target is a physical, organizational, or project-world situation, the record must say whether the structural-information claim is observational, postulated, simulated, or only a description-local compression. When the lens is used in architecturing, `C.30` governs architecture as EntityOfConcern, `C.30.ASV` governs structural-view adequacy, `C.30.AD` governs architecture descriptions, and `C.31` or `C.31.RSA` governs modularity or reusable-structure accounting. `C.29` records only the declared lens use: what recoverable structure the mathematical lens makes visible, what it loses, and where that use stops.

#### C.29:4.2d - Architecture-local lens descriptions

Architecture work may use C.29-local descriptions for graph, flow, control, structural-information, RG or coarse-graining, and multilevel-learning or frustration lenses.

| Local C.29 description | Candidate mathematical object | Visible payoff | Stop condition |
| --- | --- | --- | --- |
| `MLU.Description@ArchitectureGraphDSM` | typed graph, hypergraph, DSM, DMM, or MDM matrix | dependencies, clusters, change propagation, and bottlenecks | for semantic interface correctness, compositional quality, or an architecture decision, apply the pattern for that separate claim |
| `MLU.Description@TransformationFlowStructure` | graph, morphism-family, wiring, matrix, or network expression over a selected `TransformationFlowStructure` | flow topology, crossings, carried relations, and path slices without hidden scalarization | for a Work occurrence, gate decision, or evidence claim, apply its subject pattern |
| `MLU.Description@ArchitectureLCA` | layered control structure or multi-rate control model | planner, regulator, plant, observer, feedback timing, and externality separation | stability or causal-use questions require their dynamics, evidence, and `C.28` basis |
| `MLU.Description@EpiplexityStructuralInformation` | bounded-observer structural information or two-part code | learnable reusable structure versus residual or unmodeled structure | establish any utility, assurance, out-of-distribution guarantee, or causal-proof claim through its subject pattern |
| `MLU.Description@RGArchitecture` | scale map over architecture descriptions, fixed-point or basin metaphor, or declared coarse-graining map | scale-stability of an architecture vector and exploding exceptions | a literal physical-RG claim requires its domain theory |
| `MLU.Description@MultilevelLearningFrustration` | multilevel learning over structurally renormalizable descriptions, frustrated optimization landscape, or variational residual model | residual-reducing architecture moves across declared scopes or holon levels | a project-wide optimization claim requires a separately justified global function |

`MLU.Description@RGArchitecture` applies only when the use names a declared aggregation scope, scale variable or scale window, coarse-graining rule, preserved structure, lost structure, source-return condition, declared use, and stop condition. Include a blocked overread only when it passes F.19's plausible-reader test. If the claim becomes a scale-preference claim, `C.31.ASAP` governs the architecture preference side; C.29 keeps the declared mathematical-lens use.

Minimum RG architecture description:

```text
MLU.Description@RGArchitecture:
  TargetPhenomenon:
  CandidateMathObject:
  LensMappingMode:
  ScaleWindow?:
  CoarseGrainingRule?:
  PreservedStructure:
  LostStructure:
  VisiblePayoff:
  SourceReturnCondition?:
  declaredLensUse:
  NextLensUseAction:
  StopCondition:
  blockedLensOverread?:
```

For architecture work, a common RG-shaped candidate object is:

```text
A_l = (Holons_l, FunctionalRelations_l, FlowRelations_l, ControlRelations_l,
       ModuleRelations_l, InterfaceSpecificationRefs_l, DependencyEdges_l,
       WorkMethodRefs_l, EvidencePackageRefs_l, QualifierRefs_l)

R_l : A_l -> A_{l+1}
```

`InterfaceSpecificationRefs_l` contains only governed `U.EpistemeRef` values that resolve independently identified `InterfaceSpecification` epistemes under the identifying rule located at A.6.M. The references, their resolution, and the specification content remain separate; changing a lens token or retargeting a reference does not edit the specification.

The index `_l` is a declared aggregation-scope index inside this C.29 lens, not a generic level, tier, layer, or ladder. Each use names the aggregation scope, the coarse-graining rule, the lost structure, and the source-return condition.

`MLU.Description@MultilevelLearningFrustration` applies only when the use names declared holon levels or declared scopes, a mapping between them, conflicting constraints or residuals, preserved structure, lost structure, and the nearest neighboring FPF pattern for any measurement, causal, evidence, assurance, work, selected-set, or decision claim.

Minimum multilevel-learning and frustration description:

```text
MLU.Description@MultilevelLearningFrustration:
  TargetPhenomenon:
  CandidateMathObject:
  LensMappingMode:
  PreservedStructure:
  LostStructure:
  VisiblePayoff:
  declaredLensUse:
  NextLensUseAction:
  SourceReturnCondition?:
  StopCondition:
  blockedLensOverread?:
```

Declared lens use: triage, explanation, candidate generation, rival-lens comparison, scale-window reasoning, source-return triggers, and architecture-decision rationale only when the neighboring pattern defines or constrains any non-C.29 claim. Stop or return when the mapping, scale window, preserved structure, or source basis no longer supports the use. A causal-proof, assurance-score, or necessary-complexity-growth claim needs its own argument and source basis. Apply `C.11`, `C.28`, `B.3`, `C.16`, `G.5`, or the applicable stakeholder or ethics pattern when its respective non-C.29 claim is current. Include a project-wide-optimizer or other blocked overread only when it passes F.19's plausible-reader test.

#### C.29:4.3 - Use boundary

Use C.29 for a consequential choice or transfer of mathematical representation. Ordinary equations, data structures and accepted domain models remain usable directly when no such issue is open. A separate causal, measurement, dynamics, semantic-bridge or other claim uses its subject pattern under :4.4.6.

Use **structure-preserving representation** in discoverability-bearing prose unless equivalence or identity is explicitly the justified mapping mode.

#### C.29:4.4 - Record the result for its receiving use

First complete or delimit the mathematical move in :4.1. Record its question, concrete object, correspondence, retained and lost structure, consequence and next action when another reader or later reliance needs them. Choose the smallest sufficient form below; a form does not replace a missing construction, derivation or observation.

**One reliance rule.** A conditional derivation, diagnostic comparison or reusable explanation may remain a MiniCard when it retains the same object, assumptions, correspondence, loss and narrow use, and its consequence is used to understand the model or choose the next inquiry. A FullCard is required when the result is relied on as an adequate model of the phenomenon for prediction, an operational or consequential decision, model adoption, benchmark or assurance input, Bridge-dependent reliance, or transfer as a reusable model to further cases. It then needs the applicability, rival and validation information relevant to that reliance. Publication or repetition of the same conditional explanation alone does not change its class.

Keep adequate existing domain/model documentation and refer to it; FullCard means a recoverable full account, not recopying that information into a blank form. Reassess the same rule whenever the intended use or reliance changes.

Application output classes:

| Output class | Output | Use condition | Required content |
|---|---|---|---|
| `NoMathLensUseNeeded` | No C.29 output; keep the ordinary local result or Plain orientation | Accepted local mathematics or didactic language makes no separate lens-use claim requiring resolution. | Finish with the local result. A short `NoMathLensUseNeededNote` is useful only when a proposed or disputed lens use needs an explanation; it is not a certificate required for ordinary local mathematics. |
| `LensCandidateNote` | `MathLensUse.LensCandidateNote` | A problem whose next lens-use action can depend on a mathematical lens is stable enough for a first candidate lens, but no adequate mathematical object has been named yet. | `TargetPhenomenon`, `ProblemStructureCue`, `CandidateLensFamily`, optional `CandidateMathObject?`, `WhyThisLensCouldHelp`, `ExpectedVisiblePayoff`, `ObservableOrControllableCue?`, `NextLensUseAction`, `OrdinaryRivalOrFallback`, `StopCondition`, `NextMathLensUseOutput`. |
| `OneLine` | `MathLensUse.OneLine` | A concrete object and correspondence can support a bounded first inspection or repaired phrase; adequacy for further reliance remains open. | `TargetPhenomenon`, `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `VisiblePayoff`, `NextLensUseAction`, optional `ObservationOrReadoutNeeded?`, `OrdinaryRivalOrFallback`, `StopCondition`. |
| `MiniCard` | `MathLensUse.MiniCard` | Conditional derivation, diagnostic comparison, choice of a next inquiry, or reusable explanation within the same declared assumptions and losses. | `OneLine` content plus `InvariantsExposed`, `LensUseBoundaryValue`, `declaredLensUse`, optional `blockedLensOverread?`, principal rival, and `RivalLensRelation?` when another mathematical lens changes the bounded action. |
| `FullCard` | `MathLensUse.FullCard` | Reliance on the result as an adequate phenomenon model under the rule above. | Full `MathLensUse.Card@Context`, using existing references where adequate, plus the applicable overlays and receiving subject-pattern result. |
| `NeighborGoverningPatternNote` | `NeighborGoverningPatternNote` | The next action concerns a separately governed question. | Name that question and follow its receiving action in :4.4.6. |

Micro-template examples:

Architecture and P2W first-use slice:

```text
MathLensUse.LensCandidateNote@ArchitectureP2W := {
  TargetPhenomenon: cooling-fixture deformation problem accepted as a problem-side distinction,
  ProblemStructureCue: heat-flow balance, boundary condition, interface reference plane, and deformation residual change the next architecture or method-choice question,
  CandidateLensFamily: boundary and variational heat-flow lens,
  CandidateMathObject?: temperature field with boundary-condition relation and optional energy functional,
  WhyThisLensCouldHelp: the lens can expose whether the useful distinction is a preserved heat-flow invariant, a boundary-condition mismatch, or a deformation factor outside the model,
  ExpectedVisiblePayoff: a net heat-flow imbalance would require stored-energy change; a balanced total alone would still leave the spatial gradient needed for the deformation question unresolved,
  ObservableOrControllableCue?: boundary temperatures, heat-flow observations, reference-plane assignment, deformation readout,
  NextLensUseAction: define the fixture control volume and heat paths; compare measured inflow and outflow, then obtain spatial temperatures and mechanical constraints before deriving deformation,
  OrdinaryRivalOrFallback: ordinary deformation narrative plus local measurement note,
  StopCondition: keep this as a candidate until the heat balance and temperature-to-deformation correspondence are specified; return to the deformation question when omitted gradients or constraints can change its answer,
  NextMathLensUseOutput: MathLensUse.OneLine or NeighborGoverningPatternNote
}
```

The heat balance is the proposed first mathematical operation. A formal vocabulary/law declaration uses A.6.0 only when that separate declaration is needed; carrying accepted problem-side distinctions into later work uses E.18.1. The receiving conditions are stated in :4.4.6.


```text
MathLensUse.LensCandidateNote example := {
  TargetPhenomenon: slow Product-X team flow,
  ProblemStructureCue: waiting and work-in-progress look more important than individual task difficulty,
  CandidateLensFamily: queue or flow lens,
  CandidateMathObject?: single-server or multi-server queue candidate,
  WhyThisLensCouldHelp: arrivals, service time, WIP, and waiting time could expose the bottleneck,
  ExpectedVisiblePayoff: decide whether delay is arrival-rate, service-rate, batching, or WIP-boundary pressure,
  ObservableOrControllableCue?: arrivals, service time, wait time, WIP limit,
  NextLensUseAction: observe the variables before claiming queue adequacy,
  OrdinaryRivalOrFallback: ordinary process narrative without queue assumptions,
  StopCondition: stay with the candidate note until observations support queue adequacy; use the ordinary process narrative if the queue candidate does not change the next action,
  NextMathLensUseOutput: NoMathLensUseNeededNote or MathLensUse.OneLine after observation
}
```

```text
MathLensUse.OneLine example := {
  TargetPhenomenon: Product-X backlog delay,
  CandidateMathObject: queue model over arrivals, service time, waiting time, and work in progress,
  LensMappingMode: representation,
  PreservedStructure: flow, bottleneck candidates, wait, WIP, service-rate pressure,
  LostStructure: motivation, priority politics, contractual duties, skill learning, quality of work,
  VisiblePayoff: identify whether delay is arrival-rate, service-rate, batching, or WIP-boundary problem,
  NextLensUseAction: observe arrivals, service, wait, and WIP; test one local WIP-limit or batching hypothesis,
  ObservationOrReadoutNeeded?: service-time and wait-time observations,
  OrdinaryRivalOrFallback: process narrative without queue assumptions,
  StopCondition: return to the process narrative or choose another lens when observations do not support the queue representation or its declared losses prevent the next action
}
```

**Worked conditional queue comparison.** A production manager asks whether speeding station A would raise the line's output, or whether the next investigation should focus on B. Use an authored, stipulated case: identical jobs arrive at `a_n = 10n` minutes, starting with `n = 0`, and pass through A then B. Both stations have one server, first-come-first-served non-preemptive service, no failures or rework, and an unbounded intermediate queue in the model. For a finite run the same calculation applies while its actual buffer does not fill. Transfer time is zero. A takes 10 minutes per job; B takes 15. The line starts empty.

The mathematical object is a deterministic two-station tandem queue. A job represents one part; an arrival is its release to A; service is uninterrupted processing at the named station; a departure from A is the arrival at B. This preserves order, routing, occupied service time and interstation waiting. Variable product mix, stoppages, rework and finite-buffer blocking are omitted. The network correspondence and the importance of blocking are introduced in [Wu's queueing-network lecture, slides 9 and 23–24](https://web.mit.edu/1.041/spring2023/lectures/L10-queuing-network-models-2023sp.pdf); the following deterministic numbers and derivation are constructed here.

A job can start only after it has arrived and the previous job has left that station. With previous departures initialized to zero, its departure times therefore obey:

```text
d_A(n) = max(a_n, d_A(n−1)) + 10
d_B(n) = max(d_A(n), d_B(n−1)) + 15
d_A(−1) = d_B(−1) = 0
```

| Job n | Arrival a_n, min | Departure A, min | Departure B, min | Total latency, min |
| --- | --- | --- | --- | --- |
| 0 | 0 | 10 | 25 | 25 |
| 1 | 10 | 20 | 40 | 30 |
| 2 | 20 | 30 | 55 | 35 |
| 3 | 30 | 40 | 70 | 40 |

The recurrence gives `d_A(n) = 10n + 10` and `d_B(n) = 15n + 25`: after its first arrival B remains occupied. The output spacing is 15 minutes, hence the long-run rate is 4 jobs/hour. The station-capacity bound is `min(6, 4) = 4` jobs/hour, attained in this stipulated run. Latency is `d_B(n) − a_n = 25 + 5n` minutes. It keeps growing; the calculation supplies no finite steady-state mean delay.

Now halve A's service time to 5 minutes while leaving the arrivals and B unchanged. The same recurrence gives `d_A(n) = 10n + 5` and `d_B(n) = 15n + 20`. The rate is still 4 jobs/hour; each job's latency falls by 5 minutes but still grows with n. The useful distinction is between a shorter initial traversal and a higher sustained output rate. The next inquiry is therefore to observe B's service, interruptions and queue growth, and test whether its assumed restriction describes this line. An observed-output dashboard is the ordinary fallback and a complementary check; output counts alone do not derive the two station-change scenarios.

**Use and return.** This is a MiniCard-level conditional derivation and comparison, reusable with the same premises. It directs observation, not a capacity commitment about an unvalidated line. Actual prediction, equipment selection or operational reliance uses :4.4's full applicable account and :4.5a's validation. Keeping A's original 10-minute service, if an omitted inspection adds 5 minutes to every B service, B's service becomes 20 minutes: `d_B(n) = 20n + 30`, the rate is 3 jobs/hour and latency is `30 + 10n`. Withdraw the 4-job/hour and `25 + 5n` results. If finite storage instead blocks A, reconstruct the blocked-service recurrence before reusing the schedule.

```text
MathLensUse.OneLine := {
  TargetPhenomenon,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  VisiblePayoff,
  NextLensUseAction,
  ObservationOrReadoutNeeded?,
  OrdinaryRivalOrFallback,
  StopCondition
}
```

For `MathLensUse.OneLine`, `VisiblePayoff` says what the lens makes visible, such as a bottleneck, invariant, obstruction, incompatibility, loss boundary, or diagnostic split. `NextLensUseAction` says the now-bounded user-facing action, such as compute a local quantity, compare only inside a declared structure, run a validation slice, apply a neighboring pattern, keep the phrase as local metaphor, or remove the phrase from claim-affecting use. `ObservationOrReadoutNeeded?` names the missing observable, readout, assignment, outcome, validation slice, or scale point needed before the repaired line makes the stated action usable. `OrdinaryRivalOrFallback` says what the reader would use without this mathematical lens: ordinary prose, accepted local domain theory, direct measurement, a causal model, a queueing model instead of a quantum-like metaphor, an `A.19` space declaration instead of `C.29`, or an `F.9` bridge instead of category-like wording. If two mathematical lenses already change the next action at this cheap-output class, add one ordinary-language note about the disagreement and use `MathLensUse.MiniCard` or `MathLensUse.FullCard` before claiming a reusable rival-lens relation.

```text
MathLensUse.LensCandidateNote := {
  TargetPhenomenon,
  ProblemStructureCue,
  CandidateLensFamily,
  CandidateMathObject?,
  WhyThisLensCouldHelp,
  ExpectedVisiblePayoff,
  ObservableOrControllableCue?,
  NextLensUseAction,
  OrdinaryRivalOrFallback,
  StopCondition,
  NextMathLensUseOutput
}
```

`MathLensUse.LensCandidateNote` is a cheap first-candidate lens selection note. Its successful next outputs are `NoMathLensUseNeededNote`, `MathLensUse.OneLine`, or a named neighboring subject-pattern note.

Do not use `MathLensUse.OneLine` with an empty `CandidateMathObject`. If the candidate object has not yet been named, use `MathLensUse.LensCandidateNote` first, keep ordinary prose, or write a `NeighborGoverningPatternNote` when a non-lens claim is being made.

Cheap stop: if the mathematical phrase does not affect any claim beyond orientation, do not use the full card. If the first honest output is `NoMathLensUseNeededNote`, that is a successful `C.29` result, not an underfilled card.

#### C.29:4.4.1 - Output set and declared-use boundary

Use the single output/reliance rule in :4.4. The form states the mathematical account; a used empirical, causal, semantic-bridge, assurance or decision result additionally needs its subject-pattern basis in :4.4.6.


`LensMappingMode`, `LensUseBoundaryValue`, and declared lens use are separate fields.

| Lens-use aspect | Question it answers | Where it is recorded |
|---|---|---|
| Mapping construction | How does the mathematical object represent, abstract, embed, quotient, simulate, learn, or transfer the phenomenon? | `LensMappingMode`, `PreservedStructure`, `LostStructure`, and any `ScaleWindow?` or `CoarseGrainingRule?`. |
| Lens-use boundary value | What limited lens-use value is declared for this use? | `LensUseBoundaryValue`, validation overlay when validation use is being claimed, and neighboring evidence or assurance patterns when their claims are being made. |
| Declared lens use | What can the working reader now do, and when must the use stop or return? | `declaredLensUse`, `NextLensUseAction`, `StopCondition`, optional `blockedLensOverread?`, and named governing FPF patterns. |

`LensMappingMode` names construction, not permission. Typical local values include `representation`, `abstraction`, `quotient`, `coarse-graining`, `embedding`, `homomorphism`, `isomorphism`, `functor-like transfer`, `simulation`, and `learned or fitted representation`. A broad family name such as graph, field, category, geometry, quantum-like, variational, or Bayesian is only a prompt until the concrete construction and preserved structure and lost structure are named.

`LensUseBoundaryValue` declares only a limited lens-use boundary:

| `LensUseBoundaryValue` value | Declared use | Stop or neighboring-pattern condition |
|---|---|---|
| analogy-only prompt | orientation, hypothesis generation, recognition cue | decision, assurance, causal claim, or publication as established model |
| diagnosticOnly | finding a candidate obstruction, bottleneck, mismatch, missing state variable, or rival-lens split | prediction, decision, causal use, bridge substitution, assurance, or ontology without the neighboring-pattern result named by value |
| formal derivation inside accepted theory | local explanation or theorem-backed transfer when assumptions hold | empirical claim without observation or evidence |
| simulation | candidate model and scenario exploration | real-world causal or predictive reliance without validation |
| empirical fit | local prediction inside validation regime | out-of-regime generalization and causal use |
| accepted domain theory | local domain model use | cross-context ontology import |
| SoTA-echo candidate | structured exploration and lens-use testing | accepted FPF law, assurance, release, or foundation claim |
| mechanized proof | formal property under assumptions | real-world adequacy unless assumptions and evidence hold and any needed semantic Bridge is established |

State the declared lens use in `declaredLensUse` and its stopping or return boundary in `StopCondition`. Elegance, familiarity, source prestige, and mapping type supply no substitute for that declaration. Include `blockedLensOverread?` only when it passes F.19's plausible-reader test.

#### C.29:4.4.2 - From lens to local action

A consequence can direct a new observation, make a bounded comparison possible, expose a bottleneck or obstruction, or reject a candidate representation. State which of these happens and why. If the requested result is a plan, decision or other neighboring result, supply the mathematical consequence to that result under :4.4.6.

**Worked local bottleneck: dense-state storage.** A proposed dense pure-state representation for 50 qubits contains `2^50` complex amplitudes. At a stipulated 16 bytes per amplitude, its array alone requires `16 × 2^50 = 2^54` bytes, or `16,777,216 GiB`. A 64 GiB implementation cannot hold it. Counting the representation's elements and multiplying by storage per element identifies this bottleneck before implementation.

Recover the requested observable or property, then reconsider which structure must be represented. A restricted case, another representation or a justified approximation may change the resource demand; estimating each actual candidate's storage and work can change the choice. When a particular representation change has been chosen, [A.6.3.RT:4.1][fpf-a6-3-rt-4-1-ref] supplies the conversion and preserved/lost-content check. Until a suitable domain algorithm is supplied, the present result is rejection of the dense implementation and a specific representation question. Ordinary storage arithmetic alone needs no lens card.

#### C.29:4.4.3 - No-lens entry: choosing a first candidate lens

Use this when the next lens-use action can benefit from a mathematical lens but no adequate mathematical object has been named. The output is `MathLensUse.LensCandidateNote`, not `MathLensUse.OneLine` and not a full card. State the `ProblemStructureCue`, choose one cheap `CandidateLensFamily`, say what it could make visible, name the `ObservableOrControllableCue?` when available, state the `NextLensUseAction`, compare it with the `OrdinaryRivalOrFallback`, and stop if no action changes. If the cue is still pre-articulation and no stable `ProblemStructureCue` can be named, do not mathematize it; preserve cue plurality through `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state pattern before applying `C.29`.

Use the single discovery menu in :4.2b. Compare one candidate with the ordinary fallback; broaden the search only when this comparison leaves a material question unresolved. Asking what can be observed or varied does not by itself require a measurement or experiment record; apply its subject pattern when constructing that result.

#### C.29:4.4.4 - First honest C.29 entry cases

For E.11-style first-entry recognition, distinguish the working entry case before choosing an output:

| First honest entry case | What the working reader met | First `C.29` answer |
|---|---|---|
| Pre-articulation cue | Something feels structurally wrong, but it is not yet a claim and no stable `ProblemStructureCue` can be named. | Do not impose a mathematical lens. Use `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state pattern first; apply C.29 only when the problem structure is stable enough. |
| No lens or under-lensed problem | A problem situation is stable enough for mathematical help, but no `CandidateMathObject` has been named. | Use `MathLensUse.LensCandidateNote`: `ProblemStructureCue` -> `CandidateLensFamily` -> `NextLensUseAction`. |
| Under-specified lens | A phrase such as field-like, graph-like, or quantum-like appears, but no object, mapping, preservation, or loss is stated. | Keep a `LensCandidateNote` while the object is missing. Use `OneLine` only after the object and correspondence can be supplied; otherwise keep ordinary prose. |
| Useful lens with overread | A useful conditional result is presented for a use its assumptions or correspondence do not support. | Narrow the claim and use the corresponding class in :4.4, or establish the fuller reliance through its required basis and receiving subject pattern. |
| Ordinary local math | A Markov kernel, ODE, graph data structure, or accepted domain theory appears inside its local domain use. | Stay with the local pattern and finish its result without a C.29 note or card. A separate proposed or disputed transfer retains the explanation, lost-condition examination, and validation required by that use. |
| Wrong first pattern | The reader reaches for `C.26`, `F.9`, `C.28`, `C.16`, or `A.3.3` before knowing whether mathematical-lens use is being made, or reaches for `C.29` when a neighbor already governs. | Name the first subject pattern and state what `C.29` contributes, if anything. |

#### C.29:4.4.5 - False-positive bank and entry stops

An ordinary ODE in physics, a Markov kernel in local stochastic dynamics, a graph data structure, an A.19 distance/topology/order/embedding, a category-theoretic proof internal to its domain, or a one-off teaching metaphor needs no C.29 output merely because mathematics appears. The same applies to Markov-blanket wording used only to recognize a physical interface or boundary already recovered through its subject pattern.

Enter C.29 when a separate representation or transfer issue affects the result: unexplained waiting may need a queue construction; an important comparison may need a distance with explicit losses; transferring the same graph between contexts may need both mathematical correspondence and F.9 semantics. A learned representation used for scientific explanation needs :4.5a's observation and validation conditions. A scale claim needs the applicable scale-law or preference argument in :4.4.6.

If the cue is still “something is off” and no stable structural question can be named, keep the language-state work open under :4.4.3. An inconclusive candidate, a rejected lens, an ordinary local answer and a receiving subject-pattern result are all useful stopping points.

#### C.29:4.4.6 - Subject-pattern boundary table

Use this table when the mathematical result contributes to a separately governed question. Name that question and the first receiving action; cite the existing result when it already supplies the needed basis.

`CandidateMathObject` names the mathematical object used in the representation. State its correspondence and preserved and lost structure in the accompanying account.

For a relation claim with clear participants and meaning, apply the current direct relation pattern's rule and use its result. If the rule needs an unavailable case fact, identify that fact and leave the claim unresolved pending it. Use `A.6.P` when the relation or participant meaning remains unclear; use `A.6.RCD` only after recovery when no current direct predicate can state the needed claim. Explicitly identify an obtaining relation occurrence under its direct identity rule only when a receiving claim or operation must distinguish that occurrence.

Use `A.6.0`'s FormalSubstrate profile when a separate declaration of vocabulary, laws, imports and applicability is needed. Apply `A.6.1` for mechanism import or realization of that declaration, and `E.18.1` when accepted problem-side material needs the declaration carried into later work. The same mathematical object may be designated in several epistemes or uses; select the subject pattern for the actual object and claim.

| Object or claim being made | Governing FPF pattern | C.29 contribution |
|---|---|---|
| mathematical-lens use | `C.29` | Names the C.29 discipline: candidate mathematical object, lens mapping mode, preserved structure and lost structure, invariant or distinction, `LensUseBoundaryValue`, declared lens use, any justified blocked overread, and stop or return condition. |
| durable reusable names beyond pattern-local fields | `F.18` | Cite when `MathLensUse` names become durable beyond C.29-local use. |
| broad wording and epistemic precision restoration | `F.19`, `E.10`, `C.2.P` | Use F.19 for ordinary precise-plain-language repair, E.10 for cues and unresolved wording, and C.2.P for unresolved epistemic meaning. |
| relation precision, arity, polarity, needed-claim derivation, and slot structure | The direct relation pattern; `A.6.P` for unresolved relation or participant meaning; `A.6.RCD` for a needed claim with no suitable current predicate; `A.6.5` for reusable typed participant declarations | C.29 applies only if a mathematical object represents the settled claim or derivation and changes the stated lens use. |
| object, description, and carrier distinction | `A.7` | Do not identify the phenomenon directly with the mathematical object. |
| dynamics state space and transition law; temporal aspect | `A.3.3`; `C.27.TA` for the temporal aspect | Supply the imported or contested representation and its losses to the stated dynamics/temporal question. |
| `CharacteristicSpace`, slots, topology, order, and metric-space distance overlays | `A.19` | C.29 applies only when an overlay becomes a domain-transferring or publication-bearing lens. |
| local choice among available options | `C.11` | Supply the bounded mathematical result or rival-lens note to the option comparison; use `C.11` for the `ChoiceResult` or local choice record. |
| selected method, method-family selection, `U.WorkPlan`, performed `U.Work`, work-result record, or work-relevant appearance-based reliance repair | `A.15`, `A.15.1`, `A.15.2`, `A.15.4` | Can contribute method-relevant lens use; method, plan, performed Work, and any result record stay with their direct patterns, while A.15.4 only repairs reliance on a misleading appearance. |
| evidence relation, source currentness, provenance, evidence carrier, or model card or datasheet used as evidence | `A.10` | States `LensUseBoundaryValue` only; evidence relations and provenance remain A.10 matters. |
| assurance, readiness, reliability, release confidence, safety, trust, or engineering justification | `A.15.5` for work-entry readiness; `A.10` for evidence reliance; `B.3` only for an actual named assurance claim; the direct domain pattern for other readiness, reliability, release, safety, trust, or engineering-justification claims, plus relevant G patterns when their claims are made | Treats declared lens use as possible input only; mathematical elegance does not raise assurance. |
| measurement construction, scale, unit, or comparability, or evidence-stub adequacy | `C.16` | States measurement-dependent `LensUseBoundaryValue` only; measurement construction, scale, unit, or polarity, direct comparability, and evidence-stub adequacy stay with `C.16`. |
| explanation-facing rendering or generated explanation use | `E.17.EFP` | States mathematical-lens use for the mathematical explanation used inside the rendering; explanation-use discipline stays with `E.17.EFP`. |
| bounded comparative review unit | `E.17.ID.CR` | States declared lens use for a mathematical comparison construction or rival lens when that construction affects the comparative review use. |
| same-EntityOfConcern representation-scheme transition | `A.6.3.RT` | C.29 applies only if the representation shift imports a contested or use-affecting mathematical lens. |
| coarsened rendering with narrower declared lens use and source-bearing reopen | `A.6.3.CSC` | C.29 applies only if the coarsening depends on mathematical abstraction, quotienting, or coarse-graining. |
| cross-context meaning, bridge kind, direction, CL, loss, and substitution | `F.9` | Reference the Bridge and its separate bounded-use claim; keep Bridge semantics in `F.9`. |
| causal-use question or verdict | `C.28` | Block causal overread or cite a `C.28` application or `CausalUseSupportResultRef`. |
| forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, temporal window, or rate-change used as sufficient for a use | `C.27` | Can state a prediction-relevant or distinction-relevant mathematical-lens use; temporal-claim adequacy stays with `C.27`. |
| scale-law and Bitter-Lesson preference claims | `C.18.1`, `C.19.1`, `C.31.ASAP` | Cite scale-window, scale-law, BLP, or architecture scale-preference evidence when scale behavior, general method scale preference, or architecture scale preference is being claimed. |
| quantum-like modeling | `C.26` | Treat `C.26` as C.29-compatible specialization, not as full-card inheritance for every QL-lite note. |
| selected-set result declaration, parity or benchmark result use, source harvesting and synthesis, Part-G shipping, or publication | `G.5`, `G.9`, `G.2`, `G.10`, `E.17`, and `E.24.PUB` | Use `G.5` for selected-set result declaration, `G.9` for parity or benchmark result use, `G.2` for source harvesting and synthesis, `G.10` for shipping Part-G outputs, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for an actual publication occurrence and availability. Supply the bounded mathematical result or rival-lens note with its declared use as input. |

#### C.29:4.5 - `MathLensUse.Card@Context` shape

The full card collects the account needed for a declared reliance under :4.4. `MathLensUseOutputRef` may reference any applicable C.29 output; its use does not require a FullCard. Local naming conditions are in :6.1a.

Read `MathLensUse.Card@Context` through three aspects:

| Aspect | Fields or refs | Boundary |
|---|---|---|
| Selected mathematical representation and lens mapping | `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `InvariantsExposed` | Names the selected mathematical object and the representation or correspondence used for the C.29 account. |
| Use boundary and validation | `LensUseBoundaryValue`, `ValidationUseOverlayRef?`, `LearnedLensOverlayRef?`, failure case, uncertainty or approximation note | States the lens-use boundary value for this lens use. |
| FPF use and boundaries | `declaredLensUse`, `StopCondition`, `blockedLensOverread?`, `BridgeRefSet?`, `CausalUseDisposition?`, `AssuranceUseDisposition?`, `ExportPolicyRef?` | States what the reader may do, when to stop or return, and which governing FPF patterns define or constrain neighboring claims. |

```text
MathLensUse.FullCard base fields:
MathLensUse.Card@Context := {
  TargetPhenomenon,
  entityOfConcernRef?,
  BoundedContext,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  InvariantsExposed,
  LensBoundedPredictionOrDistinction?,
  LensUseBoundaryValue,
  declaredLensUse,
  StopCondition,
  blockedLensOverread?
}
```

Conditional fields apply only when the corresponding neighboring claim, claim-bearing use, or publication use is being made:

```text
MathLensUse.FullCard conditional fields := {
  DynamicsRef?,
  TransitionLawRef?,
  ObservationMapRef?,
  ScaleWindow?,
  CoarseGrainingRule?,
  SourceReturnCondition?,
  PublicationUseClassification?,
  PrincipalRivalLens?,
  RivalLensSet?,
  RivalLensRelation?,
  ValidationUseOverlayRef?,
  LearnedLensOverlayRef?,
  BridgeRefSet?,
  CausalUseDisposition?,
  AssuranceUseDisposition?,
  ExportPolicyRef?
}
```

**Plain card gloss.** A useful mathematical lens says: what phenomenon is being seen, through which mathematical object, by what mapping, what survives, what is lost, what becomes visible, what lens-use boundary value and validation boundary make this use bounded, the now-bounded user-facing action, any justified blocked user inference, and where the lens stops.

#### C.29:4.5a - Conditional overlays

Apply overlays for the actual reliance selected in :4.4. A conditional calculation within a stipulated model still states and checks its mathematical assumptions; a claim that the model is adequate for the phenomenon additionally requires the validation account below. A learned representation needs the learned-lens information even when the exploration remains small.

```text
MathLensUse.ValidationUseOverlay@Context :=
⟨
  ClaimUse,
  ValidationRegime,
  EvaluationSlice,
  ApproximationOrUncertaintyNote,
  KnownFailureCaseOrCounterexample,
  SensitivityOrRobustnessNote?,
  DomainOfApplicability,
  OutputChangeCondition?
⟩
```

Use the validation overlay for the FullCard reliance in :4.4: prediction about the phenomenon, an operational or consequential decision, adoption of a model, benchmark/assurance input, Bridge-dependent model reliance, or transfer as a reusable phenomenon model. This includes a scientific claim of model adequacy. A published explanation of a conditional derivation needs its derivation and assumptions, not an empirical-adequacy claim invented for it. `LensUseBoundaryValue` alone is insufficient for the stronger reliance. Keep the neighboring notions separate: verification is proof or formal checking under stated assumptions; validation is fit for a declared use and regime; calibration aligns model parameters or readouts with observations; explanation states why the lens makes a distinction intelligible. The C.29 output does not let any one of these four labels silently stand in for the others.

```text
MathLensUse.LearnedLensOverlay@Context :=
⟨
  DataOrTrainingRegime,
  ObservationMapRef,
  GeneralizationClaim,
  DiscretizationOrResolutionPolicy?,
  ValidationRegime,
  ApproximationOrUncertaintyNote,
  StopCondition
⟩
```

Use the learned-lens overlay when the mathematical object is fitted, learned, latent, simulation-trained, data-derived, a neural operator, a surrogate solver, an embedding, or a world-model representation.

Use the following learned-lens stop variants when the declared use reaches the corresponding boundary. Include a separate guard only when it passes F.19's plausible-reader test:

| Tempting overread | Stop condition form |
|---|---|
| out-of-distribution generalization | no generalization outside the declared validation regime |
| causal mechanism | no causal mechanism claim without `C.28` and evidence relation |
| latent dimension ontology | latent coordinate or factor is not an entity kind without separate ontology and evidence |
| unobserved-variable recovery | no recovery of hidden variables beyond the declared observation map and validation slice |
| benchmark superiority | no benchmark or selector superiority outside the declared evaluation slice and relevant `G.*` record |
| assurance or release use | require the corresponding assurance, release, or reliability result under its direct subject pattern; use `A.10` for evidence reliance, `B.3` only for an actual named assurance claim, and relevant G patterns for their claims |

```text
MathLensUse.CausalAbstractionCheck@Context :=
⟨
  LensMappingMode,
  InterventionStructureStatus ∈ {preserved, approximated, notClaimed},
  CounterfactualUseStatus ∈ {preserved, approximated, notClaimed},
  C28ApplicationRef?
⟩
```

This is not a first-class causal abstraction card. It is a lightweight check: when `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation, and `declaredLensUse` would include intervention, policy, counterfactual, or causal explanation, apply `C.28` for causal-use question and verdict.

#### C.29:4.5b - Repair decision table

| Failed or missing item | Required repair |
|---|---|
| no `CandidateMathObject` | If the problem still needs a mathematical lens for the next lens-use action, first name the `ProblemStructureCue` and write a `MathLensUse.LensCandidateNote` with the cheapest candidate lens family and next lens-use action; downgrade to ordinary prose or remove the mathematical claim only when no candidate lens changes action. |
| no `LensMappingMode` | Choose a lens mapping mode or downgrade to analogy-only prompt. |
| no `PreservedStructure` | Remove the claim-bearing mathematical phrase. |
| no `LostStructure` account | Describe the omitted source distinctions. If none are lost for this use, explain why the relevant distinctions and operations are preserved. C.29.1 supplies the comparison. |
| no invariant, obstruction, distinction, or payoff | Keep the phrase as didactic recognition cue or orientation-only. |
| no `LensBoundedPredictionOrDistinction` where decision, prediction, or model selection is being claimed | Block decision or assurance use; downgrade to analogy-only if no declared lens-use consequence is named. |
| evidence is analogy-only | Block decision, publication-as-established-model, assurance, release, and causal use unless evidence relation, validation regime, causal-use relation, or assurance result is supplied by its subject pattern. |
| no `LensUseBoundaryValue` | Block decision, publication, assurance, benchmark, and release use. |
| causal, intervention, policy, or counterfactual overread | Apply `C.28` or block causal use. |
| cross-context meaning, export, or substitution overread | Apply `F.9` when the export or substitution needs semantic correspondence between local senses; otherwise use the direct subject pattern. Block unsupported export or substitution. |
| scale, universality, knee, exponent, or scale-advantage claim | Apply `C.18.1` for scale-law adequacy, `C.19.1` for general method scale preference, or `C.31.ASAP` for architecture scale preference when that claim is made; otherwise keep the lens local and bounded by stop condition. |
| assurance or release use | Apply the direct release pattern, `A.10` for evidence reliance, `B.3` only for an actual named assurance claim, or relevant G patterns for their claims; block unsupported assurance or release use. |
| `StopCondition` is generic | Name the condition for narrowing or stopping, a no-lens exit, or source-return trigger. Include a blocked overread only when it passes F.19's plausible-reader test. |

#### C.29:4.5c - Reopen a used result

C.29 output-change conditions:

| New condition | Required result |
|---|---|
| validation slice fails, degrades, or no longer matches the stated regime | Change `LensUseBoundaryValue` to the updated boundary value, update the failure case, narrow the declared lens use, or block prediction-facing use. |
| a principal rival lens changes the next lens-use action | Add `PrincipalRivalLens?` and `RivalLensRelation?`, or replace the lens for that use. |
| the intended use or reliance changes | Reapply :4.4's single rule. Keep a conditional explanation small when its conditions and use are unchanged; use FullCard plus the relevant validation/receiving result for phenomenon-model or consequential reliance. |
| source-use relation becomes outdated, contradicted, or demoted to background only | Change the `SourceUseRelation`, update the lens-use boundary value, or retire the lens from claim-bearing use. |
| bridge, causal, measurement, scale, temporal, evidence, assurance, selector, or benchmark claim is being made | Name the governing neighboring pattern and keep C.29 to the declared lens-use part. |
| abstraction, compression, coarse-graining, or latent representation drops a distinction now needed for the declared use | Add `SourceReturnCondition?`, narrow the use, or block the compressed-lens claim. |

Smallest source-return and output-change conditions:

| Condition | Required result |
|---|---|
| source material or a source family changes the lens family, validation boundary, limitation, or stated use used by this C.29 output | Update `SourceUseRelation`, `LensUseBoundaryValue`, and `OutputChangeCondition?`; narrow, replace, or retire claim-bearing use when the new source-use row no longer fits the declared use. |
| a later source supersedes or contradicts the source-use decision that bounded the lens use | Mark the source-use decision as superseded or contradicted for that use, then select a new source-use relation, lower the output class, or block claim-bearing use. |
| a neighboring subject pattern changes the declared lens-use boundary for measurement, evidence, causal use, assurance, Bridge semantics, scale law, selector, benchmark, decision, or work | Keep C.29 only for the declared lens-use part and apply the changed subject pattern to the neighboring claim before the C.29 output is reused. |
| the same lens family starts carrying validation, causal-use, evidence, assurance, selector, benchmark, release, or work claim | Add the subject-pattern application, or narrow the C.29 result to lens-bounded prediction, distinction, obstruction, diagnostic boundary, or stop condition only. |
| preserved structure or lost structure can no longer be replayed from the source-domain variables, observations, cases, mechanism, or episteme | Add `SourceReturnCondition?`, restate `PreservedStructure` and `LostStructure`, lower the output class, or block the compressed-lens claim. |


AI-assisted thin-echo result rule:

| Thin echo or query shape | Required result |
|---|---|
| `field-like`, `quantum-like`, `category-like`, `manifold`, `entropy`, `RG`, `graph`, `embedding`, or another mathematical prestige head appears alone | Do not answer from the family label. First name the use under repair or state that no C.29 use is being made. |
| claim being made is causal, measurement, bridge, evidence, temporal, work, assurance, selector, or benchmark-facing | Name the governing FPF pattern before any C.29 output. |
| C.29 still applies after the subject-pattern check | Return at least `CandidateMathObject`, `PreservedStructure`, `LostStructure`, `NextLensUseAction`, and `StopCondition`, or downgrade to `LensCandidateNote` or `NoMathLensUseNeededNote`. |

C.29 edge-case boundary results:

| Edge case | Required result |
|---|---|
| mechanized proof of a model property | State assumptions and proven property; empirical evidence or assurance use stays with `A.10`, `B.3`, or relevant G patterns. |
| simulation-calibrated lens | Scenario exploration is allowed; prediction, decision, or counterfactual reliance needs validation and the neighboring-pattern result named by value. |
| latent-space visualization | Use learned-lens overlay and stop latent ontology, causal mechanism, or unobserved-variable recovery unless separately governed by the neighboring pattern governing that claim. |
| isomorphism or equivalence claim named by value | Justify the relation named by value or downgrade `LensMappingMode`. |
| multi-lens composition | Name the principal lens and neighboring notes; avoid one giant full card that mixes queue, graph, causal, temporal, and assurance authority. |
| lens becomes accepted domain theory | Keep local domain theory with the domain pattern; durable FPF naming or kind change needs `F.18`, `C.3`, `F.8`, and `E.9`. |
| mathematical notation shift only | Use `A.6.3.RT` unless mathematical-lens use changes the declared use. |
| coarsened explanation | Use `A.6.3.CSC` for source-bearing return, narrowed use, and coarsened rendering; cite C.29 only for abstraction adequacy. |


#### C.29:4.5d - When a source changes the used result

`C.29` separates source-use relations from source-use disposition. `Adopt`, `Adapt`, `Reject`, and candidate-stress-test disposition say what FPF does with the source; `SourceUseRelation` says what work the source may perform inside a C.29 application.

Local `SourceUseRelation` slot discipline:

- source material reference or locator;
- declared C.29 output, lens-use boundary, or `LensUseBoundaryValue` affected by that source;
- source-use disposition for the substantive use: adopt, adapt, reject, candidate stress test or recognition cue;
- currentness, supersession, contradiction, narrowing, or demotion condition;
- output-change condition for the C.29 result;
- stop or return condition, and any blocked overread that passes F.19's plausible-reader test.

| `SourceUseRelation` | Declared `C.29` use | Use boundary or return |
|---|---|---|
| `recognitionCue` | Help the reader notice an invariant, obstruction, symmetry, duality, state variable, scale cue, or comparison cue. | For evidence, truth, ontology, a causal-use verdict, assurance, or release confidence, establish that separate claim and its basis through its subject pattern. |
| `candidateLensPrompt` | Suggest a first candidate lens family or mathematical object to test against the problem cue being repaired. | Test a candidate cheaply when it could change the next lens-use action; require use of that lens only after its contribution is established. |
| `adequacyControlSource` | Discipline preserved structure, lost structure, stop condition, validation regime, or neighboring-pattern application. | Satisfy C.29's field requirements and the applicable subject pattern for the resulting claim. |
| `validationBoundarySource` | Constrain the declared validation regime, evaluation slice, uncertainty, failure case, or domain of applicability. | An evidence relation, assurance claim, benchmark result, or release confidence requires its own basis and subject-pattern result. |
| `acceptedDomainTheory` | Permit local use inside a domain where the theory is already the governing local formalism. | For cross-context ontology import or broader transfer, establish the needed evidence relation and a stop condition; apply `F.9` when semantic correspondence between local senses is needed. |
| `proofUnderAssumptions` | Justify a formal property under stated assumptions. | A formal proof can support a real-world-adequacy claim only when its assumptions, observations, and evidence relation are also established, together with any needed semantic Bridge. |
| `negativeExample` | Expose failure, obstruction, non-transfer, counterexample, or stop condition. | Scope the result to the demonstrated failure and its return condition. |
| `rivalLensSource` | Name a principal rival lens or relation that changes the bounded lens-use action being made. | Keep the principal-rival choice bounded to the current lens-use action. Undertake a literature review, or establish a selector or benchmark result, only for that separately current question. |


#### C.29:4.6 - Field meanings

| Field | Meaning selected for `C.29` | Boundary guard |
|---|---|---|
| `TargetPhenomenon` | Plain entry prompt naming the phenomenon or situation to be understood. | |
| `entityOfConcernRef?` | EntityOfConcern reference named by value when the lens appears inside a claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. | Required only when the lens appears in a claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. |
| `BoundedContext` | Context in which the lens is claimed to work. | Cite `F.9` when the use needs semantic correspondence between local senses. |
| `CandidateMathObject` | Concrete mathematical object, structure, formal position, learned representation, or local formalism. | Broad family labels are prompts until narrowed. |
| `LensMappingMode` | `C.29`-local lens mapping mode. | Cross-context transfer uses `F.9` when bridge semantics are being claimed. |
| `PreservedStructure` | Structure preserved by the lens in the declared use. | No preserved structure means the mathematical phrase cannot justify the stated use. |
| `LostStructure` | Source structure the representation omits or does not preserve. | When none is lost for the stated use, name the preserved distinctions and operations and the reason preservation holds. A receiving domain may still contain additional objects; use C.29.1 to establish what can be returned. |
| `InvariantsExposed` | Invariant, obstruction, fixed point, symmetry, conservation law, diagnostic boundary, or other payoff. | If no payoff is visible, downgrade to recognition cue. |
| `ObservableOrControllableCue?` | Cheap cue naming what can be observed, read out, assigned, varied, or validated before a candidate lens can change action. Examples include arrivals, work in progress, service time, wait time, edge meaning, intervention assignment, outcome readout, observation map, validation slice, scale variable, or scale point. | When making a measurement, evidence, causal or dynamics claim, apply its corresponding pattern in :4.4.6. |
| `ObservationOrReadoutNeeded?` | Optional one-line note naming the observable, readout, assignment, outcome, validation slice, or scale point still needed before the stated bounded lens-use action is justified. | If the account of this missing item makes a measurement, evidence, causal, dynamics, or validation claim, apply the neighboring pattern that governs that claim. |
| `LensBoundedPredictionOrDistinction?` | The derived consequence used for a conditional comparison, prediction, choice or model claim. | State whether the consequence holds inside stipulated premises or is relied on for the phenomenon; apply :4.4 and :4.5a accordingly. |
| `DynamicsRef?`, `TransitionLawRef?` | References to dynamics defined by `A.3.3` when dynamics semantics are being claimed. | `C.29` does not define dynamics. |
| `ObservationMapRef?` | Probe, readout, or observation map when observation makes the declared lens use bounded enough for the stated claim. | Required when learned or measurement-dependent lens use is being made. |
| `ScaleWindow?`, `CoarseGrainingRule?` | Scale range and coarse-graining or compression rule when scale behavior, macro description or effective description, universality, coarse behavior, latent compression, or renormalized description is being claimed. | `C.18.1` and `C.19.1` govern scale-law and BLP evidence; the C.29 output states only how the lens remains adequate inside the declared window. |
| `SourceReturnCondition?` | Condition under which the reader must return from the compressed or coarse description to the source-domain variables, observations, cases, or mechanisms. | Required only when abstraction, coarse-graining, compression, latent representation, or macro-modeling drops source-domain distinctions that could matter to the stated use. |
| `PublicationUseClassification?` | Optional note for publication-facing use: `orientationOnly`, `explanationFacing`, `comparisonInput`, `decisionInputCandidate`, `benchmarkInput`, `assuranceInputCandidate`, or `reusableModelPublication`. | Apply :4.4 and :4.4.6 for the stated use. |
| `OutputChangeCondition?` | Condition under which this C.29 output must be narrowed, demoted, replaced, retired from claim-bearing use, or handed to a neighboring FPF pattern. |  |
| OrdinaryRivalOrFallback | Ordinary prose, accepted local theory, direct measurement, or simpler neighboring-pattern application the reader would use without this lens. | Required for cheap outputs; prevents prestige bias before broad rival review. |
| `PrincipalRivalLens?` | Default ordinary or most relevant rival lens. | Preferred over a broad literature survey. |
| `RivalLensSet?` | Broader comparison set when a selection or superiority question requires more than the principal rival. | Publication alone does not create a selector or benchmark question; use its receiving pattern when that result is needed. |
| `RivalLensRelation?` | Declared relation between the lens in this use and the principal rival or rival set being compared. Allowed local relation values include `ordinaryFallback`, `complementary`, `sameUseLowerCost`, `morePreservedStructureHigherCost`, `lowerErrorOnDeclaredEvaluationCriterion`, `clearerExplanationForDeclaredReader`, `bridgeNeedsF9`, `causalUseNeedsC28`, `differentScaleWindow`, `differentLossProfile`, `incomparableForCurrentUse`, `blockedByStopCondition`, and `unresolved`. Examples: a queueing lens and a causal lens can be complementary for different lens-use actions; a latent manifold and a causal graph can conflict when latent axes are read causally; an RG-like lens and a micro-dynamics lens can have different scale windows. | Any superiority claim names the evaluation criterion, reader, cost, scale window, or subject pattern that makes the comparison bounded for use. |
| `LensUseBoundaryValue` | Local finite lens-use boundary field. |  |
| `BridgeRefSet?` | Reference to `F.9` Bridge material when semantic correspondence between local senses is needed. | Bridge semantics stay with `F.9`. |
| `CausalUseDisposition?` | One of `noCausalUseClaim`, `causalUseBlocked`, `C28ApplicationRef`, or `CausalUseSupportResultRef`. | No causal-reference shortcut; no causal verdict from `C.29`. |
| `AssuranceUseDisposition?` | One of `noAssuranceUseClaim`, `assuranceUseBlocked`, `evidenceInputOnly`, `A10Ref`, or `B3ApplicationRef`. | No assurance verdict from mathematical elegance. |
| `declaredLensUse` | Declared lens use in this C.29 application. | Matches evidence and validation regime. |
| `blockedLensOverread?` | Optional tempting neighboring use that is blocked or governed by another subject pattern; include it only when it passes F.19's plausible-reader test. | Names the neighboring pattern when that neighboring claim is being made. `groundedLensOverread?` is an alias for this same optional value. |
| `StopCondition` | Condition for narrowing, stopping, returning to source material, or applying the direct pattern for a neighboring claim. | States the concrete boundary of the declared lens use. |
| `ExportPolicyRef?` | Governed reuse or export policy when publication or downstream reuse is being claimed. | Not required for local orientation or mini-card use. |

