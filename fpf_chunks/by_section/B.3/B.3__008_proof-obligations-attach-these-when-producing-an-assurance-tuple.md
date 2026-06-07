---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust & Assurance Calculus (F–G–R with Congruence)"
section_id: "B.3:5"
section_title: "Proof obligations (attach these when producing an Assurance tuple)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__008_proof-obligations-attach-these-when-producing-an-assurance-tuple.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "B.3 — Trust & Assurance Calculus (F–G–R with Congruence)"
  - "B.3:5 — Proof obligations (attach these when producing an Assurance tuple)"
line_start: 31371
line_end: 31424
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

### B.3:5 Proof obligations (attach these when producing an Assurance tuple)

These obligations refine the generic Proof Kit from **B.1.1 §6** for **assurance** outputs. Each Γ‑flavour that emits an *Assurance(H, C | K, S)* tuple MUST attach the applicable obligations below.

#### B.3:5.1 - Common obligations (all Γ‑flavours)

* **ASS‑CLM (Typed claim & context).**
  State the **claim** `C` (what is being assured), the **context** `K` (assumptions, environment), and the **scope** `S ∈ {design, run}`.

* **ASS‑SCA (Scale discipline).**
  Declare the **scale kind** used for each characteristic (F ordinal, G coverage, R ratio) and confirm that all operations are **admissible** for that kind (no averaging of ordinals; G via set/coverage ops).

* **ASS‑WLNK (Weakest‑link evidence).**
  Identify the **cutset** (node or edge set) that caps F/G/R for the claim (the proof spine for epistemes, the structural or assurance bottleneck for systems).

* **ASS‑CL (Congruence path).**
  Identify the **relevant integration path(s)** and record `CL_min` used in the penalty `Φ(CL_min)`.

* **ASS‑MAN (SCR).**
  Produce a **SCR** listing all contributing nodes and edges with `(F, G, R)` and `CL` values, their **DesignRunTag**, and Evidence Graph Ref (A.10). If order or time affect the claim, include the **OrderSpec** or **TimeWindow** identifiers from **B.1.4**.

* **ASS‑MONO (Declared monotone characteristics).**
  List the characteristics along which local improvement cannot reduce the aggregate (this is used by future evolution, B.4).

#### B.3:5.2 - Γ\_sys (systems) — additional obligations

* **CORE‑BIC (Interface congruence).**
  Reference the **Boundary‑Inheritance Standard** (BIC) from **B.1.2** and record any interface mismatches; these contribute to `CL_min`.

* **CORE‑ENV (Operating envelope).**
  Specify the domain used for **G** (e.g., load–temperature region) and how coverage is computed (set union constrained by evidence relation).

#### B.3:5.3 - Γ\_epist (epistemes) — additional obligations

* **EPI‑SPN (Entailment spine).**
  Identify the **premise/lemma spine** for the claim; `R_raw = min R_i` is taken along this spine, not over arbitrary satellites.

* **EPI‑MAP (Semantic mapping congruence).**
  Point to the **vocabulary/ontology mappings** used; their verification status sets the **CL** values on the integration edges.

#### B.3:5.4 - Γ\_ctx and Γ\_method (order‑sensitive) — additional obligations

* **CTX‑ORD (OrderSpec).**
  Attach the partial or total order `σ` and any **join‑soundness** conditions (types, pre/post‑conditions).
  (See B.1.4 for NC‑1..3 invariants; B.1.5 adds duration/capability typing.)

#### B.3:5.5 - Γ\_time (temporal) — additional obligations

* **TIME‑COV (Coverage & identity).**
  Show that `PhaseOf` intervals cover the declared window without overlap for the **same carrier**; justify any gap/overlap explicitly.

> **Note on Γ\_work.**
> Resource spending and efficiency live in **Γ\_work**. Their *measurement integrity* can influence **R** for a claim (e.g., if a reliability figure depends on calibrated energy input), but **costs themselves are not assurance**; keep them in Γ\_work and cite their **measurement assurance** as inputs here.

