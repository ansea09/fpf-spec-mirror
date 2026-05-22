---
chunk_kind: "child"
pattern_id: "A.19.SUPPORT-VIEW"
pattern_title: "Cross-Surface Support View"
section_id: "A.19.SUPPORT-VIEW:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SUPPORT-VIEW/A.19.SUPPORT-VIEW__015_consequences.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.19.SUPPORT-VIEW — Cross-Surface Support View"
  - "A.19.SUPPORT-VIEW:9 — Consequences"
line_start: 23900
line_end: 23913
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SURF-SPACE"
  - "A.6.3"
  - "A.6.P"
  - "C.19"
  - "C.24"
  - "E.17"
  - "E.17.0"
  - "G.10"
  - "G.2"
  - "G.5"
keywords:
  - "CrossSurfaceAtlasView"
  - "CrossSurfaceSupportView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas support"
  - "support qualifiers"
  - "support view"
  - "support-only reading"
  - "thin support"
---

### A.19.SUPPORT-VIEW:9 - Consequences

**Benefits**

- Readers get one explicit support layer without losing the declared substrate.
- FPF keeps one common support-view family without forcing `G.2` or another local specialization to carry the whole support requirement.
- Atlas-form support remains available where it helps, but thinner support views stay lawful.

**Trade-offs**

- The declaration must keep more boundaries explicit: view law, substrate, publication, and policy no longer collapse into one comfortable narrative.
- Some cases that once looked like "just a view" must now say whether they are thin support, atlas support, publication, or policy.
- The pattern requires the base palette or source surface to stay recoverable, which can make local prose slightly less terse.

