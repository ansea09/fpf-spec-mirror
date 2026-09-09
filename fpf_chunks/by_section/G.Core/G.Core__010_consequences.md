---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__010_consequences.md"
commit_sha: "886e84cadcc302e1c622aec02a0a0ba1e1c3955d"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:9 — Consequences"
line_start: 101574
line_end: 101581
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:9 - Consequences

* **Positive:** Part‑G patterns cite `G.Core` to find the governing definitions of shared invariants; refactors become safer and easier to audit.
* **Positive:** RSCR becomes reason-code driven (typed triggers), improving traceability and preventing semantic drift.
* **Positive:** Default conflicts become detectable and resolvable because each `DefaultId` names one governing definition.
* **Negative:** Adds an extra authoring step (linkage sections and CoreRef CC item) to each `G.x`.
* **Negative:** Requires careful governance of the trigger catalogue to avoid excessive fragmentation.

