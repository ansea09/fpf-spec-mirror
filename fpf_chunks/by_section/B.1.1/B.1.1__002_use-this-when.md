---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Structure and Relation Grounding"
section_id: "B.1.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__002_use-this-when.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "B.1.1 — Dependency Structure and Relation Grounding"
  - "B.1.1:0 — Use This When"
line_start: 41740
line_end: 41764
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.6.5"
  - "B.1"
  - "B.1.4"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.1:0 - Use This When

Use this pattern when an aggregation, architecture, assurance, or construction claim depends on how candidate parts, members, phases, portions, or external relations depend on each other.

Typical moments:

- a dependency diagram is used to justify a whole-level claim;
- a graph mixes parthood, mapping, order, time, resource, and boundary-crossing relations;
- a project needs to know whether a relation is part-whole, dependence, representation, influence, source use, publication use, or evidence relation;
- a selected dependency structure will be expressed with a graph, table, matrix, or another mathematical or representation lens.

**First useful move.** Name the dependency relation and its participants before choosing graph notation. Use B.1.1:4.3 to distinguish common relation kinds, then follow the pattern that defines or tests the relation in question.

**What goes wrong if missed.** A generic "depends on" edge can conceal different relations. External influence, order, or temporal dependence may be mistaken for parthood, and mathematical checks may appear precise while the relation being checked remains unclear.

**What this buys.** The practitioner can use dependency evidence in a B.1 aggregation claim while keeping the relations distinct from their graph representation.

**Not this pattern when.**

- If the current relation word is a mereology question, use `A.14`.
- If the current part-whole claim needs constructional grounding, use `C.13`.
- If the current object is architecture selected structure, use `A.22` and `C.30`.
- If the current expression is mathematical-lens choice, use `C.29`.
- If the current question is performed work, use `A.15.1`.

