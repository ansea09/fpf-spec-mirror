---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:6"
section_title: "Archetypal grounding (worked examples)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__007_archetypal-grounding-worked-examples.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:6 — Archetypal grounding (worked examples)"
line_start: 38376
line_end: 38439
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

### B.3:6 - Archetypal grounding (worked examples)

#### B.3:6.1 - System archetype — **Battery pack safety claim**

* **Claim `C`:** *Pack P meets discharge current L with thermal safety margin δ in environment K.*
* **Context `K`:** Ambient ≤ 35 °C; airflow ≥ X; duty cycle Y. Scope `S = run`.
* **Graph:** Cells `ComponentOf` modules `ComponentOf` pack; BIC exposes main power and thermal interface.
* **Inputs:**

  * `F` per node: module spec F2, cell test F1 → `F_eff = F1`.
  * `G`: operating envelope regions; union constrained by evidence relationed test regimes.
  * `R`: per‑module reliability from test data; cutset is **hot‑spot path** near weakest cell.
  * `CL`: interface congruence (sensor calibration CL2; thermal contact CL1).
* **Aggregation:**

  * `R_raw = min R_i` along the thermal cutset.
  * `R_eff = max(0, R_raw − Φ(CL_min=CL1))`.
  * `G_eff`: union of evidence-covered (L,T) rectangles, dropping regions lacking validated thermal data.
  * `F_eff = min(F_cell=F1, F_module=F2) = F1`.
* **Evidence/source record:** Evidence for calibration, test campaigns, BIC.
* **Improvement move:** raise `CL` (better thermal interface verification), raise `F` (formal thermal model), add evidenced envelope -> **R_eff** and **G_eff** increase monotonically.

#### B.3:6.2 - Episteme archetype — **Meta-analysis claim**

* **Claim `C`:** *Intervention X reduces outcome O by Δ on population P.*
* **Context `K`:** Inclusion criteria, exclusion criteria, measurement protocol; `S = design`.
* **Graph:** Studies `MemberOf` evidence corpus; effect models `ConstituentOf` synthesis; mappings align different outcome scales.
* **Inputs:**

  * `F`: two RCTs at F3, one observational at F2 -> `F_eff = F2`.
  * `R`: replication quality per study -> weakest R on the entailment spine caps `R_raw`.
  * `CL`: mapping of scales (CL1 vs CL3).
  * `G`: populations union, but unevidence-covered sub-populations are dropped.
* **Aggregation:**

  * `F_eff = F2` from the weakest study-design evidence relation in the synthesis.
  * `R_eff = max(0, min(R_RCT1, R_RCT2, R_OBS) - Φ(CL_min=CL1))`.
  * `G_eff`: union of evidence-covered sub-populations; out-of-scope groups excluded.
  * `CL_min = CL1` for scale mappings; record the mapping witness and weakest-link study in the assurance source-currentness record.
* **Evidence/source record:** Data provenance, scale mappings, bias assessment, and proof-term hash for the effect-model equivalence when it is used constructively.
* **Improvement move:** upgrade mapping verification to CL2 or CL3; increase `F` via registered analysis plan; replicate lagging study.

#### B.3:6.3 - Order-sensitive manufacturing-sequence assurance

* **Claim `C`:** *The domain manufacturing sequence `R`, mapped to an order-sensitive Method/Work sequence with an `OrderSpec`, meets output defect rate <= epsilon.*
* **Context `K`:** Materials, equipment class; `S = run`.
* **Γ_ctx records:** `OrderSpec σ` for the method/work sequence; declared independent branches; join conditions at inspection.
* **Assurance:**

  * `R_raw = min R_step` along the declared order-sensitive dependency path (including inspection effectiveness).
  * Penalty from poor join soundness `CL_min`.
  * Improvement via faster but **verified** inspection (increase `R_step`) or tighter join spec (increase `CL`).

#### B.3:6.4 - Temporal archetype — **Versioned model credibility**

* **Claim `C`:** *Model M predicts within ±δ over τ.*
* **Context `K`:** Data regime and drift tolerance; `S = run`.
* **Γ\_time records:** `PhaseOf` slices v1, v2, v3 covering `τ`.
* **Assurance:**

  * `R_raw = min(R_v1, R_v2, R_v3)`;
  * penalty if v2–v3 interface had low calibration congruence;
  * improvement via re‑calibration (↑CL) or new validation campaign (↑R\_v3).

