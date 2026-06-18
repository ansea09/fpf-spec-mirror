---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__013_relations.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:12 — Relations"
line_start: 34002
line_end: 34013
dependencies:
  - "A.10"
  - "A.16"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:12 - Relations

- **Is the first reasoning phase within:** `B.5 Canonical Reasoning Cycle`.
- **Typically operates during:** `B.5.1 Exploration`.
- **Consumes:** `U.AbductivePrompt` publications from `B.5.2.0`, often reached through `B.4.1` and `A.16`.
- **Produces:** hypothesis-bearing `U.Episteme` publications at `AssuranceLevel:L0`.
- **Feeds:** downstream deduction, probe design, and evidence acquisition in the later reasoning cycle.

#### B.5.2:12.1 - Prompt-entry broadening via `U.AbductivePrompt`

Older wording that makes `AnomalyStatement` the exclusive entry form is superseded. `B.5.2` accepts `U.AbductivePrompt`, where `AnomalyStatement` remains one canonical species alongside cue-derived prompt species such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`.

