---
chunk_kind: "child"
pattern_id: "B.2.4"
pattern_title: "Meta-Functional Transition (MFT)"
section_id: "B.2.4:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.4/B.2.4__007_conformance-checklist.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "B.2.4 — Meta-Functional Transition (MFT)"
  - "B.2.4:6 — Conformance Checklist"
line_start: 30293
line_end: 30299
dependencies:
  - "A.3.1"
  - "B.2"
  - "B.2.1"
keywords:
  - "adaptive workflow"
  - "capability emergence"
  - "functional emergence"
  - "new process"
---

### B.2.4:6 - **Conformance Checklist**

*   **CC-B2.4.1 (MFT Declaration Mandate):** The emergence of a composite `U.Method` with supervisory properties **MUST** be declared as an MFT and justified with a **Promotion Record** (Pattern B.2) that provides evidence for the B-O-S-C triggers.
*   **CC-B2.4.2 (Method-Holon Mandate):** Both the constituent functions and the resulting composite function **MUST** be modeled as `U.Method`s, documented by `U.MethodDescription`s, and enacted as `U.Work`. They are not `U.System`s.
*   **CC-B2.4.3 (Supervisor Relation Mandate):** The "meta" nature of the emergent `U.Method` **MUST** be modeled through explicit relations, such as `controls` or `supervises`, linking the `Transformer` enacting the composite `Method` to the execution of the constituent `Method`s. A new `U.MetaMethod` type **SHALL NOT** be created.
*   **CC-B2.4.4 (Interface Standard):** The emergent `U.Method` **MUST** have a formally documented interface Standard (`Method Interface Standard` or MIC, see Pattern B.1.5), which specifies how the external world interacts with it and how the internal methods are encapsulated.

