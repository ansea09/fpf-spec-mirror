---
chunk_kind: "child"
pattern_id: "B.5.MPC"
pattern_title: "Connect Physical, Mathematical and Computational Reasoning"
section_id: "B.5.MPC:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC/B.5.MPC__011_architectural-rationale.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "B.5.MPC — Connect Physical, Mathematical and Computational Reasoning"
  - "B.5.MPC:10 — Architectural Rationale"
line_start: 41725
line_end: 41770
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.3"
  - "B.3.3"
  - "B.5"
  - "B.5.4"
  - "C.11.DUA"
  - "C.16"
  - "C.29"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "C.39"
  - "C.40"
  - "U.Dynamics"
keywords:
---

### B.5.MPC:10 - Architectural Rationale

#### B.5.MPC:10.1 - Why the connection is a Method in its own right

The receiving physical question joins several operations whose local success has different meanings. Derivation establishes what follows within a mathematical account. A physical explanation supports the choice of that account for a phenomenon. A procedure obtains a represented result; its realization connects that procedure to available system behavior. Coordinating these operations requires preserving their result dependencies while selecting a useful next contribution.

The robot makes the need concrete. Circumference, transmission ratio, integer rounding and signed-command semantics are separately intelligible. The useful command exists only when they refer to compatible motion and counts. A.3.3 can help recover state, C.29 can construct and transfer the mathematical consequence, and C.16 can interpret an observation. Their contributions enter the joint question through the dependencies explained in :4; none by itself chooses all the other subject content.

B.5 provides the general inquiry method: recover the question, perform the missing contribution, make its result understandable, and settle or revise the inquiry. This specialization adds the recurring connections among physical account, mathematical interpretation, computational formulation and executing arrangement. The relation is specialization of inquiry coordination and composition with the constituent Methods. A mathematical Method does not become the parent of a physical modeling Method merely because its result is used there.

An alternative is to use a fixed forward sequence. That is convenient when every input is new and later stages expose no earlier gap. It becomes wasteful when a ready theorem supplies the answer, and inadequate when command semantics require an earlier state distinction. The dependency method retains a forward traversal but also supports backward recovery, direct entry and returns after changed conditions.

Another alternative is to let each specialist check only their own output. That can be sufficient when all receiving correspondences are already established. Where they are unresolved, a correct local output can remain unusable by the next contributor. Give the connection itself an explicit receiving question and a capable contributor.

#### B.5.MPC:10.2 - What the sources contribute to the synthesis

Rodin's *Axiomatic Architecture of Scientific Theories* develops a constructive account of axiomatization in which object-forming activity matters alongside propositions. That supports asking how the needed object is obtained and which operations its theory permits. In :4.3–4.4, this becomes recovery of an actual construction. Physical interpretation still requires its subject account; the mathematical construction does not establish that a proposed physical interaction occurs. See [Rodin, 2020, §§4.2.2–4.2.3](https://philsci-archive.pitt.edu/17600/1/bde.pdf).

