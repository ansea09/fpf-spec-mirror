---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__013_relations.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:12 — Relations"
line_start: 64857
line_end: 64866
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
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

- **Builds on:** `C.32.HCS`, `C.32.ACS`, `C.16`, `C.16.P`, `C.25`, `A.2.6`, `A.19`, `E.13`, `E.22`, `E.23`, and `A.19.CPM`; coordinates with A.3.1, A.3.2, A.15.2, A.15.1, and A.6.1 only for separately current Method, MethodDescription, planned Work, dated Work, or operation-application claims.
- **Receiving uses:** `C.32.P2S` actual-structure feedback and next-synthesis repair, `C.32` candidate synthesis, `C.32.MLAO` residual optimization, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair, `A.19.CPM` comparison, `A.19.SelectorMechanism` selection, `C.11` local choice, selected-set result declaration under `G.5`, source-backed publication-face and source-return work under `E.17`, publication-occurrence and audience-availability work under `E.24.PUB`, and architecture-decision work for `C.32.PAD`.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, uncertainty, or cross-case comparability claim is made.
- **Structural-information boundary:** `C.33`, `C.34`, and `C.35` can supply captured structure, lost structure, preservation adequacy, generated-carrier context, or discovered-carrier context for an eval only after `C.32.ACS`, `C.16`, or `C.25` has declared what is being evaluated. Use C.32.ACE for the eval-program frame, and accept each actual typed result under its own measurement, comparison, evaluation, or assertion definition and test. `C.33`, `C.34`, and `C.35` do not define eval programs.
- **Q-Bundle boundary:** Use `C.25` when the evaluated item is a composite quality family.
- **Test boundary:** Use `test` only as an eval operation for a declared expectation or hard constraint. Error recognition and architecture-synthesis repair use `C.32.FAIL`; non-architecture defects use the local defect-subject pattern.
- **Decision boundary:** An evaluation framed by an ACE record may reference separately admitted readings, ranks, dominance relations, trade-off-front descriptions, and other typed results. When such a result is current, identify the admitted System, dated evaluation Work, applicable operation application, and the definition and test used for that exact measurement, comparison, evaluation, or assertion result. Such a result may serve as source material for an A.10 evidence relation when an evidence claim is current. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for a project architecture decision. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.

