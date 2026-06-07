---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__001_intro.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:intro — Intro"
line_start: 42941
line_end: 42956
dependencies:
  - "B.3"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

## C.19 - Explore–Exploit Governor (E/E‑LOG)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Explore-exploit governor.

**Intent.** Govern exploration/exploitation policy over still-live candidate pools so frontier treatment, graduation, narrowing, and sunset treatment stay explicit, auditable, and stated as one pool-policy result without taking over local choice, enactment, or publication questions.

**Export relation.** No `Γ` operators are exported; policies parameterize calls in `C.18 NQD-CAL`.

**Depends on.** `C.18 NQD-CAL` (generators), `C.17 Creativity-CHR` (measurements), `Decsn-CAL` (objectives/constraints and scalarization lenses), `B.3` (trust adjustments), and `Compose-CAL` (set aggregation; advisory).

**Coordinates with.** `C.11` for local choice among already-available options, `C.24` for enactment planning after choice, `G.5` for selector-facing publication, `C.17`, and `G.9`.

