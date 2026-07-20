---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__004_problem.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:2 — Problem"
line_start: 2410
line_end: 2421
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:2 - Problem

Without this pattern:

1. **Role labels do not identify performers.** Work records name a role-like word, but not the holder and context needed for attribution.
2. **Assignment and role collapse.** The role value, the holder, the bounded context, and the assignment window become one label.
3. **Assignment and capability collapse.** A role assignment is treated as evidence of ability, even though capability has its own envelope and evidence.
4. **Assignment and method collapse.** Holding a role is treated as if the holder automatically has a method or has already performed work.
5. **Episteme-role drift returns.** Standards, reports, datasets, definitions, requirements, and model cards are described as role holders instead of being related through evidence, status, source, publication, requirement, or assurance relations.
6. **RoleEnactment becomes a second run-time object.** A derived performed-by fact is mistaken for a durable U-kind beside `U.Work`.
7. **Slot discipline is lost.** Holder, role value, context, window, justification, provenance, and qualifier positions are not recoverable as distinct SlotKinds.

