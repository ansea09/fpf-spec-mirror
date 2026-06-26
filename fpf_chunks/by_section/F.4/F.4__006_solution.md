---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__006_solution.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:4 — Solution"
line_start: 80829
line_end: 80900
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:4 - Solution

Use a role-description episteme to describe one `U.Role` in one bounded context. The description gives readers enough to recognize and check the role, while sending neighboring claims to their governing patterns.

```text
RoleDescriptionCore:
  DescribedRoleSlot:
  BoundedContextSlot:
  HolderAdmissionSlot:
  RecognitionTextSlot:
  RoleInvariantSetSlot:
  RoleStateRequirementRefs:
  CapabilityRequirementRefs:
  MethodRequirementRefs:
  WorkUseBoundarySlot:
  NamingRefs:
  BridgeRefs:
  NonRoleUseBoundarySlot:
```

This is a description episteme shape, not a new assignment relation. Its publication may be a card, table row, method appendix, standard clause, or pattern section. The publication form is not the role description by default; it publishes or carries the description episteme.

#### F.4:4.1 - Core Slot Meanings

| Slot | Admitted value | Meaning |
| --- | --- | --- |
| `DescribedRoleSlot` | `U.Role` | The role value being described. |
| `BoundedContextSlot` | `U.BoundedContext` | The context that gives the role value local meaning. |
| `HolderAdmissionSlot` | Holder kind or admission statement governed by `A.2` and `A.2.1` | What kind of acting holon may fill `RoleHolderSlot` in a role assignment. |
| `RecognitionTextSlot` | Short description episteme content | The first-minute description that lets a reader recognize the role. |
| `RoleInvariantSetSlot` | Small set of role invariants | Conditions that remain true of the role value in the bounded context. |
| `RoleStateRequirementRefs` | `A.2.5` references when current | Role-state or enactable-state requirements. |
| `CapabilityRequirementRefs` | `A.2.2` references when current | Ability or operating-envelope requirements; not created by the role name. |
| `MethodRequirementRefs` | `A.15`, `A.3.1`, or `A.3.2` references when current | Method or method-description requirements linked to the role. |
| `WorkUseBoundarySlot` | Boundary statement | What the role description does and does not say about performed work. |
| `NamingRefs` | `F.18` or local naming references when current | Durable role-name settlement and aliases. |
| `BridgeRefs` | `F.9` bridge references when current | Cross-context comparison or reuse of role-like senses. |
| `NonRoleUseBoundarySlot` | Boundary statement | Directs evidence, status, source, publication, requirement, definition, explanation, assurance, gate, and slot-position uses to their patterns. |

The slot list is an open-world discipline. A quick local description may fill only the role, context, recognition text, holder admission, and non-role boundary. A safety-critical work-admission use may need role-state, capability, method, assignment-window, and evidence references through neighboring patterns.

#### F.4:4.2 - Role Description vs Neighboring Values

Keep these distinctions:

| Current claim | Governing pattern |
| --- | --- |
| What role value is this? | `A.2` |
| Which holder bears the role in which context and window? | `A.2.1` |
| Is the assignment in an admitted role state? | `A.2.5` |
| Can the holder do the relevant work? | `A.2.2` |
| Which method, method description, plan, or work occurrence is current? | `A.15`, `A.15.1`, `A.15.2`, `A.3.1`, `A.3.2` |
| How do role values satisfy requirements, conflict, qualify, or bundle inside one context? | `A.2.7` |
| What durable name should this role have? | `F.18` |
| How do role-like senses compare across contexts? | `F.9` |
| How is an episteme used as evidence, source, standard, requirement, status bearer, publication, or assurance input? | Direct episteme-use, evidence-use, status-use, source-use, publication-use, requirement-use, or assurance pattern |
| Which relation position admits which filler kind? | `A.6.5` |

F.4 may point to these patterns; it does not copy their ontology.

#### F.4:4.3 - Positive Construction Rule

Write a role description in this order:

1. Name the described `U.Role` and bounded context.
2. State the admitted holder kind for role assignment.
3. Give one short recognition paragraph.
4. List the role invariants that make the role different from neighboring roles.
5. State the non-role boundary: what this description does not say about assignment, capability, method, work, evidence, status, permission, publication, or slot positions.
6. Add neighboring references only when the current use depends on them.
7. If the name is durable, public, cross-context, or Core-facing, settle it through `F.18`; if the sense crosses contexts, use `F.9`.

