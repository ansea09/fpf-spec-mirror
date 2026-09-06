---
chunk_kind: "child"
pattern_id: "C.2.5"
pattern_title: "U.LanguageStateClosureDegree"
section_id: "C.2.5:17"
section_title: "Continuing and Withdrawn Authority Handling"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.5/C.2.5__018_continuing-and-withdrawn-authority-handling.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.2.5 — U.LanguageStateClosureDegree"
  - "C.2.5:17 — Continuing and Withdrawn Authority Handling"
line_start: 44544
line_end: 44561
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.LS"
keywords:
  - "candidate-space closure"
  - "closure degree"
  - "reopen"
  - "rival routes"
  - "settledness"
---

### C.2.5:17 - Continuing and Withdrawn Authority Handling

#### C.2.5:17.1 - Authority retention rule
If higher `CD` carried endpoint expectations, guard claims, or route commitments, a closure drop must say which consequences remain and which are withdrawn. Treat any actual authority-relation change separately under its direct pattern, as required by `A.16.2`.

#### C.2.5:17.2 - Admissible retreat record
An admissible retreat through `reopen`, `sketchBackoff`, or `respecify` should retain:

- the prior closure state;
- the reason the prior fixation no longer holds;
- the assumption or route being relaxed;
- the still-binding remainder, if any.

This prevents false continuity after retreat.

#### C.2.5:17.3 - Closure versus obligation boundary
High `CD` may coexist with obligations. When prose treats "closed" as "must now be done", use `A.2.8` to identify the duty bearer, duty, and instituting rule and basis; retain the applicable `governingPatternRef` or `authoritySourceRef` for that obligation claim.

