---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:6"
section_title: "Conformance checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__010_conformance-checks.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:6 — Conformance checks"
line_start: 29790
line_end: 29821
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UNM"
  - "A.2.6"
  - "A.6.5"
  - "B.1"
  - "C.16"
  - "C.2.1"
  - "E.24"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.4"
  - "U.ClaimScope"
  - "U.ContextSlice"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
  - "system-role–Method–Work assertions stay outside A.19"
---

### A.19:6 - Conformance checks

Start with the base declaration. If the current job is only to declare a local space, or that space plus one predicate, stop after these checks.

**Base declaration**

1. The ordered basis names every slot's Characteristic, Scale, admissible value set, position, and subject/input signature.
2. A complete point contains one genuine Coordinate from each Scale. Missing, censored, unknown, and inapplicable inputs remain separate observation or evaluation statuses.
3. No order, topology, distance, normalization, indicator, aggregation, or comparison is implied. Any one that is present is named explicitly.
4. When a `CharacteristicSpacePredicate` is present, its input variable, domain, Coordinate projection, Boolean expression, cut or band, composition, and polarity are recoverable. A binary comparison remains separate.
5. The declaration contains no hidden evaluation result, gate decision, evidence relation, publication object, or permission to act.

**Triggered additions**

Apply a row only when its trigger is present.

| Trigger | Additional check |
| --- | --- |
| Subspace or product | List the carried slots and Scale meanings. Projection uses the type-correct composition law; a product performs no aggregation. |
| Embedding or lossy mapping | An embedding is point-injective and preserves every named structure. A many-to-one normalization, binning, dropped Coordinate, or other coarse-graining is a lossy mapping or projection with preserved and lost distinctions stated. |
| Normalization, quotient, equality, or join across spaces | Cite the admissible A.19.UNM instance, Scale conditions, domain, and validity window. Compare in one declared target space. Use a quotient or fixed chart when the claimed equality or join depends on normalization invariance; otherwise report the values as incomparable. |
| Same-space state comparison | Compare Coordinates directly only when both states use the same declared space, slot meanings, Scale metadata, and state definition. A.19.CPM separately binds the comparator, scope, plane, window, application, and result. |
| Indicator use | Cite the `IndicatorChoicePolicy`; a normalized value is not automatically an indicator. |
| Cross-reference-scheme or cross-plane use | Cite an F.9 Bridge only for two exact F.17 local senses when its predicate obtains, and state the bounded-use claim separately; `CL` is optional. Cite the applicable plane relation separately. Name matching, context/scheme/plane difference, and an expired mapping establish neither relation nor admissibility. |
| Predicate evaluation or state assertion | Bind the actual subject/input tuple and available Coordinates or governed projection. The consumer separately states its scope, relevant slice, reference scheme and plane, applicability or evaluation window, operation application, typed result, and partial-input rule. |
| Changed predicate, mapping, or overlay | Keep earlier assertions tied to the earlier values. A new declaration does not retroactively rewrite a historical assertion or result. |
| Sensitivity, robustness, continuity, stability, or order-preservation claim | Name the exact function or predicate use, overlay, domain, assumptions, and bound or law required by the consumer's policy. Add C.16 uncertainty and calibration limits when measured Coordinates are relied on. |
| Dynamics prediction used in comparison or gating | Apply A.3.3 and the direct consumer's policy for model edition, domain, horizon, currentness, error or uncertainty, observation, sensitivity, stability, and normalization-composition conditions. No one regularity property grants authority. |
| Gate, permission, evidence, or assurance use | Use the direct gate, authority, evidence, and assurance patterns for their applications and results. A.19 contributes only the cited space, predicate, mapping, or overlay and requires no persistence identifier or log by itself. |

Choose the needed expression form through C.2.3. Automation or assurance can require more explicit identifiers and records under their direct patterns, but it does not enlarge the base A.19 declaration.

