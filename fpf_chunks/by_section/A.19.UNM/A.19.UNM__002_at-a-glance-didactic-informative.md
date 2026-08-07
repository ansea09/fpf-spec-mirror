---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Unified Normalization Mechanism (UNM)"
section_id: "A.19.UNM:0"
section_title: "At a glance — didactic, informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__002_at-a-glance-didactic-informative.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.19.UNM — Unified Normalization Mechanism (UNM)"
  - "A.19.UNM:0 — At a glance — didactic, informative"
line_start: 31434
line_end: 31463
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:0 - At a glance — didactic, informative

**Intent.** Provide a single, explicit normalization mechanism for **coordinate values** in a `U.CharacteristicSpace`, so that **comparability** and downstream characterization steps can be stated as “**normalize-then-compare**” (governance), rather than as hidden arithmetic inside scoring/selection.

**Where it sits.**
- **CN-frame governance card:** `CN_Spec.normalization` + `CN_Spec.comparability.mode` route whether comparison is `coordinatewise` or `normalization-based`.
- **CHR suite role:** stage `normalize` (first-stage, when enabled by the suite protocol / comparability routing).

**Key outputs.**
- `NCV` (NormalizedCharacteristicValue) values for coordinates.
- A declared congruence `≡_UNM` (equivalence) induced by a chosen normalization method instance.
- Optionally, an explicit representative selection policy (`NormalizationFixSpec`, aka “NormalizationFix” in prose) when quotient objects must be presented as concrete chart items.

**Two IDs (do not conflate).**
- `UNM_id?` selects the **UNM mechanism instance** used by this CN‑frame (a `U.Mechanism` instance of type UNM; routing/governance level).
- `NormalizationMethodInstanceId` selects the **normalization method instance** applied to specific coordinate(s), with its validity window and evidence pins (method/application level).

**Minimum declaration set (didactic).**
- In `CN_Spec.comparability`: set `mode`, and (when UNM participates in acceptance/comparison) set `minimal_evidence`.
- In `CN_Spec.normalization`: declare `UNM_id?`, `methods`, `instances`, `method_descriptions`, `invariants`, and (if representatives are required) `fix`.
- In Audit: cite the chosen `NormalizationMethodInstanceId`, `NormalizationMethodDescriptionRef.edition`, declared invariants, validity window, evidence pins, and any Bridge/CL/ReferencePlane pins (plus the edition pin `UNM.TransportRegistryΦ/Phi` when transport is invoked).

**Non-goals.**
- Not indicator selection (that is **UINDM**).
- Not scoring, aggregation, comparison, selection (USCM / ULSAM / CPM / SelectorMechanism).
- Not a data governance system: UNM is a concept-level mechanism with an explicit governing pattern and auditability.

**Governing-pattern note (Phase‑3 canonicalization).**
This pattern is the governing pattern for the canonical `U.Mechanism.Intension` for `UNM.IntensionRef`. Other locations that currently carry UNM “card fragments” should be reduced to **Tell + Cite** stubs pointing here, preserving public IDs/anchors.

