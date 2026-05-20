- If one generator speaks about selected results, keep that language in the shortlist family rather than silently reusing front language.
- Prefer wording like `front over the declared DominanceSet, plus the corresponding ExplorationArchive when archive mode is active` over wording that folds `Q`, novelty, and diversity into one default front by habit.
- The local generation story should stay consistent with the declared `Front`, `Archive`, and `Shortlist` language so comparison stays intelligible and lawful.

### B.5.2.1:6 - Conformance Checklist (normative)

**CC‑B.5.2.1‑1 (CHR discipline).** If this pattern is applied in a Context, that Context **SHALL** declare the Creativity‑CHR **Characteristics** with **A.18**‑style templates (type, unit/range, polarity). No new kernel terms are introduced.
**CC‑B.5.2.1‑2 (Instrumented generation).** Step 2 of **B.5.2** **SHALL** either (a) invoke *NQD‑Generate* or (b) justify a Context‑specific generator of equivalent effect (diversity + quality + novelty with measurable **Characteristics**).
**CC‑B.5.2.1‑3 (Diversity coupling).** When this pattern is applied, **D MUST be ΔDiversity_P** computed against the current candidate Pool using the **C.17** definition of **Diversity_P** under the same Context, CharacteristicSpace, kernel, and TimeWindow.
**CC‑B.5.2.1‑Eligibility**: Eligibility requires **(i)** `ConstraintFit = pass` for the candidate (Norm‑CAL must‑set), **then (ii)** **USM** coverage for the TargetSlice and **(iii)** an enactable **RSG** state for the performer; only then may calls to `Γ_nqd.*` occur.
**CC‑B.5.2.1‑4 (Non‑dominated candidate front).** The *CandidateSet* **MUST** include the **Pareto front** over the declared `DominanceSet`. If the Context consumes the ordinary default, cite that consumed `DefaultId.DominanceRegime` rather than restating one local default doctrine. Any pruned candidate **MUST** carry a DRR note (“dominated by … on {Characteristics}”). `N`, `D=ΔDiversity_P`, `Surprise`, `IlluminationSummary`, and similar signals enter dominance only under an explicit recorded promotion policy; otherwise they remain archive, tie-break, or telemetry signals.
**CC‑B.5.2.1‑4a (Archive companion when retained exploration is in scope).** If the active policy depends on retained exploration, stepping-stone retention, or open-ended search, the emitted candidate package **MUST** include the corresponding `ExplorationArchive` or cite one explicit policy id that says archive mode is disabled for that run.
**CC‑B5.2.1‑5 (Abductive primacy preserved).** The pattern **MUST NOT** bypass the ADI ordering mandated by **B.5**: induction may not start before deduction; abductive L0 creation remains the start.
**CC‑B.5.2.1‑6 (Normalization for Pareto).** When **Q** has multiple components with different units and scales, Contexts **SHALL** normalize or use declared utility‑free monotone transforms before dominance tests.
**CC‑B.5.2.1‑7 (Use‑Value separation). ** If Use‑Value (C.17 §5.2) is recorded outside the active `DominanceSet`, it SHALL remain outside Assurance scores and MAY inform decision lenses (Decsn‑CAL). If the current Context explicitly places `Use-Value` inside the active `Q` tuple, record that declaration together with its objective id / acceptanceSpec. Do not alter **R/G** semantics based on side-measure Use‑Value. (see **C.17 §5.2** for `Use-Value` and `ValueGain` definitions)
**CC‑B.5.2.1‑8 (Provenance).** Each `h_i` in the *CandidateSet* **MUST** reference its `provenance_i` sufficient to reproduce scores given the same `Policy(TimeWindow)`, score/metric versions, and `DeterminismSeed?`.
**CC‑B.5.2.1‑9 (Secondary metrics).** **I (illumination)** and **S (surprise)** SHALL be used only for tie‑breaking/reporting unless explicitly promoted by policy; the **primary dominance test uses the declared `DominanceSet`**, which under the ordinary default means the context-declared `Q` components.
**CC‑B.5.2.1‑10 (Cell capacity & ε).** If `K>1` or `ε>0` are used, the values MUST be declared and recorded in provenance; any thinning AFTER recording the front SHALL be documented in the DRR.
**CC‑B.5.2.1‑11 (Dominance set).** If the Context consumes the ordinary default `DefaultId.DominanceRegime`, the active dominance set **SHALL be the declared `Q` components** and provenance **SHALL** cite that consumed default plus the active `C.19` policy or lens id. **N (Novelty@context)** and **ΔDiversity_P** act as **tie‑breakers** unless explicitly promoted by **policy** (record the policy‑id in provenance).

### B.5.2.1:7 - Cognitive Load & Kernel Growth Budget

**For engineers/managers (user cognitive load).**

* *Added steps:* selecting descriptor **Characteristics** & granularity; reading a Pareto table (**non‑statisticians tip:** scan the “front” row; ignore dominated rows).
* *Mitigations:* provide a one‑screen “NQD Cards” template analogous to RSG cards; default grids and metrics per Context. (Keep ≤ 7 visible **Characteristics**—mirrors RSG human‑scale guidance.)
* *Reader quickstart (engineer‑manager):* (1) Pick 2–3 **Q** characteristics aligned to the anomaly + a simple **CharacteristicSpace** (2–4 dimensions). (2) Accept defaults for `NoveltyMetric`, grid granularity, and `K=1`. (3) Run **NQD‑Generate** to a fixed budget; read the *front row* first. (4) Apply Step 3 filters; log decisions in the DRR.

**For the framework (kernel growth).**

* *Zero* new primitives; only a CHR import and a **Method**. Passes **A.11** minimal‑sufficiency.

### B.5.2.1:8 - Placement in the Reasoning Cycle (ADI)

This pattern **only structures hypothesis exploration** (Abduction) and does not define or imply any **operational** gates. It respects ADI ordering (Abduct → Deduct → Induct) and leaves deployment/readiness concerns to patterns outside this spec.

### B.5.2.1:9 - Context‑Level KPIs (optional, informative)

Contexts *may* monitor these—*not* as gates, but to improve practice:

1. **Generativity (Gv).** Fraction of abductive cycles whose selected candidate reaches **L1/L2** within policy windows (time‑to‑L1; time‑to‑evidence). (Maps onto state transitions driven by **B.5**.)
2. **Frontier‑Hit Rate (FHR).** % of cycles where the chosen candidate lies on the **Pareto front** over the declared `DominanceSet` at selection time; track novelty/diversity contribution separately as archive, tie-break, or policy-promoted evidence.
3. Coverage Gain (ΔI, report). Change in the *illumination summary* (coverage map/%filled cells) per cycle (how much of the descriptor space is now “lit”).
4. **Exploration Cost Ratio (ECR).** Compute/time spent in NQD‑Generate divided by downstream Shape/Evidence cost saved (tracks whether the pattern pays for itself).
5. **Refutation Learning Yield (RLY).** Among *refuted* candidates, % that added new coverage or raised SurpriseScore—turning “failures” into map‑building.

### B.5.2.1:10 - Worked micro‑example (abbreviated)

**Framing = Step 1 in B.5.2**
**Context:** A Context using FPF to evolve FPF itself (meta‑improvement). *Anomaly:* “Users perceive FPF as compliance‑heavy; we need first‑principles creativity surfaced.”

**Step 2 (NQD‑Generate).**

* **CharacteristicSpace:** {*creative‑characteristic count*, *explicit novelty metric present?*, *QD operator present?*, *didactic cards present?*}. *(Illustrative; Contexts SHALL define their own descriptors per §2.)*
* **Q‑measures:** {*editor effort↓*, *time‑to‑L1↓*, *reader clarity↑*}.
* **Output Pareto set (sketch):**

  * `h₁ = “Add Creativity‑CHR + NQD pattern (this pattern)”` — high *D*, high *N*, medium *Q*.
  * `h₂ = “Rename governance terms to arts vocabulary”` — low *N*, low *D*, medium *Q*.
  * `h₃ = “Add live ideation sandbox (ops tooling)”` — medium *N*, medium *D*, high *Q*.

**Step 3 (Filters).**

* **Falsifiability:** `h₂` weak—no testable prediction → drop.
* **Scope (USM):** `h₁` scoped to Part B; `TimeWindow = edition 2025‑Q4` → *covers TargetSlice*. `h₃` crosses Contexts (tooling) → requires Bridge; the overhead is accounted for in **R** (not **F/G**). *(This pattern does not create or alter Bridges.)*
* **Select prime:** `h₁` → formalize as L0 episteme (this pattern), move to *Shaping* (define checklist), then *Evidence* (track KPIs).

### B.5.2.1:10a - Trade‑offs & mitigations

* **Cognitive effort.** Interpreting Pareto sets and coverage maps adds thinking overhead. *Mitigation:* standard “NQD Card” + default grids; keep **Characteristics** small in number (≤ 7). *Manager shortcut:* pick 2–3 **Q** characteristics that reflect the anomaly, then run with defaults.
* **Locality.** Novelty/diversity are **context‑local**; Cross‑context reuse requires **re‑measurement or an explicit mapping**. This pattern **does not define** Cross‑context operational controls.
* **Not a magic idea machine.** Abduction remains human/agentic; the pattern *structures* search, it does not automate insight. B.5’s abductive primacy stands.
* **Metric gaming & collinearity.** Avoid making **N** and **S** redundant by policy; when strong collinearity is detected, freeze one as informative only and record rationale in the DRR.

### B.5.2.1:11 - Related Patterns

* **Extends:** **B.5.2 Abductive Loop** (Step 2/3 operationalization).
* **Driven by / feeds:** **B.5 Canonical Reasoning Cycle** (Abduction→Deduction→Induction), **B.4 Evolution Loop** (Observe/Refine).
* **Uses:** **A.17/A.18** for characteristic discipline and **B.5 ADI ordering**. **May** refer to Context‑specific MAP‑Elites/novelty‑search implementations in the MethodDescription. **No operational gating is in scope here.** C.17 (Use‑Value / ValueGain, normative definition).
* **Respects:** **A.11** (no kernel growth beyond CHR template import + Method).

### B.5.2.1:End

---

## B.5.3 - Role-Projection Bridge

### B.5.3:1 - **Problem Frame**

The FPF is built upon a small set of universal, domain-agnostic concepts (`U.Types`) like `U.System`, `U.Objective`, and `U.State`. This universality is the source of its power, allowing it to be applied to any domain, from thermodynamics to software engineering. However, practitioners in these domains do not speak in terms of `U.Types`; they use their own rich, specialized vocabularies. A thermodynamicist talks about a "Thermodynamic System" and its "Macrostate," not a `U.System` and its `U.State`.

### B.5.3:2 - **Problem**

How can FPF bridge this gap between its universal core and the specific language of a domain without either polluting the kernel with domain-specific terms or forcing experts to abandon their familiar vocabulary? A simple alias mechanism (e.g., a dictionary mapping `U.System` to "Thermodynamic System") is insufficient because:

1.  **It's brittle:** It assumes a one-to-one mapping, which often breaks down. A single domain concept can play multiple universal roles in different contexts.
2.  **It's semantically poor:** It only captures naming, not the rich constraints and relationships that a domain-specific concept entails. We can't express that a "Thermodynamic System" is a *special kind* of `U.System` with specific properties related to temperature and pressure.
3.  **It's not integrated:** The mappings live outside the formal model, making them difficult to govern, version, and use in automated reasoning.

### B.5.3:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Universality vs. Specificity** | How to maintain a lean, universal kernel while accommodating the rich, specific terminologies of countless domains. |
| **Flexibility vs. Rigor** | How to allow a single entity to be viewed through multiple lenses (e.g., as a physical system and an economic asset) without creating ambiguity. |
| **Integration vs. Isolation** | How to incorporate domain knowledge into the formal model without hard-coding it into the FPF kernel, thereby preserving the Open-Ended Kernel principle (P-4). |

### B.5.3:4 - **Solution**

FPF solves this with the **Role-Projection Pattern**, a mechanism that creates a robust, semantically rich **Concept-Bridge** between the universal kernel and domain-specific vocabularies. This pattern is built on three core components:

#### B.5.3:4.1 - The `Role` Concept

*   **Description:** FPF introduces a new universal type, `U.Role`. A `Role` is not a concrete thing but an **abstract, context-dependent role** that an entity can play. It represents the domain-specific *interpretation* of a universal concept.
*   **Example:** "Thermodynamic System" is not modeled as a new subtype of `U.System`. Instead, it is modeled as a `Role` that a `U.System` can *play* when it is being analyzed from a thermodynamic perspective.

#### B.5.3:4.2 - The `refinesType` Relation**

*   **Description:** Every `Role` **MUST** declare which universal `U.Type` it refines or specializes. This is done via the `refinesType` relation.
*   **Example:** The `ThermodynamicSystemRole` would have the relation `refinesType: U.System`. This creates a formal, unbreakable link to the kernel. It guarantees that any entity playing this role still inherits all the fundamental properties and invariants of a `U.System`. This is a many-to-one relationship: many different roles (e.g., `EconomicSystemRole`, `BiologicalSystemRole`) can all refine the same `U.System` type.

#### B.5.3:4.3 - The `plays_role_of` Relation**

*   **Description:** This relation connects a **concrete entity** in a model to a `Role`. It is the assertion that "this specific thing is currently playing that specific role."
*   **Example:** In a model of a steam engine, we would assert that our specific engine instance `plays_role_of: ThermodynamicSystemRole`. This assertion signals to all tools and reviewers that this engine should be interpreted as a `U.System` and that the rules and constraints associated with the `ThermodynamicSystemRole` now apply to it.

> **Didactic Note for Managers: From "Alias" to "Job Description"**
>
> The Role-Projection pattern is the difference between giving someone an alias and giving them a job description.
>
> *   **An Alias (the old way):** Simply says "Bob is also known as The Manager." It's just a name swap.
> *   **A Role (the FPF way):** Says "Bob `plays_role_of` Manager." This is much richer. It implies that Bob has specific responsibilities, authorities, and performance expectations that come with the "Manager" role. He might also play other roles, like "Mentor" or "Team Lead."
>
> Similarly, when we say a component `plays_role_of` "Sensor," we are not just renaming it. We are activating a rich set of expectations and rules that come with being a sensor (e.g., it must have an output port, it must have a defined accuracy, etc.). This makes our models smarter, safer, and more precise.

### B.5.3:5 - **Archetypal Grounding**

To illustrate the pattern in action, let's consider how we would bridge the domain of **classical thermodynamics** to the FPF kernel.

1.  **Define the Roles:** A domain expert creates a set of `Role`s, each refining a core `U.Type`:
    *   A `U.Role` named `ThermodynamicSystemRole` with `refinesType: U.System`. It might have a description: "A region of the universe under study, separated by a boundary."
    *   A `U.Role` named `MacrostateRole` with `refinesType: U.State`. Its description could specify that it is defined by variables (P, V, T, N).
    *   A `U.Role` named `ControlVolumeRole` with `refinesType: U.Boundary`.
    *   A `U.Role` named `FreeEnergyObjectiveRole` with `refinesType: U.Objective`.

2.  **Apply the Roles in a Model:** An engineer modeling a heat engine would then use these roles:
    *   They create an instance of `U.System` representing the engine and assert: `HeatEngine_Instance plays_role_of: ThermodynamicSystemRole`.
    *   They model the engine's state and assert: `EngineState_Instance plays_role_of: MacrostateRole`.
    *   They define the system's goal and assert: `EngineObjective_Instance plays_role_of: FreeEnergyObjectiveRole`.

**What this achieves:**

*   The model is now **semantically rich**. Tools can now understand that `HeatEngine_Instance` is not just any system, but one that should be analyzed using the laws of thermodynamics.
*   The model is **verifiable**. A tool could now check if an entity playing the `MacrostateRole` actually has attributes for Pressure and Temperature, enforcing domain-specific consistency.
*   The model remains **universally compatible**. Because `ThermodynamicSystemRole` refines `U.System`, the heat engine can still be reasoned about as a generic system in a wider context (e.g., in a model of the entire power plant).

**Conformance Checklist**

*   **CC-B5.3.1 (Role Grounding Mandate):** Every `U.Role` **MUST** be linked to exactly one universal `U.Type` via the `refinesType` relation. Orphaned roles are forbidden.
*   **CC-B5.3.2 (Explicit Role Assertion):** A domain-specific concept **SHALL NOT** be treated as a subtype of a `U.Type` directly. Its relationship **MUST** be expressed using the `plays_role_of` relation to a `U.Role`.
*   **CC-B5.3.3 (Multi-Role Flexibility):** A single entity **MAY** `play_role_of` multiple `Role`s simultaneously, even from different domains.
*   **CC-B5.3.4 (Semantic Integrity):** A `Role` **MAY** introduce additional constraints or required attributes that are more specific than those of the `U.Type` it refines, but it **SHALL NOT** contradict them.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Subtype Explosion"** | The list of system "types" in the project grows endlessly: `ThermodynamicSystem`, `EconomicSystem`, `SoftwareSystem`, etc. The ontology becomes bloated and unmanageable. | **CC-B5.3.2** forbids this. There is only one `U.System`. Different perspectives on it are modeled as `Role`s, which keeps the core ontology lean. |
| **The "Magic Synonym"** | A developer simply renames `U.System` to "Thermodynamic System" in their diagrams, but there are no formal rules or constraints attached. The term is just an alias. | The FPF pattern requires a formal `Role` with a `refinesType` link. This is a rich, structural connection, not just a cosmetic name change. |
| **The "One-Hat Fallacy"** | The model forces an entity to be only one thing. An asset can be a "Physical Component" or a "Financial Asset," but not both, leading to duplicated models. | **CC-B5.3.3** explicitly allows an entity to play multiple roles. A single server in your data center can simultaneously `play_role_of` "PhysicalComponent" (for Sys-CAL) and "DepreciableAsset" (for a financial mechanisms). |

### B.5.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Semantic Richness and Precision:** The pattern allows domain-specific constraints and rules to be formally integrated into the model, enabling much more powerful automated checking and reasoning. | **Increased Modeling Granularity:** It introduces a layer of indirection (`Entity → Role → U.Type`) that modelers must learn. *Mitigation:* Tooling can automate much of this, suggesting relevant roles based on the context or domain. |
| **Multi-Domain Integration:** The pattern provides a clean and robust mechanism for a single model to incorporate concepts from multiple, diverse domains without conflict. | - |
| **Preserves a Lean Kernel:** The FPF kernel remains small and universal, with all domain-specific complexity handled in a modular, plug-in fashion via `Role` libraries. | - |
| **Enhanced Traceability and Clarity:** The roles an entity plays are explicit assertions. This makes the model's intent clear and auditable. | - |

### B.5.3:7 - **Rationale**

The Role-Projection pattern is the cornerstone of FPF's approach to **universality with specificity**. It is a direct implementation of the **Open-Ended Kernel (P-4)** and **FPF Layering (P-5)** principles. By separating the timeless, universal concepts (`U.Types`) from their context-dependent, domain-specific interpretations (`Role`s), FPF achieves a powerful balance.

This approach is inspired by contemporary practices in both ontology engineering (e.g., the use of role concepts in foundational ontologies like UFO) and software architecture (e.g., aspect-oriented programming and role-based modeling), but it integrates them into a single, coherent pattern. It provides a formal, scalable, and semantically rich solution to the perennial problem of bridging the universal and the particular.

### B.5.3:8 - **Relations**

*   **Implements:** `ADR-003: Role-Projection Pattern and Concept-Bridge`.
*   **Enables:** The practical application of all FPF patterns by providing the "glue" that connects them to the FPF kernel.
*   **Used By:** All other patterns in the reasoning cycle, as it provides the vocabulary for framing hypotheses and interpreting evidence in a domain-specific context.

### B.5.3:End

# **Part C — Kernel Extensions Specifications**

| §                                            | Pattern                        | Tag | Scope & Exports                                                      |
| -------------------------------------------- | ---------------------------------- | --- | -------------------------------------------------------------------- |
| **Cluster C.I – Core CALs / LOGs / CHRs**    |                                    |     |                                                                      |
| C.1                                          | **Sys‑CAL**                        | CAL | Physical holon composition; conservation invariants; resource hooks. |

## C.2 - Epistemic holon composition (KD-CAL)

**Scope & exports.** A substrate‑neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their motion and equivalence. Exports: (i) three **point‑characteristics**—**Formality F**, **ClaimScope G**, **Reliability R**—that locate a single episteme; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ‑moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; (v) propagation laws for CL through mappings and notation bridges. KD‑CAL is typed by `U.EpistemeSlotGraph` and never confuses `ClaimGraph`, `DescribedEntitySlot`, `GroundingHolonSlot`, `Viewpoint`, `View`, `ReferenceScheme`, notation, publication form, or carrier. All F–G–R computations are **context‑local**; Cross‑context traversals **require** an explicit **Bridge** with **CL** and apply the **B.3** congruence penalty **Φ(CL)** to **R**.  // Contexts ≡ U.BoundedContext; substitution is plane‑preserving only.

**Formality F** is the rigor characteristic defined **normatively in C.2.3**. All KD‑CAL computations and guards **SHALL** use `U.Formality` (F0…F9) as specified there; **no parallel “mode” ladders** are allowed.

### C.2:1 - Problem Frame

FPF fixes two archetypal sub‑holons: **`U.System`** (physical/operational) and **`U.Episteme`** (knowledge holon). KD‑CAL is the primary composition pattern for `U.Episteme`, giving engineers a compact, testable way to say (a) how strictly an episteme is written (**F**), (b) how much structure it manages (**G**), (c) how well it is warranted by evidence or severe tests (**R**), and (d) how closely **two** epistemes coincide (**CL**). KD‑CAL is built atop **C.2.1 U.Episteme — Epistemes and their slot graph**, which reifies every episteme through `U.EpistemeSlotGraph`: `ClaimGraph`, `DescribedEntitySlot`, `GroundingHolonSlot`, `Viewpoint`, `View`, and `ReferenceScheme`. Notation, publication forms, carriers, and work occurrences remain outside episteme content and are linked by their own FPF relations.

### C.2:2 - Problem

Teams routinely entangle **programs, specifications, proofs, and datasets**; a “proof” is treated as a tested routine, a “program” is cited as if it entailed a theorem. **Trust decays** because justification and evidence freshness are not explicit. Epistemes are anthropomorphised as actors (“the standard enforces…”), producing **category errors at execution**. Without a shared composition and equivalence calculus, aggregates hide weakest links and analogies harden into overclaims. KD‑CAL must stop these failure modes with a **single constitution and scale‑set**.


### C.2:3 - Forces

* **Universality vs domain idioms.** One calculus must cover physics theories, legal codes, safety specs, algorithms, and formal proofs without flattening their differences.
* **Meaning vs materiality.** Meaning must be independent of carrier, yet accountable to it historically.
* **Deductive vs empirical.** Axiomatic certainty and empirical trust have different evidence-continuity profiles; both must compose.
* **Abstraction vs enactment.** Epistemes constrain action; **systems** act. The calculus must keep the roles distinct.


### C.2:4 - Solution

#### C.2:4.1 - Coordinates and the episteme slot graph

**KD‑CAL characteristics (single‑episteme, point‑values).**

* **Formality F.** From free prose to **machine‑checkable proof/specification**. Litmus: *would a machine reject it if wrong?*
* **Claim scope (G), a set‑valued applicability over `U.ContextSlice`, with ∩/SpanUnion/translate algebra; CL penalties apply to R, not to F/G.** Litmus: *how wide is the declared scope, and under what minimal assumptions does the claim hold?*
* **Reliability R.** From untested idea to **continuously validated claim**. Litmus: *where is the last successful severe test?* **R‑claims MUST bind to evidence and declare relevance windows; stale bindings degrade R or require waiver per ESG policy.**

 **Congruence Level (CL), pairwise ladder.**
 `CL‑0` **Opposed/Disjoint** (contrastive; no substitution); `CL‑1` **Comparable / Naming‑only** (label similarity; no substitution); `CL‑2` **Translatable / RoleAssignment‑eligible** (structure‑preserving mapping in a declared fragment with **stated loss**; theorems may transport); `CL‑3` **Near‑identity / Type‑structure‑safe** (invariants match; type‑structure substitution allowed). *CL is a characteristic of a relation between two epistemes; it is not a fourth member of the F–G–R assurance tuple and it is not a characteristic space of its own.* **Norm:** substitution is permitted only if plane‑preserving and **CL ≥ 2**; substituting **type‑structure** requires **CL = 3**.

**Slot-graph link.** The assurance components are stated over `U.EpistemeSlotGraph`: *F* by the internal `ClaimGraph` and formal substrate, *G* by the `ClaimScope` attached to the described entity and assumptions, and *R* by evaluation templates and evidence bindings. Notation belongs to representation and reference-scheme structure; carriers remain outside the episteme and link through SCR/RSCR or other exact carrier relations. Multiple notations are allowed only when their relation is explicit; authors SHOULD register `NotationBridge(n₁,n₂)` with an associated **CL** to make conversion loss explicit.

#### C.2:4.2 - Four Δ‑moves (epistemic motion)

* **ΔF — Formalise.** Rewrite for stricter calculi/grammars; raise proof obligations.
* **ΔG — Generalise / Specialise.** Widen or narrow the **claim scope** (assumptions & scope). Changes to decomposition granularity are an **orthogonal view** and do not change **G** unless they alter the envelope.
* **ΔR — Calibrate / Validate.** Strengthen severe tests or add live monitoring; update evidence bindings.
* **ΔCL — Congrue.** Establish and record the sameness relation between **two** epistemes (ladder 0→3).
  Moves compose into **paths**; CL along a path is the **minimum** of its links.

#### C.2:4.3 - Composition (Γ\_epist) and propagation

Let **Γ\_epist** combine epistemes `{Eᵢ}` into a composite episteme **Γ** that makes a joint claim (*AND‑style*) or exposes an interface (*series composition*). KD‑CAL imposes **safe defaults**:

