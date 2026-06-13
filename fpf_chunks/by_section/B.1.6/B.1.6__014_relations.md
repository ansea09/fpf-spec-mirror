---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__014_relations.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:13 — Relations"
line_start: 31373
line_end: 31392
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "B.1"
  - "B.1.2"
  - "B.1.4"
  - "B.1.5"
  - "C.5"
keywords:
  - "Resrc-CAL"
  - "cost"
  - "energy consumption"
  - "resource aggregation"
  - "work"
---

### B.1.6:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: an authored claim that planned effort, actual effort trace, resource burn, effort window, resistance, or cost changes a temporal outcome.
- This pattern keeps: `Gamma_work` actual work/resource aggregation; `Gamma_time` declared temporal slices and phase composition remain separate.
- Non-admissible use: work logs, resource aggregation, or phase names do not by themselves infer acceleration, transition law, causal proof, or benchmark result.
- Exit: use C.27 only for the temporal-claim adequacy question; use work/resource patterns for actual work evidence and cite dynamics, causal/evaluation, or benchmark patterns when those other questions are live.

* **Builds on:** A.12 **Transformer Principle**; A.14 **Mereology Extension** (PortionOf, PhaseOf); A.15 **Strict Distinction** (MethodDescription / Method / Work).
* **Coordinates with:** B.1.5 **Γ\_method** (order and concurrency), B.1.4 **Γ\_time** (temporal coverage), B.1.2 **Γ\_sys** (system assembly).
* **Triggers:** B.2 **Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes** when feasibility constraints (WLNK) are beaten by structural redundancy/substitution.
* **Feeds:** B.3 **Trust & Assurance Calculus (F–G–R with Congruence)** (cost‑aware confidence overlays) — informative only, without altering Γ\_work’s conservation semantics.

> **Summary for practitioners.**
> Use **Γ\_method** to say **what happens and in which order**.
> Use **Γ\_work** to say **what it costs across a boundary**.
> Keep boundaries, time windows, units, yields, and transformers explicit.
> When apparent “free gains” appear, declare the structural change (MHT) and apply the same algebra one level up.

