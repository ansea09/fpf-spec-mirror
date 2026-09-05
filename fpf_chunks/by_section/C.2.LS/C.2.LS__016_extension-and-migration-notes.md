---
chunk_kind: "child"
pattern_id: "C.2.LS"
pattern_title: "U.LanguageStateFacetProfile - Thin profile bundle for language-state facets"
section_id: "C.2.LS:15"
section_title: "Extension and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.LS/C.2.LS__016_extension-and-migration-notes.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.2.LS — U.LanguageStateFacetProfile - Thin profile bundle for language-state facets"
  - "C.2.LS:15 — Extension and Migration Notes"
line_start: 44111
line_end: 44127
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.3"
  - "C.2.4"
  - "C.2.4-C.2.7"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "E.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "anchoring"
  - "articulation"
  - "closure"
  - "facet profile"
  - "representation factors"
  - "threshold package"
---

### C.2.LS:15 - Extension and Migration Notes

#### C.2.LS:15.1 - Local extension rule
Contexts may extend the profile with local threshold refs, route notes, or additional descriptive aids, but they shall not add a new master facet that collapses the named facet set into one summary factor.

#### C.2.LS:15.2 - Migration from surrogate prose
Older prose often says:

- "the episteme is still early",
- "the issue is not mature enough",
- "the note is ready",
- "the cue is still raw".

A conforming migration rewrites such statements into explicit facet talk: which facet is low, which is high, which threshold is or is not met, and which move that fact justifies.

#### C.2.LS:15.3 - Boundary reminder
`U.LanguageStateFacetProfile` is a coordination record. If authors put move rules, bridge rules, scale rules, or bundle semantics into the profile itself, that content belongs with the pattern that defines the move, Bridge, scale, or bundle.
