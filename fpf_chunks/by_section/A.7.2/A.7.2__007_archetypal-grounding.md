---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__007_archetypal-grounding.md"
commit_sha: "0c6ade275e9360f0c5ab9715d8f05c0dbaa13cf8"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:5 — Archetypal Grounding"
line_start: 23983
line_end: 23992
dependencies:
  - "A.10"
  - "A.7.1"
  - "A.7.2"
  - "A.7.CP"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
keywords:
  - "actual source-use relations"
  - "context split"
  - "dated FPF applications"
  - "exact used clauses and premises"
  - "optional convergence"
  - "result claims or decisions"
  - "same receiving claim or consequence"
---

### A.7.2:5 - Archetypal Grounding

**Compatible repair.** The receiving claim asks whether a `MaintenanceCoordinatorAssignment` obtains for holder `MaintenanceSystem-4` and assigned kind `MaintenanceCoordinatorKind` in scope `S`. Its independently admitted local rule requires a policy-valid assignment act and treats the signed organization chart as evidence only. The chart is present, but current facts establish that the required act did not occur. One dated application of the local rule concludes that the relation does not obtain; another application of a chart-sufficiency clause concludes that it obtains for the same participants and scope. Reconciliation Work recovers both result claims, their method clauses, source uses, and reasoning-basis uses of `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. It repairs the assignment clause to apply the local obtaining rule and use the chart as evidence for an assertion. Replaying both applications now yields the supported non-obtaining conclusion, without inventing an assignment occurrence. The result is `reconciledCompatibility` for that claim and scope.

If the evidence does not establish whether the required act occurred, reliance on the obtaining claim remains unresolved. Under a different independently admitted rule, authorized signing may itself be the required act; establish that actual act instead of applying this case's evidential-only rule. A separate policy-valid act may create `MaintenanceCommitment-17`, borne by `MaintenanceSystem-4`; neither this commitment nor the assignment claim by itself establishes responsibility. Test any responsibility claim separately against its admitted maintenance-responsibility predicate, actual participants, applicability, and identity; if that governor is missing, return the exact missing governor.

**Context split.** One dated application uses a pattern's `ComponentOf` clause for a pump assembly; another applies a maintenance-set pattern's belongs-to rule to a candidate item. Both result claims say “part”, but their subjects, receiving claims, constructions, and consequences differ. The result is `contextSplit`; neither source clause nor application result defeats the other.

**Non-convergence.** Two dated method applications yield incompatible same-scope dependence claims, but available evidence and formal consequences warrant neither correction. The result is `doNotCompose` for the affected assurance use or `unresolvedEscalation` with exact result claims, missing evidence basis or decision predicate and source, and reopen condition. Familiarity or institutional status cannot manufacture convergence.

