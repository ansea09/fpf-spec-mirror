---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:5"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__006_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:5 — Common Anti-Patterns and How to Avoid Them"
line_start: 40110
line_end: 40118
dependencies:
  - "A.10"
  - "B.3"
  - "B.3.4"
  - "B.3.5"
  - "C.28"
keywords:
  - "assurance profile"
  - "conceptual correspondence"
  - "constructive support"
  - "empirical validation"
  - "use-qualified assurance"
  - "verification"
---

### B.3.3:5 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure in use | Repair |
| --- | --- | --- |
| Tested but referring to different things | Requirements and architecture use “Sensor” for different participants; the test concerns only one. | Resolve that correspondence and re-examine affected claims; more test links do not fix it. |
| Perfect blueprint, unsupported operation | A proof assumes conditions that the actual system has not been shown to meet. | Obtain or use the needed empirical and assumption evidence for the actual claim, or narrow the conclusion. |
| Maturity by receipt | A fresh smoke test and a term mapping receive a positive performance label. | Judge the support for the requested performance, not the receipt count or type combination. |
| Proof as an admission toll | Sufficient empirical support is rejected because an unrelated formal proof is absent. | Apply the receiving claim's evidence rules; retain formal proof obligations where their contribution is necessary. |

