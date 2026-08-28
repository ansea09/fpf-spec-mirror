---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__003_problem-frame.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:2 — Problem frame"
line_start: 96134
line_end: 96147
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:2 - Problem frame

Unification work fails when composition is claimed before local meaning, exact object recovery, and continuity are checked:

1. **Locality leak.** Same spelling is treated as one meaning without comparing exact `<ReferenceScheme, LocalSenseClaim>` projections.
2. **Row sprawl.** F.17 rows or F.18 NameCards multiply although an existing governed value and admitted naming use already suffice.
3. **System-role or status inflation.** Adjectival, temporal, or source-label variants become new system-role kinds or status values without recovery through the pattern that defines them.
4. **Silent rewrite.** An edition or rename changes claim content while a stable id is treated as continuity proof.
5. **Bridge hardening.** A description, Card, `CL`, or earlier relation claim is later used as equivalence or use authority without a current obtaining occurrence and separate bounded-use claim.
6. **Check collapse.** Scope, rule, application/work, result claim, witness/evidence path, record episteme, publication, and currentness are treated as one object.
7. **Register split.** Tech and Plain designation expressions drift away from the exact current F.18 NameCard, governed value, or local sense.

F.15 catches these failures before the finite slice is used for naming reuse, cross-local comparison, assurance input, or another downstream claim.

