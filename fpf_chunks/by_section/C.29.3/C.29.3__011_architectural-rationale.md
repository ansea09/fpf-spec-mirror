---
chunk_kind: "child"
pattern_id: "C.29.3"
pattern_title: "Computational Realization"
section_id: "C.29.3:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.3/C.29.3__011_architectural-rationale.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.3 — Computational Realization"
  - "C.29.3:10 — Architectural Rationale"
line_start: 60812
line_end: 60845
dependencies:
  - "A.3.3"
  - "A.6.1"
  - "B.5.MPC"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.29.3:10 - Architectural Rationale

#### C.29.3:10.1 - Why realization needs its own method

Mathematical result transfer compares accounts and their operations. Computational formulation constructs a procedure for the requested result. Realization begins with that procedure and asks how an executing arrangement supplies it. Its new work is preparation, physical or operational execution, readout and comparison under the conditions of use.

A.6.1 provides the declaration and realization relation. It leaves the design and interpretation of a particular executing arrangement to the method that uses the relation. C.29.3 supplies that constructive work within the mathematical-use family. The method can be entered directly with an available computation.

Checking a program alone is useful when its execution environment is already established. It is insufficient for the unresolved interface, readout and shared-stock cases here. The present comparison follows only connections on which the receiving result depends.

#### C.29.3:10.2 - Preparation, execution and interpretation

[Horsman and colleagues (2014)](https://arxiv.org/abs/1309.7979) distinguish abstract computation from its use through physical preparation, evolution and representation. Adopt their comparison as the basis for :4. The practical extension here is to return the equality, bound or behavior needed by the work, and to repair the particular connection that defeats it.

That account is one theory of physical computation. The method uses its constructive comparison without settling every philosophical classification of computing systems. For the declared use, establish whether the interpreted execution supplies the required result under the stated conditions, using :4.5.

The examples explain why both directions matter. Input preparation asks what state can be made; output interpretation asks what result can be obtained from the state or indication. They can have different scales, ranges and physical means.

#### C.29.3:10.3 - Realization and the surrounding physical activity

A computation can contribute to physical control while the controlled system continues to evolve. [Horsman, Stepney, Clarke and Kendon (2026), §§3.3–3.4 and 5.3](https://arxiv.org/html/2604.16162v1) distinguish the compute cycle within control from the broader physical control cycle. Adopt that distinction in :4.1 and the requirement to include consequential timing in :4.3.

The robot calculation supplies a command; the command's execution and its relation to travel supply further claims. In the card arrangement, the abstract admission rule is carried through reservation, crossing and return. The physical conditions that maintain those relations must remain understandable.

#### C.29.3:10.4 - Changing model and means together

A fixed computation can be a useful constraint on the device design. A fixed device can instead suggest more suitable computational operations. [Stepney (2019), §§4–5](https://eprints.whiterose.ac.uk/id/eprint/147381/) proposes combining these directions in model-and-substrate co-design.

[Kalita and colleagues (2026), §§1 and 3–4](https://arxiv.org/html/2603.24531v1) develop the reverse direction through a bosonic-device example: capabilities of the physical system inform a computational model and language. Adapt this source contribution as the formulation return in :4.6. Developing such a language requires its own constructive repertoire; a return from realization identifies that work rather than completing it.

The analog example shows a small instance of the same design freedom. Keeping the averaging circuit and changing its encoding or decoding can supply a useful addition operation. The physical relation constrains which interpretation works.

Thermodynamic sampling and optical ML hardware extend this design choice to computations based on distributions or iterative physical evolution. [Melanson et al. (2025)](https://www.nature.com/articles/s41467-025-59011-x) demonstrate sampling and matrix inversion on a small stochastic circuit. [Kalinin et al. (2025)](https://www.nature.com/articles/s41586-025-09430-z) co-design an optical/electronic fixed-point computation with its learning model. Their different result and execution forms motivate the choices in :4.1–4.5. The detailed sampler, model-training and device-construction Methods supply the corresponding specialist work.

