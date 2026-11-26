---
chunk_kind: "child"
pattern_id: "E.5.2.L"
pattern_title: "Languages, Expressions and Interpretation"
section_id: "E.5.2.L:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2.L/E.5.2.L__012_sota-echoing.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "E.5.2.L — Languages, Expressions and Interpretation"
  - "E.5.2.L:11 — SoTA-Echoing"
line_start: 102887
line_end: 102890
dependencies:
  - "A.6.3.RT"
  - "C.2.1"
  - "E.5.2"
  - "F.18"
keywords:
---

### E.5.2.L:11 - SoTA-Echoing

For a spelling check, comparing the written signs can settle the question. RDF permits distinct concrete syntaxes to express the same abstract graph. In SMT-LIB, the signature and the sorting rules determine whether a term of the indicated sort can be formed. A structure interprets the symbols of that signature. For those uses, comparing spellings alone can miss equivalent readings or accept a construction whose declared sorts do not fit. Section 4 therefore asks which constructions are admitted and, for an interpreted language, which readings its conventions support. A shared convention for writing identifiers still leaves an issued identifier’s assignment to be resolved. Reopen the affected comparison when a declaration changes the admissible construction or reading, or a new binding changes the referent. [W3C RDF 1.1 Concepts, §§1.3 and 2](https://www.w3.org/TR/rdf11-concepts/) · [SMT-LIB standard, §§5.2–5.3](https://smt-lib.org/papers/smt-lib-reference-v2.7-r2025-04-09.pdf)

