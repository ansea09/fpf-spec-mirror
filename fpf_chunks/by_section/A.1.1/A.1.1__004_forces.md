---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__004_forces.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:3 — Forces"
line_start: 1347
line_end: 1373
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

### A.1.1:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Local coherence** | A context must be internally unambiguous ↔ real work crosses boundaries and needs translation. |
| **Pluralism** | Multiple valid frames must coexist ↔ readers demand apparent “one truth”. |
| **Governance cost** | Explicit boundaries and rules improve reliability ↔ too many contexts create overhead and fragmentation. |
| **Evolvability** | Contexts must change over time ↔ change must remain traceable and non-destructive to prior meaning. |
| **Familiarity** | Practitioners use domain-native vocabulary ↔ the kernel must stay universal and type-stable. |
| **Domain-family convenience** | People want “the domain” as a handle ↔ FPF requires specific, named semantic frames. |

#### A.1.1:3.1 - Prophylactic clarification — Domain family vs `U.BoundedContext`

To prevent a common category error, **Domain (as used colloquially)** and **`U.BoundedContext`** are **not synonyms** in FPF, and “Domain” is not a kernel type.
Per **E.10.D1 (D.CTX)**, **Domain is an informative family label** grouping multiple contexts; there is no “domain context”.

| Characteristic | **Domain family (informative)** (e.g., Healthcare, Physics, Workflow) | **`U.BoundedContext`** (e.g., `Hospital.OR_2025`, `Theory:QuantumMechanics`, `BPMN_2_0`) |
| :--- | :--- | :--- |
| **Nature** | An external field of practice/knowledge; a catalog handle. | An internal FPF holon: a named semantic frame with local vocabulary and local invariants. |
| **Role in FPF** | Groups contexts for survey, coverage, and stewardship discussions. | Localizes meaning and rules; provides a semantic firewall where words and obligations are coherent. |
| **Relationship** | One family contains many legitimate perspectives/editions. | One context carries one such perspective with explicit `Glossary`, `Invariants`, `Roles`, and optional `Bridges`. |

**Well-formedness constraint (didactic):** In any `U.RoleAssignment`, `context` is total and points to **exactly one** `U.BoundedContext` (cardinality **1..1**).
*Think “specific room” (e.g., `Hospital.OR_2025`), not “the whole building” (e.g., “Healthcare”).*

**Manager’s one-liner:** A **Domain family** is the *territory label*; a **Bounded Context** is a *purpose-made map* of one perspective on that territory.

