---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "U.Flow.ConstraintValidity — Eulerian"
section_id: "A.20:Appendix"
section_title: "A — CV Class Gloss (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__014_a-cv-class-gloss-normative.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.20 — U.Flow.ConstraintValidity — Eulerian"
  - "A.20:Appendix — A — CV Class Gloss (normative)"
line_start: 28145
line_end: 28170
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
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
  - "TransductionFlow"
  - "flow"
---

### A.20:Appendix A — CV Class Gloss (normative)

* **MechanismUnitsCoherence.** Internal unit and scale coherence within the step when quantities, scales, units, or reference planes are actually used; no declarations or translations of units/planes occur in CV.
* **LawSetInvariants.** Mechanism-declared invariants hold (e.g., mass/energy balance in a model, determinism under fixed editions).
* **AdmissibilityConditionsSatisfaction.** Inputs lie within admissible windows/guards declared by the mechanism's **AdmissibilityConditions**; failure yields `degrade` or `abstain` per class policy.
  **Minimum declaration (normative):**
  `AdmissibilityDecl := { domains: {name: set/poset}+, guards: [predicate_id]*, windows: {Γ_time: snapshot|interval|policy}, observables: [signal_id]*, edition: EditionId }`.
  The declaration is published on MVPK as references only; it introduces no arithmetic on faces.
  **Minimal declaration template (normative):**
  `AdmissibilityConditions := { Domains[]{var, type, range, units, plane}, Guards[]{predicate, editionRefs}, ObservationWindows[]{Γ selector, freshness window}, ObservableSigns[]{name, detection rule}, Editions{...} }`
  — **No unit/plane declaration or translation** here; only references. Γ selectors SHALL be explicit.
* **LipschitzBounds / stability.** Bounded sensitivity under a declared metric, used only when a perturbation, sensitivity, robustness, continuity, safety-envelope, or stability claim changes the CV use.
  **Publication ref shape (normative):**
  `LipschitzBoundRef := { method ∈ {spectral_norm|CROWN|IBP|rand_smoothing|other}, metric_space: {X: norm_id, Y: norm_id}, bound: value_or_interval, units/plane: P, validity_window: Γ_time(basis), edition: EditionId, certificateRef?: LipschitzCertificateId }`.
  **Referenced evidence/certificate object (normative):**
  `LipschitzCertificate := { metricId (with units and plane), bound L, methodId, methodRef (e.g., spectral estimate or certified robustness bound), validity region (inputs and state), proof sketch or reference }`.
  The method MUST be cited; units/plane of the metric MUST be explicit; proofs and witness records are referenced; bounds are ref-only at CV; any acceptance action remains GateFit.
* **TypeDomainRange.** Well-typedness and type, domain, and range consistency for the transformation signature; refs point to the governing definitions.
* **ReinterpretationEquivalence (StructuralReinterpretation only).** Existence of a correspondence/reversibility witness between source and retarget projections; preservation of `⟨L,P,E⃗,D⟩`; no comparator/plane/unit declaration or translation at CV.
  **Witness (normative):** `ReinterpWitness` / `ReinterpretationEquivalenceWitness` (see §4.7) with: `(i)` `PathSliceId`, `PublicationScopeId`, `(ii)` bidirectional mapping (iso/optic) with Put-Get/Get-Put obligations, `(iii)` commuting squares for adjacent raw transfers, `(iv)` **NoHiddenScalarization** assertion when comparable, and `(v)` definedness region.
  The witness is PathSlice-local and is admissible only for idempotence and reversibility within the addressed slice. Any EntityOfConcernRef change SHALL have `KindBridge (CL^k)` on UTS.

#### A.20:Appendix B — LEX discipline (summary)

Register token classes (Tech) include: `U.TransductionFlow`, `U.TransductionGraph`, `OperationalGate`, `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`, `FreshnessTicket`, `FinalizeLaunchValues`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `VALATA`; discriminators use `Base__P2W`, `Base__EvaluatingAndRefreshing`; Tech names are ASCII; aliases `GammaTimeRule/Plane`, `CLPlane`, `Phi` follow E.10. A.20 references these tokens; it does not introduce additional LEX classes. **For each published CV check, `GateCheckRef.aspect` is fixed to `ConstraintValidity`.** *MVPK minima for CV faces also include `PathId/PathSliceId` where slice-local refresh applies through `E.18`, `A.20`, and `G.11` when live.*

