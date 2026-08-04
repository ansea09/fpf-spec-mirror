---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__011_rationale.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:10 — Rationale"
line_start: 70333
line_end: 70338
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

### E.4.PFAD:10 - Rationale

FPF already has decision, architecture decision, and ADR-projection patterns. The reason PFAD exists is narrower: framework authors repeatedly need the same framework-specific slots that generic decision patterns do not keep visible by default. Those slots are edition dependency, selected pattern set, relation structure, publication carrier, access carrier, source-return, naming, quality route, and currentness route.

PFAD is therefore a specialization by obligation, not by vocabulary. If those obligations are not live, the specialization has no value.

