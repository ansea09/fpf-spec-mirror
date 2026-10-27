---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator (CPM)"
section_id: "A.19.CPM:6"
section_title: "Bias-Annotation — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__008_bias-annotation-informative.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator (CPM)"
  - "A.19.CPM:6 — Bias-Annotation — informative"
line_start: 38796
line_end: 38806
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

### A.19.CPM:6 - Bias-Annotation — informative

CPM makes comparator choices and failure behavior inspectable. This can expose hidden thresholds, tie-breakers or unknown coercion; the declaration alone does not establish that an application avoided them.

Typical bias risks and mitigations:

* **Comparator choice encodes value judgments.** Weights, priority orders, thresholds, and “tie‑break” conventions can encode organizational bias. Declare these choices in the selected `ComparatorSpec` or policy, using existing prose or code when it makes their meaning and edition recoverable.
* **Systematic missingness.** If evidence is systematically missing for certain contexts or groups, naive “unknown → worse” is a bias amplifier. CPM’s tri‑state guard avoids coercion; but teams must still define policy‑bound failure behavior and be explicit when abstention is acceptable.
* **Cross-scheme comparisons can embed structural unfairness.** A comparison that relies on a semantic relation between two exact F.17 `SchemeSenseCell` values cites the obtaining F.9 `Bridge` and its separate bounded-use claim; together they expose the tested correspondence or difference and tolerated loss. A plane-only crossing cites the applicable ReferencePlane relation and policy. Neither branch replaces comparison scope, predicate, comparator, or time.
* **Overconfidence via scalarization.** Collapsing partial orders into scalars often overstates certainty and hides tradeoffs. CPM makes set‑valued outcomes first‑class, so the human or managerial decision can remain honest about tradeoffs.

