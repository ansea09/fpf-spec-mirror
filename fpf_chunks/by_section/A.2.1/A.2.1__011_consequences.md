---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__011_consequences.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:9 — Consequences"
line_start: 2635
line_end: 2644
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:9 - Consequences

`A.2.1` makes work attribution and role admission replayable. A reader can ask: who is the holder, what role value is assigned, which bounded context gives that role meaning, and which window or source is current for the claim?

The benefit is compactness. FPF can keep one role-assignment relation for enactment-facing roles instead of multiplying role kinds for documents, standards, reports, dashboards, interfaces, method descriptions, and relation arguments.

The cost is discipline. Authors must recover neighboring claims instead of putting them into assignment prose. Capability, role state, method, work plan, performed work, evidence, status, publication, assurance, gate, and decision claims each keep their governing pattern.

Reopen `A.2.1` only when the core assignment relation changes: admitted holder kinds, SlotSpecs, assignment-currentness discipline, direct work-role qualifiers, or the treatment of `RoleEnactmentFact`. Reopen neighboring patterns when the dispute is about capability, role state, method, work, evidence, status, source, publication, assurance, gate, or decision use.

