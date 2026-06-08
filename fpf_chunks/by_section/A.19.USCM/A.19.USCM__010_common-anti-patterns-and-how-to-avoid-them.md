---
chunk_kind: "child"
pattern_id: "A.19.USCM"
pattern_title: "Unified Scoring Mechanism, USCM"
section_id: "A.19.USCM:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.USCM/A.19.USCM__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.19.USCM — Unified Scoring Mechanism, USCM"
  - "A.19.USCM:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 26742
line_end: 26759
dependencies:
keywords:
  - "CG-Spec.MinimalEvidence"
  - "CSLC-lawful transforms"
  - "ScaleComplianceProfile (SCP)"
  - "ScoringMethodDescription"
  - "score profile"
  - "scoring"
  - "tri-state admissibility (pass"
---

### A.19.USCM:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden normalization inside scoring.** Scoring silently normalizes or aligns measures. Avoid by making UNM explicit in choreography and keeping USCM’s `Score` legality‑only.

* **Weighted sum across mixed or non-admissible scales.** Treating “weights + sum” as universal. Avoid by requiring SCP+CSLC admissibility; if the scale operation is not scale-admissible, it is not admissible.

* **Silent scalarization.** Collapsing vector scores or partial orders into a single “overall score” via an untracked tie‑breaker. Avoid by leaving vector scores intact, and making scalarization an explicit declared commitment.

* **Implicit scoring method (“we just use the standard formula”).** The scoring method is assumed rather than declared and pinned. Avoid by requiring `ScoringMethodDescriptionSlot` and edition pinning in planned baseline; treat “identity scoring” (if ever needed) as an explicit method description, not a hidden default.

* **Unknown → 0 coercion.** Treating missing evidence as zero, false, or “good enough.” Avoid by tri‑state guards and explicit failure behavior, with auditable effective evidence policy.

* **Shadow CG‑Spec.** Hard‑coding legality rules inside a scoring method description instead of citing `CGSpecSlot.SCP`. Avoid by keeping legality in CG‑Spec and treating method details as wiring.

* **Telemetry or publish leakage.** Treating scoring as a reporting step. Avoid by keeping publish/telemetry outside suite closure and using the appropriate post-suite mechanisms.

* **SlotKind drift.** Renaming or re‑purposing slots across specializations or across mechanisms. Avoid by using the suite SlotKind lexicon and the `⊑/⊑⁺` discipline.

