---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Replace a Constituent Method in Its Encompassing Uses"
section_id: "B.1.5.RS:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__002_problem-frame.md"
commit_sha: "3e9ea496420256ac09257c024b3120fcbc762b81"
heading_path:
  - "B.1.5.RS — Replace a Constituent Method in Its Encompassing Uses"
  - "B.1.5.RS:1 — Problem frame"
line_start: 39478
line_end: 39487
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.11.DUA"
  - "C.29"
keywords:
---

### B.1.5.RS:1 - Problem frame

Use this pattern when a constituent Method could be replaced, simplified or implemented differently and you need to know which encompassing uses remain possible. A faster check returns the same answer on familiar inputs but no longer exposes information another part needs. An approximation is adequate for ranking options but unsuitable for deciding whether a limit is exceeded.

Start with the direction of replacement and the practical gain sought. Ask: **“What do the receiving wholes rely on, and does this candidate still supply it under their conditions?”**

The first useful result is a bounded substitution decision: the uses preserved, uses needing adaptation or restriction, and uses for which the replacement is incompatible or unresolved. One decisive comparison may be enough. Do not perform a new trial when an available argument or known counterexample settles the decision.

Use B.1.5.EW first if the constituent and its encompassing uses are unclear. If only the wording or diagram changes and the performed Method remains unchanged, check that representation's correspondence instead. If the replacement supplies an entire standalone Method, use the relevant fit and choice Methods; this pattern contributes only the constituent-in-whole question.

