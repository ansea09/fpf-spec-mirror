---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__010_consequences.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:9 — Consequences"
line_start: 20475
line_end: 20483
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.8"
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

### A.15.3:9 - Consequences

| Benefit | Trade‑off / Cost | Notes / Mitigation |
| --- | --- | --- |
| Improved modularity | Requires an explicit baseline plan item | Keep baselines minimal; specialise only when a suite truly needs it. |
| Audit clarity | More up-front authoring work | The authoring workload is intentional: it buys attributable variance and prevents “mystery defaults”. |
| Edition honesty | Forces authors to think about editions and time | Use editioned refs and time selectors by ref; keep actual `Γ_time` in Work evidence. |
| Controlled specialisation | Multiple PlanItem kinds may exist (core + suite‑specialised) | Use DRR to document why specialisation is warranted; keep the universal core stable. |

