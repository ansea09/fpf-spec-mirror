---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__012_rationale.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:10 — Rationale"
line_start: 1963
line_end: 1970
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

### A.1.1:10 - Rationale

`U.BoundedContext` is the semantic companion to `U.Holon`. A holon boundary says what counts as inside or outside the whole for a claim. A bounded-context boundary says where vocabulary, invariant, role taxonomy, episteme-use/status relation set, and inference rule are locally coherent when those claims are current.

The pattern is generalized from domain-driven design but is not software-only. Scientific theories, legal standards, hospital procedures, manufacturing cells, model cards, research programs, and FPF evaluation contexts all need local meaning. FPF makes that locality an ontic rather than leaving it as "it depends."

This also protects role and episteme ontology. A `U.Role` is not global; it is valid inside a bounded context. A `U.Episteme` is meaningful only when its EntityOfConcern, viewpoint, reference scheme, and bounded context are known. Bridges then make cross-context correspondence explicit instead of letting spelling decide.

