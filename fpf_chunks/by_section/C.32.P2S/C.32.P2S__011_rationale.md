---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Transformation Flow"
section_id: "C.32.P2S:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__011_rationale.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Transformation Flow"
  - "C.32.P2S:10 — Rationale"
line_start: 59753
line_end: 59760
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.3.4"
  - "B.2"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "architecture work flow"
  - "owner-specific return"
  - "problem-to-structure architecturing flow"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:10 - Rationale

C.32.P2S belongs under C.32 because the central transformation is architecture synthesis: recovering problem pressure and structural uncertainty, generating candidate selected-structure changes, preserving alternatives, making decision-ready content, and returning actual-structure feedback to the next synthesis question.

It cannot be only a C.22 pattern because a problem card does not carry architecture synthesis, decision, realization, and feedback. It cannot be only a C.30 pattern because grounded architecture and structural-view adequacy do not themselves construct candidate palettes or govern downstream work. It cannot be only a C.32 pattern because the palette is only one stage of the larger architecturing flow. It cannot be only C.32.PAD or C.32.ADR because decisions and records do not create the candidate space and do not realize structures. It cannot be only A.15 or E.18.1 because method and work carry-through and P2W do not govern architecture candidate synthesis or selected-structure decision content.

The structural-information lane is selected now because otherwise P2S cannot explain what changes. Architecturing refines uncertainty about future structures into candidate, selected, expected, and actual structures, while descriptions, decisions, methods, work, and eval reports capture only part of that content. The practitioner records which structural content is captured by descriptions, decisions, method handoffs, work records, evals, and measurements; which structure remains latent, hidden, or lost; and which source-return condition returns the work to stronger structure inspection or a `C.29` lens use such as epiplexity, DSM, graph, coarse-graining, equivalence, or morphism.

