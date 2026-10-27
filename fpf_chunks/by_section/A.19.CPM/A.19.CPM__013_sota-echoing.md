---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator (CPM)"
section_id: "A.19.CPM:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__013_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator (CPM)"
  - "A.19.CPM:11 — SoTA-Echoing"
line_start: 38889
line_end: 38900
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

### A.19.CPM:11 - SoTA-Echoing

The following research lines inform comparator choices. Their methods require their own conditions; no source family alone establishes the CPM outcome or admission rule.

Concrete comparator-family SoTA packages are cited through their current Part G pack or claim sheet when one governs the use. CPM's kernel semantics remain unchanged.

| Research contribution                                                                                                   | How it connects to CPM                                                                                                                                           | Adoption status in FPF                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Fair ranking and constrained ranking** (e.g., Zehlike et al., 2017; Biega et al., 2018)                                             | Reinforces the “no hidden tie‑breaks and thresholds” stance: fairness constraints belong in explicit comparator and acceptance policies, not as silent kernel constants. | Integrate via `ComparatorSpec` editions in `CG‑Spec.ComparatorSet` + policy pins; CPM remains unchanged.              |
| **Uncertainty-aware and set-valued inference** (e.g., Romano et al., 2019; Barber et al., 2021)                                       | Prediction intervals or other uncertainty results retain their own semantics. A declared comparator determines which relation tokens follow; an interval is neither a CPM token set nor by itself a reason for abstention.                         | Model as comparator families (or supporting method families) packaged in `G.2`; wired into declared `ComparatorSpec`. |
| **Differentiable sorting and learned comparators** (e.g., Grover et al., 2019; Blondel et al., 2020) | When comparators are learned, explicit comparator specs, edition and policy bindings in the actual operation application, its `ComparisonResultSlot` binding, and A.10 evidence-provenance become even more important for replay and drift control. | Use a sorting or learned-comparison component only under a ComparatorSpec that establishes the returned relation semantics and required conditions; an algorithm label is insufficient. |

