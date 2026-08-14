---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__014_relations.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:13 — Relations"
line_start: 94532
line_end: 94543
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:13 - Relations

**Builds on:**

- Use **F.1** and **F.0.1** to recover exact sources and local claims, and **F.2**, **F.3**, and **F.17** only when expressions or durable addresses are needed.
- Use **F.5** for clear designations, **F.9** only for an actual relation between distinct local meanings, **F.10** for separate EvidenceStatus and RequirementStatus uses and windows, and **F.11** to keep Method, MethodDescription, Work, and output distinct.
- Use **A.2.3** for exact promise content, PromiseContentUse, delivered outcome, and fulfilment; **A.15.1** for delivery and evaluation Work; and **A.6.1** for the exact evaluation-operation application and result binding.

**Uses direct subject patterns.** Use C.2 and C.16 for observations, characteristics, scales, units, and measured values. When the measurement does not directly concern the promised characteristic, use C.16.P to recover the distinct indicator relation and cite the pattern that defines or tests it; use A.6.RCD `missing-governor` when no such rule exists. Use A.10 for evidence use, B.3 only for assurance or material reliance, E.13 only for optimized or decision-driving proxies, and the appropriate direct pattern for kind, control, or transformation claims.

**Constrains:** Reporting and assurance keep promise content, delivery Work, observation, measured value, window, evaluation Method and Work, operation application, result binding, declared result scale, optional verdict episteme, EvidenceStatus, RequirementStatus, evidence use, material reliance, any defined indicator relation, and any F.9 relation distinct. A relation-specific CL or loss is reported with that relation, not folded into the result or status.

