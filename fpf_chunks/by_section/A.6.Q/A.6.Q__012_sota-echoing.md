---
chunk_kind: "child"
pattern_id: "A.6.Q"
pattern_title: "U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
section_id: "A.6.Q:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.Q/A.6.Q__012_sota-echoing.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.6.Q — U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
  - "A.6.Q:11 — SoTA-Echoing"
line_start: 13498
line_end: 13540
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.17.0"
  - "E.17.2"
  - "F.9"
  - "F.9.1"
keywords:
  - "bridge reading"
  - "endpoint classification"
  - "evaluative ascription"
  - "language-state seam"
  - "quality senses"
  - "quality-term precision restoration"
---

### A.6.Q:11 - SoTA-Echoing

**Evidence binding note.** If your Context maintains a **SoTA Synthesis Pack** for evaluative language, architecture-quality vocabularies, selector/objective semantics, world-model evaluation, or embodied/preconceptual articulation, this section **SHALL cite** its ClaimSheet IDs / CorpusLedger entries / BridgeMatrix rows and keep the adoption stances below consistent with those IDs. Otherwise, treat the table below as the seed source set for this pattern revision.

This section follows the required structure: **claim > practice > source > alignment > adoption status**. A.6.Q aligns with contemporary practice across architecture-description standards, software-quality standards, evolutionary architecture, QD search, active inference/world-model research, phenomenology/TAE, affordance theory, and philosophy of explanation—while making one explicit FPF move that those traditions usually leave implicit: the overloaded token *quality* is repaired into explicit evaluative endpoint forms, with `evaluativeAscription(...)` available as a declared transitional record carrying `QualitySense`, bearer, frame, admissible normal form, and bridge stance while routing remains open.

