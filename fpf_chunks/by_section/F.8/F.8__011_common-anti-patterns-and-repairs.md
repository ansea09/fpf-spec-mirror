---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:9"
section_title: "Common Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__011_common-anti-patterns-and-repairs.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:9 — Common Anti-Patterns and Repairs"
line_start: 74407
line_end: 74419
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:9 - Common Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Suffix minting | A word ending in `Role`, `Status`, `Graph`, `Map`, or `Record` becomes ontology. | Recover kind and use first; send to direct pattern. |
| Evidence role revival | `EvidenceRole` becomes a role-name family. | Recover evidence-use relation; name it only through direct evidence naming. |
| Status-role fusion | `ReadyReviewerRole` or `ApprovedRole` names a role plus state. | Separate role from state or status-use relation. |
| Row overuse | Naming row justifies role assignment or structural inference. | Lower use to row scope or repair the row and bridges. |
| Alias with payload | Alias changes kind, scope, or authority. | Treat as a new decision; use `F.5` and `F.18`. |
| Source prestige minting | Standard or framework term becomes FPF selected name by source prestige. | Use source term as evidence or alias; select FPF name only after recovered meaning fits. |
| U.Type comfort minting | New `U.Type` proposed because existing names feel awkward. | Attempt reduction to local sense, row, role description, direct relation, or existing type. |
| Policy id as magic word | Policy id used without resolvable specification or mint decision. | Add `PolicyIdRef` or lower the claim. |

