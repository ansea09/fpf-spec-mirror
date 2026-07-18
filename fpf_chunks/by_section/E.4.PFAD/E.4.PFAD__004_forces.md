---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__004_forces.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:3 — Forces"
line_start: 66003
line_end: 66012
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

### E.4.PFAD:3 - Forces

| Force | Tension |
| --- | --- |
| Decision memory | The framework needs durable rationale, but decision memory must not be confused with the framework structure itself. |
| Framework-specific slots | Generic decision patterns carry much of the method, but framework editions add dependency, naming, source-return, publication, and currentness obligations. |
| Lightweight publication | ADR-like records are useful, but their headings do not create the decision relation. |
| Evolution | Framework decisions may become obsolete when sources, Core editions, domain scope, or local use changes. |
| Non-duplication | A child pattern must not repeat `E.9`, `C.32.PAD`, or `C.32.ADR` without adding framework-specific value. |

