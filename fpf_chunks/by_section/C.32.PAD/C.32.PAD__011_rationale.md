---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__011_rationale.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:10 — Rationale"
line_start: 66351
line_end: 66358
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.6"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.18.NET"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:10 - Rationale

C.32.PAD exists because candidate synthesis and architecture decision are different work moments. C.32 builds the option space; PAD commits the project to a current architecture option or bounded exception and records the method and work consequences of that commitment.

The pattern keeps four layers apart: an obtaining C.30 `ArchitectureRelation` over one architecture-bearing holon and selected `U.Structure`; any `ArchitectureClaim` that states actual, negative, unresolved, candidate, required, desired, or expected content about the holon, relation, or structure; `ArchitectureDecisionRelation@Project`, which connects composite project Work to the selected option and declared work consequences; and `ArchitectureDecisionDescription@Project`, whose project use is established through the C.30.AD relation and which can be published in ADR-like or other forms. Optional system-of-interest, local-kind, System-classification, assignment-species, assignment-occurrence, architecture-influence, and network references retain their A.15.6, A.2 and A.2.1, C.32.CONWAY, E.18.NET, and C.30.TFS-REL subject patterns. This lets FPF reuse its existing architecture, description, Method, work, evidence, assurance, measurement, publication, project, and network patterns instead of creating a separate architecture-decision ontology for those facts.

The pattern is architecture-reusable across holon kinds, not because every decision target is itself a holon kind. The same decision relation can apply to admitted holons such as systems, organizations-as-systems, built assets, AI-agent setups, epistemes, work occurrences, or disciplines. It can also concern Method, evidence, or an exact object or relation recovered from role wording, provided those values stay under `A.3.1`, `E.10.ROLE`, `A.2.7`, `A.10`, and `A.15` rather than being admitted as holons by label.

