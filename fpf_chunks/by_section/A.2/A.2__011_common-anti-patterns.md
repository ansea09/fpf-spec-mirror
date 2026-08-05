---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:9"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__011_common-anti-patterns.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:9 — Common Anti-Patterns"
line_start: 2921
line_end: 2930
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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
| `PumpAsCoolingCirculator` as a system subtype | It turns one assignment into system identity. | Keep the pump kind stable and state `CoolingCirculatorRole` through `U.RoleAssignment`. |
| `PumpUnit-3#CoolingCirculatorRole:Plant-A@Window` | The compact token hides taxonomy, scheme, and the kind of `Plant-A`, while suggesting a mandatory context participant. | Use the `U.RoleAssignment` SlotSpecs governed by `A.2.1`; keep Plant A as the actual plant system or work locus. |
| `AssistantReviewerRole partOf ReviewerRole` | No constructive role whole or role-part relation has been established. | Determine whether the exact claim is an A.2.7 qualification, substitution, incompatibility, or bundle relation, or another role value under A.2; send responsibility, capability, method, and work claims to their direct governing patterns. |
| `The PDF enforced the rule` | An episteme is substituted for the system that performed enforcement work. | Name the holder system and work occurrence; state the PDF's direct external-rule, evidence, or reliance relation separately. |
| `Same role label, therefore same role` | Labels establish neither semantic identity, an obtaining Bridge, nor suitability for a proposed use. | Compare the role claims and exact sense cells. If a cross-scheme action is proposed, establish the F.9 Bridge, separate bounded-use assertion, and current A.10 or B.3 reliance; otherwise stop without identity or permission inference. |

