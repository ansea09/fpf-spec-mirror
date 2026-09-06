---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:11"
section_title: "Regression and stability rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__013_regression-and-stability-rules.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:11 — Regression and stability rules"
line_start: 98055
line_end: 98111
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

### F.15:11 - Regression and stability rules

The RSCR family compares exact earlier and later refs for each changed member. Every result names the continuity or change proposition, admitted losses, receiving use, and evidence path. It does not infer identity or difference from spelling, path, stable id, table position, timestamp, or edition label.

#### F.15:11.1 - Schemes, versions, and known confusions

**RSCR-F15-E1 (Exact before/after and no silent replacement).**
For each changed member, resolve exact `@t0` and `@t1` refs and versions. A changed effective ReferenceScheme changes interpretation-bearing content; an unchanged label or shared designator does not prove continuity. State the exact identity, continuity, split, retirement, or replacement claim and cite the rule that defines or tests it.

**RSCR-F15-E2 (Known confusion check).**
Recheck or explicitly retire every prior confusion, blocked use, and nearest counterexample affected by the change. A new edition does not erase an old trap.

#### F.15:11.2 - Local senses and SchemeSenseCells

**RSCR-F15-E3 (Reconstructible local sense).**
When the basis episteme, source unit, or attestation changes, the `@t1` local-sense claim remains recoverable from exact current basis relations and descriptions. Changed witnesses or source publication do not silently rewrite the sense claim.

**RSCR-F15-E4 (SchemeSenseCell value identity).**
The exact F.17 cell value is `<ReferenceScheme by value, LocalExpression, LocalSenseClaim>`. Changing any component yields another coordinate value; keeping a label or id does not preserve it. Same sense under a renamed expression is handled through designation/lineage rather than cell identity by wish.

#### F.15:11.3 - UnifiedTermRows

**RSCR-F15-E5 (Row episteme identity and edition).**
Compare the exact C.2.1 row epistemes and their ClaimGraphs, EntityOfConcern values, and effective schemes. Changed governed value, NameCard, selected designation, cell, Bridge ref, admitted use, or rationale creates the corresponding later row claim content; an edition id cannot hide it.

**RSCR-F15-E6 (Explicit add, split, merge, or retire).**
When a changed value, sense, or use alters row support, preserve the exact earlier row and state the later add, split, merge, retirement, admitted losses, and receiving use under F.13/F.17. Do not mutate a shared table cell as continuity proof.

#### F.15:11.4 - SystemRoleKindDescriptions and names

**RSCR-F15-E7 (`SystemRoleKindDescription` continuity).**
Compare exact F.4 description epistemes and the described kinds' candidate domains, operative membership conditions, intended member/non-member boundaries, continuity rules, current `KindSignature` editions, effective schemes, and claim content. Source or practice provenance is a cue to compare those definitions, not an identity key. A label-only change cannot prove that the described kind or description episteme stayed the same.

**RSCR-F15-E8 (Alias for expression change; direct recovery for meaning change).**
If only a selected expression changes while the exact value, scheme, sense, and use are preserved, F.13 and F.18 may record an alias or rename. A changed described kind, candidate domain, operative membership distinction, member/non-member boundary, continuity rule, scheme, local sense, or description claim requires the corresponding new object or episteme and a fresh naming settlement. A practice or source change by itself triggers comparison; it proves neither continuity nor a split.

#### F.15:11.5 - Bridges and bounded uses

**RSCR-F15-E9 (Exact Bridge change).**
Compare exact prior/later endpoint cells and relation-semantic profiles. A changed endpoint or profile concerns another Bridge candidate and obtaining test; changed assertion, description, Card, evidence, reliance, or bounded-use claim does not by itself reidentify or negate a fixed obtaining occurrence.

**RSCR-F15-E10 (No drift to equivalence or use authority).**
A later equivalence claim requires an exact Equivalence profile, true predicate, required dependencies, and a separately identified obtaining occurrence. A new witness set, high `CL`, polished Card, or earlier partial relation is insufficient. Any later substitution still needs its own bounded-use claim and reliance.

#### F.15:11.6 - Status and system-role-kind relation structure

**RSCR-F15-E11 (Status-window and status-use stability).**
Compare the exact status family and value definitions, target, scope, window, source condition, and intended use at `@t0` and `@t1`. Changed time, scale, confidence, or edition does not create a new family or preserve an old result automatically.

**RSCR-F15-E12 (System-role-kind relation stability).**
Preserve, retire, or restate each exact incompatibility, monotonic kind order, residual qualification, bundle, requirement, or selected `SystemRoleKindRelationStructure` before using it in a naming, assignment, or Work claim. No later description or fused label substitutes for the relation occurrence.

#### F.15:11.7 - Public naming, publication, and currentness

**RSCR-F15-E13 (Public name continuity).**
F.13/F.18 record the exact selected-expression lineage and NameCard change; F.17 separately records the later row episteme and admitted use. E.24.PUB publication occurrence/form/carrier and G.11 currentness are rechecked only when their exact refs or receiving use changed. A local rename, row edition, or upload does not prove public-name continuity or publication.

