---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:6"
section_title: "Objects under check"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__008_objects-under-check.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:6 — Objects under check"
line_start: 79221
line_end: 79236
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

### F.15:6 - Objects under check

F.15 may check these values together, but does not redefine them:

1. `U.BoundedContext` cards from F.1.
2. Local-Senses from F.2 and F.3.
3. SenseCells, meaning `(Context, Local-Sense)`.
4. Concept-Set rows from F.7.
5. RoleDescriptions from F.4, each describing one local `U.Role` through one SenseCell.
6. Bridge Cards from F.9.
7. Status families, values, confidence, and windows from F.10 or the direct status pattern.
8. Aliases from F.13.
9. Candidate names and durable names from F.5, F.8, F.14, F.17, and F.18.

If the slice contains role assignments, performed work, evidence use, source use, publication use, assurance, gate, decision, method, capability, or policy claims, F.15 records that those claims leave the harness for direct governing patterns. It does not absorb them.

