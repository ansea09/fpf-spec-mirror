---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__007_archetypal-grounding.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:5 — Archetypal Grounding"
line_start: 22106
line_end: 22113
dependencies:
  - "A.10"
  - "A.7.1"
  - "A.7.2"
  - "A.7.CP"
  - "C.2.1"
  - "C.29"
  - "E.17"
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

**Compatible repair.** One dated method application yields a claim that a policy-valid instituting act creates `MaintenanceCommitment-17`, an exact `U.Commitment` whose actual bearer is `MaintenanceSystem-4`; it does not thereby establish responsibility. Another application yields a claim that a signed organization chart is sufficient to make `MaintenanceAssignment-17 : MaintenanceCoordinatorAssignment` obtain. Reconciliation Work recovers both result claims, their method clauses, source uses, and reasoning-basis uses of `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. It repairs the assignment clause so the chart is evidence for an assignment assertion rather than constitution of the assignment. If responsibility is also claimed, it is tested independently under an admitted maintenance-responsibility predicate with actual participants, applicability, and identity; otherwise the exact missing governor is returned. The result is `reconciledCompatibility`: commitment, assignment, responsibility, performing system, and Work no longer substitute for one another, while unrelated evidence and publication law stays unchanged.

**Context split.** One dated application uses a pattern's `ComponentOf` clause for a pump assembly; another applies a maintenance-set pattern's belongs-to rule to a candidate item. Both result claims say “part”, but their subjects, receiving claims, constructions, and consequences differ. The result is `contextSplit`; neither source clause nor application result defeats the other.

**Non-convergence.** Two dated method applications yield incompatible same-scope dependence claims, but available evidence and formal consequences warrant neither correction. The result is `doNotCompose` for the affected assurance use or `unresolvedEscalation` with exact result claims, missing evidence basis or decision predicate and source, and reopen condition. Familiarity or institutional status cannot manufacture convergence.

