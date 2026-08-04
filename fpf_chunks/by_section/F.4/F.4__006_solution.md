---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__006_solution.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:4 — Solution"
line_start: 90529
line_end: 90599
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

Constitute one role-description episteme through `C.2.1`: its exact ClaimGraph describes one `U.Role`, that role is the EntityOfConcern, and one effective `U.ReferenceScheme` governs interpretation. The ClaimGraph names the exact role-taxonomy episteme that supplies the role vocabulary. The description gives readers enough to recognize and check the role while routing neighboring claims to their direct patterns.

The following is a content checklist, not a relation signature or a mandatory record:

**Always make recoverable:**

- the described `U.Role`;
- the role-taxonomy episteme and effective reference scheme;
- a short recognition explanation;
- the independently admitted `U.System` holder kind and, when needed, a reference to its separately governed admission claim;
- the smallest role-invariant set needed by the current use;
- the non-role boundary: what this description does not assert about assignment, capability, method, work, evidence, status, permission, publication, or relation slots.

**Add only when the current use depends on them:**

- role-state predicate references under `A.2.5`;
- capability-condition references under `A.2.2`;
- method or method-description references under `A.3.1`, `A.3.2`, or `A.15`;
- durable-name or alias references under `F.18`;
- bridge references under `F.9`;
- a selected `BoundedModelUseStructure` designated by the receiving assertion or use when it changes that interpretation.

These are claims and neighboring references in an episteme. They are not `SlotSpec` declarations and do not add participants to `U.RoleAssignment` or another generic role relation. A card, table row, method appendix, or pattern section may publish the description; publication form and carrier remain separate from the episteme.

#### F.4:4.1 - Content Meanings

| Content element | Meaning |
| --- | --- |
| Described role | The exact `U.Role` that is the episteme's EntityOfConcern. |
| Role taxonomy and effective scheme | The exact episteme and by-value interpretation scheme under which the role vocabulary is read. |
| Eligible holder kind | Which independently admitted `U.System` kind may participate as holder in `U.RoleAssignment`; the description itself admits nobody and creates no assignment. |
| Recognition explanation | The first-minute explanation that lets a reader distinguish this role from neighboring roles. |
| Role invariants | Conditions about the role value that remain current under the named taxonomy and scheme. |
| Conditional neighboring references | Direct exits for role state, capability, method, naming, and bridges only when the receiving use depends on them. |
| Non-role boundary | The explicit separation from assignment, work, evidence, status, permission, publication, and relation-slot claims. |

A quick local description can stop after the always-recoverable content. A consequence-bearing work-admission use opens only the neighboring relations it actually needs.

#### F.4:4.2 - Role Description vs Neighboring Values

Keep these distinctions:

| Current claim | Governing pattern |
| --- | --- |
| What role value is this? | `A.2` |
| Which admitted system holds the role, and during which assignment occurrence? | `A.2.1` |
| Is the assignment in an admitted role state? | `A.2.5` |
| Can the holder do the relevant work? | `A.2.2` |
| Which method, method description, plan, or work occurrence is current? | `A.15`, `A.15.1`, `A.15.2`, `A.3.1`, `A.3.2` |
| How do role values satisfy admission conditions, conflict, qualify, or bundle under one interpreted taxonomy and scheme? | `A.2.7` |
| What durable name should this role have? | `F.18` |
| How do role meanings compare across taxonomies or schemes? | `F.9` |
| How is an episteme used as evidence, source, standard, requirement, status bearer, publication, or assurance input? | Direct episteme-use, evidence-use, status-use, source-use, publication-use, requirement-use, or assurance pattern |
| Which relation position admits which filler kind? | `A.6.5` |

F.4 may point to these patterns; it does not copy their ontology.

#### F.4:4.3 - Positive Construction Rule

Write a role description in this order:

1. Name the described `U.Role`, its role-taxonomy episteme, and effective reference scheme.
2. State the independently admitted holder kind eligible for role assignment.
3. Give one short recognition paragraph.
4. List the role invariants that make the role different from neighboring roles.
5. State the non-role boundary: what this description does not say about assignment, capability, method, work, evidence, status, permission, publication, or slot positions.
6. Add neighboring references only when the current use depends on them.
7. If the name is durable, public, or Core-facing, settle it through `F.18`; if role meanings must be compared across taxonomies or schemes, use `F.9`.

