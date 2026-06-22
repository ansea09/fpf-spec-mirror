---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Recommendation and Pattern-Use Sequence"
section_id: "E.11.PUR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__003_problem.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "E.11.PUR — Pattern-Use Recommendation and Pattern-Use Sequence"
  - "E.11.PUR:2 — Problem"
line_start: 65705
line_end: 65713
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.5"
  - "A.16"
  - "A.21"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "E.8"
keywords:
---

### E.11.PUR:2 - Problem

Without an explicit pattern-use recommendation relation, four failures recur:

1. A pattern that only recommends a next FPF use is overread as if it performed work, passed a gate, or authorized work.
2. Applicability and recommendation collapse: "this pattern can be used" becomes "this pattern is the selected useful use now."
3. Several pattern uses are described as a workflow or lifecycle, even when they are only a recommended pattern-use sequence.
4. Teaching language such as "first useful move" becomes a false kind and starts competing with `U.Work`, `U.WorkPlan`, P2W, A.16 language-state moves, C.24 call planning, and C.30 architecture candidate material.

