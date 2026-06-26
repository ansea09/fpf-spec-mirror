---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Structural Correspondence, Equivalence, and Morphism Adequacy"
section_id: "C.34:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__011_rationale.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy"
  - "C.34:10 — Rationale"
line_start: 61699
line_end: 61706
dependencies:
  - "A.22"
  - "A.6.M"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
keywords:
  - "directionality"
  - "equivalence"
  - "lost structure"
  - "mapping mode"
  - "morphism"
  - "preserved structure"
  - "scope"
  - "structural correspondence"
---

### C.34:10 - Rationale

Architecture preservation is use-relative. The same two structures can be equivalent for one use, merely corresponding for another, and unusable for a third. A mature C.34 therefore cannot be a generic formalism pattern. It must start from source and target selected structures, then choose the weakest mapping mode that licenses the next architecture use.

This keeps C.34 separate from its neighbors. `C.29` owns mathematical-lens use. `C.30.AD` and `C.30.ASV` own description and view records. `F.9` owns cross-context bridges. `F.15` owns regression and conformance harnesses. `C.32` owns candidate synthesis. C.34 contributes the preservation claim that those owners may need, but it does not replace them.

The source families explain the safeguards. Structural-equivalence research shows that symmetry can compact search only under explicit conditions. Applied category theory shows why preservation maps are powerful but still formal lenses until tied to the architecture use. MBSE view practice makes projection and omitted structure ordinary. Sapunov and ToCS, plus GonzoML, show why observed relation maps and neural substitution labels need typed relation, confidence, and source-label recovery before architecture use.

