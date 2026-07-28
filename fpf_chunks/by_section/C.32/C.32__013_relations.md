---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__013_relations.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:12 — Relations"
line_start: 63659
line_end: 63666
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:12 - Relations

- **Builds on:** `C.30`, `C.30.P`, `C.30.ASV`, `A.22`, `A.6.F`, `A.6.M`, `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.31.ASAP`, `C.16`, `C.16.P`, `E.22`, `E.23`, `C.19.1`, `C.30.LCA`, `C.30.TFS-REL`, `E.18`, `A.3.4`, `A.15`, and local patterns for recovering source-side architecture referents.
- **Uses:** `C.30.ILC` when a residual starts the candidate work; `C.32.MLAO` when residual-reducing multilevel framing is being used; `C.32.CONWAY` when transformer and transformed architectures must be co-synthesized; `C.32.FAIL` when a candidate needs repair before explicit comparison, selection, local choice, or decision; `C.32.ACE` when candidate eval results are needed before later comparison or selection; `C.33` when a source, description, view, decision record, eval report, handoff, or realized observation captures only part of selected structure; `C.34` when candidate or source structures need preservation adequacy or correspondence adequacy; `C.35` when generated or discovered carriers need admission support before candidate palette use; `C.29` when mathematical-lens use is being claimed.
- **Receiving patterns:** `A.19.CPM` for explicit comparison claims, `A.19.SelectorMechanism` for set-returning selection claims, `G.5` for claims about publishing a selected set, `C.18` and `C.19` for archive, front, or pool-treatment policy, `C.11` for fixed local choice, `C.30.AD`, `E.17`, and `E.24.PUB` for architecture-description or publication-face work, and `C.32.PAD` for project architecture decisions.
- **P2S docking:** `C.32.P2S` uses C.32 for the candidate-synthesis stages after problem pressure, selected structures, architecture characteristics, and structural uncertainty have been recovered; C.32 remains the candidate-palette owner.
- **Boundary:** C.32 governs candidate architecture palette construction for one grounded architecture question over selected structures of a described holon. C.35 may feed C.32 with generated or discovered carrier adequacy, but C.35 does not select candidates, publish sets, or decide the project architecture. Evidence, assurance, gate, release, work authorization, method governance, ethical mediation, and causal claims use their own patterns when those claims are being made.

