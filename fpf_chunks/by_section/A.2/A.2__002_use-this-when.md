---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__002_use-this-when.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:0 — Use This When"
line_start: 2697
line_end: 2730
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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

**Plain name.** Enactment-facing role value.

Use this pattern when the same admitted `U.System` can participate in different work, transformation, functioning, or method enactments without becoming a different system kind, and a project must state what that system is being in the current participation.

Typical moments:

- the same pump is a cooling circulator in plant operation and a test article in qualification work;
- a relied-on claim names a role but omits the role vocabulary, interpretation scheme, holder, or assignment window;
- ordinary wording says that an episteme, capability, method, or value filling a relation participant slot "plays a role", while the direct FPF relation is still hidden;
- a proposed "part of a role" may instead be a separate role value, role relation, role-state predicate, capability-fit condition, responsibility, commitment, or method or work structure.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Role`: an enactment-facing role value interpreted through one named role-taxonomy episteme and its effective `U.ReferenceScheme`. It says what an admitted `U.System` holder is being for a current participation claim. `U.Role` is a root U-kind but not an admitted holon kind; proposed decompositions are dispatched to the direct patterns governing the recovered objects and relations.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who must keep system identity stable while making role meaning and role assignment inspectable. A later reader must be able to recover the role vocabulary and scheme, the holder, the assignment window, and the separate work or method claim that relied on the assignment.

**First useful move.** Name the role value, the role-taxonomy episteme, and its effective reference scheme. Add `U.RoleAssignment` when holder or assignment-window identity matters. Then state capability, role state, method admission, performed work, responsibility, evidence, or episteme use through its direct governing pattern.

**Concern-word boundary.** *Concern* is Plain reader- or viewpoint-facing wording; it does not admit `U.Concern` or replace the exact EntityOfConcern, viewpoint episteme, role-taxonomy interpretation, assignment, or receiving relation needed by the claim.

**What goes wrong if missed.** One system's different participations become artificial system kinds, or one role label silently absorbs the holder, local meaning, assignment window, capability, method, and work claim. At the opposite extreme, every contribution is called a role even when no system holds one. Both failures make it impossible to tell who participated, under which interpretation, and what actually happened.

**What this buys.** A small role vocabulary can be reused without type explosion or a universal context object. The same system may hold several roles through distinct assignments; identical labels under different role taxonomies or reference schemes do not establish identical role meanings; epistemes remain participants in their own use and evidence relations rather than becoming role holders.

**Not this pattern when.**

- Use `A.2.1` when the current object is the assignment relation and its occurrence identity.
- Use `A.2.2` for a holder's capability and `A.2.5` for a current role state.
- Use `A.2.7` for selected substitution, incompatibility, qualification, or bundle relations among role values.
- Use `A.15` and its method and work neighbors for method admission, planned work, and performed work.
- When the current participant is an episteme rather than a system holder, recover the direct use, evidence, publication, external-rule, currentness, or reliance relation. `C.2.1`, `A.10`, `E.17`, `F.10`, and `A.15.4` are common exits.
- If only the word `role` is unclear, use `A.6.RSIR` until the governed object or relation is recovered.

