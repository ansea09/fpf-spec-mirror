---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10"
section_title: ".2 - Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__004_2-problem.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10 — .2 - Problem"
line_start: 59349
line_end: 59356
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.22"
  - "E.23"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10.2 - Problem

1. **Polysemy drift.** *Process, function, service, agent, activity* slide between structure, recipe, execution, and promise.
2. **Cross‑context collision.** A label (e.g., *Owner*) is assumed “global” though meanings differ per `U.BoundedContext`.
3. **Name bloat vs. parochialism.** Either hyper‑specific domain names leak into core types, or vague umbrella names obscure invariants.
4. **EntityOfConcern and Description-episteme boundary and specification-use collapse.** Authors mix **EntityOfConcern** (the thing under concern), **Description episteme** (how we describe it), and **specification use** (testable criteria, formality, acceptance, and harness-gated use of a Description episteme).
5. **Register soup.** Tech terms bleed into Plain pedagogy and vice‑versa, inviting category errors.

