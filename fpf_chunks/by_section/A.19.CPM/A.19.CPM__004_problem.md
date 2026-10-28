---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator (CPM)"
section_id: "A.19.CPM:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__004_problem.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator (CPM)"
  - "A.19.CPM:2 — Problem"
line_start: 38689
line_end: 38702
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass"
---

### A.19.CPM:2 - Problem

Engineering teams frequently need to compare two options (designs, methods, vendors, trajectories, hypotheses, etc.) across multiple measures and under incomplete evidence. Without a canonical comparison mechanism, teams predictably fall into one or more of these failure modes:

* **Hidden scalarization:** forcing a single number (or a single winner) from multi‑criteria reality, erasing incomparability and ties.
* **Silent totalization:** inventing an implied total order by convenience tie‑breakers or implicit thresholds, even when only a partial order is warranted.
* **Inadmissible arithmetic:** comparing across measures using operations that are not scale-admissible (CSLC‑violating) or not admitted by the declared admissibility frame.
* **Comparator drift:** the comparison rule or selected edition is unresolved, so teams can use different rules for the same profiles. Explicit prose or code can supply the rule when its meaning and edition are recoverable.
* **Unknown coercion:** missing or unknown evidence is coerced into an outcome (e.g., `missing = equal`), producing comparisons that look decisive but are epistemically unsafe.
* **Comparison-boundary drift:** the same result label is reused after the profile pair, comparator, A.19 predicate, claim scope, selected context slices, reference plane, or evaluation window changed.
* **Cross-scheme or cross-plane leakage:** a comparison relies on a semantic relation between two exact F.17 `SchemeSenseCell` values without an obtaining F.9 `Bridge` and its separate bounded-use claim, or crosses exact ReferencePlanes without the applicable plane relation and policy. The relation or policy needed by the comparison is then unrecoverable.

CPM exists to make comparison explicit, admissibility-gated, set-valued, and replayable, so downstream selection can remain a separate policy-bound step.

