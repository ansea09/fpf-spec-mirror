---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept‑Set Table"
section_id: "F.7:13"
section_title: "Relations (with other patterns)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__014_relations-with-other-patterns.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "F.7 — Concept‑Set Table"
  - "F.7:13 — Relations (with other patterns)"
line_start: 82921
line_end: 82932
dependencies:
  - "A.6.9"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "columns"
  - "comparisons"
  - "concept-set"
  - "differences"
  - "row"
  - "table"
---

### F.7:13 - Relations (with other patterns)

**Builds on:**
F.1 **Contexts fixed** → defines the column set; F.2 **Harvest** → supplies harvested terms; F.3 **SenseCells** → provide cell addresses; F.5 **Naming Discipline** → provides the two‑register **FPF labels**; F.9 **Bridges** → justify each row.

**Constrains:**
F.4 **Role Description** — when a template cites an FPF label from the table, it **inherits the Row Scope**; no template may claim semantics beyond the row’s licence.
F.6 **Role Assignment & Enactment Cycle (Six-Step)** — Move M‑4 (“choose label”) must reference a row if it wants Cross‑context reading.

**Used by.**
Part C patterns for didactic alignment pages; Part B trust calculus (B.3) may consume **Row CL(min)** when computing translation penalties.

