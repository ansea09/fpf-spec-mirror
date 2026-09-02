---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:6"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__008_archetypal-grounding-tell-show-show.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:6 — Archetypal Grounding (Tell–Show–Show)"
line_start: 51898
line_end: 51933
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:6 - Archetypal Grounding (Tell–Show–Show)

*Tell–Show–Show hook (per E.8):* label examples as **Show‑1 (continuous ODE)** and **Show‑2 (MIP)** and cite CHR guard‑macros in‑line so engineers can see **which field supplied which Eligibility or Acceptance input**.  **Explicitly annotate which S2 fields triggered each Eligibility and Acceptance decision** (e.g., `service_level@ordinal → ORD_COMPARE_ONLY`, `budget@ratio → unit alignment check`).

**A. Differential equations (continuous systems, solver choice).**
*ProblemProfile.* `DataShape=ODE, stiff?=unknown, SizeAndConditionProfile={n≈10^3}, ObjectiveProfile={↓error@ratio, ↑throughput@ratio}, ConstraintRefs={budget-envelope relation, safety-predicate relation}, RegularityTraits={Lipschitz known?=unknown, Jacobian sparsity=high}, Missingness=MAR`.
*Attachment.* Selector consumes TaskSignature; **eligibility** filters MethodFamilies whose acceptance conditions include known stiffness or differentiability, with unknown yielding **degrade or abstain** per family. **Acceptance** treats `safety_gate` as an **ordinal predicate**, not an average (`ORD_COMPARE_ONLY`), and treats budgets with **unit-aligned sums** on ratio scales. The selector returns a **Pareto set**; no cross-ordinal weighting.

**B. Mixed‑integer optimisation (planning and scheduling).**
*ProblemProfile.* `DataShape=MIP, NoiseModel=deterministic, ObjectiveProfile={↓cost@ratio, ↑service_level@ordinal}, Constraints={SLA hard, workforce soft}, RegularityTraits={convex_relaxation=available}, SizeAndConditionProfile={vars~10^5}, Missingness=MCAR`.
*Attachment.* **CG‑Spec** forbids means over **service_level** (ordinal); **Acceptance** holds acceptance-gate thresholds; **Eligibility** checks convex-relaxation availability; **Selection** applies the **lexicographic** guard (assumption-fit before evidence-fit before resource). If a named assurance use or material-reliance threshold is current, B.3 computes its separate assurance result from the relied-on evidence relations and the declared policy; otherwise this example adds no assurance fold. If the admissible comparison remains partial, return a **Pareto set**.

