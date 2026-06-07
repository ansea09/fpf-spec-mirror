---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:14"
section_title: "Relations (explicit pattern‑to‑pattern edges)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__015_relations-explicit-pattern-to-pattern-edges.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:14 — Relations (explicit pattern‑to‑pattern edges)"
line_start: 66377
line_end: 66406
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:14 - Relations (explicit pattern‑to‑pattern edges)

> Directed edges (→) are typed as **builds_on / constrains / coordinates / specializes / publishes_on / requires / provides_checks_for**.

**Foundations**
* **E.TGA →builds_on→ E.17 MVPK (for Morphisms).** Faces, pins, lanes, functorial publication, Lean/Core/Regulated profiles.
* **E.TGA →builds_on→ A.6.0 U.Signature / A.6.1 U.Mechanism.** Node kinds and governing-definition content boundaries.
* **E.TGA -> builds_on -> A.7 Strict Distinction (EntityOfConcern, Description episteme, Description episteme admitted for specification use, and publication/carrier separation).** No new claims on faces; publication faces project graph, crossing, or flow-valuation information without becoming the governed graph object, Description episteme, specification use, evidence, gate decision, work occurrence, or carrier.

**Flow semantics & checks**
* **E.TGA →coordinates→ A.20 U.Flow (ConstraintValidity scope).** CV checks live inside transformations; no declaration/translation of planes/units in CV; **error/timeout/unknown folds** follow **CC‑TGA‑22** as the **minimum default** (profiles can be stricter).
  **Terminology discipline (A.20 boundary).** In CV scope, publications use **status/witness** language; **GateDecisionRationale/GateDecisionExplanation** are reserved for gating and do not apply to CV.
* **E.TGA →coordinates→ A.21 GateProfilization (GateFit scope).** **GateFit-scoped GateChecks** are aggregated by `OperationalGate(profile)` with CV⇒GF activation; the **enumeration and publication shape** of GateChecks live in **A.21**. **Equivalently:** a GateFit decision different from `abstain` appears only when aggregated `ConstraintValidity = pass`; otherwise the **GateDecisionExplanation (GateFit‑oriented)** does not apply.
* **E.TGA →uses→ USM.CompareGuard and USM.LaunchGuard.** Guards publish scope and responsible gate; guard failures are handled by the declared gate.
* **E.TGA -> constrains -> F.9/F.17 bridge and terminology-synchronization loci (Bridge+UTS, CL/CL^plane, Phi -> R).** A transition is treated as a **Crossing** iff `Bridge+UTS` and the appropriate `CL/CL^plane` are published; otherwise this crossing explanation does not apply. Where Phi defines penalties, they appear in the R-lane only.
* **Operational interpretation (default): Eulerian.** A flow is a **valuation** over `U.Transfer`; edges carry **assurance‑only operations** (see CC‑TGA‑17); no token‑passing semantics are assumed.

**UNM & comparability**
* **E.TGA →constrains→ UNM declaration and use loci.** `CG‑Spec`, `ComparatorSet`, and `UNM.TransportRegistryΦ` declarations are governed by UNM; normalize-then-compare is mandatory.
* **E.TGA →constrains→ G.5 SelectionAndTuning.** Set‑returning, comparator‑pinned decisions, no hidden scalarization; `MethodTuning` without launch‑value slot filling.
* **E.TGA →constrains→ G.11 EvaluatingAndRefreshing.** EditionBumpProposal, two-phase update through the UNM declaration locus, path-local refresh.

**Work boundary**
* **E.TGA →coordinates with→ A.15 U.WorkEnactment (`FinalizeLaunchValuesOnlyInWork`).** Single point of `FinalizeLaunchValues`; `FreshnessUpToDate` hard at LaunchGate; acceptance/telemetry published here.

**Structure & reuse**
* **E.TGA →specializes→ U.TransductionFlow (and its family).** The graph architecture is the common graph-architecture base on which flow patterns (e.g., P2W, EvaluatingAndRefreshing) are defined; E.TGA provides coherence checks for their crossings, guards, and MVPK faces.
* **E.TGA -> coordinates with -> C.30.TGA-FLOW-REL.** When a TGA graph is used in an architecture-flow relation, `C.30.TGA-FLOW-REL` records the relation between flow/transduction structure and `ArchitectureOf@Context`; E.TGA keeps graph, crossing, and flow-valuation discipline.
* **E.TGA →publishes_on→ E.17 MVPK views** (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) for every edge/node where publication occurs; Lean mode allowed only as per profile.

