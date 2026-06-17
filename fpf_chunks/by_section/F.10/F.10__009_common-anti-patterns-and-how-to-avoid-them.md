---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 75462
line_end: 75474
dependencies:
  - "A.2.4"
  - "B.3"
  - "F.1"
  - "F.18"
  - "F.3"
  - "F.9"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| `Validated -> approved -> compliant` | One label carries evidence, standard, and requirement status at once. | Split into evidence, standard, and requirement status-use statements; add bridge and evaluation rule only where admitted. |
| Approved method means SLO satisfied | Design-time standard status is used as run-time requirement status. | Keep method-description approval separate from run-time evidence and clause evaluation. |
| Status badge as gate passage | A display cue is treated as source, decision, and permission. | Recover source relation, target, window, and direct gate or release pattern. |
| Clause-less compliance | "Compliant" is asserted without a requirement clause. | Name the clause or acceptance criterion and the window. |
| Bridge-free roll-up | Cross-context dashboard aggregates labels as if meanings were native. | Add F.9 bridges with loss notes or downgrade to local explanation. |
| Evidence escalation without independence | One repeated lab result is called replicated. | Keep it measured or corroborated unless independent replication conditions are named. |
| Status role for episteme | A report, standard, or requirement is said to hold a role. | Use A.2.4 status-use or evidence-use relation slots and F.10 status-family mapping. |
| Tool-state explosion | Every local tool state becomes a new status kind. | Map local labels to the nearest context-local status cell; keep tool labels as local names when no durable family is needed. |

