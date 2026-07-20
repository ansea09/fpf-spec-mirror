---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__003_problem.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:2 — Problem"
line_start: 67645
line_end: 67650
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

### E.4.PFAD:2 - Problem

Framework architecture decisions recur in FPF-grounded work. A steward must decide whether a set of patterns belongs in Core, in a domain framework, in a local framework, or in publication and pedagogy. They must also decide how the framework depends on FPF Core, what edition boundary it has, what sources ground it, what names are admissible, and which carriers publish or expose the framework.

If those decisions are hidden in prose, table shape, or an ADR-like file, later maintainers cannot tell which structure was selected, which alternative was rejected, what consequences were accepted, or when the decision should be repaired or superseded.

