---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__014_relations.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:13 — Relations"
line_start: 62902
line_end: 62918
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
  - "E.23"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "adaptation signature"
  - "budget-to-threshold"
  - "corridor entry"
  - "downside field"
  - "prior exposure"
  - "retention"
  - "stepping stone"
  - "task-family specialization"
  - "time-to-threshold"
  - "transfer"
---

### C.22.1:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim that a holder, dyad, team, explicitly scoped specialist portfolio, or agent acquires usable specialization faster on one declared `TaskFamilyRef` or `TaskSignature`. A method may be selected, refined, or retired as part of that story.
- This pattern keeps: threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, corridor-entry evidence, and adaptation-signature fields.
- Generic "learns faster" wording without a task-family anchor leaves the adaptation claim incomplete. Faster threshold crossing alone does not establish durable specialization; retention needs its own window and evidence, and any additional transfer, downside or corridor-entry claim needs its stated grounds.

- Next-question boundary: classify the claim as Dyn1 when only a trend is live; use C.24 for call planning after the action or option is fixed; use the C.22.1 adaptation signature when specialization is the live adaptation question.

**Builds on:** `C.22` TaskSignature anchoring, `C.19.1` `BLP` compatibility, `A.15` system-role-kind and assignment, Method, WorkPlan, and Work-occurrence separation, `C.24` call planning and `CheckpointReturn` semantics after the action or option is fixed, `E.16` budget enforcement.
**Coordinates with:** `G.5` selector specialization profiles, `G.9` adaptation parity, `G.11` later telemetry/refresh reuse.

**Coordinates with:** `E.23` when repeated object improvement includes a claim of durable task-family specialization. C.22.1 supplies the adaptation account for that claim; E.23 governs the improvement loop.

**Constrained by:** `E.10` lexical discipline.

