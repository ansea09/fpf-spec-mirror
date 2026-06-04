---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__005_forces.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:3 — Forces"
line_start: 51813
line_end: 51823
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.8"
  - "F.18"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:3 - Forces

| Force | Tension |
| --- | --- |
| Useful description vs architecture overread | A good description guides architecture work, but it is not the architecture, selected structure, decision, proof, or release authority. |
| Multi-view richness vs selected-structure recovery | Several views can be needed, but each view names the architecture claim, viewpoint, selected structure or structure kind, and admissible use before it is relied on. |
| Viewpoint utility vs viewpoint-as-kind collapse | Viewpoints help a role or practice inspect an architecture; they do not themselves choose the structure kind unless `C.30.ASV` or an exact structure-view pattern names that relation. |
| Reuse vs freshness | A reused architecture description needs source edition, structure edition, or source-return boundaries when its admissible use depends on currentness. |
| Specification-use vs publication form | A description can be used as a specification, but specification use is a use boundary over a Description episteme or its publication form, not the architecture itself. |
| Thin C.30 bridge vs full description mechanism | C.30 keeps the architecture move central; this pattern carries the heavier architecture-description mechanism when durable description use is live. |

