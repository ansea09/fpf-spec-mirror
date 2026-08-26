---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__002_use-this-when.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:0 — Use This When"
line_start: 22532
line_end: 22558
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.2.7"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
keywords:
---

### A.12:0 - Use This When

Use this pattern when a source says that something changes, repairs, configures, updates, verifies, teaches, controls, or improves itself, or when the acting side of a change is hidden behind a passive or self-action sentence.

Typical moments:

- "the robot calibrates itself";
- "the model updates itself";
- "the document refreshes its own cross-references";
- "the organization corrected itself";
- "the system verifies that its own change succeeded";
- "the lathe makes the workpiece, therefore the workpiece is part of the lathe during manufacturing".

**First useful move.** Separate the exact continuing subject named as changed from the exact entity proposed for the acting side. Identify the changed subject by the identity rule that defines that referent. Before calling the acting-side entity a `U.System`, show that it satisfies the complete A.1 criterion; otherwise retain the exact `U.Entity` and its `recognized | rejected | unknown` disposition or exact blocker and leave the acting-system position empty. After recognition, name that `U.System` and recover its exact acting-side participation relation. Add an obtaining occurrence of one directly declared `U.SystemRoleAssignment` species under `A.2.1` only when the work-facing claim uses it; use `A.2.7` separately only for a relation among exact local system-role kinds. If an actual bounded change is current, use A.3.4's change test for that same continuing subject; use `A.15` and `A.15.1` for Method and Work, `F.6` for Work attribution, `A.10` for evidence, and `A.1`, `A.14`, or `C.13` for holon and part-whole claims.

**What goes wrong if missed.** A system becomes its own cause, a document acts, a controller and controlled part collapse into one object, evidence becomes self-certifying, and a system that changes another holon is mistaken for the larger whole containing it without an obtaining part-whole relation.

**What this buys.** Self-action wording becomes a reviewable relation among one exact continuing changed subject, the exact entity proposed for the acting side, its same-entity `U.System` reading only after A.1 recognition, and any separately governed participation, role, method, Work, boundary-crossing, or evidence claims that are current. Reflexive use remains the narrower holon case with two exact parts or subsystems.

**Not this pattern when.**

- If the current question is whether a bounded change occurred, use `A.3.4`.
- If the current question is whether work was performed or succeeded, use `A.15` and `A.15.1`.
- If the current question is an assignment occurrence, use `A.2.1`; if it is a relation among exact local system-role kinds, use `A.2.7`. For another participation relation, use the pattern that defines that relation.
- If the current question is evidence independence or source use, use `A.10` and the evidence-use or source-use patterns.
- If the current question is part-whole admission, use `A.1`, `A.14`, and `C.13`.

