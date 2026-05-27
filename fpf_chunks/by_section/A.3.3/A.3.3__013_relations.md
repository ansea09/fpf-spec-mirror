---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics"
section_id: "A.3.3:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__013_relations.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.3.3 — U.Dynamics"
  - "A.3.3:12 — Relations"
line_start: 6593
line_end: 6616
dependencies:
  - "A.19"
  - "B.4"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim whose downstream use depends on a reusable transition law, prediction, simulation, calibrated control, or formal model.
- This pattern keeps: state space, transition law, observation/model constraints, simulation, prediction, calibrated control, and validity discipline.
- Non-admissible use: a `Dyn2TemporalClaimAdequacyCard` or Dyn2 classification is not a law of change, and `dynOrder` is not a property of the state space or transition law.
- Exit: if the answer requires a reusable law, prediction, simulation, or calibrated control model, the claim belongs with `U.Dynamics`; C.27 only cites that pattern relation and keeps the temporal-claim adequacy question.

* **Builds on:**
  `A.1.1 U.BoundedContext` (local meaning/units),
  `A.2 Role` / `A.2.1 RoleAssigning` (agents that *use* the law),
  `A.15.1 U.Work` (run‑time evidence).

* **Coordinates with:**
  `A.3.1 U.Method` / `A.3.2 U.MethodDescription` (planning/control using the law),
  `A.2.3 U.PromiseContent` (promises informed by predictions),
  **KD‑CAL** (knowledge dynamics as a specialisation: belief‑update laws),
  **Resrc‑CAL** (cost/energy models as dynamics over resources).

* **Constrained by lexical rules:**
  **E.10 L‑PROC** (process disambiguation), **L‑ACT** (activity/action), **L‑FUNC** (function).


