---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher & MethodFamily Registry"
section_id: "G.5:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__013_conformance-checklist-normative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "G.5 — Multi‑Method Dispatcher & MethodFamily Registry"
  - "G.5:7 — Conformance Checklist (normative)"
line_start: 79192
line_end: 79238
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry/eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:7 - Conformance Checklist (normative)

| ConformanceId   | Statement |
| --------------- | ----------|
| `CC‑G5‑CoreRef` | **Core conformance bridge.** `G.5` is conformant only if the **effective** `G.Core` obligations referenced by `G.5:4.1 (GCoreLinkageManifest)` are satisfied (after profile/set expansion and explicit deltas). |
| `CC‑G5.0`       | Core standards **SHALL** remain notation‑independent; vendor/tool keywords are forbidden in registry, eligibility, assurance, or selector‑kernel obligations (E.5.*). |
| `CC‑G5.1`       | Every `MethodFamily` **SHALL** declare an `EligibilityStandardRef` using CHR/CAL terms (typed; edition‑pinned where applicable). Standards **SHALL NOT** rely on tool‑specific keywords.  |
| `CC‑G5.2`       | Selection **SHALL** be a pure function of `TaskSignatureRef` + pinned policy/edition refs; side effects are limited to emitting DRR/SCR pins and telemetry/RSCR triggers (no hidden mutation of constraint-bearing spec refs). |
| `CC‑G5.3`       | **Delegated (ID‑continuity).** Cross‑Context use **MUST** follow `G.Core` crossing visibility and penalty routing. **Delegation targets:** `CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`.  |
| `CC‑G5.4`       | **Default rule for** `DefaultId.GammaFoldForR_eff`. The selector **MUST** default to the weakest‑link rule for `R_eff` and record contributors in SCR; it **MAY** use an alternative Γ‑fold only when provided by an explicitly pinned policy/profile with proof obligations satisfied (monotonicity; boundary behavior). |
| `CC‑G5.5`       | Ordinal scales **MUST NOT** be averaged/subtracted; any aggregation/comparison must respect CHR scale typing and legality constraints (incl. CSLC where applicable). |
| `CC‑G5.6`       | Method and generator family identities **SHALL** be published to UTS with the required naming discipline (twin labels where applicable; deprecations follow lexical continuity rules). *(Core conformance applies; `G.5` adds the registry‑specific publication obligation.)* |
| `CC‑G5.7`       | **Conditional.** If `G.5:Ext.EELog` is present, exploration **MUST** be budgeted under the pinned E/E‑LOG policy; probe outcomes **MUST** feed refresh via canonical RSCR trigger kinds. |
| `CC‑G5.8`       | **CG‑Frame gate enforced.** Selection rejects or abstains from candidates that do not meet the pinned `CG‑Spec.MinimalEvidence` requirements for the characteristics they cite. |
| `CC‑G5.9`       | **Delegated (ID‑continuity).** Set‑return semantics are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑SET‑1`. Candidate ordering **MUST** be admissible over typed traits and legality constraints. If only a partial order is available, selection **MUST** return one declared selector outcome (for example one `SetResultOutcome` with `Shortlist`/`RankedShortlist`, one `HandoffOutcome` with `SpecialistHandoff`, or another pinned outcome result), with no forced totalisation via illegal scalarisation. |
| `CC‑G5.10`      | **SCR completeness.** SCR **MUST** enumerate Γ‑fold contributors (when used), referenced constraint-bearing spec editions, the evidence citations (`PathId/PathSliceId`) used in gating/rationale, and `MinimalEvidence` gating verdicts *(by lane & carrier, when such gating is relied upon).* |
| `CC‑G5.11`      | **Delegated (ID‑continuity).** Tri‑state eligibility/acceptance semantics and unknown handling are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑GUARD‑1`. *(Includes the rule that `degrade(...)` is expressed via a pinned FailureBehavior/SoS‑LOG branch id — not as a fourth status.)* |
| `CC‑G5.12`      | **No “universal” cross‑Tradition scoring.** Cross‑Tradition selection **MUST NOT** rely on a single numeric formula not justified by pinned CHR/CAL constraints and the constraint-bearing spec refs. If a triad or selected set **claims universality**, it **MUST** satisfy **explicit, pinned** heterogeneity gates (ids/pins), e.g., `FamilyCoverage ≥ k` and `MinInterFamilyDistance ≥ δ_family`, where `k` and `δ_family` are declared by the pinned policy/TaskSignature/SoTA pack, and cite the relevant **Context Card id (F.1)** in DRR/SCR; otherwise treat the outcome as Context‑local.  |
| `CC‑G5.13`      | **Conditional.** If the selector consumes admissibility/maturity records (e.g., via `G.5:Ext.SoSLOG`), it **MUST NOT** recompute thresholds; it consumes pinned admissibility ledger rows and cites clause/rung ids in audit pins. |
| `CC‑G5.14`      | **Φ(CL) / Φ_plane discipline.** If crossing or plane penalties are applied, the active penalty policy ids (e.g., `Φ(CL)`, `Φ_plane`) **MUST** be explicit in audit pins, and the pinned policies **MUST** satisfy the monotone & bounded requirements asserted by their cited constraint-bearing spec refs and be published via those same cited spec refs (e.g., `CG‑Spec`). SCR **MUST** record the policy‑id in use; penalty routing semantics remain pinned through `G.Core`. |
| `CC‑G5.15`      | Unit and scale legality **MUST** be established via CSLC (A.18) before any aggregation or Γ‑fold; unit and scale mismatches are a fail‑fast defect. |
| `CC‑G5.16`      | Hidden thresholds are forbidden. Thresholds live in explicitly pinned acceptance/eligibility policy records, not in selector prose, LOG shells, or code.  |
| `CC‑G5.17`      | ReferencePlane **MUST** be declared (pinned) for any claim that is used in dispatch, and the selector’s audit records must cite it (including plane‑crossing pins when applicable). |
| `CC‑G5.18`      | Numeric comparisons/aggregations used by dispatch **MUST** cite an admissible, edition‑pinned comparator/spec publication (as provided by the constraint-bearing spec refs); illegal mixes of scale types are forbidden. |
| `CC‑G5.19`      | **Conditional (QD).** If `G.5:Ext.NQD` is present, the required QD telemetry triple (quality/diversity/QD summary) **MUST** be computable and publishable under the pinned descriptor/distance definitions and archive policy, without redefining their semantics in G.5. |
| `CC‑G5.20`      | **Conditional (QD).** QD/illumination summaries are treated as telemetry unless explicitly promoted by a pinned acceptance/policy record; the selector must record the promoting policy id in audit pins. |
| `CC‑G5.21`      | **Conditional (Archive/QD).** Any use of archives **MUST** declare `InsertionPolicyRef` and pin the required editions for reproducibility (e.g., descriptor/distance definitions and any method editions they depend on).  |
| `CC‑G5.22`      | **Conditional (QD).** Twin‑naming discipline for descriptor vs plain space (if used) must be respected (distinct objects; no aliasing).  |
| `CC‑G5.23`      | **Default rule for** `DefaultId.PortfolioMode`. The selector **MUST** expose `PortfolioMode ∈ {Pareto, Archive}` with **default = `Archive`**, and echo it in DRR/SCR and declared selector results when not explicitly overridden by pinned policy/TaskSignature. The default is a retention/evidence-preservation policy, not a public selected-set label, not a dominance default, and not a substitute for `SetResultFamily`. `ε`‑fronts are allowed as *local* decision aids under `CG‑Spec` when explicitly pinned.  |
| `CC‑G5.23a`     | **Parity‑run publication.** If parity harness is in use, a selector/generator **MUST** publish a parity run and `ParityCard` to **UTS** (see `G.9`). This obligation remains mandatory irrespective of dominance/`PortfolioMode` policy. |
| `CC‑G5.24`      | **Conditional (Open‑Ended).** If `G.5:Ext.OpenEndedFamilyWiring` is present, the selector **MUST** return declared sets of `{Environment, MethodFamily}` pairs as set‑valued outcomes under explicit pins. |
| `CC‑G5.25`      | **Conditional (Open‑Ended).** In Open‑Ended mode, `TransferRulesRef.edition` is mandatory and **MUST** be visible to telemetry and RSCR triggers.  |
| `CC‑G5.26`      | **Conditional (Archive/QD).** Within any archive niche/cell, ordering and tie‑breaks **MUST** remain admissible over compatible scales; illegal mixed‑scale weighted sums are forbidden. |
| `CC‑G5.27`      | If the selector cites any `GateCrossing`, the corresponding `CrossingBundle` publication **MUST** be present and conformant; missing/non‑conformant `CrossingBundle` blocks downstream consumption. |
| `CC‑G5.28`      | **Default rule for** `DefaultId.DominanceRegime`. `DominanceRegime` **SHALL** default to `ParetoOnly`. Any inclusion of additional telemetry dimensions into dominance (e.g., illumination) requires an explicitly pinned acceptance/policy record and must be recorded in audit pins. **Parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy. |
| `CC‑G5.29`      | **Conditional (QD/Open‑Ended).** Any telemetry event that materially changes an archive / retained-set state **MUST** log `PathSliceId`, the active policy id, and the active editions of the relevant definition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `TransferRulesRef.edition` when applicable) and expose them to RSCR triggers. |
| `CC‑G5.30`      | **No Strategy minting.** Within `G.5`, “strategy” is a policy‑bound composition template; the pattern **SHALL NOT** mint a new universal `U.Type` named `Strategy` (E.10 discipline). If a stable reference is needed, publish composition/policy ids (e.g., UTS entries) rather than minting a universal type. |
| `CC‑G5.31`      | **Strategy hint on non‑admissible sets.** If selection yields `CandidateSet = ∅`, the selector **SHALL** emit an explicit escalation hint (`ActionHint`) that is **DRR/SCR‑compatible** and auditable: include (at minimum) the top‑3 blocking constraints as cited ids/pins, and (where applicable) the relevant edition pins (e.g., `TransferRulesRef.edition` in Open‑Ended mode) to guide exploration under explicitly pinned lenses (e.g., E/E‑LOG). |
| `CC‑G5.32`      | **Parity‑run publication + admissible roll‑ups.** If parity harness is in use, parity publication is required per `CC‑G5.23a` (ID‑continuity). Any scalar roll‑up or summary view **MUST** be admissible under **CG‑Spec** (no mixed‑scale sums), and published views must preserve set‑return semantics (no single‑score leaderboards as authoritative outputs without an explicit, admissible comparator publication). |
| `CC‑G5.33`      | **Conditional (bounded specialization).** When the selection question is acquisition of usable specialization on a declared `TaskFamilyRef` or `TaskSignature`, selector outputs **SHALL** either publish `TaskFamilySpecializationProfile@Context` or cite equivalent pins carrying the `C.22.1` adaptation-signature fields needed for comparison: work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, and any declared transfer, retention, downside, or specialization-entry notes. |
| `CC‑G5.34`      | **Selected-set publication label.** When `SelectorOutcomeKind = SetResultOutcome`, the published selected-set label **MUST** be explicit. Use `Shortlist` as the public selected-set label, `RankedShortlist` only when ordering materially belongs to the result, publish `ShortlistId` when one public identifier is emitted, and do not silently let `ChoiceSet` replace that public label. |
| `CC‑G5.34a`     | **Selector outcome typing.** Published selector results **MUST** declare `SelectorOutcomeKind`. `SetResultFamily` is required only when `SelectorOutcomeKind = SetResultOutcome`; `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`. Non-set outcomes **MUST NOT** masquerade as one public selected-set label. |
| `CC‑G5.35`      | **Publication closure.** Any published selector result **MUST** state the declared `SelectorOutcomeKind`, any applicable public selected-set label, retained members or narrowed handoff content, ordering status (when applicable), and basis pins directly in the emitted result rather than relying on upstream `C.11`, `C.19`, or `C.24` notes. |
| `CC‑G5.36`      | **Neighboring-pattern boundary.** If the current question is still local choice among already-available options, pool policy over still-live candidate lines, or enactment planning after choice, `G.5` **MUST** consume the published result from `C.11`, `C.19`, or `C.24` rather than restating those patterns as if publication itself decided the matter. |
| `CC‑G5.37`      | **Derived tradition-view publication discipline.** If the selector publishes one result through a derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep the declared base `SourceSetFamily` explicit, keep `SoTAPaletteDescription` recoverable through `BasePaletteRef`, and **MUST NOT** let the derived view become the default meaning of `Tradition`, `TraditionPalette`, or the base palette. |
| `CC‑G5.38`      | **Causal method dispatch declarations.** If method selection involves causal methods, each compared method **MUST** declare `causalMethodUseClassification` as observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only method, and **MUST** carry `causalUseSupportRecordRef` and `causalUseSupportVerdict` when it consumes `C.28` causal-use support rather than treating method dispatch as causal certification. |

