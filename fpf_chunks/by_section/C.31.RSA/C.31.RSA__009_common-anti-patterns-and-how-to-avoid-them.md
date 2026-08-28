---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 62224
line_end: 62234
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

### C.31.RSA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ArchitectureAmount` | A reusable share is treated as an amount of architecture. | Restate as report-only share under one declared accounting basis. |
| `ResidueIsWaste` | All bespoke residue is marked bad. | Split repairable residue from bounded exception. |
| `HeterogeneousPseudoSum` | Templates, interface variants, work items, evidence packages, and exceptions are summed as if they shared one unit. | Declare accounting basis or keep the decomposition qualitative. |
| `EvidenceReuseAsAssurance` | Evidence reuse share is treated as assurance. | Apply A.10, B.3, or G.6 for validity and assurance reliance. |
| `RSAAsC31Duplicate` | RSA repeats every modularity characteristic. | Keep RSA to reusable loci, bespoke residue, residual uncertainty, report-only shares, and source-return conditions. |
| `NoSourceReturn` | Accounting hides source distinctions used by downstream action. | Add `sourceReturnCondition` or narrow admissible use. |

