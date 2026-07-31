---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__013_relations.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:12 — Relations"
line_start: 64828
line_end: 64837
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:12 - Relations

- **Builds on:** `C.32.HCS`, `C.32.ACS`, `C.16`, `C.16.P`, `C.25`, `E.13`, `E.22`, `E.23`, and `A.19.CPM`.
- **Receiving uses:** `C.32.P2S` actual-structure feedback and next-synthesis repair, `C.32` candidate synthesis, `C.32.MLAO` residual optimization, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair, `A.19.CPM` comparison, `A.19.SelectorMechanism` selection, `C.11` local choice, publication of a selected set under `G.5`, and architecture-decision work for `C.32.PAD`.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, uncertainty, or cross-case comparability claim is made.
- **Structural-information boundary:** `C.33`, `C.34`, and `C.35` can supply captured structure, lost structure, preservation adequacy, generated-carrier context, or discovered-carrier context for an eval only after `C.32.ACS`, `C.16`, or `C.25` has declared what is being evaluated. ACE remains eval-program and eval-result owner; `C.33`, `C.34`, and `C.35` do not define eval programs.
- **Q-Bundle boundary:** Use `C.25` when the evaluated item is a composite quality family.
- **Test boundary:** Use `test` only as an eval operation for a declared expectation or hard constraint. Error recognition and architecture-synthesis repair use `C.32.FAIL`; non-architecture defects use the local defect-governing pattern.
- **Decision boundary:** ACE can produce readings, ranks, dominance relations, trade-off-front descriptions, and source material for an A.10 evidence relation when an evidence claim is current. Explicit comparison, set-returning selection, local choice, publication of a selected set, and project architecture decision belong to `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, and `C.32.PAD`.

