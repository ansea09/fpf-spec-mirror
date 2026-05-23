---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__012_rationale.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:10 — Rationale"
line_start: 26689
line_end: 26696
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

### A.19.CPM:10 - Rationale

1. **Set‑valued by design:** partial orders are common in multi‑criteria settings; pretending they are total creates false certainty and brittle decisions.
2. **ComparatorSet gating:** declaring what comparisons are legal (and under what scale/evidence rules) prevents “algorithm by convenience”.
3. **Tri‑state guards:** explicit `pass|degrade|abstain` preserves epistemic honesty: unknown is not silently converted into an outcome.
4. **Strict distinction:** separating compare from score and select prevents hidden semantic coupling and improves evolvability (methods change via wiring; kernel stays stable).
5. **Governing-pattern canonicalization:** keeping one governing pattern eliminates “multiple near‑identical cards” that drift apart and destroy usability.

