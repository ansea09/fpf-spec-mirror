---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__010_conformance-checklist.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:6 — Conformance Checklist"
line_start: 42108
line_end: 42118
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2"
  - "B.2.P"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-B1.4-1 | The aggregation claim identifies its subject, included inputs and relations, combining rule, required result, aggregation mode, ClaimScope when needed, temporal reference/window when relevant, and admissible use. | Makes the aggregation usable without requiring a separate record when an ordinary answer suffices. |
| CC-B1.4-2 | Contextual aggregation identifies its ordered relations and OrderSpec. Temporal aggregation identifies its intervals, bearers, temporal reference and TimeWindow; the proper-phase profile also establishes one-carrier identity and the direct phase relations. | Keeps order, temporal aggregation and proper-phase claims distinguishable. |
| CC-B1.4-3 | Independence, join, coverage, and overlap-policy conditions are present when the claim uses them. | Keeps local composition reviewable. |
| CC-B1.4-4 | Method, method-description, work-plan, work-occurrence, work-resource, transformation, and whole-reidentification claims use the patterns that define or test them. | Prevents B.1.4 from absorbing neighboring objects. |
| CC-B1.4-5 | Mathematical notation is treated as a selected lens or expression, not as the in-life object or relation. | Keeps `Gamma_ctx`, `Gamma_time`, graph, and algebra language bounded. |
| CC-B1.4-6 | Use stays within the established operation, identity and coverage conditions. When a required condition fails or remains unknown, narrow the result or retain the unresolved conclusion; use the subject pattern for a distinct identity, change or whole-reidentification question. | Preserves actual stops without requiring a stronger claim merely to finish an ordinary aggregate. |

