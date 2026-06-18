---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__002_problem-frame.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:1 — Problem Frame"
line_start: 32943
line_end: 32948
dependencies:
  - "A.10"
  - "B.3"
  - "B.3.3"
  - "B.4"
keywords:
  - "decay"
  - "epistemic debt"
  - "evidence aging"
  - "freshness"
  - "stale data"
---

### B.3.4:1 - **Problem Frame**

The FPF assurance model (Pattern B.3.3) provides a robust framework for building trust in holons by anchoring claims to a rich body of evidence. However, it implicitly treats this evidence as timeless. A proof verified today is assumed to hold forever; a validation test run last year is given the same weight as one run yesterday. This assumption is dangerously flawed in any dynamic environment.

Consider a bridge certified in 1980. The assurance case, resting on evidence about steel fatigue from that era, would be considered highly reliable *at that time*. Today, after decades of environmental change, new material science insights, and an entirely different traffic load, would we still trust that original certification without re-evaluation? The context has drifted, and the original evidence has lost its relevance. FPF requires a formal mechanism to account for this natural decay of trust.

