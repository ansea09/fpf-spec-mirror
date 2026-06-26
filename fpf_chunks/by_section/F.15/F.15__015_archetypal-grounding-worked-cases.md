---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:13"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__015_archetypal-grounding-worked-cases.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:13 — Archetypal Grounding - worked cases"
line_start: 85116
line_end: 85174
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

### F.15:13 - Archetypal Grounding - worked cases

#### F.15:13.1 - Activity and task in two run contexts

Contexts: `PROV-O run context` and `IEC 61131-3 run context`.

Local senses: `activity` in the first context and `task` in the second.

F.15 result:

* SCR-F15-S9 passes only if a Concept-Set row lists both SenseCells.
* SCR-F15-S12 requires a Bridge Card. The admitted use may be comparison or explanation, not direct substitution.
* A RoleDescription named `ExecutionRole` may use one local SenseCell only. It does not describe both senses at once.
* If a later edition makes the `task` sense cyclic while the `activity` sense remains non-periodic, RSCR-F15-E9 rechecks the Bridge and may lower `CL`.

#### F.15:13.2 - Service availability row across service and observation contexts

Contexts: `ITIL service-management context` and `SOSA observation context`.

Row: `ServiceAvailability` with one SLO SenseCell and one uptime-observation SenseCell.

F.15 result:

* SCR-F15-S9 passes because two contexts are present.
* SCR-F15-S12 requires Bridge kind, direction, `CL`, loss, and admitted use.
* SCR-F15-S16 treats evidence and assurance claims under A.10 and B.3; the row itself does not make the observation adequate evidence.
* SCR-F15-S14 treats time-window and confidence variation under F.10.

#### F.15:13.3 - Rename a RoleDescription without changing meaning

Slice: `IncidentReviewerRoleDescription` is renamed to `ServiceIncidentReviewerRoleDescription`, while the described local `U.Role` and SenseCell stay the same.

F.15 result:

* RSCR-F15-E7 checks single-cell continuity.
* RSCR-F15-E8 admits an alias because only the label changed.
* F.18 updates durable naming if the name is reusable outside the local context.
* If the described role changed, F.15 rejects alias-only treatment; F.4, F.8, and F.18 govern the repaired claim.

#### F.15:13.4 - Weak bridge later claimed as equivalence

Slice: a Bridge between an OWL subclass sense and an FCA order-edge sense was partial overlap at `CL = 2`. A later formal result claims equivalence inside one constrained fragment.

F.15 result:

* RSCR-F15-E10 requires a new witness set for equivalence.
* SCR-F15-S12 updates kind, direction, loss, and admitted use.
* C.29 may govern the mathematical-lens claim; F.15 only checks that the changed Bridge is not silently strengthened.

#### F.15:13.5 - Peak-hours status proposal

Slice: a team proposes `PeakHoursAvailabilityStatus` as a new status family.

F.15 result:

* SCR-F15-S14 fails if the only difference is a time window.
* F.10 governs the status-family and window claim.
* F.14 and F.18 block a new durable name unless a new recovered status family is present.

