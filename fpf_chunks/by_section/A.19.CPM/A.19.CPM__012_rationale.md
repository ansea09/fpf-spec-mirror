---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator"
section_id: "A.19.CPM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__012_rationale.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator"
  - "A.19.CPM:10 — Rationale"
line_start: 40780
line_end: 40787
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

### A.19.CPM:10 - Rationale

1. **Set‑valued by design:** partial orders are common in multi‑criteria settings; pretending they are total creates false certainty and brittle decisions.
2. **ComparatorSet gating:** declaring which comparisons are admissible, and under what scale or evidence rules, prevents “algorithm by convenience”.
3. **Tri‑state guards:** explicit `pass|degrade|abstain` keeps unknown from being converted into an outcome.
4. **Comparison, scoring and selection remain separate:** separating compare from score and select prevents hidden semantic coupling and improves evolvability (methods change via wiring; kernel stays stable).
5. **Single governing pattern:** one governing definition lets other descriptions cite the comparison semantics they use.

