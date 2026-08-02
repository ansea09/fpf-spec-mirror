---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__002_use-this-when.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:0 — Use This When"
line_start: 2664
line_end: 2698
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

Use this pattern when a project needs to say what an admitted `U.System` holder, such as a system, organization-as-system, person, team, tool, agent, machine, motor, pump, or component, is being in a bounded context before method, plan, work, transformation, functioning, evidence, responsibility, or naming claims can be made safely.

Typical moments:

- a project sentence says "engineer", "reviewer", "operator", "supplier", "model verifier", "agent", "service provider", "drive motor", "cooling circulator", "load-bearing brace", or another role-like name, and it is unclear what holder, context, and work, transformation, or functioning claim are current;
- a team treats a role name as if it created capability, commitment, obligation, permission, method, work, or evidence;
- a standard, report, dataset, model card, publication, requirement, or definition is described as having a "role" in evidence, status, assurance, source use, or publication use;
- a method, plan, work occurrence, or result is attributed to a role without naming the holder and role assignment under which the work is performed;
- role names must be kept reusable across contexts without making each context-local role into a new system kind;
- a role boundary is being decomposed into factors, states, responsibilities, or method participation, and the project must recover the current neighboring object instead of treating role as a holon.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Role`: a context-bound enactment-facing role value in the role `ontologicalNeighborhood`. A role value names what an admitted `U.System` holder is being for a bounded context when method admission, role-state checking, transformation or functioning participation, or work attribution depends on that role. `U.Role` is a root U-kind, but it is not an admitted holon kind: role decompositions resolve to assignment, state, capability, responsibility, permission, commitment, obligation, method, work, or role-relation owners rather than to role parts.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who must separate role value, holder, role assignment, method, plan, work, evidence, and source-use claims before acting or writing a pattern. The downstream reader is the project participant who needs role language to answer who held what role, in which context, for which claim.

**First useful move.** Name the role value, the bounded context, and whether the current claim is about role identity, a role assignment, role description, role state, role relation structure, capability-fit condition, functional or transformation participation, method role-admission condition, planned work, performed work, or an episteme used as evidence, source, standard, requirement, definition, explanation, status bearer, or publication.

**What goes wrong if missed.** Role words become an ontology shortcut. A document becomes a "verifier role"; a capability becomes a role; a role name is treated as evidence that work happened; a method is treated as a role's hidden behavior; a publication is treated as if it acted. FPF then grows a second role ontology for epistemes, status labels, access labels, relation arguments, and source labels.

**What this buys.** A small role vocabulary can serve many projects without type explosion. The same system can hold different roles in different contexts; work remains performed by a holder under a role assignment; epistemes remain used through their own evidence, status, source, publication, requirement, definition, explanation, and assurance relations.

**Not this pattern when.**

- If the current claim is the assignment relation linking holder, role, context, and window, use `A.2.1`.
- If the current claim is capability, use `A.2.2`.
- If the current claim is role state, use `A.2.5`.
- If the current claim is role-admission substitution, incompatibility, qualification, or bundles, use `A.2.7`.
- If the current claim is method, method description, work plan, or performed work alignment, use `A.15`.
- If the current claim is an episteme used as evidence, source, standard, definition, requirement, explanation, status bearer, publication, or assurance input, use the direct evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, or assurance pattern. Do not force it through `U.Role`.
- If the current issue is only a confusing role-like word, first use `A.6.RSIR` to recover the governed object or claim kind.

