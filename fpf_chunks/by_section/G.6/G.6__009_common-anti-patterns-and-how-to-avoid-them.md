---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 96049
line_end: 96059
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.21"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "E.18"
  - "E.18.2"
  - "E.24"
  - "E.5.2"
  - "F.10"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Narrative-only provenance | The reader cannot replay which evidence carried the claim. | Write `PathCitationRecord` with nodes, edges, windows, and `NotCarried`. |
| Evidence role node | Recreates old `U.EvidenceRole` ontology. | Use evidence-use relation nodes and work-facing role assignment refs only when producer externality matters. |
| Workflow overread | Treats declarative graph structure as work instruction. | `PathId` cites declared provenance graph structure; if actual work is current, use `A.15.1`; if transformation-flow structure is current, use `E.18`. |
| Dashboard-to-decision shortcut | A visible cell is treated as a downstream decision basis by itself. | Use `F.10` for status-use, `A.10` for source evidence, and the direct governing pattern for the stronger downstream use. |
| Provenance means truth | Origin, history, or attestation is treated as truth, safety, or adequacy. | Keep provenance as evidence for a named claim and use; apply direct patterns for truth-claim adequacy or assurance. |
| Global refresh | One source change triggers an undifferentiated rewrite of every record. | Reopen only affected `PathId`, `PathSliceId`, or graph subpath. |

