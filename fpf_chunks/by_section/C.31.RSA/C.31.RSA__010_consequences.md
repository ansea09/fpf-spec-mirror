---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__010_consequences.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:9 — Consequences"
line_start: 74790
line_end: 74804
dependencies:
  - "A.10"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "G.5"
  - "G.6"
keywords:
  - "accounting basis"
  - "bespoke residue"
  - "refactoring opportunity"
  - "report-only share"
  - "reusable share"
  - "reusable-structure accounting"
  - "source return"
---

### C.31.RSA:9 - Consequences

Benefits:

- Reusable structure and bespoke residue become visible without a false architecture amount.
- Practitioners get a cheap triage before accounting.
- Report-only shares can guide repair without becoming proof.
- Evidence reuse, work repeatability, interface grammar, and bounded exceptions can be separated instead of averaged.

Costs:

- Some attractive reuse reports remain report-only.
- Numeric shares require an explicit counting and scale basis. Comparison needs aligned bases and its comparator; each further claim adds only its own required grounds.
- The pattern raises a source-return question whenever accounting hides distinctions needed by downstream action.

