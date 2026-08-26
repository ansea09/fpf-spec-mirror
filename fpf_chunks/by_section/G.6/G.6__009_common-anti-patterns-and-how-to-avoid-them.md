---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 101929
line_end: 101941
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
  - "F.6"
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
| MethodDescription as run trace | Generic declarations acquire actual participants, time, or results by graph membership. | Cite one independently admitted dated Work ref, its actual performer refs, and applicable obtaining F.6 relation refs through §4.1. Keep Method enactment, resources, direct participation, and A.6.1 bindings separate; expose an assignment occurrence ref only when the receiving use consumes it. |
| Generic result node | Measurement, evaluation, aggregation, episteme, outcome, and decision collapse. | Keep each local result under its domain governor and each durable assertion under C.2.1. |
| Provenance as result or assurance | A path or ledger row is read as truth, currentness, safety, permission, or acceptance. | Use A.10, G.11, and B.3 under their entry conditions, and state the exact local result under its applicable predicate and pattern. |
| Citation as actual use | A downstream record cites a path and is assumed to have used it. | Ground dated downstream work and one exact premise, reference, argument, or decision-use relation. |
| Workflow overread | A declarative path becomes a method or action route. | Handle Work under A.15.1 and transformation-flow structure under E.18; limit G.6 to representation and citation. |
| Global refresh | One changed source or relation reopens every graph. | Reopen only the affected path, slice, node projection, or relation-edge projection. |

