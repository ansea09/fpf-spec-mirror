---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:10"
section_title: "Twin-register checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__012_twin-register-checks.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:10 — Twin-register checks"
line_start: 93772
line_end: 93790
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.Role"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:10 - Twin-register checks

Use these checks when a Unified Tech label and Plain label are both present.

**SCR-F15-T1 (Same local sense).**
`TechLabel t and PlainLabel p -> both resolve to the same SenseCell or NameCard target.`

**SCR-F15-T2 (Same kind).**
`TechLabel t names kind K -> PlainLabel p does not suggest another kind.`

**SCR-F15-T3 (Ambiguous head guarded).**
`PlainLabel p has a high-risk head -> first use includes a kind head or short gloss.`

**SCR-F15-T4 (No normative displacement).**
`PlainLabel p is reader-facing -> it does not replace the Unified Tech label in normative Core claims.`

**SCR-F15-T5 (Bridge before copying).**
`PlainLabel p is reused in another context -> F.9 Bridge Card or F.17 public term-sheet row exists first.`

