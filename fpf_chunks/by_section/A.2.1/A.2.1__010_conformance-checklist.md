---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__010_conformance-checklist.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:8 — Conformance Checklist"
line_start: 3245
line_end: 3261
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-A2.1-1 | The relation predicate states when one admitted `U.System` holds one `U.Role`. |
| CC-A2.1-2 | The `RelationSignature` declares each participant through one complete SlotSpec with exact SlotKind, ValueKind, and refMode. |
| CC-A2.1-3 | `AssignmentInterval` is assertion or occurrence-description content, not a relation-participant SlotSpec; it states one currently known continuous temporal extent. |
| CC-A2.1-4 | The identity rule uses the four stable participant fillings plus uninterrupted obtaining of the assignment predicate; representation keys remain separate. |
| CC-A2.1-5 | Closing an open interval can refine the same uninterrupted occurrence; a demonstrated non-assignment gap ends it. |
| CC-A2.1-6 | Generic `U.RoleAssignment` has exactly four participants; any selected model-use structure is designated only by a receiving assertion or use. |
| CC-A2.1-7 | Role state, capability, method admission, work, responsibility, decision, evidence, reliance, provenance, and publication are not assignment slots. |
| CC-A2.1-8 | Performed work is attributed through direct `performedUnderAssignment(W, RA)`; the actual performer is the admitted System in `RA.HolderSystemSlot`. |
| CC-A2.1-9 | An assignment assertion, roster row, identifier, and publication remain epistemic or representational objects distinct from the relation occurrence. |
| CC-A2.1-10 | Every reference filling has its exact RefKind and resolves to the ValueKind declared by that SlotSpec. |
| CC-A2.1-11 | An evidence gap is not treated as a demonstrated interval in which the assignment predicate failed. |
| CC-A2.1-12 | Reduced use stops before explicit individuation when no receiving use needs an assignment reference. |

