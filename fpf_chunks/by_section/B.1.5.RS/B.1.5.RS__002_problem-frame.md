---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Evaluate a Method Replacement in Its Encompassing Uses"
section_id: "B.1.5.RS:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__002_problem-frame.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "B.1.5.RS — Evaluate a Method Replacement in Its Encompassing Uses"
  - "B.1.5.RS:1 — Problem frame"
line_start: 44546
line_end: 44555
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

Use this pattern when a constituent Method could be replaced, simplified or implemented differently and you need to know which encompassing uses remain possible. A faster check returns the same answer on familiar inputs but no longer exposes information another part needs. An error bound can preserve the order of well-separated options while leaving a value near a decision threshold unresolved. The same bound can settle a threshold when the entire interval falls on one side of it.

Start with the direction of replacement and the practical gain sought. Ask: **“What do the receiving wholes rely on, and does this candidate still supply it under their conditions?”**

An assessment identifies the uses preserved, uses needing adaptation or restriction, and uses for which the replacement is incompatible or unresolved. This can finish a request for a compatibility judgement. Choosing and introducing a replacement can be a further assignment. One decisive comparison may be enough. Use an available argument or counterexample when it decides compatibility. A trial commissioned as a separate deliverable remains due on its agreed terms.

Use B.1.5.EW first if the constituent and its encompassing uses are unclear. If only the wording or diagram changes and the performed Method remains unchanged, check that representation's correspondence instead. If the replacement supplies an entire standalone Method, use the relevant fit and choice Methods; this pattern contributes only the constituent-in-whole question.

