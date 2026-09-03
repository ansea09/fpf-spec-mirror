---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:6"
section_title: "Choosing the right relation (decision table)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__007_choosing-the-right-relation-decision-table.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:6 — Choosing the right relation (decision table)"
line_start: 24342
line_end: 24355
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27.TA"
  - "C.29"
  - "C.3"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
keywords:
  - "AspectOf"
  - "ComponentOf"
  - "ConstituentOf"
  - "PhaseOf"
  - "PortionOf"
  - "aspect"
  - "belongs to"
  - "component"
  - "constituent"
  - "member"
  - "part"
  - "phase"
  - "portion"
---

### A.14:6 - Choosing the right relation (decision table)

| You want to say... | Use | Why |
| --- | --- | --- |
| “This is a piece of the same stuff or extent.” | **PortionOf** | One extensive measure and conservation rule govern the claim. |
| “This is a discrete structural part inside the whole.” | **ComponentOf** | The part is structurally integrated; amount and facet selection do not decide it. |
| “This is a logical or content part of a conceptual whole.” | **ConstituentOf** | The claim concerns conceptual or epistemic assembly. |
| “This dependent structural part is one aspect of this bearer under this facet rule.” | **AspectOf** | Name the aspect, bearer, facet rule, occurrence, and identity rule; a Characteristic, view, projection, partition, or time window is not enough. |
| “This is the same entity during a proper sub-interval.” | **PhaseOf** | The same carrier and its identity rule hold over a proper temporal restriction. |
| “This item belongs to that collection.” | **The belongs-to rule defined for that collection** | Name the entity and collection, state what makes belonging begin and end, and distinguish recurrence. Belonging establishes neither parthood nor its impossibility. |
| “This System holds a local work-facing kind or relation position.” | local system-role-kind classification, `U.SystemRoleAssignment`, or an A.6.5 relation position | Kind classification, assignment occurrence, and relation participation are not parts. |

> **Firewall reminder.** If the sentence is about system-role-kind classification or assignment, how action is done, or what happened when, use `A.2`/`A.2.1`, `A.3.1`, or `A.15.1` as appropriate. For an episteme, use A.14 for content parthood or a proper interval of one unchanged C.2.1 identity; changed claims, EntityOfConcern, or effective reference scheme identify another episteme, and any historical continuation uses C.2.1 `EpistemeEditionRelation` only when its predicate obtains.