Fong and Spivak make preservation under composition explicit: a functor preserves identities and composition between categories. The use here is the comparison of corresponding operations, supplied by C.29.1. It explains why relabelling objects alone cannot establish a transfer. A physical approximation may instead need a bound or another qualified relation; the coordinating Method does not require every connection to be a functor. See [*Seven Sketches in Compositionality*, §3.3.2](https://arxiv.org/pdf/1803.05316).

Horsman, Stepney, Wagner and Kendon distinguish the representation of a physical system from the preparation and interpretation needed to use a physical process for computation. Their account supports :4.5's two routes and the distinction between refining an abstract description and realizing it. It also permits input preparation and result reading to differ. The present Method adapts that comparison to a receiving physical question and to useful bounds, rather than adopting their account as a universal definition of all computation. See [*When Does a Physical System Compute?*, 2014, §§VI–VIII](https://arxiv.org/abs/1309.7979).

Turing's 1936 construction of a universal computing machine provides a historical demonstration that an executor can interpret an encoded description of another machine's procedure. That helps distinguish the rule description, its interpreter and the realized operation. The finite interpreter in C.29.2:5.1 provides a small entry to that distinction. Use C.29.2 for the computation-specific cost account when a resource limit matters; :4.4 carries that cost and the computation's meaning into the joint use. See [Turing, *On Computable Numbers*, §6](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf).

These contributions answer different construction questions. The synthesis is to hold their input and result meanings together for a physical use, inspect their joint and alternative dependencies, and let a failed connection determine the next contribution. It preserves mathematical, empirical and realization grounds at the points where they are needed.

#### B.5.MPC:10.3 - Why notation and understanding remain part of the work

An expression can help a practitioner perform a construction. Macbeth's account of paper-and-pencil reasoning explains how a diagram or inscription can participate in the reasoning, including by allowing the same content to be analysed in more than one way. Dutilh Novaes examines formal languages as cognitive tools whose use depends on learned abilities to read and manipulate signs. These accounts support the operative expression step in :4.3. They do not establish that a notation improves every task or that a human learning effect transfers unchanged to AI. See [Macbeth, 2011](https://doi.org/10.1093/philmat/nkr006) and [Dutilh Novaes, 2012, §§3.2, 5.2 and 6.1](https://doi.org/10.1017/CBO9781139108010).

For this Method, the practical consequence is precise. Naming the same count N in several expressions is useful only while its participant and operation remain recoverable. A gear graph helps reason about closed contact paths because its edge meaning and traversal rules are available. The four card states distinguish occupancy from reservation throughout entry and exit, where an undifferentiated “not free” count gives only a bound. These are changes to what the expression helps someone do, not merely choices of appearance.

A second alternative is to make one formal language carry the whole inquiry. This can help when a mature language expresses the required physical, mathematical and execution distinctions and its users can work with it. If it cannot express a necessary distinction, use another representation or develop the language. Retaining interpretable correspondences allows several forms to contribute without assuming that one form already covers the whole problem.

Levenchuk's [2012 robotics account](https://ailev.livejournal.com/1034484.html) describes difficulty combining familiar speed calculations, several distance quantities, program expressions and physical timing. It motivates changing the question while retaining the interpreted relations in :4.3, and examining the timing of observation and execution in :4.5. The account is a historical report of a particular learning situation. The resulting Method here is a conceptual synthesis.

AI can reduce the cost of obtaining a calculation, candidate proof or explanation while leaving the choice and interpretation of the receiving question open. Klowden and Tao discuss the difference between a formally checked statement, its intended meaning and the understanding that enables further use. Section :4.8 turns that distinction into a contribution question: who can recover the decisive connection and adapt it when the premise changes? This is a capability to arrange, not an assertion that every participant must reproduce every proof. See [*Mathematical Methods and Human Thought in the Age of AI*, 2026, §4](https://arxiv.org/html/2603.26524v1).

#### B.5.MPC:10.4 - Why a sufficient answer can also open a better question

Deutsch's discussion of foundational theories treats their connections as sources of criticism across areas, rather than relying on a theory's foundational status to settle another question. This motivates examining how a claim about computation constrains a physical proposal and how physical knowledge constrains an executing arrangement. The specific correspondences still require their arguments. See [Deutsch's interview on *The Beginning of Infinity*](https://beginningofinfinity.org/interview/).

The same connection work can generate a worthwhile next problem. The robot account raises which observations distinguish rolling from slip. The gear witness raises which physically available contact change removes the obstruction. The card bound raises whether redistribution can reduce waiting while preserving the shared stock. Each continuation identifies an additional possible action and a construction or uncertainty that matters to it.

A sufficient answer remains a legitimate stopping point when the current use is complete. When inquiry development is selected, retain the useful connection and work a consequential change to the question or apparatus. A general invitation to keep exploring supplies less direction than the particular obstruction or newly available operation.

