---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 91109
line_end: 91122
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
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
  - "G.6"
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
| Interpretation tag in label | `Participant-BPMN`, `Task-IEC61131`, `ReviewerRole-SchemeA` | Put source, edition, role taxonomy, and effective reference scheme in their governing episteme or Name Card; keep the label clean. |
| Witness capture | `Observation` chosen because one standard uses it | Recover the exact value and its `E.24.UK` or direct-pattern admission; use the Concept-Set row only as witness-comparison evidence, then choose a neutral head if the admitted witnesses diverge. |
| Role and status fusion | `ApprovedReviewerRole`, `AccessRole` treated as work-facing role | Separate `U.Role` from status-use, policy relation, or access relation before naming. |
| Evidence role revival | `EvidenceRole` kept as durable role ontology | Recover evidence-use relation slots and name that relation only if needed. |
| Verbified role | `Reviewing` used as a role label | Use role noun for `U.Role`; use method or work patterns if the current claim is action or occurrence. |
| Slot role | `ProviderRole` names a relation argument | Use `ProviderSlot` or another slot head under `A.6.5`. |
| Threshold in name | `CriticalReviewer0.2mmRole` | Put threshold, capability envelope, or window in the governing pattern. |
| Alias spray | Several Tech labels for one meaning | Keep one Tech label; place other strings in alias or lineage records under `F.18` or `F.13`. |
| Decorative precision | `CanonicalActionStatus`, `ValidatedRoleCue` | Recover the governed kind and relation; do not replace one umbrella with another. |

