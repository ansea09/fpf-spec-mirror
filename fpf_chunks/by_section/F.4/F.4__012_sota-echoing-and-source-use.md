---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:10"
section_title: "SoTA-Echoing and Source-Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__012_sota-echoing-and-source-use.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:10 — SoTA-Echoing and Source-Use"
line_start: 81957
line_end: 81969
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

### F.4:10 - SoTA-Echoing and Source-Use

| Practice line | What FPF takes | Practical implication |
| --- | --- | --- |
| Role modeling in organizations, access-control, safety, and method engineering separates role labels, assigned holders, permissions, responsibilities, and performed work. | F.4 keeps only the role-description episteme and sends assignment, permission, capability, method, and work to direct patterns. | A readable role description does not become an access policy, staffing record, or work log. |
| Modern context and interoperability practice treats local meanings as bounded and compares them by explicit mappings, not by shared labels. | F.4 role descriptions stay local to one bounded context; cross-context reuse goes through `F.9`. | Same label does not make the same role. |
| FPF episteme and publication ontology separates the described entity, description episteme, and publication form. | A role description is a description episteme about `U.Role`; a card or table may publish it. | Editing the publication is not automatically changing the role value or assignment relation. |
| FPF slot discipline separates relation positions from fillers. | "Role" in a relation-position phrase is repaired to SlotKind or ValueKind when no work-facing `U.Role` is current. | Slot names do not create role values. |

Current best-known pressure for this problem is not a larger universal role taxonomy. It is explicit separation of local role value, assignment, attributes or capability, permission or policy standing, performed work, and evidence or status use. RBAC, ABAC, zero-trust authorization, safety independence practice, method engineering, and FPF slot discipline all push in that direction, while F.4 keeps only the role-description episteme and hands the neighboring claims to direct patterns.

Currentness and reopen condition: reopen this pattern when `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.15`, `A.6.5`, `C.2.1`, `F.9`, `F.10`, `F.18`, or the accepted episteme-use and status-use discipline changes enough that role-description, holder admission, or non-role-use boundaries would be stated differently.

