---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__002_use-this-when.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:0 — Use This When"
line_start: 2285
line_end: 2318
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

### A.2.1:0 - Use This When

**Plain name.** Work-role assignment.

Use this pattern when a project must say which system, organization, person, team, service, agent, device, or other acting holon holds which `U.Role` in which bounded context, and when that assignment is current enough to admit, check, plan, or attribute work.

Typical moments:

- a work record says that "Alice reviewed", "Robot-7 inspected", "CI bot deployed", or "the operations team approved" and the role, holder, bounded context, or assignment window is missing;
- a method or method description names required roles, but the project has not linked those roles to concrete performers;
- a role state, capability requirement, separation-of-duties rule, or work gate depends on who holds the role now;
- a source phrase gives an episteme an "evidence role", "standard role", "status role", or "requirement role" and the text must be normalized without making epistemes into work performers;
- a local notation such as `Holder#Role:Context@Window` is useful, but the notation must not replace the typed relation it abbreviates.

**Primary EntityOfConcern.** The EntityOfConcern is `U.RoleAssignment`: a typed work-facing assignment relation value. It links an admitted acting holder, a `U.Role`, a `U.BoundedContext`, and any assignment-currentness window or assignment source that is current for the claim.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who needs work attribution, role admission, role-state checks, method requirements, or responsibility language to remain inspectable across contexts and editions.

**First useful move.** Recover the four core slots of the assignment relation: holder, role value, bounded context, and assignment window when current. Then recover any direct work-role qualifier, role-state admission, capability requirement, method requirement, work-plan relation, or work occurrence through its governing pattern.

**What goes wrong if missed.** Role labels float without holders or contexts. A method appears to have been enacted by a document. A work record names a person but not the role under which the work was admitted. A report or standard is treated as if it held a role because it is used as evidence or requirement source. The corpus then grows one role ontology for work and a second role ontology for epistemes.

**What this buys.** `U.RoleAssignment` gives one narrow relation for work-facing role holding. It keeps role values reusable, work attribution replayable, method requirements checkable, and episteme evidence or status uses outside the role-assignment relation.

**Not this pattern when.**

- If the current claim is the role value itself, role taxonomy, or role relation-neighborhood, use `A.2`.
- If the current claim is ability or operating envelope, use `A.2.2`.
- If the current claim is role state, role-state predicate, or enactable-state admission, use `A.2.5`.
- If the current claim is role-requirement substitution, incompatibility, qualification, or role bundle, use `A.2.7`.
- If the current claim is method, method description, work plan, performed work, or role-method-work alignment, use `A.15` and the direct A.15 subpattern.
- If the current claim is evidence, source, standard, requirement, definition, explanation, publication, status, assurance, gate, or decision use of an episteme, use the direct pattern for that relation. Do not make the episteme a `U.RoleAssignment` holder.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.