* **R (Reliability).** Along any justification **path** `P`, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`** (weakest‑link with congruence penalty). For **series** composition (claims needed conjunctively), the path‑wise weakest‑link applies; for **parallel** support (independent lines to the *same* claim), use **`R(Γ) = max_P R_eff(P)`** (annotate independence); never exceed the best attested line. Cross‑context steps and **NotationBridge** traversals contribute to `CL_min(P)`.

* **F (Formality).** `F(Γ) = minᵢ F(Eᵢ)` (monotone non‑increasing along used paths). To raise **F**, apply **ΔF** to the weakest parts.
* **G (ClaimScope).** On any dependency **path**, take the **intersection** of claim scopes (the **narrowest overlapping scope**). Across **independent support paths to the same claim**, set **`G(Γ) = SpanUnion({G_path})` constrained by support** (drop unsupported regions). Widening/narrowing the scope is an explicit **ΔG±** operation.
* **CL (Congruence).** For a chain of mappings `E₀ ~ E₁ ~ … ~ Eₖ`, the **path congruence** is `min CL(Eⱼ,Eⱼ₊₁)`. Passing through a **NotationBridge** sets CL to the bridge’s declared level; the **Φ(CL)** penalty is applied in the **R** fold for any path that traverses it.

These rules keep Γ aligned with the **holonic kernel**: Γ is only defined on holons and respects identity/boundary discipline from the core.

#### C.2:4.4 - What **must not** be conflated (normative guards)

* **Representation structure ≠ carrier.** Files, PDFs, or repositories are **carriers** outside the episteme; they never count as parts of `U.Episteme` (**see C.2.1 EP‑1; CC‑EPI‑2/3**).
* **Epistemes do not act.** Only **systems** perform work; epistemes carry constraints and evaluation criteria through their `ClaimGraph`, described entity, grounding holon, scope, and evidence bindings (**per Core A.15 / CC‑EPI‑3**).
* **CL is not a score.** It is a **qualitative ladder** of preservation classes; do not average it.


### C.2:5 - ✱ Archetypal Grounding (Tell–Show–Show)

**Universal rule (tell).** *Compose knowledge by Γ\_epist with weakest‑link R, monotone F, and explicit CL on every bridge; keep `ClaimGraph`, described entity, grounding holon, viewpoint, view, reference scheme, notation, publication form, and carrier in their exact FPF relations.*

**System (show, Sys‑CAL lens).** Consider a **battery‑pack thermal subsystem** integrating a physics model of heat flow and an operating envelope for fast‑charge. As a **system**, it composes pumps, sensors, and controllers by physical Γ with conservation constraints (Sys‑CAL). The assurance story depends on epistemes about the model and envelope; the system **acts**, epistemes constrain. (Archetypes and boundary discipline per core.)

**Episteme (show, KD‑CAL lens).** Consider a **CMIP‑class climate projection episteme** (post‑2015 generation): its `ClaimGraph` covers PDEs and parameterisations; its described entity and grounding holon identify what projection claim is about and how it is grounded; its `ClaimScope` names historical forcings, resolution, and assumptions; its representation may include domain equations and a tabular schema linked by a **NotationBridge** with an explicit CL. Compose sub‑epistemes for radiation, clouds, and ocean mixing: `R = min` across the critical path; an independent hindcast line can raise `R` only up to its own level; `F` is bounded by the least‑formal sub‑claim unless the composition adds formal invariants.


### C.2:6 - Bias‑Annotation

* **Metric worship.** Treating `[F,G,R]` as ends rather than means; mitigation: require **evidence bindings** and narrative of limits in the claim scope and grounding envelope.
* **Category slip.** Equating a notation or carrier with `ClaimGraph`, described entity, or grounding holon; mitigation: slot-graph and carrier separation under C.2.1.
* **Analogy inflation.** Presenting CL‑0/1 as identity; mitigation: always name the **CL rung** for cross‑mappings.


### C.2:7 - Conformance Checklist

1. **C2‑1 (Slot graph).** Every `U.Episteme` **MUST** satisfy C.2.1 slot discipline for `ClaimGraph`, `DescribedEntitySlot`, `GroundingHolonSlot`, `Viewpoint`, `View`, and `ReferenceScheme`; carriers link through SCR/RSCR or other exact carrier relations and are never parts of the episteme.
2. **C2‑2 (Coordinates).** Each episteme **SHALL** declare `[F,G,R]` with a brief rationale; **F** is `U.Formality ∈ {F0…F9}` per **C.2.3**, **exactly one episteme‑level F** computed as the **min over essential parts**. CL is declared for **pairs only**. Sub‑anchors: ** Contexts **MAY** mint named sub‑anchors (e.g., `F4[OCL]`, `F7[HOL]`), which **MUST** preserve the global order and **map to their parent anchor** from C.2.3.
3. **C2‑3 (Composition).** Authors **SHALL** choose Γ_mode (**series** vs **parallel**). For any justification **path** use **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for **parallel** independent lines to the *same claim*, take **`R(Γ) = max_P R_eff(P)`** (never exceeding the highest-R support line). Compute `F(Γ) = min` along the used paths. For **G**, use **path‑wise intersections** and then **SpanUnion({G_path}) constrained by support**. Cross‑context traversals **MUST** use a Bridge with **CL** and apply **Φ(CL)** to `R`.
4. **C2‑4 (NotationBridge).** Multi‑notation representation components **SHOULD** register `NotationBridge` edges with CL and loss note; any cross‑notation reasoning **MUST** cite the bridge’s CL.
5. **C2‑5 (No action).** Epistemes **MUST NOT** be assigned actions; work is executed by systems in role.


### C.2:8 - Consequences

**Benefits.** A single, compact **map** for all knowledge epistemes or publications; fast detection of weakest‑link **R** in aggregates; disciplined reuse across domains with explicit **CL**; consistent separation of **meaning** from **material carriers**.
**Trade‑offs.** Authors must learn to declare Γ‑mode and CL explicitly; multi‑notation work requires bridge bookkeeping; *mitigation:* the episteme slot graph and CL scale keep the discipline brief and repeatable.


### C.2:9 - Rationale

KD‑CAL turns the coarse legacy semiotic picture into **holonic composition** over `U.EpistemeSlotGraph`, where formal structure and claim scope (**F,G**), evidence (**R**), and cross‑mapping congruence (**CL**) are visible and composable. The explicit C.2.1 slot graph prevents carrier confusion; the characteristics provide a **manager‑readable** yet **formalisation‑ready** scale (with **G** grounded in **scope/envelope**, not part‑count); the CL scale replaces overloaded “alignment” with a typed sameness relation.


### C.2:10 - Relations

* **Depends on:** `U.Episteme — Epistemes and their slot graph` (C.2.1): identity invariants, slot definitions, carrier separation, and evidence bindings.
* **Peers:** **Sys‑CAL** (C.1), which composes **systems**; KD‑CAL composes **epistemes** and feeds assurance lenses in Part B.
* **Constrained by authoring:** Architectural patterns must include Tell–Show–Show with **Archetypal Grounding** (this section).

### C.2:11 - Worked mini‑examples (post‑2015 flavours)

* **Formal lift (ΔF).** Recasting a 2019 **variational free‑energy** narrative into a typed calculus raises **F**, clarifies scope, and enables CL‑2 bridges between biological and ML formulations—*without* claiming empirical gain (**R** unchanged).
* **Parallel evidence (R, max).** Two independent **hindcast** lines (circa CMIP6, 2019) supporting the same forecast allow `R(Γ)=max(R₁,R₂)`; if one line drifts, the composite is bounded by the higher-R support line until series constraints apply.
* **Notation bridge (CL drop).** A 2021 **type‑theoretic specification** rendered in a semi‑formal DSL requires a `NotationBridge` with a CL<3 note; any theorem transported across must respect the bridge’s declared preservation.

*(No tooling is implied; these are conceptual moves within the calculus.)*

### C.2:End

## C.2.1 - U.Episteme — Epistemes and their slot graph

> **One-line summary.** `U.Episteme` is the holon type for epistemes; its internal ontology is given by `U.EpistemeSlotGraph`, which replaces the legacy **semantic triangle** with a typed graph n-ary relation over `DescribedEntity`, `GroundingHolon`, `ClaimGraph`, `Viewpoint`, `View`, and `ReferenceScheme`, aligned with `U.RelationSlotDiscipline` and ready for both symbolic and distributed representations.

### C.2.1:1 - Context

FPF’s kernel recognises two archetypal sub‑holons: **System** and **Episteme**. Systems are operational wholes; **epistemes** are **knowledge holons**—theories, models, specifications, standards, algorithms, proofs—whose reason for being is to **say something defeasible or deductive about something** and to be **held to account** by justification.

**Readers.** Engineering managers and lead designers who need a uniform way to reason about **theories, specifications, algorithms, proofs**—from charter memos up to formal axiomatics—without collapsing into tooling or discipline‑specific notations.

KD‑CAL (C.2) needs a precise notion of **what an episteme is** and **how it mediates** between:

* the thing(s) it is about,
* the contexts and systems that ground and test it, and
* the representational machinery (notations, carriers, operations) we use to work with it.

Contemporary work on **formal languages as cognitive artifacts** (Dutilh Novaes), **operational iconicity** of notations (Krӓmer), **material engagement** (Malafouris), **distributed representations** and **latent‑space communication** in ML, and **tool‑augmented reasoning** (ReAct‑style agent loops) shows that:
* the relation between an episteme and its **DescribedEntitySlot** is not a single “Object-vertex”: it involves explicit **slots and morphisms** (described-entity mapping, grounding, evaluation) typed by SlotKinds and contexts;
* **representations** come in heterogeneous forms (symbolic, diagrammatic, latent, interactive), with very different **supported operations**;
* **inference** is often **mixed‑mode**: symbolic reasoning plus calls to tools, solvers, and learned models.

FPF therefore needs a **more modular, graph‑shaped ontology** for epistemes which:
* keeps **KD‑CAL** and I/D/S discipline intact,
* is compatible with **A.6.0/A.6.5** signatures (`SlotKind`/`ValueKind`/`RefKind`),
* can be used uniformly by A.6.2–A.6.4 (epistemic morphisms) and E.17.* (views & publication),
* and demotes the old non-SoTA **semantic triangle** to a **didactic projection**, not the normative ontology.

In this pattern:
* `U.Episteme` is the **holon genus** for epistemes (C.2), with components and identity governed by A.1/A.6.0/A.7.
* `U.EpistemeSlotGraph` names the **internal ontology graph** of `U.Episteme`: the small, typed n-ary relation over episteme positions (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) on which KD-CAL, A.6.2–A.6.4 and E.17.* rely.
* Species such as `U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication` are holonic realisations of `U.Episteme` whose component structure is constrained to be compatible with `U.EpistemeSlotGraph`.

### C.2.1:2 - Problem

Without a shared **episteme constitution**, teams fall into recurring failure modes:

1. **Object–Description–Carrier soup.** Diagrams and files are treated as *the theory itself*. Changes to a PDF are confused with theoretical change.
2. **DescribedEntity blur.** A spec seems to describe “everything in general”. The **DescribedEntitySlot** - what exactly this knowledge describes - is implicit and drifts, while the **GroundingHolonSlot** that would say where the claim is grounded is also missing.
3. **Proof vs program confusion.** Algorithms, specifications, and proofs are mixed: a “proof” is used as if it were a tested routine; a “program” is cited as if it entailed a theorem (Curry–Howard misunderstood).
4. **Unanchored trust.** Claims accumulate with no explicit **justification graph** or **evidence freshness**, so assurance degrades invisibly.
5. **Category errors at execution.** Epistemes appear as *actors* (“the standard enforces…”) instead of **systems** acting *with* or *on* epistemes such as data sets or algorithms.

The legacy non-SoTA “Semantic Triangle” treated an episteme as a holon with three components: **Concept** (ClaimGraph), **Object** (Reference Map), and **Symbol** (notation).

This worked well for:
* separating **meaning** (Concept) from **carriers**, and
* integrating KD‑CAL’s **F–G–R** characteristics (Formality, ClaimScope, Reliability).

But for current use‑cases it has structural blind spots:

1. **No explicit DescribedEntity slot.**
   The “Object vertex” bundles together *what the episteme is about* with *how we interpret and test it*. There is no explicit **slot** for the entity‑of‑interest (`U.Entity`) and no clear separation between:
   * the **described entity**, and
   * the **ReferenceScheme** used to read claims as statements about that thing.

2. **Grounding collapses into Object.**
   Material and organisational contexts (labs, infrastructures, organisations) that **ground** an episteme (in Malafouris’ sense) are hidden in the Object/Reference Map. KD‑CAL and Bridges need explicit **GroundingHolon** positions.

3. **Viewpoints are not first‑class.**
   ISO‑style **viewpoints** (families of stakeholders, concerns, conformance rules) and their induced **views** appear only indirectly, via KD‑CAL or MVPK. There is no explicit `U.Viewpoint` / `U.View` pair at the episteme core, which makes it hard to:

   * connect to I/D/S **DescriptionContext**,
   * organize multi‑view descriptions (E.17.0), or
   * align publication viewpoints with engineering viewpoints.

4. **Representations and operations are compressed into “Symbol”.**
   Very different representational regimes are flattened into one Symbol vertex:

   * label-only notations (no internal inference calculus),
   * fully operational calculi (e.g., proof assistants),
   * interactive visualisations,
   * latent vectors and prompt‑programs for LLMs.
     There is no place to say “this representation admits **syntactic inference** of such‑and‑such kind” vs “this is just a **passive label**”.

5. **No explicit signature discipline.**
   The triangle speaks of “Object/Concept/Symbol” but not of **slots** and **references** in the sense of A.6.5 `U.RelationSlotDiscipline`. In episteme this leads to:
   * names where **slot, value and ref** are conflated (`DescribedEntityRef` used as if it were a slot),
   * ambiguity between the **described entity** (what the episteme describes) and the **episteme** (the description),
   * fragile interoperability with signatures for roles, methods, services.

Thus we have problems of:
* **DescribedEntity drift.**
 Specifications and models accumulate without a stable notion of **which DescribedEntitySlot value they carry**; fields like `SubjectRef` are overloaded and resist safe refactoring.
* **Viewpoint confusion.**
  Engineering, publication and governance views are mixed, making it hard to maintain consistency across surfaces or to reason about conformity of descriptions under different viewpoints.
* **Representation mismatches.**
  Trade‑offs between neural vs symbolic, diagrammatic vs textual, or interactive vs batch representations cannot be expressed at the episteme level; they leak into ad‑hoc tool descriptions.
* **Broken modularity.**
  As soon as we add KD‑CAL, LOG‑CAL, MVPK, and E.TGA, multiple **implicit triangles** appear, each with slightly different semantics, instead of a single shared `U.EpistemeSlotGraph`.

We need a replacement for the triangle that keeps its **didactic clarity** but matches the **graph‑ and morphism‑centric** reality of contemporary epistemic work.

### C.2.1:3 - Forces

| Force                                          | Tension we must resolve                                                                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Geometry vs. operations**                    | Simple geometric pictures (triangles) are memorable; real epistemic work is **operational and graph‑shaped** (many nodes, many edges). |
| **Universality vs. representation regimes**    | One ontology must accommodate symbolic calculi, diagrams, DSLs, interactive notebooks, and latent vectors.                             |
| **Intension vs. description vs. spec (I/D/S)** | Intensional objects (I) are not epistemes; descriptions (D) and specifications (S) are. The core must honour Strict Distinction.       |
| **Viewpoint locality vs. reuse**               | Viewpoints should be **local** to families of descriptions, yet we want reusable **viewpoint bundles** across domains (E.17.1/E.17.2). |
| **Slot discipline vs. usability**              | A clean `SlotKind`/`ValueKind`/`RefKind` discipline is vital for reasoning, but must not render engineering episteme unreadable.             |
| **Stability vs. SoTA evolution**               | The core must remain stable while integrating evolving practices: LLM tool‑use, ReAct‑style loops, structured cospans, optics, etc.    |

### C.2.1:4 - Solution — from outdated semantic triangle to `U.EpistemeSlotGraph`

#### C.2.1:4.0 - Overview

For `U.Episteme`, the legacy semantic triangle is replaced by `U.EpistemeSlotGraph` that is a **small, typed ontology graph** and an **n-ary relation view** over the core episteme positions:

 **Nodes / positions / slots.**
  Minimal **kernel SlotKinds** (with their ValueKinds) that every episteme can refer to, following A.6.5:
  * `DescribedEntitySlot`  (ValueKind `U.Entity` or a declared subkind) → *“what this episteme is about”*;
  * `GroundingHolonSlot`   (ValueKind `U.Holon`) → *“where/how this is grounded”*;
  * `ClaimGraphSlot`       (ValueKind `U.ClaimGraph`) → *“what is being said (intensional content)”*;
  * `ReferenceSchemeSlot`  (ValueKind `U.ReferenceScheme`) → *“how we read claims as statements about entities”*;
  * `ViewpointSlot`        (ValueKind `U.Viewpoint`) → *“under which viewpoint we read/validate this episteme”*;
  * `ViewSlot`             (ValueKind `U.View`) → *“a view‑episteme produced under a viewpoint”*.

* **Slots and signatures.**
  These positions are realised as **SlotKinds** with associated **ValueKinds** and **RefKinds** under `U.RelationSlotDiscipline` (A.6.5). An **episteme kind** (`U.EpistemeKind`) is a **signature** over these slots.

* **Episteme as n‑ary relation and as holon.**
  Each concrete episteme instance can be seen both as:

  * a **tuple** filling these slots (`U.EpistemeTuple`), and
  * a **holon with components** (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) whose fields correspond to those slots.

`U.Episteme` is thus the holon type whose components are *disciplined* by the `U.EpistemeSlotGraph`; C.2.1 fixes that discipline.

* **Morphisms.**
  Simple **epistemic morphisms** (described-entity mapping, grounding, encoding, evaluation) are expressed as ordinary relations/functions between these positions. A.6.2–A.6.4 then specify general laws for effect-free morphisms over `U.Episteme`.

* **Legacy triangle as didactic projection.**
  The classic Symbol–Concept–Object triangle becomes a **didactic view** of this graph, not the normative ontology; it is simply the projection to:

  * `Symbol` ≈ a subset of `U.RepresentationScheme`/`U.RepresentationToken`,
  * `Concept` ≈ `U.ClaimGraph`,
  * `Object` ≈ `{DescribedEntity, ReferenceScheme}`.

The rest of this pattern fixes the **minimal core** needed by KD‑CAL, A.6.2–A.6.4 and E.17.\*. The representational nodes (`U.RepresentationScheme`, `U.RepresentationToken`, `U.PresentationCarrier`, `U.RepresentationOperation`) are introduced as an **extension C.2.1+**, preserving the interface defined here.

#### C.2.1:4.1 - Minimal epistemic positions (nodes & slots)

This section defines the **minimal node set** for `U.EpistemeSlotGraph` and the associated **SlotKinds**. These are the positions that A.6.2–A.6.4 and E.17.* can rely on.

##### C.2.1:4.1.1 - `DescribedEntitySlot` — “what this episteme is about”

**Tech:** `DescribedEntitySlot` (SlotKind), `describedEntityRef : U.EntityRef` (Ref slot in tuples/cards).
**Plain:** *described entity*, *entity of interest*.

**Intent.** Provide a **single, explicit slot** for the entity (or entities) that an episteme is about, avoiding the former conflation of Object/Reference/Context.

**Normative definition.**

1. `DescribedEntitySlot` is a **SlotKind** in the sense of A.6.5 `U.RelationSlotDiscipline`.

   * Its **ValueKind** is `U.Entity`.
   * Its **RefKind** is `U.EntityRef` (or a species thereof) and **MUST** be realised in data as a field named `describedEntityRef : U.EntityRef` (E.10 discipline).
1. Species of `U.EpistemeKind` **MAY** constrain the ValueKind to a subtype `EoIClass ⊑ U.Entity` (for example, “EoI is always a `U.Holon` and, more specifically, a `U.System` or `U.Episteme`”). The subtype **MUST NOT** be named `U.DescribedEntity`; “described entity” remains a **role name**, not a kernel type.
2. Wherever episteme previously used `U.EpistemicObject` as a separate type, it is re‑interpreted as **“`U.Entity` in the role of filling `DescribedEntitySlot`”** and is marked as **legacy alias** in LEX‑BUNDLE.

**Didactic cue.**
“Ask: *What, exactly, is this description about?* That is the DescribedEntity.”

##### C.2.1:4.1.2 - `GroundingHolonSlot` — “where / in what holon this is grounded”

**Tech:** `GroundingHolonSlot` (SlotKind), `groundingHolonRef : U.HolonRef?`.
**Plain:** *grounding holon*, *holon‑of‑grounding*, *engagement context*.

**Intent.** Capture the **material–social holon** (system, lab, infrastructure, organisation, runtime environment) with respect to which an episteme’s claims are **tested, calibrated or validated**.

**Normative definition.**

1. `GroundingHolonSlot` is a **SlotKind** with:

   * **ValueKind** `U.Holon`,
   * **RefKind** `U.HolonRef` (or a species thereof),
   * and recommended field name `groundingHolonRef? : U.HolonRef` in episteme cards/views.
2. `GroundingHolonSlot` is **optional** at the minimal core: an episteme may be **un‑grounded** at M‑mode (e.g., purely mathematical), but any episteme used for **empirical evaluation or assurance** under KD‑CAL **SHALL** either:

   * populate `groundingHolonRef`, or
   * declare explicitly that no such grounding is possible (e.g., counterfactuals, abstract logics), with consequences reflected in KD‑CAL `R`.
3. The phrase *“grounding holon”* is **plain‑register**; there is no kernel type `U.GroundingHolon`. It always means “the holon currently filling `GroundingHolonSlot` for this episteme.”

**Didactic cue.**
“Ask: *In which lab/organisation/world‑slice do we test or observe this?* That is the GroundingHolon.”

##### C.2.1:4.1.3 - `U.ClaimGraph` and `ClaimGraphSlot` — intensional content

**Tech:** `U.ClaimGraph` (kernel type), `ClaimGraphSlot` (SlotKind).
**Plain:** *claim graph*, *intensional content*.

**Intent.** Reuse the existing KD‑CAL notion of **ClaimGraph** as the episteme’s **intensional body**, but make its role as a **slot value** explicit.

**Normative definition.**

1. `U.ClaimGraph` is the **ValueKind** for `ClaimGraphSlot`:

   * nodes: typed claims (definitions, axioms, theorems, requirements, properties, assumptions);
   * edges: logical/derivational/refinement relations, as already defined in C.2.
2. `ClaimGraphSlot` is a **SlotKind** whose instances are always **stored by value** in core patterns:

   * `content : U.ClaimGraph` is the normative field in `U.EpistemeCard` / `U.EpistemeView`;
   * C.2.1 **MUST NOT** introduce `U.ClaimGraphRef` as a ValueKind. Any reference type for ClaimGraphs, if needed, is a **RefKind** defined by discipline packs on top of `U.ClaimGraph`.
3. `ClaimGraphSlot` is **mandatory**: every `U.EpistemeKind` that uses C.2.1 **SHALL** have exactly one `ClaimGraphSlot`.

**Didactic cue.**
“Ask: *What is actually being claimed, defined, required, proved?* That is the ClaimGraph.”

##### C.2.1:4.1.4 - `U.Viewpoint` and `ViewpointSlot` — perspective of concerns and validators

**Tech:** `U.Viewpoint` (kernel type), `ViewpointSlot` (SlotKind), `viewpointRef : U.ViewpointRef?`.
**Plain:** *viewpoint*, *perspective*, *stakeholder perspective*.

**Intent.** Provide a **first-class reusable catalogue** for ISO-style viewpoints and their generalisations, as used by E.17.0 `U.MultiViewDescribing`, MVPK, and TEVB.

**Normative definition.**

1. `U.Viewpoint` is the type of **intensional viewpoint specifications**:

   * families of **RoleEnactors/stakeholder groups** the viewpoint speaks for,
   * their **concerns**,
   * allowed **kinds of descriptions/specifications**,
   * and **conformance rules** for views under this viewpoint.
     (The internal structure of `U.Viewpoint` is fixed in E.17.0, not here.)
2. `ViewpointSlot` is a **SlotKind** with:

   * **ValueKind** `U.Viewpoint`,
   * **RefKind** `U.ViewpointRef`,
   * normative field name `viewpointRef? : U.ViewpointRef` on episteme cards/views.
3. For **I/D/S descriptions/specs** (E.10.D2), `viewpointRef` is a **mandatory part of `DescriptionContext`**; C.2.1 treats that as a **species‑level constraint**, not as a universal requirement for all epistemes.
4. `ViewpointSlot` may be unset in purely internal, pre‑viewpoint epistemes (e.g., raw formal developments), but any episteme that participates in **MultiViewDescribing** (E.17.0) **MUST** set it or be deterministically associated to it via a `ViewpointBundle`.

**Didactic cue.**
“Ask: *Who is this for, and what do they need to see to accept it?* That is the Viewpoint.”

##### C.2.1:4.1.5 - `U.EpistemeView` / `U.View` and `ViewSlot` — episteme‑level views

**Tech:** `U.EpistemeView` (kernel species of `U.Episteme`), alias `U.View`; `ViewSlot` (SlotKind); `viewRef : U.ViewRef`.
**Plain:** *view*, *epistemic view*.

**Intent.** Distinguish **view‑epistemes** (views **of** descriptions/specifications) from both:

* the underlying descriptions/specifications themselves, and
* the MVPK `PublicationSurface`/`InteropSurface` `SurfaceKind` values and the external carriers/renderings on which views are made available (E.17, L-SURF, SCR/RSCR).


**Normative definition.**

1. `U.EpistemeView` is a **species of `U.Episteme`** whose episteme kind includes, at minimum:

   * one `ClaimGraphSlot` (typically a **sliced or projected ClaimGraph**),
   * one `DescribedEntitySlot`,
   * one `ViewpointSlot`,
   * and appropriate `ReferenceSchemeSlot`.
2. `U.View` is an **alias** for `U.EpistemeView` in E‑cluster patterns (especially E.17.\*), used where the word “view” is conventional.
3. `ViewSlot` is a **SlotKind** whose:

   * **ValueKind** is `U.View`,
   * **RefKind** is `U.ViewRef` (or `U.EpistemeViewRef` species),
   * intended usage is **in meta‑structures** such as `U.MultiViewDescribing` families and MVPK.
4. `ViewSlot` **MUST NOT** be confused with publication-face labels, `SurfaceKind` declarations, or carrier slots: a concrete MVPK face that is a view is represented as `U.View` or `U.EpistemeView`, while the face label or profile, `PublicationSurface` kind or `InteropSurface` kind, and carrier or rendering remain separate lanes.


**Didactic cue.**
“Ask: *Which particular slice of the description under this viewpoint are we talking about?* That is the View.”

##### C.2.1:4.1.6 - `U.ReferenceScheme` and `ReferenceSchemeSlot` — reading ClaimGraph as claims about entities

**Tech:** `U.ReferenceScheme` (kernel type), `ReferenceSchemeSlot` (SlotKind); `referenceScheme? : U.ReferenceScheme`.
**Plain:** *reference scheme*, *interpretation scheme*, *description scheme*.

**Intent.** Separate **what is being said** (ClaimGraph) from **how claims are read as statements about entities and contexts** (designation, measurement, evaluation envelopes), without reifying the referents themselves as a vertex.

**Normative definition.**

1. `U.ReferenceScheme` is a **component type of epistemes**, not an external object:

   * it determines how nodes of `U.ClaimGraph` are mapped to **properties/relations** over values of `DescribedEntitySlot`,
   * it specifies **measurement/evaluation templates** (how to test claims on `GroundingHolon`),
   * it fixes **claim-scope predicates / admissible regions** over declared `U.ContextSlice` selectors (and, where needed, references to domain spaces used inside those selectors).
2. `ReferenceSchemeSlot` is a **SlotKind** with:

   * **ValueKind** `U.ReferenceScheme`,
   * **no RefKind in the minimal core** (ReferenceSchemes are stored by value as `referenceScheme? : U.ReferenceScheme` fields on episteme cards/views).
     Discipline packs **may** introduce `U.ReferenceSchemeRef` as a **RefKind**, but **must not** repurpose it as a new ValueKind.
3. `ReferenceScheme` is the place where the legacy “Object‑vertex” semantics now live:

   * it does **not** “contain” the described entity or grounding referent,
   * it carries the **rules** that tie claims to entities and groundings.

**Didactic cue.**
“Ask: *Given this ClaimGraph, how exactly do we treat it as talking about these entities in these contexts, and how do we test it?* That is the ReferenceScheme.”

##### C.2.1:4.1.7 - Minimal node set and extension C.2.1+

The **minimal `U.EpistemeSlotGraph` core** for C.2.1 consists of positions (the episteme core SlotKinds of A.6.5 CC‑A.6.5‑5):
* `DescribedEntitySlot` (ValueKind `U.Entity`),
* `GroundingHolonSlot` (ValueKind `U.Holon`),
* `ClaimGraphSlot` (ValueKind `U.ClaimGraph`),
* `ViewpointSlot` (ValueKind `U.Viewpoint`),
* `ViewSlot` (ValueKind `U.View`),
* `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`).

This pattern **only fixes these positions**.
The **extension C.2.1+** (second step of the refactor) adds:
* `U.RepresentationScheme` and `RepresentationSchemeSlot`,
* `U.RepresentationToken` and `RepresentationTokenSlot`,
* `U.PresentationCarrier` and `PresentationCarrierSlot`,
* `U.RepresentationOperation` and `RepresentationOperationSlot` (with inference regime annotations),

without changing:
* the definition of `U.EpistemeKind`,
* the minimal `U.EpistemeCard` interface,
* or the assumptions A.6.2–A.6.4 / E.17.* make about episteme components.

In C.2.1+ `U.PresentationCarrier`, `U.Surface`, MVPK face, carrier, and rendering relations remain **publication-side carriers, surfaces, faces, or rendering relations**, not semantic parts of the episteme:
`U.PresentationCarrier` values are linked to `U.Episteme` and `U.View` via MVPK and L-SURF relations, such as `isCarriedBy` and MVPK face relations, and **MUST NOT** be counted as components when reasoning about episteme identity, DescribedEntitySlot occupancy, GroundingHolonSlot occupancy, or KD-CAL morphisms. Changing carriers or surfaces alone **never** changes the `U.Episteme` instance determined by C.2.1; it only produces `U.Work` occurrences that publish or republish the same `U.Episteme`.

##### C.2.1:4.1.8 - Attached epistemic structures (non-slot components)

`U.EpistemeSlotGraph` deliberately does **not** reify every episteme-adjacent structure as a node. Several key structures remain **attached, non-slot components** of `U.Episteme`:
* **`JustificationGraph`** — the argument/evidence graph for nodes of `U.ClaimGraph` (A.10/B.3).
* **`EvidenceBindings`** — per-claim `U.EvidenceRole` assignments that connect claims to external `U.Work` and carriers.
* **`EditionSeries`** — the `PhaseOf` chain of episteme editions (A.14) with change-class annotations (symbol-only vs ClaimGraph vs ReferenceScheme changes).
* **`ScopeCard` and `U.ClaimScope`** — USM scope objects (A.2.6) describing where the episteme's claims hold.

These attached structures are **not extra positions** of `U.EpistemeSlotGraph`; they hang off the `U.ClaimGraph` and `U.ReferenceScheme` pair and are governed by KD-CAL (C.2), A.10, and B.3. C.2.1 only requires that an episteme which participates in KD-CAL exposes them in a way that keeps **ClaimGraph, ReferenceScheme, Evidence, EditionSeries, and `ClaimScope`** clearly distinguishable.

#### C.2.1:4.2 - Episteme as n‑ary relation and as holon

To prevent confusion between **described entities**, their **descriptions**, and the **slots they occupy in an episteme**, C.2.1 explicitly treats epistemes both as:

1. **n‑ary relations with a signature** (slots & values), and
2. **holons with components** (fields & parts).

##### C.2.1:4.2.1 - `U.EpistemeKind` — episteme as a typed n‑ary relation

**Tech:** `U.EpistemeKind` (kernel type).

**Intent.** Provide a **signature‑level** description of an episteme as an n‑ary relation whose arguments are governed by `SlotKind`/`ValueKind`/`RefKind` triples per A.6.5.

**Normative definition.**

1. Every episteme that participates in KD‑CAL **belongs to some `U.EpistemeKind`**.
   The kind determines:

   * which **SlotKinds** appear (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`, …),
   * the **ValueKind** for each slot (always a subtype of `U.Type`),
   * the **RefKind** used to store it in episteme (when applicable).
