---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:9"
section_title: "Conformance Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__011_conformance-checks.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:9 — Conformance Checks"
line_start: 82063
line_end: 82086
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.RSIR"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:9 - Conformance Checks

Use these checks before a durable name enters a pattern or `UnifiedTermSheet`.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a direct governing pattern. |
| Context | The bounded context and local sense are named. |
| Kind | The kind is stated as governed value kind, not inferred from spelling. |
| Candidate set | Rejected plausible labels are visible with reasons. |
| Role boundary | Role, role assignment, holder, capability, method, work, evidence, and status claims are not collapsed. |
| Slot boundary | Relation slot, interface, port, signature, and relation names cite direct governing patterns. |
| Public row | `F.17` is used only for term-row publication; the row is not the value. |
| Bridge | Cross-context sameness uses `F.9`, not spelling. |
| Lineage | Renames, aliases, splits, merges, and retirements are recorded under `F.13`. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |

Regression checks:

- When a context edition changes, re-check local sense and bridge claims.
- When a role description changes, re-check role name and any holder-assignment name.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

