---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:8"
section_title: "Common Anti-Patterns And Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__010_common-anti-patterns-and-repairs.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:8 — Common Anti-Patterns And Repairs"
line_start: 83332
line_end: 83341
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "G.11"
  - "G.5"
keywords:
---

### E.18.3:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **P2W as launch permission** | A carry-through note is used to begin work. | Add method, work-plan, work-entry, or gate record under the direct pattern before work is authorized. |
| **Flow card as architecture decision** | A P2S flow card is treated as the decision or ADR. | Keep flow structure in E.18.3 or C.32.P2S; use `C.32.PAD` and `C.32.ADR` for decision and ADR projection. |
| **Network graph as admitted slice** | Raw member paths, edge labels, copied positions, or one global tag are inserted into a demonstrative slice. | Select and verify the E.18.NET-conforming network first, then admit typed E.18.3 positions and exact relation-reference epistemes; then map to those same values through A.22.CGUS, or keep the graph provisional. |
| **Evidence path as evidence** | A path through evidence-looking boxes is treated as sufficient evidence. | Open `A.10`, `B.3`, or `G.6`; name the evidence relation and admissible use. |
| **Loop as improvement** | A retry loop in the flow is called quality improvement. | Use `E.23` only when object version, evaluation frame, repair, and re-evaluation are current. |

