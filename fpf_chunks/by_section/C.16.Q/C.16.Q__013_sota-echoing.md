---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__013_sota-echoing.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:11 — SoTA-Echoing"
line_start: 41926
line_end: 41970
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.16.P"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### C.16.Q:11 - SoTA-Echoing

**Evidence binding note.** If your Context maintains a **SoTA Synthesis Pack** for evaluative language, architecture-quality vocabularies, selector and objective semantics, world-model evaluation, or embodied and preconceptual articulation, this section **SHALL cite** its ClaimSheet IDs, CorpusLedger entries, and BridgeMatrix rows and keep the adoption statuses below consistent with those IDs. Otherwise, use the table below as the current source-use and source-currentness record for this pattern revision, not as a generic seed list.

This section follows the required structure: **claim > practice > source use and currentness > source > alignment > adoption status**. C.16.Q aligns with contemporary practice across architecture-description standards, software-quality standards, evolutionary architecture, QD search, active-inference and world-model research, phenomenology and TAE, source-tradition `affordance` work, and philosophy of explanation, while making one explicit FPF move that those traditions usually leave implicit: the overloaded token *quality* is repaired into explicit evaluative endpoint forms, with `qualityTermAscription(...)` available as a declared transitional record carrying `QualitySense`, bearer, frame, admissible normal form, and bridge disposition while governing-pattern assignment remains open.

**Source-use convention.** `Current-best source use` means the row is used as the best-known current line for the narrow effect named in the alignment cell. `Current-standard and reference-only use` means an official standard supplies a useful distinction but does not by itself solve C.16.Q's quality-term restoration question. `Current-practice reference use` means the source family records a widely used current practice that C.16.Q adapts. `Lineage and local-gloss material` means the row helps recognition or terminology only. `Rejected import` states what C.16.Q refuses to import as FPF ontology.

