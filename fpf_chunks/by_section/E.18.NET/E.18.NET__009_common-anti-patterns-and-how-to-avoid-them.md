---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 83692
line_end: 83704
dependencies:
  - "A.12"
  - "A.15"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "E.11.PUA"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "F.18"
  - "U.Transfer"
keywords:
---

### E.18.NET:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One giant flow | Development, use, evaluation, and refresh are called valuations solely because they are coupled. | Test shared TFS identity; when independent members and a direct relation are needed, select a network. |
| Detail becomes a member | A zoomed diagram, team boundary, or named stage becomes another TFS. | Use E.18 `SubflowRef` while every position and internal transfer still resolves in one parent. |
| Universal cross-flow edge | `creates`, `produces`, `uses`, `input`, `result`, `handoff`, or `transfer` labels stand in for several relations. | Apply each direct owner: missing kind/predicate returns `missing-governor`; unresolved or false predicates and missing endpoint bindings retain their own stop results. |
| Record makes the world | Filling `memberRows` or drawing edges is treated as establishing members and relations. | Ground members and relation occurrences first; keep the record descriptive. |
| Recursive flattening | A parent copies all nested positions and state into one global graph. | Keep finite member paths and expose only the boundary positions needed by the parent use. |
| Global design/run ladder | One `DesignRunTag` is assigned to the network. | Restore one tag per exact leaf position binding. |
| Network as actor or workflow | The network builds, evaluates, repairs, schedules, or authorizes. | Name the acting system and Work, or the exact decision/gate/assurance owner; keep the network non-agentive. |
| Pretty graph as network | A connected diagram is accepted without exact members, relations, constraints, and use frame. | Keep it as an E.18.2 or provisional description until all four A.22 discriminators are recoverable. |

