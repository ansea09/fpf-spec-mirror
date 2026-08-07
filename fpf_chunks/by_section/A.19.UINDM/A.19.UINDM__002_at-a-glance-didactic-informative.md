---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Unified Indicatorization Mechanism (UINDM)"
section_id: "A.19.UINDM:0"
section_title: "At a glance (didactic, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__002_at-a-glance-didactic-informative.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.19.UINDM — Unified Indicatorization Mechanism (UINDM)"
  - "A.19.UINDM:0 — At a glance (didactic, informative)"
line_start: 31844
line_end: 31854
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:0 - At a glance (didactic, informative)

* **Suite stage:** `indicatorize` (ordering lives only in `A.19.CHR:suite_protocols`).
* **Inputs (conceptual):** base `U.CharacteristicSpaceRef` + `CNSpecRef` + `IndicatorChoicePolicyRef` + `U.BoundedContextRef`,
  with optional `CGSpecRef` (+ optional `MinimalEvidenceRef` override) when the chosen policy is evidence‑gated.
* **Output:** `IndicatorSetSlot` = a set of `U.CharacteristicRef` (chosen coordinates), not measurements.
* **Non‑goals:** does **not** normalize, score, compare, aggregate, threshold, publish, or emit telemetry; it only selects a subset under explicit policy.
* **P2W seam:** concrete edition/policy pins are bound in planned baseline plan items (`A.15.3` + `A.19.CHR:4.7.2`); executions only record effective refs/pins in `Audit`.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); unknown never coerces to `pass`.
* **Quick rule of thumb:** if `CN‑Spec.indicator_policy` is absent → `IndicatorizeEligibility = abstain` (fail‑closed); if the selected policy is evidence‑gated → `CGSpecRef` MUST be available and the effective MinimalEvidence MUST be explicit (override or `CG‑Spec.MinimalEvidence`).

