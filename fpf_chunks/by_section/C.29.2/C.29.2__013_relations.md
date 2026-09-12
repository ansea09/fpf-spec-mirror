---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__013_relations.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:12 — Relations"
line_start: 60519
line_end: 60531
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

### C.29.2:12 - Relations

- **Member of C.29:** supplies the computational formulation used when the mathematical account does not yet provide a way to obtain its consequence. Direct entry is available.
- **Uses C.29.1 when needed:** establishes the result-preservation or bounded-transfer claim for a representation reduction or changed operation.
- **Exchanges results with C.29.3:** supplies represented inputs, operations, output interpretation and computational conditions; receives execution limits or available capabilities that can revise them.
- **Uses B.5:** recovers an available construction and its argument from an explanation, and revises dependent reasoning when premises change.
- **Uses A.3.3:** constructs sufficient state and permitted continuations, including control and retained history when required.
- **Uses A.6.3.RT:** constructs expressions under available notation rules and checks the content of a representation change. Notation- or language-design methods supply missing rules.
- **Uses C.39 and C.40 by their entry conditions:** obtains a missing way, or develops branching search when a workable change-and-test operation is available.
- **Uses subject Methods:** algorithm design, numerical analysis, symbolic computation and other computational disciplines supply their specific constructions, proofs and cost models. C.16 and physical-modeling methods supply measurement and empirical conditions when the requested result depends on them.
- **Coordinates with A.3.1, A.6.1, B.1.5 and B.1.6:** Method identity, an explicitly needed operation declaration, composition of identified Methods and resource accounting for performed Work remain under those patterns. A description of a procedure is not a claim that its execution occurred.
- **Uses C.2.1, A.10 and B.3 for the corresponding claims:** C.2.1 governs episteme identity, A.10 governs evidence use, and B.3 governs assurance of the particular result and reliance being asserted.

