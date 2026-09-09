---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Frame Standard and Comparability Governance — CG‑Spec"
section_id: "G.0:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__008_conformance-checklist-normative.md"
commit_sha: "aa10af7e8221518114822d00bb9cf11e6c41f6b2"
heading_path:
  - "G.0 — Frame Standard and Comparability Governance — CG‑Spec"
  - "G.0:7 — Conformance Checklist (normative)"
line_start: 102170
line_end: 102192
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.5"
  - "E.5.2"
  - "F.9"
  - "G.1"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "CG-Frame"
  - "CG-Spec"
  - "CL-routing"
  - "ComparatorSet"
  - "MinimalEvidence"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "ScaleComplianceProfile (SCP)"
  - "admissibility gate"
  - "edition pins"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:7 - Conformance Checklist (normative)

| ConformanceId | Statement |
| --- | --- |
| **CC‑G0‑CoreRef** | `G.0` is conformant only if the applicable core obligations listed in `G.0:4.1` are satisfied (delegation to `CC‑GCORE‑*`; no shadow specs, no competing defaults, typed RSCR triggers, explicit pins). |
| CC‑G0‑01 | `CG‑Spec` is published as a notation-independent UTS object with explicit `Edition`, `Context`, `Scope`, `entityOfConcern`, and a minimum `ReferenceMap`. |
| CC‑G0‑02 | `CNSpecRef.edition` is present and identifies the edition of the external governance card cited by `CNSpecRef` (no local redefinition of CN semantics). *(Delegation target: `CC‑GCORE‑CN‑CG‑1`.)* |
| CC‑G0‑03 | `ComparatorSet` is explicit and finite; each comparator is typed and bound to `SCP` and referenced CHR characteristics; **anything not enumerated MUST be treated as illegal/abstain by default** (no implicit comparator defaults). |
| CC‑G0‑04 | `SCP` declares, per characteristic, the lawful operation regime needed for each referenced comparator (scale/unit/polarity constraints and any required proofs/refs). |
| CC‑G0‑05 | `MinimalEvidence` is declared per characteristic and includes explicit lane/carrier requirements, freshness window references (if any), and explicit failure behavior wiring (tri-state semantics delegated). If freshness windows are used, a stable reference making the applicable window recoverable (e.g., a `PathSliceId` with its declared time window) MUST be pinned for audit. |
| CC‑G0‑06 | The edition-addressable Γ-fold segment **MUST** cite `DefaultId.GammaFoldForR_eff` at `G.5 CC‑G5.4`. Pin any numerical model/policy actually used, with its receiving quantity, input meanings and scales, dependencies, operation and proof/justification refs as required by that governing rule and B.3/C.2.2. With no justified numerical fold, retain the separate support permitted by the governing rule; the segment is not a demand for a score. |
| CC‑G0‑07 | If crossing penalties are used, `CL‑Routing` and `Φ` policy ids are explicit and auditable (policy ids are exposed as pins/refs) **and are required pins for downstream SCR publication on penalised claims** (see `G.6`). |
| CC‑G0‑08 | `AcceptanceStubs` in `CG‑Spec` are templates only; any context-local thresholds/acceptance policies are governed by CAL acceptance artefacts (G.4) and are cited, not duplicated. |
| CC‑G0‑09 | RSCR tests and triggers for edits to legality surfaces and evidence minima are present and use canonical `RSCRTriggerKindId`s. The RSCR test set SHOULD cover at least: illegal_op_refusals; unit and scale legality checks; freshness windows; partial-order scalarisation refusals; threshold semantics; CL→`R_eff` routing; refusal of `degrade.order` on unit mismatches (MM‑CHR). |
| CC‑G0‑10 | `PublicIdContinuity` is declared: governing definition, DRR link, refresh cadence, decay and aging policy, and deprecations. Deprecations preserve lexical continuity (Δ-discipline; delegated to `CC‑GCORE‑ID‑*`). |
| CC‑G0‑11 | *(Conditional)* If `Illumination` / QD hooks are present, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and any `InsertionPolicyRef` / promotion policy ids are pinned (or explicitly marked absent) and are recorded in provenance/audit pins. |
| CC‑G0‑12 | *(Conditional)* If freshness windows influence gating/selection, they are published and enforced, and references making the relevant windows recoverable (`PathSliceId` with a declared time window, or equivalent) are recorded in SCR/audit pins. |
| CC‑G0‑13 | **Pre-flight numeric gates.** Any numeric comparison/aggregation declared in `ComparatorSet` has associated `GateChecks` for unit legality, scale legality, pinned SOP/editions, and declared comparability assumptions; failing any check requires refusing the operation or returning an `abstain` guard result (tri-state semantics delegated). |
| CC‑G0‑14 | **GateCrossing hook exposure.** Exports provide `Expose_CrossingHooks` inputs so `GateChecks` (`E.18/A.21`) can validate plane consistency, crossing intent, lane purity, and lexical SD; failures MUST block publication. |
| **CC‑G0‑Φ** | An actually used numerical Φ(CL) or plane-loss policy has a justified receiving quantity, scale, input interpretation, assumptions, and derivation or calibration under B.3/C.2.2. Publish the policy ids and any required table. Preserve the model's loss direction and bounds; monotonicity, boundedness, or clipping alone does not establish a valid loss model. |
| **CC‑G0‑Unknowns** | *Delegated.* Unknown handling MUST follow the tri-state guard semantics `{pass|degrade|abstain}` with no silent coercions. (See `CC‑GCORE‑GUARD‑1`.) |
| **CC‑G0‑CSLC** | Scale/unit/polarity legality MUST be proven before any aggregation; illegal arithmetic on ordinal/nominal values is nonconformant. (Governed by the relevant legality patterns; `G.0` only binds and cites.) |

