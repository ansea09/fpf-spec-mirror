---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__005_forces.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:3 — Forces"
line_start: 59846
line_end: 59856
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.3.NAR"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:3 - Forces

| Force | Tension |
| --- | --- |
| Useful description vs architecture overread | A good description guides architecture work, but it is not the architecture, selected structure, decision claim, proof, or release authorization. |
| Multi-view richness vs selected-structure recovery | Several views can be needed, but each view names the architecture claim, viewpoint, selected structure or structure kind, and admissible use before it is relied on. |
| Viewpoint utility vs viewpoint-as-kind collapse | Viewpoints help a role or practice inspect an architecture; they do not choose the structure kind unless `C.30.ASV` or another governing structural-view pattern names the structure-kind relation by value. |
| Reuse vs freshness | A reused architecture description needs source edition, structure edition, or source-return boundaries when its admissible use depends on currentness. |
| Specification-use vs publication form | A description can be used as a specification, but specification use is a use boundary over a Description episteme or its publication form, not the architecture itself. |
| Thin C.30 bridge vs full description mechanism | C.30 keeps the architecture move central; this pattern carries the heavier architecture-description mechanism when durable description use is being made. |

