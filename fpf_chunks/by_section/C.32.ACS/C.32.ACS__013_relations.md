---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__013_relations.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:12 — Relations"
line_start: 59573
line_end: 59584
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19.CPM"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "anti-Goodhart guard"
  - "architecture characteristic criteria set"
  - "criteria row"
  - "improvement cycle"
  - "protected counter-characteristic"
  - "proxy risk"
---

### C.32.ACS:12 - Relations

- **Builds on:** `C.32.HCS`, `A.17`, `A.18`, `C.16`, `C.16.P`, `C.25`, `C.30`, `C.30.P`, `C.31`, `C.31.ASAP`, `E.13`, `E.22`, and `E.23`.
- **Receiving uses:** `C.32.P2S` problem-to-structure architecturing flow, `C.32` candidate synthesis, `C.32.MLAO` multilevel residual work, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair cues, `C.32.ACE` eval programs, `A.19.CPM` comparison inputs, `A.19.SelectorMechanism` selection inputs, `C.11` local choice inputs, inputs for publishing a selected set under `G.5`, and architecture-decision inputs for `C.32.PAD`.
- **Starter-pack boundary:** Use `C.32.HCS` when the project needs a holon-family starting set before criteria rows exist.
- **Q-Bundle boundary:** Use `C.25` when the architecture characteristic is really a composite quality family with several measures, scope slots, mechanisms, statuses, qualification windows, or evidence.
- **Eval boundary:** Use `C.32.ACE` when a project wants an eval program over declared rows, Q-Bundle slots, candidates, or selected-structure changes.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, or cross-case comparability claim is made.
- **Proxy boundary:** Use `E.13` when an optimization indicator, score, eval result, or dashboard state begins to replace the declared architecture concern.
- **Synthesis boundary:** Use `C.32` after criteria rows exist and the next useful work is to synthesize candidate selected-structure changes.
- **Decision and publication boundary:** Use `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, and `C.32.PAD` when comparison, selection, choice, publication of a selected set, or architecture decision is being made.

