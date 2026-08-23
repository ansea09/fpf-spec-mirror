---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__007_bias-annotation.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:6 — Bias-Annotation"
line_start: 100863
line_end: 100874
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

### G.6:6 - Bias-Annotation

| Bias | Guard |
| --- | --- |
| Graph-authority bias | A node or edge represents an object or direct relation only after its governor establishes it. |
| Generic-edge bias | Reject fallback `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, and `evidences` relations; recover the exact direct relation. |
| Result-node bias | Keep subject result, result episteme, carrier, outcome, assurance, and later action distinct. |
| Declaration-runtime bias | A method, description, policy, clause, signature, or plan establishes no occurrence or actual binding. |
| Provenance-as-truth bias | Origin and history support only their named bounded claim; provenance is not truth, safety, approval, or assurance. |
| Path-as-workflow bias | Graph path identity supports citation and refresh; actual work and transformation flow retain their subject patterns. |
| Ledger-process bias | The ledger contains replayable provenance records, not campaign status, review proof, or work-progress notes. |

