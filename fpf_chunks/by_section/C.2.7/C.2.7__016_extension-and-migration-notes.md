---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "U.LanguageStateRepresentationFactorBundle"
section_id: "C.2.7:15"
section_title: "Extension and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__016_extension-and-migration-notes.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.2.7 — U.LanguageStateRepresentationFactorBundle"
  - "C.2.7:15 — Extension and Migration Notes"
line_start: 44601
line_end: 44610
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.6"
  - "C.2.LS"
  - "F.9"
  - "F.9.1"
keywords:
  - "factor bundle"
  - "locality"
  - "representation factors"
  - "representation organization"
  - "sparsity"
  - "symbolicity"
---

### C.2.7:15 - Extension and Migration Notes

#### C.2.7:15.1 - Local extension rule
Contexts may add extra factors, but each added factor should answer a distinct question rather than duplicating locality, sparsity, or symbolicity under another label.

#### C.2.7:15.2 - Migration from alias-heavy prose
Aliases such as `EncodingBasis` or similar should be unfolded into explicit factor dockings before they are relied upon for comparison, bridge claims, or downstream use.

#### C.2.7:15.3 - Boundary reminder
`U.LanguageStateRepresentationFactorBundle` describes representational organization only. It does not determine admissible use, closure, or anchoring by itself.
