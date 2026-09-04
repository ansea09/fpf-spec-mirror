---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__013_relations.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:12 — Relations"
line_start: 64634
line_end: 64647
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
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

- **Builds on:** `C.32.HCS`, `A.17`, `A.18`, `A.2.6`, `A.19`, `C.16`, `C.16.P`, `C.25`, `C.30`, `C.30.P`, `C.31`, `C.31.ASAP`, `E.13`, `E.22`, and `E.23`; uses A.1.1 only when a selected `BoundedModelUseStructure` changes one row's interpretation.
- **Receiving uses:** `C.32.P2S` problem-to-structure architecturing flow, `C.32` candidate synthesis, `C.32.MLAO` multilevel residual work, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair cues, `C.32.ACE` eval programs, `A.19.CPM` comparison inputs, `A.19.SelectorMechanism` selection inputs, `C.11` local choice inputs, inputs for selected-set result declaration under `G.5`, source-backed publication-face and source-return inputs under `E.17`, publication-occurrence and audience-availability inputs under `E.24.PUB`, and architecture-decision inputs for `C.32.PAD`.
- **Starter-pack boundary:** Use `C.32.HCS` when the project needs a holon-family starting set before criteria rows exist.
- **Q-Bundle boundary:** Use `C.25` when the architecture characteristic is really a composite quality family with several measures, scope slots, mechanisms, statuses, qualification windows, or evidence.
- **Scale-preference boundary:** Use `C.31.ASAP` when a project claims that one architecture alternative is preferable over another under a declared scale window; the ACS row supplies a criterion, not that preference.
- **Eval boundary:** Use `C.32.ACE` when a project wants eval-program framing over declared rows, Q-Bundle slots, candidates, or selected-structure changes; state each actual typed result separately under its exact predicate or constraint.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, or cross-case comparability claim is made.
- **Structural-information boundary:** Use `C.33` or `C.34` when the issue is captured structure, lost structure, or preservation adequacy before a criterion row exists. Use C.32.ACS only when that structural-information or preservation concern becomes a declared architecture-characteristic criterion row. Use `C.35` only as generated-carrier admission support or discovered-carrier admission support before C.32 or ACS receives a criteria-bearing claim.
- **Proxy boundary:** Use `E.13` when an optimization indicator, score, eval result, or dashboard state begins to replace the declared architecture concern.
- **Synthesis boundary:** Use `C.32` after criteria rows exist and the next useful work is to synthesize candidate selected-structure changes.
- **Decision and publication boundary:** Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for selection, `C.11` for choice, `G.5` for selected-set result declaration, and `C.32.PAD` for an architecture decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.

