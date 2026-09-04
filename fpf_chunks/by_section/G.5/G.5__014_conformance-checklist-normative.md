---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__014_conformance-checklist-normative.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:7 — Conformance Checklist (normative)"
line_start: 104084
line_end: 104139
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
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
  - "in core registry and eligibility fields"
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
| `CC‑G5‑CoreRef` | **Core conformance bridge.** `G.5` is conformant only if the **effective** `G.Core` obligations referenced by `G.5:4.1 (GCoreLinkageManifest)` are satisfied (after profile and set expansion plus explicit deltas). |
| `CC‑G5.0`       | Core standards **SHALL** remain notation‑independent; vendor or tool keywords are forbidden in registry, eligibility, assurance, or selector‑kernel obligations (`E.5.*`). |
| `CC‑G5.1`       | Every `MethodFamily` **SHALL** declare an `EligibilityStandardRef` using CHR and CAL terms (typed; edition‑pinned where applicable). Standards **SHALL NOT** rely on tool‑specific keywords.  |
| `CC-G5.2`       | Selection **SHALL** be a pure function of `TaskSignatureRef`, exact method- and generator-family row refs, any conditionally current exact `TaskMapRef`, and pinned policy or edition refs; side effects are limited to emitting DRR and SCR pins, telemetry triggers, and RSCR triggers (no hidden mutation of constraint-bearing spec refs). |
| `CC‑G5.3`       | **Delegated (ID‑continuity) plus F.9 use boundary.** When a selector use relates expressions with distinct F.17 source-local meanings, it **MUST** resolve the exact cells, an obtaining F.9 Bridge, a separate C.2.1 `<u,d,r,t,polarity>` proposition, and the matching A.10 or B.3 reliance branch. G.Core crossing visibility and penalty-assignment semantics still apply. **Delegation targets:** `CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`. Pins alone **MUST NOT** establish the Bridge, use, reliance, or actual selector application. |
| `CC‑G5.4`       | **Default rule for** `DefaultId.GammaFoldForR_eff`. The selector **MUST** default to the weakest‑link rule for `R_eff` and record contributors in SCR; it **MAY** use an alternative Γ‑fold only when provided by an explicitly pinned policy or profile with proof obligations satisfied (monotonicity; boundary behavior). |
| `CC-G5.5`       | Ordinal scales **MUST NOT** be averaged or subtracted; any aggregation or comparison must respect CHR scale typing and admissibility constraints, including CSLC where applicable. |
| `CC‑G5.6`       | Method and generator family identities **SHALL** be published to UTS with the required naming discipline (twin labels where applicable; deprecations follow lexical continuity rules). *(Core conformance applies; `G.5` adds the registry‑specific publication obligation.)* |
| `CC‑G5.7`       | **Conditional.** If `G.5:Ext.EELog` is present, exploration **MUST** be budgeted under the pinned exploration and exploitation log policy; probe outcomes **MUST** feed refresh through canonical RSCR trigger kinds. |
| `CC‑G5.8`       | **CG‑Frame gate enforced.** Selection rejects or abstains from candidates that do not meet the pinned `CG‑Spec.MinimalEvidence` requirements for the characteristics they cite. |
| `CC-G5.9`       | **Delegated (ID-continuity).** Set-return semantics are pinned through `G.Core`. **Delegation target:** `CC-GCORE-SET-1`. Candidate ordering **MUST** be admissible over typed traits and admissibility constraints. If only a partial order is available, selection **MUST** return one declared selector outcome, for example one `SetResultOutcome` with `Shortlist` or `RankedShortlist`, one `HandoffOutcome` with `SpecialistHandoff`, or another pinned outcome result, with no forced totalisation via inadmissible scalarisation. |
| `CC-G5.10`      | **SCR completeness.** SCR **MUST** enumerate Gamma-fold contributors when used, referenced constraint-bearing spec editions, the evidence citations (`PathId` and `PathSliceId`) used in gating and rationale, and `MinimalEvidence` gating verdicts by lane and carrier when such gating is relied upon. |
| `CC‑G5.11`      | **Delegated (ID‑continuity).** Tri‑state eligibility and acceptance semantics plus unknown handling are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑GUARD‑1`. *(Includes the rule that `degrade(...)` is expressed through a pinned FailureBehavior or SoS‑LOG branch id, not as a fourth status.)* |
| `CC-G5.12`      | **Applicability of a selected method set.** A selected method-set result **MUST** state the exact task, exact row refs or other exact members, grouping and selection basis, truthful outcome kind, ordering, selection or inclusion conditions, and the named next use. Add `ClaimScope`, selected A.2.6 slices, a validity or evaluation window, source or scheme editions, intended-use restrictions, counterexamples, evidence pins, and transfer or change conditions only when they change eligibility, selection, applicability, or a receiver's justified reliance. Omitting any such action-changing value fails this check and reopens the affected result; values that change no current action stay out. Coverage, descriptors, and distance may guide a named search for omissions but **MUST NOT** establish broader applicability. Apply `E.24.UK` or `A.8` only to a separate claim about a durable kind or kernel placement; neither claim widens the selected set's applicability. |
| `CC‑G5.13`      | **Conditional.** If the selector consumes admissibility or maturity records (e.g., through `G.5:Ext.SoSLOG`), it **MUST NOT** recompute thresholds; it consumes pinned admissibility ledger rows and cites clause and rung ids in audit pins. |
| `CC‑G5.14`      | **Φ(CL) and Φ_plane discipline.** If crossing or plane penalties are applied, the active penalty policy ids (e.g., `Φ(CL)`, `Φ_plane`) **MUST** be explicit in audit pins, and the pinned policies **MUST** satisfy the monotone and bounded requirements asserted by their cited constraint-bearing spec refs and be published through those same cited spec refs (e.g., `CG‑Spec`). SCR **MUST** record the policy id in use; penalty assignment semantics remain pinned through `G.Core`. |
| `CC-G5.15`      | Unit and scale admissibility **MUST** be established via CSLC (A.18) before any aggregation or Gamma-fold; unit and scale mismatches are a fail-fast defect. |
| `CC‑G5.16`      | Hidden thresholds are forbidden. Thresholds live in explicitly pinned acceptance or eligibility policy records, not in selector prose, LOG shells, or code.  |
| `CC‑G5.17`      | ReferencePlane **MUST** be declared (pinned) for any claim that is used in dispatch, and the selector’s audit records must cite it (including plane‑crossing pins when applicable). |
| `CC-G5.18`      | Numeric comparisons and aggregations used by dispatch **MUST** cite an admissible, edition-pinned comparator or spec publication (as provided by the constraint-bearing spec refs); inadmissible mixes of scale types are forbidden. |
| `CC-G5.19`      | **Conditional (QD).** If `G.5:Ext.NQD` is present, the required QD telemetry triple (quality, diversity, and QD summary) **MUST** be computable and ready for emission under the pinned descriptor and distance definitions and archive policy, without redefining their semantics in G.5. If actual publication is current, use E.17 for a source-backed face and return to source and E.24.PUB for the publication occurrence and audience availability. |
| `CC‑G5.20`      | **Conditional (QD).** QD and illumination summaries are treated as telemetry unless explicitly promoted by a pinned acceptance or policy record; the selector must record the promoting policy id in audit pins. |
| `CC-G5.21`      | **Conditional (Archive and QD).** Any use of archives **MUST** declare `InsertionPolicyRef` and pin the required editions for reproducibility, including descriptor and distance definitions and any method editions they depend on. |
| `CC‑G5.22`      | **Conditional (QD).** Twin‑naming discipline for descriptor vs plain space (if used) must be respected (distinct objects; no aliasing).  |
| `CC-G5.23`      | **Default rule for** `DefaultId.PortfolioMode`. The selector **MUST** expose `PortfolioMode` with values `Pareto` or `Archive`, with **default = `Archive`**, and echo it in DRR and SCR records and declared selector results when not explicitly overridden by pinned policy or TaskSignature. The default is a retention and evidence-preservation policy, not a public selected-set label, not a dominance default, and not a substitute for `SetResultFamily`. Epsilon-fronts are allowed as *local* decision aids under `CG-Spec` when explicitly pinned. |
| `CC-G5.23a`     | **Parity-run publication.** If parity harness is in use, a selector or generator **MUST** publish a parity run and `ParityCard` to **UTS** (see `G.9`). This obligation remains mandatory irrespective of dominance policy or `PortfolioMode` policy. |
| `CC‑G5.24`      | **Conditional (Open‑Ended).** If `G.5:Ext.OpenEndedFamilyWiring` is present, the selector **MUST** return declared sets of `{Environment, MethodFamily}` pairs as set‑valued outcomes under explicit pins. |
| `CC‑G5.25`      | **Conditional (Open‑Ended).** In Open‑Ended mode, `TransferRulesRef.edition` is mandatory and **MUST** be visible to telemetry and RSCR triggers.  |
| `CC-G5.26`      | **Conditional (Archive and QD).** Within any archive niche or cell, ordering and tie-breaks **MUST** remain admissible over compatible scales; inadmissible mixed-scale weighted sums are forbidden. |
| `CC‑G5.27`      | If the selector cites any `GateCrossing`, the corresponding `CrossingBundle` publication **MUST** be present and conformant; missing or non‑conformant `CrossingBundle` blocks downstream consumption. The bundle packages already governed crossing evidence for that named use; it **MUST NOT** create the F.17 endpoints, F.9 Bridge, bounded-use proposition, A.10/B.3 reliance, gate decision, authorization, or actual selector use. |
| `CC‑G5.28`      | **Default rule for** `DefaultId.DominanceRegime`. `DominanceRegime` **SHALL** default to `ParetoOnly`. Any inclusion of additional telemetry dimensions into dominance (e.g., illumination) requires an explicitly pinned acceptance or policy record and must be recorded in audit pins. **Parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy. |
| `CC-G5.29`      | **Conditional (QD and Open-Ended).** Any telemetry event that materially changes an archive state or retained-set state **MUST** log `PathSliceId`, the active policy id, and the active editions of the relevant definition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `TransferRulesRef.edition` when applicable) and expose them to RSCR triggers. |
| `CC‑G5.30`      | **No Strategy minting.** Within `G.5`, “strategy” is a policy‑bound composition template; the pattern **SHALL NOT** mint a durable U-kind named `Strategy` (E.10 and E.24.UK discipline). If a stable reference is needed, publish composition and policy ids (e.g., UTS entries) rather than minting a universal kind. |
| `CC-G5.31`      | **Strategy hint on non-admissible sets.** If selection yields `CandidateSet = EMPTY`, the selector **SHALL** emit an explicit escalation hint (`ActionHint`) that is compatible with DRR and SCR records and auditable: include at minimum the top three blocking constraints as cited ids and pins, and where applicable include the relevant edition pins, for example `TransferRulesRef.edition` in Open-Ended mode, to guide exploration under explicitly pinned lenses such as the exploration and exploitation log policy. |
| `CC‑G5.32`      | **Parity‑run publication and admissible roll-ups.** If parity harness is in use, parity publication is required per `CC‑G5.23a` (ID‑continuity). Any scalar roll-up or summary view **MUST** be admissible under **CG‑Spec** (no mixed‑scale sums), and published views must preserve set‑return semantics (no single‑score leaderboards as authoritative outputs without an explicit, admissible comparator publication). |
| `CC‑G5.33`      | **Conditional (bounded specialization).** When the selection question is acquisition of usable specialization on a declared `TaskFamilyRef` or `TaskSignature`, selector outputs **SHALL** either emit `TaskFamilySpecializationProfile@Context` or cite equivalent pins carrying the `C.22.1` adaptation-signature fields needed for comparison: work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, and any declared transfer, retention, downside, or specialization-entry notes. |
| `CC‑G5.34`      | **Selected-set result kind.** When `SelectorOutcomeKind = SetResultOutcome`, the public result kind **MUST** be explicit. Use `Shortlist` for unordered alternatives retained for later choice, `RankedShortlist` only when the result orders those alternatives, and `JointUseSet` only when every named member is included for one named use. `ChoiceSet` **MUST NOT** silently replace the public result kind. |
| `CC‑G5.34a`     | **Selector outcome typing.** Declared selector results **MUST** state `SelectorOutcomeKind`. `SetResultFamily` is required only when `SelectorOutcomeKind = SetResultOutcome`; `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`. Non-set outcomes **MUST NOT** masquerade as one public selected-set label. |
| `CC‑G5.35`      | **Result-content closure.** Any declared selector result **MUST** state the `SelectorOutcomeKind`, applicable public result kind, retained members or keyed joint-use entries, ordering, named use and inclusion conditions when required, and basis pins directly in the emitted result rather than relying on upstream `C.11`, `C.19`, or `C.24` notes. |
| `CC‑G5.36`      | **Neighboring-pattern boundary.** If the current question is still local choice among already-available options, pool policy over still-live candidate lines, or enactment planning after choice, a `G.5` use **MUST** consume the result produced by applying `C.11`, `C.19`, or `C.24` rather than restating those patterns as if declaring selector-facing content decided the upstream matter. |
| `CC‑G5.37`      | **Derived tradition-view result discipline.** If the selector emits one result through a derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep the declared base `SourceSetFamily` explicit, keep `SoTAPaletteDescription` recoverable through `BasePaletteRef`, and **MUST NOT** let the derived view become the default meaning of `Tradition`, `TraditionPalette`, or the base palette. |
| `CC‑G5.38`      | **Causal method dispatch declarations.** If method selection involves causal methods, each compared method **MUST** declare `causalMethodUseClassification` as observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only method, and **MUST** carry `causalUseSupportResultRef` and the cited result's verdict when it consumes `C.28` causal-use support rather than treating method dispatch as causal certification. |
| `CC-G5.39`      | **Registry grounding, edition, and grouping boundary.** Every consumed method-family row **MUST** be addressed by one exact `MethodFamilyRowRef` whose immutable edition resolves its non-empty `MethodRef[]` to exact A.3.1 Methods; every consumed generator-family row **MUST** use one exact `GeneratorFamilyRowRef` and resolve non-empty exact generator refs under their subject patterns. Each row edition cites the independently established classification, membership relation, or explicit project-local grouping criterion used by this selector. A row, id, label, description, family card, eligibility or maturity record, policy, evidence pin, shortlist, or publication **MUST NOT** create a member or membership fact. Missing grounding or an unresolved row edition blocks that row's family use. |
| `CC-G5.40`      | **Composition and selected-structure boundary.** A composition shape **MUST** remain a template unless one already identified A.3.1 Method separately passes B.1.5's complete composite-method qualification. An organization that does not constitute one Method **MUST** be consumed as an A.22 `U.Structure` only after all four A.22 identity discriminators are present. A template, A.3.2 description, registry row, selector outcome, diagram, label, or notation **MUST NOT** create either governed object or its underlying relations. |
| `CC-G5.41`      | **Declaration, actuality, performer, result and publication boundary.** A registry, selector, policy, template, shortlist, DRR, SCR, telemetry or publication-content declaration **MUST NOT** be treated as an A.13 performer core, dated Work, F.6 attribution, actual A.6.1 `Select` application or binding, domain-result truth, C.2.1 result episteme, A.10 evidence relation, B.3 assurance claim, authorization, or E.24.PUB publication occurrence. Every claimed precise performer **MUST** first have the A.13 core; A.15.1 **MUST** admit the Work independently; F.6 enters only for a current exact assignment-bound attribution through the same obtaining assignment. Every other claimed actual object or relation **MUST** be recovered under its subject pattern; missing actuality blocks only that stronger claim. |
| `CC-G5.42`      | **Crossing completeness.** A selector use that relates expressions with distinct source-local meanings **MUST NOT** proceed from Bridge, CL, loss, registry, policy, `CrossingAllowance`, `GateCrossing`, `CrossingBundle`, DRR, or SCR pins alone. It requires exact F.17 endpoint senses, an obtaining F.9 Bridge, a separate C.2.1 bounded-use proposition, and the matching A.10 reliance disposition or B.3 assurance branch; authorization and the actual selector application remain separate. |
| `CC-G5.43`      | **Ordinary-use proportionality.** A bounded selector run over already grounded rows **MUST** be usable from the exact task, immutable row-edition refs, Methods and grouping bases, declared eligibility or comparison basis, truthful outcome, members, ordering status, basis refs and next use. It **MUST NOT** demand a fresh registry build, crossing branch, A.10 reliance claim, B.3 assurance claim, stable public identity, or E.24.PUB occurrence unless that stronger object or claim is current. Missing conditional apparatus blocks only the stronger claim. |
| `CC-G5.44`      | **Joint-use membership integrity.** A declared selector-result record with `SetResultFamily = JointUseSet` **MUST** name one bounded use, set `ordering = unordered`, and use keyed `memberEntries` with each exact `memberRef` present at most once. Entry order has no semantic effect; the result **MUST NOT** add an undefined per-member contribution or basis field; and any top-level `members` **MUST** be only the unique set projection of the entry keys, never an independently maintained list. Exact supporting content or claims remain in their own records and may be cited only among sufficient top-level `basisPins`. |
| `CC-G5.45`      | **Joint-use ontic and actuality boundary.** A declared selector-result record with `SetResultFamily = JointUseSet` is well formed only if every exact framework-edition or other non-Method `memberRef` resolves under its existing identity and the record adds no `MethodRef` value or registry row merely for membership. Candidate-pool and excluded-candidate records, direct member relations, local choice, actual selection Work, publication availability, and access remain separate. |
| `CC-G5.46`      | **Operation-path integrity.** A `JointUseSet` over non-Method members **MUST** be emitted through `G.5-6 DeclareSetResult` from exact already identified `memberRef` values and a current inclusion basis; it **MUST NOT** use `RegisterFamily` or `G.5-3 Select`. `DeclareSetResult` **MUST NOT** be treated as the upstream choice, an actual `Select` application, dated Work, persisted result episteme, or E.24.PUB availability occurrence. |
| `CC-G5.47`      | **G.4 TaskMap receiving boundary.** `TaskMapRef` is required only when this selector uses G.4 CAL gates. Its immutable map edition **MUST** cite the same C.22 `TaskSignatureRef` supplied to selection, resolve one exact `CALCharterRef` and every cited clause, operator, flow, and evidence profile at its exact edition, and travel in result-basis and refresh pins. A mismatch or unresolved ref blocks that gated use. The map **MUST NOT** construct the TaskSignature, copy thresholds, duplicate acceptance semantics, or become mandatory for an ordinary selector with no G.4 gate. |

