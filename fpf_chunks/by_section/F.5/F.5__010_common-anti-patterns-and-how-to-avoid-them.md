---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 88484
line_end: 88497
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
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
keywords:
  - "U-kind naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "role-description labels"
  - "twin registers"
---

### F.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Context tag in label | `Participant-BPMN`, `Task-IEC61131` | Put context and edition in Context or SenseCell fields; keep label clean. |
| Witness capture | `Observation` chosen because one standard uses it | Check the Concept-Set row; choose a neutral head if witnesses diverge. |
| Role and status fusion | `ApprovedReviewerRole`, `AccessRole` treated as work-facing role | Separate `U.Role` from status-use, policy relation, or access relation before naming. |
| Evidence role revival | `EvidenceRole` kept as durable role ontology | Recover evidence-use relation slots and name that relation only if needed. |
| Verbified role | `Reviewing` used as a role label | Use role noun for `U.Role`; use method or work patterns if the current claim is action or occurrence. |
| Slot role | `ProviderRole` names a relation argument | Use `ProviderSlot` or another slot head under `A.6.5`. |
| Threshold in name | `CriticalReviewer0.2mmRole` | Put threshold, capability envelope, or window in the governing pattern. |
| Alias spray | Several Tech labels for one meaning | Keep one Tech label; place other strings in alias or lineage records under `F.18` or `F.13`. |
| Decorative precision | `CanonicalActionStatus`, `ValidatedRoleCue` | Recover the governed kind and relation; do not replace one umbrella with another. |

