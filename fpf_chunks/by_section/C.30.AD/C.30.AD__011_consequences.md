---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__011_consequences.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:8 — Consequences"
line_start: 55202
line_end: 55216
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

### C.30.AD:8 - Consequences

Positive consequences:

- Architecture descriptions become reusable without pretending to be the architecture itself.
- Multi-view work can keep viewpoints, views, selected structures, correspondences, source return, freshness, and specification use inspectable.
- Description, publication, evidence, assurance, gate, decision, work, release, and mathematical-lens claims stay with separate governing patterns.
- C.30 can stay focused on architecture while C.30.AD carries the heavier description machinery.

Costs:

- A useful architecture document needs explicit links to `ArchitectureOf@Context`, selected structures, viewpoints, and admissible use.
- Reused or regulated descriptions may need correspondence, source-return, and freshness fields before they can be relied on.
- Familiar document forms lose implicit authority; evidence, assurance, gate, decision, and release claims must be established by their own patterns.

