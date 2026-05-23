---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__007_bias-annotation.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:6 — Bias-Annotation"
line_start: 1405
line_end: 1412
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

### A.1.1:6 - Bias-Annotation

This pattern is intentionally universal, but it can be misread through narrower lenses:

* **Software-centrism bias:** Readers may assume “bounded context” only applies to microservices/teams. *Mitigation:* the Episteme archetype is first-class; contexts apply equally to theories, standards, and scientific practices.
* **Boundary reification bias:** Authors may treat boundaries as “natural facts” rather than modelling choices. *Mitigation:* boundaries are declared for governance and clarity, and cross-context relations are handled via Bridges with explicit loss/fit.
* **English-label bias:** Examples often use English visible terms, which can hide multilingual drift. *Mitigation:* language/edition discipline in D.CTX governs when to split/merge contexts; multilingual labels are metadata when semantics are truly bound.

