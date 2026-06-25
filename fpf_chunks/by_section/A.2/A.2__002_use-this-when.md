---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__002_use-this-when.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:0 — Use This When"
line_start: 1924
line_end: 1957
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:0 - Use This When

**Plain name.** Work-facing role value.

Use this pattern when a project needs to say what a system, organization, person, team, tool, agent, machine, or other acting holon is being in a bounded context before method, plan, work, evidence, responsibility, or naming claims can be made safely.

Typical moments:

- a project sentence says "engineer", "reviewer", "operator", "supplier", "model verifier", "agent", "service provider", or another role-like name, and it is unclear what holder, context, and work claim are current;
- a team treats a role name as if it created capability, commitment, obligation, permission, method, work, or evidence;
- a standard, report, dataset, model card, publication, requirement, or definition is described as having a "role" in evidence, status, assurance, source use, or publication use;
- a method, plan, work occurrence, or result is attributed to a role without naming the holder and role assignment under which the work is performed;
- role names must be kept reusable across contexts without making each context-local role into a new system kind.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Role`: a context-bound role value in the role `ontologicalNeighborhood`. A role value names what an acting system or acting holon is being for a bounded context. It is not the holder, not the assignment relation, not a capability, not a method, not a work occurrence, not a commitment, not an obligation, not a permission, not a description, and not a slot kind.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who must separate role value, holder, role assignment, method, plan, work, evidence, and source-use claims before acting or writing a pattern. The downstream reader is the project participant who needs role language to answer who held what role, in which context, for which claim.

**First useful move.** Name the role value, the bounded context, and whether the current claim is about role identity, a role assignment, role description, role state, role relation structure, capability requirement, method requirement, planned work, performed work, or an episteme used as evidence, source, standard, requirement, definition, explanation, status bearer, or publication.

**What goes wrong if missed.** Role words become an ontology shortcut. A document becomes a "verifier role"; a capability becomes a role; a role name is treated as evidence that work happened; a method is treated as a role's hidden behavior; a publication is treated as if it acted. FPF then grows a second role ontology for epistemes, status labels, access labels, relation arguments, and source labels.

**What this buys.** A small role vocabulary can serve many projects without type explosion. The same system can hold different roles in different contexts; work remains performed by a holder under a role assignment; epistemes remain used through their own evidence, status, source, publication, requirement, definition, explanation, and assurance relations.

**Not this pattern when.**

- If the current claim is the assignment relation linking holder, role, context, and window, use `A.2.1`.
- If the current claim is capability, use `A.2.2`.
- If the current claim is role state, use `A.2.5`.
- If the current claim is role-requirement substitution, incompatibility, qualification, or bundles, use `A.2.7`.
- If the current claim is method, method description, work plan, or performed work alignment, use `A.15`.
- If the current claim is an episteme used as evidence, source, standard, definition, requirement, explanation, status bearer, publication, or assurance input, use the direct evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, or assurance pattern. Do not force it through `U.Role`.
- If the current issue is only a confusing role-like word, first use `A.6.RSIR` to recover the governed object or claim kind.

