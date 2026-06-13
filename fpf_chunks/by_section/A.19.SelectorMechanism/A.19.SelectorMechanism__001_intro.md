---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__001_intro.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:intro — Intro"
line_start: 28067
line_end: 28086
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

## A.19.SelectorMechanism - Unified Selection Kernel, SelectorMechanism

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism-governing patterns (Phase‑3)
> **Source:** FPF / CHR Phase‑3 mechanism-governing patterns
> **Modified:** 2026‑01‑20
>
> **Governing-pattern note (Phase‑3 canonicalization):** this pattern governs the canonical `U.Mechanism.Intension` for `SelectorMechanism.IntensionRef` (CHR suite stage `select`). Mechanism-intension semantics are governed by explicitly designated governing patterns (`E.20:4.2`).
> `A.6.1` governs the **template** of `U.Mechanism.Intension` and the `U.MechAuthoring` discipline; this pattern governs the **SelectorMechanism-specific** slots, operations, laws, admissibility, applicability, transport, plane, time, and audit obligations for that template.
>
> **ID continuity note.** When migrating away from any legacy “card location”, preserve public anchors: keep the legacy section heading/ID as a **Tell + Cite stub** (or dock aliases via `F.18`) rather than deleting or silently renaming it.
>
> **Canonicalization hook (ID‑continuity‑safe):** any other appearances of the SelectorMechanism intension content (e.g., a legacy grounding stub in `A.6.1` or suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.SelectorMechanism:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
> Such stubs MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility / Audit content (no “second center of gravity” via near‑duplicate prose).
> * **ID‑continuity‑safe:** if content is moved from an earlier location, preserve the earlier heading and its IDs as a stub that cites `A.19.SelectorMechanism:4.1`.
> * **Alias‑dock, don’t break:** if any legacy tokens exist (e.g., a historical `UNSELM` name token), dock them via `F.18` + E.10 rules; do not mint a competing head.
> * **No shadow semantics:** derived summaries MAY be informative, but MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility / Audit; they may only summarise and cite.

