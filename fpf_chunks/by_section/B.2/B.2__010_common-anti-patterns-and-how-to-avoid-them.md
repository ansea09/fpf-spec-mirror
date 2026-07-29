---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta-Holon Transition - Whole Reidentification"
section_id: "B.2:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "B.2 — Meta-Holon Transition - Whole Reidentification"
  - "B.2:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 37078
line_end: 37089
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "B.1"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30.ILC"
  - "C.32.P2S"
  - "E.24.UK"
  - "G.11"
  - "U.Episteme"
keywords:
---

### B.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Emergence by adjective | A capability or property is called emergent without reidentifying the whole. | Use `B.2.P` to recover claim kind, then B.2 only if whole reidentification is current. |
| Record as ontology | Trigger profile, result field, or record name is treated as a world-side kind. | Keep profile, check, and reidentification record as `U.Episteme` values; let `E.24.UK` govern the candidate new whole's public kind and A.1 govern recognition of that candidate. |
| Content field as relation slot | A reference field inside a profile or record is treated as a participant SlotKind or as evidence that the referenced relation obtains. | Keep the field in episteme content, resolve its reference to the direct occurrence, and use that occurrence's governing pattern for obtaining and identity. |
| KPI jump as MHT | A metric improves and MHT is declared. | Run `ExistingWholeExplanationCheck`; use the direct measurement, characteristic, method, work, or architecture pattern when it explains the change. |
| Agency shortcut | Agency threshold crossing creates a new root kind. | Use the direct characteristic-space and threshold patterns; apply B.2 only when closure, supervision, objective, or identity changes. |
| Math result as MHT | Graph, RG-like, MSPD, or benchmark expression declares new whole. | Use `C.29`; recover holon identity before B.2. |
| Transformation as containment | A system changes another holon and is treated as its super-holon. | Use A.12, A.3.4, A.15.1, and the direct crossing relation pattern; use parthood only when an exact grounded part relation independently obtains. |

