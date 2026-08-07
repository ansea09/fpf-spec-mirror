---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__002_use-this-when.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:0 — Use this when"
line_start: 29104
line_end: 29127
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

### A.19.SPR:0 - Use this when

Use `A.19.SPR` when state-family wording has FPF-governed use but does not yet say what is in which state, according to which state frame or governing pattern, with which value or classification, for which admissible use.

Typical triggers:

- `state`, `status`, `posture`, `readiness`, `stance`, `currentness`, `validity`, `degraded`, `accepted`, `admissible`, `blocked`, `candidate`, `stable`, `ready`, or close compounds;
- local fields such as `source posture`, `evidence posture`, `assurance posture`, `publication posture`, `release posture`, `validation posture`, `readiness posture`, or `support posture`;
- precision-looking local fields such as `LensUseAdmissibilityValue`, `dynClaimPosture`, or a specification-use label when their bearer, value set, governing pattern, use boundary, or reopen condition is not recoverable.

**What goes wrong if missed.** A broad state word becomes a miniature hidden ontology. A source gets called "current", "supporting", or "accepted" without a source-use relation. Evidence becomes assurance. A publication face becomes gate passage. A lens-use label becomes empirical truth. An external administrative status leaks into pattern prose. A readiness word implies work may proceed without the threshold, evidence path, gate, or decision record that would carry that claim.

**What this buys.** The reader can recover the state-like claim named by value, the governing pattern, the allowed use, and the blocked adjacent overread before acting on the word.

**First useful move.** Ask: what bearer has which state-like value under which state frame or governing pattern? If that cannot be answered, demote the wording to ordinary prose, quote-only source wording, a reduced-use cue, or a blocker.

**Not this pattern when.**

- If the pattern governing the recovered claim and state-like field are already recoverable by value, use that pattern directly.
- If the wording is ordinary prose and carries no FPF-governed use, keep it ordinary.
- If the state-like claim concerns one `Characteristic`, `Scale`, coordinate, score, or metric, use `C.16.P` before state-family repair.
- If the state-like claim concerns source-expression, publication, carrier, or source-use wording, use `C.2.P` first; return to `A.19.SPR` only if a state-like claim remains.
- If the claim being made is relation construction, architecture or structure wording, quality-term or evaluative characterization, function-like wording, or naming, use `A.6.P`, `C.30.P`, `C.16.Q`, `A.6.F`, or `F.18` as selected by `E.10`.

