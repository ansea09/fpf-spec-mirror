---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__010_consequences.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:9 — Consequences"
line_start: 6386
line_end: 6405
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:9 - Consequences

* Method-like language becomes reusable across physical, informational, organizational, and mathematical work without privileging software code or ordered instructions.
* Teams can compare descriptions, variants, and implementations without confusing them with dated work.
* Work planning and evidence become more reliable because a method no longer smuggles in authority, proof, schedule, or performed-work claims.
* The cost is explicit slot recovery: when wording says "method", "algorithm", "workflow", "process", "procedure", "program", "recipe", "proof", or "solver", the user must recover which FPF object or claim position is current before relying on it.

#### A.3.1:9.1 - Lowering and refresh conditions

Lower confidence in a `U.Method` use when:

* the text cannot state transformation or enactment kind, `EntityOfConcern`, preconditions, and intended effects;
* the method name is only a document, repository, diagram, model, run log, team name, supplier label, or authorization claim;
* the same typed value is assigned as both `U.Method` and `U.Mechanism` without a governing pattern admitting the dual typing;
* the first usable move requires a long related-pattern catalogue before the method slot is visible;
* graph, path, query, table, or predicate wording is treated as ordered execution without `C.2.P.DR` recovery;
* a later `U.MethodDescription`, `U.WorkPlan`, `U.Work`, `U.Mechanism`, `C.29`, `E.18`, or evidence pattern changes the slot relation on which the method statement relied.

The smallest useful repair is usually local: rewrite the method statement, split the neighboring value into its governing pattern, or add one `ClaimBoundary` line. Reopen the wider method family only when repeated project material shows that `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, `U.Mechanism`, formal substrate, or mathematical-lens use can no longer be separated by the current slot rules.

