---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:7"
section_title: "Authoring guidance (for engineers and leads)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__008_authoring-guidance-for-engineers-and-leads.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:7 — Authoring guidance (for engineers and leads)"
line_start: 1640
line_end: 1645
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:7 - Authoring guidance (for engineers and leads)

* **Name roles for intent, not mechanics.** Prefer `CoolingCirculatorRole` over `ChannelFluidWithCentrifugalProfile`.
* **Pin the context early.** If two teams disagree, split contexts and (optionally) define an alignment bridge; do not over‑generalise the role.
* **Document the enactment chain.** For any operational claim, be ready to point to: `RoleAssigning → RoleAssignment → (Role ↦bindsMethod↦ Method) ↔ MethodDescription → Work`. (Readers’ dictionary: *workflow/script/state‑machine/dynamical model/quantum circuit → MethodDescription; run/job/operation → Work.*)

