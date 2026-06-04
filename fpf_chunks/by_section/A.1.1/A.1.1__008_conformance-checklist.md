---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__008_conformance-checklist.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:7 — Conformance Checklist"
line_start: 1433
line_end: 1446
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

### A.1.1:7 - Conformance Checklist

To ensure `U.BoundedContext` is used consistently and rigorously, the following normative checks apply.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A1.1.1 (Holon Nature)** | A `U.BoundedContext` **MUST** be modeled as a `U.Holon` with a defined `U.Boundary`. | Reinforces that contexts are well-defined entities, not vague groupings. Enables reasoning about contexts themselves as systems. |
| **CC-A1.1.2 (Flat Context Map)** | A `U.BoundedContext` **MUST NOT** be modeled as inheriting from, containing, or being contained by another `U.BoundedContext`. Cross-context relations **MUST** be expressed only via explicit `Bridges` (E.10.D1 / E.10.U9). | Prevents semantic leakage and hidden globalism; keeps cross-context translation auditable and loss-aware. |
| **CC-A1.1.3 (Role Localization)** | Every `U.Role` **MUST** be defined within the `Roles` taxonomy of at least one `U.BoundedContext`. A "global role" is forbidden. | Ensures roles are never context-free; meaning remains local and checkable. |
| **CC-A1.1.4 (Invariant Scope)** | An invariant defined within a context **MUST** only apply to holons and processes operating *within* that context. | Prevents local rules from leaking into global reasoning; preserves modularity. |
| **CC-A1.1.5 (Bridge Explicitness)** | Any interaction or alignment between two `U.BoundedContext`s **MUST** be modeled as an explicit `Bridge` record. | Forbids implicit cross-context equivalences; makes dependencies visible and auditable. |
| **CC-A1.1.6 (RoleAssignment Context Binding)** | Every `U.RoleAssignment` **MUST** reference exactly one `U.BoundedContext` in its `context` field (cardinality 1..1). | Guarantees that each assignment is interpreted in one authoritative frame of meaning. |
| **CC-A1.1.7 (Domain family is informative)** | “Domain context” **MUST NOT** appear in normative prose; Domain labels **MAY** appear only as informative family metadata that groups multiple contexts (E.10.D1). | Prevents the domain/context conflation that breaks locality and auditability. |

