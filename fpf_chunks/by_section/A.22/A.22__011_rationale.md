---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__011_rationale.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:10 — Rationale"
line_start: 30916
line_end: 30923
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.2"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "architecture-description boundary"
  - "preserved and lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:10 - Rationale

FPF needs one general selected-structure EntityOfConcern because many useful project claims depend on organization before they depend on a specific architecture, mathematical, measurement, or publication pattern. The selected-structure entity has to be dependent, non-agentive, and claim-bearing through descriptions or views: it can be described, sourced, compared, coarsened, extracted, or used by architecture, but it does not act or certify.

The selected design keeps A.22 small enough for first use. A practitioner can write one `StructureQuestionCard@Project` and stop. Heavier DescriptionContext, A.6.6 base-dependence, extraction, lens, evidence, and source-return records are used only when the next use would otherwise hide loss, source dependence, or non-structure claim kind.

The reason to keep C.30 separate is architectural clarity. Architecture is selected structure for a described holon under context and concern; architecture descriptions are Description epistemes and specification-use cases or views over that claim, while publications only make those epistemes or views available. A.22 supplies the structure substrate, not the architecture ontology.

