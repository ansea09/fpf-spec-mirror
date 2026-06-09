---
chunk_kind: "child"
pattern_id: "E.5.1"
pattern_title: "DevOps Lexical Firewall"
section_id: "E.5.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.1/E.5.1__005_solution.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.5.1 — DevOps Lexical Firewall"
  - "E.5.1:4 — Solution"
line_start: 56659
line_end: 56675
dependencies:
  - "E.5"
keywords:
  - "CI/CD"
  - "DevOps"
  - "IDE commands)"
  - "conceptual purity"
  - "file extensions"
  - "jargon"
  - "lexical firewall"
  - "tool-agnostic"
  - "yaml"
---

### E.5.1:4 - Solution
Establish a **Lexical Firewall** around the **Conceptual Core** *(conceptual constraint; not a build‑time linter)*:

1. **Forbidden lexicon**
   Normative patterns **SHALL NOT** contain tool‑or file‑specific words
   (e.g. protocol keywords, file extensions, IDE commands).
   Permissible wording: “a reference parser”, “a serialisation schema”.

2. **Indirection rule**
   When a Core concept needs an executable illustration, the pattern
   cites the **Tooling Reference family** artefact by *conceptual name*,
   never by concrete path or syntax.

3. **Glossary pointer**
   If an unavoidable technical term appears, it is defined in a *Tooling Glossary* outside the Core and referenced by conceptual alias—not embedded.
*Non‑normative automation.* Machine checks **MAY** exist in Tooling; they are advisory and **MUST NOT** be imported into the Core.

