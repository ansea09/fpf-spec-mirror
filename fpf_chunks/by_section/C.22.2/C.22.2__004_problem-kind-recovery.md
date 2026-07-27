---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:3"
section_title: "Problem-Kind Recovery"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__004_problem-kind-recovery.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:3 — Problem-Kind Recovery"
line_start: 51251
line_end: 51268
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

### C.22.2:3 - Problem-Kind Recovery

For this decision, `problem` remains an ordinary word in non-FPF-governed prose. Recovery is required only when the wording changes a governed use, FPF kind, FPF relation kind, downstream selector reference, evidence claim, causal-use claim, bridge claim, assurance claim, decision claim, use-boundary claim, or another governed claim named by value. The preferred center is the framed problem representation: a problem-side representation of a selected EntityOfConcern under context, scope, viewpoint or role concern, constraints, and improvement or acceptance probe. When `problem` carries FPF work, selection, evidence, causal, bridge, assurance, decision, or use-boundary claim, the claim is recoverable through this table:

| FPF-governed use | Current FPF recovery | `C.22.2` disposition |
|---|---|---|
| Symptom, anomaly, deviation, risk signal, or stakeholder signal | Problem signal or problem signal reference | May trigger a `ProblemCard@Context`, but is not yet a problem-side representation by itself. |
| Problematic situation | Plain cue for an exact condition, entity, work, transformation, relation, or combination already governed by their direct patterns | The card states claims about the exact recovered objects; the phrase does not introduce `U.Situation`. An actual Problem requires an obtaining `ProblematicForRelation` under `C.22.PFR`. |
| Framed problem representation | Problem-side representation of a selected EntityOfConcern under context and acceptance constraints | Center of `ProblemCard@Context`; representation-change claims apply `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` when current. |
| Candidate problem in archive or retained candidate pool | Member of a retained candidate set, pool, archive, or front | Must preserve source set or reference, declared set relation when that FPF relation is being made and named by value, retention criterion, budget or window, and review cadence when the retention rule requires it. |
| Selected problem from a set-return treatment | Selected set member or emitted problem-side record under a selection criterion | `ProblemCard@Context` may carry the selected problem, but selected-set semantics remain with `G.5`, `C.18`, `C.19`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q`. |
| Problem ready for selector-facing use | Problem-side record sufficient to emit or bind `TaskSignature` or `TaskKind` | `C.22` uses the typed selector reference; `C.22.2` does not expand `TaskSignature` into a problem-card dump. |
| Downstream task or performed-work cue | Method known enough for task typing, method-family selection, planning, or performed work | Use the selector, work-family, transformation-flow, evidence, provenance, assurance, gate, or decision pattern named by value for that claim. |
| E.8 pattern `Problem frame` | Practitioner-recognition section inside a pattern | Not the C.22 problem-side representation. |
| E.9 DRR `Problem frame` | Decision-rationale section in a design-rationale record | Not the C.22 problem-side representation. |

Local interpretation rule: `ProblemCard@Context` is the problem-side record shape before downstream typing or work. It may name candidate `ProblemProfile`, candidate `TaskSignature`, `setContextRef`, problem-side cue, governing-pattern cue, or first-principles cue material only when those references change the problem-card use. It does not promote those references into local kinds or claims outside `C.22.2`.

