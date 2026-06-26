---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__002_use-this-when.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:0 — Use This When"
line_start: 20186
line_end: 20212
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.7"
  - "A.3.4"
  - "B.2"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "C.30"
  - "E.17"
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

**First useful move.** Separate the changed holon from the acting system or candidate acting system. Then use the direct owner for the current claim: `A.3.4` for bounded transformation, `A.15` and `A.15.1` for method and work, `A.2.1` and `A.2.7` for role assignment and role relations, `A.10` for evidence, and `A.1`, `A.14`, or `C.13` for holon and part-whole claims.

**What goes wrong if missed.** A system becomes its own cause, a document acts, a controller and controlled part collapse into one object, evidence becomes self-certifying, and a system that changes another holon is mistaken for that holon's super-holon.

**What this buys.** Self-action wording becomes a reviewable relation among a changed holon, an acting system in role, method or work claims when current, boundary-crossing relation when current, and evidence when current.

**Not this pattern when.**

- If the current question is whether a bounded change occurred, use `A.3.4`.
- If the current question is whether work was performed or succeeded, use `A.15` and `A.15.1`.
- If the current question is the role assignment or role relation, use `A.2.1` and `A.2.7`.
- If the current question is evidence independence or source use, use `A.10` and the evidence or source-use owners.
- If the current question is part-whole admission, use `A.1`, `A.14`, and `C.13`.

