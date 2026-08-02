---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__008_conformance-checklist.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:7 — Conformance Checklist"
line_start: 77354
line_end: 77368
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.22.PFR"
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
| `PUR-4` | Recommendation | Recommended candidate is applicable and its expected result answers the current concern under a compact explicit rationale. `ordinaryCompact` has no applicability-finding ref; `relianceBearing` has one current finding with five addressable fit findings. |
| `PUR-5` | Coordination | All members concern the same bounded coordination question and have distinct candidate identities. |
| `PUR-6` | Ordering mode | Unordered has no pairwise relations; partial and total order contain only justified pairwise relations. |
| `PUR-7` | Exact precedence | `prerequisiteResult` reuses the prerequisite candidate's expectation and one current E.11.PUA closure finding that identifies the exact result, direct owner, governed relative object, category-correct basis, and governor, and its stated condition is satisfied; other basis values leave both result positions absent. |
| `PUR-8` | Boundary | Recommendation or coordination does not assert plan, work, gate, decision, authorization, actual Problem, actual Transformation, or subject result. |
| `PUR-9` | Problem actuality | A Problem-frame fit or ProblemCard is not an actual Problem; any relied-on Problem resolves to one C.22.PFR occurrence and keeps support and adverse-episode identity separate. |
| `PUR-10` | Plain move | *Next move* names only a recommendation or conditional pattern-use continuation; it creates no Move identity and performs no Work or Transformation. |

