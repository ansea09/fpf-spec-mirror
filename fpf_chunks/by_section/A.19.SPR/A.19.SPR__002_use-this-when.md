---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__002_use-this-when.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:0 — Use this when"
line_start: 30158
line_end: 30182
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

Use this pattern when a phrase such as “the system is ready”, “the source is current”, or “the evidence status is incomplete” matters to an FPF claim but does not yet say which item the sentence is about, what is true of it, or which rule makes that statement meaningful.

**What goes wrong if missed.** A short status word starts carrying several claims at once. A source label becomes evidence, a readiness label becomes gate passage, or a project-side status leaks into pattern guidance.

**First question.** Ask:

> What exact item is this sentence about, what does it say about that item, and which rule or criterion gives the statement its meaning?

**Cheap direct repair.** Write the answer as one ordinary technical sentence. Name the item, the actual value, relation, result, or claim, and the rule or criterion only when the reader needs it to understand or act. If that sentence is clear and safe for the intended use, stop. Do not create a repair note or list every claim the sentence does not make.

**What this buys.** A reader can understand the statement and its next practical use without learning a hidden status vocabulary.

Typical triggers include `state`, `status`, `posture`, `stance`, `currentness`, `validity`, `stable`, `accepted`, `blocked`, `candidate`, `degraded`, `readiness`, `ready`, and similar compounds. A precise-looking field such as `LensUseAdmissibilityValue` or `dynClaimPosture` is also a trigger when its object, possible values, or rule cannot be recovered.

**Not this pattern when.**

- If the exact item, claim or value, and applicable rule are already clear, use that rule directly.
- If `readiness` or `ready` still hides whether the sentence concerns a subject state, assignment condition, work entry, gate decision, publication use, permission, or performed Work, use `E.10.MOVE` first.
- If the wording is ordinary prose and carries no FPF-governed claim, keep it ordinary.
- If one `Characteristic`, Scale, Coordinate, score, or measurement construction is hidden, use `C.16.P` first.
- If a source expression, publication, carrier, or source-use relation is hidden, use `C.2.P` first and return here only if a state-wording problem remains.
- For relation, architecture, quality, function, or naming problems, use `A.6.P`, `C.30.P`, `C.16.Q`, `A.6.F`, or `F.18` as selected by `E.10`.

