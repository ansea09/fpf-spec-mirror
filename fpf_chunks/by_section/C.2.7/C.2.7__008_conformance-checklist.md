---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "U.LanguageStateRepresentationFactorBundle"
section_id: "C.2.7:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__008_conformance-checklist.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.2.7 — U.LanguageStateRepresentationFactorBundle"
  - "C.2.7:7 — Conformance Checklist"
line_start: 43940
line_end: 43945
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

### C.2.7:7 - Conformance Checklist
- `CC-C.2.7-1` `LanguageStateRepresentationFactorBundle` **SHALL** be published as a factor bundle, not as a hidden scalar.
- `CC-C.2.7-2` Local aliases such as `EncodingBasis` **MAY** exist only with an explicit docking to the governed factors.
- `CC-C.2.7-3` Representation factors **MUST NOT** silently replace `LanguageStateAnchoringMode` or `LanguageStateClosureDegree`.
- `CC-C.2.7-4` New local factors **SHALL** preserve the factor-bundle discipline.

