---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__006_solution.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:4 — Solution"
line_start: 85894
line_end: 85902
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

### F.15:4 - Solution

The harness has two families of rules.

1. **Static Conformance Rules (SCR).** Check the current snapshot. Contexts, Local-Senses, SenseCells, rows, RoleDescriptions, bridges, windows, aliases, and names must satisfy their direct local rules now.
2. **Regression and Stability Conformance Rules (RSCR).** Check a changed snapshot against the earlier snapshot. The rule asks what stayed the same, what changed, what must be forked, what must be retired, and which bridge or name needs a fresh witness.

Both families are judgement schemas over content claims. They do not prescribe storage, implementation, team responsibility, or publication format.

