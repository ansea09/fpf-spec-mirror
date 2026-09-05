---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Reusable Way of Doing with Explicit Applicability"
section_id: "A.3.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.3.1 — U.Method: Reusable Way of Doing with Explicit Applicability"
  - "A.3.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 8384
line_end: 8394
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.22"
  - "A.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.3.1"
  - "C.3.2"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "F.9"
  - "G.5"
keywords:
---

### A.3.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Treating executable text as sufficient Method identity. | If the claim is about the repository or executable text, use `U.MethodDescription`; if it is about the semantic way of doing, name the `U.Method`, participant meanings, applicability, effects, and bounds. |
| Treating a workflow diagram as the dated Work occurrence. | Use `U.MethodDescription` for the diagram, `U.WorkPlan` for planned work, and one Work occurrence admitted under `U.Work` for the dated occurrence. |
| Inferring prescribed action from graph layout. | Use `E.18` when the sentence is about graph structure and `C.2.P.DR` when layout is being made to prescribe action. If the source actually asserts gate passage or authority, state that separate gate or authority claim. |
| Leaving the optimization-model claim unresolved. | Ask whether the sentence states a formal object, a method description, a reusable way, a work plan, dated Work, or evidence; then keep only that claim in the method position. |
| Inferring safe execution solely from protocol approval. | Separate publication-state claim, gate or authorization claim, evidence claim or assurance claim, work plan, and dated work. |
| Using a team's identity in place of method semantics. | Keep admitted Systems, local system-role kinds, classifications, assignments, and capability claims with their direct patterns; keep participant meanings, applicability, conditions, effects, and bounds with the Method. |

