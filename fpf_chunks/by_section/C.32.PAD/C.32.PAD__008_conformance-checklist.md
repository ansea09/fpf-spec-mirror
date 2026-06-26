---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__008_conformance-checklist.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:7 — Conformance Checklist"
line_start: 60790
line_end: 60803
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
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

### C.32.PAD:7 - Conformance Checklist

| Requirement | Required result |
|---|---|
| `CC-PAD-1` | The decision subject, described holon, bounded context, and decision question are explicit. |
| `CC-PAD-2` | The decision cites candidate basis from `C.32` or a named receiving candidate pattern, or states why no candidate-set question is live. |
| `CC-PAD-3` | The selected architecture option or bounded exception is named. |
| `CC-PAD-4` | Affected selected structures are named with governing pattern refs. |
| `CC-PAD-5` | Architecture-characteristic trade-offs, accepted losses, and guardrails are recorded. |
| `CC-PAD-6` | Architecture-description refs, method-use instructions, and performed-work boundaries remain distinct. |
| `CC-PAD-7` | The architect-developer split, source-return condition, and reopen conditions are recorded. |
| `CC-PAD-8` | Triggered holon-transition or BOSC boundary pressure cites `B.2.P` or `B.2`, and structural-information loss or compression cites `C.29`. |
| `CC-PAD-9` | ADR-like publication, evidence, assurance, gate, comparison, selection, selected-set publication, local choice, and work claims exit to their receiving patterns. |

