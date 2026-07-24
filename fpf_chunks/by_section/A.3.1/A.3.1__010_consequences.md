---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__010_consequences.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:9 — Consequences"
line_start: 7045
line_end: 7066
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.22"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.REL"
  - "B.1.5"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.20"
  - "C.29"
  - "C.36"
  - "C.36.P"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
---

### A.3.1:9 - Consequences

* Method-like language becomes reusable across physical, informational, organizational, and mathematical work without privileging software code or ordered instructions.
* Teams can compare descriptions, variants, and implementations without confusing them with dated work.
* Work planning and evidence become more reliable because a method no longer smuggles in authority, proof, schedule, or performed-work claims.
* The cost is explicit recovery of the governed object and claim position: reliance on wording such as "method", "practice", "algorithm", "workflow", "process", "procedure", "program", "recipe", "proof", or "solver" begins only after the current FPF object or claim is recovered.

#### A.3.1:9.1 - Lowering and local repair conditions

Lower or withdraw the current `U.Method` identification when:

* the text cannot state transformation or enactment kind, `A.3.4 transformedEntityOrStructure`, preconditions, and intended effects;
* the method name is only a document, repository, diagram, model, run log, team name, supplier label, or authorization claim;
* the same typed value is assigned as both `U.Method` and `U.Mechanism` without a governing pattern admitting the dual typing;
* source wording such as `practice` has not been recovered to one current claim position before method reliance begins;
* graph, path, query, table, or predicate wording is treated as ordered execution without `C.2.P.DR` recovery;
* a later `U.MethodDescription`, `U.WorkPlan`, Work occurrence admitted under `U.Work`, `U.Mechanism`, `C.29`, `E.18`, or evidence pattern changes an exact relation or semantic condition on which the method statement relied.

If the semantic way of doing cannot be recovered, withdraw the `U.Method` typing and keep the wording as an unresolved cue. If a neighboring description, plan, work, mechanism, representation, or evidence value has taken the method position, split that value into its direct governing relation. If only one relied-on identity-basis relation changed, review that relation and the affected method identity rather than invalidating every use of the method.

The smallest useful repair is usually local: revise the method identification, split the neighboring value into its governing pattern, or add one `ClaimBoundary` line. A new method-description edition repairs the description relation unless it changes a relied-on method-identity field. A changed work fact repairs the work claim; a changed measurement, evaluation, production, delivery, acceptance, or evidence result repairs that separately governed claim. Neither changes the method unless it changes the accepted participant meanings, preconditions, intended effects, bounds, or transformed-entity relation on which method identity depends. Return to `G.5` or the direct method-family pattern only when repeated project material shows that the current family or selector relation no longer separates methods, descriptions, plans, work, mechanisms, or neighboring claims adequately. A verbose or poorly ordered explanation is a didactic defect to repair in the description; it does not by itself lower the identified method.