1. `U.EpistemeKind` is a **special case** of `U.Signature` (A.6.0), with its slots governed by `U.RelationSlotDiscipline` (A.6.5). C.2.1 **MUST NOT** define an alternative slot discipline.
2. For the minimal core, every `U.EpistemeKind` **MUST** include:
   * exactly one `ClaimGraphSlot`,
   * at least one `DescribedEntitySlot`,
   * and at least one `ReferenceSchemeSlot`.
     Inclusion of `GroundingHolonSlot`, `ViewpointSlot`, `ViewSlot` **MAY** be species‑level constraints (mandatory for D/S‑epistemes, optional for others).

**Didactic cue.**
“An `EpistemeKind` is the *type* of episteme: which positions it has and what can go into them.”

##### C.2.1:4.2.2 - `U.EpistemeTuple` — episteme as filled n‑ary relation

**Tech:** `U.EpistemeTuple` (kernel species).

**Intent.** Model **filled instances** of an episteme’s signature, separating the n‑ary relation from any particular holonic packaging or publication.

**Normative definition.**

1. `U.EpistemeTuple` is a species whose instances are **pure value tuples**:
   * for each SlotKind in the associated `U.EpistemeKind`, a value of the slot’s **ValueKind** (or a reference value of **RefKind**, if the kind is configured as such).
2. `U.EpistemeTuple` is **notation‑agnostic** and **carrier‑agnostic**: it does not know about files, formats, or surfaces.
   It exists to give A.6.2–A.6.4 a minimal notion of “episteme as a point in Ep”.
3. In episteme, `U.EpistemeTuple` rarely appears directly; it is typically **induced** by `U.EpistemeCard` and `U.EpistemeView` (which add component structure and meta‑information).

**Didactic cue.**
“An `EpistemeTuple` is the abstract record of *what fills which slots* — nothing more.”

##### C.2.1:4.2.3 - `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` — holonic realisations

**Tech:** `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` (species of `U.Episteme`).

**Intent.** Provide **holon‑level structures** that engineers can work with (components, mereology, provenance), while keeping them aligned with `U.EpistemeKind` and `U.EpistemeTuple`.

**Normative definition.**

1. **`U.EpistemeCard`.**
   A species of `U.Episteme` whose components correspond one‑to‑one to slots of some `U.EpistemeKind`:
   * `content : U.ClaimGraph` (for `ClaimGraphSlot`),
   * `describedEntityRef : U.EntityRef` (for `DescribedEntitySlot`),
   * `groundingHolonRef? : U.HolonRef` (for `GroundingHolonSlot`),
   * `viewpointRef? : U.ViewpointRef` (for `ViewpointSlot`),
   * `referenceScheme? : U.ReferenceScheme` (for `ReferenceSchemeSlot`),
   * optionally `representationSchemeRef? : U.RepresentationSchemeRef` (C.2.1+),
   * `meta : Edition/Provenance/Status…`.
     Minimal episteme identity is the pair `⟨content, describedEntityRef⟩` within a `U.BoundedContext`; all other fields are optional at the genus level but may be mandatory in species. Changes that alter `content` or the effective `referenceScheme` (or that intentionally re-identify `describedEntityRef`) **SHALL** be realised as new phases in an `U.EditionSeries` (PhaseOf chain) under A.14 and A.7. Changes confined to `U.PresentationCarrier`, `U.Surface`, MVPK face, carrier, or rendering relations **do not** create a new episteme; they are captured as publication work over the same `U.Episteme`.
2. **`U.EpistemePublication`.**
   A species representing **epistemes that have been published** onto surfaces (MVPK). It:
   * has at least the components of `U.EpistemeCard`,
   * plus references to MVPK `U.View`, face identity, `PublicationSurface` and `InteropSurface` `SurfaceKind` values, publication-scope fields, profile fields, and external carrier or rendering refs as required by E.17 and L-SURF,


   * but **does not** re-interpret face labels, `SurfaceKind` values, or carriers/renderings as parts of the episteme; carriers remain external.


3. **`U.EpistemeView`.**
   As defined in §4.1.5, a species of `U.Episteme` representing a **view** under a specific `U.Viewpoint`.
   Its components are a specialisation of `U.EpistemeCard`:
   * ClaimGraph often restricted/projection of a base description/specification,
   * Viewpoint fixed,
   * ReferenceScheme tailored to that viewpoint.

**Alignment requirement.**
For any of these species, the pattern **MUST** state explicitly:
* which `U.EpistemeKind` it realises, and
* how each component maps to a SlotKind/RefKind under `U.RelationSlotDiscipline`.

This ensures that A.6.2–A.6.4 can treat any `U.Episteme*` uniformly as both:
* an object in the category **Ep**, and
* a structured holon with components.

##### C.2.1:4.2.3a - Episteme, publication, view, carrier, cue, and authority-reference lanes  *(normative)*

C.2.1 is the default FPF pattern for claim-bearing units. Do not mint a generic `U.SemioObject`, `U.SemioticObject`, `U.SignObject`, `U.WorkingObject`, or `U.SourceMaterial` when the object in question is a claim-bearing unit. Use `U.Episteme` or a declared species of `U.Episteme`.

When the same claim-bearing unit is available to readers, tools, or downstream work as a published episteme, name that lane as `U.EpistemePublication` or as a governed `U.Episteme` publication. Then keep the adjacent lanes separate:

* **publication form** — the concrete form in which the episteme is made available for some use, such as a cue pack, transfer-prepared claim set, prompt form, partial normal form, record, card, table, or profile;
* **view, including MVPK face** — `U.View` or `U.EpistemeView` under a declared `U.Viewpoint`, including MVPK faces such as `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane`;
* **carrier or rendering** — the SCR/RSCR, document, dashboard, generated screen, trace file, transport envelope, or display that bears or renders a publication;
* **source-finding cue** — a badge, tile, heading, signature-looking mark, credential display, generated explanation, or other cue that helps find a source but does not by itself create an authority-reference relation;
* **governing pattern reference and authority-reference field** — `governingPatternRef` when one FPF pattern governs admissible interpretation or use; `authoritySourceRef` when a non-pattern `authoritySourceRef` target such as an external standard, editioned register, DRR, gate decision, policy source, or role-assignment or status register carries the relevant authority. The publication records this reference; it does not become the referenced authority.

No publication form, view, face, carrier, rendering, source-finding cue, dashboard signal, credential display, generated explanation, FPF pattern file, or FPF pattern section is itself a substitute for a governed `U.Episteme`, an evidence relation, an assurance claim, a gate decision, a permission, a role claim, a status claim, or a `U.Work` occurrence. If the next move concerns work, keep candidate reliance, `U.WorkPlanning`, planned work, actual `U.Work`, work result, and work-result measurement in their own P2W lanes rather than storing them inside the episteme or its carrier.

##### C.2.1:4.2.4 - SlotKind / ValueKind / RefKind discipline for DescribedEntity & GroundingHolon


C.2.1 adopts **A.6.5 `U.RelationSlotDiscipline`** wholesale. For the two key positions:
1. **DescribedEntitySlot.**
   * `SlotKind = DescribedEntitySlot`;
   * `ValueKind = U.Entity` (species may constrain to `EoIClass ⊑ U.Entity`);
   * `RefKind = U.EntityRef` (or a species thereof);
   * normative field name in episteme cards: `describedEntityRef : U.EntityRef`.
     No kernel type named `U.DescribedEntity` is introduced; the phrase “described entity” always means “an instance of `U.Entity` in the role filling `DescribedEntitySlot`”.
1. **GroundingHolonSlot.**
   * `SlotKind = GroundingHolonSlot`;
   * `ValueKind = U.Holon`;
   * `RefKind = U.HolonRef`;
   * normative field name: `groundingHolonRef? : U.HolonRef`.
     There is no kernel type `U.GroundingHolon`; “grounding holon” is a **slot occupant name**.
Any episteme that previously mixed slot/value/ref concepts (e.g., using `DescribedEntityRef` as if it were a type) **MUST** be migrated to this discipline over time; C.2.1 provides the normative anchor, and F.18 / discipline packs provide the migration guide.

#### C.2.1:4.3 - Minimal epistemic morphisms (informal schema)

> **Note.** The full mathematical treatment (categories Ep and Ref, describedEntity functor `α : Ep → Ref`, and effect‑free morphisms) lives in A.6.2–A.6.4. Here we fix only the **episteme-slot relations** that C.2.1 expects to exist between its positions.

At the level of `U.EpistemeCard` components and SlotKinds, we assume the following **primitive relations** (not all are functions):

1. **`describedEntitySet : U.Episteme → P(U.Entity)`**
   *derivable from `DescribedEntitySlot` and `ReferenceScheme`*
   * For an episteme `E`, `describedEntitySet(E)` is (at least) the singleton containing the entity referenced by `describedEntityRef(E)`; in more complex cases, it may be a finite set or bundle of entities, determined by `ReferenceScheme`.
   * The **functorial DescribedEntity mapping** `δ_E : Ep → Ref` used in A.6.2–A.6.4 is the categorical lift of this relation: it forgets episteme internals and keeps only the described entity in the ReferencePlane determined by the pair `<DescribedEntitySlot, GroundingHolonSlot>`.

2. **`grounds : (U.Entity, U.Holon) ⇝ GroundingRelation`**
   *relates described entities to grounding holons*
   * Captures how values of `DescribedEntitySlot` are **situated** in holons that make evaluation possible (labs, infrastructures, organisations).
   * Need not be total or functional; an entity may admit multiple grounding holons, or none.

3. **`designates : (U.ReferenceScheme, U.ClaimGraph, U.Entity, U.Holon) ⇝ DesignationProfile`**
   *how claims are read as statements about entities in contexts*
   * Specifies, for each claim in `content` and each `<describedEntityRef, groundingHolonRef>`, what property/relation it purports to state, and under what conditions.

4. **`satisfies / evaluatesTo : (U.ClaimGraph, U.ReferenceScheme, U.Holon) → TruthProfile/SuccessProfile`**
   *evaluation of claims under a reference scheme and grounding*
   * Forms the bridge to KD‑CAL’s `F, G, R` evaluation; details are given in C.2 and B.3.

5. **View-related morphisms** (to be connected with A.6.3):
   * `viewProject : (U.Episteme, U.Viewpoint) → U.View`
     — effect-free, **DescribedEntity-preserving** projection that slices `ClaimGraph` and specialises `ReferenceScheme` under a given viewpoint.
   * `viewEmbed : U.View → U.Episteme`
     — embedding of a view back into the wider episteme, typically as a reference with correspondence proofs.

5. **Reflexive describedEntity guard.**
   When `DescribedEntitySlot` or `ReferenceScheme` picks out an episteme or claim that includes the referring claim itself (**ReferencePlane = episteme**), publishers **SHALL** ensure that the induced justification/evaluation structure is **acyclic per evaluation chain**: reflexive describedEntities may exist as literature handles, but they MUST NOT form a minimal support cycle for acceptance or KD‑CAL assurance. Self‑reference is allowed as a citation pattern, not as a way to close justification loops.

These are **not yet laws**; they are the **hooks** that A.6.2–A.6.4 will formalise into:
* `U.EffectFreeEpistemicMorphing` (Ep→Ep morphisms over this structure),
* `U.EpistemicViewing` (describedEntity‑preserving Ep→Ep),
* `U.EpistemicRetargeting` (describedEntity‑retargeting Ep→Ep).

### C.2.1:5 - Legacy semantic triangle as didactic view  *(informative)*

**Position.** The classical semiotic or semantic triangle (“Symbol–Concept–Object”, Ogden–Richards/Frege–Carnap style) is **not** the normative ontology for epistemes in FPF. For `U.Episteme`, it is treated as a **didactic projection** of the richer hypergraph `U.EpistemeSlotGraph`:
* **“Symbol” corner** ≈ {`U.RepresentationToken`, `U.RepresentationScheme`, `U.PresentationCarrier`} when C.2.1+ is in use; in the minimal core this is collapsed into whichever external carrier bears the `U.ClaimGraph` publication.
* **“Concept” corner** ≈ `U.ClaimGraph` + `U.ReferenceScheme` under a chosen `U.Viewpoint`. This is the intensional content plus its interpretation recipe.
* **“Object” corner** ≈ the occupant of `DescribedEntitySlot` (ValueKind `U.Entity`) plus the occupant of `GroundingHolonSlot` (ValueKind `U.Holon`) and the grounding relation between them.

Under this reading the triangle is a **three‑node quotient** of the `U.EpistemeSlotGraph`:
```
(Symbol)      = RepresentationToken + Scheme + Carrier
(Concept)     = ClaimGraph + ReferenceScheme (+ Viewpoint)
(Object)      = DescribedEntity + GroundingHolon
```

All **viewpoints, operations, carriers and reference planes** are suppressed in the classical diagram. The cost of this suppression is precisely the confusion that motivates C.2.1:
* describing becomes a single unlabeled arrow,
* inference regimes disappear,
* measurement and grounding are invisible.

**Didactic use.** C.2.1 allows the triangle **only** in the following cases:
1. As an **introductory picture** in guidance material (“this is the coarse triangle; the actual pattern is the episteme slot graph”).
2. As a **quotient diagram**: an explicit note that “this figure ignores viewpoint, grounding, carrier, and operationality; see C.2.1 for the full structure”.
3. As a **legacy alignment aid** when mapping to standards or literature that speak only in triangle terms.

**Guard.** Any pattern or documentation page that uses a “semantic triangle” diagram **MUST** either:
* explicitly state “this is a didactic projection of C.2.1 `U.EpistemeSlotGraph`”, or
* treat it as a legacy reference when aligning with external standards.

The triangle **MUST NOT** be used as a kernel‑level ontology or as a basis for morphism laws. All normative reasoning about epistemes proceeds via the slots and components of `U.EpistemeSlotGraph`.

### C.2.1:6 - Interaction with I/D/S and DescriptionContext  *(normative)*

C.2.1 is the **episteme‑layer carrier** that I/D/S discipline (A.7, E.10.D2) relies on. The link is made via `DescriptionContext`.

#### C.2.1:6.1 - DescriptionContext over C.2.1 components

For any episteme that is a **Description** or a **Specification** in the sense of E.10.D2, the field `subjectRef : U.SubjectRef` is interpreted as a **DescriptionContext triple**:
```
DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩
```

where:
* `DescribedEntityRef : U.EntityRef` — occupies `DescribedEntitySlot` (ValueKind `U.Entity`, species often constrained via EoIClass ⊑ `U.Entity`).
* `BoundedContextRef : U.BoundedContextRef` — points to the context that fixes vocabulary, units, and legal inferences for this description (E.10.D1).
* `ViewpointRef : U.ViewpointRef` — occupies `ViewpointSlot` (ValueKind `U.Viewpoint`) and determines which concerns, role‑enactor families, and conformance rules apply.

**Normative requirement (IDS‑13).**
For every `…Description` / `…Spec` episteme:
1. `subjectRef` **SHALL** be decodable to a well‑formed DescriptionContext triple.
2. `DescribedEntityRef` from that triple **SHALL** be identical to the field `describedEntityRef` that fills `DescribedEntitySlot` in the corresponding `U.EpistemeCard`/`U.EpistemeView`.
3. `ViewpointRef` in DescriptionContext **SHALL** agree with `viewpointRef` in the episteme card or be uniquely derivable from a `U.ViewpointBundle` in E.17.1 (with the derivation rule documented).

Intensions (I‑layer) such as `U.System`, `U.Method`, `U.Role` **do not** inhabit C.2.1 directly; they are the *targets* of I→D operations (`Describe_ID`) and appear as values of `DescribedEntitySlot` in resulting descriptions/specs.

#### C.2.1:6.2 - I→D and D→S morphisms over C.2.1

* **Describing (`Describe_ID : I → D`).**
  Produces an episteme whose:
  * `content : U.ClaimGraph` encodes the descriptive claims about the intension,
  * `describedEntityRef` points to the intension’s entity,
  * `groundingHolonRef` (if present) fixes where the description is evaluated or tested,
  * `viewpointRef` selects the describing viewpoint.

  `Describe_ID` is **conformant** to A.6.2 but not an Ep→Ep morphism (domain is Intension, codomain is Episteme). C.2.1 provides the **codomain schema** and ensures that the resulting Description has a valid DescriptionContext.

* **Specifying/Formalising (`Specify_DS/Formalize_DS : D → S`).**
  Takes a Description episteme and returns a Specification episteme with:
  * the same `describedEntityRef`,
  * the same `BoundedContextRef` and `ViewpointRef` (hence same DescriptionContext),
  * a `content : U.ClaimGraph` that raises formality F (F≥4) and adds test harness hooks, but is conservative with respect to the underlying intension.

  As an Ep→Ep morphism, `Specify_DS` is a **species of A.6.2** and must obey the invariants over the C.2.1 slots (DescribedEntityChangeMode = preserve; no change to DescribedEntity; ClaimGraph refinement only).

C.2.1 does **not** define I/D/S; it only insists that any `…Description`/`…Spec` species that claims to respect I/D/S discipline must:
* implement `U.EpistemeCard` or `U.EpistemeView` **with** `content`, `describedEntityRef`, `groundingHolonRef?`, `viewpointRef?`, and `referenceScheme?` fields, and
* wire these fields into `subjectRef` as DescriptionContext.

### C.2.1:7 - Alignment with A.6.2–A.6.4 (episteme morphisms)  *(normative)*
`U.EpistemeSlotGraph` is the **object‑level substrate** for the episteme morphism patterns:
* A.6.2 `U.EffectFreeEpistemicMorphing`
* A.6.3 `U.EpistemicViewing`
* A.6.4 `U.EpistemicRetargeting`

#### C.2.1:7.1 - Effect‑free episteme morphisms (A.6.2) over C.2.1
For any `f : X → Y` that is an instance of `U.EffectFreeEpistemicMorphing`:
* **Typed objects.**
  X and Y are `U.Episteme` instances realised as `U.EpistemeCard` / `U.EpistemeView` with at least the minimal core components:

  ```
  content            : U.ClaimGraph
  describedEntityRef : U.EntityRef      // DescribedEntitySlot
  groundingHolonRef? : U.HolonRef       // GroundingHolonSlot
  viewpointRef?      : U.ViewpointRef   // ViewpointSlot
  referenceScheme?   : U.ReferenceScheme// ReferenceSchemeSlot (ByValue)
  ```

  Any additional C.2.1+ components (RepresentationScheme, Tokens, Carriers, Operations) are visible to A.6.2 only through their declared SlotKinds (A.6.5).
* **DescribedEntityChangeMode characteristic.**
  `f` **MUST** declare a **`describedEntityChangeMode ∈ {preserve, retarget}`**:
  * `preserve` — `describedEntityRef(Y) = describedEntityRef(X)` and any change to `groundingHolonRef`/`viewpointRef` must be justified by Bridges/CorrespondenceModel, without changing the DescribedEntitySlot value;
  * `retarget` — permitted only for A.6.4 species; see below; in this case the characteristic records an intentional change in the pair `<describedEntityRef, groundingHolonRef>` under a declared `KindBridge` in the appropriate ReferencePlane.

  This **DescribedEntityChangeMode** is a CHR-style *characteristic* (A.17) on episteme morphisms, which points directly to `DescribedEntitySlot`. Avoid introducing a separate “describedEntity” term alongside `DescribedEntity`.

* **Component discipline.**
  P0–P5 from A.6.2 are read **directly** in terms of C.2.1 components:
  * purity ⇒ only C.2.1 components of Y may change; no Work/Mechanism side‑effects;
  * conservativity ⇒ claims in `content_Y` read via `referenceScheme_Y` about the new `<DescribedEntity, GroundingHolon>` do not go beyond what already follows from `content_X` via `referenceScheme_X` under the declared DescribedEntityChangeMode and Bridges;
  * functoriality ⇒ composition of such transformations respects the slot structure and ReferenceSchemes.

Any Ep→Ep pattern that operates on `U.Episteme` **MUST** state which C.2.1 slots it reads and which it may write, in terms of SlotKinds/ValueKinds/RefKinds (A.6.5), and then declare itself a species of A.6.2/3/4 as appropriate.

#### C.2.1:7.2 - EpistemicViewing (A.6.3) as describedEntity‑preserving projections

`U.EpistemicViewing` is the **DescribedEntity-preserving** species of A.6.2. Over C.2.1 this means:
* `describedEntityRef(Y) = describedEntityRef(X)` — the same value in `DescribedEntitySlot`.
* `groundingHolonRef` is preserved, or changed only within a fixed grounding context (e.g. normalising identifiers for the same lab or runtime).
* `viewpointRef` is either:
  * preserved (internal normalisation under the same viewpoint), or
  * replaced by another `U.ViewpointRef` *within* a `U.MultiViewDescribing` family (E.17.0), with invariants enforced by a CorrespondenceModel.
* `content` and `referenceScheme` are transformed **conservatively**: no new intensional claims about the same DescribedEntity are introduced.

Typical examples:
* filtering or aggregating `U.ClaimGraph` to a view relevant for a stakeholder group;
* rendering a behavioural specification into a tabular or diagrammatic episteme under a publication viewpoint;
* normalising a logic‑heavy episteme into a more operational one, while keeping the same described system and context.

In terms of SoTA, EpistemicViewing behaves like a **lens** or **optic** over C.2.1: a focus (SlotKinds for content/representation) is manipulated while the DescribedEntity is fixed.

#### C.2.1:7.3 - EpistemicRetargeting (A.6.4) as DescribedEntity-bundle retargeting on episteme morphisms

`U.EpistemicRetargeting` is the species of A.6.2 where **`describedEntityChangeMode = retarget`**.
It is always a **morphism between epistemes** (`f : X → Y` in `U.Episteme`), but the adjective “retargeting” refers **not** to the fact that an episteme is mapped to another episteme (this is true for all A.6.2 species), and **not** to a separate describedEntity, but specifically to the **change in the DescribedEntity-bundle** selected by C.2.1:
* `describedEntityRef(Y) ≠ describedEntityRef(X)` — the value stored for `DescribedEntitySlot` changes;
* a `KindBridge` must relate `Kind(describedEntityRef(X))` and `Kind(describedEntityRef(Y))`;
* `groundingHolonRef` may remain the same (e.g. same plant, different subsystem) or be transformed along a Bridge in the same ReferencePlane.

In practice, many retargetings operate on the **target bundle** `<DescribedEntitySlot, GroundingHolonSlot>` (for example, when an episteme about a physical module is re-interpreted as an episteme about a function-holon realised in a different environment). The characteristic `describedEntityChangeMode` still classifies such morphisms by whether this bundle is preserved or intentionally re-identified under a `KindBridge` and reference-plane policy; the episteme on the codomain side is just the usual A.6.2 target episteme.


Over C.2.1 this is used for:
* **functional vs structural reinterpretation** (e.g. an episteme about a physical module retargeted to an episteme about the function it realises; StructuralReinterpretation in E.TGA becomes a species of A.6.4);
* **signal vs spectrum** transitions (Fourier-style moves where the `DescribedEntitySlot` value changes from time-domain signal to frequency-domain representation but an invariant, such as energy, is preserved);
* **data vs model** transitions (e.g. retargeting an episteme about raw observations to an episteme about a learnt model, with an invariant such as likelihood or sufficient statistics).

C.2.1 ensures that these retargetings have a **clear source `DescribedEntitySlot` value and target `DescribedEntitySlot` value** and that any such move is expressed as a morphism over well‑typed slots, not as an unstructured rewrite of “subject” or “object” labels.

### C.2.1:8 - Alignment with E.17.* (Multi‑View Describing & Publication)  *(normative)*

`U.EpistemeSlotGraph` underpins the E.17 cluster:
* E.17.0 `U.MultiViewDescribing`
* E.17.1 `U.ViewpointBundleLibrary`
* E.17.2 `TEVB — Typical Engineering Viewpoints Bundle`
* E.17 `MVPK — Multi‑View Publication Kit`

#### C.2.1:8.1 - Multi‑View Describing (E.17.0)

`U.MultiViewDescribing` organises **families of descriptions/specifications** over a shared entity‑of‑interest:
* The **EoIClass** parameter of E.17.0 is a species constraint on the ValueKind of `DescribedEntitySlot` (`EoIClass ⊑ U.Entity`).
* Each member of a multi‑view family is a `…Description`/`…Spec` episteme with:
  * `describedEntityRef` into that EoIClass,
  * `viewpointRef` drawn from a `U.ViewpointBundle`,
  * `subjectRef` decoding to DescriptionContext.

Within this pattern:
* `U.Viewpoint` is **exactly** the ValueKind of `ViewpointSlot` in C.2.1.
* `U.View` is `U.EpistemeView`, a species of `U.Episteme` whose `content` is already restricted to a particular `U.Viewpoint` and often also to a particular `U.RepresentationScheme`.

C.2.1 thus supplies the **per‑episteme** structure that E.17.0 rearranges into multi‑view families.

#### C.2.1:8.2 - Viewpoint bundles (E.17.1/E.17.2)

`U.ViewpointBundleLibrary` and TEVB specialise the `U.Viewpoint` node:
* A ViewpointBundle is a **set of `U.Viewpoint` instances** tailored to a class of DescribedEntities (e.g., holons in engineering contexts).
* TEVB fixes `EoIClass = U.Holon` (typically `U.System` or `U.Episteme`) and provides canonical engineering viewpoints: functional, structural, role‑enactor, interface‑oriented, etc.

