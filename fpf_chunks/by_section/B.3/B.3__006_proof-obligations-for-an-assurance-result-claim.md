---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:5"
section_title: "Proof obligations for an assurance-result claim"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__006_proof-obligations-for-an-assurance-result-claim.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:5 — Proof obligations for an assurance-result claim"
line_start: 39105
line_end: 39164
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

### B.3:5 - Proof obligations for an assurance-result claim

These obligations adapt the current B.1 and B.1.1 dependency-structure and relation-grounding checks for B.3 outputs. They are checks applied in dated assurance-assessment work; their pass/fail claims, witnesses, and optional record remain distinct from both the work and the assurance-result claim. Each Γ-flavour whose result is consumed by a B.3 assurance assessment supplies the applicable basis below; Γ does not emit assurance by itself.

#### B.3:5.1 - Common obligations (all Γ-flavours)

* **ASS-CLM (Exact target claim and use).**
  Name `E_C`, its ClaimGraph, EntityOfConcern, effective ReferenceScheme and direct subject-result governor; then name `U_A`, `G_A`, assumption/condition refs, and `T_A`. Do not use a title, carrier, holon label, generic context, or status value as the target claim.

* **ASS-WRK (Assessment and result separation).**
  Name the dated assessment work, performer assignment, enacted method, exact rule/application bindings, input-result claims, assurance-result episteme, witnesses or calculation traces, and any optional record/publication separately. A rule, record, or witness does not perform the check or become the result.

* **ASS-EVD (Evidence-use and warrant separation).**
  Cite each exact A.2.4 evidence-use relation and the minimum A.10/G.6 path needed for `U_A`. State polarity, scope, window, rival explanation, reliance disposition, and unsupported use. Evidence availability or loss may change warrant without changing target truth.

* **ASS-SCA (Scale discipline).**
  Declare the scale kind and exact bearer for each value: `F` ordinal, `G` set-valued scope, `R` ratio or declared conservative ordinal proxy, and `CL` ordinal on an exact integration relation. Confirm that every aggregation operation is defined for that scale kind.

* **ASS-WLNK (Weakest-link basis).**
  Identify the exact cutset or the declared premise/lemma path, distinguish them when both are used, and cite the input result/evidence-use refs that cap `F`, `G`, and `R`; graph membership alone supplies none of them.

* **ASS-CL (Congruence on integration dependency).**
  Identify every direct integration relation occurrence on the relevant path and the exact `CL_min` used in `Φ(CL_min)`. A mapping label, Card, or description is insufficient.

* **ASS-MAN (Replayable assurance record).**
  If a reusable record is needed, let it cite `E_C`, `U_A`, `RS_A`, `G_A`, `T_A`, all input result claims and evidence-use refs, F/G/R/CL values and bearers, assessment work and application refs, witnesses, limitations, decay, and an A.10/G.6 path. Include exact `OrderSpec` or `TimeWindow` refs when current. The record neither performs the assessment nor creates result truth, assurance, currentness, status, or later reliance.

* **ASS-MONO (Declared monotone characteristics).**
  List the characteristics along which a local input improvement cannot reduce the aggregate, and state the exact target/input identity and scope conditions under which that monotonicity claim holds.

#### B.3:5.2 - Γ\_sys (systems) — additional obligations

* **CORE‑BIC (Interface congruence).**
  Reference the **Boundary‑Inheritance Standard** (BIC) from **B.1.2** and record any interface mismatches; these contribute to `CL_min`.

* **CORE‑ENV (Operating envelope).**
  Specify the domain used for **G** (e.g., load–temperature region) and how coverage is computed (set union constrained by evidence relation).

#### B.3:5.3 - Γ\_epist (epistemes) — additional obligations

* **EPI‑SPN (Entailment path/subgraph).**
  Identify the exact **premise or lemma path/subgraph** for the claim, including its premises or nodes, inference edges, claim endpoint, scope, and rule selecting that path/subgraph; `R_raw = min R_i` is taken only over that declared object, not over arbitrary satellites.

* **EPI‑MAP (Semantic mapping congruence).**
  Point to the exact vocabulary/ontology mapping relation occurrences and the direct assessment results used to assign their `CL` values; a verification status label alone supplies neither the relation nor `CL`.

#### B.3:5.4 - Γ\_ctx and Γ\_method (order‑sensitive) — additional obligations

* **CTX‑ORD (OrderSpec).**
  Attach the partial or total order `σ` and any **join-soundness** conditions (types, preconditions, and postconditions).
  (See B.1.4 for NC‑1..3 invariants; B.1.5 adds duration/capability typing.)

#### B.3:5.5 - Γ\_time (temporal) — additional obligations

* **TIME-COV (Coverage and identity).**
  Show that `PhaseOf` intervals cover the declared window without overlap for the **same phased entity**; justify any gap or overlap explicitly.

> **Note on Γ\_work.**
> Resource spending and efficiency belong in **Γ_work**. Their *measurement integrity* can influence **R** for a claim (e.g., if a reliability figure depends on calibrated energy input), but **costs themselves are not assurance**; keep them in Γ_work and cite their **measurement assurance** as inputs here.

