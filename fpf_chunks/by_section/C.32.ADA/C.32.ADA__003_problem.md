---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__003_problem.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:2 — Problem"
line_start: 67179
line_end: 67186
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
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

### C.32.ADA:2 - Problem

Architecture decisions are multi-kind objects in practice. A decision relation can be strong while its ADR projection is weak. A record can be readable while the decision lacks candidate traceability. A candidate basis can be strong while method docking is absent. A method instruction can be clear while the architecture-characteristic trade-off is hidden.

Because of that, a single pass, single grade, or average score is misleading. Adequacy must be evaluated by coordinates tied to the declared use. "Ready for internal architecture review", "ready for developer work", "ready for ADR publication", and "ready for governance enforcement" can require different stop conditions, but each use still needs complete coordinate inspection.

C.32.ADA supplies an E.21-shaped ordinal evaluation pattern for architecture decisions. It uses the E.21 value domain and labels directly, then defines architecture-decision coordinates over PAD relation, method docking, publication projection, structural description, characteristic trade-off, and evolution. Weak coordinates point back to `C.32.PAD`, `C.32.ADR`, `C.30.AD`, `A.15`, `C.32.ACS`, `C.32.ACE`, `C.16`, `C.25`, or another governing pattern.

