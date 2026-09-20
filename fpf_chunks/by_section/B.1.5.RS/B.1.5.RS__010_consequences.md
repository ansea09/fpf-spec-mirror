---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Replace a Constituent Method in Its Encompassing Uses"
section_id: "B.1.5.RS:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__010_consequences.md"
commit_sha: "1fa007d1110d961d54ced2fa58e08177663c401f"
heading_path:
  - "B.1.5.RS — Replace a Constituent Method in Its Encompassing Uses"
  - "B.1.5.RS:9 — Consequences"
line_start: 39589
line_end: 39594
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.11.DUA"
  - "C.29"
keywords:
---

### B.1.5.RS:9 - Consequences

Useful replacements can be adopted where they work without silently breaking other wholes. An incompatibility can also expose a better architecture: different variants, an explicit interface or a changed combination.

The method requires knowledge of receiving uses. Its cost grows with meaningful differences among them, not necessarily with the number of documents or callers. Reuse one comparison across uses only when their relevant conditions and relied-on contribution match.

