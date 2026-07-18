---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Transformer and Transformed Architecture Correspondence"
section_id: "C.32.CONWAY:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__012_sota-echoing.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.32.CONWAY — Transformer and Transformed Architecture Correspondence"
  - "C.32.CONWAY:11 — SoTA-Echoing"
line_start: 61874
line_end: 61887
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "G.5"
keywords:
  - "Conway correspondence"
  - "changing relation"
  - "coordination cost"
  - "inverse Conway maneuver"
  - "selected-structure correspondence"
  - "transformed holon"
  - "transformer holon"
---

### C.32.CONWAY:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.CONWAY. Each row states which field, repair row, or boundary the draft sets or revises from the source. The source family is used as architecture practice support, not as an ontology import.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32.CONWAY | Concrete C.32.CONWAY mutation | Blocked overread |
|---|---|---|---|---|
| Melvin Conway, `How Do Committees Invent?` (`https://www.melconway.com/Home/Committees_Paper.html`) | Original mature source for the relation between a design organization and the structure of the designed system. It also states the graph-like correspondence idea that later practice uses as Conway's law. | Treat communication and design organization as pressure on architecture candidates. | The frame requires `transformerHolonRef`, `transformedHolonRef`, selected structures on both sides, architecture characteristics under pressure, and `correspondenceClaims`. | The correspondence claim must say which transformer structures constrain which transformed structures, and what candidate change or bounded exception follows. |
| MacCormack, Rusnak, and Baldwin 2012 mirroring hypothesis (`https://doi.org/10.1016/j.respol.2012.04.011`) and Colfer and Baldwin 2016 exceptions survey (`https://www.hbs.edu/ris/Publication%20Files/16-124_7ae90679-0ce6-4d72-9e9d-828872c7af49.pdf`) | Empirical and theory line for product and organization architecture mirroring, including exceptions. It keeps the pattern from treating mirroring as adequacy. | Use correspondence as a hypothesis evaluated across selected structures and exceptions. | Failure-mode rows add mirror-as-adequacy and static-correspondence guards; conformance requires source-return and C.29 use for structural similarity claims. | A mirrored structure must still be evaluated against architecture characteristics, exception cost, and a receiving claim pattern before it can guide a candidate. |
| DORA loosely coupled teams, last updated 2025-10-20 (`https://dora.dev/capabilities/loosely-coupled-teams/`) | Current practitioner line tying architecture, team independence, testing, deployment, coordination load, and inverse Conway. It is load-bearing because it gives observable architecture characteristics, not only terminology. | Treat independent change, testability, deployability, and coordination load as architecture characteristics under pressure when transformer-side structures constrain transformed-holon change. | Solution and checklist require affected architecture characteristics; repair cue `TransformedArchitectureNoTransformerFit` opens inverse-Conway or transformed-architecture retargeting as the candidate-change question. | Evidence about microservices, team autonomy, or work-transfer count must be mapped to selected structures and architecture characteristics before it guides a candidate. |
| Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Current organization-design pattern family for fast flow, team interaction modes, cognitive load, platform teams, and evolving team boundaries toward a desired transformed architecture. | Team types and interaction modes are transformer-side selected structures or candidate-change inputs when they shape architecture synthesis. | Row `inverseConwayRetargeting` and worked cases require migration cost, interaction burden, and evolution window. | Team-topology vocabulary must be converted into selected transformer structures, interaction burden, and candidate-change cost before module-interface, work-authorization, or decision claims are handled by their receiving patterns. |
| Current FPF `A.3.4`, `A.3.4.P`, `E.18`, `A.15`, `A.6.M`, `C.29`, `C.32`, `C.32.MLAO`, and `C.32.FAIL` | Governing local ontology for bounded transformation, transformation-flow structure, work and role claims, module-interface repair, mathematical-lens use, candidate synthesis, residual reduction, and failure repair. | Recover the changing relation and selected structures before using Conway wording. | Relations and conformance rows assign stronger claims to exact receiving patterns and keep C.32.CONWAY inside candidate synthesis. | No new `U.Conway`, no new `U.Correspondence`, no local adequacy kind, and no bypass around architecture-decision work. |

**Source-currentness boundary.** Use each source row only for the C.32.CONWAY field, repair row, or boundary named in that row. Recheck the row when the project's transformer structures, transformed structures, evolution window, source practice, or named receiving FPF pattern changes. If the source row no longer supports the local selected-structure correspondence, lower it to background lineage and keep the candidate frame only when the local architecture-characteristic pressure remains recoverable.

