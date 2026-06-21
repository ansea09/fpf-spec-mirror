---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:10.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__014_bias-annotation.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:10.1 — Bias-Annotation"
line_start: 4614
line_end: 4617
dependencies:
  - "A.1.1"
  - "A.2.2"
  - "A.2.3"
  - "B.3"
keywords:
  - "& guard style)"
  - "ClaimScope (G)"
  - "WorkScope"
  - "applicability"
  - "scope"
  - "set-valued"
---

### A.2.6:10.1 - Bias-Annotation

USM counters three recurring biases. First, scope wording can hide a claim that the object is usable everywhere; require an addressable `U.ContextSlice` instead of a vague domain phrase. Second, abstract wording can be mistaken for wider scope; keep abstraction tier and detail separate from `U.Scope`. Third, publication convenience can be mistaken for content permission; `U.PublicationScope` bounds the publication surface and does not widen `U.ClaimScope` or `U.WorkScope`.

