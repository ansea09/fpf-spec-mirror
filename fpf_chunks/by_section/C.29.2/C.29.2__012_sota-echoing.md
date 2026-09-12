---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__012_sota-echoing.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:11 — SoTA-Echoing"
line_start: 60892
line_end: 60923
dependencies:
  - "A.10"
  - "A.3.1"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.1.5"
  - "B.1.6"
  - "B.3"
  - "B.5"
  - "C.16"
  - "C.2.1"
  - "C.29.1"
  - "C.29.3"
  - "C.39"
  - "C.40"
keywords:
---

### C.29.2:11 - SoTA-Echoing

**Practice question.** What is the strongest usable way to turn a stated mathematical result into a computation at the effort warranted by the task? The selected line is to reuse an applicable construction when possible, make its input/output meaning and argument explicit, and compare alternatives using the accuracy and resources that can change the answer. There is no single best algorithm across the input classes in this pattern.

#### C.29.2:11.1 - Meaning and correctness before a larger claim

The current [Dafny tutorial, “Loop Invariants” and “Termination”](https://dafny.org/latest/OnlineTutorial/guide#loop-invariants), demonstrates constructing a preserved relation to the answer and proving progress separately. **Adapt** that practice in :4.4 and :5.1: a short manual argument can establish the finite interpreter's stated semantics; a few traces cannot establish its whole input class. Mechanized checking is a serious alternative when program complexity or assurance needs justify its specification and proof effort. Reopen the choice when the procedure or required assurance becomes too large for the retained argument.

#### C.29.2:11.2 - Choose numerical methods by their guarantees and costs

The [SciPy bisection documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html) states the bracketing premises and its absolute-plus-relative termination criterion. **Adopt** explicit tolerance selection in :4.5; library defaults need not match the receiver's requirement.

[The documented Brent routine](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html) is a serious alternative combining bracketing, bisection and interpolation. **Adapt** the choice in :5.2: retain bisection for its simple bound and small exact case, while considering Brent's method when function evaluations are costly. The deliberate trade-off is a simpler argument for potentially more evaluations. Reopen for a changed function class, tolerance, evaluation cost or finite precision failure.

#### C.29.2:11.3 - Cost the represented objects, not the problem label

[Qiskit Aer's simulator documentation](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html) supplies a concrete current comparator: dense state-vector storage, alternative simulation representations, and controls that discard matrix-product-state coefficients. **Adopt** representation-sensitive counting in :4.6 and **reject** treating a truncation setting as an accuracy guarantee for an arbitrary observable. The :5.3 payload arithmetic and restricted product-state construction expose the relevant gain directly. The suitable general simulator remains unselected until the state family, operations, output and error are known. Reopen the calculation when those conditions or the actual algorithm change.

#### C.29.2:11.4 - Let executing capabilities change the formulation

[Kalita, Butler, Stepney and Kendon, *Novel models of computation from novel physical substrates: a bosonic example*, v1 (2026), §§1, 3–4](https://arxiv.org/html/2603.24531v1), develop computational concepts, a language and reference implementation from a physical-model contribution. Their bosonic example includes probability distributions in the computational meaning. **Adapt** the reverse entry in :4.2 and the return in :4.7 instead of requiring every device to implement a preselected model. This is a research Method candidate with a bosonic illustration. Section 4.7.1 explicitly leaves physical implementation for later work; its simulation does not establish device execution.

[Stepney, *Co-designing the computational model and the computing substrate* (2019), §§4–5](https://eprints.whiterose.ac.uk/id/document/1547865), proposes jointly exploring model and substrate rather than fixing one permanently. **Adapt** that reciprocal return while retaining a settled model when it already answers the use. Joint design costs a larger search; undertake it when a capability or mismatch can change the useful computation. The paper's demonstrated reservoir-characterization work does not establish the proposed general co-design process. Reopen for a useful operation excluded by the chosen model or a formulation whose required operation cannot be realized.

#### C.29.2:11.5 - Keep structural reformulation and numerical solution distinct

[ModelingToolkit's model-building reference, “System simplification” and “Exploring the results of simplification”](https://docs.sciml.ai/ModelingToolkit/stable/API/model_building/), describes reformulating equations and recovering eliminated variables through stored expressions. **Adopt** that pairing in :4.2 and :5.4. Hand substitution suffices for the small circuit; a symbolic compiler becomes useful when model size or changing equations make that work substantial.

[Its initialization tutorial](https://docs.sciml.ai/ModelingToolkit/stable/tutorials/initialization/) distinguishes required conditions from guesses and shows how changing the givens can require releasing a retained constraint. **Adapt** that distinction when parameters or initial quantities become unknowns. Consistency of an initial system and numerical success in finding its solution are different questions.

[Dyad's transient-analysis documentation](https://help.juliahub.com/dyad/stable/analyses/transient.html) separates the initial-value problem from algorithm and tolerance choices. **Adopt** that separation: structural reduction supplies a computational problem and recoverable outputs; numerical analysis supplies an appropriate solution method and accuracy argument. Reopen the affected choice when equations, initial constraints, requested outputs or accuracy change.

