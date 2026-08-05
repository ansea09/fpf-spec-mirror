---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:4"
section_title: "Solution — Discipline Health Characterisation (DHC)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__006_solution-discipline-health-characterisation-dhc.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:4 — Solution — Discipline Health Characterisation (DHC)"
line_start: 50740
line_end: 50816
dependencies:
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.20"
  - "E.10"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Discipline"
keywords:
  - "alignment"
  - "discipline"
  - "disruption"
  - "field health"
  - "reproducibility"
  - "standardisation"
---

### C.21:4 - Solution — **Discipline Health Characterisation (DHC)**

#### C.21:4.0 - Ontology quick sheet (normative, clarifying)
**What “DHC” is.** DHC is a **CHR vocabulary pack** that defines **Characteristics** + **Scales/Units/Polarity** for discipline health; it is not a document or a run.
**Artifacts.**
• **`U.DHCPack`** (I-lane name; published as an episteme): the **slot set** (Characteristic/Scale declarations) for a Context.
• **`U.DHCMethodSpec`** (S-lane): the **computational specification(s)** for deriving each DHC slot (e.g., replication‑window definition, CD‑index class), table‑backed; multiple per slot allowed, editioned separately.
• **`U.DHCSeries`** (episteme w/ `EditionSeries`): a **time‑indexed publication** of computed DHC readings for a Discipline×Context, each value bound to `…Ref.edition` for every referenced method/metric/distance.
**Edition subjects.**
(i) **DHCPack.edition** — when the **slot semantics** (Characteristic/Scale) change.
(ii) **DHCMethodSpecRef.edition** — when a **computation method** (formula/class/policy) changes.
(iii) **DHCSeries.edition** — when the **published series** changes its content (not carriers).
**Publication.** Releases are **Work** on Carriers; **no** edition change unless content changes per `U.EditionSeries`.
**Ref discipline.** All bindings to packs/methods/distances use `...Ref.edition` (dot on the Ref).

Define a **portable minimal set** of CHR **slots**. Each slot is **CHR-typed** (Characteristic, Scale/Unit/Polarity per **A.17–A.18**), **Context-local**, and guarded by **USM** (Claim scope **G**), **freshness windows**, and **evidence lanes** (TA/VA/LA).  Contexts may extend the set; conforming extensions do not alter scale types inadmissibly.

**“Health” is a vector** of CHR‑typed coordinates; **no single scalar** is implied. Scale-admissible scalarization lives in **Acceptance** (G.4) under an explicit **CG‑Spec ScaleComplianceProfile (SCP)** and **Γ‑fold** rules, and is never embedded in CHR.

#### C.21:4.1 - Core Characteristics (kernel-portable names)

