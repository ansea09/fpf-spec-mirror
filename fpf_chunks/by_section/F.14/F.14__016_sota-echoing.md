---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:15"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__016_sota-echoing.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:15 — SoTA-Echoing"
line_start: 91796
line_end: 91805
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

### F.14:15 - SoTA-Echoing

**SoTA note.** F.14 does not import access-control, policy, terminology, or status taxonomies as FPF ontology. It uses their shared discipline: separate the named value from assignment, permission, status, evidence, and currentness claims before making a durable name.

| Current pressure | Practice line | F.14 adoption |
| --- | --- | --- |
| Role labels alone are too weak for authorization, work attribution, or capability claims. | RBAC lineage, ABAC, zero-trust, and policy-as-code practice separate role-like attributes, current context, policy decision, resource action, and evidence. | Keep role names separate from holder assignment, capability, policy, and work; use A.2.1, A.2.2, A.2.5, A.15.1, and direct policy and evidence patterns. |
| Terminology work distinguishes terms, concepts, designations, and contexts. | Current terminology and ontology practice treats a shared term as insufficient for identity. | Recover the value first; use F.9, F.17, and F.18 before public or cross-context reuse. |
| Status dashboards and presentation labels often hide criteria. | Operational monitoring and assurance practice separates indicator, threshold, time window, status value, evidence, and decision. | Keep status family, status value, window, evidence, and presentation separate; use F.10, A.10, B.3, and E.17. |

