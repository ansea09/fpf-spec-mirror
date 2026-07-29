---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:6"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__008_archetypal-grounding-tell-show-show.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:6 — Archetypal Grounding (Tell–Show–Show)"
line_start: 51039
line_end: 51068
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
*Attachment.* **CG‑Spec** forbids means over **service\_level** (ordinal); **Acceptance** holds acceptance-gate thresholds; **Eligibility** checks convex‑relaxation availability; **Selection** applies **lexicographic** guard (assumption‑fit ≻ evidence‑fit ≻ resource), compute **R\_eff** with Γ‑fold, apply **CL** penalty to **R** only; if partial order remains, return a **Pareto set**.

> *Current practice anchor:* the 2026 [SciML Problem Interface](https://docs.sciml.ai/DiffEqDocs/stable/basics/problem/) constructs an immutable problem value before solver use and supports explicit `remake` when problem fields change. C.22 adapts only that problem-before-selector separation; it does not import Julia types as FPF ontology.

**C. Quality-Diversity archive and declared set (illumination).**
*ProblemProfile.* `DataShape=policy‑search; ObjectiveProfile={↑reward@ratio, ↑coverage@ratio (report‑only)}, DominanceRegime=ParetoOnly, PortfolioMode=Archive, CharacteristicSpaceRef(d=3, characteristics=CHR‑typed), ArchiveConfig(grid, res=32×32×16, K=1, InsertionPolicyRef=elite‑replace, DistanceDefRef.edition=v1), EmitterPolicyRef=v2, Budgeting{eval=1e6}, TelemetryHooks{PathSliceId=…}`.
*Selection result.* Selector may return an **archive**; **coverage and illumination** are **reported** but **excluded** from dominance (default). Any change of `DistanceDefRef.edition` or Emitter policy is **editioned** and logged in SCR.

**D. Open‑ended environment generation (POET‑class).**
*ProblemProfile.* `GeneratorIntent{GeneratorFamilyRef=…, EnvironmentValidityRegion=… (CHR‑typed), TransferRulesRef=…, CoverageMetric=…}`, `PortfolioMode=Archive`.
*Selection result.* Selector outputs **{environment, method}** pairs that pass Eligibility; **TransferRules** govern cross‑environment policy reuse; telemetry reports **coverage and regret** and **IlluminationSummary** with **edition and policy‑id** when improved.

**E. Physical manufacturing method-family eligibility.**
*Problem-side record.* A shop must finish a declared alloy-part family inside one machine and inspection context. The receiving question is which available finishing-method families can be compared without presuming one of them.
*TaskSignature.* `TaskKind=surface-finishing work`, `ProblemSideRecordRef=accepted part-family problem card`, `ScopeSlice(G)=declared part family and production window`, `ObjectiveProfile={surface roughness Ra@ratio in micrometres with downward polarity, throughput@ratio}`, `ConstraintRefs={geometric-tolerance relation, heat-distortion relation, resource-envelope relation}`, and material-hardness condition as a live `unknown` with an explicit measurement relation and unknown-handling policy. The TaskSignature makes eligibility reviewable; it does not select grinding, honing, polishing, or another method and does not establish that any part was finished.

**F. Clinical rehabilitation method-family eligibility.**
*Problem-side record.* A rehabilitation service has a bounded patient cohort and must compare admissible intervention families for a stated capability-change question under clinical safety constraints.
*TaskSignature.* `TaskKind=rehabilitation-method-family comparison`, `ProblemSideRecordRef=accepted cohort problem record`, `ScopeSlice(G)=declared cohort and care setting`, outcome characteristics with their actual scale kinds and follow-up windows, contraindication and resource constraints, current evidence relations, and unknown tolerance or comorbidity values preserved as unknown. C.22 makes the comparison inputs explicit. It does not diagnose a person, recommend treatment, authorize care, prove benefit, or record performed clinical work; those claims remain with their clinical, evidence, gate, role, and work patterns.

