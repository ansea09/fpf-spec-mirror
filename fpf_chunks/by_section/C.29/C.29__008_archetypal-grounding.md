---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__008_archetypal-grounding.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:7 — Archetypal Grounding"
line_start: 59475
line_end: 59521
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

### C.29:7 - Archetypal Grounding

| Archetype | Candidate lens | Preservation | Loss | Output and stop condition |
|---|---|---|---|---|
| Production line as queueing network | Queueing network | flow, service and waiting under stated premises | station failures, rework and blocking if omitted | MiniCard for the conditional comparison in :4.4; FullCard with validation when the same result is used for actual capacity or latency reliance. Withdraw the affected result when its premises fail. |
| Team backlog as queue | Queueing lens | work arrival, work in progress, service time, waiting time | obligation, motivation, priority legitimacy, skill learning | `MathLensUse.OneLine` or mini-card; admits bottleneck reasoning; moral or managerial authority, when claimed, needs its own basis. |
| Manager sees slow throughput but has no lens | Queue or flow candidate note | possible arrivals, work in progress, service bottleneck, waiting time | motivation, duty, priority legitimacy, full team ontology | Start with `MathLensUse.LensCandidateNote`; use `MathLensUse.OneLine` or mini-card only after the candidate queue or flow lens changes the next lens-use inspection. |
| Measurement comparison as declared distance or scoring choice | Metric-space distance, embedding, or scoring-function lens | comparability, distance, proximity, clustering, threshold structure | evidence relation, causal mechanism, value judgment | `MathLensUse.OneLine` or mini-card; admits comparison design and sensitivity checks, not truth or priority by itself. |
| Stabilizing system as state-space dynamics | State-space or transition lens | state variables, transition relation, attractor, control handle when the neighboring relation is named by value | unobserved motivation, obligation, causal mechanism beyond the model | `MathLensUse.OneLine` or mini-card; admits state inspection or transition inspection, not full dynamics ontology. |
| Research field as citation graph or category-like network | Graph or categorical structure | adjacency, composition, interface, failed transfer, citation or transformation patterns | semantic truth, evidence relation, social meaning | First inspect adjacency, composition, interface, or failed transfer; `MathLensUse.MiniCard` plus `F.9` when the use needs semantic correspondence between local senses; never substitute graph proximity for truth or evidence. |
| Quantum-like dashboard | Quantum-like probe and order lens | order effects, probe effects, incompatible frames when actually present | physical quantum ontology | `C.26` with C.29-compatible stop condition `QL-NQ`; not a full-card cost for QL-lite notes. |
| RG-like scale-law claim | Coarse-graining or fixed-point lens | scale variable, coarse-graining rule, invariants across scales | micro-mechanism identity and universal applicability | `C.29` plus `C.18.1` or `C.19.1`; stops outside scale window. |
| Learned operator as scientific lens | Learned operator, latent space, surrogate solver | trained input-output structure, resolution behavior when validated | causal mechanism, out-of-domain generalization, unobserved variables | Learned-lens overlay; validation regime and stop condition required. |

Worked micro-cases by failure mode:

| Failure mode | Reader sees | C.29 repair |
|---|---|---|
| No-lens repair | "Throughput is slow, but we have no model." | Start with a queue or flow `MathLensUse.LensCandidateNote`; observe arrivals, work in progress, service time, wait time, and bottleneck candidate before using `MathLensUse.OneLine` or mini-card. |
| Under-specified-lens repair | "The market is a field." | Write `MathLensUse.OneLine` only if the candidate mathematical object, mapping, preserved structure, lost structure, payoff, and stop condition can be stated; otherwise remove the phrase or keep it as ordinary metaphor. |
| Overread repair | "The latent manifold explains reality." | Use the learned-lens overlay, name observation map and validation slice, and stop causal or ontology overread unless an exact causal or ontological predicate is defined and current facts satisfy it. |
| Wrong-neighbor repair | "The same graph appears in two contexts, so the meanings are the same." | Apply `F.9` for Bridge semantics; keep `C.29` only for mathematical-lens use. |
| Local-math non-use | Accepted Markov kernel inside local dynamics. | Stay in `A.3.3`; return `NoMathLensUseNeededNote` if useful; do not use C.29 merely because local mathematics appears. |
| Speculative SoTA stress | A proposed metric/noise coupling is carried from a learning model to a physical or biological system. | Use :13.2's candidate conditions; identify variables and assumptions and test the correspondence before using the transferred result. |

A speculative learning-dynamics model can be tried as a candidate with a concrete mathematical object and a testable correspondence. The bounded source use is in :13.2.

#### C.29:7.1 - Preserve a reservation operation

A display that retains on-hand quantity n but omits reserved quantity r merges (n,r)=(1,0) and (1,1), although only the first permits another reservation. **C.29.1:5.1** constructs the available quantity `F(n,r)=n-r`, compares reservation before and after mapping, and establishes the shared permission condition. It returns a quantity that supports the reservation question while retaining separate totals when another question needs them.

#### C.29:7.2 - A route summary changes the cost question

Routes costing 1 and 4 can have the same endpoints without having the same cost. **C.29.1:5.2** shows why the cost of a chosen route cannot be assigned to their common endpoint summary, then constructs a different answer: the minimum over admissible routes. A shared continuation preserves that minimum; a continuation available only after the more expensive prefix defeats minimizing the first stage alone. The repair retains the continuation condition or compares compatible complete routes.

#### C.29:7.3 - Make calculation rules available as data

The same executor can perform different integer calculations when their instructions are supplied as data. **C.29.2:5.1** constructs its state and instruction rules, obtains 8 and 7 from two orders applied to input 3, and gives separate arguments for the result, termination and cost. Adding jumps, interaction or larger stored integers returns to the corresponding behavior or resource question.

#### C.29:7.4 - A correct distance calculation meets a finite command range

A calculated count of 63,662 motor increments cannot be sent as a positive signed 16-bit command. **C.29.3:5.1** derives the count from a stated motion model, shows the wrapped command's contrary motion, and tests splitting the count under relative and absolute command meanings. It returns a command procedure with its supported range and motion conditions; B.5.MPC:5.1 shows the joint physical, mathematical and computational reasoning.

#### C.29:7.5 - Realize a capacity bound with a shared stock of cards

Three unique admission cards can support a three-visitor bound when their possession and transfer rules control entry. **C.29.3:5.3** follows free, reserved, inside and awaiting-return states. The free-card count gives a sufficient occupancy bound during handover; an occupancy equality additionally needs the intermediate states. A second entrance must share or partition the same stock. The worked construction shows how copying the stock defeats the bound and how controlled transfers restore it.