From the C.2.1 perspective:

* these bundles populate the ValueKind of `ViewpointSlot`;
* engineering episteme species that want to be “TEVB‑aligned” must restrict `viewpointRef` to TEVB’s `EngineeringVPId` set, while keeping the same DescribedEntitySlot discipline.

#### C.2.1:8.3 - MVPK (E.17) as publication over C.2.1 views

MVPK treats `U.View` (i.e. `U.EpistemeView`) as its primary input:
* it uses `U.EpistemicViewing` species (A.6.3) to generate publication‑oriented views from engineering or logical views;
* it then publishes these `U.View` epistemes as `U.Surface` values with declared publication viewpoints and faces.

C.2.1’s distinction between:

* `U.Viewpoint` (intensional, epistemic perspective) and
* `U.PresentationCarrier` (carrier in C.2.1+ and L-SURF)

keeps **epistemic perspective and physical medium separate**:
* MVPK operates on `U.View` epistemes and then on carriers;
* the same View can be realised on multiple carriers without changing its describedEntity or ClaimGraph.

Any MVPK species that claims to be C.2.1‑conformant **MUST**:
* treat `U.View` as a `U.EpistemeView` with a valid C.2.1 core,
* document which C.2.1 slots it reads/writes (typically only representation/carrier‑related ones, leaving `DescribedEntitySlot` and `GroundingHolonSlot` untouched),
* refrain from introducing new claims about the described entity beyond what is in the source `U.View`’s ClaimGraph.

### C.2.1:9 - Bias‑annotation  *(informative)*

**Episteme‑first and pragmatics‑first.**
The pattern assumes that *nothing is a meaningful episteme* unless it is **about something for someone under some perspective**. This follows the pragmatic turn in semantics: describedEntity and concerns are not afterthoughts but part of the core structure. The graph is therefore built around slots for DescribedEntity, GroundingHolon, Viewpoint and ClaimGraph, not around abstract “propositions in the void”.

**Operational/representational bias.**
C.2.1+ anticipates that certain RepresentationSchemes are **operational** in Novaes’ sense (supporting direct syntactic inference, like pen‑and‑paper arithmetic or proof states) while others are **purely notational**. The pattern remains neutral on which schemes are used but bakes in a place for operations and carriers so that:

* symbol‑manipulating tools (SAT/SMT, proof assistants, classical programming languages),
* distributed/latent representations (LLM embeddings, latent protocols like “DroidSpeak”, “Coconut”‑style communication),
* hybrid ReAct‑style agent loops

can all be treated as different species operating over the same `U.EpistemeSlotGraph`. There is a bias towards making these operational differences **explicit** instead of hiding them behind “the model”.

**Viewpoint and stakeholder bias.**
The pattern leans on the ISO‑style idea that viewpoints encode **stakeholder concerns and role‑families**, but it generalises this beyond architecture. `U.Viewpoint` is intentionally intensional and not bound to any single discipline; still, the examples are skewed toward engineering and epistemic use‑cases.

**Didactic bias.**
The pattern is written to be teachable: semantic triangles are kept as didactic projections; examples like stools on lab rigs, services and SLAs, and model‑evaluation epistemes are deliberately simple. This may under‑represent more exotic epistemes (e.g. artistic, legal, or socio‑technical ones), but the intention is that these use the same slots with different species‑level constraints.

### C.2.1:10 - Conformance checklist  *(normative)*

**CC‑C.2.1‑1 - Minimal core components for episteme species.**
Any species of `U.Episteme` that participates in I/D/S discipline or in E.17 multi‑view/publishing **MUST** be representable as `U.EpistemeCard`/`U.EpistemeView` with at least:

```
content            : U.ClaimGraph
describedEntityRef : U.EntityRef
groundingHolonRef? : U.HolonRef
viewpointRef?      : U.ViewpointRef
referenceScheme?   : U.ReferenceScheme      // ByValue
meta               : …                      // edition, provenance, status (A.7/F.15)
```

