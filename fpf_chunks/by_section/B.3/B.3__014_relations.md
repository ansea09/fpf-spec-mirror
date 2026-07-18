---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:11"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__014_relations.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:11 — Relations"
line_start: 36139
line_end: 36151
dependencies:
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
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

* **Builds on:** B.1 where its current composition invariants are named by value, B.1.1 dependency-structure and relation-grounding checks, current system-composition, context, temporal, and work patterns when those operators are active, A.14 (Mereology), A.7 (EntityOfConcern and Description strict distinction), A.10 (evidence-provenance and carrier/source-currentness relations), A.15 (role, method, work-plan, and work alignment), A.2 and A.2.1 (role values and role assignments), A.3.4 (Transformation when actual change is current), and **C.13 (Compose-CAL)**.
* **Coordinates with:** **E.14 (Human‑Centric Working‑Model)** for publication-facing assertion discipline and **B.3.5 (CT2R‑LOG)** for Working‑Model relation label-meaning and grounding (`tv:*`, `validationMode`).
* **Coordinates with:** `C.28` for `CausalUseSupportVerdict`, `CausalityLadderRung`, `CausalEvidenceSupportBasis`, identification profile refs, realizability profile refs, supported causal use, and unsupported causal use; `A.10` for the evidence-provenance graph path carrying causal-evidence refs.
* **Coordinates with:** `A.15` for work disposition and reliance disposition, `A.6` for mixed authority wording, `A.21` for `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`, `A.20` for `ConstraintValidity` status or witness, and `A.15.1` for release or deployment work occurrence. B.3 only handles typed assurance use; labels and evidence pointers stay with the source relation that governs them when assurance is not being claimed.
* **Used by:** KD-CAL improvement patterns (to plan improvements), B.4 (Evolution loops that raise `F`, `G`, `R`, or `CL` over time).
* **Triggers:** B.2 (Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes) when genuine new capabilities emerge that change the applicable cutsets or envelopes.

> **One‑page takeaway.**
> Report assurance as **⟨F, G, R⟩** for a **typed claim** under explicit **context and scope**, and penalize by the **lowest edge-scoped Congruence Level (`CL`) value**.
> Improve assurance by raising **F**, **G**, **R**, or **CL**—and keep order, time, and cost in their own lanes.

