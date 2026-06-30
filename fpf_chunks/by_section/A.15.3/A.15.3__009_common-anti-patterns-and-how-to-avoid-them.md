---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 22691
line_end: 22701
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

### A.15.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Plan-as-execution | The plan contains launch values, witnesses, decision logs, or actual fillers. | Record actuals under performed `U.Work`, gate, evidence, or result records; leave planned rows in A.15.3. |
| Latest-as-baseline | "Latest" is used where replay needs a pinned edition or time rule. | Add time selector and edition pins, or lower to a plan cue. |
| View-as-baseline | A card, dashboard, or generated page becomes the row source. | Make the PlanItem rows authoritative and treat the view as E.17 projection. |
| Mechanism-prose baseline | Suite or mechanism prose hides plan-instance choices. | Put suite meaning in the suite pattern and planned fillers in A.15.3. |
| Generic ref placeholder | `SpecRef`, `PolicyRef`, or `GateRef` is used without concrete RefKind. | Use the concrete RefKind defined by the governing pattern, or block until one exists. |
| Backfilled plan | Performed work edits the plan after the fact so variance disappears. | Preserve the cited PlanItem; record variance, substitution, or crossing witness in performed work or the governing gate, evidence, result, or variance relation. |

