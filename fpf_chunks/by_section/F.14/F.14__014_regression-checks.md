---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:13"
section_title: "Regression checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__014_regression-checks.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:13 — Regression checks"
line_start: 88626
line_end: 88635
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:13 - Regression checks

| Check | Reopen condition |
| --- | --- |
| RSCR-F14-01 | Reopen when candidate names grow faster than recovered values. |
| RSCR-F14-02 | Reopen when a role name starts carrying assignment, capability, method, work, evidence, status, source, or publication claims. |
| RSCR-F14-03 | Reopen when a status label starts carrying role, holder, assignment, or work claims. |
| RSCR-F14-04 | Reopen when a public or cross-context name is reused without F.9, F.17, or F.18 admission. |
| RSCR-F14-05 | Reopen when role-relation expressions become fake holders, fake capabilities, or fake method families. |

