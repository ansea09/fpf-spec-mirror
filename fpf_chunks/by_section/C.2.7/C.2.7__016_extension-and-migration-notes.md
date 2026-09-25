---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "U.LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
section_id: "C.2.7:15"
section_title: "Extension and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__016_extension-and-migration-notes.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "C.2.7 — U.LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
  - "C.2.7:15 — Extension and Migration Notes"
line_start: 50220
line_end: 50229
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
Authors may add extra local factors, but each added factor should answer a distinct question rather than duplicating locality, sparsity, or symbolicity under another label.

#### C.2.7:15.2 - Migration from alias-heavy prose
Aliases such as `EncodingBasis` or similar should be unfolded into explicit factor dockings before they are relied upon for comparison, bridge claims, or downstream use.

#### C.2.7:15.3 - Boundary reminder
`U.LanguageStateRepresentationFactorBundle` describes representational organization only. It does not determine admissible use, closure, or anchoring by itself.
