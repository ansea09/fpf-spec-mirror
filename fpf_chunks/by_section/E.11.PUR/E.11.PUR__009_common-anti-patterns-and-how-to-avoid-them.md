---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "a87d0ef4f3712507edd6e5a59f4de5bf7a55905a"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 80400
line_end: 80411
dependencies:
  - "A.10"
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

### E.11.PUR:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Recommend before aggregating fit | A partial match is overread as selection. | Resolve all five aspects or return `insufficientBasis`. |
| Rank every candidate | A scalar order hides complements and incomparable results. | Use unordered or partial coordination when that matches the current relation. |
| Use sequence as WorkPlan | Pattern-use relations acquire dates, resources, and work authority that no such relation establishes. | Create an A.15.2 WorkPlan only when intended work is current. |
| Copy or merely expect the prerequisite result | Duplicated kind and signature can drift from the candidate expectation, while an expectation alone proves no result or basis. | Reference the exact expectation and one current E.11.PUA closure finding; if its result or direct basis is absent, keep the precedence relation non-obtaining. |
| Treat a context label as identity | A project, domain, or context label is made a participant or identity field for recommendation or coordination. | Identify the C.2.1 episteme from its claim content, EntityOfConcern, and effective reference scheme; keep every neighboring scope, model-use, work, and qualification relation separate. |
| Treat recommendation as authorization | Guidance bypasses evidence, gate, commitment, or work governance. | Continue to the direct evidence, gate, decision, authorization, or work pattern for that stronger claim. |
| Repeat a result under another stage name | The same question is answered again and the two result descriptions can drift. | Compare the earlier result under the pattern that defines or tests it; cite a matching result or reopen the smallest changed result question. |

