---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__004_forces.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:3 — Forces"
line_start: 23271
line_end: 23281
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.7"
  - "B.3"
  - "C.27.TA"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.20"
  - "E.24"
  - "G.11"
  - "G.6"
  - "U.RelationSlotDiscipline"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:3 - Forces

| Force | Demand |
| --- | --- |
| WorkPlanning vs performed work | The baseline should be citeable before work without containing actuals, launch values, or gate outcomes. |
| Slot meaning stability | The plan can choose fillers; it cannot redefine the SlotKinds of the target description. |
| Edition and time honesty | References that matter for reproducibility need edition and time pins. |
| Suite and kit modularity | Suite descriptions can require planned baselines, but each plan instance still chooses its fillers separately. |
| Publication affordability | Cards and views help people read the baseline, but they cannot become a second canonical row source. |
| Audit and improvement | Later work needs a stable planned baseline so variance can be attributed and improved. |

