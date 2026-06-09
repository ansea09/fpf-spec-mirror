---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 1629
line_end: 1640
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

### A.1.1:8 - Common Anti-Patterns and How to Avoid Them

These failure modes recur when applying `U.BoundedContext` in real programs and knowledge work.

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| :--- | :--- | :--- | :--- |
| **Domain-as-Context** | “Healthcare” or “Physics” is used where a specific context is required. | Violates Domain-family convenience vs precision; meaning stays ambiguous. | Use a specific context id (edition- and source-scoped), and keep the domain label as informative family metadata only. |
| **Implicit equivalence across contexts** | The same string in two contexts is treated as “obviously the same”. | Violates local coherence; creates silent semantic overwrites. | Publish an explicit Bridge with relation kind and loss/fit note (F.9 / E.10.U9). |
| **Context hierarchy / nesting** | Authors model “sub-contexts” as containment or is‑a between contexts. | Violates the flat context map discipline; leaks rules by inheritance. | Remove context-to-context containment; express relationships via Bridges only (E.10.D1). |
| **Time-as-Context** | “Design context” and “Runtime context” are created as separate contexts. | Violates evolvability and clarity; multiplies frames incorrectly. | Use TimeScope tags (`design`/`run`) on descriptions, records, or carriers; keep the semantic frame fixed (C-7; D.CTX). |
| **Glossary-only context** | A context is defined by vocabulary but has no invariants or role taxonomy. | Violates governance intent; “local truth” remains implicit. | Add at least one invariant and a minimal local role taxonomy, even if initially coarse. |

