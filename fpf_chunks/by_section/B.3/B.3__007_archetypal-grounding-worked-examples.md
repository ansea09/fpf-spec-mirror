---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:6"
section_title: "Archetypal grounding (worked examples)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__007_archetypal-grounding-worked-examples.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:6 — Archetypal grounding (worked examples)"
line_start: 38895
line_end: 38960
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.4"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "C.29"
  - "D.4"
  - "E.14"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.6"
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
* **Target and assurance use:** exact pack-safety claim episteme under the engineering ReferenceScheme; `G_A` is the load/temperature/airflow/duty-cycle envelope; `T_A = run` for the named operational-safety use.
* **Graph:** Cells `ComponentOf` modules `ComponentOf` pack; BIC exposes main power and thermal interface.
* **Inputs:**

  * `F` for exact module-spec and cell-test claim inputs: module spec F2, cell test F1 → `F_eff = F1`.
  * `G`: operating envelope regions; union constrained by evidence relationed test regimes.
  * `R`: per‑module reliability from test data; cutset is **hot‑spot path** near weakest cell.
  * `CL`: interface congruence (sensor calibration CL2; thermal contact CL1).
* **Aggregation:**

  * `R_raw = min R_i` along the thermal cutset.
  * `R_eff = max(0, R_raw − Φ(CL_min=CL1))`.
  * `G_eff`: union of evidence-covered (L,T) rectangles, dropping regions lacking validated thermal data.
  * `F_eff = min(F_cell=F1, F_module=F2) = F1`.
* **Assessment and record boundary:** dated safety-assessment work consumes the exact calibration/test input-result claims and A.2.4 evidence-use refs; its B.3 result episteme states the tuple, witnesses show the calculation, and an optional record cites the BIC and A.10/G.6 path.
* **Improvement move:** raise `CL` (better thermal interface verification), raise `F` (formal thermal model), add evidenced envelope -> **R_eff** and **G_eff** increase monotonically.

#### B.3:6.2 - Episteme archetype — **Meta-analysis claim**

* **Claim `C`:** *Intervention X reduces outcome O by Δ on population P.*
* **Target and assurance use:** exact meta-analysis claim episteme under the analysis ReferenceScheme; inclusion/exclusion criteria and measurement protocol are condition refs, `G_A` is population/scope, and `T_A = design` for the named evidential-credibility use.
* **Graph:** Studies `MemberOf` evidence corpus; effect models `ConstituentOf` synthesis; mappings align different outcome scales.
* **Inputs:**

  * `F`: two RCTs at F3, one observational at F2 -> `F_eff = F2`.
  * `R`: replication quality per study -> weakest R on the declared entailment path/subgraph caps `R_raw`.
  * `CL`: mapping of scales (CL1 vs CL3).
  * `G`: populations union, but unevidence-covered sub-populations are dropped.
* **Aggregation:**

  * `F_eff = F2` from the weakest study-design evidence relation in the synthesis.
  * `R_eff = max(0, min(R_RCT1, R_RCT2, R_OBS) - Φ(CL_min=CL1))`.
  * `G_eff`: union of evidence-covered sub-populations; out-of-scope groups excluded.
  * `CL_min = CL1` for the exact scale-mapping relation; cite the mapping witness and weakest-link input claim in the assurance record, while the assurance-result episteme remains separate.
* **Assessment and record boundary:** dated credibility-assessment work consumes the exact study/effect input-result claims, A.2.4 evidence-use refs, scale-mapping occurrences, bias result, and any constructive equivalence result; the B.3 result episteme, calculation witness, optional record, and A.10/G.6 provenance path remain distinct.
* **Improvement move:** upgrade mapping verification to CL2 or CL3; increase `F` via registered analysis plan; replicate lagging study.

#### B.3:6.3 - Order-sensitive manufacturing-sequence assurance

* **Claim `C`:** *The domain manufacturing sequence `R`, mapped to an order-sensitive Method/Work sequence with an `OrderSpec`, meets output defect rate <= epsilon.*
* **Target and assurance use:** exact sequence-defect claim episteme; materials and equipment class are condition refs, the manufacturing envelope is `G_A`, and `T_A = run` for the named process-reliability use.
* **Γ_ctx records:** `OrderSpec σ` for the method/work sequence; declared independent branches; join conditions at inspection.
* **Assurance:**

  * `R_raw = min R_step` along the declared order-sensitive dependency path (including inspection effectiveness).
  * Penalty from poor join soundness `CL_min`.
  * Improvement via faster but **verified** inspection (increase `R_step`) or tighter join spec (increase `CL`).

#### B.3:6.4 - Temporal archetype — **Model credibility across exact episteme identities**

* **Claims `C_i`:** each exact model episteme `M_i` carries its own prediction claim and declared applicability window; a receiving assurance use may additionally ask whether the selected claims jointly support prediction within ±δ over τ.
* **Target and assurance use:** each exact model claim keeps its own effective ReferenceScheme and window; the selected data regime and drift tolerance are condition refs, and the joint prediction-credibility use declares its own `G_A` and `T_A = run`.
* **C.2.1 identity and continuity:** compare the exact claim content, EntityOfConcern, and effective ReferenceScheme for the items labelled v1, v2, and v3. A changed discriminator identifies another episteme. Assert `EpistemeEditionRelation(M_v1,M_v2)` or `EpistemeEditionRelation(M_v2,M_v3)` only when each ordered pair satisfies C.2.1's independent historical-continuation predicate; labels, revision Work, provenance, publication order, and common lineage establish neither occurrence.
* **Temporal aggregation:** a B.1.4/Γ\_time record may order those already recovered edition relations, applicability windows, or publication windows for the bounded assurance use. It does not turn the distinct epistemes into `PhaseOf` slices. If one exact episteme instead remains unchanged and the use needs proper interval restrictions, A.14 `PhaseOf(M@τ_i,M)` remains available and B.3 `TIME-COV` applies to that same phased entity.
* **Assurance:**

  * compute `R_raw = min(R_C1, R_C2, R_C3)` only when the named assurance use actually consumes all three exact edition-specific claims and their evidence relations;
  * apply the declared penalty when the mapping or calibration congruence between the edition-specific prediction/evidence bases is low;
  * re-calibration or a new validation campaign may improve the exact supported claim, mapping, or evidence relation, but creates neither episteme identity, edition continuity, currentness, nor publication availability; and
  * a non-continuing replacement receives an independent assurance assessment and inherits no `F`, `G`, `R`, `CL`, evidence, or reliance result by label.

