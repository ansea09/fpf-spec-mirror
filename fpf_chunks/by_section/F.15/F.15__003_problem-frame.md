---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__003_problem-frame.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:2 — Problem frame"
line_start: 92755
line_end: 92767
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

### F.15:2 - Problem frame

Unification work fails when composition is claimed before locality and continuity have been checked:

1. **Locality leak.** A same-spelled label is treated as one meaning across contexts.
2. **Row sprawl.** Concept-Set rows grow laterally with near-duplicates.
3. **Role or status inflation.** Adjectival, temporal, or source-label variants become new role or status types.
4. **Silent rewrite.** An edition or rename changes meaning while keeping the old row or name.
5. **Bridge hardening.** A weak Bridge is later used as equivalence without a new witness set.
6. **Register split.** Unified Tech and Plain labels drift apart and no longer refer to the same local sense.

F.15 catches these failures before the slice is used for cross-context reuse, naming, assurance, or downstream claims.

