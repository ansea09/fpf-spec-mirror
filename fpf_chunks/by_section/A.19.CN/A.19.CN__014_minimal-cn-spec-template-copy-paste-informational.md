---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:13"
section_title: "Minimal CN‑Spec template (copy/paste, informational)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__014_minimal-cn-spec-template-copy-paste-informational.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:13 — Minimal CN‑Spec template (copy/paste, informational)"
line_start: 38273
line_end: 38318
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "loss evidence"
  - "maintained editions"
  - "normalization refs"
  - "optional CL"
  - "semantic relations"
  - "separate use claims"
  - "Γ-fold governance"
---

### A.19.CN:13 - Minimal CN‑Spec template (copy/paste, informational)

This example arranges the information needed to specify the comparison basis. A.19.UNM defines normalization terms; A.19.UINDM defines indicatorization; C.16 governs measurement and evidence backing; G.0 supplies the applicable admission conditions.

```
CN‑frame: <Name>      Edition: <edition>      Bearer: <bearer ref>
ComparisonBasis: <corpus, baseline, reference state, or declared comparison set>
ScopeAndWindow: <scope ref and qualification interval, when used>
IntendedUse: <claim, comparison, admission, or aggregation use>
characteristics:
  - <CharacteristicName> : <Scale; Unit when applicable>  [Polarity, when used: <preference rule>]
Chart:
  reference_state: <text>
  coordinate_patch: <domain/subset>
  measurement_protocol_ref?: <applicable measurement MethodDescriptionId>
  value_ascription_basis?: <applicable evaluation rule and evidence>
Normalization (when used):
  UNM: <UNMId?>
  methods: [<NormalizationMethodId>… ]
  method_descriptions: [<NormalizationMethodDescriptionRef>… ]
  invariants: [<property>… ]           # what the selected transformation preserves; name losses too (A.19.UNM)
  fix?: <NormalizationFixSpec>          # only for an established class whose receiving use needs a representative (A.19.UNM)
Indicators (optional):
  policy_ref: <IndicatorChoicePolicyRef>
  resulting_indicators: [<IndicatorId>… ] // selection is policy‑defined; NCVs alone do not make an Indicator (see A.19.UINDM)
Comparability:
  mode: coordinatewise | normalization-based
  minimal_evidence: <basis required for this comparison>  # admission conditions under G.0; measurement/evidence backing under C.16
Aggregation (when used):
  fold: <Γ_fold expr>   time_policy: <window, statistic>
  WLNK/COMM/LOC/MONO: <only selected property claims, with their model and applicability basis>
Acceptance:
  checklist: [<observable criterion>… ]
  window?: <qualification interval when required>
  evidence_anchors: [<required observation, evaluation or other support refs>… ]
Alignment (optional):
  semantic_uses: [<obtaining Bridge, separate use claim, required reliance, kept/lost distinctions, applicable guards, optional CL>… ]
  plane_relations: [<applicable plane relation>… ]
MaintenanceAndDeprecation (for a maintained edition):
  responsibility: <responsible holder or maintenance arrangement>
  DRR_links?: [<DRR ids for decisions that need them>… ]
  deprecation_plan: <short note>
```

When producing a `StateAssertion`, an implementation should be able to cite the CN-Spec edition and evidence anchors used, along with any normalization instance and Bridge on which the assertion depends.

