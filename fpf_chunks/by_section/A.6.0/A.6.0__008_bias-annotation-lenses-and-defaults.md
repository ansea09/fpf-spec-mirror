---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:6"
section_title: "Bias-Annotation (lenses and defaults)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__008_bias-annotation-lenses-and-defaults.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:6 — Bias-Annotation (lenses and defaults)"
line_start: 10188
line_end: 10195
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

### A.6.0:6 - Bias-Annotation (lenses and defaults)

* **Local‑first meaning.** Laws are **local** to the named Context; cross‑context use must be explicit (Bridge), never implicit.

* **No illicit scalarisation.** If numbers appear, legal comparability follows **CG-Spec and MM-CHR**; **no ordinal means**, **partial orders return sets**; unit and scale alignment is explicit.

* **Register hygiene.** Keep Tech vs Plain register pairs; avoid tooling or vendor talk in Kernel prose (E.10).

