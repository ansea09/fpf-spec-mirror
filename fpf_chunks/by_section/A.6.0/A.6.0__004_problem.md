---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
section_id: "A.6.0:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__004_problem.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.6.0 — U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
  - "A.6.0:2 — Problem"
line_start: 9899
line_end: 9908
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:2 - Problem

If each family (theories, mechanisms, methods, disciplines) invents its own “signature”:

1. **Tight coupling.** Private definitions leak as public standards, breaking substitutability.

2. **Lexical drift.** The same lexical label (e.g., *scope*, *normalization*) hides different laws.

3. **Scope opacity.** Applicability (where the words mean what) remains implicit, violating D.CTX.

