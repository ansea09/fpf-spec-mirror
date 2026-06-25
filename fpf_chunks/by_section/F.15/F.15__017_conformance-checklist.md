---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:14.5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__017_conformance-checklist.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:14.5 — Conformance Checklist"
line_start: 83765
line_end: 83774
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.Role"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:14.5 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-F15-1` | Name the unification slice and the current or changed moving parts before applying SCR or RSCR rows. |
| `CC-F15-2` | Check local contexts, Local-Senses, SenseCells, rows, RoleDescriptions, bridges, status windows, aliases, and public names under their direct patterns. |
| `CC-F15-3` | Treat a failed rule as a return to the direct governing pattern, not as permission for F.15 to absorb that pattern's object. |
| `CC-F15-4` | Require bridge kind, direction, `CL`, loss, admitted use, and witness before cross-context reuse. |
| `CC-F15-5` | Recheck only the changed moving parts when an edition, row, bridge, role description, alias, name, or status window changes. |

