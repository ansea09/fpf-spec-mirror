---
chunk_kind: "child"
pattern_id: "B.5.QD"
pattern_title: "Develop a New Question from a Result or Construction"
section_id: "B.5.QD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD/B.5.QD__012_sota-echoing.md"
commit_sha: "8581bcf6502498b53aaa9fd42ed925a1371c08d1"
heading_path:
  - "B.5.QD — Develop a New Question from a Result or Construction"
  - "B.5.QD:11 — SoTA-Echoing"
line_start: 44591
line_end: 44600
dependencies:
  - "B.5.MPC"
  - "B.5.RA"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.39"
  - "C.40"
  - "E.10.INT"
keywords:
---

### B.5.QD:11 - SoTA-Echoing

For developing a question after a failed proof or conjecture, **adapt** Lakatos's proof-analysis method in *Proofs and Refutations (I)* (1963), §3 and the beginning of §4. Distinguishing a counterexample to a lemma from one to the main conjecture preserves recoverable reasoning; asking for the missing construction improves on protecting the claim by convenient restrictions alone. Sections :4.1–:4.3 and :5.1 use that contribution. The historical dialogue supplies a method of criticism and question change; the resulting mathematical claims still need their own arguments. Reopen the choice when a different failure prevents recovery of the consequential dependency. [Original article](https://pi.math.cornell.edu/~mann/classes/chicago/Lakatos.pdf).

For obtaining questions from either an unfinished proof or available constructions, **adapt** the distinction between goal-directed lemma discovery and bottom-up theory exploration in Zhang and Tan's *Automated Conjecturing and Theorem Finding: A Survey* (2026), §§3 and 5. The two approaches support different entries in :4.2. The surveyed filters for false, redundant or uninteresting conjectures help theorem search; using those filters as a general question filter would discard a useful counterexample. Section :4.3 instead evaluates the question's contribution separately from a proposed answer's truth. Syntactic complexity and proof-related scores remain local heuristics. Reopen when a stronger generation method offers more useful questions at comparable effort for the receiving practice. [Survey](https://jcst.ict.ac.cn/cn/article/pdf/preview/10.1007/s11390-026-6040-0.pdf).

For finding further uses of a successful operation, **adopt** Blelloch's constructive treatment of all-prefix-sums in *Prefix Sums and Their Applications* (1993), §1.1. It exposes an operation and its application conditions, improving on retaining only a program's final answer. Section :5.3 uses cumulative addition to develop an interval question; its range-sum derivation is worked here. Prefix operations over other associative operators can serve other questions, but subtraction requires the additional algebraic structure used in this example. The source's parallel implementations are separate Methods. Reopen when the operations, numeric semantics or workload change. [Author's chapter](https://www.cs.cmu.edu/afs/cs/academic/class/15750-s11/www/handouts/PrefixSumBlelloch.pdf).

For questions beyond a fixed objective, **adapt** Wang et al.'s *Enhanced POET* (2020), §§2–3, through C.40's coupled development of problems and ways. Relative difficulty and transfer can make a question worth retaining even when it is poorly served by the present best method. Against requiring an already known route to a final objective, :4.5 keeps a useful nearer contribution and examines its cost. The reported computational environments demonstrate that search approach under their conditions; they do not establish a universal measure of interest or development. E.10.INT supplies the broader distinction. Reopen when retained questions cease to enable useful transfer or the contributors' capabilities change. [Paper](https://proceedings.mlr.press/v119/wang20l/wang20l.pdf).

