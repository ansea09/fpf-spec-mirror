---
chunk_kind: "child"
pattern_id: "C.2.LS"
pattern_title: "Language-State Facet Profile: Publish Readings and Use Conditions Together"
section_id: "C.2.LS:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.LS/C.2.LS__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.LS — Language-State Facet Profile: Publish Readings and Use Conditions Together"
  - "C.2.LS:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 53097
line_end: 53103
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.3"
  - "C.2.4"
  - "C.2.4-C.2.7"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "E.18"
  - "E.24.PUB"
  - "F.9"
  - "F.9.1"
keywords:
  - "articulation"
  - "closure"
  - "facet profile"
  - "local thresholds"
  - "representation factors"
  - "source and use claims"
---

### C.2.LS:8 - Common Anti-Patterns and How to Avoid Them
- **Shadow progression.** Treating `early/late` as a master scale. Split the judgement into the named facets.
- **Formality capture.** Letting `F` stand in for closure or articulation. Publish those facets explicitly.
- **Bundle inflation.** Turning the profile into a second `A.19`. Keep it thin and referential.
- **Opaque readiness.** Using words such as `ready` or `mature` without naming which facet justifies the claim.
- **Route-note capture.** Letting an informative route note act as a move rule, gate state, or endpoint rule. Keep route notes informative. Use `A.16` for admissible moves, the applicable pattern for a downstream definition or test, the applicable gate or Work pattern for those claims, and an `authoritySourceRef` only when an external authority actually supplies the rule.

