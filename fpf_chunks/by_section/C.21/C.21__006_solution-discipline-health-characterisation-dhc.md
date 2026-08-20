---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:4"
section_title: "Solution — Discipline Health Characterisation (DHC)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__006_solution-discipline-health-characterisation-dhc.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:4 — Solution — Discipline Health Characterisation (DHC)"
line_start: 50379
line_end: 50455
dependencies:
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.20"
  - "E.10"
  - "F.17"
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
• **`U.DHCPack`** (I-lane name; published as an episteme): the **slot set** of Characteristic and Scale declarations selected for a named discipline-health use under an exact effective `ReferenceScheme`.
• **`U.DHCMethodSpec`** (S-lane): the **computational specification(s)** for deriving each DHC slot (e.g., replication‑window definition, CD‑index class), table‑backed; multiple per slot allowed, editioned separately.
• **`U.DHCSeries`** (episteme with an `EditionSeries`): a **time-indexed publication** of computed DHC readings for one named discipline, `ClaimScope`, comparison basis, and intended use; each value is bound to `…Ref.edition` for every referenced characteristic, scale, method, metric, and distance.
**Edition subjects.**
(i) **DHCPack.edition** — when the **slot semantics** (Characteristic/Scale) change.
(ii) **DHCMethodSpecRef.edition** — when a **computation method** (formula/class/policy) changes.
(iii) **DHCSeries.edition** — when the **published series** changes its content (not carriers).
**Publication.** Releases are **Work** on Carriers; **no** edition change unless content changes per `U.EditionSeries`.
**Ref discipline.** All bindings to packs/methods/distances use `...Ref.edition` (dot on the Ref).

Define a **portable minimal set** of CHR **slots**. Each slot is CHR-typed (Characteristic, Scale, Unit, and Polarity per **A.17–A.18**) and each reading names its effective `ReferenceScheme`, `ClaimScope`, comparison basis, freshness window, evidence lanes, and exact characteristic, scale, method, metric, and distance editions that matter. A local extension is another declared slot; it does not alter an existing scale type in place.

**“Health” is a vector** of CHR‑typed coordinates; **no single scalar** is implied. Scale-admissible scalarization lives in **Acceptance** (G.4) under an explicit **CG‑Spec ScaleComplianceProfile (SCP)** and **Γ‑fold** rules, and is never embedded in CHR.

#### C.21:4.1 - Core Characteristics (kernel-portable names)

