---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:4"
section_title: "Problem, Task, Method, Work, and Result Split"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__005_problem-task-method-work-and-result-split.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:4 — Problem, Task, Method, Work, and Result Split"
line_start: 50251
line_end: 50272
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
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
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
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
  - "actual PFR versus non-actual or solvability claim"
  - "assertion polarity"
  - "current reliance"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card episteme"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "validation boundary"
---

### C.22.2:4 - Problem, Task, Method, Work, and Result Split

`ProblemCard@Context` remains usable while the method is unknown, contested, not yet selected, or not yet specific enough for downstream work. A known method does not by itself make the problem ready: if the proposed method is known but the problem signal, scope, acceptance probe, or EntityOfConcern remains unstable, `C.22.2` remains current. If both the problem representation and the method are already accepted and the remaining question is planned execution, apply `A.15`. The card may carry method-family cues and reasons for method search, but it does not present downstream work as already known task execution.

Use this split:

| Term or local name | Current FPF recovery | Local disposition |
|---|---|---|
| `Problem` | Either Plain wording for the framed problem episteme or an actual `ProblematicForRelation`, according to the current claim | `C.22.2` governs the episteme; `C.22.PFR` governs the actual relation. Do not infer either from the label alone. |
| ProblemCard@Context | Compact problem-side record before P2W | `C.22.2`-governed record shape under `C.22`; stabilizes a problem-side representation under declared context. |
| ProblemProfile | C.22-facing `ProblemProfile` prepared or bound from a problem-side representation when sufficient | Downstream `ProblemProfile` reference; not the card itself and not a work request. |
| `TaskKind` | Selector-facing task kind in `C.22` | Downstream typed selector reference; not a work-plan entry. |
| `TaskFamilyRef` | Reference to a family of task kinds or method-consumption classes | Used only when current `C.22` selector logic requires it. |
| `TaskSignature` | Minimal selector-facing signature for eligibility, acceptance, and selection | May be emitted or bound from `ProblemCard@Context`; stays minimal. |
| Method-family selection claim | Comparison or selection among method families | Governing pattern `G.5`; not a problem-card field. |
| `U.Method`, `U.MethodDescription` | Method and method description | Governing pattern family `A.15` and related method-description anchors. |
| `U.WorkPlan`, `SlotFillingsPlanItem` | Planned work and work-plan entry | Governing pattern family `A.15`; not a C.22 task signature. |
| `U.Work` | Performed work | Governing pattern family `A.15`; if the attempted claim is evidence, provenance, or assurance, use `A.10`, `G.6`, or `B.3` for that relation. |
| Result record and result measurement | Evidence, provenance, measurement characterization, assurance, or refresh material according to the attempted claim | Use `A.10`, `G.6`, `B.3`, `C.16`, or `G.11` according to the claim kind being made. |

Transition condition: `ProblemCard@Context` may prepare a candidate `ProblemProfile`, bind an existing `ProblemProfile`, emit a candidate `TaskSignature`, or bind a `TaskSignature` only when P2W or selector readiness is declared. If several downstream signatures remain plausible, keep them as candidate signatures instead of binding one chosen `TaskSignature`. When the issue under repair becomes method-family selection, selected method, planned work, performed work, result record, or result measurement, apply the governing FPF pattern for that claim; do not expand the card.

