---
chunk_kind: "child"
pattern_id: "E.10.ROLE"
pattern_title: "Recovering What “Role” Means in the Current Claim"
section_id: "E.10.ROLE:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ROLE/E.10.ROLE__002_use-this-when.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "E.10.ROLE — Recovering What “Role” Means in the Current Claim"
  - "E.10.ROLE:0 — Use This When"
line_start: 77312
line_end: 77332
dependencies:
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.19"
keywords:
  - "ambiguous role wording"
  - "assignment"
  - "declaration slot"
  - "interface place"
  - "ordinary wording"
  - "relation participant"
  - "representation position"
  - "responsibility"
  - "system-role kind"
---

### E.10.ROLE:0 - Use This When

Use this pattern when claim-bearing wording uses *role* and the current sentence does not yet reveal which object or relation it means.

> A **system role** is a context-local kind for an entity already admitted under A.1 as a `U.System`, which may be a person, team, organization, or non-human technical object. The name creates no admission, assignment, agency, capability, or Work.

A **system-role assignment** is one exact occurrence under `U.SystemRoleAssignment`. The bare word *role* identifies neither object.

**First useful result.** Rewrite the ordinary domain sentence so that its recognizable object and action or relation are explicit. Select the pattern for that object or relation. Stop there unless the receiving claim needs a technical designation, exact occurrence, predicate, assertion, or reference.

For example:

- “Alice is reviewer” may remain ordinary recognition prose;
- “Alice holds the review assignment for this manuscript” makes an assignment claim current;
- “the report plays a role in approval” normally needs an evidence-use, source-use, reliance, or other direct relation, not a system-role assignment;
- “the first role in this tuple” normally points to a representation position, not a system-role kind.

**Not this pattern when.** Keep ordinary or quoted wording unchanged when no FPF claim relies on the word. When the object and its direct pattern are already clear, use that pattern directly. Use `A.6.RSIR` when the unresolved question is specifically about participation in a direct relation, a relation declaration, an interface, or a representation position.

`ROLE` remains in this PatternID because it is the ambiguous source word that opens this recovery. It is not a Tech designation for one governed object and is not a naming precedent.

