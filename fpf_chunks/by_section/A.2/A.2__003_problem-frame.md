---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__003_problem-frame.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:1 — Problem Frame"
line_start: 2733
line_end: 2740
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

### A.2:1 - Problem Frame

One system can participate differently while retaining its system identity. `PumpUnit-3` remains the same pump while it holds `CoolingCirculatorRole` in plant operation and `TestArticleRole` in qualification work. A person remains the same person while holding author and verifier roles in different assignments. Role values let a project name these differences without inventing a new system kind for each participation.

Role meaning is not global. A role-taxonomy episteme contains the vocabulary and relation claims through which a role value is interpreted, and an effective `U.ReferenceScheme` fixes the current interpretation. `U.RoleAssignment` then states which admitted system holds the role and during which uninterrupted occurrence. When a selected `BoundedModelUseStructure` changes one receiving interpretation, the receiving assertion or work use may designate that structure; it is not an optional participant of the generic role relations.

Ordinary language also uses `role` to mean contribution. A design method may use a standard publication as the source for a constraint claim, a report may participate in an evidence relation, and a value may fill a participant slot of another relation. Those are useful claims, but none makes the episteme or slot filler a role holder. The direct relation must be recovered before the wording becomes relied-on FPF content.

