---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__007_conformance-checklist.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:6 — Conformance Checklist"
line_start: 24150
line_end: 24162
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
  - "C.9"
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

To ensure the agency model is applied rigorously and consistently, all FPF publications must adhere to the following normative checks.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A13.1 (Holder Type)** | The holder System of an obtaining agential `U.SystemRoleAssignment` **MUST** be a `U.System`. | Prevents the "episteme-as-actor" category error. Enforces **Strict Distinction (A.7)**. |
| **CC-A13.2 (Assignment Mandate)** | A precise claim of agency **MUST** name the exact local agential system-role kind and an obtaining occurrence of a directly declared `U.SystemRoleAssignment` species. Any claim scope, working situation, and time window needed by the use remain separate. | Binds agency to a specific holder and assignment without turning a generic context field into their identity. |
| **CC-A13.3 (Characteristic Evidence)** | Any claim about a holder's Agency Grade or autonomy profile **MUST** be substantiated by an auditable agency-characteristic profile with Evidence Graph Ref (A.10). | Makes claims of agency falsifiable and prevents "agency by marketing." |
| **CC-A13.4 (Grade is Didactic)**| The **Agency Grade (0-4)** **SHALL NOT** be used as a normative input for formal reasoning. It is a didactic summary of the agency-characteristic profile. | Prevents oversimplification in formal models. The detailed profile, not the summary grade, must be used for assurance cases. |
| **CC-A13.5 (Collective as System)** | To claim agency for a collective (e.g., a team, a swarm), the collective **MUST** first be modeled as a `U.System` with a defined `U.Boundary` and a coordination `U.Method`. | Prevents the error of assigning agency to a mere set or collection (`MemberOf`). Aligns with **A.1** and **A.14**. |
| **CC-A13.6 (MHT for Emergent Agency)** | If a collection of systems, previously non-agential or at a lower grade, develops a new supervisory structure and crosses a documented agency-characteristic threshold, a **Meta-Holon Transition (MHT, B.2)** **MUST** be declared. | Makes the emergence of collective agency an explicit, auditable event, preventing "magic" emergence. |

