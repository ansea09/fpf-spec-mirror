---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__010_consequences.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:9 — Consequences"
line_start: 55337
line_end: 55351
dependencies:
keywords:
---

### C.31.RSA:9 - Consequences

Benefits:

- Reusable structure and bespoke residue become visible without a false architecture amount.
- Practitioners get a cheap triage before accounting.
- Report-only shares can guide repair without becoming proof.
- Evidence reuse, work repeatability, interface grammar, and bounded exceptions can be separated instead of averaged.

Costs:

- Some attractive reuse reports remain report-only.
- Numeric shares require declared `accountingBasisRef`, declared scale or unitless-value rule, relevant unit and polarity, admissible comparability relation, and comparator admission named by value before they can guide outside-RSA comparison, ranking, selection, gate, or decision use.
- The pattern raises a source-return question whenever accounting hides distinctions needed by downstream action.

