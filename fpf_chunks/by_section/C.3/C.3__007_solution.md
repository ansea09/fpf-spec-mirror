---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__007_solution.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:5 — Solution"
line_start: 41549
line_end: 41563
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.8"
  - "C.2.3"
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

Use C.3 when the current claim is about typed compatibility, membership, kind intent, kind extent, or cross-context kind bridges.

Do not use C.3 to admit durable U-kind names. That decision belongs to `E.24.UK`, with `A.8`, `A.11`, `F.8`, and `F.18` when kernel-level or public naming force is current.

Normative decisions:

1. `U.Kind` is context-local and intent-bearing.
2. `U.SubkindOf` is a partial-order relation over C.3 `U.Kind` values.
3. Kind intent and kind extent are different claims and may have different evidence.
4. Kinds do not carry scope; claim scope and work scope remain USM values.
5. Cross-context kind reuse requires bridge discipline and loss notes.
6. Public `U.*` spelling in a heading, title, filename, or ToC row does not follow from C.3 typed reasoning.

