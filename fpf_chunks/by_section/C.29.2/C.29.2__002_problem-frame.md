---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__002_problem-frame.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:1 — Problem frame"
line_start: 60148
line_end: 60165
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

### C.29.2:1 - Problem frame

**Use this when.** You know what a mathematical answer would mean, but the available expression, data and operations do not yet explain how to obtain it. An equation may characterize a solution without giving a procedure; a proposed procedure may need information its stored state has discarded; or a short calculation may expand into an unaffordable representation.

The practical question is: **What should be represented, and how will the available computation obtain an interpretable answer?** Begin with the distinction the answer must make. For example, if an executor must accept either “increment, then double” or “double, then increment”, storing only the two operation names loses a distinction: on input 3 the required answers are 8 and 7. Ordered instructions and a current position make that distinction operable.

**The object being developed** is a computational construction for a stated question: represented quantities or state, computational rules, and a way of obtaining and interpreting the requested result. *Computational formulation* names this work. The construction may leave evaluation order to a solver or describe a stochastic or continuing process. Its account can be a short derivation, pseudocode or a program with an explanation; these are ways to communicate the construction, not additional required records.

**Intended reader.** A practitioner who can state the working question and read its subject mathematics, and who needs to recover, construct or commission the computation. Elementary arithmetic and following a sequence of instructions suffice for the first case. A numerical or quantum-modeling case additionally supplies its relevant mathematical assumptions locally; developing a production solver still needs that discipline's preparation.

Computational thinking is the wider practice. This pattern covers formulation: represented inputs and state, computational rules, a way to obtain and interpret the output, and the argument and resource account needed for its use. Algorithm design, numerical analysis, programming-language design, learning and distributed computation supply deeper construction methods. This body is not a complete repertoire for those disciplines.

**Family relation.** C.29 groups methods for constructing, transferring and realizing interpretable mathematical accounts. C.29.2 contributes a computational formulation by composition and result use; it does not inherit every step or recording option of C.29. C.29.1 supplies a needed result-transfer argument. C.29.3 connects a computation with a system that prepares, performs and exposes its result. Enter this pattern directly when the working question is already available.

**First useful result.** Return a formulation with an applicable way to obtain and interpret the requested result under stated conditions, or a demonstrated obstruction and the particular construction still needed. A justified restriction, error bound or resource rejection may finish the current question.

**Ordinary non-use.** Use an already adequate local calculation or implementation directly when its inputs, operations and result are understood. Open C.29.1 for an unsettled transfer between accounts, C.29.3 for an unsettled execution correspondence, or the relevant subject method when that is the only missing contribution.

