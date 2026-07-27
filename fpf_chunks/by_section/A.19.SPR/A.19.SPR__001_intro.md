---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__001_intro.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:intro — Intro"
line_start: 28729
line_end: 28747
dependencies:
  - "A.10"
  - "A.16"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.P"
  - "C.27"
  - "C.29"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.8"
  - "E.9.DA"
  - "F.18"
keywords:
---

## A.19.SPR - State-Family Precision Restoration

> **Type:** State-family precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** State-wording repair.

**Intent.**
Recover `state`, `status`, `posture`, `readiness`, and close state-family wording whose bearer, state frame, value set, admissible use, or receiving FPF pattern is hidden.

This pattern does not define a general `Posture` kind. It repairs wording that acts like a state-like claim before a reader treats the word as evidence, assurance, gate passage, release permission, source authority, maturity, or work completion.

**Builds on.** `E.10`, `E.10.ARCH`, `A.19`, `A.3.3`, `C.2.2a`, `A.16.*`, `A.10`, `B.3`, `A.20`, `A.21`, `C.27`, `C.29`, `E.17`, `E.9.DA`, `E.21`, `F.18`, and project-side administrative, review, dispatch, release or admission, or source-control records when the state-like claim is administrative rather than FPF-content-bearing.

**Coordinates with.** `A.17`, `A.18`, `C.16`, `C.16.P`, `C.16.Q`, `A.6.P`, `C.2.P`, `C.30.P`, `E.8`, `E.19`, and `E.11`.

**E.10.ARCH governing-pattern relation.** When `E.10` encounters state-family wording such as `state`, `status`, `posture`, `readiness`, `stance`, `currentness`, `validity`, `stable`, `ready`, `accepted`, `blocked`, `candidate`, or close compounds whose bearer, state frame, value set, admissible use, validity window, reopen condition, or governing pattern is hidden, `E.10.ARCH` assigns the repair to `A.19.SPR` only until those values are recovered or the claim being made belongs to `C.2.P`, `A.10`, `B.3`, `A.20`, `A.21`, `C.27`, `C.29`, `E.9.DA`, `E.21`, `A.6.P`, `A.15`, or the project-side administrative, review, dispatch, release or admission, or source-control record.

