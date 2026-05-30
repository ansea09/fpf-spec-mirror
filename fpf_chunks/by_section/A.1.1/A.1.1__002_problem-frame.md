---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__002_problem-frame.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:1 — Problem Frame"
line_start: 1319
line_end: 1328
dependencies:
  - "A.1"
  - "A.2.1"
  - "D.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "U.Boundary"
  - "U.BoundedContext"
  - "U.Holon"
keywords:
  - "DDD"
  - "context"
  - "domain"
  - "glossary"
  - "invariants"
  - "local meaning"
  - "semantic boundary"
---

### A.1.1:1 - Problem Frame

Large systems of thought (and large engineered systems) break down when meaning is treated as globally uniform.
The same label (e.g., “role”, “service”, “ticket”, “evidence”) routinely carries incompatible senses across teams, disciplines, standards editions, and historical eras.

FPF needs a first-class mechanism that answers a simple question with precision:
**“In which semantic frame does this term, rule, or role-claim hold?”**

The `U.BoundedContext` is that mechanism. It makes “it depends” explicit and governable by naming *what it depends on*.

