---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__013_rationale.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:11 — Rationale"
line_start: 2941
line_end: 2954
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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

### A.2:11 - Rationale

Roles solve a participation problem, not a system-identity problem. The pump does not become a new system because it is used as a cooling circulator, and the person does not become a new system kind because a verification assignment starts. `U.Role` names what the holder is being; `U.RoleAssignment` states who holds that role and when.

The selected ontology keeps three levels separate:

1. the role value interpreted through a role-taxonomy episteme and effective reference scheme;
2. the obtaining `U.RoleAssignment` relation occurrence linking holder, role value, taxonomy episteme, and scheme, with its actual extent derived from uninterrupted obtaining and described separately;
3. direct neighboring relations for role state, capability, method admission, responsibility, commitment, work, transformation, evidence, reliance, description, and publication.

This separation explains why `U.Role` is not a holon. Proposed role "parts" do not pass a constructive assembly and meta-holon transition test for the role value. They repeatedly resolve into relation occurrences, predicates, other role values, method or work structures, or parts of description epistemes. The useful structure is therefore the selected role relation structure governed by `A.2.7`, not role mereology.

Semantic locality also does not require a universal bounded context. The role-taxonomy episteme and reference scheme ordinarily suffice. A receiving assertion or use may designate a selected `BoundedModelUseStructure` only in the narrower case where an actual model-use organization changes that interpretation.

