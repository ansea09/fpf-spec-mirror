---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__012_sota-echoing.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:11 — SoTA-Echoing"
line_start: 24094
line_end: 24107
dependencies:
  - "A.19.CN"
  - "A.19.ULSAM"
  - "B.1"
  - "B.2"
  - "C.29"
keywords:
  - "aggregation law"
  - "bounds"
  - "cross-scale consistency"
  - "dependency model"
  - "intended result"
  - "ordered composition"
  - "singleton identity"
---

### A.9:11 - SoTA-Echoing

**Practice question.** Which law, and which property check, preserve the intended result when dependence, order or numerical interpretation matters?

The selected line separates the subject model from the permitted computation. For the reliability branch, the NIST/SEMATECH *e-Handbook*, [§8.1.8.2, series model](https://www.itl.nist.gov/div898/handbook/apr/section1/apr182.htm), and [§8.1.8.3, parallel model](https://www.itl.nist.gov/div898/handbook/apr/section1/apr183.htm), supply concrete competing laws with their independence and failure-event assumptions. **Adopt** that event-first choice in §4 steps 1–3 and §5's .72/.98 cases. With the same component data, neither a familiar product nor a minimum answers both questions. A minimum can still supply a bound where the intended event warrants it. These sources support those non-repairable or first-failure reliability models; they establish no law for every aggregate.

For computation, [MPI 5.0, §7.9.1, Reduce](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report/node132.htm), supplies the practical comparison. Its reduction contract permits regrouping under associativity and, where applicable, reordering under commutativity. It also recognizes that floating-point addition can change under those freedoms and advises enforcing an evaluation order when the application requires it. The source supplies both a serious parallel-reduction default and an explicit-order alternative, not proof that a caller's domain operation has the assumed properties.

**Adapt** this contract distinction in §4 step 4 and the `LOC` question. Given the same operands and required result, first check only the property needed for the proposed rearrangement. A tree reduction is appropriate when that property or an adequate error bound holds. An explicit ordered fold is the stronger answer when a particular evaluation order is part of the required result. It preserves that result at the possible cost of parallelism; it does not become the most accurate summation algorithm merely by fixing order. **Reject** treating acceptance by a reduction interface as evidence that rearrangement is harmless.

For a constructed binary64 calculation with round-to-nearest, ties-to-even, `(10^16 + (-10^16)) + 1` yields `1`, while `10^16 + ((-10^16) + 1)` yields `0`. The inputs, two additions and operand order are the same; grouping alone changes the answer. If the receiver requires the left-associated result, the second calculation fails that requirement. If a justified receiving tolerance permits both, this example alone does not forbid regrouping. Both candidates can be compared from the same operands and result requirement before choosing an implementation.

Reopen the selected law when the intended event or dependence model changes. Reopen only the affected computation claim when the numeric representation, allowed error, grouping or order changes. A stronger reduction method matters when it preserves the required result with a preferable cost; its speed alone does not establish the domain law.

