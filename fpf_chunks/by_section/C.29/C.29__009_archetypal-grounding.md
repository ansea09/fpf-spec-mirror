---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__009_archetypal-grounding.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:7 — Archetypal Grounding"
line_start: 53766
line_end: 53792
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
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
  - "C.29"
  - "C.31.ASAP"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
  - "LensUseAdmissibilityValue"
  - "coarse-graining"
  - "invariants"
  - "learned lens"
  - "lens mapping mode"
  - "lost structure"
  - "mathematical lens"
  - "ontology smuggling"
  - "preserved structure"
  - "rival lens"
  - "scale window"
  - "stop condition"
  - "structure-preserving representation"
  - "validation boundary"
---

### C.29:7 - Archetypal Grounding

| Archetype | Candidate lens | Preservation | Loss | Output and stop condition |
|---|---|---|---|---|
| Production line as queueing network | Queueing network | flow, service rates, bottlenecks, waiting time | human motivation, contractual duties, rare events not modeled | `MathLensUse.MiniCard`; admits throughput and latency reasoning, not full organizational ontology. |
| Team backlog as queue | Queueing lens | work arrival, work in progress, service time, waiting time | obligation, motivation, priority legitimacy, skill learning | `MathLensUse.OneLine` or mini-card; admits bottleneck reasoning, not moral or managerial authority. |
| Manager sees slow throughput but has no lens | Queue or flow candidate note | possible arrivals, work in progress, service bottleneck, waiting time | motivation, duty, priority legitimacy, full team ontology | Start with `MathLensUse.LensCandidateNote`; use `MathLensUse.OneLine` or mini-card only after the candidate queue or flow lens changes the next lens-use inspection. |
| Measurement comparison as declared distance or scoring choice | Metric-space distance, embedding, or scoring-function lens | comparability, distance, proximity, clustering, threshold structure | evidence relation, causal mechanism, value judgment | `MathLensUse.OneLine` or mini-card; admits comparison design and sensitivity checks, not truth or priority by itself. |
| Stabilizing system as state-space dynamics | State-space or transition lens | state variables, transition relation, attractor, control handle when the neighboring relation is named by value | unobserved motivation, obligation, causal mechanism beyond the model | `MathLensUse.OneLine` or mini-card; admits state inspection or transition inspection, not full dynamics ontology. |
| Research field as citation graph or category-like network | Graph or categorical structure | adjacency, composition, interface, failed transfer, citation or transformation patterns | semantic truth, evidence relation, social meaning | First inspect adjacency, composition, interface, or failed transfer; `MathLensUse.MiniCard` plus `F.9` when contexts cross; never substitute graph proximity for truth or evidence. |
| Quantum-like dashboard | Quantum-like probe and order lens | order effects, probe effects, incompatible frames when actually present | physical quantum ontology | `C.26` with C.29-compatible stop condition `QL-NQ`; not a full-card cost for QL-lite notes. |
| RG-like scale-law claim | Coarse-graining or fixed-point lens | scale variable, coarse-graining rule, invariants across scales | micro-mechanism identity and universal applicability | `C.29` plus `C.18.1` or `C.19.1`; stops outside scale window. |
| Learned operator as scientific lens | Learned operator, latent space, surrogate solver | trained input-output structure, resolution behavior when validated | causal mechanism, out-of-domain generalization, unobserved variables | Learned-lens overlay; validation regime and stop condition required. |

Worked micro-cases by failure mode:

| Failure mode | Reader sees | C.29 repair |
|---|---|---|
| No-lens repair | "Throughput is slow, but we have no model." | Start with a queue or flow `MathLensUse.LensCandidateNote`; observe arrivals, work in progress, service time, wait time, and bottleneck candidate before using `MathLensUse.OneLine` or mini-card. |
| Under-specified-lens repair | "The market is a field." | Write `MathLensUse.OneLine` only if the candidate mathematical object, mapping, preserved structure, lost structure, payoff, and stop condition can be stated; otherwise remove the phrase or keep it as ordinary metaphor. |
| Overread repair | "The latent manifold explains reality." | Use the learned-lens overlay, name observation map and validation slice, and stop causal or ontology overread unless a governing pattern governs it. |
| Wrong-neighbor repair | "The same graph appears in two contexts, so the meanings are the same." | Apply `F.9` for Bridge semantics; keep `C.29` only for mathematical-lens use. |
| Local-math non-use | Accepted Markov kernel inside local dynamics. | Stay in `A.3.3`; return `NoMathLensUseNeededNote` if useful; do not use C.29 merely because local mathematics appears. |
| Speculative SoTA stress | Vanchurin-style universe-as-learning. | Treat as candidate-lens stress, not accepted physics, foundation, assurance, or release input. |

Vanchurin-style universe-as-learning is not an ordinary first grounding archetype. Keep it in the validation harness and SoTA use as a candidate stress test: it can teach overclaim control and adapt-not-adopt discipline, but it does not ground accepted physics, assurance, quantitative law, or routine lens use.

