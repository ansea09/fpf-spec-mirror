---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:14"
section_title: "Assessing formality in practice"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__015_assessing-formality-in-practice.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:14 — Assessing formality in practice"
line_start: 53208
line_end: 53233
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.7"
  - "C.2.LS"
  - "C.39"
  - "F.9"
keywords:
  - "Formality assessment"
  - "expression properties"
  - "language-state separation"
  - "local ordinal scale"
  - "partial order"
  - "proof"
  - "specification"
---

### C.2.3:14 - Assessing formality in practice

#### C.2.3:14.1 - First-pass questions

1. Which claim, declaration or argument must be understood, executed, combined or checked?
2. Are its terms, domains and interpretation sufficient for that operation?
3. Are the required predicates, operations and inference steps actually expressed?
4. Which calculus and assumptions matter, and what checking result is available when required?
5. Would changing the expression property change the receiving result, or would it only add unused apparatus?

#### C.2.3:14.2 - Short assessment

A short assessment names the subject, required properties, observed basis and consequential gap. For example: “The interface condition gives typed inputs and outputs and an explicit postcondition. The procedure has executable semantics. The preservation of this postcondition across the retry branch is not expressed.” The next useful change is the missing retry argument, not the acquisition of a more elaborate specification language.

For repeated comparisons, use the same property meanings and conditions for every candidate. A compact profile can record them. Add a local rank only when its declared mapping preserves the distinctions used by the comparison.

#### C.2.3:14.3 - Typical improvements

- Replace unstable terms with explicit definitions and consistent references when interpretation is blocked.
- State a necessary acceptance condition as a predicate with its types, units and meaning when it must be evaluated or reasoned about.
- Supply operational semantics when the result must be computed.
- State the relations and obligations joining formal subsystems when the whole must be analysed.
- Express the missing derivation when the result depends on a conclusion from premises, then obtain the checking evidence required for that use.

These changes can occur independently or together. Describe the property changed; use a local rank difference only when the named scale gives it meaning.

