---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:8"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__009_invariants.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:8 — Invariants"
line_start: 83203
line_end: 83213
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:8 - Invariants

1. **Kind first.** A candidate name is not admitted as a durable role or status name until its recovered value is named.
2. **No status roles.** Status, evidence, requirement, source, publication, and access uses do not become work-facing roles by suffix.
3. **No assignment by name.** A RoleDescription label or role-relation expression does not assign a holder and does not prove performed work.
4. **No hybrid role by convenience.** Role-bundle and incompatibility expressions stay in A.2.7 unless a bounded context deliberately creates a new role value with F.8 and F.18 admission.
5. **No capability by role label.** Role names do not prove capability, skill, permission, assurance, or method validity.
6. **Status windows stay status-side.** Time, confidence, grace, or presentation variation stays with F.10 or the direct status pattern unless a new status family is recovered.
7. **Cross-context reuse needs a bridge.** Shared labels across contexts use F.9 before any Concept-Set row, public name, or durable cross-context reuse.
8. **Lineage labels do not preserve ontology.** A historical label may be recorded as lineage or source wording, but it does not carry its old fused ontology forward.