| Claim (C.16.Q need) | SoTA practice (post-2015) | Source use and currentness | Primary source (post-2015 unless marked lineage) | Alignment with C.16.Q | Adoption status |
|---|---|---|---|---|---|
| Description-side quality must not be confused with system-side quality. | Contemporary architecture-description practice distinguishes the **system or entity that fills the architecture-description `EntityOfConcern`** from the **architecture description** and structures discourse through viewpoints, concerns, and model kinds. | **Current-standard and reference-only use.** The standard is a current architecture-description reference for entity, description, and viewpoint separation; it is not treated as a full quality-term repair method. | ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description*. | C.16.Q mirrors this split by separating `QS.ArchitecturalDescriptionFitness` from system-side `QS.EngineeringQualityFamily`, and by requiring an explicit bearer lane plus `referencePlane` when phrases such as *architecture quality* appear. | **Adopt and adapt.** Adopt the EntityOfConcern-vs-description split; adapt by making lexical repair and bearer-lane publication mandatory. Reject importing the standard's conceptual model as FPF ontology. |
| Engineering “quality” should resolve to explicit heads, not free adjectives. | Contemporary systems/software quality practice works through named **characteristics** and **subcharacteristics** used to specify, measure, and evaluate quality, and to define acceptance criteria and requirements. | **Current-standard and reference-only use.** The standard supplies a current quality-model reference for explicit heads; C.16.Q still requires FPF `U.Characteristic`, `Q-Bundle`, objective, or exact endpoint governance. | ISO/IEC 25010:2023, *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Product quality model*. | C.16.Q adopts the explicit-head discipline by assigning engineering uses either to one admissible `Characteristic` or to one explicit `Bundle` or `Q-Bundle`, and by refusing to leave *quality requirement(s)* as bare noun phrases. | **Adopt and adapt.** Adopt explicit quality heads; adapt by treating composite families as bundles rather than pretending that every family label is already a scalar. Reject ISO characteristic lists as automatically sufficient FPF evaluation spaces. |
| Evolutionary architecture needs continuously checked heads rather than generic “quality”. | Evolutionary-architecture practice uses **fitness functions** to drive, manage, and automate change across architectural concerns, and ties structure to the capacity for change. | **Current-practice reference use.** The row records concern-specific fitness heads, not a universal definition of quality. | Ford, Parsons, Kua, Sadalage (2022), *Building Evolutionary Architectures*, 2nd ed. | C.16.Q aligns by treating engineering quality families and change-enabling concerns as explicit evaluative heads under declared frames, not as one rhetorical “high quality” scalar. | **Adopt and adapt.** Adopt the fitness-function discipline; adapt by keeping `QS.EngineeringQualityFamily`, `QS.ControlAdequacy`, and `QS.UseValue` distinct and by forbidding function and quality-family collapse. |
| In QD, NQD, or selector settings, “quality” is an objective head under a declared search frame. | Modern QD work is explicit that search returns a **collection** of solutions that are high with respect to an objective and diverse with respect to declared measures and behavior descriptors; the archive is not a synonym for one hidden global score. | **Current-best source use for selector-quality semantics in this pattern revision.** The row governs the `QS.UseValue` default, objective form, and scalar-collapse boundary; it does not define all QD and NQD practice. | Fontaine, Togelius, Nikolaidis, Hoover (2020), *Covariance matrix adaptation for the rapid illumination of behavior space*; Fontaine & Nikolaidis (2023), *Covariance Matrix Adaptation MAP-Annealing*. | C.16.Q therefore defaults selector-context *quality* to `QS.UseValue` in `Objective` form, while keeping novelty, diversity, and constraints explicit and separate. | **Adopt and adapt.** Adopt objective-explicit selector semantics; adapt by making the Q-head a named `QualitySense` and by rejecting unexplained scalar collapse. |
| Latent fit, world-model adequacy, and closed-loop control must not collapse into one phrase. | Contemporary world-model and active-inference work evaluates generative and predictive models, planning, action, uncertainty reduction, and intrinsic objectives through explicit factor sets rather than through one undifferentiated “model quality”. | **Current research and practice source use.** The row is used for multi-factor separation of latent, control, and value claims; it is not imported as an active-inference ontology for FPF. | Parr, Pezzulo, Friston (2022), *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*; LeCun (2022), *A Path Towards Autonomous Machine Intelligence*; Friston et al. (2024), *Designing Ecosystems of Intelligence from First Principles*. | C.16.Q adapts this by separating `QS.LatentFit`, `QS.ControlAdequacy`, and `QS.UseValue`, and by requiring explicit evaluation frames and witnesses for each ascription. | **Adapt.** Adapt multi-factor evaluation into one repair discipline; reject the colloquial habit of letting *model quality* silently cover representation, prediction, control, and utility at once. |
| Preconceptual felt fit should remain pre-metric until admissibly articulated. | TAE-style practice treats felt aspects of thinking as something that can be clarified progressively with tentative language that stays responsive to lived experience and widens conceptual structure. | **Current-practice reference use with lineage use.** The row is used for progressive articulation and the `SignalPack` boundary; it is not current-best source use for metric construction. | Schoeller (2022), work on Thinking at the Edge and embodied critical thinking. | C.16.Q uses this as a practice reason for `QS.PreconceptualFit` in `SignalPack` form, with exemplars, articulation notes, and an explicit ban on premature promotion to `Characteristic`. | **Adopt and adapt.** Adopt progressive articulation from felt sense to wording; adapt by giving that articulation an admissible publication form and explicit witness discipline. |
| Some trigger uses of “quality” are really about action invitation, not evaluative characterization. | Recent source-tradition `affordance` work treats affordances as perceptually available action possibilities, and in some accounts as invitations or action-guiding structures that position the agent to act. | **Current research cue and boundary cue.** The row is used only to recognize action-invitation cases and send them to `A.6.A` or another exact action-invitation governing pattern. | Hansen (2024), *Perceiving affordances and the problem of visually indiscernible kinds*; Jorba & Lopez-Silva (2024), *Mind in action: expanding the concept of affordance*. | C.16.Q uses this only as an action-invitation cue: when the trigger use is primarily action-invitation talk, the admissible FPF move is to use `exitToReceivingPattern(...)` into `A.6.A` or another exact action-invitation governing pattern rather than forcing a `QualitySense` or `qualityTermAscription(...)`. | **Adopt and adapt.** Adopt the action-guiding insight; adapt by making the exact FPF governing-pattern exit explicit and auditable. Reject importing `affordance` as a quality sense or FPF governing-pattern name. |
| Explanation quality is an epistemic merit family, not engineering quality or selector utility. | Contemporary philosophy of explanation treats understanding, explanatory value, and the cognitive significance of explanations as a distinct epistemic topic. | **Lineage and reference source use for a local evaluative family.** The row is used for the `QS.ExplanatoryMerit` distinction and anti-scalarization boundary; it is not presented as current-best source use for all explanation evaluation. | Khalifa (2017), *Understanding, Explanation, and Scientific Knowledge*. | C.16.Q therefore treats explanatory evaluation as `QS.ExplanatoryMerit`, typically `Bundle`-shaped, and rejects silent collapse into engineering `-ilities`, bare usefulness, or one unexplained “high-quality explanation” score. | **Adapt.** Adapt explanatory-value practice into a slot-explicit evaluative family; reject cross-family scalarization by label. |

