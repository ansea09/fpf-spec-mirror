---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__008_conformance-checklist.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:6 — Conformance Checklist"
line_start: 24385
line_end: 24397
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "C.16"
  - "E.16"
  - "F.6"
keywords:
  - "autonomy grading"
  - "classification"
  - "conditional characteristic profile"
  - "evidence-backed core"
  - "exact System"
  - "local agential system-role kind and criterion"
  - "obtaining assignment"
  - "scope"
  - "window"
  - "working situation"
---

### A.13:6 - Conformance Checklist

Apply these normative checks to the corresponding agency, profile or Grade claim in an FPF publication:

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A13.1 (Holder Type)** | The holder System of an obtaining agential `U.SystemRoleAssignment` **MUST** be a `U.System`. | Prevents the "episteme-as-actor" category error. Enforces **Strict Distinction (A.7)**. |
| **CC-A13.2 (Assignment Mandate)** | A precise claim of agency **MUST** name the exact local agential system-role kind and an obtaining occurrence of a directly declared `U.SystemRoleAssignment` species. Any claim scope, working situation, and time window needed by the use remain separate. | Binds agency to a specific holder and assignment without turning a generic context field into their identity. |
| **CC-A13.3 (Characteristic Evidence)** | Any claim about a holder’s Agency Grade or autonomy profile **MUST** be substantiated by an auditable agency-characteristic profile with Evidence Graph Ref (A.10). | Requires support for the Grade or profile claim. |
| **CC-A13.4 (Grade is Didactic)** | The **Agency Grade (0-4)** **SHALL NOT** be used as a normative input for formal reasoning. It is a didactic summary of the agency-characteristic profile. | An assurance case that consumes these characteristics uses their supported values, not the Grade. |
| **CC-A13.5 (Collective as System)** | To claim agency for a collective (e.g., a team or swarm), it **MUST** first be admitted as a `U.System` under the complete A.1 criterion. Identify its defined boundary and coordination `U.Method`; those two features alone do not establish Systemhood. | Distinguishes an admitted collective System from a mere set or collection (`MemberOf`); parthood claims use A.14. |
| **CC-A13.6 (MHT for Emergent Agency)** | If a collection of Systems develops a new supervisory structure and crosses a documented agency-characteristic threshold, apply B.2’s whole-reidentification test. When B.2 establishes the transition, a **Meta-Holon Transition (MHT)** **MUST** be declared. | Supervision and threshold crossing prompt the inquiry. If the same whole explains the changed facts, stop without MHT. A prior description as non-agential or at a lower didactic Grade may describe the starting case; it is not a normative premise. |

