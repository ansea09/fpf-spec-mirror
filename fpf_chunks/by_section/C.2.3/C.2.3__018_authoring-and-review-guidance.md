---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:17"
section_title: "Authoring and Review Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__018_authoring-and-review-guidance.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:17 — Authoring and Review Guidance"
line_start: 40246
line_end: 40259
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
keywords:
  - "F-scale"
  - "F0-F9"
  - "Formality"
  - "language-state separation"
  - "proof"
  - "rigor"
  - "specification"
---

### C.2.3:17 - Authoring and Review Guidance

#### C.2.3:17.1 - For authors

Declare `F` honestly and early. A low `F` declaration is not a defect; it is often the correct statement about an early expression. Raise `F` by changing the expression form itself, not by applying prestige language or by pointing to surrounding machinery.

#### C.2.3:17.2 - For reviewers

Review the actual claim core. Ask whether the target anchor semantics are visibly satisfied, whether essential support contains segments with lower `R`, lower `F`, or missing witness coverage, and whether status or other characteristics have leaked into the `F` declaration.

#### C.2.3:17.3 - For integrators and assurance leads

Use `F` explicitly in gates and composition analysis, but do not let it absorb work that belongs to `G`, `R`, `CL`, or `C.2.LS`. Large `F` gaps across collaborating epistemes are signals for explicit formalization work, not excuses for wishful leveling.

