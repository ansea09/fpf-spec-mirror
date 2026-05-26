---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "RepresentationTransduction — same-described-entity representation-scheme transition"
section_id: "A.6.3.RT:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__002_problem-frame.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.6.3.RT — RepresentationTransduction — same-described-entity representation-scheme transition"
  - "A.6.3.RT:1 — Problem frame"
line_start: 11038
line_end: 11047
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
  - "diagram"
  - "notation shift"
  - "reasoning medium"
  - "recoverability"
  - "representation transduction"
  - "same-described-entity representation change"
  - "source tether"
  - "state-representation shortcut"
  - "table"
---

### A.6.3.RT:1 - Problem frame

The same described entity often needs to be carried across more than one representation regime:
- prose into a table that makes comparison or coverage clearer;
- a table into a diagram that foregrounds dependency or topology;
- a diagram into a structured notation suitable for replay or technical review;
- a source representation into another regime that changes reasoning possibilities without changing the underlying described entity.

In practice these shifts are often treated as harmless reformatting. But some representation changes alter reasoning possibilities, reduce recoverability, or quietly change what appears to be present in the source. FPF already has `A.6.3` for same-described-entity conservative viewing. This pattern names the recurring same-described-entity case where the published result changes representation scheme while the case still remains inside `A.6.3`.

