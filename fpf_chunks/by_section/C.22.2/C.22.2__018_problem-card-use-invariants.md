---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:17"
section_title: "Problem-Card Use Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__018_problem-card-use-invariants.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:17 — Problem-Card Use Invariants"
line_start: 50512
line_end: 50520
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

### C.22.2:17 - Problem-Card Use Invariants

| Invariant | Requirement |
|---|---|
| One card, one current problem-side representation | One `ProblemCard@Context` instance carries one problem-side representation under one declared context. A changed represented problem states the changed representation or the relation that is reopened. |
| `P2W-ready` is problem-side readiness | The card can be ready as input to P2W or selector-facing use without being ready for work execution, gate passage, method selection, evidence use, or autonomy control. |
| Claims outside `C.22.2` stay outside the card | Evidence, provenance, assurance, gate, autonomy, work, archive, selected-set, comparison, acceptance, representation, temporal, causal, and mathematical-lens claims remain with the pattern that governs each claim being made. |
| Stale or blocked cards state a disposition | A stale, unknown-blocked, changed-representation, or missing required reason, criterion, or source-reference card states refresh, retirement, bounded use, `abstainOrNoChange`, or the relation that is reopened. |