1. **ReproducibilityRate** *(ratio ∈ [0,1]; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Fraction of tested claims or benchmarks that independent teams **replicate** for a named benchmark, corpus, cohort, protocol, and `ClaimScope` within a declared **Γ_time** window. **Lane tags:** LA (validation) with TA (typing) for protocols.

2. **StandardisationLevel** *(ordinal; polarity ↑; ReferencePlane=episteme)*
   {none, *emerging*, *de facto*, *de jure*}. **No mean.** Use medoid/mode; admissible comparisons are ≤/=/> only. Tracks convergence on vocabularies, interfaces, or procedures.

3. **AlignmentDensity** *(ratio; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Density of obtaining **F.9 Substitution Bridges** with `CL≥2` between exact F.17 `SchemeSenseCell` values used by major `U.Tradition`s, per 100 cells in the declared comparison set. Free substitution is permitted at `CL=3`; at `CL=2`, substitute only with the stated extra guard. Units: `bridges_per_100_cells`. The reading names every cell set, Bridge relation, admitted use, and loss note; penalties affect **R_eff** only.

 4. **DisruptionBalance** *(interval; polarity = target band; ReferencePlane=episteme; CG‑Spec‑bound)*
  Relative share of **disruptive vs consolidating** works within **Γ_time** using a **registered CD‑index class** (editioned; cite **method id** in UTS). **Default plane:** *episteme*. Publish the **target band** via **Acceptance (G.4)**; not in CHR.

  5. **EvidenceGranularity** *(ordinal or ratio as declared by the selected characteristic and scale editions; polarity ↑; ReferencePlane=episteme)*
   If ratio: units = `claims_per_artifact` or `anchors_per_claim` (declare). If ordinal: publish level names and **ORD_COMPARE_ONLY**.
   Fineness of evidential units and declared envelopes (experiment cards, benchmark tasks, audit granules). Encourages *smaller, well-scoped* claims over monoliths.

  6. **MetaDiversity** *(portfolio dispersion; polarity ↑ to band; ReferencePlane=episteme; CG‑Spec‑bound)*
  Use entropy/HHI **over MethodFamily/Tradition shares** (method edition id in UTS); publish **guard‑band** as **Acceptance** binding; cross‑ordinal scalarisation is forbidden.
  Entropy- or Herfindahl-type dispersion across `U.Tradition`s, method families, or data regimes, bounded by the guard-band declared for this use under the selected policy edition (too low ⇒ monoculture; too high ⇒ incoherence).

> **Typing & admissibility.** Each slot declares **Scale/Unit/Polarity**; inadmissible operations (for example, means on ordinals or unit mixing) fail fast per **A.18/MM-CHR**.

#### C.21:4.1a - Engineering-grade and semio-substitution extension slots

A discipline-health use MAY add these DHC slots when its question asks either how recoverable the justification of an engineering claim is or how strongly representations are being mistaken for their subjects. Such questions arise, for example, in architecturing, optimization, prediction, comparison, assurance or decision input, first-principles justification, mathematical-lens use, and source-publication overread. These slots remain discipline-health characteristics. They do not become evidence relations, assurance relations, gate decisions, mathematical-lens use, measurement admissibility, release permission, or project authority.

7. **EngineeringClaimJustificationRecoverability** *(ordinal; polarity ↑; ReferencePlane=episteme|world by declared claim; CG-Spec-bound when aggregated)*
   Degree to which engineering-grade claims in the named discipline and `ClaimScope` expose the exact justification that carries their force for the intended use. That justification is the named construction, source, model, lens, or relation on which the claim relies. Examples include evidence, characteristic, assurance, gate, and method relations, as well as a stated heuristic triage boundary. When that force is live, the claim cites the pattern and exact rule that define or constrain the operative construction or relation (`A.10`, `B.3`, `A.15`, `A.20`, `A.21`, `C.16`, `C.29`, or another applicable pattern). Heuristic examples may carry recognition and triage only; prediction, comparison, optimization, falsification, assurance-input, decision-input, or architecture-readiness force requires the recoverable justification.

8. **SemioSubstitutionPressure** *(ordinal or ratio; polarity ↓ to band; ReferencePlane=episteme; CG-Spec-bound when aggregated)*
   Degree to which a discipline mistakes a representation or its apparent fluency for the engineering subject, relation, or claim it is meant to support. Representations include, for example, wording, publication forms, records, dashboards, views, and source chains. The displaced subject may be an entity, relation, Work occurrence, evidence or assurance claim, gate, decision, method, or mathematical-lens claim. Lower pressure is healthier when an EntityOfConcern remains distinct from epistemes about it and from their publications, sources, and carriers, and each current project-side claim or use boundary cites the pattern and rule that define or constrain it.

**Extension guard.** Activating either extension slot requires a local `EngineeringClaimJustification` note or semio-substitution note that names the current claim kind or admissible-use boundary, the pattern and rule that define or constrain it, admissible use, non-admissible overread, and stop or reopen condition. The note is a DHC value explanation, not a new evidence source, assurance case, gate, release record, or work authority.

#### C.21:4.2 - Guard Macros (normative)

* **ORD\_COMPARE\_ONLY(x)** — for **StandardisationLevel** (ordinal).
* **UNIT\_CHECK(x)** — forbid cross-unit aggregation (AlignmentDensity, ReproducibilityRate).
* **POLARITY_CHECK(x)** — enforce declared polarity (↑/↓/target-band) per MM‑CHR.
* **FRESHNESS(x; window)** — ensure values come from evidence within declared **Γ_time**; record **valid_until**; stale ⇒ {degrade|abstain} at Acceptance.
* **PLANE_NOTE(x)** — record **ReferencePlane**; compute **CL^plane** on crossings; penalties → **R_eff** only.
* **LANE\_TAGS(x; {TA|VA|LA})** — annotate contribution lanes.
* **SCOPE\_COVERS(x; TargetSlice)** — enforce **USM** coverage of the computation.
* **CROSS_LOCAL_RELATION(x; relation, admittedUse)** — when a roll-up actually relates distinct F.17 cells, require the exact F.9 relation, its CL, admitted use, and loss notes; penalties affect **R** only. If ReferencePlanes differ, also apply the exact plane relation and cited policy. For **AlignmentDensity**, count only obtaining relations in the declared comparison set; `CL=3` counts as free substitution and `CL=2` requires the stated extra guard.

#### C.21:4.3 - Legality Matrix (extract)

| Operation     | ReproducibilityRate (ratio) | StandardisationLevel (ordinal) | AlignmentDensity (ratio) | DisruptionBalance (interval) |
| ------------- | --------------------------: | -----------------------------: | -----------------------: | ---------------------------: |
| mean          |                      **OK** |                     **FORBID** |                   **OK** |                       **OK** |
| median        |                          OK |                         **OK** |                       OK |                           OK |
| compare (<,>) |                          OK |                         **OK** |                       OK |                           OK |
| unit mix      |                  **FORBID** |                            n/a |               **FORBID** |                          n/a |

*Note:* For **MetaDiversity/EvidenceGranularity (ordinal)** use **median/mode**; forbid affine ops; unit mix always fails.

