---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__002_problem-frame.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:1 — Problem frame"
line_start: 28806
line_end: 28818
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:1 - Problem frame

In FPF, every aggregation is a *material act*:

```
Γ : (D : DependencyGraph, T : U.TransformerRole) → H′ : U.Holon
```

`D` is the *only* admissible input shape for Γ. It must capture **part–whole** structure faithfully (A.1, A.14) while staying neutral to order (handled by Γ\_ctx and Γ\_method), time (Γ\_time), and accounting (Γ\_work). If `D` is sloppy—mixing kinds of relations or scopes—Γ becomes unpredictable and the Quintet invariants (IDEM, COMM, LOC, WLNK, MONO) fail in subtle ways.

This pattern normatively defines `DependencyGraph`, the **mereological vocabulary** allowed on its edges, and the **guards** that make Γ provable and comparable across domains.


