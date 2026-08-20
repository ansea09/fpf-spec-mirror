---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__004_forces.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:3 — Forces"
line_start: 66478
line_end: 66488
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

### C.32.PAD:3 - Forces

| Force | Tension |
|---|---|
| Candidate plurality | Several candidate configurations can be valid under different trade-offs, while project work needs one current direction or a bounded exception. |
| Trade-off visibility | Architecture characteristics compete; a decision that hides accepted losses cannot be responsibly executed or reopened. |
| Structure and method coupling | The decision must govern actual or modal structure content for the described or transformed-side holon and may also prescribe developer methods intended to produce or preserve those structures. |
| Work split | Structures fixed by the decision and refinement left open must be separated without severing source return. |
| Evolution | A decision must close enough work for now while staying reopenable when context, eval readings, or candidates change. |
| Publication pressure | Teams often want an ADR file before the decision relation is recoverable. |

