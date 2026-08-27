---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__002_use-this-when.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:0 — Use This When"
line_start: 92430
line_end: 92456
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
  - "A.3"
  - "A.6.9"
  - "A.6.REL"
  - "C.3.3"
  - "E.10.ROLE"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
keywords:
  - "Work attribution"
  - "exact assignment occurrence"
  - "holder equality"
  - "performedUnderAssignment"
  - "performer System"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:0 - Use This When

**Plain name.** Check who performed this Work under which system-role assignment.

Use this pattern when deciding whether a dated `U.Work` occurrence was performed under a particular assignment occurrence from the `U.SystemRoleAssignment` family. When it was, the direct world-side performed-under-assignment relation obtains. A separate assertion or record can identify the two occurrences and state that relation.

Typical moments:

- a work record says “Alice reviewed”, “Robot-7 inspected”, or “the operations team approved”, but the assignment occurrence is missing;
- a MethodDescription names a system-role kind and the project must connect actual Work to the assigned performer;
- source wording says `RoleEnactment`, “played the role”, or `Holder#Role:Context@Window`;
- a stronger appointment has a commission, position, or locus participant and must retain that occurrence identity during attribution;
- a report, standard, dashboard, or access label is described with role wording although it did not perform Work;
- a corresponding kind or assignment from another context is cited without a current Bridge and local occurrence.

**Primary EntityOfConcern.** One obtaining `performedUnderAssignment` relation occurrence between a `U.Work` occurrence and an assignment occurrence whose species is declared under `U.SystemRoleAssignment`.

**Primary working reader.** An engineer, operator, Method author, manager, or FPF author deciding whether a performed-Work attribution is grounded strongly enough for the next use.

**First useful move.** Name the Work and the assignment occurrence under which it is said to have been performed. Recover the occurrence's declared species and participant values, then ask what case fact links this Work to this assignment. Confirm that its holder is the performer and that it covers the Work interval; those checks alone do not create the link. If the case does not establish the pair, leave the attribution unresolved. Otherwise say plainly that the holder System performed the Work under that assignment.

**What goes wrong if missed.** Assignment is treated as proof of Work, a label replaces the assignment occurrence, a generic assignment duplicate erases a stronger appointment, or a log or report is made the performer. When several assignments overlap, interval coverage then attributes the same Work to all of them even though the exact pair was never established.

**What this buys.** Attribution is one thin relation. The holder System remains the actor, the assignment occurrence remains linked to its species and participant values, and Work, Method, capability, state, result, evidence, publication, and cross-context use remain separate.

**Not this pattern when.** Use `A.2` for the system-role kind and classification, `A.2.1` for assignment species and occurrence identity, `A.2.5` for assignment state, `A.2.2` for capability, and `A.15.1` for the Work occurrence. Use the direct evidence, source-reliance, publication, access, authority, permission, responsibility, status, gate, or decision pattern when that relation is current. Use `E.10.ROLE` and `A.6.RSIR` when *role* denotes another object or relation position.

