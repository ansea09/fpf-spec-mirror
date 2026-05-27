---
chunk_kind: "child"
pattern_id: "A.3"
pattern_title: "Transformer Constitution (Quartet)"
section_id: "A.3:6"
section_title: "Illustrative scenarios (substrate‑neutral)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3/A.3__007_illustrative-scenarios-substrate-neutral.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.3 — Transformer Constitution (Quartet)"
  - "A.3:6 — Illustrative scenarios (substrate‑neutral)"
line_start: 5678
line_end: 5688
dependencies:
  - "A.15"
  - "A.2"
  - "A.3.1"
  - "A.3.2"
keywords:
  - "Method"
  - "MethodDescription"
  - "System-in-Role"
  - "Work"
  - "action"
  - "causality"
  - "change"
---

### A.3:6 - Illustrative scenarios (substrate‑neutral)

#### A.3:6.1 - Physical system — Cooling loop
`PumpUnit#3` (**system bearing TransformerRole**) executes `ChannelFluid` (**Method**) as per `centrifugal_pump_curve.ld` (**MethodDescription**), producing `run‑2025‑08‑08‑T14:03` (**Work**, 3.6 kWh; ΔT=6 K). Evidence goes to carriers in SCR; resource spend goes to Γ\_work.

#### A.3:6.2 - Epistemic change — Proof revision
`LeanServer` (**system bearing TransformerRole**) edits `proof_tactic.lean` (carrier) per MethodDescription; `lemma‑42‑check‑2025‑08‑08` is **Work**; the **episteme** (theorem) changes through its carriers; evidence is attributed to the external transformer.

#### A.3:6.3 - Reflexive maintenance — “calibrates itself”
Split into **Regulator** (calibration module, acting side) and **Regulated** (sensor suite, target) with an interaction boundary; credit evidence to the regulator; no self‑evidence.

