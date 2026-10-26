---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:13"
section_title: "SoTA-Echoing (informative; not a center of gravity)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__015_sota-echoing-informative-not-a-center-of-gravity.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:13 — SoTA-Echoing (informative; not a center of gravity)"
line_start: 38464
line_end: 38483
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

These source lines inform candidate methods. Their use still requires the selected quantity, fold and admission conditions; the examples do not establish a universally preferred aggregation.



| SoTA practice pointer (post‑2015+) | Primary source | Where it connects | Adoption status |
|---|---|---|---|
| Permutation‑invariant set aggregation as a *method family* (set → summary) | Zaheer et al., “Deep Sets” (2017) [A19ULSAM-1] | Candidate `ΓFold` families can include permutation‑invariant folds; ULSAM keeps them admissibility-gated and policy-pinned. | **Adapt** (keep admissibility/pins explicit; do not treat learned folds as implicit defaults). |
| Attention-based permutation‑invariant set aggregation as a *method family* | Lee et al., “Set Transformer” (2019) [A19ULSAM-4] | Alternative learnable set folds (pooling by attention); still requires explicit policy binding and admissibility gating. | **Adapt** (publish as method family in SoTA pack; pin editions/policies; keep kernel unchanged). |
| Choosing a risk-aware objective under distributional uncertainty | Rahimian & Mehrotra, “Distributionally Robust Optimization: A Review” (2019) [A19ULSAM-2] | The optimization framework is not itself a fold over these measures. A receiving application identifies the particular risk quantity and operation, then establishes its aggregation law and conditions. | **Adapt** (policy‑bound and SCP/CSLC‑gated). |
| Governing-pattern discipline for architectural statements | ISO/IEC/IEEE 42010:2022 [A19ULSAM-3] | FPF adapts architecture-description distinctions to explicit governing-pattern references; the one-pattern assignment is an FPF design choice. | **Adapt** (local FPF pattern assignment, not a rule attributed to the standard). |

[A19ULSAM-1]: https://arxiv.org/abs/1703.06114 "Zaheer et al., Deep Sets, 2017"
[A19ULSAM-2]: https://arxiv.org/abs/1908.05659 "Rahimian & Mehrotra, Distributionally Robust Optimization: A Review, 2019"
[A19ULSAM-3]: https://www.iso.org/standard/74393.html "ISO/IEC/IEEE 42010:2022 — Systems and software engineering — Architecture description"
[A19ULSAM-4]: https://arxiv.org/abs/1810.00825 "Lee et al., Set Transformer, 2019"

