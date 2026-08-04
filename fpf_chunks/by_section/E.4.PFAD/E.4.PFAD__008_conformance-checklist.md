---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__008_conformance-checklist.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:7 — Conformance Checklist"
line_start: 70306
line_end: 70317
dependencies:
  - "C.32.ADR"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFAD.1 Decision relation exists | A filled `PrincipleFrameworkArchitectureDecision@Context` relation exists before any ADR-like publication is treated as the decision. |
| CC-PFAD.2 Framework-specific slots live | The decision uses at least one framework-specific slot: edition dependency, selected pattern set, relation graph, publication carrier, access carrier, name cards, source-return, quality route, or currentness route. |
| CC-PFAD.3 Generic owners reused | Rationale uses `E.9`; project architecture decision shape uses `C.32.PAD`; publication projection uses `C.32.ADR` or `E.17`. |
| CC-PFAD.4 Alternatives and consequences present | Rejected alternatives, rationale, consequences, and repair or supersession conditions are recoverable. |
| CC-PFAD.5 Source and name routes present | Source packs, source-return conditions, and required name-card work are named. |
| CC-PFAD.6 Quality and admission separated | `E.21` quality evaluation refs and `E.19` admission review refs are separate or explicitly absent. |
| CC-PFAD.7 Demotion checked | If framework-specific obligations are absent, the decision is handled directly by neighboring patterns. |

