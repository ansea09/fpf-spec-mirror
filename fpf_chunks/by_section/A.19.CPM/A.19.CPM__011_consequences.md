---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator"
section_id: "A.19.CPM:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__011_consequences.md"
commit_sha: "dba39812b83cac74dd2a3251c134cdc23dfaec86"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator"
  - "A.19.CPM:9 — Consequences"
line_start: 40731
line_end: 40738
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass\\"
---

### A.19.CPM:9 - Consequences

* **Improved usability:** CPM gives a single, engineer‑readable place to learn “what admissible comparison means” and what it does *not* mean.
* **Higher replayability:** comparison results remain traceable through the `Compare` application and its `ComparisonResultSlot` binding, any consumed obtaining F.9 `Bridge` with its separate bounded-use claim, and any ReferencePlane relation and policy. Recover dated comparison `U.Work` and the A.10 evidence-provenance path when the account asserts them or the receiving use consumes them.
* **Reduced semantic drift:** teams cannot silently shift from Pareto to lexicographic to “weighted sum” without changing explicit comparator specs and pins.
* **Explicit tradeoffs:** set-valued outcomes retain incomparability and uncertainty for downstream reasoning.
* **Cost:** downstream consumers (notably selection) must handle sets, abstentions, and partial orders explicitly. This moves complexity from hidden heuristics into explicit policy‑bound mechanisms.

