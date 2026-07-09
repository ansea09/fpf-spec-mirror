---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__014_relations.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:13 — Relations"
line_start: 47721
line_end: 47737
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
  - "E.19"
  - "E.22"
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

- C.27 may flag: a claim that a holder, dyad, team, specialist portfolio, method, or agent acquires usable specialization faster on one declared `TaskFamilyRef` or `TaskSignature`.
- This pattern keeps: threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, corridor-entry evidence, and adaptation-signature fields.
- Non-admissible use: generic "learns faster" wording without task-family anchors does not create a C.27 profile or a complete adaptation signature; faster threshold crossing is not durable specialization unless transfer, retention, downside, and corridor-entry evidence are stated when claimed.

- Exit: downgrade to Dyn1 trend when only a trend is live; use C.24 when the question is only tool-use planning; use C.22.1 when specialization is the live adaptation question.

**Builds on:** `C.22` TaskSignature anchoring, `C.19.1` `BLP` compatibility, `A.15` role, method, work-plan, and work-occurrence separation, `C.24` scout/probe and `CheckpointReturn` semantics, `E.16` budget enforcement.
**Coordinates with:** `G.5` selector specialization profiles, `G.9` adaptation parity, `G.11` later telemetry/refresh reuse.

**Coordinates with:** `E.23` when a quality-improvement loop claims durable task-family specialization. `C.22.1` carries the adaptation-signature fields for threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, and corridor entry; it does not restate the `E.23` loop method, `E.22` review framing, or pattern-quality or DRR-adequacy object-under-improvement evaluations.

**Constrained by:** `E.10` lexical discipline and `E.19` pattern-quality review when this child section is newly landed or materially revised.

