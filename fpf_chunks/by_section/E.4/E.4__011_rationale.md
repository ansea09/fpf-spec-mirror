---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__011_rationale.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:10 — Rationale"
line_start: 63969
line_end: 63974
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.1"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.19"
  - "E.2"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.5.3"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4:10 - Rationale

The ecosystem needs architecture because FPF patterns, frameworks, source packs, publication units, quality records, and decisions are not one kind of object. A file tree cannot preserve the differences among those objects. A relation graph cannot preserve decision rationale or dependency compatibility. A local monolith cannot preserve all source-return and currentness obligations. Architecture work must therefore name the selected structures and route non-owned claims to their owners.

The old Core, Tooling Reference, and Pedagogical Companion distinction remains valuable, but it is only one family partition. Domain and local principle frameworks need their own framework editions so they can depend on Core without redefining it.

