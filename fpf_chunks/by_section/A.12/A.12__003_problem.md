---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "External Transformer & Reflexive Split"
section_id: "A.12:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__003_problem.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.12 — External Transformer & Reflexive Split"
  - "A.12:2 — Problem"
line_start: 18891
line_end: 18898
dependencies:
  - "A.3"
  - "B.2.5"
  - "U.Interaction"
keywords:
  - "agency"
  - "causality"
  - "control loop"
  - "external agent"
  - "self-modification"
---

### A.12:2 - Problem

Without a strict rule of agent externalization, models become ambiguous and untraceable, leading to critical failures in design and audit:

1.  **Causality Collapse ("Self-Magic"):** Phrases like "the system configures itself" or "the document updates itself" create a causal black hole. It becomes impossible to answer the question, "What *caused* this change?" This makes debugging, root cause analysis, and assigning responsibility impossible.
2.  **Audit Dead-Ends:** An auditor tracing a change finds that the system is its own justification. There is no external evidence, no log from an independent actor, and therefore, no way to verify the integrity of the transformation. This is a direct violation of **Evidence Graph Referring (A.10)**.
3.  **Hidden Dependencies:** In a "self-healing" system, the healing mechanism (the regulator) and the operational part (the regulated) are modeled as a single monolithic block. This hides the critical internal dependency between them. A failure in the regulator might go unnoticed until the entire system collapses, because its role was never made explicit.

