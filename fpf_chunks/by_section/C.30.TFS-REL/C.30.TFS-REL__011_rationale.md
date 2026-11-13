---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Use Transformation-Flow Structures and Networks in Architecture"
section_id: "C.30.TFS-REL:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__011_rationale.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.30.TFS-REL — Use Transformation-Flow Structures and Networks in Architecture"
  - "C.30.TFS-REL:10 — Rationale"
line_start: 78419
line_end: 78424
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.CONWAY"
  - "E.10"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "E.18.NET"
  - "E.24.PUB"
  - "F.18"
keywords:
  - "ArchitectureTransformationFlowStructureRelation"
  - "TFS"
  - "architecture use"
  - "crossing"
  - "flow valuation"
  - "functional view"
  - "path"
  - "transformation-flow structure"
  - "transformation-flow structure network"
---

### C.30.TFS-REL:10 - Rationale

E.18 governs one selected TFS, its paths, crossings, valuations, and pins; E.18.NET governs one selected network and its cross-member relations. Architecture needs to use either object without taking over its ontology or inventing an unnamed architecture bearer. The smallest stable result is therefore one qualified C.30-side account identifying the architecture and flow objects it uses and preserving the applicable architecture-use branch from :4.4a when a network is selected.

This pattern also protects functional architecture and actual-change semantics. A functional structure may correspond to a transformation-flow structure, and in some cases both views may designate the same selected `U.Structure`; that identity is not automatic. Required or desired effect remains claim content, while an actual `U.Transformation` requires the independent A.3.4 basis.

