---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__011_conformance-checklist.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:9 — Conformance Checklist"
line_start: 91482
line_end: 91495
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:9 - Conformance Checklist

1. `WorkOccurrenceSlot` names one admitted dated `U.Work` occurrence.
2. `RoleAssignmentSlot` names one obtaining `U.RoleAssignment` occurrence.
3. The assignment exposes holder system, role value, role-taxonomy episteme, and effective reference scheme as participants; its maximal continuous assignment extent is checked separately.
4. The assignment holder is the system claimed to have performed the work.
5. The assignment episode covers the selected work occurrence's interval; attribution to only one part first selects that part as `U.Work`.
6. The attribution uses direct `performedUnderAssignment` wording and introduces no `RoleEnactmentFact`.
7. Role state, capability, method, result, evidence, source reliance, publication, gate, and decision claims use their direct patterns.
8. Any selected model-use structure is designated by the receiving attribution assertion or use, not by an optional slot in generic `U.RoleAssignment`.
9. Missing evidence leaves the relied-on assertion unresolved rather than proving non-attribution.
10. Compact source notation is unfolded before a receiving use depends on hidden assignment positions.
11. The work assertion makes a separately obtaining actual `enactsMethod(W, M)` relation to one exact `U.Method` recoverable; it does not make the role value, assignment, capability, method, or method description the actor, and it does not infer `U.MethodDescription` membership from a label or algorithm-possession phrase.

