---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility & Value Alignment"
section_id: "E.13:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__006_conformance-checklist.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "E.13 — Pragmatic Utility & Value Alignment"
  - "E.13:5 — Conformance Checklist"
line_start: 61389
line_end: 61395
dependencies:
  - "E.12"
  - "E.2"
keywords:
  - "Goodhart's Law"
  - "MVE"
  - "Proxy-Audit Loop"
  - "pragmatic"
  - "utility"
  - "value"
---

### E.13:5 - **Conformance Checklist**

*   **CC-E13.1 (Proxy Declaration Mandate):** Any `U.Characteristic` used as a primary driver for an objective **MUST** be explicitly linked to that `U.Objective` via the `isProxyFor` relation.
*   **CC-E13.2 (Proxy-Audit Mandate):** A formal Proxy-Audit review **MUST** be conducted at regular conceptual intervals (e.g., before each major release). The outcome of this review **MUST** be a documented episteme.
*   **CC-E13.3 (MVE Mandate):** The development of any new `U.System` **MUST** be preceded by the creation of an MVE that satisfies the `AssuranceLevel:L1` requirement.
*   **CC-E13.4 (MVE Traceability):** The full-scale `U.System` **MUST** maintain a formal traceability link (`isEvolutionOf`) to its originating MVE.

