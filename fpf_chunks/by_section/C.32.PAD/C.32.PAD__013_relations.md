---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__013_relations.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:12 — Relations"
line_start: 66088
line_end: 66101
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.6"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
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
  - "C.30.TFS-REL"
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
  - "E.18.NET"
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

### C.32.PAD:12 - Relations

- **Builds on:** `A.15.6`, `A.2`, `A.2.1`, `C.30`, `C.30.ASV`, `C.30.AD`, `C.30.TFS-REL`, `E.18.NET`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.ACS`, `C.32.ACE`, `C.32.CONWAY`, `C.32.FAIL`, `C.25`, `C.16`, `C.29`, `C.31`, and `C.31.ASAP`.
- **Comparison and selection boundary:** Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for selected-set result declaration, and `C.11` for local choice. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. PAD records the architecture decision relation with its exact composite project-work participant after those inputs are sufficient.
- **Description boundary:** `C.30.AD` and `C.30.ASV` govern architecture-description and selected-structure view adequacy. PAD may cite those descriptions but does not replace them.
- **Structural-information boundary:** `C.33`, `C.34`, and `C.35` may support PAD only for captured structure, lost structure, preservation adequacy, generated-carrier typing, or discovered-carrier typing used by the decision relation. Use PAD for the decision relation, rationale, consequences, accepted losses, Method consequences, Work consequences, source return, repair, and supersession claims.
- **Publication boundary:** Use `C.32.ADR` to project an `ArchitectureDecisionDescription@Project` into ADR-like form, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability.
- **Adequacy boundary:** `C.32.ADA` evaluates a PAD decision relation, method docking, and publication projection for a declared use.
- **P2S docking:** P2S reaches PAD only when implementation commitment is live; PAD records the decision relation and returns reopen conditions to P2S when actual structures, eval results, or source-return change the architecture question.
- **Project system-of-interest boundary:** Use `A.15.6` for composite project Work, actual-versus-intended System designation, independent Work, change and use facts, project-network judgment, and `missing-substrate[project-selection-conjunction]`. `E.10.ROLE` recovers `SystemOfInterestRole` wording; use `A.2` and `A.2.1` separately for local kind, classification, and obtaining assignment. PAD cites those objects only when the architecture decision uses them and proves none of them.
- **Network and architecture-influence boundary:** use `E.18.NET` to identify the selected network, its members, obtaining cross-flow occurrences, constraints, endpoints, and use frame; `C.30.TFS-REL` defines architecture use; `C.32.CONWAY` is the pattern for the synthesis frame and exact qualified pair row. PAD cites the smallest exact refs and never turns a record or row citation into network membership, a direct relation occurrence, actor identity, performance, or actual structure effect.
- **Method and work boundary:** `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, and `C.24` govern method descriptions, work plans, readiness, pattern-use recommendations, and agentic tool-use work.
- **Evidence, assurance, and gate boundary:** `A.10`, `B.3`, and `A.21` govern evidence relations, assurance calculus, and gate profiles when those claims are current.

