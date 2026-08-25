---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
section_id: "F.5:8"
section_title: "Common Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__010_common-anti-patterns-and-repairs.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
  - "F.5:8 — Common Anti-Patterns and Repairs"
line_start: 91124
line_end: 91137
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.3"
  - "C.3.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.6"
keywords:
  - "Plain and Tech designations"
  - "SystemRoleKindDescription label"
  - "U-kind name"
  - "local meaning"
  - "naming after ontology recovery"
  - "system-role-kind name"
---

### F.5:8 - Common Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Interpretation tag in label | `Participant-BPMN`, `Task-IEC61131`, `ReviewerSystemRole-SchemeA` | Put source, edition, local boundary, and scheme in the direct declaration, description, or NameCard. |
| Witness capture | `Observation` chosen because one standard uses it | Recover the exact value and admission; use comparison evidence only as evidence, then choose a neutral head when witnesses diverge. |
| System role and status fusion | `ApprovedReviewerSystemRole` or `AccessRole` treated as a work-facing kind | Separate the local kind from status, policy, permission, and access relations. |
| Evidence role revival | `EvidenceRole` retained as durable ontology | Recover and, if needed, name the evidence-use relation. |
| Verbified system role | `Reviewing` used as a kind label | Use a concrete kind noun; use Method or Work patterns for action or occurrence. |
| Position role | `ProviderRole` names a relation argument | Use an exact slot or position name under A.6.RSIR and A.6.5. |
| Threshold in name | `CriticalReviewer0.2mmSystemRole` | Put threshold, capability envelope, or window in the direct claim. |
| Alias spray | Several Tech labels for one meaning | Keep one selected Tech designation; retain other strings as lineage or aliases under F.18 or F.13. |
| Decorative precision | `CanonicalActionStatus`, `ValidatedSystemRoleCue` | Recover the governed object and relation; do not replace one umbrella with another. |