**Short alignment notes.**

**Architecture-description practice.** ISO 42010 is a current-standard reference for not collapsing the selected system or other entity under description into its description. C.16.Q adopts that guardrail and adds lexical discipline: a draft may not say *architecture quality* without publishing which bearer lane is under evaluation and whether the evaluation is description-side or system-side.

**Engineering quality practice.** ISO 25010 gives a mainstream current-standard reason not to leave *quality* as a free noun: contemporary quality work is organized around named characteristics and subcharacteristics that are specified, measured, and evaluated. C.16.Q adopts that explicit-head discipline, but adapts it by assigning composite cases to `Bundle` or `Q-Bundle` and by treating *quality requirement(s)* as requirements over explicit heads rather than as self-standing nouns.

**Evolutionary-architecture practice.** Fitness functions treat architecture-relevant concerns as continuously monitored heads tied to change and governance, not as one mystical scalar. C.16.Q adopts that operational spirit, but adapts it by keeping engineering-family evaluation, control adequacy, and selector value distinct and by forbidding function and quality-family collapse.

**QD and NQD practice.** Modern QD work is explicit that search returns a collection of solutions that are high with respect to an objective and diverse with respect to declared measures. C.16.Q therefore adopts the default rewrite of selector-context *quality* to `QS.UseValue` in `Objective` form and rejects any rewrite that silently blends novelty, diversity, constraints, and utility into an unexplained scalar.

**World-model and active-inference practice.** Contemporary world-model and active-inference work uses generative and predictive models for perception, planning, learning, and action, which makes evaluation inherently multi-factor: latent representation quality, model evidence or predictive adequacy, policy adequacy, and task and objective value are not one thing. C.16.Q adapts this by separating `QS.LatentFit`, `QS.ControlAdequacy`, and `QS.UseValue`, and by requiring explicit evaluation frames and witnesses for each ascription.

**Phenomenology and TAE practice.** TAE-style work treats a felt sense as something that can be clarified and worded progressively, with tentative language that stays responsive to lived experience. C.16.Q adopts this progressive-articulation stance by giving `QS.PreconceptualFit` an admissible `SignalPack` form and by keeping `QS.PhenomenalCharacter` separately available when the experienced character itself, not action-guiding fit, is the topic.

**Action-invitation boundary.** Recent source-tradition `affordance` work emphasizes that affordances can be perceptually experienced as action possibilities that position or invite the agent to act. C.16.Q uses that insight only as a governing-pattern boundary cue: when the trigger use of *quality* is really action-invitation talk, the text should use `exitToReceivingPattern(...)` into `A.6.A` or another exact action-invitation governing pattern rather than forcing a `QualitySense` or `qualityTermAscription(...)`.

**Explanation practice.** Contemporary philosophy of explanation keeps explanatory understanding and epistemic value distinct from engineering performance or utility maximization. C.16.Q adapts this by publishing `QS.ExplanatoryMerit` as its own evaluative family, typically `Bundle`-shaped, and by rejecting hidden scalarization into “high-quality explanation” without explicit heads.

**Scale legality.** The rows above do **not** license free arithmetic on the word *quality*. Whenever C.16.Q operationalizes engineering heads, selector objectives, or control adequacy numerically, it **SHALL** bind the comparison to an explicit `ComparatorSet`, `CG-Spec`, or declared aggregation policy and **SHALL** reject covert scalarization of bundles, explanations, or preconceptual signals.

**Cross-Context and plane note.** This section states alignment and non-identity only; it does **not** assert silent sameness across `U.BoundedContext`s or across planes. Any actual reuse of a quality vocabulary, selector head, or viewpoint-bound quality family across Contexts and planes **SHALL** publish `BridgeId`, `CL`, and loss-note policy and, where planes differ, the relevant `Φ(CL)` and `Φ_plane` policy ids.

**Historical-lineage note.** Earlier touchstones such as Pirsig, Popper, and Deutsch remain useful as lineage and local-gloss resources, but C.16.Q does not use them as formal SoTA anchors here because E.8 requires post-2015 primary sources for Architectural patterns unless the row is explicitly lineage or local-gloss material.

This SoTA alignment backs the pattern’s central move: *quality* is not one universal evaluative noun. In contemporary practice, the relevant work is already distributed across explicit characteristics, objectives, viewpoints, world-model criteria, explanatory virtues, felt signals, and action invitations; C.16.Q makes that distribution first-class and auditable.

