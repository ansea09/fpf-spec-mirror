---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:9"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__011_common-anti-patterns.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:9 — Common Anti-Patterns"
line_start: 2185
line_end: 2195
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `TransformerSystem` as a system subtype | It fuses system identity with a contextual role. | Use `U.RoleAssignment(holderRef=<system-or-acting-holon>, roleRef=TransformerRole@Context, boundedContextRef=<context>)` when a holder role assignment is current. |
| "The PDF enforced the rule" | The episteme did not perform work. | Name the system or acting holon that performed enforcement work, and name the PDF's source, requirement, or evidence use separately. |
| "The report has EvidenceRole" | It treats evidence use as a role held by an episteme. | Use an evidence-use relation around the report, target claim, grounding holon when current, claim scope, polarity, relevance window, and provenance constraints. |
| "The role grants capability" | A role name does not create ability. | Name capability under `A.2.2` and link it as a requirement or checked value when current. |
| "The role contains the method" | A role value is not a method. | Name method and method description through `A.15`, `A.3.1`, and `A.3.2`. |
| "Argument role equals U.Role" | A relation position is not a work-facing role value. | Use `A.6.5` SlotKind and relation signature discipline. |

