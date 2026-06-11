---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__011_rationale.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:10 — Rationale"
line_start: 14328
line_end: 14335
dependencies:
keywords:
  - "are used only for pattern users"
  - "claims"
  - "conformance items"
  - "evidence records"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "records"
---

### A.6.M:10 - Rationale

The central decision is to treat module as a context-sensitive and viewpoint-sensitive relation role of U.Holon, not as a new root kind. This keeps FPF compatible with many engineering contexts where the same system, episteme, method, organization, publication family, or other structured holon can be a component under one declared relation, a module under another, a functional element under another, and an evidence, assurance, source, or publication artifact under another.

A.6.M follows `A.6.P`: overloaded relation language is repaired by reconstructing kind, slots, qualifiers, admissible use, and witnesses. It also follows the architecture relation discipline: boundary notes catch the first confusion, while A.6.M supplies the full repair body for module relation, interface specification, substitutability, change policy, and open-architecture conformance and admissible-use claims.

The pattern deliberately keeps measurement out of the first move. A module relation can be repaired before anyone knows whether external coupling density, interface standardization share, evidence reuse, or reusable-structure accounting will be needed. When those claims are being made, A.6.M applies `C.31`, `C.31.RSA`, and `C.16`.

