---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 76437
line_end: 76446
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

### E.11.PUR:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Recommend before aggregating fit | A partial match is overread as selection. | Resolve all five aspects or return `insufficientBasis`. |
| Rank every candidate | A scalar order hides complements and incomparable results. | Use unordered or partial coordination when that matches the current relation. |
| Use sequence as WorkPlan | Pattern-use relations acquire dates, resources, and work authority they do not own. | Create an A.15.2 WorkPlan only when intended work is current. |
| Copy the prerequisite result | Duplicated kind and signature can drift from the candidate expectation. | Reference the exact expectation. |
| Treat recommendation as authorization | Guidance bypasses evidence, gate, commitment, or work governance. | Continue to the direct governing pattern for the stronger claim. |

