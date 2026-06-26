---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__010_consequences.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:9 — Consequences"
line_start: 58853
line_end: 58865
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

### C.32:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Candidate architecture configurations are visible before local choice or decision. | Losses and constraint fits must be named earlier. |
| Architecture-characteristic improvement is handled as iterative architecture work. | Each iteration must say which characteristic pressure changed, which selected structures were changed, which reading or feedback is admissible as synthesis input, and what source-return condition opens the next synthesis question. |
| Multi-structure synthesis is reviewable. | The practitioner must keep functions, modules, placement, control, work, evidence, and other selected structures distinct when they matter. |
| Architecture characteristics and quality bundles are recorded as comparison inputs for the receiving pattern. | The palette may need characteristic repair through `C.25`, `C.31`, `C.16`, or later comparison handling through `A.19.CPM`, `C.11`, `A.19.SelectorMechanism`, or `G.5` when those claims are being made. |
| Holonic architecture breadth is preserved. | Examples and candidates must name the described holon and selected structures instead of using domain defaults as unstated selected structures. |
| Source cues can inform architecture work without importing source-domain ontology. | Source-side expressions require recovery of referent, selected structure, architecture-change kind, and source-return condition. |
| Downstream G.5 publication and architecture-decision work stay cleaner. | The team must open the receiving pattern when it wants to publish a selected set, make a local choice, or decide the project architecture. |
| Evolutionary and search practices are usable without hidden single-winner optimization. | The palette may need retained alternatives even when one candidate looks convenient. |

