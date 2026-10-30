---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
section_id: "C.2.7:15"
section_title: "Extension and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__016_extension-and-migration-notes.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.7 — LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
  - "C.2.7:15 — Extension and Migration Notes"
line_start: 54026
line_end: 54035
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "A.19"
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
Authors may add extra local factors, but each added factor should answer a distinct question rather than duplicating locality, sparsity, or symbolicity under another label.

#### C.2.7:15.2 - Migration from alias-heavy prose
Aliases such as `EncodingBasis` or similar should be unfolded into explicit factor dockings before they are relied upon for comparison, bridge claims, or downstream use.

#### C.2.7:15.3 - Boundary reminder
`LanguageStateRepresentationFactorBundle` describes representational organization only. Admissible use, closure and source or interaction claims retain their own conditions and grounds.
