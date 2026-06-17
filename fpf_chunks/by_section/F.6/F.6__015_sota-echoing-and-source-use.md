---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:13"
section_title: "SoTA-Echoing and Source-Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__015_sota-echoing-and-source-use.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:13 — SoTA-Echoing and Source-Use"
line_start: 73800
line_end: 73805
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:13 - SoTA-Echoing and Source-Use

External traditions such as RBAC, BPMN, PROV, service management, safety standards, and process-notation traditions use "role", "activity", "participant", "status", "approval", and "execution" in different ways. F.6 does not treat any one tradition as semantic authority. The FPF role-assignment ontology recovers the bounded context and local role value first; assigns acting holders only through `U.RoleAssignment`; represents performed work through `U.Work`; and represents evidence, status, source, publication, and bridge claims through their own patterns.

When a source tradition is current, cite it through the direct source-use or bridge relation. Do not let source prestige, familiar vocabulary, or a popular notation collapse FPF kinds.

