---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__007_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:5 — Solution"
line_start: 42835
line_end: 42849
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.7.1"
  - "A.8"
  - "C.2.3"
  - "C.3"
  - "C.3.1"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

### C.3:5 - Solution

Use C.3 when the current claim is about typed compatibility, membership, kind intent, kind extent, or kind bridges across reference schemes or context slices.

Do not use C.3 to admit durable U-kind names. That decision belongs to `E.24.UK`, with `A.8`, `A.11`, `F.8`, and `F.18` when kernel-level or public naming force is current.

Normative decisions:

1. `U.Kind` is local to a declared typed-reasoning use and intent-bearing under an effective `U.ReferenceScheme`; its extent is evaluated over `U.ContextSlice` values.
2. `U.SubkindOf` is a partial-order relation over C.3 `U.Kind` values.
3. Kind intent and kind extent are different claims and may have different evidence.
4. Kinds do not carry scope; claim scope and work scope remain USM values.
5. Kind reuse across reference schemes or context slices requires bridge discipline and loss notes.
6. Public `U.*` spelling in a heading, title, filename, or ToC row does not follow from C.3 typed reasoning.

