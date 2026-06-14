---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:11"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__012_relations.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:11 — Relations"
line_start: 33007
line_end: 33019
dependencies:
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.3"
  - "B.3.5"
  - "B.3.x"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "D.4"
  - "E.14"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

### B.3:11 - Relations

* **Builds on:** B.1 (Universal Γ), B.1.1 (Proof Kit), B.1.2 (Γ_sys and BIC), B.1.3 (Γ_epist and SCR), B.1.4 (Γ_ctx and Γ_time), A.12 (Transformer), A.14 (Mereology), A.7 (EntityOfConcern and Description strict distinction) and A.15 (role, method, and work alignment), **C.13 (Compose-CAL)**.
* **Coordinates with:** **E.14 (Human‑Centric Working‑Model)** for publication-facing assertion discipline and **B.3.5 (CT2R‑LOG)** for Working‑Model relation aliasing and grounding (`tv:*`, `validationMode`).
* **Coordinates with:** `C.28` for `CausalUseSupportVerdict`, `CausalityLadderRung`, `CausalEvidenceSupportBasis`, identification profile refs, realizability profile refs, supported causal use, and unsupported causal use; `A.10` for the evidence graph path carrying causal-evidence refs.
* **Coordinates with:** `A.15` for work disposition and reliance disposition, `A.6` for mixed authority wording, `A.21` for `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`, `A.20` for `ConstraintValidity` status or witness, and `A.15.1` for release or deployment work occurrence. B.3 only handles typed assurance use; labels and evidence pointers stay with the source relation that governs them when assurance is not being claimed.
* **Used by:** KD-CAL improvement patterns (to plan improvements), B.4 (Evolution loops that raise `F`, `G`, `R`, or `CL` over time).
* **Triggers:** B.2 (Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes) when genuine new capabilities emerge that change the applicable cutsets or envelopes.

> **One‑page takeaway.**
> Report assurance as **⟨F, G, R⟩** for a **typed claim** under explicit **context and scope**, and penalize by the **lowest edge-scoped Congruence Level (`CL`) value**.
> Improve assurance by raising **F**, **G**, **R**, or **CL**—and keep order, time, and cost in their own lanes.

