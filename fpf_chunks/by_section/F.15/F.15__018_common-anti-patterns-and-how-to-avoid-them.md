---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:14"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__018_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:14 — Common Anti-Patterns and How to Avoid Them"
line_start: 86217
line_end: 86230
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

### F.15:14 - Common Anti-Patterns and How to Avoid Them

| Code | Anti-pattern | Symptom | Why it breaks | Harness catch and repair |
| --- | --- | --- | --- | --- |
| H1 | Row of one | A Concept-Set row spans one context | Fake unification | SCR-F15-S9 fails; drop the row or add the second SenseCell |
| H2 | Bridge by label | Same name is assumed across contexts | Imports meaning and hides loss | SCR-F15-S12 fails; write a Bridge Card or withdraw the claim |
| H3 | Silent edition swap | A new edition keeps the old context without a recency decision | Retcons earlier claims | RSCR-F15-E1 fails; declare new context or explicit recency |
| H4 | Locality blur | A Local-Sense mixes contexts | Cross-context clustering | SCR-F15-S3 fails; split back by context |
| H5 | Window as type | A time or scale variant becomes a new status type | Status-family inflation | SCR-F15-S14 or RSCR-F15-E11 fails; use F.10 value or window |
| H6 | Role fusion by convenience | A bundle or incompatibility becomes one RoleDescription | Hides role relation structure and assignment checks | SCR-F15-S15 fails; use A.2.7, A.2.1, F.6, and A.15.1 |
| H7 | Alias as merge | Alias hides meaning change | Loses history | RSCR-F15-E8 fails; mint new RoleDescription or row |
| H8 | CL optimism | Bridges quietly strengthen over time | Over-trusts reuse | RSCR-F15-E9 or E10 fails; recheck witnesses and admitted use |
| H9 | Plain label drift | Plain label suggests another kind | Reader imports wrong prototype | SCR-F15-T2 or T3 fails; repair label or add kind head and gloss |

