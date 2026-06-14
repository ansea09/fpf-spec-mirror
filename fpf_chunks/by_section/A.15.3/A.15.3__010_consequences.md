---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__010_consequences.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:9 — Consequences"
line_start: 21907
line_end: 21915
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
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

| Benefit | Trade-off and cost | Notes and mitigation |
| --- | --- | --- |
| Improved modularity | Requires an explicit baseline plan item | Keep baselines minimal; specialise only when a suite truly needs it. |
| Audit clarity | More up-front specification work | The explicit-writing workload is intentional: it buys attributable variance and prevents “mystery defaults”. |
| Edition honesty | Forces practitioners to declare editions and time | Use editioned refs and time selectors by ref; keep actual `Γ_time` in Work evidence. |
| Controlled specialisation | Multiple PlanItem kinds may exist (core + suite‑specialised) | Create a suite-specific refinement only when the suite description requires it; keep the universal core stable. |

