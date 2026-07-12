---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__002_use-this-when.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:0 — Use this when"
line_start: 44742
line_end: 44758
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.20"
  - "A.21"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
  - "G.0"
  - "G.5"
  - "G.9"
keywords:
---

### C.16.P:0 - Use this when

Use this pattern when wording such as `axis`, `dimension`, `feature`, `property`, `metric`, `indicator`, `score`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, `rating`, `benchmark`, `quality coordinate`, or `architecture score` carries a characterization claim but does not yet show the recoverable construction.

**What goes wrong if missed.** A metric becomes a measure without a scale, a score becomes proof, `strong` becomes a verdict without a characteristic, a level becomes an undefined maturity status, an indicator becomes the thing indicated, or a benchmark result becomes gate passage or release permission.

**What this buys.** The reader can recover the bearer, characteristic, scale, value, score, unit, scoring method, indicator role, comparison reference or comparator set, threshold, admissible use, and governing pattern before treating a number, adjective, coordinate, or comparison as actionable.

**First useful move.** Ask which bearer, characteristic, scale, value or score construction is recoverable; then apply `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, or the neighboring pattern governing that claim instead of letting the compact word decide.

**Not this pattern when.**

- If the `Characteristic`, `Scale`, value set, scoring method, and admissible use are already recoverable, use `C.16`, `A.17`, `A.18`, or `A.19` directly.
- If the claim being made is a Q-bundle, quality-term or evaluative characterization, or pattern-quality coordinate, use `C.25`, `C.16.Q`, or `E.21` directly after any needed characteristic-scale repair.
- If the claim being made is mathematical-lens use, use `C.29`.
- If the claim being made is evidence, assurance, gate, work, decision, causal-use, release, benchmark harness, or project-side authority claim, use the governing pattern for that claim after characteristic and scale construction is recovered or blocked.

