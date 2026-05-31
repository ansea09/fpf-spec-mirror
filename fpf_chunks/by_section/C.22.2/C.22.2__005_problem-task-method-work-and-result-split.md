---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:4"
section_title: "Problem, Task, Method, Work, and Result Split"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__005_problem-task-method-work-and-result-split.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:4 — Problem, Task, Method, Work, and Result Split"
line_start: 44034
line_end: 44055
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:4 - Problem, Task, Method, Work, and Result Split

`ProblemCard@Context` is admissible while the method is unknown, contested, not yet selected, or not yet specific enough for downstream work. A known method does not by itself make the problem ready: if the proposed method is known but the problem signal, scope, acceptance probe, or described entity remains unstable, `C.22.2` remains live. If both the problem representation and the method are already accepted and the remaining question is planned execution, exit to `A.15`. The card may carry method-search exits and method-family cues, but it must not present downstream work as already known task execution.

Use this split:

| Term or object | Current FPF reading | Local disposition |
|---|---|---|
| `Problem` | Problem-side representation of the described entity of concern under context | Center of `C.22.2` only after problem-kind recovery. |
| ProblemCard@Context | Compact problem-side record before P2W | `C.22.2`-governed record shape under `C.22`; stabilizes a problem-side representation under declared context. |
| ProblemProfile | C.22-facing profile prepared or bound from a problem-side representation when sufficient | Downstream profile anchor; not the card itself and not a work item. |
| `TaskKind` | Selector-facing task kind in `C.22` | Downstream typed anchor; not a plan item. |
| `TaskFamilyRef` | Reference to a family of task kinds or method-consumption classes | Used only when current `C.22` selector logic requires it. |
| `TaskSignature` | Minimal selector-facing signature read for eligibility, acceptance, and selection | May be emitted or bound from `ProblemCard@Context`; must stay minimal. |
| Method-family selection object | Comparison or selection among method families | Receiving pattern `G.5`; not a problem-card field. |
| `U.Method`, `U.MethodDescription` | Method and method description | Receiving pattern family `A.15` and related method-description anchors. |
| `U.WorkPlan`, `SlotFillingsPlanItem` | Planned work and plan item | Receiving pattern family `A.15`; not a C.22 task signature. |
| `U.Work` | Performed work | Receiving pattern family `A.15`, with evidence, provenance, and assurance exits when live. |
| Result record and result measurement | Evidence, provenance, measurement characterization, assurance, or refresh material depending on use | Receiving patterns `A.10`, `G.6`, `B.3`, `C.16`, `G.11`, and neighbors. |

Transition condition: `ProblemCard@Context` may prepare a candidate `ProblemProfile`, bind an existing `ProblemProfile`, emit a candidate `TaskSignature`, or bind a `TaskSignature` only when P2W or selector readiness is declared. If several downstream signatures remain plausible, keep them as candidate signatures instead of binding one chosen `TaskSignature`. When method-family selection, selected method, planned work, performed work, result record, or result measurement becomes live, use the receiving pattern; `C.22.2` does not absorb that pattern's authority.

