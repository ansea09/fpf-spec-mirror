---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:7"
section_title: "Source Record-Form Recovery"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__008_source-record-form-recovery.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:7 — Source Record-Form Recovery"
line_start: 48563
line_end: 48576
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:7 - Source Record-Form Recovery

Source record names are recovered by use, not by label shape. This section prevents source prose from becoming local `C.22.2` subobjects.

| Source form family | `C.22.2` preservation | Governing pattern named by value for outside use |
|---|---|---|
| Problem card, problematization passport, problem-side note, or ordinary problem signal | Carry the problem signal, context grounding, scope cut, improvement check or acceptance probe, and next use. | `C.22.2` governs only the problem-side record shape; downstream selector-facing use remains with `C.22`. |
| Archive, portfolio, palette, front, shortlist, selected set, `LivePool`, set-return, or retained candidate | Preserve `setContextRef`, source-set kind, selection or retention criterion, budget or window when current, and non-scalar next use. | `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q` according to the relation named by value. |
| Characterization passport, characteristic card, parity plan, comparison note, rule-of-choice card, or acceptance-looking row | Preserve the cue, candidate criterion, comparator cue or window cue, and current reason the relation changes formulation. | `C.16`, `A.19`, `C.25`, `G.0`, `G.4`, `G.9`, or `C.11` according to the relation named by value. |
| Evidence pack, provenance note, assurance row, gate log, autonomy budget, runbook, rollback plan, method selection, work plan, performed-work note, result record, or result measurement | Preserve only the problem-side cue, risk or validation boundary, source reference, and stop condition before that use. | `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, `G.5`, `A.15`, `C.16`, or `G.11` according to the claim named by value. |
| Candidate solution, described system, ordinary log, budget, ledger, protocol, plan, pack, or factory wording | Recover the use under repair: problem-side source material, problem-side source relation, selected-set material, work, evidence, gate, or autonomy material, or ordinary example. | Apply the governing pattern for the recovered relation; do not mint a local `C.22.2` kind from the label. |

The repair rule is short: if the source material supplies problem-side material, copy the material into the card's current fields. If it supplies another FPF-governed claim, keep only the local cue and apply the pattern that governs that claim.

