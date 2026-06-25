---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__004_problem.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:2 — Problem"
line_start: 1673
line_end: 1682
dependencies:
  - "A.1"
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.24"
  - "E.24.PUB"
  - "F.0.1"
  - "F.18"
  - "F.9"
  - "U.Holon"
keywords:
---

### A.1.1:2 - Problem

Without `U.BoundedContext`:

1. **Semantic drift hides in shared words.** Teams keep the same label while changing the object, role, rule, or allowed inference.
2. **Local rules leak globally.** A policy, status, role, or invariant valid in one context is applied in another without a bridge relation.
3. **Pluralism looks like contradiction.** Two contexts can each be coherent, but absent context they look mutually inconsistent.
4. **Role assignments lose their footing.** A `U.Role` is used as a global label rather than a value defined in a local role taxonomy.
5. **Domain labels pretend to govern.** "Healthcare", "AI", "architecture", or "physics" is used where a specific semantic frame is required.

