---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__002_use-this-when.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:0 — Use This When"
line_start: 23839
line_end: 23865
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

Use this pattern when self-action or passive wording hides the acting participant or the subject claimed to change, or when interaction is mistaken for parthood.

Typical moments:

- "the robot calibrates itself";
- "the model updates itself";
- "the document refreshes its own cross-references";
- "the organization corrected itself";
- "the system verifies that its own change succeeded";
- "the lathe makes the workpiece, therefore the workpiece is part of the lathe during manufacturing".

**First useful move.** Name the proposed acting participant and the subject claimed to change, then state the relation between them that matters to your question. For the robot below, the calibration controller acts on the sensor suite. Use the precise account in §4.1 when you need to distinguish their identities or establish a particular System, change, Work or evidence claim; the ordinary acting-side distinction does not require constructing that frame.

**What goes wrong if missed.** A controller and controlled part can collapse into one object, an automated publication update can hide its performer, and the performer’s output can be mistaken for sufficient evidence of success. Changing another holon can also be mistaken for containing it.

**What this buys.** You can locate the acting participant, trace the claimed change, and ask separately what establishes the change or its success. When both participants are distinct parts of one holon, Reflexive Split exposes their internal relation.

**Not this pattern when.**

- If the current question is whether a bounded change occurred, use `A.3.4`.
- If the current question is whether work was performed or succeeded, use `A.15` and `A.15.1`.
- If the current question is an assignment occurrence, use `A.2.1`; if it is a relation among exact local system-role kinds, use `A.2.7`. For another participation relation, use the pattern that defines that relation.
- If the current question is evidence independence or source use, use `A.10` and the evidence-use or source-use patterns.
- If the current question is part-whole admission, use `A.1`, `A.14`, and `C.13`.