| Claim (A.6.Q need) | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with A.6.Q | Adoption status |
|---|---|---|---|---|
| Description-side quality must not be confused with system-side quality. | Contemporary architecture-description practice distinguishes the **entity of interest** from the **architecture description** and structures discourse through viewpoints, concerns, and model kinds. | ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*. | A.6.Q mirrors this split by separating `QS.ArchitecturalDescriptionFitness` from system-side `QS.EngineeringQualityFamily`, and by requiring an explicit bearer lane plus `referencePlane` when phrases such as *architecture quality* appear. | **Adopt/Adapt.** Adopt the entity-vs-description split; adapt by making lexical repair and bearer-lane publication mandatory. |
| Engineering “quality” should resolve to explicit heads, not free adjectives. | Contemporary systems/software quality practice works through named **characteristics** and **subcharacteristics** used to specify, measure, and evaluate quality, and to define acceptance criteria and requirements. | ISO/IEC 25010:2023, *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. | A.6.Q adopts the explicit-head discipline by routing engineering uses either to one admissible `Characteristic` or to one explicit `Bundle` / `Q-Bundle`, and by refusing to leave *quality requirement(s)* as bare noun phrases. | **Adopt/Adapt.** Adopt explicit quality heads; adapt by treating composite families as bundles rather than pretending that every family label is already a scalar. |
| Evolutionary architecture needs continuously checked heads rather than generic “quality”. | Evolutionary-architecture practice uses **fitness functions** to drive, manage, and automate change across architectural concerns, and ties structure to the capacity to support change. | Ford, Parsons, Kua, Sadalage (2022), *Building Evolutionary Architectures*, 2nd ed. | A.6.Q aligns by treating engineering quality families and change-support concerns as explicit evaluative heads under declared frames, not as one rhetorical “high quality” scalar. | **Adopt/Adapt.** Adopt the fitness-function discipline; adapt by keeping `QS.EngineeringQualityFamily`, `QS.ControlAdequacy`, and `QS.UseValue` distinct and by forbidding function/quality-family collapse. |
| In QD / NQD / selector settings, “quality” is an objective head under a declared search frame. | Modern QD work is explicit that search returns a **collection** of solutions that are high with respect to an objective and diverse with respect to declared measures / behavior descriptors; the archive is not a synonym for one hidden global score. | Fontaine, Togelius, Nikolaidis, Hoover (2020), *Covariance matrix adaptation for the rapid illumination of behavior space*; Fontaine & Nikolaidis (2023), *Covariance Matrix Adaptation MAP-Annealing*. | A.6.Q therefore defaults selector-context *quality* to `QS.UseValue` in `Objective` form, while keeping novelty/diversity/constraints explicit and separate. | **Adopt/Adapt.** Adopt objective-explicit selector semantics; adapt by making the Q-head a named `QualitySense` and by rejecting unexplained scalar collapse. |
| Latent fit, world-model adequacy, and closed-loop control must not collapse into one phrase. | Contemporary world-model and active-inference work evaluates generative/predictive models, planning, action, uncertainty reduction, and intrinsic objectives through explicit factor sets rather than through one undifferentiated “model quality”. | Parr, Pezzulo, Friston (2022), *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*; LeCun (2022), *A Path Towards Autonomous Machine Intelligence*; Friston et al. (2024), *Designing Ecosystems of Intelligence from First Principles*. | A.6.Q adapts this by separating `QS.LatentFit`, `QS.ControlAdequacy`, and `QS.UseValue`, and by requiring explicit evaluation frames and witnesses for each ascription. | **Adapt.** Adapt multi-factor evaluation into one repair discipline; reject the colloquial habit of letting *model quality* silently cover representation, prediction, control, and utility at once. |
| Preconceptual felt fit should remain pre-metric until admissibly articulated. | TAE-style practice treats felt aspects of thinking as something that can be clarified progressively with tentative language that stays responsive to lived experience and widens conceptual structure. | Schoeller (2022), work on Thinking at the Edge and embodied critical thinking. | A.6.Q uses this as direct support for `QS.PreconceptualFit` in `SignalPack` form, with exemplars, articulation notes, and an explicit ban on premature promotion to `Characteristic`. | **Adopt/Adapt.** Adopt progressive articulation from felt sense to wording; adapt by giving that articulation an admissible publication form and explicit witness discipline. |
| Some trigger uses of “quality” are really about action invitation, not evaluative ascription. | Recent affordance work treats affordances as perceptually available action possibilities, and in some accounts as invitations or action-guiding structures that position the agent to act. | Hansen (2024), *Perceiving affordances and the problem of visually indiscernible kinds*; Jorba & Lopez-Silva (2024), *Mind in action: expanding the concept of affordance*. | A.6.Q adopts this as an explicit carve-out: when the trigger use is primarily action-invitation talk, the admissible move is to `changeRelationKind(...)` out of `evaluativeAscription` rather than forcing an evaluative reading. | **Adopt/Adapt.** Adopt the action-guiding insight; adapt by making relation-family exit explicit and auditable. |
| Explanation quality is an epistemic merit family, not engineering quality or selector utility. | Contemporary philosophy of explanation treats understanding, explanatory value, and the cognitive significance of explanations as a distinct epistemic topic. | Khalifa (2017), *Understanding, Explanation, and Scientific Knowledge*. | A.6.Q therefore treats explanatory evaluation as `QS.ExplanatoryMerit`, typically `Bundle`-shaped, and rejects silent collapse into engineering `-ilities`, bare usefulness, or one unexplained “high-quality explanation” score. | **Adapt.** Adapt explanatory-value practice into a slot-explicit evaluative family; reject cross-family scalarization by label. |

**Short alignment notes.**

**Architecture-description practice.** ISO 42010 is the clearest contemporary guard against collapsing the described entity into its description. A.6.Q adopts that guardrail and adds lexical discipline: a draft may not say *architecture quality* without publishing which bearer lane is under evaluation and whether the evaluation is description-side or system-side.

