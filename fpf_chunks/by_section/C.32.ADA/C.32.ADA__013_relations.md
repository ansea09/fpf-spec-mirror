---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__013_relations.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:12 — Relations"
line_start: 63187
line_end: 63197
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:12 - Relations

- **Builds on:** `C.32.PAD`, `C.32.ADR`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.ACS`, `C.32.ACE`, `C.32.CONWAY`, `C.32.FAIL`, `C.30.AD`, `C.30.ASV`, `A.15`, `C.16`, `C.25`, `C.29`, `E.17`, and `E.21`.
- **Evaluation boundary:** ADA evaluates architecture-decision adequacy for declared use. It does not perform candidate synthesis, comparison, selection, selected-set publication, local choice, evidence support, assurance, gate passage, governance enforcement, or pattern-quality evaluation.
- **Decision and projection boundary:** Use `C.32.PAD` to repair the decision relation and `C.32.ADR` to repair ADR-like publication projection.
- **Description and structure boundary:** Use `C.30`, `C.30.AD`, and `C.30.ASV` for architecture claim, description, and view adequacy.
- **P2S docking:** Use `C.32.P2S` when a weak decision-adequacy row must reopen the connected architecturing flow rather than only repair the decision record.
- **Method and work boundary:** Use `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, and `C.24` for method, work, readiness, pattern-use, and agentic tool-use claims.
- **Characteristic and eval boundary:** Use `C.32.ACS`, `C.32.HCS`, `C.25`, `C.32.ACE`, `C.16`, `C.31`, and `C.31.ASAP` for characteristic rows, Q-Bundles, eval programs, measurement, modularity, and scale preference.
- **Evidence, assurance, gate, and governance boundary:** Use `A.10`, `B.3`, `A.21`, and local governance patterns when those claims are live.

