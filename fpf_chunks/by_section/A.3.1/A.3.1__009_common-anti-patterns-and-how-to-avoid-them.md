---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 6461
line_end: 6471
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "B.1.5"
  - "C.2.P.DR"
  - "C.29"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The code is the method." | If the claim is about the repository or executable text, use `U.MethodDescription`; if it is about the semantic way of doing, name the `U.Method` and its context. |
| "The workflow diagram is the work." | Use `U.MethodDescription` for the diagram, `U.WorkPlan` for planned work, and `U.Work` for dated occurrence. |
| "The graph path routes the decision." | If it is graph structure, use `E.18`; if it is overread as route or action, use `C.2.P.DR`; if a gate or authority claim is current, use the direct gate or authority pattern. |
| "The optimization model is the process." | Recover whether the current claim is formal substrate, method description, method semantics, work plan, work, or evidence. |
| "The protocol approval proves safe execution." | Separate publication-state claim, gate or authorization claim, evidence claim or assurance claim, work plan, and dated work. |
| "The team is the method." | Keep holders and assignments in role assignment; keep capability in capability; keep method requirements context-local. |

