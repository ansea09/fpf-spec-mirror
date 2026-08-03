---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__003_problem.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:2 — Problem"
line_start: 39229
line_end: 39236
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

### B.3.4:2 - **Problem**

Without a calculus for evidence aging, FPF models are vulnerable to three critical failure modes:

1.  **Silent Risk Accumulation:** Trust silently decays. A component's high `AssuranceLevel` can become an illusion, resting on foundational evidence that is no longer valid in the current operational context. When aggregated, this stale trust propagates upwards, creating a seemingly robust system-of-systems that is, in fact, incredibly brittle.
2.  **Audit Illusion:** An assurance target can pass an audit with flying colors, showing a complete set of anchors to high-quality evidence, yet be fundamentally untrustworthy because that evidence is obsolete. This leads to a false sense of security and undermines the very purpose of the assurance case.
3.  **Maintenance Paralysis:** Without a systematic way to flag stale evidence, re-validation efforts are often misdirected. Teams either engage in costly, unfocused re-testing of everything, or, more commonly, do nothing, allowing epistemic debt to accumulate until a failure forces a crisis.

