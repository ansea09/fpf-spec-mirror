---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:6"
section_title: "Characterization, Indicators, and Comparability"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__007_characterization-indicators-and-comparability.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:6 — Characterization, Indicators, and Comparability"
line_start: 51583
line_end: 51600
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

### C.22.2:6 - Characterization, Indicators, and Comparability

`ProblemCard@Context` states either a recoverable `characterization relation` and `comparability or parity relation`, or an explicit current reason why the problem can proceed without one.

The heavy content stays with existing FPF patterns:

- `C.16` carries measurement characterization, backing, and comparability discipline;
- `A.19` carries characteristic, scale, unit, polarity, and indicator-use discipline;
- `C.25` carries Q-bundles and quality-like multi-characteristic bundles;
- `G.9` carries parity, comparison-window, comparator, budget, unit, repeatability, and reproducibility pins;
- `G.0` carries comparison-frame and CG-Spec governance;
- `G.4` carries acceptance clauses and threshold predicates;
- `G.5` governs selected-set publication when the problem enters a selected set.

Missing characterization or parity relation is a current disposition. The record applies the characterization, parity, search, or pool pattern when that relation is current instead of pretending the problem is ready for P2W.

The `C.22.2` candidate acceptance criterion separates functional check, constraint compliance, risk or safety boundary, parity or comparison relation, and freshness window when those relations are current. Comparison frame, CG-Spec, or comparability governance is governed by `G.0`. Acceptance clauses and acceptance threshold predicates apply `G.4`; `C.22.2` may name only the needed relation, cue, or reference. Passing a test, improving one observed indicator value, or naming an acceptance phrase is not by itself sufficient for P2W use.

