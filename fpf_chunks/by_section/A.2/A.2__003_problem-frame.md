---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__003_problem-frame.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:1 — Problem Frame"
line_start: 2699
line_end: 2706
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:1 - Problem Frame

FPF needs role language because the same holon can be used, treated, expected, or named differently in different bounded contexts. A pump can be a cooling circulator in one plant context and a test article in another. A person can be verifier in one work package and author in another. A service can be supplier in one agreement-like relation and consumer in another. Without a role value, these contextual uses either become new system subtypes or remain vague source language.

At the same time, role language is dangerous. Everyday phrases such as "the role of this standard", "the role of this dataset", "the role of this theorem", "the role of this dashboard", or "the role of this interface" can hide several different FPF claims. They may be evidence-use, source-use, publication-use, status-use, requirement-use, explanation-use, interface, signature, capability, method, or work claims. They are not automatically `U.Role` claims.

A.2 therefore keeps `U.Role` real, but narrow. A role is a context-bound enactment-facing role value. Enactment-facing does not mean "human job" or "social agent only": a motor can be assigned as a drive motor, a pump can be assigned as a cooling circulator, and a valve can be assigned as a regulator inside a functional or transformation context. A method or method description may name role-admission conditions; performed work cites a `U.RoleAssignment`; transformation and functioning claims may also need the same role value. A role becomes operational through neighboring relations, especially `U.RoleAssignment` in `A.2.1`, role-method-work alignment in `A.15`, transformation participation in `A.3.4`, and functional precision restoration in `A.6.F` when function wording is current. It does not absorb every relation in which a value participates.

