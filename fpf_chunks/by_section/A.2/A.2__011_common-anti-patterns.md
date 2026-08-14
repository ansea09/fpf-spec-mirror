---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "System-Role Kinds and Assignments"
section_id: "A.2:9"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__011_common-anti-patterns.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "A.2 — System-Role Kinds and Assignments"
  - "A.2:9 — Common Anti-Patterns"
line_start: 3059
line_end: 3072
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10.ROLE"
  - "F.4-F.6"
keywords:
  - "U.SystemRoleAssignment"
  - "ambiguous role wording"
  - "assignment"
  - "holder System"
  - "local System classification"
  - "system-role kind"
  - "work-facing contribution"
---

### A.2:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `PumpAsCoolingCirculator` as a new system subtype | One contribution is mistaken for system identity. | Keep the pump kind stable; use a local `CoolingCirculatorSystemRole` classification and a separate assignment when it obtains. |
| `PumpUnit-3#CoolingCirculatorSystemRole:Plant-A@Window` | The compact token hides the kind declaration, assignment species and occurrence, and the kind of Plant A while suggesting a mandatory context participant. | State the local kind and judgment; when assignment matters, name the A.2.1 occurrence and its declared species, and keep Plant A as the plant System or Work locus. |
| `ReviewerSystemRole` means “assigned reviewer” | Kind membership and assignment occurrence are collapsed. | Evaluate the signature; state the assignment independently. |
| Membership means “an assignment to this kind obtains” | Broader classification would require a broader assignment and subkind order would create world-side facts. | Use direct governed system features; assignment can be one explicitly declared feature. |
| One generic assignment signature accepts `U.Kind` | Arbitrary kinds enter the assigned-kind slot and stronger appointments lose their participant law. | Declare a direct species with an exact local system-role-kind domain. |
| Taxonomy and scheme are assignment participants | Interpretation editions become world-side identity changes. | Keep them in declarations, assertions, or evidence about the predicate. |
| `AssistantReviewerSystemRole partOf ReviewerSystemRole` | No constructive whole or part relation is established. | Test an exact qualification, substitution, incompatibility, bundle, or another local kind and direct relation. |
| `The PDF enforced the rule` | An episteme replaces the system and Work that performed enforcement. | Name the performer and Work; state the PDF's source-use, external-rule, evidence, or reliance relation separately. |
| Same label, therefore same kind or assignment | Spelling establishes neither local identity, Bridge, nor obtaining relation. | Recover the two kinds and establish the exact cross-context result needed by the use. |