**Engineering quality practice.** ISO 25010 gives a mainstream reason not to leave *quality* as a free noun: contemporary quality work is organized around named characteristics and subcharacteristics that are specified, measured, and evaluated. A.6.Q adopts that explicit-head discipline, but adapts it by routing composite cases to `Bundle` / `Q-Bundle` and by treating *quality requirement(s)* as requirements over explicit heads rather than as self-standing nouns.

**Evolutionary-architecture practice.** Fitness functions treat architecture-relevant concerns as continuously monitored heads tied to change and governance, not as one mystical scalar. A.6.Q adopts that operational spirit, but adapts it by keeping engineering-family evaluation, control adequacy, and selector value distinct and by forbidding function/quality-family collapse.

**QD / NQD practice.** Modern QD work is explicit that search returns a collection of solutions that are high with respect to an objective and diverse with respect to declared measures. A.6.Q therefore adopts the default rewrite of selector-context *quality* to `QS.UseValue` in `Objective` form and rejects any rewrite that silently blends novelty, diversity, constraints, and utility into an unexplained scalar.

**World-model and active-inference practice.** Contemporary world-model and active-inference work uses generative/predictive models for perception, planning, learning, and action, which makes evaluation inherently multi-factor: latent representation quality, model evidence or predictive adequacy, policy adequacy, and task/objective value are not one thing. A.6.Q adapts this by separating `QS.LatentFit`, `QS.ControlAdequacy`, and `QS.UseValue`, and by requiring explicit evaluation frames and witnesses for each ascription.

**Phenomenology / TAE practice.** TAE-style work treats a felt sense as something that can be clarified and worded progressively, with tentative language that stays responsive to lived experience. A.6.Q adopts this progressive-articulation stance by giving `QS.PreconceptualFit` an admissible `SignalPack` form and by keeping `QS.PhenomenalCharacter` separately available when the experienced character itself—not action-guiding fit—is the topic.

**Action-invitation boundary.** Recent affordance work emphasizes that affordances can be perceptually experienced as action possibilities that position or invite the agent to act. A.6.Q adopts that insight as a relation-family boundary: when the trigger use of *quality* is really action-invitation talk, the author should `changeRelationKind(...)` out of `evaluativeAscription` rather than forcing an evaluative reading.

**Explanation practice.** Contemporary philosophy of explanation keeps explanatory understanding and epistemic value distinct from engineering performance or utility maximization. A.6.Q adapts this by publishing `QS.ExplanatoryMerit` as its own evaluative family—typically `Bundle`-shaped—and by rejecting hidden scalarization into “high-quality explanation” without explicit heads.

**Scale legality.** The rows above do **not** license free arithmetic on the word *quality*. Whenever A.6.Q operationalizes engineering heads, selector objectives, or control adequacy numerically, it **SHALL** bind the comparison to an explicit `ComparatorSet` / `CG-Spec` / declared aggregation policy and **SHALL** reject covert scalarization of bundles, explanations, or preconceptual signals.

**Cross-Context / plane note.** This section states alignment and non-identity only; it does **not** assert silent sameness across `U.BoundedContext`s or across planes. Any actual reuse of a quality vocabulary, selector head, or viewpoint-bound quality family across Contexts/planes **SHALL** publish `BridgeId` + `CL` / loss-note policy and, where planes differ, the relevant `Φ(CL)` / `Φ_plane` policy-ids.

**Historical-lineage note.** Earlier touchstones such as Pirsig, Popper, and Deutsch remain useful as lineage and local-gloss resources, but A.6.Q does not use them as the formal SoTA anchors here because E.8 requires post-2015 primary sources for Architectural patterns.

This SoTA alignment supports the pattern’s central move: *quality* is not one universal evaluative noun. In contemporary practice, the relevant work is already distributed across explicit characteristics, objectives, viewpoints, world-model criteria, explanatory virtues, felt signals, and action invitations; A.6.Q makes that distribution first-class and auditable.

