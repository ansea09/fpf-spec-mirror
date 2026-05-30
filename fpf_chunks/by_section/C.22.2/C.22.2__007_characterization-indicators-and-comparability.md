---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:6"
section_title: "Characterization, Indicators, and Comparability"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__007_characterization-indicators-and-comparability.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:6 — Characterization, Indicators, and Comparability"
line_start: 43763
line_end: 43780
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "A.6.Q"
  - "B.3"
  - "C.11"
  - "C.16"
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

### C.22.2:6 - Characterization, Indicators, and Comparability

`ProblemCard@Context` must state either a recoverable `characterization basis` and `comparability or parity basis`, or an explicit current reason why the problem can proceed without one.

The heavy content stays with existing FPF patterns:

- `C.16` carries measurement characterization, backing, and comparability discipline;
- `A.19` carries characteristic, scale, unit, polarity, and indicator admissibility discipline;
- `C.25` carries Q-bundles and quality-like multi-characteristic bundles;
- `G.9` carries parity, comparison-window, comparator, budget, unit, repeatability, and reproducibility pins;
- `G.0` carries comparison-frame and CG-Spec governance;
- `G.4` carries acceptance clauses and threshold predicates;
- `G.5` governs selected-set publication when the problem enters a selected set.

Missing characterization or parity basis is a current disposition. The record exits to characterization, parity, or search or pool work under the receiving pattern instead of pretending the problem is ready for P2W.

The `C.22.2` candidate acceptance basis must distinguish functional check, constraint compliance, risk or safety boundary, parity or comparison basis, and freshness window when those relations are live. Comparison frame, CG-Spec, or comparability governance exits to `G.0`. Acceptance clauses and acceptance threshold predicates exit to `G.4`; `C.22.2` may name only the need, cue, or reference. Passing a test, improving one observed indicator value, or naming an acceptance phrase is not by itself admissible acceptance for P2W.

