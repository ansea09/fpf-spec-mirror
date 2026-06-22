---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__004_forces.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:3 — Forces"
line_start: 80359
line_end: 80369
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

### F.14:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Parsimony versus real difference | A small vocabulary is useful only if real distinctions remain recoverable. |
| Locality versus public reuse | Role and status names start in bounded contexts; some later need public or cross-context reuse. |
| Recognition versus assignment | A good role name helps recognition; it does not assign a holder or prove work. |
| Role relation structure versus new role | Role-requirement substitution, incompatibility, qualification, and bundle expressions are useful, but they do not automatically mint a new `U.Role`. |
| Status family versus status name | Time windows, values, confidence, and presentation labels should not multiply status families. |
| Qualifier visibility versus kind discipline | A visible qualifier may belong to role state, work plan, capability, method, status window, evidence, source, or publication rather than the role name. |

