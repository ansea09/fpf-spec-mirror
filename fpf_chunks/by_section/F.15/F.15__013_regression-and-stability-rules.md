---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:11"
section_title: "Regression and stability rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__013_regression-and-stability-rules.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:11 — Regression and stability rules"
line_start: 92038
line_end: 92101
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

### F.15:11 - Regression and stability rules

The RSCR family compares an earlier snapshot `@t0` and a later snapshot `@t1`.

#### F.15:11.1 - Contexts and editions

**RSCR-F15-E1 (No silent replacement).**
`Context C@t0 edition e0, Context C@t1 edition e1, e1 != e0 -> new context or explicit recency decision.`
A new edition becomes a new context when sense changes; otherwise the recency decision is visible.

**RSCR-F15-E2 (Known confusion check).**
`C@t1 derives from C@t0 -> known confusion cases from C@t0 are rechecked or explicitly retired.`
Old traps do not disappear merely because an edition changed.

#### F.15:11.2 - Local-Senses and SenseCells

**RSCR-F15-E3 (Reconstructible Local-Sense).**
`Local-Sense lambda@t0 changes attestations -> lambda@t1 remains reconstructible from attestations@t1.`

**RSCR-F15-E4 (SenseCell context stability).**
`SenseCell (C, lambda)@t0 -> (C2, lambda2)@t1 -> same cell only if C2 = C and lambda2 preserves local sense.`
A SenseCell does not migrate across contexts through edits.

#### F.15:11.3 - Concept-Set rows

**RSCR-F15-E5 (Row identity).**
`Row rho@t0 with cells cell_i -> row rho@t1 is same row only if each cell preserves its local sense.`
If a cell changes sense, mint a new row and retire the old row.

**RSCR-F15-E6 (Add or retire before silent mutation).**
`Row rho loses or gains a cell because an edition split occurred -> preserve old row and add or retire rows explicitly.`

#### F.15:11.4 - RoleDescriptions

**RSCR-F15-E7 (Single-cell continuity).**
`RoleDescription tau@t0 -> tau@t1 -> refersTo(tau@t1, one SenseCell) and same cell or justified switch.`

**RSCR-F15-E8 (Alias for rename, new RoleDescription for meaning change).**
`name(tau@t0) -> name(tau@t1) -> alias if only label changed; new RoleDescription if described role or local sense changed.`

#### F.15:11.5 - Bridges

**RSCR-F15-E9 (Recheck Bridge on endpoint movement).**
`Bridge beta@t0 and either endpoint cell changes -> beta is rechecked; CL, loss, admitted use, and witness may change.`

**RSCR-F15-E10 (No drift to equivalence).**
`Bridge beta kind is not equivalence at t0 and equivalence is claimed at t1 -> new witness set is required.`
Equivalence is rare and cannot arrive by gradual wording drift.

#### F.15:11.6 - Status windows and role relation structure

**RSCR-F15-E11 (Window stability).**
`Status family windows@t0 -> windows@t1 -> changed only when variance of meaning or use is shown.`

**RSCR-F15-E12 (Role-relation stability).**
`role incompatibility, bundle, qualification, or role-requirement substitution@t0 -> @t1 -> preserved, retired, or restated before assignment or naming use.`
No later RoleDescription fuses roles that were kept distinct by A.2.7.

#### F.15:11.7 - Public naming

**RSCR-F15-E13 (Public name continuity).**
`Public or term-sheet-facing name changes -> F.17 or F.18 records lineage, alias, split, merge, or retirement.`
Local rename is not enough when the name already faces other contexts.