and corresponding SlotSpecs consistent with A.6.5 (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`).

**CC‑C.2.1‑2 - No kernel type for “DescribedEntity” or “GroundingHolon”.**
Patterns **MUST NOT** introduce kernel types `U.DescribedEntity` or `U.GroundingHolon`:
* DescribedEntitySlot has ValueKind `U.Entity` ( species‑constrained via EoIClass if needed),
* GroundingHolonSlot has ValueKind `U.Holon`.

Plain terms “described entity” and “grounding holon” are allowed only as **role descriptions** of slot occupants.

**CC‑C.2.1‑3 - SlotKind/ValueKind/RefKind discipline.**
All episteme‑related slots, including `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot` (and any extensions in C.2.1+), **MUST**:
* follow the naming discipline of A.6.5 (`*Slot` for SlotKinds, `*Ref` only for RefKinds/fields),
* declare a ValueKind and refMode (`ByValue` or a RefKind),
* be used consistently across patterns that refer to the same conceptual position.

**CC‑C.2.1‑4 - DescriptionContext wiring.**
Any episteme species whose name or pattern claims to be a `…Description` or `…Spec` in the sense of E.10.D2 **MUST**:
* expose `subjectRef : U.SubjectRef`,
* provide a decoding to `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* ensure that `DescribedEntityRef` matches `describedEntityRef` (DescribedEntitySlot), and
* ensure that `ViewpointRef` matches `viewpointRef` or is derivable from a `U.ViewpointBundle` under documented rules.

**CC‑C.2.1‑5 - Morphism declarations over slots.**
Any pattern in A.6.2–A.6.4, E.17, E.TGA, or discipline packs that defines morphisms between epistemes **SHALL**:
* state whether it is a species of `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, or `U.EpistemicRetargeting`,
* declare its `describedEntityChangeMode` (preserve/retarget),
* name which SlotKinds it reads and writes,
* state its behaviour on `describedEntityRef`, `groundingHolonRef`, `viewpointRef`, and `referenceScheme`.

**CC-C.2.1-5a - Episteme/publication lane split for semio-facing terms.**
Any pattern, profile, support note, or FPF-facing term that uses pre-FPF sign vocabulary, explanation, publication, source cues, authority-looking cases, or reader reliance **MUST** name the claim-bearing value as `U.Episteme`, `U.EpistemePublication`, or a declared species of `U.Episteme`. When publication is live, it **MUST** separately name the publication form, `U.View` or MVPK face, carrier or rendering, source-finding cue, and either `governingPatternRef` or `authoritySourceRef` when interpretation or use depends on a named authority reference. It **MUST NOT** use generic semio wording, generic source wording, generic project-work wording, or container-placement wording as solution terms.

**CC‑C.2.1‑6 - Semantic‑triangle usage guard.**


If a semantic triangle or parallelogram diagram appears in a pattern or tutorial, there must be an explicit note that:
* it is a didactic projection of `U.EpistemeSlotGraph`, and
* normative laws are stated in terms of C.2.1 nodes and morphisms, not in terms of triangle corners.

**CC‑C.2.1‑7 - KD‑CAL / ReferencePlane alignment.**
Any pattern that evaluates or compares epistemes (KD‑CAL/LOG‑CAL, CHR, CG‑Spec, etc.) **MUST** point out:
* how `U.ClaimGraph` is interpreted in a ReferencePlane,
* how `GroundingHolonSlot` figures into measurement or validation,

**CC‑C.2.1‑8 - Context locality and Bridges.**
Any `U.Episteme` species that is consumed by KD‑CAL / LOG‑CAL / CHR‑based patterns **SHALL** declare a `U.BoundedContextRef`; all F–G–R computations and C.2.1 slot interpretations are **context‑local**.  Cross‑context use **MUST** proceed via an explicit Bridge with CL / Φ‑policy (F.9/B.3), with penalties routed to R‑lanes only; F and the slot structure from C.2.1 remain unchanged.

**CC‑C.2.1‑9 - Carriers and Work outside episteme content.**
C.2.1 **inherits** A.7 and A.12 separation obligations: `U.PresentationCarrier` values, `U.Surface` values, and `U.Work` occurrences **MUST NOT** be treated as parts of `U.Episteme` or as values of any SlotKind in `U.EpistemeSlotGraph`. Episteme content stays in `U.ClaimGraph` and `U.ReferenceScheme`; evidence enters only via `U.EvidenceRole` bindings that point to external `U.Work` occurrences and carriers (A.10 and B.3). Changing carriers or re-publishing work alone does **not** change the episteme determined by ⟨content, describedEntityRef, referenceScheme⟩ in its `U.BoundedContext`.

**CC‑C.2.1‑10 - Reflexive describedEntity guard.**
When an episteme uses C.2.1 to speak **about** another episteme (ReferencePlane = episteme), or about itself (self‑describing or meta‑specification cases), patterns **SHALL** ensure that the resulting JustificationGraph / evaluation chains are **acyclic** along support paths. Reflexive `describe` / citation edges may exist as literature anchors, but they MUST NOT form minimal support cycles for acceptance or KD‑CAL assurance decisions; the trust calculus MUST always bottom out in external evidence (`U.Work` with `U.EvidenceRole`) rather than in purely self‑referential claims.

### C.2.1:11 - Consequences  *(informative)*

**Benefits**
* **Single, extensible episteme core.**
  C.2.1 gives a small, stable set of positions (DescribedEntity, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme) and components (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) on which all higher‑level patterns depend. This avoids the proliferation of “epistemic objects” and “facets” with overlapping semantics.
**Transparent DescribedEntity & grounding discipline.**
  The pair (`DescribedEntitySlot`, `GroundingHolonSlot`) is no longer hidden inside ad-hoc “SubjectRef” fields or semantic triangles: both are explicit, typed slots. This makes retargeting, viewing and correspondence laws (A.6.2–A.6.4, E.17.0) easier to state and check.
* **Better fit for contemporary representation practice.**
  By distinguishing ClaimGraph, RepresentationScheme, Tokens, Carriers and Operations (in C.2.1+), the pattern matches contemporary SoTA views of notation and formalism:
  * formal languages as cognitive tools and de-semanticisation techniques (Novaes),
  * operational iconicity and medium‑sensitive reasoning (Krämer, Malafouris),
  * hybrid symbolic–neural workflows (e.g. ReAct, tool‑augmented LLMs, latent protocols).
  FPF can model both symbol‑heavy and latent‑heavy workflows without privileging either.
* **Uniform substrate for multi‑view description and publication.**
  MultiViewDescribing, viewpoint bundles (TEVB), and MVPK all land on the same episteme core. This avoids the current “views vs viewpoints vs faces” confusion and leaves “architecture” as a domain‑specific specialisation rather than a competing meta‑ontology.
* **Tooling alignment.**
  Slot discipline plus explicit episteme components map cleanly to implementation types (records, row‑typed schemas, effectful handlers). Tools can generate code, schemas or telemetry from episteme species without guessing what “subject”, “context” or “object” mean.

**Trade‑offs / costs**
* **More explicit structure.**
  Authors must declare slots, ValueKinds and references explicitly, and keep DescriptionContext consistent. This is more upfront work than writing ad‑hoc “Subject/Object” fields, but it pays off in substitution safety and cross‑pattern reuse.
* **Migration effort.**
  Legacy uses of “EpistemicObject”, “Facet”, “Subject”/“Object”, and raw `…Ref` fields will need refactoring into C.2.1 slots + A.6.5 SlotSpecs. Migration notes and aliasing can ease the transition, but mechanical cleanup will still be required.
* **Exposure of representation biases.**
  Being explicit about RepresentationSchemes and Operations may surface disagreements about which representations are “primary” in a team or discipline. C.2.1 does not resolve these disagreements; it only makes them visible and therefore debatable.

#### C.2.1:12 - Relations  *(overview)*

**Builds on**
* A.1 `U.Holon` — for treating episteme as a holon with components.
* A.6.0 `U.Signature` — for interpreting episteme kinds as n‑ary relations over slots.
* A.6.5 `U.RelationSlotDiscipline` — for SlotKind/ValueKind/RefKind discipline over episteme slots.
* A.7, E.10.D2 — for I/D/S discipline and the Interpretation of `subjectRef` as DescriptionContext.
* C.2 (KD‑CAL, LOG‑CAL) — for ClaimGraph semantics, ReferencePlanes, and Bridges.
* E.8, E.10 — for pattern authoring discipline and lexical guards.

* **Constrains**
* A.6.2–A.6.4 — by fixing the minimal episteme component set those morphisms operate on and by requiring an explicit **DescribedEntityChangeMode characteristic** (`describedEntityChangeMode ∈ {preserve, retarget}`) over `DescribedEntitySlot`/`GroundingHolonSlot`.
* E.17.0–E.17.2 — by specifying how `DescribedEntity`, `Viewpoint`, `View` and ReferenceSchemes are represented at episteme level.
* E.17 (MVPK) — by separating `U.View` (episteme) from `U.PresentationCarrier` (surface), and by requiring that publication morphisms be `U.EpistemicViewing` species over C.2.1‑conformant views.
* F.18 (LEX‑BUNDLE) — by providing the episteme‑specific name cards and guards for DescribedEntity/GroundingHolon/Viewpoint/View/ReferenceScheme and their SlotKinds.

**Used by**
* A.6.2 `U.EffectFreeEpistemicMorphing` — as the default episteme object structure for episteme‑to‑episteme transforms.
* A.6.3 `U.EpistemicViewing` — as the substrate for describedEntity‑preserving projections (views).
* A.6.4 `U.EpistemicRetargeting` — as the substrate for DescribedEntity-bundle retargeting transforms between epistemes (Ep→Ep with `describedEntityChangeMode = retarget`).
* E.17.0 `U.MultiViewDescribing`, E.17.1, E.17.2 — to organise families of D/S‑epistemes under Viewpoints and EoI classes.
* E.17 (MVPK) — to publish episteme views as surfaces.
* E.TGA — to interpret StructuralReinterpretation and other engineering projections as episteme morphisms over a well‑typed `U.EpistemeSlotGraph`.

Together, these relations make `U.EpistemeSlotGraph` the **single normative core** for thinking about epistemes, their DescribedEntity mapping, their representations, and their transformations across FPF.

### C.2.1:End

## C.2.2 - Reliability R in the F–G–R triad

> Reliability (R) is a conservative, evidence-bound warrant signal for a typed claim under an explicit claim scope (G). Cross-context reuse is **Bridge-only**: scope may be re-expressed via `translate(Bridge,·)` (often narrowing), while congruence penalties route to **R only**.

> **Type:** Architectural (A)
> **Status:** Stable

### C.2.2:1 - Problem frame

KD‑CAL asks a simple operational question: *“Where can I safely use this claim?”*
FPF answers with a minimal “epistemic location” built from three coordinates and one bridge qualifier:

* **F** (Formality) describes *how the claim is expressed* and how strongly it supports verification workflows (C.2.3).
* **G** (Claim scope) describes *where the claim is asserted to apply* as a set-like object (A.2.6).
* **R** (Reliability) describes *how strongly the claim is warranted* by linked evidence under that scope.
* **CL / CL^k / CL^plane** (Congruence Levels) describe *lossy transport* when claims are reused across contexts, kinds, or planes (B.3, C.3).
  CL values live on **edges/bridges** (not on the claim as a “4th coordinate”).

In practice, the triad is frequently used before it is made explicit:

* Authors implicitly “average” disparate evidence and report a single confidence.
* Teams treat higher formality (F) as if it automatically implies higher warrant (R).
* Scope growth is smuggled in through phrasing instead of explicit scope operators (A.2.6).
* Cross-context reuse occurs without explicit bridges and without routing congruence loss into R.

This pattern makes **R** explicit in KD‑CAL and fixes the **triad discipline** required by Kind‑CAL (C.3) and the Trust & Assurance calculus (B.3).

### C.2.2:2 - Problem

FPF needs a reliability coordinate that is:

1. **Auditable.** A reader can trace R to concrete evidence and see how reuse penalties were applied.
2. **Composable.** R can be propagated through claim graphs conservatively, without illegal scale arithmetic.
3. **Orthogonal.** R is not conflated with F (expression) or G (scope).
4. **Bridge-safe.** Any loss from transport across contexts/kinds/planes is explicit and affects **R only**.
5. **Minimal.** The solution does not introduce new core types or new face-kinds.

### C.2.2:3 - Forces

| Force                                         | Tension                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Single number vs multi-tradition evidence** | People want one scalar ↔ evidence comes from heterogeneous practices (proofs, tests, telemetry, expert review).    |
| **Rigor vs humility**                         | Claims need to be usable in decisions ↔ overconfident scores are dangerous and hard to unwind.                     |
| **Formal vs empirical warrant**               | Proof can be decisive in a formal theory ↔ real-world deployment requires empirical adequacy and drift management. |
| **Scope realism vs marketing scope**          | Narrow scopes raise R ↔ incentives push for broad statements with hidden preconditions.                            |
| **Reuse vs semantic loss**                    | Reuse is valuable ↔ reuse across contexts/kinds/planes is inherently lossy.                                        |
| **Toolability vs expressive freedom**         | A validator needs crisp rules ↔ authors want flexible narratives and domain nuance.                                |

### C.2.2:4 - Solution

#### C.2.2:4.1 - Canonical triad relation

**Definition DEF‑C2.2‑1 (Epistemic location).**
An epistemic location for a claim `c` is the tuple:

`Loc(c | K, S) = ⟨F(c), G(c), R_eff(c)⟩`

where:

* `F(c)` is Formality (C.2.3), treated as an **ordinal**.
* `G(c)` is Claim scope (A.2.6), treated as a **set-like scope object**.
* `R_eff(c)` is Effective reliability for `c`, treated as a **ratio-scale** scalar in `[0,1]` (or an **ordinal proxy** at **[M‑0/M‑1]**; see §4.5.A).
  `R_eff` is computed **pathwise** (DEF‑C2.2‑3): when more than one admissible justification path exists, publish multiple path records (PathId rows) and cite which PathId(s) a guard/decision consumed (see §4.8.A / G.6). Any collapse to a single scalar is an explicitly declared Γ‑policy (no implicit averaging).

A location is always understood *relative to* a bounded context and the assurance carriers used elsewhere in FPF:
* `K` is the declared `U.BoundedContext`.
* `S ∈ {design, run}` is the claim’s stance carrier (no DesignRunTag chimeras).
* `ReferencePlane` is declared where applicable; plane crossings apply `CL^plane` and penalize **R only**.
* When the claim is published on the Working‑Model surface, the author also declares `validationMode ∈ {postulate, inferential, axiomatic}` (E.14 / B.3).

**Mode-to-lane hint (informative).** `validationMode` sets the *default expectation* for which assurance lane carries the initial support load (B.3.3 or B.3.5).
It does **not** add a new characteristic and does **not** change the meaning of `R`:
* `axiomatic` → VA-dominant (constructive grounding or proof carriers); if `ReferencePlane=world`, LA may still be required.
* `inferential` → VA+TA-dominant (reasoned chain + typing/alignment assurance); LA is optional and scope-bound.
* `postulate` → LA-dominant (empirical validation with freshness/decay); VA is optional.
In all modes, **R remains warrant**, not ontological truth; “proof ⇒ R=1 in the world” is a category error.

**Profile note (informative; fold compatibility).** Some profiles treat empirical `R` as N/A for strictly **axiomatic** lines and use a tagged proxy `R_proxy := F` (`line=formal`) for folding, as an explicit proxy rather than an implicit “F⇒R” rule (B.1.3).

`⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do not draw “trajectories” in `⟨F,G,R⟩`.

#### C.2.2:4.2 - What Reliability R means in KD‑CAL

**Definition DEF‑C2.2‑2 (Reliability as warrant).**
`R` is a conservative, evidence-bound indicator of how strongly the claim “holds as stated” under its declared scope and context. It is interpreted as a *warrant strength*, not as truth.

**Prophylactic clarification.**

* A higher `R` means “the evidence and its relevance supports relying on this claim under this scope.”
* A higher `F` means “the claim’s form is amenable to higher-formality checking and wider reuse,” but does not itself imply the claim is warranted.
* A larger `G` means “the claim applies to more cases,” but does not itself imply the claim is warranted in those cases.

#### C.2.2:4.3 - Pathwise weakest-link propagation (series vs parallel)

KD‑CAL’s default Γ‑fold is **weakest‑link** on the *entailment spine* (the premises/lemmas actually needed), computed per justification path. It is conservative, monotone, and auditable.

**Definition DEF‑C2.2‑3 (Pathwise weakest-link fold).**
Let `P` be a justification path for claim `c`. Let `SpineClaims(P)` be the required supports on the entailment spine, and let `SpineBridges(P)` be the bridges actually traversed on that spine (scope bridges, kind bridges, plane/notation transports where applicable).

Define the raw warrant of the path as:

`R_raw(P) = min_{i ∈ SpineClaims(P)} R_eff(i)`

and compute the effective warrant of the path by applying congruence penalties (see §4.5 for policy shape):

`R_eff(P) = Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P)))`

**Spine discipline.** The `min` is taken over the *entailment spine* only (no satellites, no “nice-to-have” citations).

This matches the KD‑CAL propagation rule (C.2:4.3) and the Trust & Assurance skeleton (B.3): weakest-link on the spine, penalize only by the worst (lowest) congruence encountered on the path (no averaging).

**Parallel support (optional, declared).**
If the same claim `c` has multiple **independent** justification paths `{P_j}` (OR‑style support), the default is:

`R_eff(c) = max_j R_eff(P_j)`

Independence is recorded as an explicit note (e.g., separate rigs/datasets/proof lines), per CC‑C.2.2‑10 and the KD‑CAL composition rule (C.2:4.3).
If the “multiple paths” actually cover **different** scope slices, do not use `max` to hide weaker slices; instead publish distinct `G_path` (SpanUnion‑style coverage) and keep per‑path `R_eff` traceable (A.2.6 / C.2:4.3).

**Conflict detection (no averaging).**
If the evidence graph supports both `p` and `¬p` with overlapping scope, do **not** average. Separate by context/scope, or mark the claim **provisional** with explicit conflict edges until resolved.

#### C.2.2:4.4 - Congruence penalties route to R only (no silent widening)

Cross-context reuse and cross-kind reuse are treated as **transport with loss**, and loss is expressed as a penalty that reduces `R`.

**Invariant INV‑C2.2‑1 (R-only penalty routing).**
For any transport step that uses a bridge with a declared congruence level, the transported claim preserves its **F** value, re-expresses its scope via an explicit **scope translation** (`translate`) when needed, and only its **R** value is decreased by congruence penalties:

`F_out = F_in`
`G_out = translate(Bridge, G_in)`  *(identity only for within-context identity use; cross-context use is undefined without a Bridge)*
`R_out ≤ R_in`

Claim scope may be *re-expressed* by an explicit translation, but must not be silently widened:

`G_out = translate(Bridge, G_in)`  (may narrow / drop unmappable slices; never widen without an explicit ΔG)

**No implicit translation.** Translation between contexts never occurs implicitly: if the target context differs, an explicit Bridge (with declared CL and loss note) is mandatory; otherwise the reuse is non-conformant.
**No implicit translation.** Cross‑Context reuse is conformant only via an explicit Bridge (declared CL + loss note) and an explicit `translate(Bridge,·)`; see **CC‑C.2.2‑4**.

This invariant is why KD‑CAL guard macros and crossing bundles can be simple: transport never silently *widens* a claim; it either (i) translates/narrows scope explicitly, and/or (ii) reduces warrant.

`translate` is the USM operator (A.2.6). It may drop unmappable slices and may include refit-like normalization; **this is not a penalty**. Any further narrowing is an explicit Δ‑move (ΔG−) under A.2.6. Congruence loss (CL/CL^k/CL^plane) still routes to **R only**.

**Notation/plane transports.** NotationBridge and plane transports contribute to the relevant `CL*_min(P)` bottlenecks for the path; they do not “lower F” by penalty. If an author actually rewrites a claim into a different formality level, that is a new episteme (ΔF), not “transport”.

#### C.2.2:4.4.A - Worked micro-example: `translate(G)` + penalty (A.2.6:12.2)

**Source context:** `MaterialsLab@2026`. Claim:

> `c:` “Adhesive X retains ≥85% tensile strength on Al6061 for 2 h at 120–150 °C.”

* `G_src := {substrate=Al6061, temp∈[120,150]°C, dwell≤2h, Γ_time=window(1y), rig=Calib‑v3}`
* `Loc_src(c) = ⟨F_src, G_src, R_raw⟩`

**Target context:** `AssemblyFloor@EU‑PLANT‑B`. Reuse requires a declared Bridge `b`:

* Bridge `Bridge#MatLab_to_PlantB` maps lab rig → plant rig and introduces a measurement correction; `CL(Bridge#MatLab_to_PlantB)=2` with loss note “±2 °C bias.”
* **Scope translation:** `G_tgt := translate(b, G_src)` which (in this case) narrows the temperature span to `[122,148]°C` due to the correction.
* **Penalty routing:** using policy `Φ=Φ_v1`, compute
  `R_eff := max(0, R_src − Φ_v1(CL(Bridge#MatLab_to_PlantB)))`.

**Key point:** `G` changed only because `translate(b,·)` explicitly re-expressed the *same entitlement* in the target Context’s slice vocabulary; the **congruence loss** still affects **R only**. If authors decide that only `[125,145]°C` is safe to claim on the floor, that is an explicit **ΔG−** decision (scope edit), not a congruence penalty.

#### C.2.2:4.5 - Effective reliability under transport (policy-defined, monotone, bounded)

When a claim is reused via bridges, `R_eff` is computed by applying penalties determined by congruence levels.

**Definition DEF‑C2.2‑4 (Effective reliability under transport).**
Let:

* `CL` be the congruence level of a scope bridge (B.3).
* `CL^k` be the congruence level of a kind bridge (C.3).
* `CL^plane` be the congruence level of a plane transport bridge (B.3 / plane patterns).

Let `Φ`, `Ψ`, and `Φ_plane` be **policy-defined**, **monotone**, **bounded**, **table-backed** penalty policies applied on the relevant edges:
* `Φ(CL)` — scope/context Bridge penalty (CL).
* `Ψ(CL^k)` — KindBridge penalty (CL^k) when kinds are mapped.
* `Φ_plane(CL^plane)` — plane-crossing penalty when `ReferencePlane` differs.

**Important (direction of monotonicity).** Congruence ladders are “polarity up” (higher CL = better fit). Per **CC‑G0‑Φ** and the Trust & Assurance skeleton, penalty tables are monotone **decreasing** in their CL ladders (if `CL1 < CL2` then `Φ(CL1) ≥ Φ(CL2)`, analogously for `Ψ` and `Φ_plane`) and bounded so that `R_eff` remains within `[0,1]` after clipping. Penalty magnitudes are not required to lie in `[0,1]` (tables may exceed 1 to force `R_eff → 0` under the subtractive default); what matters is monotonicity, boundedness, and published policy identifiers.

Define:

`R_eff(P) = clip_0^1( Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P))) )`

where each `*_min(P)` is the **lowest** congruence level encountered on the entailment spine of `P` for that dimension (a bottleneck; no averages), and `clip_0^1(x)` truncates to `[0,1]`.

**Default (safe) instantiation (subtractive).**
When policies are expressed as subtractive penalties, a safe default is:

`R_eff(P) = max(0, R_raw(P) − Φ(CL_min(P)) − Ψ(CL^k_min(P)) − Φ_plane(CL^plane_min(P)) )`

This generalises the B.3 skeleton to multiple congruence ladders (scope vs kind vs plane) without introducing new penalty characteristics. If a dimension is not present on the path, its penalty term is treated as neutral (`0` in the subtractive default).

**Provisional marking.**
Default admissibility thresholds for reuse are set by Bridge calibration profiles (e.g., G.7). Typically, `CL=1` requires an explicit waiver to proceed and `CL=0` is inadmissible; this pattern only specifies that such thresholds gate transport before any numeric penalty is meaningful.

#### C.2.2:4.5.A - Math-by-level gating (B.1.3:4.3)

* **[M‑0/M‑1]** allow **ordinal** comparisons only (no arithmetic on `R_eff`); Φ/Ψ/Φ_plane may be qualitative (“low/med/high”). Publish evidence links + lane tags.
* **[M‑2/L1]** numeric `R_eff` requires referencing numeric, table-backed policy identifiers for Φ/Ψ/Φ_plane (and Π if not default), plus reproducibility tags for empirical legs; otherwise treat the claim as [M‑1] semantics.

#### C.2.2:4.6 - Evidence lanes are not new characteristics

KD‑CAL does not add new global coordinates beyond F–G–R. Instead, it requires that reliability be *explainable* via **assurance lanes** (B.3.3):

* **TA** (Typing assurance): semantic/type alignment sufficient for transport and composition.
* **VA** (Verification assurance): logical/algorithmic checking, proof, model checking, static guarantees.
* **LA** (Validation assurance): empirical adequacy under declared conditions, tests, benchmarks, telemetry.

Lane reporting is how KD-CAL supports the common research distinction between logical soundness and empirical adequacy **without introducing new global characteristics**.
Lanes remain **separable** in SCR/Notes; they are not averaged into a “single tradition score”.

#### C.2.2:4.7 - Scope operations are kind-safe (and use the ClaimScope algebra)

Reliability is meaningless if scope operations are applied to ill-typed entities.

**Well-formedness constraint WFC‑C2.2‑1 (Type before scope).**
Let `G1` and `G2` be claim scopes associated to described entities of kinds `K1` and `K2`. A scope operation that combines them (e.g., `G1 ∩ G2` for serial intersection, `SpanUnion({G_i})` for parallel coverage, or `translate(Bridge, G)` for cross‑context reuse) is defined only if:
* `K1 = K2`, or
* (same `U.BoundedContext`) `K1 ⊑ K2` or `K2 ⊑ K1` (an explicit kind relation/cast is named), or
* (cross‑Context) there exists a declared **KindBridge** relating `K1` and `K2` with an explicit `CL^k` (C.3).

This constraint prevents “type-by-scope” anti-patterns where scope manipulation is used to hide type mismatch.

#### C.2.2:4.8 - Minimal authoring recipe

A minimal, conforming KD‑CAL authoring flow for reliability is:

1. **Fix the typed claim.** State the claim as a typed proposition about a described entity (Kind‑CAL, C.3).
2. **Declare claim scope.** Write `G` explicitly using A.2.6 operators; avoid scope-by-wording.
3. **Declare stance carriers.** Declare `K=U.BoundedContext`, `S ∈ {design, run}`, and (where relevant on Working‑Model surfaces) `validationMode ∈ {postulate, inferential, axiomatic}`; declare `ReferencePlane` if crossings are in play.
4. **Bind evidence.** Attach evidence stubs and lane tags (TA/VA/LA) and validity windows / decay policy where applicable (B.3.3, B.3.4).
5. **Choose Γ-mode.** Declare whether the support is **series** (required) or **parallel** (independent lines to the same claim).
6. **Compute R_raw.** Use the weakest-link fold on the entailment spine; for parallel support, use `max` only with an explicit independence note.
7. **Declare bridges on reuse.** If you reuse across contexts/kinds/planes/notations, declare the bridge(s) (including NotationBridge where applicable) and their CLs.
   Cross‑Context reuse is conformant only when an explicit Bridge is declared; CL admissibility rules apply (waiver or forbid) before any numeric penalty is meaningful (see **CC‑C.2.2‑4**).
   **Reuse note (FPF discipline).** When this section refers to “reuse/portability across contexts or planes”, interpret it as Bridge-only reuse per §4.4: e.g., Bridge `Bridge#MatLab_to_PlantB` with `CL=2` and an explicit loss note, applying policy ids `Φ=Φ_v1` (and, where applicable, `Ψ=Ψ_v2`, `Φ_plane=Φ_plane_v1`) to reduce `R_eff` only.

8. **Compute R_eff.** Apply the declared penalty policies into `R` (never into `F` or `G`), and publish `⟨F,G,R_eff⟩` with traceable references and policy identifiers.

A reliable claim is not a loud claim; it is a claim that can be *carried*.

#### C.2.2:4.8.A - Authoring template: Path summary row (copy/paste)

When publishing `R_eff` for a claim, authors SHOULD include a compact, claim-local **path summary**. This is intentionally shaped so it can be turned into tooling later (EvidenceGraph/PathId in G.6) without introducing new Core types or face-kinds.

| PathId | Entailment spine (required supports) | CL_min | CL^k_min | CL^plane_min | Policy-id(s) (Φ / Ψ / Φ_plane) | R_raw | R_eff | Lane tags (TA/VA/LA) | valid_until |
| ------ | ----------------------------------- | ------ | -------- | ----------- | ------------------------------ | ----- | ----- | --------------------- | ---------- |
| P‑1    | `c ← {c_a, c_b, c_c}`               | 2      | 3        | —           | `Φ=Φ_v1`, `Ψ=Ψ_v2`             | 0.82  | 0.67  | {TA, LA}              | 2026‑09‑30 |

Notes:
* `CL_*_min` values are **bottlenecks** on the relevant path/dimension (no averaging).
* `valid_until` is the **earliest** expiry across empirical legs (or `—` / “fenced to TheoryVersion” for non-decaying proof legs).
* If you publish multiple admissible paths, include multiple rows and cite which PathId(s) your decision/guard consumed.

### C.2.2:5 - Archetypal Grounding

Informative; non-binding.

#### C.2.2:5.1 - System illustration

**System.** A brake controller `S` has a claim:

> `c1:` “For road friction μ ∈ [0.2, 0.9] and vehicle mass m ∈ [900, 2200] kg, wheel slip stays in [0.05, 0.25] under ABS control.”

* `F(c1)=F5` because the controller and constraints are expressed as a machine-checkable model plus executable test harness (C.2.3).
* `G(c1)` is the declared operating envelope (A.2.6) as a product set in `(μ, m, speed, tire)` space.
* Evidence:

  * VA: model-checking of a simplified plant/controller model (strong, but only for the simplified plant).
  * LA: HIL simulation + track tests under sampled conditions with recorded telemetry windows (freshness required).
  * TA: typed alignment between “μ” in simulations, “μ” in the estimation pipeline, and “μ” inferred from real-world sensors.

If telemetry is reused from the track context to the road context, a scope bridge is declared with `CL=2`. Using the default monotone penalty table (B.3), the LA contribution is reduced, and the derived `R_eff(c1)` drops accordingly. The claim’s envelope `G(c1)` does not change; only the warrant for transporting the evidence does.

#### C.2.2:5.2 - Episteme illustration

**Episteme.** A paper asserts two claims about an algorithm `A`:

* `c2:` “A terminates for all inputs in domain D.” (axiomatic / proof-carrying)
* `c3:` “A achieves ≥ 0.92 F1 on dataset family F under deployment preprocessing P.” (empirical)

`c2` can achieve high VA with a proof carrier; its LA lane may be N/A, but its TA lane remains relevant because the intended meaning of “domain D” must align with the implementation’s input model.
`c3` requires LA evidence and a freshness/shift policy because dataset and preprocessing drift change the scope and the warrant. If `c3` is reused from a lab dataset context to a production context, a bridge with explicit CL is required, and `R_eff` is reduced until new in-context evidence is attached.

### C.2.2:6 - Bias-Annotation

Informative; non-binding.

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

* **Onto/Epist bias:** High formality is often mistaken for high warrant (“proof therefore true in the world”). This pattern mitigates by forcing LA/TA visibility and by routing transport loss into R rather than mutating the claim.
* **Prag bias:** Teams may Goodhart R by narrowing scope or selecting easy tests. This pattern mitigates by requiring explicit scope declaration and by making scope changes first-class (A.2.6).
* **Gov bias:** Overconfident reuse across contexts is a recurring failure mode in governance settings. This pattern mitigates by forcing explicit bridges and penalties for reuse.
* **Did bias:** A single scalar is seductive; it hides what kind of warrant exists. Lane reporting keeps the scalar honest.

### C.2.2:7 - Conformance Checklist

Normative.

| ID                                            | Requirement                                                                                                                                                                                                                 | Purpose                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **CC‑C.2.2‑1 (Triad publication).**           | Authors of a KD‑CAL location **SHALL** publish `⟨F,G,R_eff⟩` as a bundle for a specific claim, rather than publishing `R` alone.                                                                                            | Prevents decontextualised confidence scores.                                  |
| **CC‑C.2.2‑2 (R-only penalty routing).**      | A conforming implementation of KD‑CAL transport **SHALL** satisfy **INV‑C2.2‑1**.                                                                                                                                           | Ensures bridges reduce warrant without silently mutating expression or scope. |
| **CC‑C.2.2‑3 (Weakest-link fold).**           | A conforming implementation of KD‑CAL reliability propagation **SHALL** use **DEF‑C2.2‑3** as the default for required supports, unless an alternative Γ‑fold is explicitly declared and remains monotone and conservative. | Prevents confidence laundering through aggregation.                           |
| **CC‑C.2.2‑4 (Bridge visibility for reuse).** | Authors **SHALL** declare explicit bridges with CL values for any cross-context, cross-kind, or cross-plane reuse that affects `R_eff`.                                                                                     | Makes transport loss auditable and machine-checkable.                         |
| **CC‑C.2.2‑5 (Penalty policy visibility).**   | Authors or tooling **SHALL** reference the active policy identifiers used for `Φ`, `Ψ`, `Φ_plane` **and** the penalty aggregation rule `Π` (if not the default) when computing `R_eff`.                                   | Ensures repeatability and prevents hidden policy drift.                       |
| **CC‑C.2.2‑6 (Type before scope).**           | Authors and validators **SHALL** enforce **WFC‑C2.2‑1** for scope composition operations.                                                                                                                                   | Prevents ill-typed scope algebra from creating incoherent reliability claims. |
| **CC‑C.2.2‑7 (Evidence binding).**            | Authors **SHALL** bind any asserted `R_eff` to evidence references that enable TA/VA/LA inspection, consistent with the assurance lane discipline (B.3.3) and evidence decay discipline (B.3.4).                            | Keeps R grounded and updateable.                                              |
| **CC‑C.2.2‑8 (No ordinal arithmetic).**       | Validators **SHALL** reject any computation that treats `F` or `CL` as if they were ratio-scale numbers (e.g., averaging, subtraction), except where explicitly permitted as a policy-defined penalty function on `R`. Validators **SHALL** also reject arithmetic over `R_eff` when it is published as an **ordinal proxy** ([M‑0/M‑1]). | Enforces CSLC legality and prevents silent scalarisation.                     |
| **CC‑C.2.2‑9 (Stance carriers declared).**    | Authors **SHALL** declare `U.BoundedContext K`, `S ∈ {design, run}`, and (where applicable) `ReferencePlane` and `validationMode`, and **SHALL NOT** merge design- and run-time assurance into one score.                 | Prevents DesignRunTag chimera and makes interpretation auditable.              |
| **CC‑C.2.2‑10 (Parallel requires independence).** | Authors **SHALL** treat `max`-composition of support paths as admissible **only** when an explicit independence justification is recorded; otherwise supports are treated as one entangled line and remain weakest-link. | Prevents confidence inflation by double-counting correlated evidence.         |

### C.2.2:8 - Common Anti-Patterns and How to Avoid Them

Informative; non-binding.

| Anti-pattern               | Symptom                                                                                       | Why it fails                                                     | How to avoid / repair                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Averaging assurance**    | A mean/weighted sum of `R` values is reported as “confidence”.                               | It violates WLNK and is usually illegal scale arithmetic.        | Use weakest-link `min` on the entailment spine, then apply congruence penalties into `R` only.          |
| **Truth-by-score**         | `R=0.9` is treated as “the claim is true.”                                                    | R is warrant strength, not ontological truth.                    | Require explicit evidence links and scope; treat R as decision warrant only.                             |
| **Scope laundering**       | The claim’s applicability grows by wording changes while `G` is unchanged.                    | It silently widens scope, making comparisons meaningless.        | Use A.2.6 operators and treat scope changes as explicit revisions.                                       |
| **Bridge laundering**      | A claim is reused in a new context without a bridge, and R is carried over unchanged.         | It hides semantic loss and encourages overconfident reuse.       | Declare bridges with CL and recompute `R_eff` using penalties.                                           |
| **DesignRunTag chimera**     | Design-time proofs and run-time telemetry are mixed as if they were the same evidence object. | Evidence belongs to different stances and decays differently.    | Separate lanes and validity windows; treat crossings explicitly.                                         |
| **Ordinal arithmetic**     | CL or F levels are averaged to produce a pseudo-score.                                        | It violates scale legality and produces non-auditable numbers.   | Keep CL/F ordinal; convert only via declared penalty tables on R.                                        |
| **Many-weak-makes-strong** | Numerous low-quality supports are combined to inflate confidence.                             | It violates the weakest-link intent of conservative propagation. | Default to `min` for required supports; allow `max` only with explicit independence arguments.          |

### C.2.2:9 - Consequences

Informative; non-binding.

| Benefits                                                                                                     | Trade-offs and mitigations                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability.** Different claims can be compared in a disciplined way when F and G are explicit.          | **Conservatism.** Weakest-link propagation can feel pessimistic; mitigate by making support structure explicit and improving the weakest evidence. |
| **Auditability.** Transport loss is visible and localised to R.                                              | **Overhead.** Declaring bridges and evidence links is work; mitigate with templates and reuse of standard lane schemas.                            |
| **Upgradeable knowledge.** R can improve incrementally as evidence accumulates, without rewriting the claim. | **Scalar temptation.** People still want one number; mitigate by requiring lane breakdown visibility behind the number.                            |

### C.2.2:10 - Rationale

A triad only works if each coordinate has a single job.

* **G carries entitlement.** It states where the claim is asserted to apply. If G is implicit, teams argue about “what was meant” instead of updating scope.
* **F carries checkability.** It states how much the claim’s form supports mechanised scrutiny and reuse. If F is conflated with R, formalisation becomes a rhetorical weapon.
* **R carries warrant.** It states how much evidence supports relying on the claim under G. If R is not conservative, evidence with a low `R` coordinate can be laundered into high confidence.

Routing congruence loss into **R only** prevents a subtle but pervasive failure mode: transport across contexts/kinds/planes does not silently rewrite the claim; it only reduces how confidently we should carry it.

Weakest-link propagation is chosen because it is the simplest rule that is monotone, conservative, and auditable. When better combination rules exist, they can be introduced as explicit Γ‑policies, but the default must be safe.

### C.2.2:11 - SoTA-Echoing

Normative.

**SoTA pack binding note.** If a SoTA Synthesis Pack exists for KD‑CAL reliability / cross‑context warrant transport in your Context (G.2), cite its ClaimSheet IDs / CorpusLedger entries / BridgeMatrix rows here. Otherwise, record `SoTA-Pack: TBD/none` and treat this section as the seed (do not fork it silently elsewhere).

| Practice claim                                                                                                      | Post‑2015 source anchor                                                                   | Alignment to this pattern                                                                                                                                                           | Adoption status                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Verification and validation should be distinguished and tied to evidence quality, not to rhetoric.                  | ASME V&V 40‑2018 (model credibility assessment).                                          | This pattern separates VA and LA lanes and binds `R_eff` to evidence and declared scope rather than to narrative confidence.                                                        | **Adopt**, with KD‑CAL’s conservative fold as an explicit default.                                                   |
| Trustworthiness is context- and risk-dependent and requires explicit documentation of limits.                       | NIST AI Risk Management Framework 1.0 (2023).                                             | This pattern makes limits first-class via `G` and makes reuse loss explicit via CL penalties rather than informal caveats.                                                          | **Adapt**, because FPF treats transport loss as an epistemic penalty, not as a purely organisational risk statement. |
| Safety arguments should make claims, evidence, and assumptions explicit and reviewable.                             | UL 4600 (2020) and related assurance-case practice in autonomous systems.                 | This pattern treats `R` as an auditable warrant signal whose inputs are explicit evidence items and whose reuse requires explicit transport justification.                          | **Adopt**, while remaining notation-independent and avoiding tool mandates.                                          |
| Empirical results should be accompanied by structured provenance and usage conditions to enable reuse and critique. | “Datasheets for Datasets” (Gebru et al., 2018) and “Model Cards” (Mitchell et al., 2019). | This pattern’s scope discipline and lane reporting make empirical warrant portable only when its conditions are explicit; cross‑Context reuse is Bridge-only (e.g., `Bridge#MatLab_to_PlantB`, `CL=2`, `Φ=Φ_v1`), and congruence loss routes to `R_eff` only. | **Adopt**, with congruence penalties as the reuse control mechanism.                                                 |
| Reproducibility requires packaging evidence and making it re-checkable by others.                                   | ACM Artifact Review and Badging (updated practices post‑2015) and The Turing Way (2019).  | This pattern treats evidence as something that can be inspected across TA/VA/LA lanes and allows reliability to decay when evidence becomes stale or non-replayable.                | **Adapt**, because FPF treats decay and transport penalties as first-class calculus elements.                        |
| Strong inference benefits from “severe tests” rather than from accumulation of weak confirmations.                  | Mayo (2018) on severity in statistical inference.                                         | Weakest-link propagation and explicit scope declarations discourage superficial confirmation piling and encourage explicit, discriminating evidence.                                | **Adapt**, because KD‑CAL is agnostic to frequentist vs Bayesian inference but requires auditability.                |

### C.2.2:12 - Relations

**Builds on:** C.2 (KD‑CAL overview), A.2.6 (Claim scope and operators), C.2.3 (Formality F), B.3 (Trust & Assurance calculus), B.1.3 (Γ‑fold patterns), B.3.3 (assurance lanes), B.3.4 (refresh/decay), C.3 (Kind‑CAL and kind bridges), F.9 (Bridges & CL), G.6 (EvidenceGraph PathId discipline), G.7 (Bridge calibration / admissibility thresholds).
**Coordinates with:** C.16 (MM‑CHR evidence discipline), E.14 (working-model assertions), E.18/F.9/F.17/E.17/A.21 where crossing bundles and gate checks are live, C.25 (Q‑Bundle, for avoiding confusion between epistemic reliability and system reliability).
**Used by:** C.3.3 (cross-kind reuse discipline), guard macro bundles in C.3.A and C.21, and any acceptance/gating logic that consumes `R_eff` while preserving `F` and `G`.
**Clarifies:** The KD‑CAL meaning of reliability implicit in C.2:4.1 and the transport clauses referenced across B.3 and C.3.

### C.2.2:End

## C.2.2a - `U.LanguageStateSpace` - Language-state chart over `U.CharacteristicSpace`

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state space.

**Builds on.**
`A.19`, `E.10`, `F.18`.

**Used by.**
`C.2.LS`, `C.2.3`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `F.9.1`, `A.6.P`, `A.6.Q`, `A.6.A`.

### C.2.2a:1 - Problem frame
In engineering, inquiry, operator, and management practice, teams often need to say where a governed `U.Episteme` publication currently stands before it has reached a late endpoint governing pattern. That governed publication may later appear through several cue-bearing, route-bearing, or endpoint-bound publication forms, but the chart claim remains about the governed `U.Episteme` publication rather than about a local alias or a carrier lane.

Cue packs, routed cue sets, abductive prompts, typed route-bounded projection publications, partial normal forms, and endpoint-bound records are not rival occupants of the space. They are publication forms through which a current position claim is made visible. MVPK faces may render those forms, but faces are not themselves the forms. By contrast, a service disturbance, a model-vs-observation discrepancy, a bodily tension, a telemetry trace, a model output, or a carrier document may trigger, witness, or carry that episteme, but none of those is itself a coordinate in the space.

Practitioners, including engineers, operators, researchers, managers, and engineer-managers, still have to decide where such an episteme currently stands, which thresholds matter next, which publication form is admissible, and what must not yet be claimed. If this domain is described only with folk labels such as `raw`, `early`, `settled`, or `ready`, the real geometry disappears.

### C.2.2a:2 - Problem
Without an explicit language-state chart:

1. teams collapse several facets into one maturity story;
2. `F` is silently misused as a surrogate for articulation, closure, anchoring, and representation factors;
3. thresholds are published as vague readiness statements instead of explicit facet conditions;
4. source phenomena, governed epistemes, publication forms, publication faces, and carriers are conflated;
5. bridge and endpoint work inherit under-described upstream states.

### C.2.2a:3 - Forces
| Force | Tension |
| --- | --- |
| **Multi-facet fidelity vs readable publication** | The chart must preserve several independent facets without becoming unreadable. |
| **Stable basis vs local thresholds** | Basis slots should stay stable across contexts, while thresholds remain context-local. |
| **Position semantics vs publication semantics** | A position claim is not identical to the source phenomenon, publication form, or carrier through which it is currently expressed. |
| **Comparability vs non-collapse** | Teams need to compare positions, but not by flattening them into one pseudo-scale. |
| **Bridge reuse vs local authority** | Cross-context work benefits from a stable upstream chart, yet each context keeps local threshold authority. |

### C.2.2a:4 - Solution
`U.LanguageStateSpace` is the cluster-local name for the declared language-state chart over `U.CharacteristicSpace` as disciplined by `A.19`.

It is not a second kernel state-space apparatus beside `A.19`. It is the particular declared `U.CharacteristicSpace` whose basis slots are the language-state facets used in this cluster.

#### C.2.2a:4.1 - Core role
`U.LanguageStateSpace` gives FPF one explicit declared chart for answering five questions:

- which basis slots define where the governed episteme stands;
- what a position claim in that chart means;
- which thresholds are locally declared over those slots;
- what comparisons are admissible without cross-facet collapse;
- and how the same position claim stays distinct from the publication form currently expressing it.

#### C.2.2a:4.2 - Position reading under `A.19`
A language-state position is a partial, slot-explicit coordinate claim in the declared language-state `U.CharacteristicSpace`.

Each basis slot publishes a `ValueSet(slot)`, interval, or other admissible set-valued claim. Early seam publications may leave some slots unknown or wide, but that uncertainty must be declared rather than hidden inside one stage word.

`position` language is therefore admissible here only as shorthand for such slot-explicit `A.19` coordinate claims. It does **not** authorize a rival process-sequence or feature-vector story.

#### C.2.2a:4.3 - Facet basis
The language-state chart is coordinated by explicit facet governing patterns rather than by an informal master progression. In the current cluster the basis is formed by:

- `C.2.3` for `F`;
- `C.2.4` for articulation explicitness;
- `C.2.5` for language-state closure degree;
- `C.2.6` for language-state anchoring mode;
- `C.2.7` for the language-state representation-factor bundle.

`C.2.2a` states that these basis slots together define the chart. It does **not** govern the internal scale semantics of the individual facets.

#### C.2.2a:4.4 - Ontological role lanes
Within this cluster, keep five roles distinct:

- **occupant** - the governed `U.Episteme` publication whose current position is being claimed;
- **grounds / witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, exemplars, or contrasts that justify the current reading;
- **publication forms** - cue packs, routed cue sets, prompt forms, typed route-bounded projection publications, partial normal forms, and endpoint-bound records through which the episteme is published;
- **publication faces** - the existing MVPK faces on which those publication forms are rendered when face typing matters;
- **carriers** - documents, console notes, cards, trace files, or model carriers that hold or render a publication.

`U.LanguageStateSpace` governs only the coordinate reading of the position claim. It does not collapse that claim into the grounds, publication form, publication face, or carrier.

#### C.2.2a:4.5 - Position publication rule
A published position claim in `U.LanguageStateSpace` should normally make at least the following explicit:

- the occupant whose position is being described;
- the relevant slot values, `ValueSet` claims, or intervals;
- the current publication form and, when it matters, the MVPK face carrying it;
- the load-bearing grounds, witnesses, or carriers that explain those values;
- any local threshold declarations if the position is being used for a routing or gate decision;
- any note that distinguishes source anchoring from current publication-face anchoring.

A position claim may be partial when some slots are intentionally unknown, but the unknowns should be declared rather than hidden under a broad readiness label.

#### C.2.2a:4.5.a - Local position-reading witness
For this pattern, a position claim is reviewable when:

- the occupant is named or inherited by an already pinned upstream publication;
- the slot values, intervals, or `ValueSet` claims are explicit enough to show where the publication stands;
- the grounds, witnesses, or inherited pins that support those values remain visible;
- any threshold-bearing use states the local threshold note or the pinned threshold source it inherits;
- and the text keeps the occupant, publication form, publication face, and carrier in distinct role lanes.

A polished note, a carrier with more preservation or distribution support, or a more formal face does not by itself prove a new position. The chart claim remains admissible only when those role lanes and slot claims stay visible.

#### C.2.2a:4.6 - Non-substitution of `F`
`F` remains one basis slot in the chart, not the whole chart.

A conforming account shall not infer:

- closure from formality alone;
- anchoring from publication-face format alone;
- representation factors from articulation alone;
- or routing legality from a lone `F` statement.

Where operationally meaningful thresholds exist, they must publish on the relevant slots rather than being disguised as informal `F` sublevels.

#### C.2.2a:4.7 - Position versus publication form
A position claim in `U.LanguageStateSpace` is distinct from:

- the underlying governed `U.Episteme`,
- the source disturbance, discrepancy, or witness,
- the current publication form,
- the MVPK face that renders that publication,
- the carrier that stores or displays it,
- or the endpoint-pattern-governed publication that may later result from it.

Those roles are coupled but distinct. `U.LanguageStateSpace` keeps the position claim readable without collapsing it into any one bearer lane.

#### C.2.2a:4.8 - Threshold publication discipline
If a threshold is used to justify a move, a handoff, or an endpoint entry, that threshold shall be stated on explicit basis slots in the chart. Statements such as `this is now ready`, `this has matured`, or `this is still too early` are non-conformant when they substitute for undeclared slot conditions.

#### C.2.2a:4.9 - Comparison and bridge note
Comparisons inside one context may use the shared chart and local thresholds. Comparisons across contexts require explicit bridge discipline. Label similarity or stage-language similarity does not establish sameness of charts, positions, or thresholds.

`C.2.2a` therefore supports bridge work, but does not grant cross-context identity by itself.

#### C.2.2a:4.10 - Corridor reading note
The current `Language-State & Semantic Routing Corridor` in this cluster is a distributed overlay over:

- `C.2.2a`
- `C.2.LS`
- `C.2.4–C.2.7`
- `A.16`
- `A.16.0–A.16.2`
- `B.4.1`
- `B.5.2.0`

`A.16.1 / U.PreArticulationCuePack` remains the earliest durable seam publication form in that corridor. `B.4.1` is the explicit route-bearing seam after cue preservation, not the first publication in the corridor. `B.5.2.0` is typed prompt entry, not generic route governance.

`A.6.Q`, `A.6.A`, `A.6.P`, `B.5.2`, `A.15`, and `C.25` are seam-coupled downstream governing patterns rather than members of this language-state governing-pattern set.

This note gives readers one corridor map only. It does not relocate articulation, closure, route, prompt, bridge, or endpoint semantics out of their current governing patterns.

### C.2.2a:5 - Archetypal Grounding
**Tell.** One note can have high operator-loop anchoring yet still low closure. Another can be document-mediated and symbol-heavy while still open on route choice. Both are positions in one language-state chart, but not on one maturity progression.

**Show (System).** A service disturbance is a system-side phenomenon. The governed occupant is the alerting `U.Episteme` published from that disturbance; its position claim may be moderately formal, low-closure, high in operator-loop anchoring, and mixed in representation because terse codes and natural-language hints coexist.

**Show (Episteme).** A model-vs-observation discrepancy is a witness-level tension, not the occupant itself. Once preserved as a cue pack, the resulting governed `U.Episteme` may be low in articulation, low in closure, trace-anchored, and only partly symbolic even when later written into prose.

### C.2.2a:6 - Bias-Annotation
The pattern deliberately biases authors toward decomposable coordinate claims and away from folk stage vocabularies. That costs some brevity, but it prevents collapse of genuinely different state facets into one adjective.

### C.2.2a:7 - Conformance Checklist
- `CC-C.2.2a-1` `U.LanguageStateSpace` **SHALL** be treated as the declared language-state chart over `U.CharacteristicSpace`, not as a rival kernel space and not as a disguised `F` progression.
- `CC-C.2.2a-2` Published positions **SHALL** cite explicit facet governing patterns when those positions matter for movement, routing, or endpoint entry.
- `CC-C.2.2a-3` Position claims **SHALL** use slot-explicit values, `ValueSet` claims, or intervals; uncertainty **SHALL NOT** be hidden inside stage words such as `ready`, `early`, or `mature`.
- `CC-C.2.2a-4` A position claim in the chart **MUST NOT** be conflated with the current ground, witness, publication form, publication face, or carrier.
- `CC-C.2.2a-5` Cross-context comparison of positions or threshold talk **SHALL** go through bridge discipline rather than label similarity.
- `CC-C.2.2a-6` Corridor and navigation notes **MUST NOT** be read as relocation of facet, seam, bridge, or downstream governing-pattern semantics into the chart governing-pattern set.
- `CC-C.2.2a-7` If a position claim is used for routing, endpoint entry, or gate-adjacent reasoning, the threshold note and the role-lane distinction between occupant, publication form, face, and carrier **SHALL** remain explicit or explicitly inherited from a pinned upstream publication.

### C.2.2a:8 - Common Anti-Patterns and How to Avoid Them
- **Maturity monism.** Replace five facets with one stage word. Repair by publishing explicit slot placement.
- **Formality capture.** Use `F` to stand in for articulation, closure, or anchoring. Repair by naming the actual facet governing pattern.
- **Carrier collapse.** Treat a document, cue pack, or routed note as if it were the position itself. Repair by separating carrier lane, publication form, publication face, and position claim.
- **Threshold folklore.** Speak of readiness without any explicit threshold declaration. Repair by publishing relevant local threshold notes on explicit slots.
- **Bridge by vibe.** Treat similar stage language in two schools as equivalence. Repair by explicit `F.9` bridge with loss notes.
- **Corridor inflation.** Treat the navigation cluster or corridor map as if it were the governing-pattern set for all downstream semantics. Repair by naming whether the current statement belongs to the chart governing-pattern set, a seam publication form, or a downstream governing pattern.

### C.2.2a:9 - Consequences
The benefit is that practitioners, including engineers, operators, researchers, managers, and engineer-managers, can speak about where a governed `U.Episteme` stands without hiding the reasons inside vague maturity language. The trade-off is that publication must carry explicit slot and threshold information when decisions depend on it.

### C.2.2a:10 - Rationale
Language-state work needs one explicit statement of what this chart is before individual facet, move, and endpoint patterns start using it. Without that statement, readers have to reconstruct the same geometry from scattered local rules and examples.

### C.2.2a:11 - SoTA-Echoing

**SoTA note.** This section does not mint a second rule source. It is a load-bearing alignment statement: the Solution, Conformance Checklist, and role-lane discipline of this pattern must match the stance stated here or explicitly justify divergence.

**Traditions covered.** This pattern binds itself to architecture-description governance, model-based systems engineering, and risk/governance profiling practice.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `C.2.2a` | Adoption status |
|---|---|---|---|---|
| Complex technical state should be published through explicit views, viewpoints, and model distinctions rather than one implicit maturity word. | Contemporary architecture-description governance separates source architecture description, view, viewpoint, and correspondence evidence instead of letting one visible adjective stand in for the whole state. | ISO/IEC/IEEE 42010:2022 | `C.2.2a` adopts this by keeping chart position, publication form, face, and carrier in distinct role lanes and by rejecting stage-language as a surrogate coordinate system. | **Adopt.** |
| Rich engineering state is better represented through typed properties and relations than through one maturation progression. | Recent MBSE practice favours explicit model elements, properties, and cross-view consistency over one implicit readiness staircase. | OMG SysML v2 (2025) | `C.2.2a` adapts this into a declared language-state chart with named basis facets, slot-explicit values, and local thresholds instead of one maturity rail. | **Adapt.** |
| Governance-relevant readiness requires context-local profiles and thresholds, not one global adjective. | Current governance and risk frameworks use explicit profiles, thresholds, and scoped conditions rather than one blanket readiness label. | NIST AI RMF 1.0 (2023) | `C.2.2a` adopts the threshold-publication discipline and rejects the popular shortcut where `ready`, `early`, or `mature` replaces explicit slot conditions. | **Adopt/Reject-popular-shortcut.** |

**Architecture-description governance.** `C.2.2a` adopts the discipline that positions, publication forms, faces, and carriers stay explicitly distinct, even when one local rendering makes them look aligned.

**MBSE and profile discipline.** `C.2.2a` adapts multi-property state publication into a chart over `U.CharacteristicSpace` whose basis facets remain decomposable and locally thresholded.

**Local stance.** The load-bearing SoTA claim for this pattern is narrow: best-known current practice treats governed language-state as a multi-facet chart with explicit thresholds and role-lane distinctions, not as one maturity progression or one polished publication face.

### C.2.2a:12 - Relations
- Builds on: `A.19`, `E.10`, `F.18`.
- Coordinates with: `C.2.LS`, `C.2.3`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `F.9`, `F.9.1`, `E.17.1`.
- Constrains: threshold publication, positional claims, and anti-collapse discipline across the language-state cluster.

### C.2.2a:13 - Worked Examples

#### C.2.2a:13.1 - Inquiry cue before endpoint capture
A research cue note may occupy a position claim with:

- moderate `F`,
- low articulation explicitness,
- low closure,
- strong embodied or trace-based anchoring,
- and mixed representation factors.

That position explains why the note should remain upstream of `A.6.P` or `C.25` even if its prose happens to look polished.

#### C.2.2a:13.2 - Routed operator alert note
A routed operational alert may have:

- moderate formality,
- medium articulation,
- low closure because several responses remain live,
- high operator-loop anchoring,
- and mixed symbolic and natural-language representation.

That position explains why the alert belongs in a route-bearing seam publication before it hardens into an endpoint-pattern-governed work record or reliance record.

#### C.2.2a:13.3 - Viewpoint-bound adequacy note
A document-mediated adequacy note about an architecture description may be relatively high in formality and articulation, mid-level in closure, document-mediated in anchoring, and symbolic in representation. That position remains within the same language-state chart even though its carrier lane differs from an embodied inquiry cue.

#### C.2.2a:13.4 - Polished prose is not closure
A prose rewrite may look cleaner, more compact, or more manager-readable than the source cue and still remain low in closure or articulation explicitness. If the underlying slot values, uncertainty, and route plurality remain unchanged, then publication polish changes the rendering or carrier lane, not the chart position by itself.

### C.2.2a:14 - Position Publication Package Discipline
A publishable position claim should normally identify:

- the occupant whose position is being described;
- the relevant slot values, `ValueSet` claims, or intervals;
- the current publication form and, if relevant, the MVPK face and carrier;
- any source-versus-face anchoring distinction that matters;
- the thresholds, if any, being invoked;
- and the next governing pattern or move family that depends on the claim.

This keeps the claim operationally useful without pretending that the position is itself a full trajectory or endpoint form.

### C.2.2a:15 - Review Guidance
A reviewer should ask:

1. Is the author naming a position claim in the chart, or only a folk stage label?
2. Is `F` being used as a surrogate for another slot?
3. Are source phenomena, publication forms, publication faces, and carriers being confused with the occupant?
4. Are threshold claims explicit enough for the next move or endpoint decision?
5. If the text compares two contexts, is there a real bridge or only a lexical resemblance?

### C.2.2a:16 - Boundary Notes
`C.2.2a` does not govern move kinds, seam publication forms, endpoint repair semantics, or bridge substitution licence. Those belong respectively to `A.16` / `A.16.0`, `A.16.1` / `B.4.1` / `B.5.2.0`, `A.6.*` / `C.25`, and `F.9` / `F.9.1`.

Its job is narrower and more foundational: to make the declared language-state `U.CharacteristicSpace` chart readable so that downstream patterns can refer to one visible common geometry instead of rebuilding it piecemeal.

### C.2.2a:End

## C.2.3 - Unified Formality Characteristic F

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Formality characteristic.

**One-line summary.** `C.2.3` defines **Formality (F)** as one ordinal `U.Characteristic` with polarity `up`, anchored by the default ladder `F0...F9`, and declared as the `F` coordinate of the typed `F-G-R` assurance tuple.

### C.2.3:1 - Problem frame

Transdisciplinary work needs one shared way to speak about rigor of expression. A research hypothesis in constrained natural language, a software interface specification with explicit invariants, a controller model checked against hybrid obligations, and a proof-bearing formal development are not comparable by domain lore alone. They are comparable by **how strictly the content is expressed**.

Historically, that distinction drifts. Teams mix editorial maturity, organizational status, notation choice, proof support, and scope narrowness into one vague story about something being *more formal*. `C.2.3` removes that drift by giving FPF one explicit `U.Characteristic` for rigor of expression.

### C.2.3:2 - Problem

Without one unified `F` characteristic:

1. **Rigor is narrated inconsistently.**
   Different contexts invent local mode/tier language with no shared comparability.
2. **Status and rigor collapse.**
   Something accepted, published, or approved is mistaken for something precisely expressed.
3. **Expression changes are hidden.**
   A move from sketch to predicates or from executable model to proof is not recorded as a distinct content change.
4. **Composition becomes unsound.**
   A composite episteme is treated as highly formal because one segment is highly formal, even when essential support still depends on less formal parts.
5. **Other characteristics are misused as surrogates.**
   Authors quietly use scope, evidence, or language-state facets as if they were part of one master formality characteristic.

### C.2.3:3 - Forces

| Force | Tension |
|---|---|
| **Readability vs precision** | Natural language is fast and legible; formal systems are unambiguous and checkable. F needs a gradient, not a cliff. |
| **Local freedom vs shared comparability** | Contexts need local exemplars and thresholds, but cross-context reasoning requires one stable characteristic. |
| **Exploration vs assurance** | Early work must be allowed at low F, while high-assurance work needs explicit higher anchors. |
| **Notation diversity vs semantic stability** | Different symbol systems may express the same rigor level; notation choice alone must not redefine F. |
| **Thin characteristic vs rich practice** | The core characteristic should stay simple, while still supporting concrete guidance, examples, and review discipline. |

### C.2.3:4 - Solution - `U.Formality` as one ordinal characteristic

`C.2.3` defines `U.Formality` as the single governing characteristic for rigor of expression in FPF.

#### C.2.3:4.1 - Identity and typing

- **Name:** `U.Formality` (abbreviated `F` in the assurance tuple)
- **Type:** `U.Characteristic`
- **Scale kind:** ordinal
- **Polarity:** `up`
- **Carrier:** any `U.Episteme`
- **Default value family:** `F0...F9`

`F` states **how strictly the content is expressed**. It does not state whether the content is true, well evidenced, widely applicable, or organizationally accepted.

#### C.2.3:4.2 - Role in the typed `F-G-R` tuple

`F` is the formality coordinate in the assurance tuple. Its interaction rules are strict:

- `F` is **not** `G`; scope remains governed by `U.ClaimScope` and other USM structures.
- `F` is **not** `R`; evidence, warrant strength, and decay remain assurance concerns.
- `CL` and bridge losses affect **`R`**, not `F`.
- Changes in notation or carrier surface do not change `F` if the formal content is preserved.

#### C.2.3:4.3 - Extensibility and local anchors

FPF provides the default anchor ladder `F0...F9`. A context may define sub-anchors or intermediate anchors such as `F4[OCL]` or `F6.5`, but only if:

- global order is preserved,
- the local anchor is explicitly docked to a parent anchor,
- the context does not invent a rival ladder or proxy scale.

#### C.2.3:4.4 - Usage obligations

- Every normative episteme shall declare one `F` value.
- Thresholds that depend on rigor should be written explicitly as `F >= Fk` conditions.
- Any raise or lowering of `F` is a content change, not a status-only change.
- `F` remains declaration and reasoning infrastructure; it is not itself a governance process.

### C.2.3:5 - Archetypal Grounding

**Tell.** `F` does not ask whether a claim is correct. It asks how strictly the claim is expressed.

**Show (System).** A system requirement written as controlled natural language with unambiguous acceptance conditions may be `F3`; the same requirement rewritten as explicit typed invariants may become `F4`; a machine-checked proof of a critical invariant may raise the relevant claim core to `F7` or above.

**Show (Episteme).** A research conjecture can begin at `F1-F3`, then gain explicit predicates at `F4`, executable semantics at `F5`, and proof-bearing core content at `F7-F8`, while remaining recognizably the same evolving claim family.

### C.2.3:6 - Bias-Annotation

The pattern biases FPF toward one explicit rigor characteristic and against stories that mix formality with status, publication quality, scope width, or evidence support. That bias is intentional. The price of explicit declaration is smaller than the cost of comparing rigor through folklore.

### C.2.3:7 - Conformance Checklist

- `CC-F-1` Every normative `U.Episteme` **SHALL** declare exactly one `U.Formality` value, either a default anchor or a local sub-anchor explicitly docked to one.
- `CC-F-2` `F` **SHALL** be treated as an ordinal characteristic; arithmetic over `F` values is invalid.
- `CC-F-3` Higher `F` **SHALL** mean greater or equal strictness of expression, not greater truth, trust, or scope.
- `CC-F-4` Contexts **MUST NOT** publish alternative "formality modes" or "tiers" as surrogates for `F`.
- `CC-F-5` Local sub-anchors **SHALL** preserve the global ordering and the parent anchor meaning.
- `CC-F-6` The episteme-level `F` of a composite episteme **SHALL** be bounded by the least-formal essential support on the relevant support path.
- `CC-F-7` Implementations **MUST NOT** average `F` values numerically.
- `CC-F-8` Changes in `G`, `R`, or `CL` **SHALL NOT** change `F` unless the expression form itself changes.
- `CC-F-9` Cross-context transport **SHALL** preserve the attributed `F`; if the receiving context rewrites the claim materially, it becomes a new episteme with its own `F`.
- `CC-F-10` Translation loss, bridge loss, and plane crossings **SHALL** affect `R` rather than being hidden as `F` changes.
- `CC-F-11` Assigned `F` values **SHALL** be justifiable by observable content such as explicit predicates, executable semantics, or machine-checked proofs.
- `CC-F-12` Declaring a tool or notation **SHALL NOT** by itself justify a higher `F` unless the content satisfies the target anchor semantics.
- `CC-F-13` Status labels such as `Draft`, `Approved`, or `Published` **MUST NOT** substitute for `F`.
- `CC-F-14` A context that uses `F` in gates or policies **SHALL** write those thresholds explicitly.
- `CC-F-15` Language-state facets such as articulation or closure **MUST NOT** be hidden as pseudo-levels of `F`.

### C.2.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Status leakage** | An episteme is called highly formal because it is approved or published. | `CC-F-13` keeps status and formality separate. |
| **Tool-worship** | A notation, prover, or execution harness is named, so the episteme is rated high-F without checking the content. | `CC-F-11` and `CC-F-12` require observable semantic grounds. |
| **Appendix inflation** | A small high-formality appendix is used to advertise the whole episteme as high-F. | `CC-F-6` keeps the whole episteme capped by the least-formal essential support. |
| **Proxy ladder** | A local context invents "bronze / silver / gold" or "ready / mature / final" and uses it instead of `F`. | `CC-F-4` rejects rival ladders. |
| **Characteristic capture** | Articulation, closure, scope, or evidence is spoken of as if it were part of `F`. | `CC-F-8`, `CC-F-10`, and `CC-F-15` keep the characteristics orthogonal. |

### C.2.3:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Shared rigor language.** Cross-domain publication units can be compared by one stable expression characteristic. | Authors must learn the anchor ladder and declare `F` explicitly. |
| **Safer composition.** Composite epistemes stop inheriting a misleadingly high rigor label from one polished segment. | Reviewers must identify essential support rather than read only visible polish. |
| **Cleaner governance.** Thresholds can be written as explicit `F` conditions instead of vague maturity labels. | Contexts must translate old local language into the canonical characteristic. |
| **Better interaction with other characteristics.** `F`, `G`, `R`, and language-state facets remain distinct. | Authors lose the convenience of one master-ladder story; that loss is deliberate. |

### C.2.3:10 - Rationale

FPF needs a rigor characteristic that is portable across mathematics, software, systems, policy, and research. The smallest stable answer is one ordinal characteristic with clear anchors and explicit composition rules. Anything more fragmented breaks comparability; anything more compressed hides the substantive differences between sketch, predicate, executable model, and machine-checked proof.

### C.2.3:11 - SoTA-Echoing

Post-2015 practice across formal methods, software architecture, safety engineering, verification, computational science, and typed proof environments converges on one broad lesson: rigor is not binary. It rises through explicit structuring, predicate expression, executable semantics, and machine-checked obligations. `C.2.3` adopts that gradient while keeping the characteristic notation-agnostic and transdisciplinary.

### C.2.3:12 - Relations

- **Defines:** the `F` coordinate of the typed `F-G-R` assurance tuple.
- **Builds on:** characteristic machinery from `A.18` / `A.19` and episteme-level characteristic assignment from Part C.
- **Coordinates with:** `C.2.2`, `B.3`, `F.9`, `C.2.LS`, `A.16`, `C.2.4`, `C.2.5`, `C.2.6`, and `C.2.7`.
- **Constrains:** any pattern, gate, or editorial rule that speaks about rigor of expression.

### C.2.3:13 - Canonical Anchors `F0...F9`

> **Reading rule.** Anchors are ordinal. They say what is minimally true of the expression form, not what is true of the world.

#### C.2.3:13.1 - `F0` - Unstructured prose

Free natural language with unstable vocabulary, implicit assumptions, and no stable internal structure.

#### C.2.3:13.2 - `F1` - Scoped notes

Still informal, but with stable topic focus and more consistent terminology. Scope is named even though criteria are not yet operationalized.

#### C.2.3:13.3 - `F2` - Structured outline

A recognizable template or full section shape exists. The expression is coherent end-to-end, but acceptance criteria are still largely placeholders or informal.

#### C.2.3:13.4 - `F3` - Controlled narrative

Claims are expressed in constrained prose with stable interpretation. Acceptance or refusal conditions are visible in language, even if not yet fully predicate-like.

#### C.2.3:13.5 - `F4` - First-order constraints

Critical claims can be rendered as explicit predicates or invariants over typed entities. Consistency and conflict are at least checkable in principle.

#### C.2.3:13.6 - `F5` - Executable math / algorithmics

The expression has declared executable semantics. Running the model, algorithm, or simulation is part of its meaning.

#### C.2.3:13.7 - `F6` - Hybrid formalism

Several formal layers are coordinated explicitly, typically discrete plus continuous or several tightly coupled formal subsystems, with declared obligations between them.

#### C.2.3:13.8 - `F7` - Higher-order verified

Core claims are encoded in a proof-capable higher-order setting and machine-checked against that logic kernel.

#### C.2.3:13.9 - `F8` - Dependent / constructive proofs

Programs-as-proofs or dependent-type expressions carry the relevant property in their types or proof terms.

#### C.2.3:13.10 - `F9` - Univalent / higher foundations

Higher-equality foundations are load-bearing. The expression relies on a frontier-grade setting where equivalence is handled as structure-level identity.

#### C.2.3:13.11 - Cross-anchor cautions

- Execution is not proof.
- Surface structure is not yet semantics.
- Publishing or approval is not an anchor.
- A local sub-anchor does not erase its parent anchor's meaning.

### C.2.3:14 - Assigning `F` in Practice

#### C.2.3:14.1 - First-pass questions

1. **Can a competent reader misread the claim materially?**
   If yes, the expression is likely at `F0-F2`; if not, it may be `F3` or above.
2. **Are the critical claims visible as explicit predicates or invariants?**
   If yes, the expression is at least `F4`.
3. **Does the expression have declared executable semantics?**
   If yes, it is likely in the `F5-F6` region.
4. **Would a logic kernel or type checker reject an incorrect change to a core claim?**
   If yes, the expression is likely `F7-F8`, or `F9` if higher-equality machinery is essential.

#### C.2.3:14.2 - Quick rubric

- No full structure -> `F0-F1`
- Full structure but mostly placeholder criteria -> `F2`
- Controlled prose with one stable reading -> `F3`
- Explicit predicates / invariants -> `F4`
- Declared executable semantics -> `F5`
- Hybrid / layered formal obligations -> `F6`
- Machine-checked proof core -> `F7`
- Dependent proof-carrying core -> `F8`
- Higher-equality foundations are essential -> `F9`

#### C.2.3:14.3 - Typical delta-`F` moves

- `F2 -> F3`: replace loose prose with controlled phrasing and explicit acceptance statements.
- `F3 -> F4`: recast acceptance into typed predicates or invariants.
- `F4 -> F5`: give the expression declared executable semantics.
- `F5 -> F6`: make multi-layer obligations explicit.
- `F6 -> F7/F8`: move critical claims into machine-checked proof or dependent-type form.

### C.2.3:15 - Composition and Interaction

#### C.2.3:15.1 - Weakest-essential-support rule

For a composite episteme, the effective `F` is bounded by the least-formal essential support on the relevant support path. A highly formal annex does not lift an informal essential claim core.

#### C.2.3:15.2 - Relation to `G`

`F` concerns expression form; `G` concerns applicability or claim scope. Tightening scope may accompany a raise in `F`, but it is a separate change and must remain visible as such.

#### C.2.3:15.3 - Relation to `R`

Higher `F` often makes evidence easier to formulate, test, or prove, but it does not create warrant strength by itself. Empirical freshness, corroboration, and bridge penalties remain `R` concerns.

#### C.2.3:15.4 - Relation to `CL` and Bridges

A bridge may expose loss or mismatch across contexts. Those losses affect `R`; they do not silently lower or raise the attributed `F`. If the receiving context must materially rewrite the claim, it should publish a new episteme with its own `F`.

### C.2.3:16 - Worked Examples

#### C.2.3:16.1 - Research hypothesis

A short note proposing a new scaling law with one stable reading and explicit acceptance conditions in prose is typically `F3`. Rewriting the acceptance conditions as typed predicates would move it toward `F4`.

#### C.2.3:16.2 - Interface specification

An interface specification with explicit preconditions, postconditions, and invariants is typically `F4`. Adding declared executable semantics in a faithful reference model may move it toward `F5`.

#### C.2.3:16.3 - Safety controller

A controller coupled to a plant model with explicit hybrid obligations is typically `F6`. If key invariants are then machine-checked in a higher-order proof environment, those claims move toward `F7`.

#### C.2.3:16.4 - Decision policy

A decision policy with controlled prose may remain `F3`. If thresholds and conditions are published as typed predicates, it becomes `F4`.

#### C.2.3:16.5 - Proof-bearing algorithm

A dependent-typed algorithm whose central property is carried by the type itself is typically `F8`.

#### C.2.3:16.6 - Executable ML recipe

A fully explicit training-and-evaluation recipe with declared execution semantics is typically `F5`. It does not become `F7` merely because the surrounding execution machinery is sophisticated.

### C.2.3:17 - Authoring and Review Guidance

#### C.2.3:17.1 - For authors

Declare `F` honestly and early. A low `F` declaration is not a defect; it is often the correct statement about an early expression. Raise `F` by changing the expression form itself, not by applying prestige language or by pointing to surrounding machinery.

#### C.2.3:17.2 - For reviewers

Review the actual claim core. Ask whether the target anchor semantics are visibly satisfied, whether essential support contains segments with lower `R`, lower `F`, or missing witness coverage, and whether status or other characteristics have leaked into the `F` declaration.

#### C.2.3:17.3 - For integrators and assurance leads

Use `F` explicitly in gates and composition analysis, but do not let it absorb work that belongs to `G`, `R`, `CL`, or `C.2.LS`. Large `F` gaps across collaborating epistemes are signals for explicit formalization work, not excuses for wishful leveling.

### C.2.3:18 - Glossary and Notation

- **`U.Formality` / `F`.** The rigor-of-expression characteristic governed by this pattern.
- **Anchor.** A named ordinal milestone on the `F` ladder.
- **Sub-anchor.** A context-local refinement docked to one parent anchor.
- **Delta-`F`.** A content change that alters expression rigor.
- **Essential support.** The support without which the central claim does not stand.
- **Example notation.** `F = F4`, `F = F7[HOL]`, `requires F >= F6`.

### C.2.3:19 - Change Log and Patch Notes

#### C.2.3:19.1 - Supersession of legacy ladder language

This pattern supersedes deprecated wording that speaks about alternate formality modes, tiers, or editorial ladders. Forward-looking use should speak in `F` directly.

#### C.2.3:19.2 - Migration guidance

When refreshing legacy material, assign an initial `F` from observable content, rewrite local maturity labels into explicit `F` declarations, and keep provenance notes only as historical annotations rather than live rigor surrogates.

#### C.2.3:19.3 - Boundary to language-state facets

For the language-space extension, `F` does **not** govern `U.ArticulationExplicitness`, `U.LanguageStateClosureDegree`, `U.LanguageStateAnchoringMode`, or `U.LanguageStateRepresentationFactorBundle`. Contexts **MUST NOT** hide thresholds for those facets as pseudo-levels or submodes of `F`; those facets remain explicitly governed by `C.2.LS` and its subordinate patterns.

### C.2.3:End


## C.2.LS - `U.LanguageStateFacetProfile` - Thin profile bundle for language-state facets

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state facet profile.


### C.2.LS:1 - Problem frame
Once position claims in the declared language-state chart over `U.CharacteristicSpace` must be published and compared, teams need one thin profile bundle that keeps the relevant facets visible as one explicit facet profile without turning that profile into a second characteristic calculus or a surrogate maturity progression.

### C.2.LS:2 - Problem
Without a dedicated profile bundle, authors blur articulation, closure, anchoring, and representation into one vague maturity story, or they silently reuse `F` as a surrogate. That blocks admissible threshold publication, undercuts `A.16` move guards, and makes school-to-school bridge work harder than it needs to be.

### C.2.LS:3 - Forces
| Force | Tension |
|---|---|
| **Thin profile bundle vs practical coordination** | Keep the bundle small, but still give one stable place where the language-state facets are named together. |
| **Reuse vs duplication** | Reuse `A.18/A.19` characteristic machinery and `E.18` path publication rather than building a rival calculus. |
| **Local thresholds vs cross-context comparability** | Contexts need local thresholds, but the facet names must stay stable enough for bridge work and viewpoint bundles. |

### C.2.LS:4 - Solution
`U.LanguageStateFacetProfile` is a typed profile bundle that names the facets by which position claims in the declared language-state chart over `U.CharacteristicSpace` are published and interpreted:

- `formalityRef` -> `U.Formality` from `C.2.3`
- `articulationExplicitnessRef` -> `U.ArticulationExplicitness` from `C.2.4`
- `languageStateClosureDegreeRef` -> `U.LanguageStateClosureDegree` from `C.2.5`
- `languageStateAnchoringModeRef` -> `U.LanguageStateAnchoringMode` from `C.2.6`
- `languageStateRepresentationFactorBundleRef` -> `U.LanguageStateRepresentationFactorBundle` from `C.2.7`
- `thresholdRefs?` -> context-local threshold declarations over the governed facets
- `routeNotes?` -> informative notes that help interpret routing or reopening decisions

`C.2.LS` is therefore a **profile-bundle governing pattern**, not a characteristic governing pattern and not a trajectory governing pattern. Characteristic semantics remain with `A.18/A.19`; admissible moves remain with `A.16`; explicit path publication remains with `E.18`.

#### C.2.LS:4.1 - Governing boundary
`C.2.LS` governs only the profile composition and the rule that the language-state facets must remain explicit and non-collapsed. It does **not**:

- redefine `F`;
- invent a second formality progression;
- govern the scale semantics of `AE`, `CD`, `LanguageStateAnchoringMode`, or `U.LanguageStateRepresentationFactorBundle`;
- govern reopen/backoff moves;
- govern endpoint classification or bridge kinds.

#### C.2.LS:4.2 - Threshold publication discipline
Any threshold used for routing, admissible move guards, or entry into `A.6.P` shall be published on explicit named facets within the profile. Contexts shall not speak of hidden sub-levels of `F` when what matters is really articulation, closure, anchoring, or the representation-factor bundle.

#### C.2.LS:4.2.a - Local profile-reading witness
For this pattern, a published facet profile is reviewable when:

- the facet refs are explicit or explicitly inherited from an already pinned upstream publication;
- any threshold-bearing use names the facet whose threshold is being invoked;
- route notes or local overlays remain informative and visibly docked to the explicit facet bundle;
- and the profile does not smuggle move rules, bridge rules, gate state, or downstream governing-pattern semantics into the bundle record.

A polished label, one strong facet, or one memorable route note does not by itself yield an admissible profile reading. The profile remains conformant only when the named facets stay explicit and decomposable.

#### C.2.LS:4.3 - Composite readings
A language-state judgement may be composite, but the composite shall be decomposable. For example, a cue may be:

- low `AE`,
- medium `CD`,
- `AM.TraceAnchored`,
- and representation-wise mixed rather than purely symbolic.

A conforming profile makes this decomposition visible rather than hiding it under one poetic label such as "early" or "raw".

#### C.2.LS:4.4 - Corridor map note
`C.2.LS` participates in the current `Language-State & Semantic Routing Corridor`, but only as the thin governing pattern of the facet-profile bundle. Readers who need one map of the full language-state governing-pattern set should read the corridor note in `C.2.2a`.

That map does not change the governing boundary here: `C.2.LS` still does not govern cue preservation, route-bearing publication, prompt entry, or downstream endpoint handoff.

### C.2.LS:5 - Archetypal Grounding
**Tell.** A team may say a draft is "still forming" for different reasons. `U.LanguageStateFacetProfile` forces the team to say whether the issue is low articulation, low candidate-space closure, an anchoring mismatch, or an unresolved representation-factor bundle.

**Show (System).** An operator alert note can be `AM.OperatorLoop` anchored and low-closure without being low-formality in every respect.

**Show (Episteme).** An inquiry note can be low articulation yet already tightly anchored to exemplars and traces.

### C.2.LS:6 - Bias-Annotation
The pattern biases authors toward explicit facet governance and away from master-scale stories. That cost is intentional: the goal is to prevent surrogate progressions from entering the Core.

### C.2.LS:7 - Conformance Checklist
- `CC-C.2.LS-1` A language-state facet profile **SHALL** reference explicit facet governing patterns rather than invent local unnamed factors.
- `CC-C.2.LS-2` `C.2.LS` **MUST NOT** redefine `F` or create a second formality progression.
- `CC-C.2.LS-3` Thresholds that matter for routing, reopening, or lexical repair **SHALL** be published on explicit facets.
- `CC-C.2.LS-4` Trajectory accounts that rely on facet profiles **SHOULD** reuse `A.16` move kinds and `E.18` path publication rules.
- `CC-C.2.LS-5` Composite labels such as `early`, `settled`, or `ready` **SHALL NOT** stand in for the explicit facet bundle when those states matter operationally.
- `CC-C.2.LS-6` Composite readings, overlays, and route notes **SHALL** remain decomposable into named facets and **MUST NOT** behave as hidden master factors.
- `CC-C.2.LS-7` A profile bundle **MUST NOT** smuggle move rules, bridge rules, gate state, or downstream governing-pattern semantics into what should remain a thin facet-profile record.

### C.2.LS:8 - Common Anti-Patterns and How to Avoid Them
- **Shadow progression.** Treating `early/late` as a master scale. Split the judgement into the named facets.
- **Formality capture.** Letting `F` stand in for closure or articulation. Publish those facets explicitly.
- **Bundle inflation.** Turning `U.LanguageStateFacetProfile` into a second `A.19`. Keep it thin and referential.
- **Opaque readiness.** Using words such as `ready` or `mature` without naming which facet justifies the claim.
- **Route-note capture.** Letting an informative route note behave like move rule, gate state, or endpoint governance. Keep route notes informative and push operative authority back to `A.16`, downstream governing patterns, or gate/work governing FPF patterns or `authoritySourceRef` targets.

### C.2.LS:9 - Consequences
The benefit is authority-reference clarity: early cue work, bridge annotations, and reopen moves can all talk about one explicit facet profile. The trade-off is more explicit profile authoring and threshold publication.

### C.2.LS:10 - Rationale
The pattern gives the declared language-state chart over `U.CharacteristicSpace` one stable facet-profile record through which its facet bundle can be published together, while respecting the rest of FPF's governing boundaries.

### C.2.LS:11 - SoTA-Echoing

**SoTA note.** This section does not mint a second rule source. It is a load-bearing alignment statement: the Solution, Conformance Checklist, and boundary discipline of this pattern must match the stance stated here or explicitly justify divergence.

**Traditions covered.** This pattern binds itself to architecture-description governance, model-based systems engineering, and governance/profile discipline.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `C.2.LS` | Adoption status |
|---|---|---|---|---|
| Multi-facet state should be published through explicit profile elements rather than one summary stage label. | Contemporary architecture-description practice keeps the relevant properties, views, and correspondence evidence explicit instead of replacing them with one reader-facing maturity word. | ISO/IEC/IEEE 42010:2022 | `C.2.LS` adopts this by requiring explicit facet refs and by rejecting profile-by-vibe labels such as `ready` or `raw` when the bundle matters operationally. | **Adopt.** |
| Complex technical state is better captured through typed properties and decomposable profiles than one maturation rail. | Recent MBSE practice favours explicit properties, viewpoints, and cross-view consistency over one implicit staircase of readiness. | OMG SysML v2 (2025) | `C.2.LS` adapts this into a thin facet-profile bundle whose members remain decomposable and whose thresholds stay tied to named facets. | **Adapt.** |
| Governance-facing readiness should stay scoped and profile-based, not collapse into one global adjective. | Current governance frameworks use explicit profiles, scoped conditions, and local thresholds rather than one blanket readiness label. | NIST AI RMF 1.0 (2023) | `C.2.LS` adopts profile-level threshold publication and rejects the popular shortcut where one polished profile label substitutes for explicit facet talk. | **Adopt/Reject-popular-shortcut.** |

**Architecture-description governance.** `C.2.LS` adopts the discipline that useful state publication should keep the relevant profile elements explicit rather than hiding them inside one summary label.

**MBSE and profile discipline.** `C.2.LS` adapts typed multi-property state publication into a thin, decomposable language-state facet bundle rather than one master scale.

**Local stance.** The load-bearing SoTA claim for this pattern is narrow: best-known current practice treats language-state publication as a small explicit facet profile with local thresholds and decomposable readings, not as one maturity adjective or one route-coloured bundle label.

### C.2.LS:12 - Relations
- Builds on: `A.18`, `A.19`, `C.2.2a`, `C.2.3`.
- Coordinates with: `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `E.18`, `F.9.1`.
- Constrains: language-state threshold publication and profile composition.
### C.2.LS:13 - Worked Examples and Composition Notes

#### C.2.LS:13.1 - Operator-facing early alert
A console alert note may be published with a language-state facet profile such as:

- `F = F2/F3` because the note is structurally controlled but still lightweight;
- `AE = AE2` because candidate anchors are visible but not yet fully relation-shaped;
- `CD = CD1` because several routes remain live;
- `LanguageStateAnchoringMode = AM.OperatorLoop` because the note is directly anchored to operator intervention/work;
- `RepresentationFactorBundle = {local, sparse, mixed-symbolic}` because alert text and compact codes coexist.

This example shows why no one facet can replace the others. The note is not `simply early`; it is early in a specific, decomposable way.

#### C.2.LS:13.2 - Research cue before lexical repair
A felt or trace-anchored mismatch cue in an inquiry note may be:

- low `AE`,
- very low `CD`,
- `AM.EmbodiedFelt`,
- and representation-wise mixed because the cue is partly verbal, partly kinesthetic, partly exemplar-based.

That profile explains why the cue should remain in `A.16.1` rather than being forced into `A.6.P` or `B.5.2` immediately.

#### C.2.LS:13.3 - Architecture-description case
A viewpoint-bound note about the adequacy of an architecture description may be moderately high in `F`, moderately high in `AE`, still mid-level in `CD`, document-mediated in `AM`, and symbolic in its representation-factor bundle. The profile keeps description-side adequacy distinct from system-side engineering quality.

#### C.2.LS:13.4 - Same `F`, different profile
Two notes may share the same rough `F` band and still differ sharply in articulation, closure, anchoring, and representation factors. One may be operator-loop anchored and low-closure; another may be document-mediated and comparatively closed. The profile bundle keeps that difference visible instead of letting `F` behave like a master factor.

### C.2.LS:14 - Authoring and Review Guidance

#### C.2.LS:14.1 - For authors
When publishing a language-state facet profile:

1. start from the local authoring problem rather than from a memorized progression;
2. name the facet refs explicitly;
3. add threshold refs only when a threshold changes routing, repair, or governance;
4. avoid global labels such as "mature", "raw", or "ready" unless the profile decomposition is already visible.

#### C.2.LS:14.2 - For reviewers
A reviewer should ask:

- is any facet silently replaced by `F`?
- is a threshold published on an explicit facet rather than on a poetic surrogate?
- do route or reopen claims actually match the published facet bundle?
- are profile notes genuinely informative, or are they smuggling governing semantics that belong elsewhere?

#### C.2.LS:14.3 - For integrators
Integrators should preserve profile references rather than rephrasing them into local slang. A local alias is acceptable only if the underlying facet docking remains explicit and stable.

### C.2.LS:15 - Extension and Migration Notes

#### C.2.LS:15.1 - Local extension rule
Contexts may extend the profile with local threshold refs, route notes, or additional descriptive aids, but they shall not add a new master facet that collapses the governed set into one summary factor.

#### C.2.LS:15.2 - Migration from surrogate prose
Older prose often says:

- "the episteme is still early",
- "the issue is not mature enough",
- "the note is ready",
- "the cue is still raw".

A conforming migration rewrites such statements into explicit facet talk: which facet is low, which is high, which threshold is or is not met, and which move that fact justifies.

#### C.2.LS:15.3 - Boundary reminder
`U.LanguageStateFacetProfile` is a coordination record. If authors find themselves putting move rules, bridge rules, scale rules, or bundle semantics into the profile itself, they are writing in the wrong governing pattern.
### C.2.LS:16 - Profile Publication Package Discipline

#### C.2.LS:16.1 - Minimal publishable profile package
A publishable `U.LanguageStateFacetProfile` should normally carry:

- the declared facet refs for `AE`, `CD`, `LanguageStateAnchoringMode`, and `LanguageStateRepresentationFactorBundle`;
- any threshold refs that substantively affect routing, repair, bridge interpretation, or review load;
- the local relation to `F` when readers might otherwise treat `F` as a surrogate;
- any omission note when a facet is intentionally unpublished, unknown, or locally irrelevant.

One-line publication is admissible only if facet governance remains legible.

#### C.2.LS:16.2 - Partial-profile rule
A partial profile is admissible only when omission is explicit. Publishing `AE` and `CD` while deferring `LanguageStateAnchoringMode` is acceptable; silently omitting it and then speaking in scalar prose such as "early" or "ready" is not.

If only one facet is published, either explain why the others are not governed in the current note or point to the note where they are already published.

#### C.2.LS:16.3 - Overlay discipline
Local overlays such as "explicit-but-open", "trace-heavy", or "operator-tight" are admissible only when they dock to explicit facet refs. Overlays remain secondary to the governed profile and must not replace the facet bundle.

### C.2.LS:17 - Cross-Facet Reading Rule

#### C.2.LS:17.1 - No master-facet reading
Do not infer the whole language-state profile from one facet. High `AE` does not entail high `CD`; strong `AM.OperatorLoop` does not fix `AE` or `CD`; symbolic representation does not entail high `F`; low `CD` does not imply low operational consequence.

#### C.2.LS:17.2 - Threshold interaction rule
When a threshold is expressed over one facet, say whether the other facets are merely informative or also constraining. A Context may allow entry into `B.5.2.0` once `AE` suffices for an explicit open question while still capping `CD` so rival answers remain live; it may allow entry into `A.6.P` at `AE3+` while still capping `CD` so the move remains exploratory rather than endpoint-binding.

#### C.2.LS:17.3 - Transition reading rule
Read profile transitions facetwise. A note may become more explicit without becoming more closed, more document-mediated without changing closure, or more symbolic without becoming more formal. `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0` should therefore cite the facet transition that actually justifies the move.

### C.2.LS:18 - Review Matrix and Migration Tests

#### C.2.LS:18.1 - Review matrix
A reviewer should ask:

- is each published facet governed by its proper pattern rather than by surrogate prose;
- does any overlay smuggle a hidden scalar or gate decision;
- are threshold claims tied to the facet that really bears them;
- do cited moves in `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, or `B.5.2.0` actually match the facet bundle;
- if the profile crosses a bridge or viewpoint boundary, are stance and loss notes kept in `F.9` or `F.9.1` rather than imported as fake facets.

#### C.2.LS:18.2 - Migration test for old prose
Legacy phrases such as "still immature", "not ready yet", or "already stable enough" should be unpacked into: which facet is claimed, which anchor or bundle member justifies it, which threshold or route consequence follows, and which `governingPatternRef` or `authoritySourceRef` carries that consequence.

#### C.2.LS:18.3 - Comparative profile use
Compare profiles facetwise unless a Context has published an explicit local aggregation for reporting. Such an aggregation remains secondary and must not replace the profile in norms, thresholds, or bridge claims.

### C.2.LS:End

## C.2.4 - `U.ArticulationExplicitness`

> **Type:** Definitional (D)
> **Status:** Draft
> **Normativity:** Normative unless marked informative

**Plain-name.** Articulation explicitness.


### C.2.4:1 - Problem frame
A governed `U.Episteme` can already matter while its semantic shape is not yet fully explicit. The declared language-state chart over `U.CharacteristicSpace` therefore needs one basis-slot governing pattern for how explicit that shape already is, without confusing articulation with rigor, truth, or closure.

### C.2.4:2 - Problem
When articulation explicitness stays implicit, authors either overstate readiness for later repair or endpoint classification, or hide early cue structure entirely. Reusing `F` for this judgement creates a category error: formality is about rigor of expression, not about whether the semantic shape is already explicit enough for repair or endpoint classification.

### C.2.4:3 - Forces
| Force | Tension |
|---|---|
| **Early capture vs false precision** | Capture low-articulation cues without pretending they already have stable slots. |
| **Comparability vs local nuance** | Keep a shared ordinal discipline while allowing context-local threshold declarations. |
| **Repair readiness vs exploratory openness** | Name when an episteme is ready for `A.6.P` without forcing every cue into late forms. |

### C.2.4:4 - Solution
`U.ArticulationExplicitness` is an ordinal characteristic over how explicit the semantic shape is in a published position claim in the declared language-state chart over `U.CharacteristicSpace`, for publication, routing, and repair.

#### C.2.4:4.1 - Characteristic specification
- **Kind:** CHR characteristic.
- **Scale discipline:** ordinal.
- **What rises:** semantic shape becomes more explicit.
- **What does not follow automatically:** truth, trust, closure, admissibility, or formality.

`AE` is therefore independent from `F`, from `LanguageStateClosureDegree`, and from endpoint authority.

#### C.2.4:4.2 - Starter anchor set
| Anchor | Reading | Typical admissible publication state |
|---|---|---|
| `AE0` | felt, latent, or low-articulation cue only | still preservable, but not yet anchor-explicit |
| `AE1` | stable cue span, contrast, or disturbance cue is nameable | `U.PreArticulationCuePack` becomes natural |
| `AE2` | candidate anchors or partial roles are visible | cue pack with candidate anchors and route candidates |
| `AE3` | minimally relation-like skeleton exists | entry to `A.6.P` becomes possible if local threshold allows |
| `AE4` | slot-explicit normal form is publishable | explicit relation or characteristic form |
| `AE5` | articulation is explicit enough for stable endpoint classification and later bridge work | endpoint-pattern-governed publication becomes straightforward |

The anchors are a starter set; a Context may refine them locally, but it shall keep the ordinal direction and the distinction from `F` intact.

#### C.2.4:4.3 - Use discipline
- `AE` may be used to state entry conditions for `A.6.P`.
- `AE` may be used to justify why an episteme remains in `A.16.1` or `B.4.1`.
- `AE` shall not be used as a surrogate for closure, confidence, or truth.
- High `F` shall not be taken to imply high `AE`, and high `AE` shall not be taken to imply high `F`.

#### C.2.4:4.4 - Change discipline
Raising `AE` requires additional explicit anchors, slots, or normal-form structure. Lowering `AE` is admissible under `A.16.2` when a prior articulation proves over-committed or misleading.

### C.2.4:5 - Archetypal Grounding
**Tell.** "Something is off" may be a real cue even before role bearer, intended work move, reliance move, or evaluator are explicit.

**Show (System).** An operator alert cue grounded in a disturbance trace may be stabilized as a candidate intervention cue before a full work relation or reliance relation specification exists.

**Show (Episteme).** A research note may name a contrast and exemplars before it has a clean proposition.

### C.2.4:6 - Bias-Annotation
The pattern legitimizes early cues. The counter-bias is explicit: low `AE` never licenses hidden semantics or unreviewable leaps.

### C.2.4:7 - Conformance Checklist
- `CC-C.2.4-1` `AE` **SHALL NOT** be treated as a synonym for `F`.
- `CC-C.2.4-2` Entry into `A.6.P` **SHOULD** require at least the Context's declared articulation threshold.
- `CC-C.2.4-3` `AE` judgements that drive routing or repair **SHALL** cite the anchors, contrasts, or slots that justify the chosen level.
- `CC-C.2.4-4` Raising `AE` **SHALL NOT** be described as if it automatically settled closure or authority.

### C.2.4:8 - Common Anti-Patterns and How to Avoid Them
- **Formal-looking but semantically thin.** High `F`, low `AE`. Declare both.
- **Mystical cue immunity.** Low `AE` presented as exempt from authoring discipline. It is not.
- **Ready-by-tone.** A sentence sounds precise, so authors assume `AE3+`. Publish the actual anchors.

### C.2.4:9 - Consequences
The benefit is admissible publication of early cues and clearer threshold setting for repair. The trade-off is that authors must distinguish "not yet explicit" from "already formal".

### C.2.4:10 - Rationale
`AE` is one basis slot in the declared language-state chart over `U.CharacteristicSpace`. Without it, `A.16.0`, `A.16.1`, and `B.4.1` cannot state crisp entry, seam, and exit conditions.

### C.2.4:11 - SoTA-Echoing
The distinction echoes work on sketching, focusing/TAE, embodied cue capture, and representation probing: a cue can be real and operationally relevant before it becomes fully explicit.

### C.2.4:12 - Relations
- Builds on: `A.18`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `C.2.5`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `A.6.P`, `B.4.1`, `B.5.2.0`.
- Constrains: articulation thresholds for routing and repair.
### C.2.4:13 - Worked Examples and Edge Cases

#### C.2.4:13.1 - High formality, low articulation
A template may be syntactically precise and therefore high in `F`, yet still low in `AE` because the actual role-bearer, relation, or intended-work-or-reliance-move slots remain unclear. This is the classic case where formal-looking language overstates semantic readiness.

#### C.2.4:13.2 - Low formality, high articulation
A short, plain note may be low in `F` yet already high in `AE` because the relation skeleton is explicit enough for `A.6.P`. This case matters because it shows that `AE` is not a stylistic measure.

#### C.2.4:13.3 - Threshold edge case
A cue with stable trigger span and candidate anchors may still sit between `AE2` and `AE3`. A Context should then publish its local threshold rule explicitly rather than pretending that entry into `A.6.P` is obvious by tone.

### C.2.4:14 - Authoring and Review Guidance

#### C.2.4:14.1 - Author prompt
To assign `AE`, ask:

- is the trigger span stable?
- are candidate anchors visible?
- is there already a minimally relation-like skeleton?
- is a normal form actually publishable, or only hinted?

#### C.2.4:14.2 - Review prompt
A reviewer should reject `AE` claims that rely only on rhetorical confidence. The claimed level should be supported by anchors, slots, contrasts, exemplars, or explicit normal-form structure.

#### C.2.4:14.3 - Threshold publication reminder
If `AE` determines whether an episteme stays in `A.16.1`, passes through `B.4.1`, or enters `A.6.P`, that threshold should be published explicitly and locally.

### C.2.4:15 - Extension and Migration Notes

#### C.2.4:15.1 - Local anchor refinement
Contexts may refine the starter anchor set with subanchors, but the refinement must preserve the ordinal direction and the distinction from `F` and `CD`.

#### C.2.4:15.2 - Migration from vague articulation prose
Statements such as "still vague", "more explicit now", or "ready for formalization" should be migrated into explicit `AE` claims plus the corresponding move or routing claim.

#### C.2.4:15.3 - Boundary reminder
`AE` does not govern closure, confidence, or warrant. If authors want those meanings, they must publish them through their own governing patterns.
### C.2.4:16 - Articulation Publication Package Discipline

#### C.2.4:16.1 - Minimal articulation package
An `AE` claim that matters for routing or repair should normally publish more than a level token. The supporting package should indicate which of the following are present:

- stable trigger span;
- candidate anchors or contrasts;
- role-bearer / intended-work-or-reliance-move / evaluator slots where relevant;
- a minimally relation-like skeleton;
- a candidate normal form, or an explicit note that no such form is yet admissible.

A bare `AE3` label is a publication with insufficient articulation support when the supporting articulation evidence is absent.

#### C.2.4:16.2 - Threshold package for route change
If entry from `A.16.1` or `B.4.1` into `A.6.P` depends on `AE`, publish the threshold together with the minimum articulation package required at crossing time.

#### C.2.4:16.3 - Evidence-limited rise rule
`AE` may rise only as far as the published anchors, slots, and contrasts warrant. Stylistic polish, templates, or rhetorical confidence do not raise `AE` on their own.

### C.2.4:17 - Threshold Crossing and Split Handling

#### C.2.4:17.1 - Admissible entry into relational repair
Entry into `A.6.P` is admissible when the local articulation threshold is met and the note already exposes enough relation structure for precision restoration to operate on a real relation-like episteme. Entry into `B.5.2.0` is admissible when the open question is explicit enough for prompt-species publication even if relation structure is still too thin for `A.6.P`. If the threshold is borderline, keep the episteme in `B.4.1` or `A.16.1` and state what anchor or slot is still missing.

#### C.2.4:17.2 - High-articulation, low-closure cases
A note may reach `AE4+` while remaining low or mid in `CD`. In such cases state that articulation is sufficient for precise handling while closure still leaves rival routes or frames live.

#### C.2.4:17.3 - Split-publication rule
If one note contains a high-`AE` fragment and a low-`AE` remainder, split the publication rather than assigning one averaged level that hides the actual route structure.

### C.2.4:18 - Review Matrix and Endpoint Boundary Tests

#### C.2.4:18.1 - Review matrix
A reviewer should ask:

- are the named anchors genuinely present rather than merely presupposed;
- does the claimed articulation level rest on structure rather than tone;
- are role-bearer, intended-work-or-reliance-move, evaluator, or comparison slots still ghosted;
- if `AE` is used to justify route transfer, is the destination governing pattern actually ready to receive the publication.

#### C.2.4:18.2 - Endpoint-boundary test
High `AE` does not by itself authorize endpoint claims, gate pressure, or quality ascriptions. If such consequences appear, show which downstream governing pattern takes over.

#### C.2.4:18.3 - Migration note for false precision
Rigid templates, capitalized labels, or tidy sentence rhythm can simulate articulation. Migration should therefore test whether anchors and slots are really present; if not, the articulation level should drop.

### C.2.4:End

## C.2.5 - `U.LanguageStateClosureDegree`

> **Type:** Definitional (D)
> **Status:** Draft
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state closure degree.


### C.2.5:1 - Problem frame
A governed `U.Episteme` may already be explicit enough for publication while its declared position claim remains intentionally open to rival routes or frames. The declared language-state chart over `U.CharacteristicSpace` therefore needs a separate basis-slot governing pattern for how fixed or closed the current candidate space has become.

### C.2.5:2 - Problem
Closure is often hidden inside vague words such as "ready", "settled", or "open". When closure is not explicit, teams cannot reason cleanly about reopen, sketch-backoff, or the admissibility of endpoint docking.

### C.2.5:3 - Forces
| Force | Tension |
|---|---|
| **Commitment vs exploration** | Preserve open search without losing auditability. |
| **Stability vs reversibility** | Allow closure increases, but also admissible reopening and reframing. |
| **Authority vs explicit retreat** | Let strong closure matter, but keep visible the moves that relax it. |

### C.2.5:4 - Solution
`U.LanguageStateClosureDegree` is an ordinal characteristic over how fixed the current candidate set, framing, and admissible next moves are in a published position claim in the declared language-state chart over `U.CharacteristicSpace`.

#### C.2.5:4.1 - Characteristic specification
- **Kind:** CHR characteristic.
- **Scale discipline:** ordinal.
- **What rises:** the local state becomes more fixed or more binding.
- **What does not follow automatically:** truth, trust, formality, or quality.

#### C.2.5:4.2 - Starter anchor set
| Anchor | Reading | Typical governance effect |
|---|---|---|
| `CD0` | exploratory-open | broad rival space remains live |
| `CD1` | weakly stabilized | some contrasts are present, but rival routes remain normal |
| `CD2` | narrowed candidate space | explicit rivals remain, but the field is meaningfully reduced |
| `CD3` | selected route or framing | one route is chosen, though reopening remains routine |
| `CD4` | publication- or operation-fixed under guard | changes require named justification |
| `CD5` | strongly fixed | relaxation requires an explicit `A.16.2` move and governance note |

#### C.2.5:4.3 - Non-collapse rules
`LanguageStateClosureDegree` is not:

- `F`;
- articulation explicitness;
- gate decision;
- evaluator confidence;
- warrant strength.

A text may be highly explicit but low-closure, or low-explicitness but already high-closure by policy. Those states shall not be collapsed.

#### C.2.5:4.4 - Change discipline
Increasing `CD` requires narrowing candidate space, route space, or frame space explicitly. Lowering `CD` is admissible only through a named move such as `reopen`, `sketchBackoff`, or `respecify`, with a retained-witness and discarded-assumption note.

### C.2.5:5 - Archetypal Grounding
**Tell.** Two notes may look equally explicit, but one is still intentionally open while the other is already committed to a single route.

**Show (System).** An incident cue can be routed to rollback while remaining reopenable if new evidence arrives.

**Show (Episteme).** A hypothesis sketch can be highly articulated but still low closure because rival explanations remain live.

### C.2.5:6 - Bias-Annotation
The pattern makes closure explicit, which resists hidden overconfidence but may feel heavy to authors who prefer implicit consensus.

### C.2.5:7 - Conformance Checklist
- `CC-C.2.5-1` Closure **SHALL** be declared independently from `F` and `AE` when it matters for routing, docking, or reopening.
- `CC-C.2.5-2` Reopen/backoff moves **SHALL** cite the prior closure state they are relaxing.
- `CC-C.2.5-3` Strong-closure states **SHOULD** name the guard, `governingPatternRef`, or `authoritySourceRef` that makes the closure binding.
- `CC-C.2.5-4` Endpoint authority **SHALL NOT** survive a closure drop silently when the supporting route or publication form no longer holds.

### C.2.5:8 - Common Anti-Patterns and How to Avoid Them
- **Closure by mood.** A sentence sounds decisive, so teams assume high closure. Publish `CD` explicitly.
- **Irreversible drift.** Closure rises informally but no reopen path exists. Use `A.16.2`.
- **Authority smuggling.** High closure is treated as if it were automatically a gate or obligation. Route those consequences through the proper governing patterns.

### C.2.5:9 - Consequences
The benefit is admissible handling of stabilization, commitment, and reopening. The trade-off is more explicit state declaration and more explicit retreat records.

### C.2.5:10 - Rationale
Closure is the route-governance basis slot that complements articulation within the declared language-state chart over `U.CharacteristicSpace`. `A.16.0` and its seam species need both.

### C.2.5:11 - SoTA-Echoing
The facet aligns with iterative design, open-world reasoning, and exploratory search practices where closure is a governance choice rather than a hidden by-product.

### C.2.5:12 - Relations
- Builds on: `A.18`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `C.2.4`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`.
- Constrains: reopen, backoff, and endpoint docking guards.
### C.2.5:13 - Worked Examples and Retreat Cases

#### C.2.5:13.1 - Explicit but still open
A note may sit at `AE4` yet only `CD1` because rival explanatory frames are still live. The important lesson is that explicit publication does not imply settled closure.

#### C.2.5:13.2 - Strong closure under policy guard
An operator rule may be only moderate in `AE` but high in `CD` because policy already fixes the next step under the current horizon. This shows why closure is governance-facing, not merely stylistic.

#### C.2.5:13.3 - Reopen case
A route may move from `CD4` back to `CD2` when counter-evidence appears. A conforming publication does not hide this as embarrassment; it records the retreat as an admissible `A.16.2` move.

### C.2.5:14 - Authoring and Review Guidance

#### C.2.5:14.1 - Author prompt
To assign `CD`, ask:

- how many rivals remain live?
- is one route merely preferred, or actually fixed?
- what guard, `governingPatternRef`, or `authoritySourceRef` makes the closure binding?
- what would count as an admissible reopen trigger?

#### C.2.5:14.2 - Review prompt
A reviewer should ask whether closure is being inferred from tone, from hierarchy, or from social pressure rather than from an explicit narrowing of route or frame space.

#### C.2.5:14.3 - Governance note
Whenever `CD` substantively affects gates, commitments, or late endpoint authority, the supporting guard, `governingPatternRef`, or `authoritySourceRef` should be visible.

### C.2.5:15 - Extension and Migration Notes

#### C.2.5:15.1 - Local anchor refinement
Contexts may refine the starter closure anchors, but shall keep the ordinal progression and the explicit link to reopen/backoff discipline.

#### C.2.5:15.2 - Migration from readiness language
Words such as "settled", "closed", "final", or "open" should be treated as migration prompts into explicit `CD` claims and, where needed, into named `A.16.2` moves.

#### C.2.5:15.3 - Boundary reminder
`CD` is not warrant strength and not a gate decision. It speaks only about the local fixity of the current episteme/publication path and its candidate space.
### C.2.5:16 - Closure Publication Package Discipline

#### C.2.5:16.1 - Minimal closure package
A publishable `CD` claim should name what has narrowed:

- the rival routes or frames that remain live;
- the route, frame, or interpretation that is currently privileged or fixed;
- the guard, `governingPatternRef`, `authoritySourceRef`, or policy that makes the narrowing binding;
- the condition under which an admissible reopen or backoff would occur.

A bare claim such as "now settled" is insufficient when closure affects routing or authority.

#### C.2.5:16.2 - Narrowing-source rule
Closure may rise because evidence eliminates rivals, governance temporarily binds a route, or protocol requires fixation under time pressure. State the source of narrowing because different sources imply different reopen expectations.

#### C.2.5:16.3 - Partial-closure rule
Closure may be local rather than global. A note can be closed enough for one route while remaining open about broader explanation or classification; a prompt may be fixed enough to hold one question steady while still open enough that rival answers remain live. Publish that locality explicitly.

### C.2.5:17 - Retained and Withdrawn Authority Handling

#### C.2.5:17.1 - Authority retention rule
If higher `CD` carried endpoint expectations, guard pressure, or route commitments, a later closure drop must say which consequences remain and which are withdrawn.

#### C.2.5:17.2 - Admissible retreat record
An admissible retreat through `reopen`, `sketchBackoff`, or `respecify` should retain:

- the prior closure state;
- the reason the prior fixation no longer holds;
- the assumption or route being relaxed;
- the still-binding remainder, if any.

This prevents false continuity after retreat.

#### C.2.5:17.3 - Closure versus obligation boundary
High `CD` may coexist with obligations, but `CD` is not itself an obligation-bearing governing FPF pattern or `authoritySourceRef` target. When prose treats "closed" as "must now be done", name the actual `governingPatternRef` or `authoritySourceRef` for that claim.

### C.2.5:18 - Review Matrix and Reopen Tests

#### C.2.5:18.1 - Review matrix
A reviewer should ask:

- what was narrowed;
- by what `governingPatternRef`, `authoritySourceRef`, or guard it was narrowed;
- what would reopen it;
- whether any gate, release, work, evidence, assurance, policy, or adjudication authority survives the claimed closure level;
- whether the publication distinguishes local closure from whole-context finality.

#### C.2.5:18.2 - False-finality test
Words such as "final", "settled", or "decided" should be challenged unless the route/guard package is explicit. Final-sounding rhetoric often overstates actual closure.

#### C.2.5:18.3 - Cross-facet reminder
Low `CD` does not imply low articulation, low anchoring, or poor representation. Reviewers should not treat openness as low seriousness.

#### C.2.5:18.4 - Split-closure review case
A publication may be closed enough for immediate local work use or reliance use while remaining open about broader explanation, long-horizon consequences, or alternative classification. Allow the split when locality is explicit; reject prose that advertises whole-case finality when only one language-state segment is fixed.

### C.2.5:End

## C.2.6 - `U.LanguageStateAnchoringMode`

> **Type:** Definitional (D)
> **Status:** Draft
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state anchoring mode.


### C.2.6:1 - Problem frame
Published position claims in the declared language-state chart over `U.CharacteristicSpace` differ not only by articulation and closure, but by how the governed `U.Episteme` in that claim is anchored to bodies, traces, model states, documents, or operator loops.

### C.2.6:2 - Problem
Without an explicit anchoring-mode declaration, embodiment and source anchoring are smuggled into informal prose or folded into representation terms. That undercuts cue comparison, undercuts bridge loss notes, and turns operator-facing language-state work into a special case with no explicit governing-pattern relation.

### C.2.6:3 - Forces
| Force | Tension |
|---|---|
| **Embodiment vs abstraction** | Preserve embodied and operator-facing cases without making them mystical exceptions. |
| **Small core vs real diversity** | Keep the core compact while allowing multiple admissible anchoring regimes. |
| **Comparability vs oversimplification** | Compare anchoring regimes without flattening them into text-vs-nontext slogans. |

### C.2.6:4 - Solution
`U.LanguageStateAnchoringMode` is a nominal characteristic that states the primary anchoring regime of the governed `U.Episteme` named by the current position claim: bodily enactment, trace, model state, document, operator loop, or an explicit mixed regime. If source anchoring and current publication-face anchoring differ, both shall be distinguished rather than collapsed.

#### C.2.6:4.1 - Starter family
| Mode | Reading | Typical evidence anchor |
|---|---|---|
| `AM.EmbodiedFelt` | bodily or kinesthetic anchoring matters directly | embodiment note, felt trace, human witness |
| `AM.TraceAnchored` | traces, logs, telemetry traces, or observations anchor the episteme | trace references, measured events, observations |
| `AM.ModelLatent` | latent or internal model state is the key anchor | model-state refs, probe results, latent summaries |
| `AM.DocumentMediated` | document or description is the principal anchor | documents, cards, method-description text |
| `AM.OperatorLoop` | the episteme is directly tied to operator intervention or console control | operator witness, console event, policy hook |
| `AM.Mixed` | more than one anchoring mode matters substantively | explicit component list and why the mix matters |

#### C.2.6:4.2 - Governing boundary
`U.LanguageStateAnchoringMode` is not a representation factor bundle, not a closure state, and not a truth status. If embodiment matters, it shall be declared here or immediately beside this characteristic rather than being hidden inside representation talk.

#### C.2.6:4.3 - Mixed-mode rule
`AM.Mixed` is admissible only when the component modes are named explicitly. "Mixed" shall not be a lazy escape from deciding whether the key anchor is bodily, trace-based, model-latent, document-mediated, or operator-loop based.

#### C.2.6:4.4 - Bridge implications
Bridge work over governed `U.Episteme` publications in the declared language-state chart should pay attention to anchoring shifts. A translation from `AM.EmbodiedFelt` to `AM.DocumentMediated`, or from `AM.ModelLatent` to prose, often requires explicit loss notes in `F.9` and often justifies a stance annotation in `F.9.1`.

### C.2.6:5 - Archetypal Grounding
**Tell.** A felt cue, a controller-side probe score, and a textual design note may all be early cues, but they are anchored differently.

**Show (System).** An alert tied to an operator console is `AM.OperatorLoop`, not just "text".

**Show (Episteme).** A model-probe cue grounded in latent state is `AM.ModelLatent` even if it is later paraphrased into prose.

### C.2.6:6 - Bias-Annotation
The pattern pushes authors to declare anchoring rather than hide it in metaphors such as "the system wants" or "the note suggests".

### C.2.6:7 - Conformance Checklist
- `CC-C.2.6-1` Anchoring mode **SHALL NOT** be inferred from publication phrasing alone when it matters for routing, trust, or bridge interpretation.
- `CC-C.2.6-2` Embodiment-sensitive or operator-loop cases **SHOULD** declare the embodiment or operator anchor explicitly.
- `CC-C.2.6-3` `U.LanguageStateAnchoringMode` **MUST NOT** be collapsed into `U.LanguageStateRepresentationFactorBundle`.
- `CC-C.2.6-4` Mixed-mode declarations **SHALL** list their component modes explicitly.

### C.2.6:8 - Common Anti-Patterns and How to Avoid Them
- **Text-only illusion.** Treating every cue as document-mediated because it was written down later.
- **Representation capture.** Using symbolic/distributed labels to hide world-anchoring distinctions.
- **Embodiment mystification.** Treating bodily or operator-loop cues as beyond explicit publication.

### C.2.6:9 - Consequences
The benefit is cleaner reasoning about embodied, operator-facing, trace-based, and model-latent cues. The trade-off is more explicit declaration work and more explicit bridge loss notes when modes shift.

### C.2.6:10 - Rationale
The declared language-state chart over `U.CharacteristicSpace` needs one explicit anchoring basis slot so that `A.16.0`, `A.16.1`, `B.4.1`, and `F.9.1` can refer to anchoring regime without redefining it.

### C.2.6:11 - SoTA-Echoing
The facet is motivated by embodied cognition, operator-facing interaction practice, active inference, and modern model-probing practice, all of which distinguish cue content from anchoring regime.

### C.2.6:12 - Relations
- Builds on: `A.18`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `A.7`, `A.16.0`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, `C.2.7`, `F.9.1`.
- Constrains: cue publication and bridge loss notes.
### C.2.6:13 - Worked Examples and Bridge-Loss Cases

#### C.2.6:13.1 - Embodied-to-document shift
A bodily felt cue later published as prose usually changes from `AM.EmbodiedFelt` toward `AM.DocumentMediated`. That shift is not harmless; it often introduces bridge loss and should be treated as such when cross-context equivalence is claimed.

#### C.2.6:13.2 - Model-latent to operator-loop case
A latent probe score may first be `AM.ModelLatent`, then later feed an operator-facing alert face where the working publication becomes `AM.OperatorLoop`. A conforming account should keep both anchoring modes visible rather than pretending the later publication wording fully captures the model-side cue.

#### C.2.6:13.3 - Mixed-mode publication
A routed alert note may admissibly be `AM.Mixed` when it combines operator-loop anchoring, trace anchoring, and document mediation. But the mix must be named explicitly rather than used as a catch-all escape.

### C.2.6:14 - Authoring and Review Guidance

#### C.2.6:14.1 - Author prompt
When declaring anchoring mode, ask:

- what is the primary anchor kind?
- does bodily or operator participation matter directly?
- is the key anchor trace-based, model-internal, or document-based?
- if multiple modes matter, which ones and why?

#### C.2.6:14.2 - Review prompt
A reviewer should watch for the common mistake where later prose formatting tricks authors into forgetting the original anchoring mode.

#### C.2.6:14.3 - Bridge note
If anchoring changes across publication or translation, `F.9` and `F.9.1` should often carry explicit loss or stance notes rather than silent equivalence language.

### C.2.6:15 - Extension and Migration Notes

#### C.2.6:15.1 - Local extension rule
Contexts may add local anchoring modes, but they should do so by extension of the starter family rather than by collapsing the family into a text-vs-world binary.

#### C.2.6:15.2 - Migration from metaphorical prose
Statements like "the system wants", "the note suggests", or "the operator-facing publication says" should be repaired by naming the actual anchoring mode and the actual detector/enactor or witness structure.

#### C.2.6:15.3 - Boundary reminder
`U.LanguageStateAnchoringMode` does not decide representation, articulation, closure, or trust by itself. It only names how the episteme is anchored.
### C.2.6:16 - Anchoring Publication Package Discipline

#### C.2.6:16.1 - Minimal anchoring package
A publishable `U.LanguageStateAnchoringMode` claim should normally identify:

- the primary anchor kind;
- any directly relevant embodiment, operator, trace, model, or document witness;
- the transformation chain if the current note is not at the original anchoring site;
- any secondary modes that remain load-bearing.

This is especially important when the final wording is prose, because prose often hides the anchoring regime.

#### C.2.6:16.2 - Source-versus-face rule
Distinguish the anchoring mode of the source cue from the anchoring mode of the current publication face. A bodily cue later written into a document may still require `AM.EmbodiedFelt` as source mode and `AM.DocumentMediated` as publication face.

#### C.2.6:16.3 - Mixed-mode decomposition rule
`AM.Mixed` is admissible only when its component modes are named and the reason for the mixture is operationally real. It must not become a convenience label for an episteme that has not yet been analyzed.

### C.2.6:17 - Anchoring Shift and Transport Discipline

#### C.2.6:17.1 - Shift declaration rule
When an episteme crosses from one anchoring mode to another, state whether the shift is merely publication-level or whether it changes what can be preserved, compared, or trusted. A move from operator-loop enactment to report prose, for example, often drops timing, bodily load, and enactment friction.

#### C.2.6:17.2 - Bridge-loss handoff
If an anchoring shift matters across contexts, `F.9` or `F.9.1` should govern the loss or stance note. `C.2.6` only requires the shift to be noticed and not misrepresented as lossless.

#### C.2.6:17.3 - Same-content illusion test
Two cues may be paraphrased into the same sentence while remaining differently anchored. If the anchoring regime differs, the cues are not automatically substitutable.

### C.2.6:18 - Review Matrix and Extension Tests

#### C.2.6:18.1 - Review matrix
A reviewer should ask:

- what the original anchoring regime was;
- what the current publication regime is;
- whether the transformation chain is explicit;
- whether any bridge loss or stance note is missing;
- whether a declared mixed mode is genuinely decomposed.

#### C.2.6:18.2 - Local extension test
A new local anchoring mode is justified only when it answers a distinct anchoring question that the starter family cannot express without distortion.

#### C.2.6:18.3 - Cross-facet reminder
Anchoring mode often correlates with representation and articulation changes, but it does not govern them. Reject prose that uses `AM.ModelLatent`, `AM.EmbodiedFelt`, or `AM.OperatorLoop` as shorthand for being vague, early, trustworthy, or closed.

### C.2.6:End

## C.2.7 - `U.LanguageStateRepresentationFactorBundle`

> **Type:** Definitional (D)
> **Status:** Draft
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state representation-factor bundle.


### C.2.7:1 - Problem frame
Published position claims in the declared language-state chart over `U.CharacteristicSpace` must distinguish representation factors such as locality, sparsity, and symbolicity without pretending they form one master factor.

### C.2.7:2 - Problem
Terms such as `EncodingBasis` collapse several independent choices. That makes comparison brittle and encourages one-factor stories such as distributed = informal or local = precise.

### C.2.7:3 - Forces
| Force | Tension |
|---|---|
| **Comparability vs reductionism** | Allow comparison without compressing several factors into one slogan. |
| **Compact core vs extensibility** | Keep a minimal starter bundle while leaving room for domain-specific refinements. |
| **Representation vs anchoring** | Describe how the current episteme is represented without hiding what it is anchored to. |

### C.2.7:4 - Solution
`U.LanguageStateRepresentationFactorBundle` is a factor bundle, not one scalar characteristic. The minimal core starter set is:

- `U.LocalityDistribution`
- `U.Sparsity`
- `U.Symbolicity`

A Context may publish a local alias such as `EncodingBasis`, but it shall dock back to the underlying factor bundle instead of replacing it.

#### C.2.7:4.1 - Minimal factor readings
| Factor | Question it answers | Typical values |
|---|---|---|
| `LocalityDistribution` | Is the representation concentrated in local units or distributed across many units? | local / mixed / distributed |
| `Sparsity` | How concentrated is activation or descriptive support? | sparse / mixed / dense |
| `Symbolicity` | How explicit are the symbolic structures and tokens? | symbolic / mixed / subsymbolic |

#### C.2.7:4.2 - Non-collapse rules
`LanguageStateRepresentationFactorBundle` is not:

- `LanguageStateAnchoringMode`;
- `Formality`;
- `ArticulationExplicitness`;
- `LanguageStateClosureDegree`.

A representation may be distributed yet have high trace anchoring; symbolic yet low-articulation; sparse yet low-closure. Those combinations shall remain visible.

#### C.2.7:4.3 - Extension rule
Contexts may add extra representation factors only if the extension is published as a factor addition rather than as a new master factor that erases the core factor bundle.

### C.2.7:5 - Archetypal Grounding
**Tell.** A model-state cue can be highly distributed but still trace-anchored; a symbolic note can be low articulation if its semantics are still vague.

**Show (System).** An operator decision aid may mix sparse alert codes and symbolic method-description text.

**Show (Episteme).** A research probe can move from distributed activation patterns to sparse symbolic hypotheses without any one-step formality story.

### C.2.7:6 - Bias-Annotation
The pattern resists folk theories that try to line up one representation factor with one stage or progression story.

### C.2.7:7 - Conformance Checklist
- `CC-C.2.7-1` `LanguageStateRepresentationFactorBundle` **SHALL** be published as a factor bundle, not as a hidden scalar.
- `CC-C.2.7-2` Local aliases such as `EncodingBasis` **MAY** exist only with an explicit docking to the governed factors.
- `CC-C.2.7-3` Representation factors **MUST NOT** silently replace `LanguageStateAnchoringMode` or `LanguageStateClosureDegree`.
- `CC-C.2.7-4` New local factors **SHALL** preserve the factor-bundle discipline.

### C.2.7:8 - Common Anti-Patterns and How to Avoid Them
- **One-factor myth.** Treating distributed/local or symbolic/subsymbolic as the whole story.
- **Progression collapse.** Equating representation shifts with formalization or closure.
- **Alias capture.** Letting `EncodingBasis` or a similar local alias erase the factor bundle.

### C.2.7:9 - Consequences
The benefit is cleaner comparison across schools, substrates, and publication forms. The trade-off is that representation talk becomes more explicit and less slogan-friendly.

### C.2.7:10 - Rationale
The factor-bundle design keeps the representation basis-slot family in the declared language-state chart over `U.CharacteristicSpace` orthogonal to articulation, closure, and anchoring.

### C.2.7:11 - SoTA-Echoing
This factorization fits current work on sparse distributed representations, symbolic/neuro-symbolic stacks, and interpretability practice.

### C.2.7:12 - Relations
- Builds on: `A.18`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `C.2.6`, `A.16.0`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, `F.9.1`.
- Constrains: language-state position publication and bridge loss notes around representation shifts.
### C.2.7:13 - Worked Examples and Factor Interaction Notes

#### C.2.7:13.1 - Distributed but explicit
A model-side summary may be representation-wise distributed and still highly explicit once published into a stable symbolic wrapper. This case matters because it blocks the folk myth that distributed implies vague.

#### C.2.7:13.2 - Symbolic but still low-articulation
A glossary-like note may be fully symbolic while still low in `AE` because the semantic anchors are not yet stabilized. This blocks the opposite myth: symbolic therefore explicit.

#### C.2.7:13.3 - Mixed-stack publication
An operator-facing publication face may combine sparse alert codes, symbolic method-description text, and distributed back-end model summaries. The representation-factor bundle should make that mixture visible instead of compressing it into one label.

### C.2.7:14 - Authoring and Review Guidance

#### C.2.7:14.1 - Author prompt
To publish a representation-factor bundle, ask separately:

- how local or distributed is the representation?
- how sparse or dense is it?
- how symbolic or subsymbolic is it?
- which additional factor, if any, genuinely matters enough to publish?

#### C.2.7:14.2 - Review prompt
A reviewer should reject any attempt to use one factor as if it summarized the rest. The factor bundle exists precisely to block that reduction.

#### C.2.7:14.3 - Cross-facet reminder
Reviewers should also watch for silent replacement of `LanguageStateAnchoringMode`, `AE`, or `CD` by representation talk.

### C.2.7:15 - Extension and Migration Notes

#### C.2.7:15.1 - Local extension rule
Contexts may add extra factors, but each added factor should answer a distinct question rather than duplicating locality, sparsity, or symbolicity under another label.

#### C.2.7:15.2 - Migration from alias-heavy prose
Aliases such as `EncodingBasis` or similar should be unfolded into explicit factor dockings before they are relied upon for routing, comparison, or bridge claims.

#### C.2.7:15.3 - Boundary reminder
`U.LanguageStateRepresentationFactorBundle` describes representational organization only. It does not determine route authority, closure, or anchoring by itself.
### C.2.7:16 - Factor-Bundle Publication Discipline

#### C.2.7:16.1 - Minimal representation package
A publishable `U.LanguageStateRepresentationFactorBundle` should normally show the current factor settings for locality/distribution, sparsity/density, and symbolicity/subsymbolicity, together with any declared extra factor. If a factor is intentionally omitted, say so rather than hiding the omission under a compact alias.

#### C.2.7:16.2 - No hidden scalar rule
Compact overlays such as "sparse-symbolic" are admissible only when they dock to the underlying factor bundle. No compact label may behave as a hidden master score for routing, bridge comparison, or stage/progression talk.

#### C.2.7:16.3 - Alias docking rule
Local aliases such as `EncodingBasis` are admissible only when their docking to the governed factors is explicit and stable. If an alias compresses several factors, the compression should remain visible.

### C.2.7:17 - Factor Interaction and Cross-Facet Reading Rule

#### C.2.7:17.1 - Interaction rule
Representation factors may correlate, but they do not determine one another. Highly distributed cues can still be sparse; symbolic publications can still be locally dense; mixed symbolicity can coexist with either strong or weak articulation. Publish the actual factor bundle rather than narrating one factor as if it predicted the rest.

#### C.2.7:17.2 - Cross-facet non-substitution
Representation talk must not silently replace `AE`, `CD`, or `LanguageStateAnchoringMode`. A shift from distributed to symbolic publication may change readability while leaving articulation low, closure open, or anchoring heavily operator-bound.

#### C.2.7:17.3 - Bridge reminder
If a representation shift matters in transport across contexts, note that the shift may alter what is preserved or salient. The bridge itself remains governed by `F.9` and `F.9.1`.

### C.2.7:18 - Review Matrix and Extension Tests

#### C.2.7:18.1 - Review matrix
A reviewer should ask:

- are all claimed factors visible in the publication or cited source;
- does any alias hide the factor bundle;
- is one factor being used as if it summarized the whole representation state;
- has representation talk started to replace articulation, closure, or anchoring claims.

#### C.2.7:18.2 - Local extension test
An additional factor is justified only if it captures a distinct representational question that cannot be reduced to locality, sparsity, or symbolicity. The extra factor should extend the bundle, not become a rival master factor.

#### C.2.7:18.3 - Migration test for legacy terminology
Legacy vocabularies often use "symbolic", "distributed", or "encoding basis" as if one term solved the whole classification problem. A conforming migration unpacks the term into explicit factor dockings and then checks whether any cross-facet claims were smuggled into the old label.

#### C.2.7:18.4 - Bundle-comparison reminder
Representation bundles may be compared across contexts only after the compared factors are explicit. If one context uses a compact local alias and another publishes the full factor bundle, require explicit docking before treating the two descriptions as commensurable.

### C.2.7:End


## C.3 - Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)

> **One‑line summary.** Establishes **`U.Kind`** as the **minimal, context‑local intensional carrier** of “what a statement is about,” separates **intent** (KindSignature + its own **F**) from **extent** (*which* instances belong to the kind **in a given Context slice**), and situates **typed reasoning** alongside **USM Scope (G)** and **F–G–R** without conflation. Details of the core objects and operations live in **C.3.1–C.3.5**; guard shapes are standardized in **C.3.A**.

**Status.** Normative in **Part C**. Identifier **C.3**. This pattern lays the **architectural invariant** and manager‑level guidance. The **mechanics** are defined by its child patterns.

**Readers.** Engineering managers, architects, and assurance leads who must reason about *typed claims* across Contexts without mixing up **describedEntity** (Kinds), **applicability** (**G**), and **assurance** (**R**).

**Depends on.**
— **A.2.6 USM** (Context slices & Scopes): **`U.ClaimScope` = G**, **`U.WorkScope`**, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridges + **CL** (scope).
— **C.2.2 F–G–R**: weakest‑link composition; penalties to **R** for Cross‑context congruence (CL).
— **C.2.3 Unified Formality F**: F0…F9 as an **ordinal Characteristic** (expression rigor).

**Sub‑patterns (normative unless noted).**
— **C.3.1** - `U.Kind` & `U.SubkindOf` (partial order).
— **C.3.2** - `KindSignature` (**intent**, with **F**) & `Extension/MemberOf` (**extent** in a slice).
— **C.3.3** - **KindBridge** & **`CL^k`** (type‑congruence; penalties route to **R**).
— **C.3.4** - **RoleMask** (context‑local adaptation without cloning kinds).
— **C.3.5** - **KindAT** (K0…K3, **informative facet**, not a Characteristic).
— **C.3.A** - **Typed Guard Macros** (annex): admit/compose, masks, Cross‑context reuse; AT is **forbidden** in guards.

**Deprecations.**
— “**Generality ladder**” for **G**; **G is Scope** only (set‑valued over `U.ContextSlice`).
— Any “**Kind scope**” characteristic (Kinds carry **intent/extent**, not Scope).
— **Mark as legacy** any uses of **‘validity’ as a Characteristic** or **‘operation’ as a Scope‑like Characteristic**; **redirect** to **`U.ClaimScope`** / **`U.WorkScope`** (A.2.6) for applicability. Editors SHOULD add glossary redirects in Part E.

**Editorial note (cut‑over).** Content formerly in C.3 that defined guard shapes, decision trees, and macro anti‑patterns now resides in **C.3.A**. Membership **evaluation obligations** live in **C.3.2** with `MemberOf`.


### C.3:1 - Purpose & Rationale

**What you get.**

1. A **neutral typed layer**: name *what* a claim quantifies over (**Kinds**) without binding to any particular “type technology” (OWL, PL types, shapes…).
2. A clean **split of characteristics**:
   – **Scope (G)** = *where* a claim holds (USM, set‑valued over **Context slices**).
   – **Kind extent** = *which instances* belong to a kind **inside** a given slice.
   – **F** = *how strictly* content is expressed (C.2.3).
   – **R** = *how well supported* (evidence & congruence penalties).
3. **Typed reuse across Contexts**: a dedicated **KindBridge** with **`CL^k`** (type‑congruence), so you can predict risk **without** touching F or G.
4. **Manager‑oriented maps**: when to invest in **formalization** (F), when to expand/narrow **Scope** (ΔG), when to test across **subkinds** (R), and what kind of **bridge** you should expect.

**Why it helps.**
