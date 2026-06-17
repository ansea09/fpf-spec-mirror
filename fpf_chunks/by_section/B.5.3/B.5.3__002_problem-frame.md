---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Role-Projection Bridge"
section_id: "B.5.3:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__002_problem-frame.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "B.5.3 — Role-Projection Bridge"
  - "B.5.3:1 — Problem Frame"
line_start: 34396
line_end: 34399
dependencies:
  - "A.2"
  - "C.3"
keywords:
  - "concept bridge"
  - "domain-specific vocabulary"
  - "mapping"
  - "terminology"
---

### B.5.3:1 - **Problem Frame**

The FPF is built upon a small set of universal, domain-agnostic concepts (`U.Types`) like `U.System`, `U.Objective`, and `U.State`. This universality is the source of its power, allowing it to be applied to any domain, from thermodynamics to software engineering. However, practitioners in these domains do not speak in terms of `U.Types`; they use their own rich, specialized vocabularies. A thermodynamicist talks about a "Thermodynamic System" and its "Macrostate," not a `U.System` and its `U.State`.

