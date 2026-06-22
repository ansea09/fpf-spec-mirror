---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:14"
section_title: "Relations (explicit pattern-to-pattern relations)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__016_relations-explicit-pattern-to-pattern-relations.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:14 — Relations (explicit pattern-to-pattern relations)"
line_start: 70715
line_end: 70744
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:14 - Relations (explicit pattern-to-pattern relations)

> Relation rows use the named relation kinds **builds_on**, **constrains**, **coordinates**, **specializes**, **publishes_on**, **requires**, and **provides_checks_for**.

**Foundations**
* **E.18 -> builds_on -> E.17 MVPK (for publications of selected structure material).** Faces, pins, lanes, functorial publication, Lean, Core, and Regulated profiles.
* **E.18 -> builds_on -> A.6.0 U.Signature and A.6.1 U.Mechanism.** Locus kinds and governing-definition content boundaries.
* **E.18 -> builds_on -> A.7 Strict Distinction (EntityOfConcern, Description episteme, Description episteme admitted for specification use, and publication and carrier separation).** No new claims on faces; publication faces project selected structure, crossing, or flow-valuation information without becoming the governed selected structure, Description episteme, specification use, evidence, gate decision, work occurrence, or carrier.

**Flow semantics and checks**
* **E.18 -> coordinates -> A.20 Flow Constraint Validity.** CV checks apply inside transformations and transformation-flow valuations; no declaration or translation of planes or units in CV; **error, timeout, or unknown folds** follow **CC-E18-22** as the **minimum default** (profiles can be stricter).
  **Terminology discipline (A.20 boundary).** In CV scope, publications use **status and witness** language; **GateDecisionRationale** and **GateDecisionExplanation** are reserved for gating and do not apply to CV.
* **E.18 -> coordinates -> A.21 GateProfilization (GateFit scope).** **GateFit-scoped GateChecks** are aggregated by `OperationalGate(profile)` with CV=>GF activation; the **enumeration and publication shape** of GateChecks are governed by **A.21**. **Equivalently:** a GateFit decision different from `abstain` appears only when aggregated `ConstraintValidity = pass`; otherwise the **GateDecisionExplanation (GateFit-oriented)** does not apply.
* **E.18 -> uses -> USM.CompareGuard and USM.LaunchGuard.** Guards publish scope and responsible gate; guard failures are handled by the declared gate.
* **E.18 -> constrains -> F.9 and F.17 bridge and terminology-synchronization loci (Bridge and UTS, CL and CL^plane, Phi -> R).** A transition is treated as a **Crossing** iff `Bridge` and `UTS` and the appropriate `CL` or `CL^plane` are published; otherwise this crossing explanation does not apply. Where Phi defines penalties, they appear in the R-lane only.
* **Operational interpretation (default): Eulerian.** A flow is a **valuation** over `U.Transfer`; transfer relations carry **assurance-only operations** (see CC-E18-17); no token-passing semantics are assumed.

**UNM and comparability**
* **E.18 -> constrains -> UNM declaration and use loci.** `CG-Spec`, `ComparatorSet`, and `UNM.TransportRegistryPhi` declarations are governed by UNM; normalize-then-compare is mandatory.
* **E.18 -> constrains -> G.5 SelectionAndTuning.** Set-returning, comparator-pinned decisions, no hidden scalarization; `MethodTuning` without launch-value slot filling.
* **E.18 -> constrains -> G.11 EvaluatingAndRefreshing.** EditionBumpProposal, two-phase update through the UNM declaration locus, path-local refresh.

**Work boundary**
* **E.18 -> coordinates with -> A.15 U.WorkEnactment (`FinalizeLaunchValuesOnlyInWork`).** Single point of `FinalizeLaunchValues`; `FreshnessUpToDate` hard at LaunchGate; acceptance and telemetry published here.

**Structure and reuse**
* **E.18 -> provides selected-structure base for transformation-flow families.** Flow patterns such as P2W and EvaluatingAndRefreshing use E.18 for selected structure, valuation, crossings, guards, MVPK faces, and slice-local refresh. The current ontology is: `A.3.4` governs each bounded `U.Transformation`, E.18 governs the selected compound structure over transformations and adjacent governed loci, and the named governing patterns govern method, work, mechanism, evidence, publication, gate, decision, and refresh claims when those claims are current.
* **E.18 -> coordinates with -> architecture transformation-flow relation patterns.** When a selected transformation-flow structure is used in an architecture-flow relation, the architecture transformation-flow relation pattern records the relation between `TransformationFlowStructure` and `ArchitectureOf@Context`; E.18 keeps selected structure, crossing, and flow-valuation discipline.
* **E.18 -> publishes_on -> E.17 MVPK views** (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) for every transfer or locus where publication occurs; Lean mode applies only as per profile.

