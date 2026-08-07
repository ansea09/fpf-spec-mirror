---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__011_rationale.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:10 — Rationale"
line_start: 64545
line_end: 64554
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
  - "U.Structure"
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

### C.32:10 - Rationale

Architecture practice needs a pattern between a grounded architecture question and an architecture decision. `C.30` can ground the architecture question over selected structures of a described holon. `C.30.ASV`, `A.6.F`, `A.6.M`, `C.30.LCA`, `C.30.TFS-REL`, `C.25`, and `C.31` can recover the particular structures and characteristics. Front patterns, `G.5` publication of a selected set, `C.11` local choice, and decision patterns can later govern downstream set treatment and project decisions.

C.32 governs the constructive middle: building a small set of candidate architecture configurations whose selected structures, allocations, characteristic trade-offs, known losses, source-return conditions, and receiving patterns are explicit.

The same middle repeats during improvement. A later criteria-row change, scale-row change, C.16 reading, C.25 or C.31 pressure change, C.31.ASAP scale-preference change, or C.18 or C.19 front, archive, or retained-alternative relation can reopen C.32 when it changes the architecture-characteristic pressure, the selected structures under stress, or the acceptable loss profile. C.32 then synthesizes another candidate palette; it does not turn the trigger into a decision.

The nontrivial work is not to warn against every possible confusion. The work is to make synthesis real enough that architecture content is available for a later front, comparison, publication of a selected set, or decision.

