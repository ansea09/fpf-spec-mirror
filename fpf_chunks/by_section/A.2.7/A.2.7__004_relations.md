---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "U.RoleAlgebra: In‑Context Role Relations"
section_id: "A.2.7:3"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__004_relations.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.2.7 — U.RoleAlgebra: In‑Context Role Relations"
  - "A.2.7:3 — Relations"
line_start: 4959
line_end: 4971
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "U.BoundedContext"
  - "U.RoleAssignment"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:3 - Relations

**Builds on / depends on**

* **A.1.1 `U.BoundedContext`** — the locality boundary within which the algebra holds.
* **A.2 Role Taxonomy** — role families and context‑local naming.

**Used by**

* **A.2.1 `U.RoleAssignment`** — avoids chained assignments; uses `≤/⊥/⊗` for checking and validation.
* **A.15 Role–Method–Work Alignment** — expands `requiredRoles` and enforces SoD requirements.
* **D.2** ethics/governance patterns — encode SoD and independence via `⊥`.

