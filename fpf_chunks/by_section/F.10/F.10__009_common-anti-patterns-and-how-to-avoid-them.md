---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 96607
line_end: 96622
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.6.1"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.6"
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
| `Validated -> approved -> compliant` | One label carries evidence, standard, requirement, and release status. | Split the target/result/status occurrences; add exact Bridge, interpretation relation, evaluation work, and rule only where current. |
| Approved method means SLO satisfied | Design approval becomes runtime result. | Keep MethodDescription approval, method enactment, runtime result, and clause evaluation separate. |
| Evidence status as domain result | `Measured`, `Corroborated`, or `Refuted` replaces measurement, proof, causal, or diagnostic result. | Recover the direct result and result episteme first; evidence status only classifies evidential standing for the named use. |
| Status defines target | A `Ready` or `Approved` row is treated as constituting a service, method, clause, person/team state, or product. | Recover target identity under its direct governor before status application. |
| Status badge or list membership as use | Display, list, or row membership is treated as source, status application, gate passage, or reliance. | Recover assertion/source and the separate actual receiving-use relation. |
| Clause-less compliance | *Compliant* is asserted without an exact clause, target, rule, scope, conditions, and window. | Recover the clause and direct evaluation result. |
| Bridge-free roll-up | A dashboard aggregates local labels as global synonyms. | Use exact cells and F.9 occurrences, or downgrade to local explanation. |
| Bridge/family edge as explanation | A Bridge or `EvidenceStatus -> RequirementStatus` arrow is treated as direct reason. | Name the `StatusInterpretationRelation`, exact rule, evaluation application, and result. |
| Evidence escalation without independence | One repeated lab result is called replicated. | Keep it measured/corroborated until independent replication conditions and results are recovered. |
| Status role for episteme | A report, standard, or requirement is said to ‘hold a role’. | Use the A.2.4 and F.10 use relations. They establish neither System admission, local system-role classification, nor an assignment. If the receiving claim needs an assignment, name the admitted System, declared assignment species and occurrence, and that System as its holder. |
| Tool-state explosion | Every local tool state becomes a durable status kind. | Keep tool labels local; create a durable cell/family mapping only for a receiving use that needs it. |

