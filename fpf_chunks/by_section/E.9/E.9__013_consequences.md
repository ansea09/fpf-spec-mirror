---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__013_consequences.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:9 — Consequences"
line_start: 71633
line_end: 71641
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.9:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Complete audit trail** – every semantic normative change carries a structured “why”. | Adds deliberate friction; mitigated by CC‑DRR.5 (Δ‑0/Δ‑1 lightweight) and CC‑DRR.1a (pointer‑based DRRs). |
| **Higher decision quality** – Pillar, alternatives, scenario, and utility checks surface hidden conflicts early. | Authors must do more real content work up front; the gain is less downstream reinvention and less hidden deferral. |
| **Institutional memory** – prevents re‑litigation of rejected alternatives. | DRR archive grows; index stored in a non‑normative annex. |
| **Executable downstream authoring** - selected patterns and selected non-pattern FPF kind-reference pairs, outside-boundary, reusable-content decisions, selected-answer stability, and remaining validation evidence obligation are explicit enough for later drafting/landing without semantic invention. | Richer DRRs need discipline to avoid becoming shadow specs or process briefs; mitigated by CC-DRR.1b, CC-DRR.4a, CC-DRR.4b, CC-DRR.4c, and CC-DRR.4d. |

