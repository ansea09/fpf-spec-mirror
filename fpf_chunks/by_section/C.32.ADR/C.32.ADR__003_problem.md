---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__003_problem.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:2 — Problem"
line_start: 64694
line_end: 64705
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

### C.32.ADR:2 - Problem

ADR practice is useful because it makes architectural decisions small enough to read and update. It is also easy to misuse. A record can become a substitute for the decision relation, a loose essay about architecture, a copied architecture description, or a method prescription with no recoverable target structure.

C.32.ADR treats ADR as a publication projection. The project decision relation belongs to `C.32.PAD`. The architecture description belongs to `C.30.AD` and related view patterns. The method description or pattern-use recommendation belongs to `A.15`, `E.8`, and `E.11.PUR` when those claims are live. The ADR-like record publishes a decision description for a declared reader and use.

For a principle framework, use C.32.ADR only in the exceptional case where the accepted framework-architecture answer is also an exact project architecture decision with the `ArchitectureDecisionRelation@Project` and `ArchitectureDecisionDescription@Project` required by this pattern. Its prior basis may then cite the accepted answer and the exact `E.9` DRR that records it; acceptance remains a separate decision, and `E.4.PFAD` only profiles the framework-specific content. An ADR-like publication may project the question, selected answer, alternatives, rationale, consequences, status, links, and supersession conditions for declared readers. That projection remains separate from the answer, its acceptance, the DRR, framework realization, pattern quality, and publication adequacy. When the principle-framework answer is not an exact project architecture decision, publish the selected decision episteme or a reader-specific projection through `E.17` and `E.24.PUB`; do not use C.32.ADR.

The section question is therefore not "which headings are allowed?" The section question is "which decision functions must a reader recover?" A heading can vary by organization or industry, but the record must carry the decision question, candidate options or reason no candidate set is live, outcome, rationale, consequences, method-use instruction when the decision guides work, work split, confirmation or eval path, source-return, status, and supersession or reopen condition.

ADR-like projection is not software-only. Engineering trade-study records, safety-certification rationale, design review memos, BIM decision logs, method-governance records, and organization-design records can play the same publication role after the project decision relation and record use are typed. The source form may differ; the FPF section functions stay recoverable.

