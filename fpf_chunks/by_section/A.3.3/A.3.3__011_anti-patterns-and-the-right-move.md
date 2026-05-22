---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics"
section_id: "A.3.3:10"
section_title: "Anti‑patterns (and the right move)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__011_anti-patterns-and-the-right-move.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.3.3 — U.Dynamics"
  - "A.3.3:10 — Anti‑patterns (and the right move)"
line_start: 6552
line_end: 6572
dependencies:
  - "A.19"
  - "B.4"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:10 - Anti‑patterns (and the right move)

* **“Dynamics = procedure.”**
  Control recipes/step graphs belong to `Method or MethodDescription`. Keep the law in `U.Dynamics`.

* **“Telemetry = dynamics.”**
  Logs are `Work` evidence. Build `trace(Work, D)` and compare to the law; do not store logs inside the law.

* **“No state space.”**
  KPI lists without an explicit `stateSpace` turn into dashboard folklore. Name characteristics with units and ranges.

* **“Hard‑coding SLO inside the law.”**
  Service targets are promises (`U.PromiseContent.acceptanceSpec`). Keep predictions and promises separate; link them.

* **“Stuffing Dynamics into BoM.”**
  A model is not a component. Leave PBS/SBS for structure.

* **“One size fits all time base.”**
  If parts of the system evolve on different clocks, declare `hybrid` and separate update rules.


