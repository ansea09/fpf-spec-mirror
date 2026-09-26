---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__002_context.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:1 — Context"
line_start: 23987
line_end: 23994
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

### A.9:1 - Context

**Use this when** a receiving decision needs a combined result, but the law that gives the proposed operation its meaning or preserves a needed property is unresolved. The same input values can support different operations: component success probabilities combine differently for “both succeed” and “at least one succeeds”. Reordering functions can change their result even when the notation looks like an ordinary fold.

The first useful result is a justified combining law with its applicable conditions, a supported limited result or bound, retained separate inputs, or the exact missing premise. Reuse an adequate domain law and its current applicability result without creating another A.9 record.

**Non-use boundary.** B.1 governs whole/part construction, C.29 governs mathematical representation and correspondence, and ULSAM performs an explicitly selected CHR fold over admitted measures. None supplies one universal aggregation algebra. Use their direct results when they already answer the question; A.9 supplies only the unresolved law-selection or property check. Composition of functions or Methods does not require a measured quantity merely to enter this pattern.

