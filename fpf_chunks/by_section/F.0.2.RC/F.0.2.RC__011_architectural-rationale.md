---
chunk_kind: "child"
pattern_id: "F.0.2.RC"
pattern_title: "Test Constructive Coverage and Refresh Dependent Explanations"
section_id: "F.0.2.RC:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.2.RC/F.0.2.RC__011_architectural-rationale.md"
commit_sha: "5282e0d9d224431a858c8fccd4c1d5bd99dd565f"
heading_path:
  - "F.0.2.RC — Test Constructive Coverage and Refresh Dependent Explanations"
  - "F.0.2.RC:10 — Architectural Rationale"
line_start: 116459
line_end: 116464
dependencies:
  - "A.10.1"
  - "A.3.1.CC"
  - "C.39.MC"
  - "E.8.ML"
  - "F.0.1"
  - "F.0.2"
keywords:
---

### F.0.2.RC:10 - Architectural Rationale

A.3.1.CC begins with a potentially contradicted claim and locates its owner. This pattern can start earlier: a promised source contribution is missing, and the language may not yet expose the claim or relation that should own it. Reconstruction finds that loss and supplies the repair question.

Combining falsification with affected refresh keeps the original promise and its change history connected. A.3.1.MV still decides whether reusable Method semantics changed; a missing description condition is not automatically a new Method variant.