1. **ReproducibilityRate** *(ratio ∈ [0,1]; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Fraction of tested claims/benchmarks that independent teams **replicate** under a declared **ContextSlice** and **Γ\_time** window. **Lane tags:** LA (validation) with TA (typing) for protocols.

2. **StandardisationLevel** *(ordinal; polarity ↑; ReferencePlane=episteme)*
   {none, *emerging*, *de facto*, *de jure*}. **No mean.** Use medoid/mode; admissible comparisons are ≤/=/> only. Tracks convergence on vocabularies, interfaces, or procedures.

3. **AlignmentDensity** *(ratio; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Density of **Substitution Bridges** (same **senseFamily**, CL≥2) between major `U.Tradition`s **per 100 DHC‑SenseCells** (G.2 F‑hooks) in the SoTA palette.  Substitution rule:  free substitution permitted at **CL=3**; at **CL=2** substitute only with extra‑guard (count in reporting, but this is not «free substitution») Units: `bridges_per_100_cells`. Cross‑Context use requires Bridge+CL; penalties → **R_eff** only.

 4. **DisruptionBalance** *(interval; polarity = target band; ReferencePlane=episteme; CG‑Spec‑bound)*
  Relative share of **disruptive vs consolidating** works within **Γ_time** using a **registered CD‑index class** (editioned; cite **method id** in UTS). **Default plane:** *episteme*. Publish the **target band** via **Acceptance (G.4)**; not in CHR.

  5. **EvidenceGranularity** *(Context-declared: ordinal|ratio; polarity ↑; ReferencePlane=episteme)*
   If ratio: units = `claims_per_artifact` or `anchors_per_claim` (declare). If ordinal: publish level names and **ORD_COMPARE_ONLY**.
   Fineness of evidential units and declared envelopes (experiment cards, benchmark tasks, audit granules). Encourages *smaller, well-scoped* claims over monoliths.

  6. **MetaDiversity** *(portfolio dispersion; polarity ↑ to band; ReferencePlane=episteme; CG‑Spec‑bound)*
  Use entropy/HHI **over MethodFamily/Tradition shares** (method edition id in UTS); publish **guard‑band** as **Acceptance** binding; cross‑ordinal scalarisation is forbidden.
  Entropy/Herfindahl-type dispersion across `U.Tradition`s, method families, or data regimes, bounded by a **Context-declared guard-band** (too low ⇒ monoculture; too high ⇒ incoherence).

> **Typing & admissibility.** Each slot declares **Scale/Unit/Polarity**; inadmissible operations (for example, means on ordinals or unit mixing) fail fast per **A.18/MM-CHR**.

#### C.21:4.1a - Engineering-grade and semio-substitution extension slots

Contexts MAY add these DHC slots when the discipline-health question includes engineering-grade reasoning, architecturing, optimization, prediction, comparison, assurance input, decision input, first-principles justification, mathematical-lens use, or source-publication overread. These slots remain discipline-health characteristics. They do not become evidence relations, assurance relations, gate decisions, mathematical-lens use, measurement admissibility, release permission, or project authority.

7. **EngineeringClaimJustificationRecoverability** *(ordinal; polarity ↑; ReferencePlane=episteme|world by declared claim; CG-Spec-bound when aggregated)*
   Degree to which engineering-grade claims in the discipline or Context expose the exact justification that carries their force for the declared use. The justification may be a named construction, source, model, lens, evidence relation, characteristic relation, assurance relation, gate relation, method relation, or heuristic triage boundary, but it must cite the neighboring pattern governing the claiming FPF pattern when that force is live (`A.10`, `B.3`, `A.15`, `A.20`, `A.21`, `C.16`, `C.29`, or another governing pattern). Heuristic examples may carry recognition and triage only; prediction, comparison, optimization, falsification, assurance-input, decision-input, or architecture-readiness force requires the recoverable justification.

8. **SemioSubstitutionPressure** *(ordinal or ratio; polarity ↓ to band; ReferencePlane=episteme; CG-Spec-bound when aggregated)*
   Degree to which discipline texts, patterns, dashboards, views, publications, source chains, or review artifacts substitute wording, publication form, record appearance, source appearance, or explanation fluency for the operative engineering entity, relation, work, evidence, assurance, gate, decision, method, or mathematical-lens claim. Lower pressure is healthier when the discipline keeps EntityOfConcern, episteme, publication, source, carrier, and project-side claim kind or admissible-use boundary separable and names the pattern governing the recovered claim for any claim being made or admissible-use boundary.

**Extension guard.** Activating either extension slot requires a local `EngineeringClaimJustification` note or semio-substitution note that names the claim kind being made or admissible-use boundary, neighboring pattern governing the claiming FPF pattern, admissible use, non-admissible overread, and stop or reopen condition. The note is a DHC value explanation, not a new evidence source, assurance case, gate, release record, or work authority.

#### C.21:4.2 - Guard Macros (normative)

* **ORD\_COMPARE\_ONLY(x)** — for **StandardisationLevel** (ordinal).
* **UNIT\_CHECK(x)** — forbid cross-unit aggregation (AlignmentDensity, ReproducibilityRate).
* **POLARITY_CHECK(x)** — enforce declared polarity (↑/↓/target-band) per MM‑CHR.
* **FRESHNESS(x; window)** — ensure values come from evidence within declared **Γ_time**; record **valid_until**; stale ⇒ {degrade|abstain} at Acceptance.
* **PLANE_NOTE(x)** — record **ReferencePlane**; compute **CL^plane** on crossings; penalties → **R_eff** only.
* **LANE\_TAGS(x; {TA|VA|LA})** — annotate contribution lanes.
* **SCOPE\_COVERS(x; TargetSlice)** — enforce **USM** coverage of the computation.
* **BRIDGE_CL(x; id, CL≥k)** — on cross‑Context roll‑ups, require **Bridge** with **CL**; penalties affect **R** only. If planes differ, apply **CL^plane** and cite **Φ_plane** policy id. **Hint:** for **AlignmentDensity** reporting, set **k=2** (CL≥2); **CL=3** counts as *free substitution*.

#### C.21:4.3 - Legality Matrix (extract)

| Operation     | ReproducibilityRate (ratio) | StandardisationLevel (ordinal) | AlignmentDensity (ratio) | DisruptionBalance (interval) |
| ------------- | --------------------------: | -----------------------------: | -----------------------: | ---------------------------: |
| mean          |                      **OK** |                     **FORBID** |                   **OK** |                       **OK** |
| median        |                          OK |                         **OK** |                       OK |                           OK |
| compare (<,>) |                          OK |                         **OK** |                       OK |                           OK |
| unit mix      |                  **FORBID** |                            n/a |               **FORBID** |                          n/a |

*Note:* For **MetaDiversity/EvidenceGranularity (ordinal)** use **median/mode**; forbid affine ops; unit mix always fails.

