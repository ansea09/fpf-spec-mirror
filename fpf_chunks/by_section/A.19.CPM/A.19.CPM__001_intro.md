---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__001_intro.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:intro — Intro"
line_start: 32364
line_end: 32376
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

## A.19.CPM - Unified Comparison Mechanism (CPM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A, CN-Spec cluster (A.19), CHR mechanism-governing patterns
> **Source:** FPF, CHR mechanism-governing patterns
> **Modified:** 2026‑01‑20
>
> **Governing-pattern note:** this pattern governs the canonical `U.Mechanism.Intension` for `CPM.IntensionRef` (CHR suite stage `compare`). Mechanism-intension semantics are governed by explicitly designated governing patterns (`E.20`).
> `A.6.1` governs the **template** of `U.Mechanism.Intension`; this pattern governs the **CPM-specific constraints** over the SlotKind field set supplied by the suite: operations, laws, admissibility, applicability, transport, plane, and audit obligations for that template. It is not a second schema and does not govern the CHR SlotKind lexicon.
> Other descriptions of CPM cite `A.19.CPM:4.1` rather than restating SlotIndex, OperationAlgebra, LawSet, AdmissibilityConditions, Applicability, Transport, time policy, plane regime, or audit content.

