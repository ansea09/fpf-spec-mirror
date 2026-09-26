---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:11"
section_title: "SoTA-Echoing — choose indicators for their intended use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__013_sota-echoing-choose-indicators-for-their-intended-use.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:11 — SoTA-Echoing — choose indicators for their intended use"
line_start: 35362
line_end: 35373
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:11 - SoTA-Echoing — choose indicators for their intended use

**Practice question.** Which coordinates should a dashboard or receiving method use when several available columns are plausible indicators? The selected line makes the phenomenon and intended use govern an explicit choice policy, then checks the selected positions and their Scale meanings. A serious alternative ranks available features by a statistical score and keeps the best k. That alternative is useful for its declared predictive or exploratory objective; its ranking alone does not decide which quantities a particular dashboard must report.

The European Commission JRC's [10 Step Guide, steps 1–2](https://knowledge4policy.ec.europa.eu/composite-indicators/toolkit_en/navigation-page/10-step-guide_en), published as a navigation guide in March 2025, supplies the purpose-led line for composite indicators: define the conceptual basis and choose relevant, analytically sound, obtainable indicators. **Adapt** that ordering to `CN-Spec.indicator_policy`, the IndicatorChoicePolicy argument in §4.1 and the selection-only law. UINDM selects existing coordinates; the guide's later normalization, weighting and aggregation steps belong to their separately declared mechanisms. The guide does not prove that any particular policy is adequate or stable under distribution shift.

The [scikit-learn SelectKBest documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html) supplies the concrete statistical alternative: choose k features using a declared scoring function; equal scores can be resolved in an unspecified way. **Adopt** statistical selection when the intended use actually chooses that criterion, with the data, scoring rule and treatment of ties declared in the policy. **Reject** substituting a top-k result for an undeclared semantic choice. The documentation establishes the selector's behavior, not the meaning or fitness of the selected indicators.

The two Temperature positions in §5.4 expose the distinction. Suppose the Celsius and kelvin columns receive equal statistical scores and k=1. Either could be retained under an unspecified tie rule, while the downstream Celsius scoring method accepts only the Celsius position. At comparable effort, the explicit Celsius policy resolves the required input directly; when prediction is the real objective, the statistical policy can instead choose a position and bind its actual Scale to an appropriate receiving method. This changes checklist items 3–4 in §7: retain the exact selected position, and resolve an action-changing tie by the policy or return its unresolved result. A promise that both columns concern Temperature is insufficient.

The trade-off is deliberate: a purpose-led policy makes the required indicator meaning inspectable, but it does not by itself optimize prediction. A statistical policy needs data and a justified score, and its selected subset can vary with them. Neither approach permits UINDM to silently rescale values. Reopen the comparison when the receiving question changes, evidence shows that the selected indicators fail that question, or a rival policy preserves the needed meaning with better usefulness at comparable effort.

