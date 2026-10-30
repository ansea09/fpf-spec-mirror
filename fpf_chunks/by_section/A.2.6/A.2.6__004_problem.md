---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
section_id: "A.2.6:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__004_problem.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
  - "A.2.6:3 — Problem"
line_start: 6668
line_end: 6675
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.2.2"
  - "A.22"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "C.2.1"
  - "C.2.2"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "E.24.UK"
  - "F.9"
keywords:
  - "alone"
---

### A.2.6:3 - Problem

1. **Unresolved scope wording.** Labels such as *applicability*, *envelope*, *generality* and *capability envelope* can hide different predicates or receiving uses. Recover the intended conditions before applying the common scope algebra.
2. **Abstraction confusion.** Calling G “generality” invited teams to treat “more abstract wording” as “broader scope,” silently masking unstated assumptions.
3. **Split mechanics.** Claims and capabilities need different use conditions, but their scopes share the set algebra. Separate those conditions without duplicating the algebra.
4. **Translation opacity.** Exact local-sense translation was confused with ordinary designation resolution, causing automatic Bridge use and hidden changes to the supported slice set.
5. **Overloaded words.** A phrase such as *validity* can mean a scope condition or an assurance judgment; *operation* can name an operation application or performed Work. Recover the intended object before applying the scope rule.

