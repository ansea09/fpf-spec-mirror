---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "System-Role Kinds and Assignments"
section_id: "A.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__002_use-this-when.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "A.2 — System-Role Kinds and Assignments"
  - "A.2:0 — Use This When"
line_start: 2656
line_end: 2696
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10.ROLE"
  - "F.4-F.6"
keywords:
  - "U.SystemRoleAssignment"
  - "ambiguous role wording"
  - "assignment"
  - "holder System"
  - "local System classification"
  - "system-role kind"
  - "work-facing contribution"
---

### A.2:0 - Use This When

**Plain name.** Work-facing system classification and assignment.

Use this pattern when one admitted `U.System` can contribute to different work or functioning without becoming a different system, and the current claim must say either:

- which exact work-facing kind the system counts under now; or
- which system-role assignment actually obtains.

A system here is any individual independently admitted by A.1. It can be a person, team, organization, service, organism, or non-human technical object. The `SystemRole` head in a name such as `ReviewerSystemRole` says that candidates are systems; it does not admit the candidate, create an assignment, imply agency or capability, prove that Work occurred, or name a relation slot.

Typical moments:

- the same pump counts as a cooling circulator in plant operation and as a test article in qualification work;
- a project must decide whether Alice counts as a reviewer in one review slice;
- a relied-on claim says that a system holds a named system role but leaves the assignment occurrence unclear;
- ordinary wording says that a publication, method, capability, or relation participant “plays a role”, although the direct relation is still hidden;
- a proposed “part of a role” may instead be another kind, a relation among kinds, an assignment-state predicate, a capability condition, a responsibility or commitment relation, or a method or Work structure.

**Primary EntityOfConcern.** One exact local `U.Kind` whose candidates are `U.System` individuals and whose operative membership condition distinguishes a stable, assignable, work-facing contribution. C.3 recovers the kind through that candidate domain and condition, a useful member/non-member boundary, and a continuity rule. A practice or source reference may locate the definition or prompt comparison; it does not identify the kind. Such a kind is called a **system-role kind**. Assignment is a neighboring direct relation, not part of the kind.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who must keep system identity stable while making classification and assignment inspectable. A later reader must be able to recover the kind's candidate domain, work-facing membership condition, member/non-member boundary, continuity rule, declaration edition, candidate and slice, useful definition provenance, and any separately obtaining assignment and Work attribution.

**First useful move.** Start with the ordinary conclusion: “Alice counts as a reviewer for this submission” or “PumpUnit-3 is assigned as cooling circulator for this operating episode.” For classification, name the local system-role kind and evaluate the candidate with one `KindSignature` under C.3.2. Add a `U.SystemRoleAssignment` occurrence only when holding or assignment identity is actually claimed.

**Concern-word boundary.** *Concern* is Plain reader- or viewpoint-facing wording. It does not admit `U.Concern` or replace the exact EntityOfConcern, viewpoint episteme, kind, assignment, or receiving relation needed by the claim.

**What goes wrong if missed.** One label absorbs kind identity, classification, holder, assignment, capability, responsibility, and Work. Or every contribution is forced into a system role even when the real claim concerns evidence use, a relation participant, a declaration slot, or ordinary wording. In both cases readers cannot tell what exists, what merely describes it, and what actually happened.

**What this buys.** Systems retain their identities while work-facing classifications and assignments change. Membership is testable from the system features named by the membership rule rather than labels or circular hierarchy edges. Practices and sources may reuse one kind or define different kinds; comparing their exact distinctions decides which. Ordinary contribution wording can stay readable without manufacturing an ontology.

**Not this pattern when.**

- Use `A.2.1` when the current object is a `U.SystemRoleAssignment` species or occurrence and its participant, predicate, or identity law matters.
- Use `A.2.2` for capability and `A.2.5` for assignment state.
- Use `A.2.7` for substitution, incompatibility, bundle, qualification, or another admitted relation among system-role kinds.
- Use `A.15` and its neighbors for method admission, planned Work, performed Work, and Work attribution.
- Use `E.24.UK` when a local system-role kind is proposed as a durable public FPF U-kind.
- Use `E.10.ROLE` when the source word *role* is ambiguous. If the recovered meaning is relation participation, a declaration place, an interface place, or a representation position, continue with `A.6.RSIR`.
- When an episteme rather than a system is current, recover its direct use, evidence, publication, external-rule, currentness, or reliance relation through the relevant subject pattern.

