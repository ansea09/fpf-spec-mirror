---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:13"
section_title: "SoTA-Echoing (informative; not a center of gravity)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__015_sota-echoing-informative-not-a-center-of-gravity.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:13 — SoTA-Echoing (informative; not a center of gravity)"
line_start: 32081
line_end: 32102
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

### A.19.ULSAM:13 - SoTA-Echoing (informative; not a center of gravity)

SoTA here is treated as **method-family source publications and `G.2` claim sheets to be wired** through `G.*:Ext.*` wiring, not as kernel semantics. ULSAM’s contribution is the stable boundary: explicit, admissible, auditable folding.

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable mechanism boundary.

**Pack note (Phase‑3):** this pattern does not currently cite a ULSAM‑specific `G.2` SoTA pack/ClaimSheet. If/when such a pack is introduced, replace the bibliographic pointers below with the pack’s `ClaimSheetId` citations, keeping the mechanism semantics unchanged.

| SoTA practice pointer (post‑2015+) | Primary source | Where it connects | Adoption status |
|---|---|---|---|
| Permutation‑invariant set aggregation as a *method family* (set → summary) | Zaheer et al., “Deep Sets” (2017) [1] | Candidate `ΓFold` families can include permutation‑invariant folds; ULSAM keeps them admissibility-gated and policy-pinned. | **Adapt** (keep admissibility/pins explicit; do not treat learned folds as implicit defaults). |
| Attention-based permutation‑invariant set aggregation as a *method family* | Lee et al., “Set Transformer” (2019) [4] | Alternative learnable set folds (pooling by attention); still requires explicit policy binding and admissibility gating. | **Adapt** (publish as method family in SoTA pack; pin editions/policies; keep kernel unchanged). |
| Robust aggregation under uncertainty/outliers as a *policy-selectable fold family* | Rahimian & Mehrotra, “Distributionally Robust Optimization: A Review” (2019) [2] | Treat “worst‑case / risk‑aware” folds as explicit Γ‑fold options (policy-bound), not as hidden safety margins. | **Adapt** (policy‑bound and SCP/CSLC‑gated). |
| Governing-pattern discipline for architectural statements | ISO/IEC/IEEE 42010:2022 [3] | Supports the “one governing pattern” rule: ULSAM intension content lives here; other places cite. | **Adopt** (principle-level; applied to FPF pattern governing-pattern assignment). |

**Reminder.** “SoTA” means best known methods; it is not a synonym for “popular right now”. SoTA material should be curated and versioned in SoTA packs and connected via wiring modules, not embedded into kernel mechanism signatures.

[1]: https://arxiv.org/abs/1703.06114 "Zaheer et al., Deep Sets, 2017"
[2]: https://arxiv.org/abs/1908.05659 "Rahimian & Mehrotra, Distributionally Robust Optimization: A Review, 2019"
[3]: https://www.iso.org/standard/74393.html "ISO/IEC/IEEE 42010:2022 — Systems and software engineering — Architecture description"
[4]: https://arxiv.org/abs/1810.00825 "Lee et al., Set Transformer, 2019"

