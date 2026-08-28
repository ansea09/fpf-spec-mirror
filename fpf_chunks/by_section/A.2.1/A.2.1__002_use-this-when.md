---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.SystemRoleAssignment - Contextual System-Role Assignment"
section_id: "A.2.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__002_use-this-when.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.2.1 — U.SystemRoleAssignment - Contextual System-Role Assignment"
  - "A.2.1:0 — Use This When"
line_start: 3393
line_end: 3426
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.3.3"
  - "F.6"
  - "F.9"
keywords:
  - "assignment predicate"
  - "direct assignment species"
  - "holder System"
  - "identity"
  - "maximal interval"
  - "performedUnderAssignment"
  - "system-role kind"
---

### A.2.1:0 - Use This When

**Plain name.** Assignment to a system role.

Use this pattern when another claim must rely on one obtaining assignment of an admitted `U.System` under one exact local system-role kind.

Typical moments:

- a MethodDescription names `InspectorSystemRole`, but no current assignment occurrence has been established;
- dated Work must be attributed through `performedUnderAssignment(W, RA)` and the exact assignment `RA` is still missing;
- the same system receives the same system-role kind during two separated episodes;
- two overlapping commissions or positions distinguish two assignments with the same holder and system-role kind;
- an appointment, installation locus, or work commission may be a real additional participant of one domain assignment species;
- a roster, configuration row, observation, decision, or evidence item supports an assignment claim without becoming an assignment participant.

**Primary EntityOfConcern.** One assignment occurrence whose relation species is declared directly under `U.SystemRoleAssignment`. Every species declares a holder participant with `U.System` as its domain, an assigned-kind participant drawn from one exact local system-role-kind domain, its own predicate and applicability, any real additional participant meanings, and its occurrence-identity rule. The occurrence supplies the actual participant values, including its holder System.

**Primary working reader.** An engineer-manager, analyst, Method author, or FPF author who must identify assignment and Work attribution without merging classification, capability, responsibility, authority, Method, Work, evidence, or publication into the assignment.

**First useful move.** Write the ordinary claim first: “Robot-7 is assigned as inspector for Shift-17.” Then identify the declared assignment species, the participant meanings and predicate it declares, and the participant values that satisfy that predicate in this case. Expose an occurrence reference only when another claim must distinguish or cite this episode.

**What goes wrong if missed.** A kind name is mistaken for an assignment, a permissive generic signature accepts arbitrary kinds, two real commissions collapse into one record, or a taxonomy and scheme become world-side participants. Work can then be attributed to the wrong occurrence while capability, authorization, and evidence hide as assignment fields.

**What this buys.** Simple assignments remain simple, stronger assignments retain their real participants, and every occurrence exposes its actual holder through the species-declared holder slot used by F.6. Repeated episodes are distinguishable without manufacturing a second generic assignment beside a stronger one.

**Not this pattern when.**

- Use `A.2` and C.3.2 for the system-role kind and one classification judgment.
- Use `A.2.2` for capability, `A.2.5` for assignment state, and `A.2.7` for relations among system-role kinds.
- Use `A.3`, `A.15`, and `A.15.1` for Method, MethodDescription, Work, and enactment.
- Use `F.6` for performed-Work attribution through an already identified assignment.
- Use the direct responsibility, commitment, permission, authority, access, decision, evidence, reliance, provenance, publication, external-rule, or currentness pattern when that relation is current.
- Use `E.10.ROLE` when the source word *role* has not yet been resolved; use `A.6.RSIR` when it means relation participation or a declaration place.

