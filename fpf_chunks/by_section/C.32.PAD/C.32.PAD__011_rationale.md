---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__011_rationale.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:10 — Rationale"
line_start: 60913
line_end: 60920
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:10 - Rationale

C.32.PAD exists because candidate synthesis and architecture decision are different work moments. C.32 builds the option space; PAD commits the project to a current architecture option or bounded exception and records the method and work consequences of that commitment.

The pattern keeps three objects apart: `ArchitectureOf@Context` as the architecture claim over structures, `ArchitectureDecisionRelation@Project` as the project relation that selects and obligates, and `ArchitectureDecisionDescription@Project` as the description that can be published in ADR-like or other forms. This lets FPF reuse its existing description, method, work, evidence, assurance, measurement, and publication patterns instead of creating a separate architecture-only duplicate ontology.

The pattern is holonic because the same decision relation can apply to systems, organizations, methods, roles, built assets, AI-agent workflows, evidence practices, or other admitted holon kinds after affected structures, bearers, roles, and work boundaries are rebound.

