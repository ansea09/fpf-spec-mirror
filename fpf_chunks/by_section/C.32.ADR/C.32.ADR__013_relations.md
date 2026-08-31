---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__013_relations.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:12 — Relations"
line_start: 66307
line_end: 66318
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
  - "C.32.ADA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
keywords:
  - "ADR projection"
  - "ArchitectureDecisionDescription@Project"
  - "ArchitectureDecisionRecordProjection@Project"
  - "architecture decision record"
  - "consequences"
  - "method-use instruction"
  - "publication boundary"
  - "rationale"
  - "section function"
  - "supersession"
---

### C.32.ADR:12 - Relations

- **Builds on:** `C.32.PAD`, `C.32.P2S`, `C.30.AD`, `C.30.ASV`, `E.17`, `E.24.PUB`, `A.15`, `E.8`, `E.11.PUR`, and `C.32.ADA`.
- **Decision boundary:** Use `C.32.PAD` for the project architecture decision relation. C.32.ADR publishes an `ArchitectureDecisionDescription@Project`; it is not generic ADR guidance and not a second decision authority.
- **Structural-information boundary:** ADR-like projections may cite `C.33`, `C.34`, or `C.35` only to show captured structure, lost structure, preservation adequacy, generated-carrier typing, or discovered-carrier typing behind the projected decision. The ADR projection remains a publication projection of a decision description; it is not the architecture, the decision relation, or generated-carrier authority.
- **P2S docking:** P2S may cite an ADR projection as one stage where decision, rationale, method expectation, and source-return are published for readers; ADR does not carry the whole architecturing flow.
- **Architecture-description boundary:** Use `C.30.AD` and `C.30.ASV` for architecture-description and view adequacy. ADR carries refs and reader-use slices, not full description authority.
- **Pattern and method boundary:** Use `E.8` when the published object is an FPF pattern, `E.11.PUR` for pattern-use recommendation, and `A.15` for method and work claims.
- **Publication boundary:** Use `E.17` and `E.24.PUB` for MVPK face, publication carrier, and publication-use claims not specific to architecture decisions.
- **Evaluation boundary:** Use `C.32.ADA` for decision adequacy; use `C.32.ACE`, `C.16`, `A.10`, `B.3`, or `A.21` for eval, measurement, evidence, assurance, or gate claims.
- **Package boundary:** A record package map aids navigation among records. It does not decide active architecture by file order; PAD relations and status refs remain governing.

