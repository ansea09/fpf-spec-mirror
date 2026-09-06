---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:5"
section_title: "Archetypal grounding (worked, didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__006_archetypal-grounding-worked-didactic.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:5 — Archetypal grounding (worked, didactic)"
line_start: 37104
line_end: 37148
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:5 - Archetypal grounding (worked, didactic)

#### B.1.3:5.1 - Episteme — **Meta‑analysis into a guidance statement**

* **Inputs (U.Episteme):**
  `E₁` randomized trial (R=0.84, F=3, G=medium), `E₂` observational study (R=0.55, F=2, G=wide), `E₃` mechanistic model (R=0.60, F=3, G=narrow).
  Mappings: dosage units (mg ↔ IU), outcome definitions (pain scale variants), each with declared **CL** (e.g., unit mapping CL=3, outcome alignment CL=2).

* **Γ\_epist^synth:**

  * **Provenance preservation:** all study protocols, datasets, analysis scripts listed in the **SCR**.
  * **Object alignment:** “acute low‑back pain within 6 weeks” via taxonomy LCA; non‑aligned chronic cohorts excluded or mapped with low CL and flagged.
  * **Concept integration:** compute provisional `R_eff` along each justification path, penalized by **Φ(CL_min(path))**; aggregate `R_eff` as the minimum over paths.
  * **Conflict handling:** `E₂` contradicts `E₁` in a subgroup; kept as **provisional** with explicit conflict edge and scope note (different baseline severity).

* **Γ_epist^compile (target journal scheme):**
  Map outcomes to the journal's required scheme through the exact sense mappings used by the fold, recalculate F/G/R with mapping penalties, and produce the compilation SCR and hashes. The result is the target-scheme episteme "Guidance Statement v1.0" with conservative `R`; any later journal publication is a separate publication occurrence.


* **Why not averaging?**
  Averaging would inflate `R` and hide low‑CL outcome mappings; Γ\_epist enforces pathwise **min** + **CL** penalty.

#### B.1.3:5.2 - Episteme — **Safety case from heterogeneous evidence**

* **Inputs:** requirement spec (F=3, R=0.7), hazard analysis (F=2, R=0.6), test logs (F=1, R=0.8), formal proof of controller property (F=3, R=0.9).

* **Γ\_epist^synth:**

  * Provenance union; **SCR** includes requirements, proof carrier, test datasets.
  * Concept integration: controller proof applies only under assumptions A; test logs violate A in edge case → **CL** low for mapping “test scenario ≡ proof assumption.”
  * `R_eff` bounded by the weakest justification path after **Φ(CL\_min)**; claim on “system‑level safety” marked **provisional** until assumption alignment is demonstrated.

* **Γ_epist^compile (target certification scheme):**
  Map the claims to the regulatory vocabulary. Where local meanings differ, identify exact source and receiving `SchemeSenseCell` values, test the F.9 Bridge, state the bounded certification use and permitted loss, and establish any relied-on use separately. C.2.1 identifies the resulting target-scheme episteme; a certification publication occurrence or acceptance verdict remains separate.

#### B.1.3:5.3 - Contrast (didactic)

| Aspect          | **Γ\_epist (Knowledge)**                                         | **Γ\_sys (Physical)**                       |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| What is folded? | Claims, models, datasets, arguments                              | Components, materials, assemblies            |
| Conservatism    | **Pathwise min** of R + penalty **Φ(CL)**                        | WLNK via **weakest part** (strength, rating) |
| Fit             | **Mappings** with declared **CL**                                | **Interfaces/BIC** compatibility             |
| Order/time | Optional **Γ\_ctx** for argument order; C.2.1 for distinct episteme identities and edition relations; A.14 for a proper restriction of one unchanged episteme; B.1.4/**Γ\_time** for bounded aggregation of recovered temporal relations | Γ\_ctx for workflows; Γ\_time for phases of directly governed enduring carriers |
| Work/cost       | External in **Γ\_work** (compute, curation)                      | External in **Γ\_work** (energy, labour)     |

