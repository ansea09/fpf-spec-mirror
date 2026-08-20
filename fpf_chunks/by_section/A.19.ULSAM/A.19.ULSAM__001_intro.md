---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__001_intro.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:intro — Intro"
line_start: 32356
line_end: 32375
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UINDM"
  - "A.19.ULSAM"
  - "A.19.USCM"
keywords:
  - "CG-Spec.SCP"
  - "CG-Spec.Γ_fold"
  - "MinimalEvidence"
  - "fold_Γ?"
  - "lawful aggregation"
  - "scale-lawful fold"
  - "tri-state guard (pass"
  - "ΓFoldRef"
---

## A.19.ULSAM - Unified Lawful Scale Aggregation Mechanism (ULSAM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism-governing patterns (Phase‑3)
> **Source:** FPF / CHR Phase‑3 mechanism-governing patterns
> **Modified:** 2026-01-20

**Governing-pattern note (Phase‑3 canonicalization):** this pattern governs the canonical `U.Mechanism.Intension` for `ULSAM.IntensionRef` (CHR suite stage `fold_Γ?`). Mechanism-intension semantics are governed by explicitly designated governing patterns (`E.20`).
`A.6.1` governs the **template** of `U.Mechanism.Intension` and the `U.MechAuthoring` discipline; this pattern governs the **ULSAM-specific** slots, operations, laws, admissibility, and audit obligations for that template.

**ID continuity note.** When migrating away from any legacy “card location”, preserve public anchors: keep the legacy section heading/ID as a **Tell + Cite stub** (or dock aliases via `F.18`) rather than deleting or silently renaming it.

**Canonicalization hook (ID‑continuity‑safe):** any other appearances of ULSAM intension content (e.g., a legacy grounding stub in `A.6.1` or suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.ULSAM:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
Such stubs MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility content (no “second center of gravity” via near‑duplicate prose).
* **ID‑continuity‑safe:** if content is moved from an earlier location, preserve the earlier heading and its IDs as a stub that cites `A.19.ULSAM:4.1`.
* **Alias‑dock, don’t break:** if any legacy tokens exist, dock them via `F.18` + E.10 rules; do not silently replace tokens “by смысл”.
* **No shadow semantics:** derived summaries MAY be informative, but MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility; they may only summarise and cite.

