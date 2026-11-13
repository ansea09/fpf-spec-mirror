---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__013_relations.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:12 — Relations"
line_start: 80140
line_end: 80177
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
  - "C.32.LCA"
  - "C.32.MLAO"
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
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
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:12 - Relations

- **Builds on:** `C.30` for the described holon, obtaining `ArchitectureRelation` occurrences, their selected `U.Structure` participants, and separately identified `ArchitectureClaim` content; `C.30.P`, `C.30.ASV`, `A.22`, `A.6.F`, `A.6.M`, `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.31.ASAP`, `C.16`, `C.16.P`, `E.22`, `E.23`, `C.19.1`, `C.30.LCA`, `C.30.TFS-REL`, `E.18`, `A.3.4`, `A.15`, and local patterns for recovering source-side architecture referents.

**Uses:**

| Need or use condition | Pattern |
| --- | --- |
| A residual starts the candidate work. | `C.30.ILC` |
| Residual-reducing multilevel framing is being used. | `C.32.MLAO` |
| Influence-source and transformed-side architecture content must be co-synthesized without inferring acting, Work, or transformation facts. | `C.32.CONWAY` |
| A defect needs repair before the candidate can serve its intended use. | `C.32.FAIL` |
| Candidate eval results are needed before later comparison or selection. | `C.32.ACE` |
| A source, description, view, decision record, eval report, handoff, or realized observation captures only part of selected structure. | `C.33` |
| Candidate or source structures need preservation adequacy or correspondence adequacy. | `C.34` |
| Recover the kind and assess the adequacy of a generated or discovered result before candidate palette use. | `C.35` |
| Mathematical representation choice, transfer or reliance remains unresolved. | `C.29` |


**Patterns for the next questions:**

| Question or use | Pattern |
| --- | --- |
| Explicit comparison claims | `A.19.CPM` |
| Set-returning selection claims | `A.19.SelectorMechanism` |
| Selected-set result declaration | `G.5` |
| Archive, front, or pool-treatment policy | `C.18` and `C.19` |
| Fixed local choice | `C.11` |
| Architecture-description work | `C.30.AD` |
| A source-backed publication face and source return | `E.17` |
| Publication occurrence and audience availability | `E.24.PUB` |
| Project architecture decisions | `C.32.PAD` |

- **P2S docking:** `C.32.P2S` uses C.32 for the candidate-synthesis stages after problem pressure, selected structures, architecture characteristics, and structural uncertainty have been recovered; C.32 continues to define the candidate palette.
- **Routes to:** `C.32.MWA` when one usable practice-architecture answer must be synthesized from several structures that do not line up one-for-one; C.32 retains general candidate-palette construction.
- **Boundary:** Use C.32 to construct a candidate architecture palette for one grounded architecture question over selected structures of a described holon. C.35 may support C.32 by recovering a generated or discovered result's kind and assessing its adequacy for candidate-palette use, but C.35 does not select candidates, publish sets, or decide the project architecture. Evidence, assurance, gate, release, work authorization, Method rules, ethical mediation, and causal claims use their own patterns when those claims are being made.


