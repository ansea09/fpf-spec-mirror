---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:3"
section_title: "Problem Reading and Kind Recovery"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__004_problem-reading-and-kind-recovery.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:3 — Problem Reading and Kind Recovery"
line_start: 43946
line_end: 43963
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

### C.22.2:3 - Problem Reading and Kind Recovery

For this decision, `problem` remains an ordinary word in non-FPF-governed prose. Recovery is required only when the wording changes an admissible move, FPF relation, downstream selector reference, evidence, causal, bridge, assurance, decision, admissibility force, or neighboring-pattern exit. The preferred center is the framed problem representation: a problem-side representation of a selected EntityOfConcern under context, scope, viewpoint or role concern, constraints, and improvement or acceptance probe. When `problem` carries FPF work, selection, evidence, causal, bridge, assurance, decision, or admissibility force, it must be recoverable through this table:

| FPF-governed use | Current FPF recovery | `C.22.2` disposition |
|---|---|---|
| Symptom, anomaly, deviation, risk signal, or stakeholder signal | Problem signal or source signal reference | May trigger a `ProblemCard@Context`, but is not yet a problem-side representation by itself. |
| Problematic situation | Context-bound situation under a viewpoint, domain, constraints, risks, and candidate EntityOfConcern | Captured only through fields that make the situation reviewable. |
| Framed problem representation | Problem-side representation of a selected EntityOfConcern under context and acceptance constraints | Center of `ProblemCard@Context`; representation-change claims exit to `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` when live. |
| Candidate problem in archive or live pool | Member of a retained candidate set, pool, archive, or front | Must preserve source set or reference, declared set relation when that exact FPF relation is live, retention criterion, budget or window, and review cadence when live. |
| Selected problem from a set-return treatment | Selected set member or emitted problem-side record under a selection criterion | `ProblemCard@Context` may carry the selected problem, but selected-set semantics remain with `G.5`, `C.18`, `C.19`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q`. |
| Problem ready for selector-facing use | Problem-side record sufficient to emit or bind `TaskSignature` or `TaskKind` | `C.22` use reads the typed selector reference; `C.22.2` does not expand `TaskSignature` into a problem-card dump. |
| Downstream task or execution target | Method known enough for task typing, method-family selection, planning, or performed work | Exits to `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, gates, or evidence patterns as applicable. |
| E.8 pattern `Problem frame` | Practitioner-recognition section inside a pattern | Not the C.22 problem-side representation. |
| E.9 DRR `Problem frame` | Decision-rationale section in a design-rationale record | Not the C.22 problem-side representation. |

Blocked interpretations: `ProblemCard@Context` is not `U.Problem`, not `ProblemProfile`, not `TaskSignature`, not `TaskKind`, not `U.WorkPlan`, not `U.Work`, not the problem-side representation itself, not a general ticket format, not an archive, not a portfolio, not an evidence object or proof, not a gate decision or gate passage, and not an autonomy object or work-plan item.

