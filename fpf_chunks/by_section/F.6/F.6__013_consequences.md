---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:11"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__013_consequences.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:11 — Consequences"
line_start: 80395
line_end: 80400
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

### F.6:11 - Consequences

Using F.6 makes role-assignment reasoning narrower and more reliable. A project can still use compact assignment strings and familiar role words, but reliance-bearing claims must expose the holder, role, bounded context, assignment-currentness disposition, and performed-by relation when actual work is claimed.

The cost is one extra split. A source sentence that says "role enacted" may become two or three typed statements: assignment admitted, work performed by that assignment, and evidence or status relation used for downstream reliance. That split is intentional. It prevents duplicate role ontologies and makes audit, bridge, capability, method, and status checks local.

