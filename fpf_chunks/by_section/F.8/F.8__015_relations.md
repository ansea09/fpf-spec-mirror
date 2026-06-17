---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__015_relations.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:13 — Relations"
line_start: 74476
line_end: 74491
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

### F.8:13 - Relations

**Builds on.** `A.7`, `A.8`, `A.11`, `E.10`, `E.10.ARCH`, `F.1`, `F.2`, `F.3`, `F.5`, `F.7`, `F.9`, and `F.18`.

**Coordinates with.** `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.6.5`, `A.15`, `A.15.1`, `F.4`, `F.6`, `F.10`, `F.13`, `F.14`, `F.15`, `F.17`, `C.3`, `E.9`, and direct status-use, evidence-use, source-use, publication-use, requirement-use, assurance, gate, decision, method, work, characteristic, and architecture patterns.

**Constrains.**

- `F.5` names only after F.8 has decided what kind of naming case is current.
- `F.4` governs only work-facing role-description naming cases.
- `F.9` and `F.7` govern cross-context row admission before F.8 reuses the row label.
- `F.18` expands durable public naming after F.8 has admitted the name decision.
- `F.14` and `F.15` use F.8 to avoid role, status, row, and alias explosion.

**Does not replace.** Direct governing patterns for the named value, role assignment, performed work, status, evidence, source, publication, requirement, assurance, gate, decision, method, work, relation-slot, characteristic, architecture, or mathematical-lens claims.

