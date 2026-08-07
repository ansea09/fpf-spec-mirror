---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 101214
line_end: 101226
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Edge as fact | Drawing or storing an edge is mistaken for an obtaining relation. | Establish the exact direct relation under its governor, then cite it through a representation record. |
| Universal evidence edge | `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` absorbs several relation families. | Replace the label with the exact formal, measurement, work, production, source, use, or other direct relation. |
| MethodDescription as run trace | Generic declarations acquire actual participants, time, or results by graph membership. | Ground dated work, role assignment, enactment, resources, and actual direct/A.6.1 bindings separately. |
| Generic result node | Measurement, evaluation, aggregation, episteme, outcome, and decision collapse. | Keep each local result under its domain governor and each durable assertion under C.2.1. |
| Provenance as result or assurance | A path or ledger row is read as truth, currentness, safety, permission, or acceptance. | Use A.10/G.11/B.3 and the exact result owner under their own entry conditions. |
| Citation as actual use | A downstream record cites a path and is assumed to have used it. | Ground dated downstream work and one exact premise, reference, argument, or decision-use relation. |
| Workflow overread | A declarative path becomes a method or action route. | Return work and transformation flow to A.15.1 and E.18; keep G.6 to representation and citation. |
| Global refresh | One changed source or relation reopens every graph. | Reopen only the affected path, slice, node projection, or relation-edge projection. |

