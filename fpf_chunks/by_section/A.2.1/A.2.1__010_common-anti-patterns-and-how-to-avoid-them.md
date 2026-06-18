---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 2486
line_end: 2497
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

### A.2.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Contextless assignment: "Alice is reviewer" | No bounded context, role identity, or assignment window is recoverable. | Recover `Alice#ReviewerRole:ReviewContext` and state window disposition when current. |
| Episteme as holder: "The report has EvidenceRole" | The report is being used in an evidence relation, not holding a work-facing role. | Use evidence-use relation with target claim, scope, polarity, and relevance window when current. |
| Assignment as capability | The role assignment is treated as evidence that the holder can perform the work. | Use `A.2.2` for capability and connect capability evidence only when the claim depends on it. |
| Assignment as work | The assignment is treated as if work already happened. | Use `A.15.1` for dated work and cite `performedBy = RoleAssignment`. |
| `U.RoleEnactment` as root object | A derived performed-by fact becomes a second run-time ontology. | Use `RoleEnactmentFact` only as a named fact over work and assignment, or write direct `Work.performedBy` relation. |
| Window omitted in a time-sensitive claim | Currentness is assumed by silence. | Fill, inherit, mark unknown, mark not asserted, or lower the stronger claim. |
| Evidence and status slots hidden in assignment provenance | Evidence polarity, target claim, status value, or status window is buried under assignment source. | Use direct evidence-use or status-use SlotSpecs; keep assignment provenance only for the assignment claim. |

