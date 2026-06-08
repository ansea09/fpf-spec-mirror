---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__007_conformance-checklist.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:6 — Conformance Checklist"
line_start: 32732
line_end: 32739
dependencies:
  - "A.12"
  - "A.4"
  - "B.4.1-B.4.3"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:6 - **Conformance Checklist**

*   **CC-B4.1 (Loop Integrity):** Any evolutionary change to a holon **MUST** be documented as a full traversal of the four-phase loop. Ad-hoc changes that bypass a phase (e.g., deploying a refinement without a documented observation and evidence phase) are a process violation.
*   **CC-B4.2 (Temporal Scope Mandate):** The *Refine* phase **MUST** operate on `design-time` epistemes such as specifications, theories, source code, or method descriptions, while the *Operate* phase involves the `run-time` holon-in-operation. The *Observe* and *Deploy* phases are the only permissible bridges between these scopes.
*   **CC-B4.3 (Transformer Mandate):** The *Observe*, *Refine*, and *Deploy* transitions **MUST** be performed by an explicitly identified external `Transformer` (Pattern A.12). A holon cannot observe, refine, or deploy itself.
*   **CC-B4.4 (Adaptive-specialization anchoring):** When `B.4.2` or `B.4.3` carries a bounded-specialization claim, that claim **MUST** name the declared `TaskFamily` or `TaskSignature`, the work-measure threshold target, the adaptation budget, and the freshness or provenance basis for reuse.
*   **CC-B4.5 (Adaptive-specialization boundary):** `B.4.2` and `B.4.3` **SHALL NOT** silently re-govern selector or parity semantics. If transfer, retention, downstream exploitation efficiency, corridor entry, or downside cost are comparison-relevant, the pattern-local note **MUST** leave those fields recoverable by the downstream `C.22.1`, `G.5`, and `G.9` governing patterns.