> *Current practice anchor:* the 2026 [SciML Problem Interface](https://docs.sciml.ai/DiffEqDocs/stable/basics/problem/) constructs an immutable problem value before solver use and supports explicit `remake` when problem fields change. C.22 adapts only that problem-before-selector separation; it does not import Julia types as FPF ontology.

**C. Quality-Diversity archive and declared set (illumination).**
*ProblemProfile.* `DataShape=policy‑search; ObjectiveProfile={↑reward@ratio, ↑coverage@ratio (report‑only)}, DominanceRegime=ParetoOnly, PortfolioMode=Archive, CharacteristicSpaceRef(d=3, characteristics=CHR‑typed), ArchiveConfig(grid, res=32×32×16, K=1, InsertionPolicyRef=elite‑replace, DistanceDefRef.edition=v1), EmitterPolicyRef=v2, Budgeting{eval=1e6}, TelemetryHooks{PathSliceId=…}`.
*Selection result.* Selector may return an **archive**; **coverage and illumination** are **reported** but **excluded** from dominance (default). Any change of `DistanceDefRef.edition` or Emitter policy is **editioned** and logged in SCR.

**D. Open‑ended environment generation (POET‑class).**
*ProblemProfile.* `GeneratorIntent{GeneratorFamilyRef=…, EnvironmentValidityRegion=… (CHR‑typed), TransferRulesRef=…, CoverageMetric=…}`, `PortfolioMode=Archive`.
*Selection result.* Selector outputs **{environment, method}** pairs that pass Eligibility; **TransferRules** govern cross‑environment policy reuse; telemetry reports **coverage and regret** and **IlluminationSummary** with **edition and policy‑id** when improved.

**E. Physical manufacturing method-family eligibility.**
*Problem-side episteme.* `PartFamilyFinishingProblemCard-E2 : U.Episteme` is the exact C.22.2 ProblemCard for a shop that must finish `AlloyPartFamily-17` on one machine under `ShopInspectionScheme-E4` and a production-window ClaimScope. The receiving question is which available finishing-method families can be compared without presuming one of them.
*TaskSignature.* `SurfaceFinishingEligibilitySignature-E1` declares `EntityOfConcernRef=AlloyPartFamilyFinishingTarget-17`, `effectiveReferenceScheme=ShopFinishing-Scheme-A`, `TaskKind=surface-finishing work`, `ScopeSlice(G)=AlloyPartFamily-17 during [2026-09-01T00:00Z, 2026-10-01T00:00Z)`, `ObjectiveProfile={surface roughness Ra@ratio in micrometres with downward polarity, throughput@ratio}`, `ConstraintRefs={geometric-tolerance relation, heat-distortion relation, resource-envelope relation}`, and material-hardness condition as a live `unknown` with an explicit measurement relation and unknown-handling policy. The TaskSignature makes eligibility reviewable; it does not select grinding, honing, polishing, or another method and does not establish that any part was finished.
*Assignment.* `FinishingMethodEligibilityUse-E1 : U.Episteme` states the exact receiving eligibility-comparison use. `TaskSignatureAssignmentRelation(PartFamilyFinishingProblemCard-E2, SurfaceFinishingEligibilitySignature-E1, FinishingMethodEligibilityUse-E1)` has exactly the problem-side episteme, signature, and receiving-use episteme as participants. It obtains only while that receiving use actually adopts that exact signature as the task-typing declaration for that exact card under `ShopFinishing-Scheme-A`, the declared part-family scope, `ShopInspectionScheme-E4`, and the production window above. Withdrawal of that adoption or change of a participant or qualification ends this assignment occurrence; a shared row, carrier, or publication does not make it obtain.

**F. Clinical rehabilitation method-family eligibility.**
*Problem-side episteme.* `CohortRehabilitationProblemCard-E3 : U.Episteme` is the exact C.22.2 ProblemCard for a rehabilitation service with `Cohort-2026-Q3` and a stated capability-change question under clinical safety constraints.
*TaskSignature.* `RehabilitationFamilyComparisonSignature-E1` declares `EntityOfConcernRef=RehabilitationCapabilityChangeTarget-4`, `effectiveReferenceScheme=ClinicalRehabilitation-Scheme-C`, `TaskKind=rehabilitation-method-family comparison`, and `ScopeSlice(G)=Cohort-2026-Q3 in the declared care setting during [2026-08-01T00:00Z, 2026-11-01T00:00Z)`. It also declares outcome characteristics with their scale kinds, contraindication and resource constraints, and unknown tolerance or comorbidity values preserved as unknown. Include the evidence relations and follow-up windows only because this comparison use relies on them.

C.22 makes the comparison inputs explicit. It does not diagnose a person or recommend treatment; those claims use their clinical patterns. It does not establish evidence or benefit, pass a gate, grant permission to provide care, or establish decision authority. Use the evidence and evaluation patterns, the gate patterns, an obtaining `GrantedPermissionRelation@Context`, or an authority predicate, or return `missing-governor`.

If clinical Work occurs, recover each exact actual performer System through A.13 and let A.15.1 independently admit the dated Work and its enacted Method. Add an assignment occurrence, its declared species, and F.6 only when this clinical account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. A local system-role kind, classification, or assignment can remain a neighboring fact, but it establishes none of the permission or authority relations above.
*Assignment.* `RehabilitationInterventionFamilyComparisonUse-E1 : U.Episteme` states the exact receiving comparison use. `TaskSignatureAssignmentRelation(CohortRehabilitationProblemCard-E3, RehabilitationFamilyComparisonSignature-E1, RehabilitationInterventionFamilyComparisonUse-E1)` has exactly the problem-side episteme, signature, and receiving-use episteme as participants. It obtains only while that receiving use actually adopts that exact signature for that exact card under `ClinicalRehabilitation-Scheme-C`, the declared cohort and care ClaimScope, the qualification window above, and the stated evidence-use conditions. Withdrawal of that adoption or loss of a participant or qualification ends this assignment occurrence; cohort labels, records, carriers, and organizations add no signature field or fourth participant.

