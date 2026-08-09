---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__002_use-this-when.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:0 — Use This When"
line_start: 2993
line_end: 3026
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:0 - Use This When

**Plain name.** System role assignment.

Use this pattern when another claim must rely on which admitted `U.System` holds which enactment-facing `U.Role`, under which role vocabulary and interpretation scheme, during which assignment window.

Typical moments:

- a method description names `InspectorRole`, but the current holder and assignment window are still unstated;
- a performed-work attribution is needed: one exact dated Work occurrence `W` and one exact assignment `RA` participate in `performedUnderAssignment(W, RA)`, the direct relation governed by `F.6`; the actual performer is the admitted holder System `S = RA.HolderSystemSlot`, and a separate assertion may designate `W` and `RA`;
- the same system receives the same role during two separate assignment episodes;
- a DDD-style model-use organization changes the interpretation of an otherwise identical role assignment;
- a constituting decision or installation relation may establish a specialized assignment occurrence;
- a roster entry, configuration line, observation, or evidence relation may support an assignment claim without becoming an assignment slot.

**Primary EntityOfConcern.** The EntityOfConcern is one obtaining `U.RoleAssignment` relation occurrence. Its four required actual participants are an admitted `U.System` holder, one `U.Role` value, the role-taxonomy episteme, and the effective `U.ReferenceScheme` under which that value is interpreted. The occurrence has a maximal continuous temporal extent determined by uninterrupted obtaining; an assignment assertion or occurrence description may state the currently known extent as an `AssignmentInterval`.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, or FPF author who must make role admission or work attribution inspectable without turning role, capability, method, performed work, evidence, or publication into one assignment relation occurrence.

**First useful move.** Write a readable assignment assertion naming the four required participants and the assignment episode being claimed. State the currently known temporal extent separately. Explicitly individuate the relation occurrence only when a receiving claim must distinguish this assignment episode from another rather than merely recognize that the direct relation obtains.

**What goes wrong if missed.** A role label is mistaken for an assignment, repeated episodes collapse into one timeless relation, or a database row is treated as what makes the assignment obtain. Work may then be attributed to the wrong holder or assignment episode, while evidence, capability, and method claims become hidden fields of the assignment.

**What this buys.** Assignment identity becomes stable enough for method admission, role-state checking, and work attribution while ordinary prose remains lightweight. The assignment relation has one exact identity rule; all support, decision, capability, method, work, evidence, and publication claims keep their direct governing patterns.

**Not this pattern when.**

- Use `A.2` for role-value interpretation and the role taxonomy itself.
- Use `A.2.2` for holder capability, `A.2.5` for role state, and `A.2.7` for selected relations among role values.
- Use `A.3.1`, `A.3.2`, and `A.15` for method and role-admission conditions.
- Use `A.15.1` and `F.6` for performed work and its attribution through an assignment.
- Use the direct decision, responsibility, commitment, evidence, reliance, provenance, publication, external-rule, or currentness pattern when that relation is current.
- Use `A.6.5` when an external relation notation labels a participant `role` and the current task is to recover its exact SlotKind and ValueKind.

