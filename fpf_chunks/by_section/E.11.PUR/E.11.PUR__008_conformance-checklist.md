---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__008_conformance-checklist.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:7 — Conformance Checklist"
line_start: 76186
line_end: 76198
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.24"
  - "C.30"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUA"
  - "E.18"
  - "E.18.1"
  - "G.11"
keywords:
---

### E.11.PUR:7 - Conformance Checklist

| ID | Check | Passing condition |
| --- | --- | --- |
| `PUR-1` | Candidate basis | Every evaluated candidate has an inspected Solution and exact result expectation. |
| `PUR-2` | Five aspects | Reliance-bearing applicability has exactly one finding for each fit criterion. |
| `PUR-3` | Aggregate | Every recommendation states an applicability result after all five aspects are considered. When a reliance-bearing applicability finding exists, its result agrees with the recommendation and carries a missing-basis boundary when needed. |
| `PUR-4` | Recommendation | Recommended candidate is applicable and its result answers the current concern under a compact explicit rationale. `ordinaryCompact` has no applicability-finding ref; `relianceBearing` has one current finding with five addressable fit findings. |
| `PUR-5` | Coordination | All members concern the same bounded coordination question and have distinct candidate identities. |
| `PUR-6` | Ordering mode | Unordered has no pairwise relations; partial and total order contain only justified pairwise relations. |
| `PUR-7` | Exact precedence | `prerequisiteResult` reuses the prerequisite candidate's expectation; other basis values leave that position absent. |
| `PUR-8` | Boundary | Recommendation or coordination does not assert plan, work, gate, decision, authorization, or subject result. |

