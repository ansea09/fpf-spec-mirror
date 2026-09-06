---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__005_forces.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:3 — Forces"
line_start: 34159
line_end: 34167
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

### A.19.CPM:3 - Forces

1. **Usability vs correctness:** engineers want a "simple compare" function; correctness demands explicit admissibility, explicit comparator choice, and explicit handling of incomparability and unknown evidence.
2. **Total order convenience vs partial order truth:** total orders simplify downstream selection; partial orders are often the faithful representation (especially in multi‑criteria settings).
3. **Evolvability vs stability:** comparator methods evolve (SoTA churn); kernel semantics and slot field sets must remain stable and wiring‑friendly.
4. **Replayability vs speed of discussion:** teams want fast decisions; replay requires the dated comparison `U.Work`, the actual `Compare` operation application with exact edition, policy, argument, and result bindings, and an A.10 evidence-provenance path.
5. **Cross-scheme reasoning vs Bridge and ReferencePlane discipline:** a comparison that relies on a semantic relation between two exact F.17 `SchemeSenseCell` values requires an obtaining F.9 `Bridge` and a separate C.2.1 bounded-use claim; a plane-only crossing requires the applicable ReferencePlane relation and policy. Neither branch supplies scope, predicate, plane, or time from an umbrella context label.
6. **Avoiding “second centers of gravity”:** mechanism semantics must have a governing pattern; otherwise the suite, `A.6.1` archetypes, and Part‑G wiring drift apart.

