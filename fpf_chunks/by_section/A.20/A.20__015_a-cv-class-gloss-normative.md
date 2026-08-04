---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:Appendix"
section_title: "A — CV Class Gloss (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__015_a-cv-class-gloss-normative.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:Appendix — A — CV Class Gloss (normative)"
line_start: 33886
line_end: 33911
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:Appendix A — CV Class Gloss (normative)

* **MechanismUnitsCoherence.** Internal unit and scale coherence within the step when quantities, scales, units, or reference planes are actually used; no declarations or translations of units or planes occur in CV.
* **LawSetInvariants.** Mechanism-declared invariants hold (e.g., mass or energy balance in a model, determinism under fixed editions).
* **AdmissibilityConditionsSatisfaction.** Inputs lie within the windows and guards declared by the mechanism's **AdmissibilityConditions**; failure yields `degrade` or `abstain` per class policy.
  **Minimum declaration (normative):**
  `AdmissibilityDecl := { domains: [{name, structureKind ∈ {set, poset}}]+, guards: [predicate_id]*, windows: {Γ_time ∈ {snapshot, interval, policy}}, observables: [signal_id]*, edition: EditionId }`.
  The declaration is published on MVPK as references only; it introduces no arithmetic on faces.
  **Minimal declaration template (normative):**
  `AdmissibilityConditions := { Domains[]{var, type, range, units, plane}, Guards[]{predicate, editionRefs}, ObservationWindows[]{Γ selector, freshness window}, ObservableSigns[]{name, detection rule}, Editions{...} }`
  — **No unit or plane declaration or translation** here; only references. Γ selectors SHALL be explicit.
* **LipschitzBounds for stability claims.** Bounded sensitivity under a declared metric, used only when a perturbation, sensitivity, robustness, continuity, safety-envelope, or stability claim changes the CV use.
  **Publication ref shape (normative):**
  `LipschitzBoundRef := { boundDerivation ∈ {spectral_norm, CROWN, IBP, rand_smoothing, other}, metric_space: {X: norm_id, Y: norm_id}, bound: value or interval, unitRef?: UnitRef, referencePlaneRef?: ReferencePlaneRef, effective_window: Γ_time(selector), edition: EditionId, certificateRef?: LipschitzCertificateId }`.
  **Referenced evidence or certificate value (normative):**
  `LipschitzCertificate := { metricId (with units and plane), bound L, boundDerivationId, boundDerivationRef (e.g., spectral estimate or certified robustness bound), validity region (inputs and state), proof sketch or reference }`.
  The bound-derivation technique or its method description MUST be cited; unit reference and plane reference of the metric MUST be explicit; proofs and witness records are referenced; bounds are ref-only at CV; any acceptance action remains GateFit. If the technique itself is relied on as a reusable `U.Method`, use `A.3.1` and `A.3.2`; A.20 only records the CV-bound reference.
* **TypeDomainRange.** Well-typedness and type, domain, and range consistency for the transformation signature; refs point to the governing definitions.
* **ReinterpretationEquivalence (StructuralReinterpretation only).** Existence of a correspondence and reversibility witness between source and retarget projections; preservation of `⟨L,P,E⃗,D⟩`; no comparator, plane, or unit declaration or translation at CV.
  **Witness (normative):** `ReinterpWitness` or `ReinterpretationEquivalenceWitness` (see §4.7) with: `(i)` `PathSliceId`, `PublicationScopeId`, `(ii)` bidirectional mapping (iso or optic) with Put-Get and Get-Put obligations, `(iii)` commuting squares for adjacent raw transfers, `(iv)` **NoHiddenScalarization** assertion when comparable, and `(v)` definedness region.
  The witness is PathSlice-local and usable only for idempotence and reversibility within the addressed slice. Any EntityOfConcernRef change SHALL have `KindBridge (CL^k)` on UTS.

#### A.20:Appendix B — LEX discipline (summary)

Register token classes (Tech) include: `TransformationFlowStructure`, `TransformationFlowMathDescription`, `OperationalGate`, `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`, `FreshnessTicket`, `FinalizeLaunchValues`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `VALATA`; discriminators use `Base__P2W`, `Base__EvaluatingAndRefreshing`; Tech names are ASCII; aliases for Gamma-time rules and plane lexemes, plus `CLPlane` and `Phi`, follow E.10. A.20 references these tokens; it does not introduce additional LEX classes. **For each published CV check, `GateCheckRef.aspect` is fixed to `ConstraintValidity`.** *MVPK minima for CV faces also include `PathId` and `PathSliceId` where slice-local refresh applies through `E.18`, `A.20`, and `G.11` when refresh wiring is present.*

