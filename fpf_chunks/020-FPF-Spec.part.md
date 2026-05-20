Governance principle vs Architectural principle clash: e.g. Core release schedule (Gov) outranks performance‑tuning (Prag)

### E.3:5 - Conformance Checklist

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑PT.1** | Every principle record **MUST** state `class` and may list `precedence_over[]`.                                      | Enables deterministic overrides. |
| **CC‑PT.2** | Precedence graph **MUST** be acyclic.    | Prevents circular law.           |
| **CC‑PT.3** | Any DRR introducing/modifying a principle **MUST** include a *Pillar Impact Analysis* and proposed precedence edges impact on each affected Pillar (P‑1… P‑11)| Aligns evolution with Pillars.   |

### E.3:6 - Illustrative Conflict Resolution

1. **The Conflict**
   * **P‑1 Cognitive Elegance** (`Arch`) demands an unambiguous term for “part–whole” entities, pushing us toward **Holon**.
   * **P‑2 Didactic Primacy** (`Did`) values immediate practitioner familiarity, pushing us to retain **System**.

2. **Risk of Stalemate**
   Without a precedence cascade, the discussion would collapse into subjective argument: *“purity beats clarity!”* vs *“clarity beats purity!”*.

3. **Applying the Precedence Model**
   * Default order: **Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did**.
   * `Arch` outranks `Did`; therefore **P‑1** takes formal precedence over **P‑2**.

4. **Principled Decision**
   We adopted **Holon** to satisfy the higher‑priority principle and mitigated the didactic cost by:
   * declaring `System ≡ U.System ⊑ U.Holon`,
   * providing aliases and an “On‑Ramp” tutorial.

> *The precedence rule did not merely name a winner; it compelled a solution that honoured both principles in proportion to their rank.*

**Precedence (high → low).** Law & Regulation → **E.5 Guard‑Rails** → **B.3 Trust & Assurance** → **E.3 governance decisions** → **E/E‑LOG policies** (editioned) → **BLP (E.2)** → Product Policies → Implementation Tactics.

**Notes.**
* BLP is a constitutional policy (see E.2 / “BLP”), but **does not supersede** E.5 Guard‑Rails nor B.3 assurance floors; it **does govern** ties among lawful, comparable‑assurance options.
* Wherever **NQD/E/E‑LOG** promotes illumination telemetry to dominance (via an explicit **CAL** policy; **policy‑id recorded in SCR**), **BLP adopts that lens** rather than overriding it (see E.2 BLP‑6).
* Any exception to policy **MUST** include a DRR with rationale and expiry.
* **BLP Override (Waiver).** When a narrower hand‑engineered method is selected over a general/scalable alternative **within declared tolerances** (α = budget, δ = assurance), the DRR **MUST** include:
  - a **BLP Scale‑Audit** (see E.2 **BLP‑1**) covering compute/data/**freedom‑of‑action** sweeps and slope/uncertainty reporting,
  - the **tolerances** α/δ and objective vector used (E.2 **BLP‑1e**),
  - a **Heuristic‑Debt** entry (responsible role, scope, expiry/review, de-hardening plan) per E.2 **BLP‑4**,
  - an **AutonomyProfileId** (see **E.3‑ABL**) and the GateDecision authority (see **Gate‑decision authority map** below).
**Set-returning parity.** All precedence decisions that compare methods **MUST** use the G.5/G.9 parity harness and **Pareto** dominance; scalarisation across mixed scales/units is **prohibited** (B.3).

**BLP — Bitter‑Lesson Hooks into Precedence**
1) **Tie‑breaking.** If two lawful options are **within δ** assurance and **within α** budget, prefer the option whose **slope vector Pareto‑dominates** over the audited window; if no dominance, prefer the **more general** method. (E.2 **BLP‑2**.)
2) **Script‑vs‑Search conflicts.** For conflicts between **procedural scripts** and **general search/learning**, scripts prevail **only** when mandated by E.5 or regulation, or when a DRR records a **BLP‑waiver** with expiry and hazard rationale (E.2 **BLP‑3/6**).
3) **Publication.** Precedence rulings that reference BLP **MUST** publish editioned policy‑IDs, edition pins, and **Resrc‑CAL** accounts to the SCR (E.2 **BLP‑1d**; G.11).

**ABL — Autonomy‑Budget & Oversight Profiles (GateProfile)**
This section defines an **extensible family of autonomy oversight profiles** for agentic tool use: each profile specifies (i) a budget envelope, (ii) a Freedom‑of‑Action (FoA) descriptor, and (iii) the required **gate‑decision publication** to authorize execution under that envelope. The familiar labels **L0…L4** are treated here as **profile identifiers** (not a fixed managerial ladder): projects MAY introduce additional profiles or sub‑profiles by minting new profile ids, provided they publish the same fields (budgets, FoA, decision roles, telemetry requirements) and keep profile changes explicit and auditable.

| ProfileId | Name                         | Freedom‑of‑Action (FoA)                  | Explore‑Share (default) | Typical Use                                     | GateDecision authority |
|---------:|------------------------------|------------------------------------------|-------------------------|-------------------------------------------------|------------------------|
| **L0** | Scripted Execution           | **Whitelist only**; fixed scripts        | 0                       | Compliance‑critical, deterministic procedures   | Engineer‑of‑Record (EoR) |
| **L1** | Constrained Sequencing       | Negative constraints; **single‑tool**    | ≤ 0.10                  | Low‑risk automation with bounded novelty        | EoR + Peer Review |
| **L2** | Supervised Autonomy          | Multi‑tool plans; bounded replanning     | 0.20 (±0.10)            | Ambiguous tasks; moderate budget                | Team Lead + Safety |
| **L3** | Auditable Autonomy           | Multi‑step, self‑replanning; adaptive    | 0.30 (±0.10)            | Production agents with learning under guard‑rails | Product + Safety + Legal |
| **L4** | Open‑Ended / Research Mode   | Broad FoA within sandbox & rails         | 0.40–0.50               | Illumination‑first exploration, sandboxes only  | Governance Board (Gov‑CAL) |

**Normative requirements by profile.**
* **Budgets.** Each profile **MUST** declare ceilings for **time / compute / cost / risk** and a FoA descriptor; units must be explicit (Resrc‑CAL). Budgets are **hard gates** at run‑time (C.Agent‑Tools‑CAL **ATC‑3**).
* **Profile binding & change visibility.** Every CallPlan **MUST** declare the active profile id. Any profile change is a **GateCrossing** (E.18) and **MUST** be published (DecisionLog entry + pinned policy‑ids), so an auditor can reconstruct which profile governed which Window.
* **Assurance floors.** **B.3** WLNK minima on **F** and **R** apply at all profiles. Any profile‑specific tightening (e.g., higher required **R_eff** or stricter CL/Φ policies for broader FoA) **MUST** be declared on the profile and pinned by policy‑id. Pre‑deployment **assurance deltas** MUST be recorded for L2+.
* **Exploration discipline.** `explore_share` MUST be explicit in the **CallPlan** (C.Agent‑Tools‑CAL **ATC‑4**). Deviations from defaults require DRR justification.
* **Provenance.** L1+ MUST emit a **CallGraph** with Service/Method editions, EmitterPolicyRef, budget deltas, and observation hooks (C.Agent‑Tools‑CAL **ATC‑5/6**).
* **BLP conformance.** For L2+, selection MUST apply **BLP** (E.2 **BLP‑2**) with **α/δ** tolerances declared in the plan policy. Any admitted heuristic requires a **Heuristic‑Debt** entry (E.2 **BLP‑4**).
* **Learning/Adaptation.** L3–L4 MAY enable **feedback‑driven adaptation** within E.5 Guard‑Rails and privacy controls; L0–L2 default **off** unless a DRR documents mitigation (E.2 **BLP‑5**).
* **Human‑in‑the‑Loop (HITL).** HITL obligations are expressed as **gate decisions and pause/resume hooks**, not an implicit “approval ladder”:
  * **L0–L1:** execution MAY start only after an explicit **GateDecision** authorizing the CallPlan is present in the declared window.
  * **L2:** sentinels MUST be able to pause execution; resumption requires a new **GateDecision** recorded in the DecisionLog.
  * **L3:** the profile MUST declare periodic review windows; continued execution across a review boundary requires an explicit **GateDecision**.
  * **L4:** continuous telemetry review; the default execution context is **sandboxed**; leaving the sandbox requires an explicit **GateCrossing** with a published CrossingBundle (`E.18` + `F.9`/`F.17`/`E.17`, with `A.21` when a gate decision is live).

**Gate‑decision authority map (default signers; who may author GateDecisions).**
* **L0:** EoR or appointed maintainer.
* **L1:** EoR **and** peer reviewer (two‑person rule).
* **L2:** Team Lead **and** Safety representative.
* **L3:** Product Owner **and** Safety **and** Legal/Privacy.
* **L4:** **Gov‑CAL Board** (multi‑disciplinary) with documented scope, time‑boxed **trial budget**, and rollback criteria.

**Profile promotion / demotion triggers.**
* **Promote** a profile when repeated **BLP‑consistent** results show stable assurance within δ and budget adherence within α for ≥ **N_policy** runs (declare **N_policy** in the active profile). Promotion is not implicit: a **GateDecision** **MUST** authorize the profile change and cite the slope evidence (E.2 **BLP‑1c**).
* **Demote** a profile when: (i) a sentinel breaches risk or budget, (ii) assurance drops below floors, (iii) policy changes, or (iv) a significant **heuristic‑debt** item expires without replacement. Demotion **MUST** be published as a GateCrossing with updated budgets/policies pinned.

### E.3:7 - **Conformance Checklist — E.3 ↔ BLP Interop**

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑E3.10** | Precedence list includes **BLP** explicitly **below** E/E‑LOG and **above** product tactics; conflicts handled via **BLP‑waiver** discipline. | Makes BLP’s standing auditable. |
| **CC‑E3.11** | Every DRR that overrides BLP **MUST** include a **Scale‑Audit** (E.2 **BLP‑1**) and a **Heuristic‑Debt** entry (E.2 **BLP‑4**). | Prevents silent heuristic drift. |
| **CC‑E3.12** | Each agentic plan declares an **AutonomyProfileId** (e.g., L0–L4) with explicit budgets, `explore_share`, and **E/E‑LOG EmitterPolicyRef**. | Aligns autonomy with assurance. |
| **CC‑E3.13** | L1+ executions emit **CallGraphs** with editioned policy/method ids and budget deltas; L3+ include adaptation status. | Ensures replayability & audit. |
| **CC‑E3.14** | Profile changes follow **promotion/demotion** triggers and are published as GateCrossings with edition pins in the SCR. | Keeps autonomy under control. |

### E.3:8 - Consequences
*Positive* — Turns subjective debate into objective, traceable decisions; high‑impact conflicts surface early.

### E.3:9 - Rationale
The chosen taxonomy mirrors FPF’s layered dependency: **Governance** rules how change occurs; **Architecture** shapes what can exist; **Epistemology** secures meaning and trust; **Pragmatics** and **Didactics** ensure usefulness and learnability. Explicit override edges supply the flexibility experts need, while the default hierarchy keeps day‑to‑day design deterministic—a “living constitution” that remains both human‑intelligible and machine‑enforceable.

### E.3:10 - Relations
* **Depends on:** `pat:constitutional/vision`, `pat:constitutional/pillars`
* **Governs:** All subsequent patterns and DRRs; Guard‑Rail patterns reference CC‑PT.\

> *“A taxonomy sorts principles; precedence gives them order—together they convert debate into design.”*

### E.3:End

## E.4 - FPF Ecosystem Family Architecture

### E.4:1 - Problem frame

The FPF ecosystem contains three maintained families: the normative Conceptual Core, executable or machine-checking Tooling Reference material, and learning-oriented Pedagogical Companion material. If these families are mingled without a clear architectural separation, the ecosystem becomes difficult to navigate, govern, and maintain. Users cannot easily distinguish binding rules from helpful advice, and the entire framework's release cycle becomes coupled to its most volatile component.

### E.4:2 - Problem

How can we structure the FPF ecosystem to ensure a clean separation of concerns between normative concepts, didactic materials, and executable tooling? A formal architecture is required to maintain conceptual purity, enable independent evolution of components, and provide a clear map for all stakeholders.

### E.4:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Stability vs. Agility** | The conceptual core must evolve slowly and deliberately ↔ tools and tutorials must iterate quickly to keep pace with technology and user needs. |
| **Authority vs. Accessibility** | Users need to know which rules are normative and binding ↔ they also need accessible, non-normative guides to help them learn. |
| **Modularity vs. Cohesion** | The different FPF ecosystem families must be able to evolve independently <-> they must remain part of a single, coherent FPF ecosystem. |

### E.4:4 - Solution

The FPF ecosystem is formally stratified into three canonical **FPF ecosystem families**. Each family has a distinct purpose and is governed by different rules, ensuring a clear separation of concerns. The interaction between these families is governed by the **Unidirectional Dependency Principle** (see Guard-Rail E.5.3).

1.  **The Conceptual Core (The Canon):** This family contains the **normative** FPF patterns, kernel definitions, rules, and invariants. It is the canonical FPF pattern set for universal FPF content. It is defined to be tool-agnostic and notation-independent.

2.  **The Tooling Reference:** This family contains executable tools and machine-checkable support publications that implement or verify the normative rules of the Core. This includes reference linters, simulators, and data schemas. This family makes Core rules operational without becoming the Core pattern set.

3.  **The Pedagogical Companion:** This family contains **non-normative, didactic publications** designed to help humans learn and apply FPF. This includes tutorials, worked examples, and playbooks. This family explains the Core and the Tooling Reference without changing Core meaning.

### E.4:5 - Archetypal Grounding (System / Episteme)

*   **For a `U.System`:**
    *   **Conceptual Core:** Defines the universal pattern `U.System`.
    *   **Tooling Reference:** Provides a modeling language profile or a serialization schema for modeling systems.
    *   **Pedagogical Companion:** Provides a tutorial on how to model a water pump using that profile.

*   **For an `U.Episteme`:**
    *   **Conceptual Core:** Defines `U.Episteme` and the F-G-R assurance tuple components (`F/R` characteristics plus `G` as ClaimScope).
    *   **Tooling Reference:** Provides the reference linting tool to automatically score epistemes.
    *   **Pedagogical Companion:** Provides a case study on how a scientific theory's R-score evolves over time.

### E.4:6 - Conformance Checklist

| ID | Requirement |
| :--- | :--- |
| **CC-E.4.1** | Every FPF pattern, support publication, tool, or pedagogical publication **MUST** declare which of the three families (Core, Tooling, Pedagogy) it belongs to. |
| **CC-E.4.2** | The content of each family member **MUST** be consistent with the defined purpose of its family (e.g., no normative rules in the Pedagogical Companion). |
| **CC-E.4.3** | Tooling Reference and Pedagogical Companion family members SHALL NOT be imported by Conceptual Core patterns. |

### E.4:7 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Clear Separation of Concerns:** Users and contributors can immediately identify the nature and authority of any given FPF pattern, support publication, tool, or learning publication. | **Requires Discipline:** Authors must be careful to place new content in the correct ecosystem family. |
| **Decoupled Release Cycles:** The Core can maintain a stable, slow release cadence, while the Tooling Reference and Pedagogical Companion families can evolve rapidly. | - |
| **Architectural Clarity:** Provides a simple, powerful mental model for navigating the entire FPF ecosystem. | - |

### E.4:8 - Rationale

This pattern establishes the macro-architecture of the entire FPF ecosystem. By separating the normative Core from executable Tooling Reference material and learning-oriented Pedagogical Companion material, it creates a system that is simultaneously stable, agile, and accessible. This layered architecture is a proven pattern in large-scale systems, from the OSI model in networking to the structure of modern operating systems, and it is essential for FPF's long-term health and scalability.

### E.4:9 - Relations

*   **Instantiates:** **P-5 (FPF Layering)** at a macro-level.
*   **Is Constrained by:** **E.5.3 (Unidirectional Dependency)**.
*   **Is Foundation For:** The entire authoring and governance model, as it defines the "territories" where different rules apply.

> *“A canon without a rationale is scripture; a rationale without a canon is gossip. FPF keeps both, fused in patterns.”*

### E.4:End

## E.5 - Four Guard‑Rails of FPF

### E.5:1 - Problem frame
FPF positions itself as a **timeless, universal “operating system for
thought.”**  Collaborative projects of this scope face four predictable
entropic pulls:

1. **Implementation gravity** – concept prose accretes tool jargon.
2. **Notation lock‑in** – one diagram style becomes “the language.”
3. **Convenience cycles** – quick fixes create reverse dependencies.
4. **Disciplinary monoculture** – implicit bias colours “universal” rules.

Left unchecked, these forces erode Pillars **P‑1 Cognitive Elegance**,
**P‑4 Open‑Ended Kernel** and **P‑5 FPF Layering**.

### E.5:2 - Problem
Without explicit, non‑negotiable protectors the Conceptual Core would
slowly:

* entangle with transient technology terms,
* hard‑freeze into a single dialect,
* devolve into a tightly coupled “big ball of mud”,
* betray its trans‑disciplinary promise.

### E.5:3 - Forces

| Force | Tension |
|-------|---------|
| **Purity vs Pragmatism** | Preserve pristine concepts ↔ need real examples. |
| **Universality vs Convention** | Rules valid across domains ↔ convenience of one familiar notation. |
| **Modularity vs Integration** | Independent layers ↔ temptation to cross‑link for speed. |
| **Objectivity vs Perspective** | Neutral framework ↔ Transformers’ unavoidable cultural lens. |

### E.5:4 - Solution — the Four Guard‑Rails
FPF establishes **four architecturally enforced guard‑rails** that every Core, Tooling, and Pedagogy artefact must obey.  They function as an “immune system” resisting each entropic pull.
**Scope note (conceptual, not lint).** These guard‑rails regulate the **architecture of thought**—concepts, claims, and their relations. They **do not** mandate tools, file formats, notations, or workflows; any linting or automation lives outside the Core and is optional, provided it preserves these conceptual constraints.


| # | Guard‑Rail | Protects against |
|---|------------|------------------|
| **GR‑1** | **DevOps Lexical Firewall** | Implementation, governance, automatisation and DevOps concerns gravity |
| **GR‑2** | **Notational Independence** | Notation lock‑in |
| **GR‑3** | **Unidirectional Dependency** | Convenience cycles |
| **GR‑4** | **Cross‑Disciplinary Bias Audit** | Disciplinary monoculture |

Concrete rules for each rail live in patterns **E.5.1 – E.5.4**.

### E.5:5 - Archetypal Grounding (System / Episteme)

| Guard‑Rail | `U.System` example | `U.Episteme` example |
|------------|-------------------|----------------------|
| GR‑1 | Definition of `U.System` never cites file formats or build scripts. | Definition of `U.Episteme` avoids naming specific proof engines. |
| GR‑2 | Pump boundary invariant is true in plain text or any diagram. | F‑G‑R semantics hold in algebraic or graph notation alike. |
| GR‑3 | A sizing helper imports Core invariants; Core never imports helper tutorials. | Learning guide cites R‑score; Core never cites guide. |
| GR‑4 | Bias audit removes thermo‑mechanical jargon from a “universal” pattern. | Audit replaces physics‑centric metaphors in a trust pattern. |

### E.5:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑GR.1** | Every new Core pattern **SHALL** cite, in its *Relations* section, the guard‑rail(s) it relies on or may affect. | Ensures traceability and deliberate rule interaction. |
| **CC‑GR.2** | Artefacts classified as Tooling or Pedagogy **MUST NOT** violate any rule in GR‑1 through GR‑4. | Keeps entropic forces outside the Conceptual Core. |
| **CC‑GR.3** | A revision to any guard‑rail pattern **REQUIRES** a Design‑Rationale Record that (a) states the reason, and (b) includes a Pillar‑impact analysis per E.3 precedence model. | Aligns evolution with higher‑level principles. |
| **CC‑GR.4** | The aggregate of guard‑rail rules **MUST** remain internally consistent and acyclic; no guard‑rail may override another without explicit precedence edges. | Preserves deterministic governance. |
| **CC‑GR.5** | Every Core pattern **MUST** anchor its primary governed object or governed relation with a declared **ReferencePlane** (`world | concept | episteme`) at first mention. | Keeps Core about extensional or intensional values rather than their paperwork, and aligns with CHR:ReferencePlane. |
*All CC‑GR duties are **conceptual**. Any automated checks are **informative only** and live in Tooling/Pedagogy.*

### E.5:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Long‑term integrity** – stops slow drift of the Core toward jargon, notation lock‑in, and hidden cycles. | Authors must run a guard‑rail checklist before submission. *Mitigation:* template auto‑inserts the checklist. |
| **Stable yet evolvable ecosystem** – Core stays timeless while Tooling & Pedagogy can iterate rapidly. | Early stage contributions may feel constrained; examples in the Pedagogical Companion show compliant paths. |
| **Trust & auditability** – stakeholders can verify the framework’s purity independently. | Adds overhead to governance; justified by safety and longevity. |

### E.5:8 - Rationale
A constitution without enforcement degrades into *dead‑letter rules*.
The four guard‑rails translate abstract Pillars into **concrete, testable
constraints**.  Grouping them under one umbrella pattern:

* gives newcomers a single “safety index” to consult,
* makes compliance binary (*pass / amend*),
* provides a stable anchor for future automated conformance tools—without
  mentioning any specific engine, thus honouring GR‑1 itself.

They collectively instantiate Pillars **P‑1**, **P‑2**, **P‑4**, **P‑5**
and reinforce the precedence order defined in **E.3**.

### E.5:9 - Relations

* **Comprises:**
  * `pat:guard/devops‑firewall` (E.5.1) – GR‑1
  * `pat:guard/notational‑independence` (E.5.2) – GR‑2
  * `pat:guard/unidirectional‑dependency` (E.5.3) – GR‑3
  * `pat:guard/bias‑audit` (E.5.4) – GR‑4
* **Depends on:**
  * `pat:constitution/pillars` (E.2)
  * `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** every Core, Tooling, and Pedagogy artefact; all DRRs.

### E.5:End

## E.5.1 - DevOps Lexical Firewall

### E.5.1:1 - Problem frame
The FPF Core is meant to remain valid across decades and technology
generations.  Implementation details—file formats, build pipelines,
runtime flags—evolve rapidly and differ between domains.  When such
terms invade normative prose, the Core ages as quickly as the tools it
mentions.

### E.5.1:2 - Problem
*Conceptual erosion*: a rule that cites a transient technology becomes
obsolete when that technology fades, forcing unnecessary Core revisions
and fragmenting historical audits.

### E.5.1:3 - Forces

| Force | Tension |
|-------|---------|
| **Timelessness** | Concepts must survive tool turnover. |
| **Pedagogic clarity** | Examples need concreteness ↔ too much concreteness hard‑codes technology. |
| **Cross‑domain reach** | Physical‑system engineers and knowledge‑theorists use different stacks. |

### E.5.1:4 - Solution
Establish a **Lexical Firewall** around the **Conceptual Core** *(conceptual constraint; not a build‑time linter)*:

1. **Forbidden lexicon**
   Normative patterns **SHALL NOT** contain tool‑or file‑specific words
   (e.g. protocol keywords, file extensions, IDE commands).
   Permissible wording: “a reference parser”, “a serialisation schema”.

2. **Indirection rule**
   When a Core concept needs an executable illustration, the pattern
   cites the **Tooling Reference family** artefact by *conceptual name*,
   never by concrete path or syntax.

3. **Glossary pointer**
   If an unavoidable technical term appears, it is defined in a *Tooling Glossary* outside the Core and referenced by conceptual alias—not embedded.
*Non‑normative automation.* Machine checks **MAY** exist in Tooling; they are advisory and **MUST NOT** be imported into the Core.

### E.5.1:5 - Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| **Normative text** | “A system boundary must expose at least one conserved‑quantity flow.” (No mention of modelling language.) | “An episteme records its F–G–R assurance tuple.” (No mention of proof syntax.) |
| **Illustrative link** | A modelling profile resides in the Tooling family; Core cites it as “the reference system‑profile”. | A linting routine lives in Tooling; Core cites it as “the reference episteme‑checker”. |

### E.5.1:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑LFW.1** | A Core pattern **SHALL** fail review if it contains implementation‑specific tokens. |
| **CC‑LFW.2** | References to executable artefacts **MUST** use conceptual names, not file paths or command strings. |
| **CC‑LFW.3** | Pedagogical examples inside Core **MAY** describe behaviour, but **MUST NOT** embed code snippets. |

### E.5.1:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays evergreen and cross‑domain. | Authors must relocate concrete examples to Tooling or Pedagogy. |
| Reviewers can machine‑scan for banned tokens. | Requires a small vocabulary allow‑list; maintained in Tooling Guide. |

### E.5.1:8 - Rationale
Language shapes thought.  By firewalling transient jargon, we uphold
**P‑1 Cognitive Elegance** (clarity), **P‑2 Didactic Primacy** (domain‑neutral
exposition) and **P‑5 FPF Layering** (clean separation between Core
and Tooling).  The rule is content‑agnostic and thus itself immune to the
very decay it prevents.

### E.5.1:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Constrains:** every pattern in Conceptual Core
* **Instantiates pillars:** P‑1, P‑2, P‑5

### E.5.1:End

## E.5.2 - Notational Independence

### E.5.2:1 - Problem frame
FPF concepts must travel across academic disciplines, modelling tools,
and future notations we cannot yet foresee. If a normative pattern binds
its *meaning* to one diagram style, file syntax, or markup dialect, the
concept ages as soon as the notation does.

### E.5.2:2 - Problem
*Semantic lock‑in*: when a definition relies on a particular glyph set or
diagram grammar, alternative communities either translate it—risking
drift—or ignore FPF altogether.

### E.5.2:3 - Forces

| Force | Tension |
|-------|---------|
| **Expressiveness** | Diagrams and formal grammars aid precision ↔ they should never become the definition itself. |
| **Longevity** | A 20‑year horizon ↔ notation life‑cycles of 3‑5 years. |
| **Cross‑discipline adoption** | Mathematicians prefer algebraic syntax; engineers prefer schematics. |

### E.5.2:4 - Solution — Notational Independence Guard‑Rail *(conceptual; semantics over syntax; not a notation mandate)*

1. **Semantics primacy**
   Normative content **SHALL** define concepts in linguistic form first
   (plain English + mathematics if needed). Visual or syntax examples
   are secondary illustrations.

2. **Equivalence clause**
   When an official alternate notation exists, the pattern must state:
   *“Representation A and Representation B are semantically equivalent
   under mapping M.”*

3. **Reference indirection**
   If the Core cites a diagram, it does so by *conceptual role*
   (“reference boundary schematic”) rather than by file or syntax name.

4. **Conceptual prefix neutrality**
   FPF **conceptual prefixes** (e.g., `U.`, `Γ_`, `ut:`, `tv:`, `ev:`, `mero:`) are  **cognitive namespaces**, not syntax tokens. Core patterns **MUST NOT**  tie their meaning to any concrete serialisation or URI scheme for these prefixes; any expansions are **illustrative only** and live in Tooling or Pedagogy.

5. **Cards and other "forms"**
Cards, tables and other "forms" exist in FPF core only as conceptual model, not as data model, thus no need to data-related notation or notation for lint. Comformance checklist and quards is also conceptual, argumentation like "this will ease machine check" is forbidden, no machine checking is intended in core; machine checks and linters live only in Tooling.

### E.5.2:5 - Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| Definition | Boundary of a pump is expressed in prose plus set notation; a diagram is illustrative. | F‑G‑R assurance components defined textually; a triple‑store serialisation is illustrative. |
| Alternate rendering | Same pump semantics rendered in a lattice diagram or a tabular sheet remain valid. | R‑scores plotted in a heatmap or listed in CSV remain equivalent. |

### E.5.2:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑NI.1** | A Core pattern **MUST NOT** embed semantics that hinge on one specific notation. |
| **CC‑NI.2** | Illustrative renderings **SHALL** be marked “informative”. |
| **CC‑NI.3** | When multiple official renderings exist, the pattern **MUST** declare the semantic mapping between them. |
| **CC‑NI.4** | If a **conceptual prefix** appears in Core, its expansion (if shown) **SHALL** be marked *informative* and **MUST NOT** be required to interpret the semantics. |

### E.5.2:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Ensures FPF survives notation turnover. | Authors invest time describing mappings; mitigated by reusable mapping templates. |
| Lowers entry barrier for domains using different diagram traditions. | Excessive illustrations can bloat pages; guidance in Pedagogical Companion limits scope. |

### E.5.2:8 - Rationale
Language and diagrams are tools, not truths. By elevating semantics over
syntax, FPF maintains **P‑1 Cognitive Elegance** and **P‑2 Didactic
Primacy** while safeguarding **P‑5 FPF Layering**: tooling layers can
add new renderers without Core edits.

### E.5.2:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Constrains:** every normative Core pattern and official alternate rendering
* **Instantiates pillars:** P‑1, P‑2, P‑5

### E.5.2:End

## E.5.3 - Unidirectional Dependency

### E.5.3:1 - Problem frame
FPF separates artefacts into stable **Conceptual Core**, executable
**Tooling Reference**, and fast‑evolving **Pedagogical Companion** (see
E.4 FPF Ecosystem Family Architecture).  If dependencies can point *both* ways,
volatile layers will eventually drag the Core into rapid revision
cycles or introduce domain‑specific bias.

### E.5.3:2 - Problem
*Architectural gravity*: a tutorial or helper script adds a new feature,
Core patterns import it “temporarily,” and within months the supposedly
timeless layer depends on transient assets—breaking Pillar **P‑5
FPF Layering**.

### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly ↔ Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts ↔ Core cannot depend on volatile code. |
| **Simplicity** | Rule must be testable and unambiguous ↔ must allow legitimate upward imports. |

### E.5.3:4 - Solution — One‑Way, Acyclic Imports
Define a strict **partial order** over FPF ecosystem families **and guard meaning flow** (see **E.10 V-1**): imports point only **upward** in stability, and **no Core semantics** may derive from Tooling/Pedagogy. No linters or machine checking in Conceptual Core.

**`imports` is a dependency DAG, not a specialisation relation (normative).** Whenever an artefact exposes an explicit `imports : [...]` list (e.g., `SignatureManifest.imports` in A.6.0), treat `imports` as **dependency edges** governed by this section: the induced `imports` graph MUST be **acyclic** (a DAG) and MUST respect the declared direction. `imports` MUST NOT be used to encode *specialisation* (e.g., `⊑` / `⊑⁺` between mechanisms); specialisation relations are declared separately via the relevant morphism and specialisation-chain rules (e.g., A.6.1 `U.MechMorph`).

Pedagogical Companion  ⟶  Tooling Reference  ⟶  Conceptual Core

1. **Allowed edges**
   Dependencies **MAY** point **only upward** (toward greater semantic
   stability). No cycle is ever permitted.

2. **No downward import**
   Conceptual Core patterns **SHALL NOT** import Tooling Reference or Pedagogical Companion family members.
   Tooling Reference family members **SHALL NOT** import Pedagogical Companion family members.

3. **Future layers**
   Any new family is inserted below an existing one or becomes part of
   the Tooling or Pedagogy strata; the ordering extends accordingly.

### E.5.3:5 - Archetypal Grounding (System / Episteme)

| Layer | `U.System` illustration | `U.Episteme` illustration |
|-------|------------------------|---------------------------|
| Core | Definition of `U.System` and boundary invariant. | Definition of F‑G‑R assurance components. |
| Tooling | “Reference system‑profile” that checks boundary flow; *imports* Core invariants. | “Episteme‑scoring routine” that calculates R‑score; *imports* Core characteristics. |
| Pedagogy | Tutorial using the system‑profile to model a pump; *imports* profile and Core term. | Case study explaining R‑score evolution; *imports* scoring routine and Core term. |
| **Forbidden** | Core pattern importing measurement script. | Core pattern importing R‑score web dashboard. |

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-UD.1** | Dependency graph among all FPF ecosystem family members **MUST** be acyclic. |
| **CC-UD.2** | A family member **SHALL** import only from its own family or any family above it in the order. |
| **CC‑UD.3** | A DRR that introduces a downward edge **SHALL** be automatically rejected. |

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Release cadence decoupled: Core (slow), Tooling (medium), Pedagogy (fast). | Slight duplication when multiple tools target same concept; mitigated by shared Core definitions. |

### E.5.3:8 - Rationale
One‑way import graphs are a proven safeguard in operating systems
(kernel vs user land) and layered protocols. Here the rule operationalises
Pillars **P‑4 Open‑Ended Kernel** and **P‑5 FPF Layering**, ensuring
that innovation happens “below” without contaminating the timeless Core.

### E.5.3:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **References family definition:** `pat:constitution/fpf-ecosystem-family-architecture` (E.4)
* **Instantiates pillars:** P‑4, P‑5
* **Constrains:** All artefact imports recorded in DRRs or SCRs

### E.5.3:End

## E.5.4 - Cross‑Disciplinary Bias Audit

### E.5.4:1 - Problem frame
FPF calls itself trans‑disciplinary, but every author carries implicit
metaphors from a source domain. If those metaphors leak into “universal”
patterns, practitioners from other fields disengage or mis‑interpret the
rules.

### E.5.4:2 - Problem
Unrecognised bias hides in wording, examples, unit choices or principle
weighting. Once embedded in normative language, such bias is hard to
remove and contradicts Pillars **P‑2 Didactic Primacy** and **P‑8
Cross‑Scale Consistency**.

### E.5.4:3 - Forces

| Force | Tension |
|-------|---------|
| **Neutrality** | One voice for all disciplines ↔ need for relatable examples. |
| **Conciseness** | Audit guidance must be brief ↔ must cover multiple bias types. |
| **Longevity** | Guidance must survive emergence of new domains. |

### E.5.4:4 - Solution — Principle‑Taxonomy‑Guided Bias Audit

1. **Bias‑Lens set**
   Every normative pattern is assessed through **five lenses** that match the
   Principle classes from **E.3**:
   `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`.

2. **Equilibrium question**
   For each lens ask:
   *“Does the pattern over‑privilege this class or silence it?”*
   *Examples:*
   *   Over‑reliance on `Onto/Epist` precision may ignore `Prag` cost.
   *   Dominant `Arch` metaphors may alienate `Did` audiences.

3. **Scope‑or‑Balance rule**
   * If imbalance is found and universality is intended, re‑phrase to
     restore balance.
   * If imbalance is intentional (domain‑specific pattern), mark the
     scope explicitly: *“Applies primarily to thermodynamic systems.”*

4. **Audit trace**
   The pattern carries a short **Bias‑Annotation** paragraph recording
   which lenses were tested and any scoping statement. No workflow checklists or
   reviewer metadata or other data and data format and data governance tips is stored in the Core.

### E.5.4:5 - Archetypal Grounding (System / Episteme)

| Bias lens | Example imbalance | Conceptual correction |
|-----------|------------------|-----------------------|
| `Arch` vs `Did` | Pump pattern uses abstract category theory terms. | Add plain‑language boundary narrative or move abstraction to appendix. |
| `Onto/Epist` vs `Prag` | Episteme trust score defined with complex logic but no guidance on empirical cost. | Add pragmatic note on evidence collection cost or scope the pattern. |

### E.5.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑BA.1** | Each Core pattern **SHALL** include a *Bias‑Annotation* listing the five lenses and any declared scope limitation. | Ensures explicit reflection on bias. |
| **CC‑BA.2** | A pattern labelled “universal” **MUST NOT** privilege a single lens without justification or scoping note. | Preserves trans‑disciplinary integrity. |
| **CC‑BA.3** | If scope is declared, the pattern **SHALL** reference the mapping or rationale that enables cross‑domain translation. | Keeps pathways open for other calculi. |
| **CC‑BA.4 (QD‑triad evidence for “universal”).** | Any pattern that labels itself **“universal”** SHALL cite **A.8 CC‑UC 1 + CC‑UC 2** and attach the **QD evidence** (Diversity_P + IlluminationSummary, with edition and binning) or else **scope** the claim to its declared `U.BoundedContext`. | preserves domain quality diversity |

### E.5.4:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Neutral, inclusive language attracts wider adoption. | Authors spend a few extra lines on Bias‑Annotation; mitigated by template snippet. |
| Bias is surfaced at writing time, not after publication. | — |

### E.5.4:8 - Rationale
Coupling the audit directly to the Principle Taxonomy keeps the guard‑rail
**concept‑driven**, not workflow‑driven. No mention of review boards,
CI‑jobs, or checklists appears in the Core; such mechanics belong in the
Tooling Guide. This guard‑rail therefore satisfies **GR‑1** (Firewall)
while securing Pillars **P‑2, P‑7 Pragmatic Utility, P‑8**.

### E.5.4:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Depends on:** `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** All normative patterns claiming universality

### E.5.4:End


## E.6 - Didactic Architecture of the Specification

### E.6:1 - Problem frame
FPF addresses readers from at least two characteristics of diversity:

* **Disciplinary** – systems engineers, knowledge scientists, ethicists.
* **Experience** – newcomers need intuition; experts need rigour.

Past drafts mixed governance mandates with domain examples, producing a
steep learning curve and repeated “forward‑reference” detours.

### E.6:2 - Problem
If core ideas are buried under formalism or scattered across parts,
readers either give up or misuse the framework. We need a didactic
macro-order that guides cognitive load from low to high while keeping
normative sections discoverable, without letting readers confuse
document order with one universal first-practical workflow.

### E.6:3 - Forces

| Force | Tension |
|-------|---------|
| **Cognitive Load** | Early clarity ↔ eventual formal depth. |
| **Conceptual Integrity** | Foregoing examples risks abstraction ↔ too many examples delay axioms. |
| **Didactic order vs practical entry** | Stable document macro-order ↔ truthful first-practical routes that may cross parts. |

### E.6:4 - Solution — “On‑Ramp to Archetypes first, Authoring last” sequence

#### E.6:4.0 - Document order is distinct from first-practical entry

The macro-order of the document is a didactic scaffold, not a universal practical workflow. Entry navigation surfaces such as the `Preface`, `J.4`, entry-neighborhood governing patterns, and worked entry readings are informative navigation only: they may cross Parts when that is the first honest entry for the live question, and they do not create a second normative process history.

The "On-Ramp First" Macro-Structure: The specification is ordered to create a smooth cognitive ramp:
* It begins with an informal, non-normative Preface (The On-Ramp), which uses storytelling and concrete examples (System and Episteme) to build intuition.
* It then proceeds through the normative Parts (A-D), moving from the foundational kernel to the rich patterns of trans-disciplinary reasoning.
* It concludes with the authoring rules (Part E) and appendices, ensuring that this "meta" content does not obstruct the primary learning path.

1. **Preface (On‑Ramp)**
   Informal tour; introduces `U.System` and `U.Episteme` via concrete
   stories before any normative language appears.

2. **Part A Kernel**
   Minimal holonic ontology and the Transformer principle give readers
   the essential vocabulary.

3. **Part B Trans‑disciplinary Reasoning**
   Tell‑Show‑Show pedagogy: universal rule → Sys‑CAL example →
   KD‑CAL example.

4. **Part C Extension Patterns**
   Domain‑specific calculi expand on the examples already seen.

5. **Part D Ethics & Conflict Optimisation**
   Shows reflective patterns only after readers grasp holonic reasoning.

6. **Part E Authoring**
   Constitution, guard‑rails, and contributor rules come last; novices
   can postpone reading.

7. **Appendices (Annexes)**
   Tutorials, tooling guides, and migration scripts live here.

### E.6:5 - Archetypal Grounding (System / Episteme)

| Narrative layer | First sight of `U.System` | First sight of `U.Episteme` |
|-----------------|---------------------------|-----------------------------|
| Preface | Coffee‑machine story (pump as system). | Meta‑analysis story (study bundle as episteme). |
| Part A | Formal definition inherits boundary invariant. | Formal definition inherits F‑G‑R coordinates. |
| Part B Tell‑Show‑Show | Γ\_sys example: assemble pump. | Γ_epist example: merge study bundle. |

### E.6:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑DA.1** | Each Part **SHALL** open with a one‑paragraph situational “hook” before formal text. |
| **CC‑DA.2** | Every architectural pattern **MUST** implement Tell‑Show‑Show: universal rule plus System & Episteme illustrations. |
| **CC‑DA.3** | Governance patterns (**Part E**) **SHALL NOT** appear before the Kernel in the main document flow. |
| **CC‑DA.4** | Navigation aids **SHALL** distinguish document order from first-practical entry guidance; entry-neighborhood and worked-reading guidance are informative and MAY cross Parts without implying a universal process history. |

### E.6:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Smooth learning curve; readers can stop at their needed depth. | Template discipline required; mitigated by authoring guide (E.8). |
| Reduces forward‑reference clutter; each concept is primed before formal use. | Preface evolves when new archetypes added; handled via On‑Ramp revision DRR. |

### E.6:8 - Rationale
Educational research shows retention improves when abstract rules are
immediately paired with contrasting illustrations. By fixing the reading
order and mandating Tell‑Show‑Show inside every architectural pattern, FPF
embeds pedagogy into its architecture, realising Pillars **P‑2 Didactic
Primacy** and **P‑1 Cognitive Elegance** without weakening rigour.

### E.6:9 - Relations
* **Depends on:** `pat:constitution/guard‑rails` (GR‑1 ensures example jargon stays outside Core).
* **Constrains:** Placement of all Parts, patterns, and appendices.
* **Instantiates pillars:** P‑1, P‑2

### E.6:End

## E.7 - Archetypal Grounding Principle

### E.7:1 - Problem frame
Universal rules are powerful only when readers can grasp them. In FPF the
Conceptual Core speaks in substrate‑agnostic language: `U.Holon`,
Γ‑aggregation, MHT emergence. Practitioners need to “see” those rules in
familiar matter—physical hardware or bodies of knowledge—before they can
reuse them.

### E.7:2 - Problem
A purely abstract statement risks two failures:

1. **Didactic failure** – readers dismiss the pattern as “too meta,”
   violating Pillar **P‑2 Didactic Primacy**.
2. **Unproven universality** – without cross‑domain instantiation the rule
   remains an untested claim.

### E.7:3 - Forces

| Force | Tension |
|-------|---------|
| **Universality vs Concreteness** | Abstract law ↔ concrete example. |
| **Brevity vs Clarity** | Spec should stay concise ↔ dual examples add length. |
| **Rigour vs Accessibility** | Formal semantics ↔ intuitive narrative. |

### E.7:4 - Solution — mandatory *Archetypal Grounding* subsection

Every architectural pattern **SHALL** include a dedicated
section, titled exactly **“Archetypal Grounding,”** that *shows* how the
abstract law SCRs in FPF’s two canonical holon flavours:

1. **`U.System`** – the archetype of a **physical, operational holon**.
2. **`U.Episteme`** – the archetype of an **abstract, epistemic holon**.

This enforces a repeatable **Tell‑Show‑Show** rhythm:

| Stage | Content |
|-------|---------|
| **Tell** | `Solution` section states the universal rule. |
| **Show #1** | `Archetypal Grounding` – concrete `U.System` example. |
| **Show #2** | Same section – parallel `U.Episteme` example. |

### E.7:5 - Archetypal Grounding (of this pattern itself)

| Universal rule | `U.System` instantiation | `U.Episteme` instantiation |
|----------------|--------------------------|----------------------------|
| “Every architectural pattern requires grounding.” | Pattern *D.1 Algebra of Aggregation* illustrates Γ\_sys on assembling a water pump. | The same pattern illustrates Γ_epist on merging a meta‑analysis. |

### E.7:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑AG.1** | Every architectural pattern in Parts A, B, C, D, E **SHALL** contain a subsection headed exactly *“Archetypal Grounding”*. | Guarantees consistent Tell‑Show‑Show rhythm. |
| **CC‑AG.2** | The Archetypal Grounding subsection **MUST** illustrate the rule with both `U.System` *and* `U.Episteme`. | Demonstrates trans‑disciplinary reach. |
| **CC‑AG.3** | If a rule intentionally applies to only one substrate, the subsection **SHALL** state the scope limitation and justify it against the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Prevents silent bias; links to Bias‑Audit guard‑rail. |
| **CC‑AG.4** | Patterns lacking a compliant Archetypal Grounding subsection **MAY NOT** progress to “Accepted” status. | Enforces discipline without referring to workflow mechanics. |

### E.7:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Immediate clarity** – readers see abstract laws in action. | Patterns grow by one short table; mitigated by consistent template snippet. |
| **Proof of universality** – every rule is self‑documenting across substrates. | Authors must think cross‑domain; fosters richer patterns. |
| **Narrative cohesion** – recurring System/Episteme protagonists create a memorable storyline. | — |
|Built-in Proof of Universality: The specification consistently demonstrates its trans-disciplinary claims, building trust and credibility. | — |

### E.7:8 - Rationale
Tell‑Show‑Show is a proven pedagogical sequence. By making it normative,
FPF hard‑codes **P‑2 Didactic Primacy** into the fabric of every architectural
pattern while still honouring **P‑1 Cognitive Elegance**—the grounding
section replaces brittle ad‑hoc anecdotes with a disciplined dual
example. Linking scope‑justification to the five Principle lenses ties the
pattern to the **Taxonomy‑Guided Bias Audit** and keeps governance
language out of the Core.

### E.7:9 - Relations

* **Implements macro flow:** `pat:authoring/didactic‑architecture` (E.6)
* **References base types:** `pat:kernel/holon` (A.1) (`U.System`, `U.Episteme`)
* **Interacts with bias guard‑rail:** `pat:guard/bias‑audit` (E.5.4) via CC‑AG.3
* **Constrains:** Authoring template in `pat:authoring/pattern‑template` (E.8)

### E.7:End

## E.8 - FPF Authoring Conventions & Style Guide

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)

### E.8:0 - Use this when

Use `E.8` when you are writing, revising, or reviewing one FPF pattern and need to know what shape, voice, reader-recognition role, and assurance support the pattern must carry before it can be treated as mature FPF text.

Use it especially when a draft is technically correct but hard to use: the cold reader cannot tell when to apply it, what action to take, what mistake that action prevents, where neighbouring patterns take over, or which assurance material is informative support rather than the first user-facing guidance.

**Not this pattern when.** Use `E.9` when the main work is deciding why FPF should change and how that decision is distributed across patterns. Use `E.19` when the main work is an admission or refresh review. Use the local domain pattern when the question is what FPF says inside that domain rather than how a pattern should be authored.

### E.8:0.1 - What goes wrong if missed

A pattern can satisfy a checklist and still be practically unreadable. It may open with package architecture instead of a recognisable working moment, bury its payoff, hide its neighbouring boundaries, or let assurance prose silently replace the reader-facing claim. The result is a formally neat text that authors can defend but practitioners cannot reliably use.

### E.8:0.2 - What this buys

`E.8` gives FPF authors one shared pattern shape and one shared authoring discipline: recognition text first, assurance text second, canonical sections present, terminology kept stable, SoTA used as live support rather than decoration, and practical consequences visible before a reader has to reconstruct the architecture.

**First useful move.** Put the working situation, first action-guiding move, practical payoff, ordinary boundary, and heavier-support condition into the recognition text before tightening template details or conformance material.

**Cheap stop.** If the draft already gives a cold reader the working situation, first useful move, practical payoff, ordinary boundary, and nearest heavier support condition, do not add more authoring apparatus just to look mature. Use conformance material to verify that guidance; do not let it replace the guidance.

**Load-bearing authoring extension.** Add heavier assurance, conformance, SoTA, or relation-support material only when the light recognition text would leave a live false claim, unstable governed object, hidden neighbouring-pattern boundary, unsupported practical payoff, or misleading admissible use.

**Maturity rule.** Section completeness is not pattern maturity. A pattern matures when its `Problem frame`, `Solution`, worked cases, boundaries, and conformance checks all point to the same usable action guidance.


**Governed object in plain terms.** The governed object is the authored FPF pattern body: its canonical sections, reader-recognition role, wording discipline, examples, rationale, anti-patterns, SoTA-Echoing, and relations.

**Primary working reader.** The first reader is an FPF author or reviewer shaping pattern prose for later practitioners and managers. The downstream practitioner is the reader the pattern must ultimately serve, so the authoring guide must model the same recognition discipline it requires.

### E.8:0.3 - Pattern Kind In Plain Terms

An FPF pattern is an action-guiding method description for a recurring working situation. It is applied by an intended FPF user who recognizes the situation, understands the problem and forces, and then uses the `Solution` to decide what to do, what to stabilize, what to avoid, and what practical change should follow.

A pattern is not a procedure, function, API, workflow engine, parameterized call, or checklist bundle. Its `Problem frame`, `Problem`, `Forces`, `Solution`, `Consequences`, worked slices, and anti-patterns carry the guidance. Its `Conformance Checklist` checks whether that guidance has been applied and authored correctly; it must not replace the `Solution` or turn the pattern into a control form.

The primary load-bearing job is constructive method guidance: the pattern must say what the user should do so the recurring error does not arise. Error prevention, auditability, and conformance checks are evidence that the guidance is usable; they are not the pattern's center.

When an action-adjacent pattern classifies wording, a name, a publication face, an explanation class, a comparison unit, or another semio-facing object, that classification is only useful if it returns to action guidance. The pattern must say what use or action is admissible now, what neighboring use or action is not admissible under the current pattern, and which exact neighboring FPF pattern governs the case when the live claim has become work, evidence, gate, decision, assurance, engineering justification, release, or reliance.
### E.8:1 - Problem frame
FPF grows through the addition of patterns written by authors from many
disciplines. Without a shared structure *and* voice, the framework would
fracture, violating Pillars **P‑1 Cognitive Elegance** and
**P‑2 Didactic Primacy**.

### E.8:2 - Problem
*Structural drift* and *stylistic fragmentation* threaten three qualities:

1. **Comparability** – readers cannot align patterns lacking common
   headings.
2. **Narrative cohesion** – prose swings from dry jargon to informal
   blog style.
3. **Reviewability after guidance** – missing sections hide boundary and support checks
   (Archetypal Grounding, Bias‑Annotation) that let reviewers verify the action guidance without replacing it.

### E.8:3 - Forces

| Force | Tension |
|-------|---------|
| **Uniformity vs Expressiveness** | Consistent template ↔ freedom for diverse domains. |
| **Rigor vs Readability** | Formal precision ↔ engaging prose. |
| **Brevity vs Completeness** | Concise patterns ↔ mandated safety subsections. |

### E.8:4 - Solution — One template, enriched by style principles

#### E.8:4.1 - Canonical Pattern Template
Within each pattern, the **canonical** section headings **SHALL** appear in the order below.
For each **canonical content section heading (1–12)**, the `<Title>` component (after the heading separator, e.g. ` - `) **MUST** start with the canonical section title (case-insensitive match; canonical capitalisation preferred); an optional clarifier after an em dash is allowed (e.g., `Solution — …`).
The **Footer marker** (section **13**, if present) is a sentinel and is governed by **H-9** rather than the standard `<FullId> - <Title>` shape.

**Extensibility.**
Authors **MAY** add additional sections. Prefer expressing them as subsections under the nearest canonical section (e.g., `4.1`, `4.1.1` under *Solution*). If an additional pattern-level section is necessary, it **MUST NOT** delete or reorder the canonical sections and its title **MUST NOT** shadow a canonical title.

**Mandatory vs optional.**
* Canonical sections **1–13** are mandatory in every pattern.
* The escape hatch `Not applicable` is permitted **only** where explicitly stated below; when used, it **MUST** include a short justification (1 paragraph).
* **First substantive authoring seed.** The first non-empty authored body of a live pattern **SHALL** already instantiate the canonical section frame by value: title line, header block, canonical sections **1–13**, and the footer marker.
* Recognition-role openings and first-minute working guidance belong **inside** that canonical frame. Any retained legacy pre-template entry material must also stay inside that same canonical frame rather than appearing as one pre-template opening memo. Authors **MUST NOT** seed one pre-template opening memo and postpone canonical sectioning, `Conformance Checklist`, or footer-marker installation to one separate `E.19`, assembly, or review-repair pass.

**Template:**
- **Title line:** Hashes + FullId + ` - ` + Pattern Title; optional `(informative)` note.
- **Header block:** Type, Status; optional Normativity override.
1. **Problem frame**
2. **Problem**
3. **Forces**
4. **Solution**
5. **Archetypal Grounding** (Tell-Show-Show; System and Episteme; `Not applicable` allowed only with justification)
6. **Bias‑Annotation**
7. **Conformance Checklist**
8. **Common Anti‑Patterns and How to Avoid Them** (`Not applicable` allowed only with justification)
9. **Consequences**
10. **Rationale**
11. **SoTA-Echoing** (post-2015 practice alignment; terminology drift and deltas; full comparison or reduced SoTA required whenever external or internal practice changes the Solution)
12. **Relations**
13. **Footer marker**

**Footer marker.** End each pattern with a single visible sentinel heading line on its own: `### <PatternId>:End`. This makes truncation detectable even when HTML comments are stripped or surfaced by editors. The footer marker is intentionally content‑free: **do not** place prose under it.

*Note.* Pattern boundaries are still parseable by scanning for the next pattern heading (`## …`), but an explicit `:End` marker helps retrieval pipelines (and LLM prompts) distinguish “this chunk is the whole pattern” from “this chunk was cut mid‑pattern”.

##### E.8:4.1.1 - Heading & ID discipline (human tooling + retrieval)
FPF is often consumed through full‑text search and retrieval (RAG). A reader or an LLM may see a subsection without its parent headings, so headings must be **self‑identifying**.

**H-1 (Heading shape).** Every pattern heading and every subsection heading inside a pattern **SHALL** follow:
`<hashes> <FullId> - <Title> (optional note of non‑normativity)`

*Exception.* The **Footer marker** is a sentinel heading and is governed by **H-9**, not by the standard `<FullId> - <Title>` shape.

**H-2 (Heading separator).** The canonical separator between `<FullId>` and `<Title>` is ` - ` (ASCII, space-hyphen-space).
Legacy text may use Unicode dash variants such as ` – ` or ` — ` as separators; tooling **SHOULD** treat those variants as migration candidates, and authors **SHOULD** migrate touched headings to ` - `.

**H-3 (FullId).** `FullId` is the full hierarchical address.
For a **pattern heading** it is the pattern ID (e.g., `A.2`, `E.10.D1`).
For **headings inside a pattern**, append dot‑separated ordinal section numbers after the colon (`:`) (e.g., `A.2:4.4`, `E.10.D2:3`).
*Exception:* the Footer marker uses the reserved sentinel token `:End` as defined in **H-9**.
The colon (`:`) is **reserved** for section paths and **MUST NOT** appear in pattern IDs.

**H-4 (Ordinals).** Ordinals in section paths **SHOULD** track the canonical template numbering (**1 = Problem frame**, …, **13 = Footer marker**) to maximise cross‑pattern comparability. During refactors or in legacy patterns, ordinals **MAY** be local. In that case, the **canonical section title at the start of `<Title>`** is the semantic key; readers and tools **MUST NOT** infer section semantics from the ordinal alone.
*Note:* the Footer marker itself is exempt from ordinal encoding; it uses the reserved token `:End` (see **H-9**).

**H-5 (Where kind and normativity live).** Pattern **kind** (e.g., Architectural / Definitional) **MUST** be declared in the **Header block**, not encoded into the heading text. Normativity (**normative** / **informative**) **MUST** also live in the Header block when it deviates from the default. If a reminder is needed for readers, authors **MAY** add a short parenthetical note at the end of the heading (e.g., `(informative)` / `(non‑normative)`), but headings **MUST NOT** use square‑bracket tags.

**H-6 (Heading levels).** Heading levels **MUST** preserve a fixed offset between structural layers (Part or Cluster (flat) → Pattern → Pattern sections):
* Part and Cluster headings **MUST** use `#` (level 1) across the file.
* A Pattern heading **MUST** use `##` (level 2).
* Inside a pattern, each nested section **MUST** add exactly one `#` per level (e.g., `## A.2 - …`, `### A.2:2 - …`, `#### A.2:2.1 - …`).

**H-7 (Ellipsis discipline).** Authors **MUST NOT** use **three consecutive full stops/dots** (`...`) as punctuation in headings or narrative prose. Authors **MUST** use the Unicode ellipsis `…` (U+2026) instead. For editorial elisions in quotations, authors **SHOULD** prefer `[…]` to make the omission explicit and distinguish it from retrieval truncation.
*Exception:* literal three‑dot sequences that are part of an external language’s syntax **MAY** appear **only inside code spans or fenced code blocks**.

**H-8 (Normative keywords).** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119, as clarified by RFC 8174 (only when capitalised). Authors **SHOULD** avoid informal deontic phrasing (“need to”, “is required to”) in normative clauses.

**Deontics vs admissibility.** Use RFC keywords only for **deontic obligations** (requirements on authors, reviewers, implementers/tooling, or published pattern or support texts) — i.e., things an agent can choose to do or omit. Do **not** use RFC keywords to state **definitions**, **structural invariants**, **typing rules**, or other **admissibility conditions** of the modeled world.

When you need an enforceable constraint that is *mathematical* rather than *deontic*, express it as a non‑deontic predicate using one of: `Definition:`, `Invariant:`, or `Well‑formedness constraint:` (optionally with formal quantifiers). Prefer mathematical terms like `cardinality 1..1 (total)` / `0..1 (partial)` / `0..n` over deontic adjectives like “mandatory or optional” when the intent is cardinality, not duty.

**Admissibility predicate discipline (recommended shape).**
When expressing admissibility/validity constraints as predicates (`Definition:` / `Invariant:` / `Well‑formedness constraint:`):
* Authors **MUST NOT** use RFC keywords inside the predicate block.
* Authors **SHOULD** give each predicate a stable identifier and short name (e.g., `RA‑1 (Locality)`, `RE‑3 (Method gate)`), so that Conformance Checklist items can reference it without re‑authoring the rule.
* Authors **SHOULD** write the constraint as a declarative predicate (optionally quantified), e.g., `role ∈ Roles(context)`, rather than as “X MUST …”.
* If the constraint needs to be checked as part of pattern conformance, authors **SHOULD** reference the predicate identifier from the Conformance Checklist (and/or call out validator behaviour), rather than duplicating the predicate with RFC keywords.

**H-9 (Footer marker sentinel).** Footer marker **SHALL** be a single heading line whose `FullId` is the pattern ID followed by the reserved sentinel token `:End` (no ordinals, no title, no square‑bracket tags):
`### <PatternId>:End`
It is the only allowed heading *inside* a pattern whose section token is non‑numeric. It **MUST** be the final line of the pattern and **MUST NOT** carry any prose. Tooling and readers **MUST** treat it as a boundary sentinel, not as a semantic section.

*Unification note:* historic A‑ and D‑templates differed only by the presence/absence of **Bias‑Annotation** and **Relations**; the unified template keeps the headings everywhere while allowing explicit `Not applicable` statements when justified.
The Alexandrian pattern canon historically calls *Problem frame* “Context”. FPF avoids that label because **Context** is already overloaded in FPF (e.g., `U.BoundedContext` and its Plain‑register label).

#### E.8:4.2 - Stylistic Principles (S-0 ... S-19)

| # | Principle | Guideline |
|---|-----------|-----------|
| S-0 | Narrative Flow Seven-Step Heuristic | Authors are encouraged to structure major paragraphs or subsections using the seven-step mnemonic. |
| S-1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S-2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S-3 | Embedded Mini-Definitions | Gloss a new term in parentheses on first appearance. |
| S-4 | Contextualisation | Brief historical or disciplinary lineage anchors. |
| S-5 | Prophylactic Clarification | Pre-empt common misreadings inside the prose. |
| S-6 | Quotable Closers | Finish Solution or Consequences with a memorable aphorism. |
| S-7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S-8 | Trans-disciplinary Tie-ins | Illustrate using at least two distinct fields. |
| S-9 | Physical Grounding Reference | Link abstractions to a `Transformer` or physical process. |
| S-10 | Punchy Blocks | <= 5 sentences per paragraph; lists for clarity. |
| S-11 | Narrative Flow | Ensure sections read as a continuous story, not bullet soup. |
| S-12 | Full sentences over tags | Avoid “keyword soup”. Each list item SHOULD contain a subject and a verb; prefer 2-4 sentence micro-paragraphs to bare tag lists. |
| S-13 | SoTA-Echo craft | In the SoTA-Echoing section, present: **claim -> practice -> source -> alignment -> adoption status (adopt/adapt/reject)**; cite Bridges & CL when crossing Contexts/planes. |
| S-14 | Support-content sufficiency | New and substantially revised patterns carry enough supporting content to be teachable without nearby project notes. |
| S-15 | Worked slices over scenario labels | Transform-like families show at least one concrete source and resulting-publication slice; scenario names alone are not enough. |
| S-16 | Ordinary vs load-bearing realism | Keep ordinary use light, and make heavier review records explicit only for disputed, high-risk, or higher-impact cases. |
| S-17 | Self-contained monolith prose | A merged pattern must explain itself inside the monolith; planning shorthand and review-context dependencies are not admissible in live prose. |
| S-18 | Reader-role discipline | Keep live pattern prose addressed to the intended FPF user; move package-development and architecture-placement rationale to separate companion notes or clearly marked informative placement notes. |
| S-19 | Precision before relaxation | In load-bearing prose, restore the head kind named by a generic phrase before treating any qualifier as trustworthy semantic guidance; then restore the load hidden in the qualifier before allowing any later plain, didactic, or coarsened restatement. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight. Engagement remains subordinate to semantic discipline: hooks, quotable lines, Plain restatements, and didactic images may improve recognition, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load they carry must be recoverable through the governed Tech reading or named neighboring pattern. Ordinary Plain prose without that load stays ordinary prose.

**S-0 (Narrative Flow Seven-Step Heuristic) — explanation**
Narrative flow is recommended to follow these steps: **Hook -> Frame -> Weave -> Anchor -> Bridge -> Flow -> Close**.

Brief explanations:
| Step       | Purpose in a paragraph/section                             |
| ---------- | ---------------------------------------------------------- |
| **Hook**   | Open attention with a vivid but bounded image or paradox that maps back to the governed object and claim. |
| **Frame**  | State the specific question or problem space.              |
| **Weave**  | Connect to earlier patterns or Pillars.                    |
| **Anchor** | Tie to a concrete System/Episteme or physical process.     |
| **Bridge** | Show the implication for the upcoming claim or rule.       |
| **Flow**   | Deliver the formal content or argument.                    |
| **Close**  | End with a quotable line or payoff that reinforces memory. |

Narrative Flow Heuristic also operationalises S-1 (Density w/o Jargon), S-2 (Internal Cohesion), S-4 (Contextualisation), and S-6 (Quotable Closers).
#### E.8:4.2.1 - Recognition text and assurance text
Every canonical pattern SHALL stabilise one governed object early enough that a cold reader can tell what kind of thing the pattern is actually governing. If ordinary forms vary (`note`, `sheet`, `guided UI`, `rendering`, `review aid`), the text must make explicit which of those are merely presentation forms of one governed object and which would instead name a different act, process, work-result record, or governing support companion. Recognition and assurance texts may refine that object differently, but they must not silently swap the central object kind.

If a pattern uses a broad umbrella or head together with a narrower operative branch, the text must also make the stack explicit early enough for first reading: what the broad head names, what the current narrowed branch is, what governed object is actually in play, what move is being carried by that object, and what wider work or process remains outside the pattern. A qualifier alone does not restore that stack.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `recognition shell / assurance shell` wording is retired.
These names refer to two reading-order roles carried by existing sections or projections inside one pattern; they do **not** mint new `authoritySourceRef` targets, governing-pattern relations, publication-form/face kinds, `SurfaceKind`s, or a second face family.
A third didactic support role remains optional and is justified only when the family is especially easy to misuse, easy to over-read, or hard to teach without extra scaffolding.

The **recognition text** is the first reading text.
It is the part of the pattern that lets a cold working reader recognise the situation quickly enough to decide whether to keep reading.
It should start from a subject-domain or practice moment before internal taxonomy whenever the pattern is meant to help real work rather than only internal canon maintenance.
In practice it usually lives in an early `Use this when` line or equivalent opening, plus the upper parts of `Problem frame`, `Problem`, `Solution`, `Consequences`, and nearby worked slices.
Its job is to make visible:
- what ordinary working situation this pattern is for;
- what goes wrong if the pattern is missed;
- what the pattern buys the reader in practice;
- when this is not the right pattern;
- what governed object is actually being kept stable;
- and, when technical terms must appear early, a pairwise plain gloss for each early load-bearing term.

The **assurance text** is the second reading text.
It carries the heavier load-bearing material that makes the pattern reviewable and auditable:
- declaration blocks and typed fields when those are part of the pattern's declared conformance or boundary claim;
- representation ontology, described-entity discipline, or governed-object discipline;
- any minimal modeling or mathematical lens that keeps the governed object stable;
- guidance/check, invariants, admissibility, and exit or neighbouring-pattern conditions;
- `SoTA-Echoing` when it is carrying live explanatory load;
- and the review hooks that let a broader or more consequential reading be checked explicitly.

The assurance text may sharpen, justify, and discipline the recognition text.
It must **not** silently replace, strengthen, or universalize the claim that the recognition text made visible.
If the recognition text says “this pattern helps with a bounded working situation”, the assurance text must not quietly turn that into an unsupported carrier claim, unsupported guarantee, or broader universality claim.

If a pattern claims **universal** or **transdisciplinary** status, that claim must already be visible in the recognition text.
It is not enough for universality to appear only later in a guidance/check sheet, declaration block, or `SoTA-Echoing` rationale.
A broad claim should therefore be demonstrated in the recognition text through at least **three heterogeneous reader or domain situations**.
When a compact matrix helps, `F.16` is the preferred template for showing that breadth.
If `SoTA-Echoing` is load-bearing, the practical implication of those rows should be recoverable from the recognition text and case bank rather than remaining a late-only justification layer.

A **third didactic support role** means enough didactic and operational support that the pattern survives without nearby project documents. Typical indicators include:
- at least one concrete source and resulting-publication slice in Archetypal Grounding when the pattern governs transforms or publication change;
- at least one boundary-heavy example or anti-example when nearby patterns or other governing support roles are easy to confuse;
- reviewer guidance that tells what to inspect first and which neighboring FPF pattern governs the failure mode and which exact project-side FPF kind and reference carries the claim or effect;
- local mini-definitions or glossary support for recurring terms that would otherwise be recovered only from project context.

Pattern density is therefore not “more metadata” and not “longer tag lists”. It is the presence of enough recognition, assurance, and, when needed, extra didactic support that a reader can understand the pattern, apply it lightly in ordinary cases, and recognise when a heavier review path is required.
#### E.8:4.2.2 - Package-form and governing-pattern relation role-word discipline

FPF pattern prose is not free-form descriptive English. When authors name a *package-form* or a *governing-pattern relation*, they must use role words with stable semantic intent.

Use the following distinctions explicitly:

This is a cross-cutting review discipline, not a replacement for local pattern lexica. For example, `A.6.7` / `A.19.CHR` already carry the suite/kit/pack distinction, and `E.17.1` already carries the viewpoint bundle/family/library distinction.
- **governing pattern** = the pattern that carries the primary guidance/check load of the family;
- **specialization** = a named refinement under an existing governing pattern;
- **overlay** = a cross-cutting governance or reading layer over existing governing patterns;
- **profile** = a declarative review/use role derived from a governing pattern rather than a replacement pattern;
- **family** = a recurring class of cases governed by one pattern or governing support companion;
- **bundle** = a packaged set of defaults, allowances, or coordinated members;
- **cluster** = a navigation or reading grouping; not by itself a governing-pattern claim;
- **suite** = a coordinated set of members with explicit suite semantics under the governing FPF pattern or named authority reference;
- **pack** = an editorial or review grouping, not automatically a semantic-authority claim;
- **kit** = a reusable coordinated publication or boundary-description package with kit-level semantics under the governing FPF pattern or named authority reference;
- **record** = a case, report, or review record;
- **umbrella** = a provisional or review-stage head spanning possible subfamilies before a final governing FPF pattern, accepted `DRR`, or pattern-body decision.

These words are not interchangeable. In particular, authors must not let `cluster`, `bundle`, `suite`, `family`, `profile`, `overlay`, or `umbrella` do the work of an unnamed governing-pattern relation. When that relation matters, it must be stated directly: `specialization under ...`, `profile governed by ...`, `overlay over ...`, `bundle under ...`, or another equally explicit formulation.

A pattern may reuse a pattern-native role word when that role is already defined by the governing pattern. Outside that case, authors must not improvise near-synonyms or shift between role words for stylistic variety.

#### E.8:4.2.3 - Reader-role discipline for live pattern prose

A live pattern is written for its intended FPF user: the person who will use the pattern to organise thought, inspect a case, publish a note, or review a result under that pattern.
Its load-bearing sections therefore explain what the pattern lets that user do, what it forbids, what it costs, and how it relates to neighbouring patterns in user terms. When neighbouring patterns or other governing support roles are named, the prose should answer one user question such as `which neighboring FPF pattern applies`, `which exact project-side FPF kind and reference is live`, `which nearby pattern is easy to confuse`, or `what must stay coordinated here`; it should not read as one explanatory aside about why the package architecture was split that way.
`E.8` reader and reviewer wording is FPF pattern-authoring wording. Project-side publication readers, explanation readers, comparative review units, and participants in named project-side review relations are governed by the publication or project-side patterns that name those live objects, such as `E.17`, `E.17.ID.CR`, `E.17.EFP`, `A.10`, `A.15.4`, `A.20`, or `A.21`.

Authors must keep FPF-development or package-architecture material separate from that user-facing body.
In particular, `Problem`, `Solution`, `Consequences`, `Rationale`, worked slices, and ordinary-vs-load-bearing guidance must not do the work of:
- arguing that the material is worth isolating;
- justifying overlay/profile/governing-pattern or authority-reference choice as a package decision;
- discussing authority-reference freeze, naming freeze, merge posture, blast radius, or safest landing form;
- or narrating future package promotion or defer decisions.

If architecture-placement commentary is still helpful, the default place is a separate companion note or ADR-like architecture note.
A live pattern may include a short optional informative subsection such as `Architectural placement note (informative)` only when that placement materially helps users avoid misuse; even then, it must stay clearly separated from the user-facing solution and rationale rather than replacing them.

#### E.8:4.2.4 - Human-facing fit beyond role correctness
Human-facing fit is also subject-domain fit. A recognition text that starts from internal taxonomy, pattern-placement convenience, or package-architecture wording before the problem-domain moment is still under-authored even if its later guidance/check text is correct. When a broader umbrella name and a narrower operative branch are both live, the recognition text should also tell the reader which stack is actually active rather than leaving that reconstruction to a later declaration block or companion note.

A pattern can already be role-clean, boundary-clean, and reader-role-clean, yet still fail the first minute of use for a cold working reader.
That failure usually appears when the text is admissible but does not yet make the working situation, practical payoff, governed object, non-use boundary, or first action-guiding move visible enough.

**P-2 semantic cleanup check.** When `E.10.SEMIO` is used to repair pattern prose, the first admissible action-guiding move must survive as a remaining admissible reader move or be replaced by a named neighboring-pattern handoff that now carries the live claim. This is a direct `E.2` `P-2` and `E.12` requirement, not an optional style preference. Intentional didactic metaphors and vivid Plain recognition lines are admissible when they are ordinary recognition aids or when their load maps back to Tech under `E.10:6.2`. A semantically corrected rewrite that leaves the recognition text inert is still under-authored.


For canonical patterns, the first reading text should behave as a **recognition text** and the heavier review load should remain in an **assurance text**.

When a pattern claims practice guidance or is meant to be used by engineers, managers, researchers, or other working readers, authors should make the following visible before the heavier harness takes over:
- a recognisable `Use this when` or equivalent first-minute recognition cue;
- a concrete working situation in `Problem frame`, not only taxonomic or pattern-placement language;
- a short statement of what goes wrong if the pattern is missed or misread;
- a short statement of what this pattern buys the reader in practice;
- the first admissible action-guiding move the user should take in that situation;
- a short `Not this pattern when` boundary for ordinary nearby non-use cases;
- one minimally viable worked case or use slice that shows what changes in practice;
- when a typed declaration block, formal lens, or other compact modeling support is load-bearing, a short user-facing statement of what kind of object the pattern is governing and what minimal lens keeps that object reviewable;
- pairwise plain glosses for any load-bearing technical terms that must appear before the heavier declaration role arrives;
- when `SoTA-Echoing` is carrying live explanatory load, a short working-reader implication for each row or cluster of rows and a visible link back to the case bank or worked slices that those rows discipline;
- a visible split between the recognition text and the heavier assurance text or support companion;
- and, if the draft implicitly serves several working-reader situations, an explicit primary working reader, primary concern, or primary viewpoint.

**Problem-frame recognition signature (informative).** A canonical pattern should
expose the working situation through its `Problem frame`, not through one
separate navigation block. When an `E.11` pattern-entry discoverability problem
is live, the same `Problem frame` may also carry candidate-pattern and
tempting-wrong-pattern cues; otherwise it should stay with action guidance
rather than becoming a local catalogue row.

The local recognition signature should make recoverable:

- the concrete working situation;
- the governed object or stabilized concern;
- what goes wrong if the pattern is missed or misread;
- the first admissible action-guiding move and what that move buys;
- the ordinary not-this-pattern boundary;
- the first admissible action-guiding result; when an `E.11` discoverability
  problem is live, the first admissible entry stop or entry-stabilizing result.

`Use this pattern when`, `This pattern applies when`, or equivalent `Problem
frame` prose may be used as the first sentence or compact cue of this
signature.
It is not one separate required section.
Cross-pattern comparison belongs in `J.4`; expanded case reading belongs in
`I.2`.

If the prose points to neighbouring patterns or other governing support roles, it should present them as neighboring FPF patterns, exact project-side FPF kinds and references, or `E.11` entry-load reclassifications rather than as hidden co-authorities of the current pattern.

If the pattern claims broad, universal, or transdisciplinary usefulness, that breadth should already be visible in the recognition text.
At minimum the recognition text should show at least three heterogeneous reader or domain situations rather than one narrow case family with a later broad claim attached.
When a compact matrix helps, `F.16` is the preferred template for making that breadth legible.

This is not a request to flatten the pattern into plain language only.
It is a rule about ordering, layering, and text consistency: the recognition text must help a working reader recognise the pattern early, while the assurance text continues to carry the full semantic load.
If the pattern uses technical lexicon, ontological distinctions, or a mathematical lens, those supports must remain recoverable, but the first reading text should not require the reader to decode that full stack before recognising the working situation.
The assurance text may tighten or discipline the recognition text; it must not silently shift what the recognition text claimed.

**Illustrative migration example (informative).**

Old pre-template top:

```text
Start here when the dominant live question is API, protocol, SLA, published boundary, or compliance wording.
First output: Claim Register.
Neighboring pattern exits / entry-load reclassifications: A.6.B, A.6.C.
```

Repaired Problem-frame recognition signature:

```text
Use this pattern when boundary-facing language - API, protocol, SLO/SLA, compliance clause, or other published boundary description - mixes guidance/check clauses, admissibility gates, duties, and evidence into one sentence or published boundary description.

If missed, the text becomes boundary-claim soup: runtime behavior, governance, and evidence are treated as one undifferentiated promise.

Do not use this pattern merely because the text mentions an API or boundary description. If the live question is still one unstable cue, preserve it through the admissible cue-preservation line first.

First admissible action-guiding result: one `A.6.B`-governed atomic claim set or one Claim Register whose live claim/use questions are explicit enough for the governing FPF pattern or named project-side FPF kind and reference to inspect.
```

#### E.8:4.2.5 - Design-time and run-time referents stay separated in live pattern prose

Live pattern prose must keep its referent index explicit. In ordinary body sections, the default truth-makers are run-time or governed-domain objects, states, moves, boundaries, consequences, and user-facing practical effects. Standard-plane wording is still admissible when the sentence is explicitly about the standard as a normative publication, for example in marked legacy navigation examples, marked informative notes, or conformance/checklist clauses.

Design-time and control-plane referents are different objects. The current draft, current body, current pass, author, reviewer, handoff, packet, governing support companion, landing choice, or other writing-process/control objects must not be smuggled in as the hidden truth-condition of live pattern prose. A quick test is: what makes this sentence true? If the sentence is true because the current text is arranged a certain way, because the author or reviewer must do something next, or because the current control state says so, then it is design-time residue, not live pattern content.

Move that material to the authored-slice carrier, handoff, `DRR`, or companion architecture note. If a sentence is kept in the live pattern, rewrite it so that its truth depends on the governed run-time/domain object or on the standard's declared normative claim set rather than on the current writing pass.

If a pattern or example claims **autonomy** for any Role/Method/Service:
1) Add a subsection **“Autonomy (RoC‑E.16)”** that lists:
   * `AutonomyBudgetDeclRef` (id, version, Scope (G), Γ_time),
   * `Aut-Guard policy-id (PolicyIdRef)`,
   * `OverrideProtocolRef` (SpeechAct names, SoD),
   * pointer to where **Green‑Gate** applies in the Method steps,
   * where **AutonomyLedgerEntry** is recorded on `U.Work`.
2) Include one **Tell‑Show‑Show** vignette that demonstrates **depletion** and **override** handling.
3) Use **LEX‑BUNDLE** terms (Scope (G), Γ_time, Role/Method/Work). Avoid “validity”, “process”, “actor”, “system”, “mechanism” unless mapped to kernel types.

### E.8:5 - Archetypal Grounding (System / Episteme)

| Template element | `U.System` illustration | `U.Episteme` illustration |
|------------------|------------------------|---------------------------|
| Section order | Pump‑assembly pattern follows sections **1–12** (and, optionally, **13**). | Meta‑analysis pattern follows the same sections. |
| S‑1 Density w/o Jargon | “The pump boundary is the sealing plane.” | “This episteme raises **F (Formality)** by making falsifiers testable.” |
| Hook‑Weave‑Anchor | Opens with field anecdote → weaves in Γ‑core → anchors to motor torque. | Opens with historical paradox → weaves in **A.10** anchors → anchors to peer‑review data. |

*Note:* Prefer examples that reuse FPF’s own characteristics vocabulary (e.g., **F (Formality)** rather than “F‑score”) unless you explicitly mean an external metric and name it as such.

### E.8:6 - Bias‑Annotation
Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for the authoring conventions in this pattern.
This guidance biases toward **Did** (readability, narrative flow) and **Arch** (template regularity) by design; the mitigation is explicit optionality (`Not applicable`) and the requirement to justify omissions in‑text.

### E.8:7 - Conformance Checklist

**CC style (canonical).**
Conformance Checklist items are authoring checks: they test whether the pattern guidance has been applied and written correctly in a pattern or support text that claims conformance. They do not replace `Solution`, do not make the pattern a control form, and do not state deontic obligations about the modeled world. A CC clause of the form “X SHALL ...” is to be read as “In a conforming pattern or support text, X SHALL ...”.

**Preferred wording for new or edited CC items:** start with an explicit conformance subject (e.g., “Authors ...”, “Reviewers ...”, “A conforming implementation ...”, “A validator ...”). If a CC item is enforcing an admissibility predicate, it **SHOULD** cite the predicate’s identifier (from a `Definition:` / `Invariant:` / `Well-formedness constraint:` block) rather than restating the predicate as “X MUST ...”. For boundary/interface/protocol/declaration patterns, prefer A.6.B-governed claim IDs (L/A/D/E) or cite an existing Claim Register (A.6.B:7) instead of restating mixed prose.

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC-SG.0 (Heading discipline).** | Pattern and subsection headings **SHALL** follow **H-1 ... H-9** (FullId prefix, reserved punctuation, heading levels, ellipsis discipline). The Footer marker **SHALL** follow **H-9**. | Makes chunks self-contained; reduces ambiguity between author elision and retrieval truncation. |
| **CC-SG.1** | Every new pattern **SHALL** follow the section order defined in the Canonical Template (Title block -> ... -> Footer marker). | Guarantees structural comparability. |
| **CC-SG.1a (Initial live draft shape).** | The first non-empty authored version of a live pattern **SHALL** already use the canonical section frame (Title block -> Footer marker). Authors **MUST NOT** start from one pre-template opening memo and promise to backfill canonical sections later. | Prevents large late-stage structural rewrites and keeps drafting aligned with `E.8` from the first substantive pass. |
| **CC-SG.2 (Grounding required).** | Every pattern **MUST** include an *Archetypal Grounding* section. If **System** or **Episteme** grounding is inapplicable, authors **MUST** state `Not applicable` and give a one-paragraph justification. | Keeps patterns teachable and reduces “definition-only” ambiguity. |
| **CC-SG.3** | The *Bias-Annotation* section **SHALL** cite the five Principle-Taxonomy lenses and declare either “Universal” or an explicit scope limitation. | Keeps cross-disciplinary neutrality explicit (ties to Guard-Rail 4). |
| **CC-SG.4** | Deontic normative sentences **MUST** use only RFC-style keywords (see **H-8**); RFC keywords **MUST NOT** appear inside `Definition:`/`Invariant:`/`Well-formedness constraint:` blocks. When enforceable, admissibility/validity predicates **SHOULD** be referenced by id from the Conformance Checklist (rather than duplicated as “X MUST ...”). Informal deontic verbs are prohibited in normative clauses. | Prevents ambiguity between obligation language and model validity; improves auditability. |
| **CC-SG.5** | Pattern prose **SHOULD** demonstrate adherence to Style Principles **S-0 ... S-19**; reviewers are empowered to request revision when clarity or didactic quality suffers. | Embeds common narrative voice without rigid policing. |
| **CC-SG.6 (SoTA-Echo required).** | Every pattern **SHALL** include a **SoTA-Echoing** section and clearly state divergence of its Solution from SoTA with explanation of why. Architectural patterns **SHALL** satisfy the full obligations below. Definitional patterns **SHALL** carry reduced SoTA when a full comparison is not meaningful: name which current practice is adopted, adapted, or rejected for terminology work, ambiguity or sense recovery, separation between constraint and ontology, controlled-vocabulary caution, or a comparable definitional problem. Internal coherence alone is not enough. | Ensures explicit lineage, guards against vocabulary drift, and prevents definitional patterns from using internal coherence as zero SoTA. |
| **CC-SG.7 (Post-2015, multi-Tradition).** | For Architectural patterns, SoTA-Echoing **SHALL** cite >= 3 post-2015 sources across >= 2 Traditions; each item **MUST** carry adoption status (adopt/adapt/reject) with reason. | Guards against monoculture; makes intent explicit. |
| **CC-SG.8 (Bridge & CL on reuse).** | Any cross-Context or plane reuse mentioned in SoTA-Echoing **MUST** cite **Bridge id + CL** and (if planes differ) **Φ(CL)**/**Φ_plane** policy-ids; penalties **-> R_eff** only. | Safe, auditable reuse. |
| **CC-SG.9 (Lexical hygiene).** | The term **mapping** **SHALL NOT** appear in SoTA-Echoing except in the precise E.10 sense; use **alignment/Bridge/relation** instead. | Avoids overloading reserved vocabulary. |
| **CC-SG.10 (No keyword soup).** | SoTA-Echoing items **MUST** be written as sentences (not bare noun phrases); bullet lists are acceptable only with complete clauses. | Improves didactic quality and comparability. |
| **CC-SG.11 (Anti-patterns).** | Every pattern **SHALL** include a **Common Anti-Patterns and How to Avoid Them** section. It **MAY** be `Not applicable` only with a one-paragraph justification. | Makes misuse paths explicit and reduces review churn. |
| **CC-SG.12 (Boundary claim-set discipline).** | If a pattern’s subject is a boundary, interface, API, protocol, connector, SLA, or other published boundary description, it **MUST** either (a) provide an **A.6.B**-governed atomic claim set (`L-*`/`A-*`/`D-*`/`E-*`, with stable IDs), or (b) explicitly cite an existing **A.6.B Claim Register** / governed claim set that it reuses. | Pulls A.6.B into the authoring contour, prevents boundary-kind soup, and makes review more explicit and repeatable. |
| **CC-SG.13 (Didactic sufficiency).** | New patterns and substantial revisions **MUST** remain understandable without project-planning notes. When a pattern introduces a new named family, profile, or specialization, or adds a non-trivial governing-pattern-derived note, its Solution and Grounding **SHALL** carry enough supporting content: explicit governing-pattern relation, ordinary-vs-load-bearing guidance, at least one concrete source and resulting-publication slice where applicable, and visible neighboring-pattern or exact project-side FPF kind and reference cues. | Prevents skeleton-only patterns and project-context leakage. |
| **CC-SG.14 (Controlled prose, not free shorthand).** | Load-bearing prose **SHALL NOT** rely on bare relation words or planning shorthand whose governing-pattern relation is left implicit (e.g., bare “species”, “branch”, “flow”, or API-like “input/output” language). When a governing-pattern relation matters, authors **MUST** name it explicitly (`specialization under ...`, `profile governed by ...`, `overlay over ...`, etc.). | Keeps pattern prose precise and self-identifying. |
| **CC-SG.15 (Package-form and governing-pattern relation role-word discipline).** | When a pattern names a package-form or the governing-pattern relation of a family (`primary carrier`, `specialization`, `profile`, `overlay`, `family`, `bundle`, `cluster`, `suite`, `pack`, `kit`, `record`, `umbrella`), the chosen role word **MUST** match the intended ontology and **MUST NOT** be swapped for stylistic variety or left to implication. | Prevents semantic blur in pattern prose and keeps governing-pattern relations auditable. |
| **CC-SG.16 (Reader-role discipline).** | Authors **MUST** keep live pattern sections user-facing. FPF-development or package-architecture reasoning about isolation, overlay or carrier choice, freeze, merge posture, or planned evolution **MUST NOT** occupy `Problem`, `Solution`, `Consequences`, `Rationale`, or worked slices; if such placement reasoning is still needed, it **MUST** live in a separate companion note or a clearly marked informative placement note. | Keeps pattern prose aligned with its intended reader and prevents package-governance leakage into live use guidance. |
| **CC-SG.16a (Referent-index discipline in live prose).** | Live pattern sections **MUST** keep run-time/domain referents, standard-plane referents, and design-time/control-plane referents distinct. In ordinary live prose, sentence truth **MUST** depend on the governed run-time/domain object or on the pattern's declared normative claim set, not on the current draft state, author action, reviewer action, or control-plane posture. If a sentence is true only because of the current writing/review pass or text arrangement, it is design-time residue and belongs in carriers or companion notes, not in the live pattern body. | Prevents Conway/process leakage and reduces late cleanup before review or landing. |
| **CC-SG.17 (Recognition text and assurance text).** | Admission or substantial revision runs **MUST** check that a canonical pattern exposes a recognition text early enough for the intended working reader and an assurance text that carries declaration, guidance/check, modeling, and review load without silently shifting the recognition-text claim. The recognition text **MUST** expose a recognisable working situation, what goes wrong if the pattern is missed, what the pattern buys, and a clear ordinary `not this pattern when` boundary. Any load-bearing typed declaration or modeling lens **MUST** be exposed by a short user-facing statement of the governed object, early load-bearing technical terms **MUST** receive nearby pairwise plain glosses, and any `SoTA-Echoing` used as live explanatory support **MUST** state a short practitioner or manager implication plus visible linkage to the worked cases or boundary slices it disciplines. If the pattern claims universal or transdisciplinary reach, the recognition text **MUST** demonstrate that claim through at least three heterogeneous reader or domain situations, preferably using an `F.16`-style example matrix or an equally explicit alternative. | Prevents text-clean but reader-opaque patterns and keeps broad claims visible where cold readers actually enter the text. |
| **CC-SG.17a (Problem-frame recognition signature and E.11 boundary).** | Authors **SHOULD** express a pattern's concrete working situation through the pattern's `Problem frame`, not through a separate navigation block. The `Problem frame` should make recoverable the governed object or stabilized concern, what goes wrong if the pattern is missed or misread, the ordinary not-this-pattern boundary, the first admissible action-guiding move, and the result that move buys. Only when an `E.11` pattern-entry discoverability problem is live should the same recognition text add candidate-pattern, tempting-wrong-pattern, entry-load reclassification, or first admissible entry-stop cues. Cross-pattern comparison belongs in `J.4`; expanded case reading belongs in `I.2`; lexical-query support belongs under the lexical/naming patterns and support companions that already govern it. Pattern-local `Start here when`, `First output`, neighboring-pattern lists, and `Common wrong escalations and boundary transfers` blocks **SHOULD NOT** replace the action-guiding `Problem frame` and `Solution`. | Keeps working-use recognition inside the canonical pattern frame while preventing navigation/workflow language from becoming local pattern structure. |
| **CC-SG.17b (Semantic repair preserves action guidance).** | When authors edit pattern prose under `E.10.SEMIO`, the repaired recognition text **MUST** preserve or restore the first admissible action-guiding move as a remaining admissible reader move, or explicitly name the neighboring FPF pattern that now carries the live claim. When both Tech and Plain registers are live, any Plain or didactic wording **MUST** map back to the recovered Tech reading under `E.10:6.2` when it carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load. More engaging recognition wording remains admissible as ordinary Plain prose only when it does not carry such load, or as a recognition aid whose load is recoverable through the recovered Tech reading or named handoff. Type-correct but inert wording is not mature pattern prose. | Prevents semio cleanup from leaving pattern guidance inert while also preventing expressive prose from reintroducing overread. |

| **CC-SG.18 (Precision before relaxation).** | In load-bearing prose, authors **MUST NOT** leave a generic head noun or load-bearing qualifier uninterpreted when that phrase carries semantic, boundary, or authority load. A narrowing qualifier by itself does **not** restore the head kind. Authors **MUST** restore head kind first, then qualifier load, then any comparison/escalation basis before downstream claim or effect. If a later Plain, didactic, or coarsened rendering is kept, the more precise upstream reading **MUST** remain recoverable. | Prevents ambiguity from being hidden inside ordinary-looking phrases and keeps softened prose subordinate to an explicit authoritative reading. |

### E.8:8 - Common Anti-Patterns and How to Avoid Them

These failure modes recur in drafts and in downstream application. They are predictable ways the Forces in this pattern get violated.

| Anti-pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
|-------------|---------|------------------------------|-----------------------|
| **Template cargo-culting** | Headings exist, but each section is a thin bullet list with no narrative. | Satisfies Uniformity but loses Readability and Didactic Primacy. | Use S-0 narrative flow per section; write 2-4 sentence micro-paragraphs before any list/table. |
| **Un-grounded abstractions** | Problem/Solution stay abstract; no concrete System/Episteme Tell-Show-Show. | Breaks teachability and makes misuse likely. | Fill Archetypal Grounding first; then back-propagate concrete nouns into Problem/Forces/Solution. |
| **SoTA name-dropping** | SoTA-Echoing is a list of nouns/buzzwords with no adopt/adapt/reject rationale. | Violates CC-SG.7 and CC-SG.10; readers cannot audit alignment. | For each source, state what is adopted/adapted/rejected and why (complete clauses, 2-4 sentences). |
| **Tool-bound normativity** | A vendor tool, file format, or schema is described as required to apply the pattern. Data governance implied. | Violates Guard-Rails (lexical firewall; notation independence, data governance absence); reduces portability and conceptual clarity. | Keep normative content conceptual; move tooling and data governance into Context-local Profiles. |
| **Hidden trade-offs** | Solution sounds universally good; Consequences lists only benefits. | Removes decision-support value; applicability cannot be judged. | In Consequences, include at least one trade-off and a mitigation; if none exists, explain why. |
| **Skeleton-only pattern** | The template is present, but the pattern gives only one compressed definition block and scenario labels. | Passes form while failing didactic sufficiency. | Add supporting content: local decomposition, concrete slices, reviewer cues, and neighboring-pattern or exact project-side FPF kind and reference guidance. |
| **Project-context leakage** | A reader needs architecture memos or planning notes to understand the pattern. | The monolith stops being self-sufficient. | Move the essential problem framing, worked slices, and rationale into the pattern itself; keep project reviews informative only. |
| **Generic-head underspecification** | A load-bearing phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the text never restores what kind of thing that phrase names. | The reader cannot tell what ontology the sentence is actually governing. | Restore the head kind first in pattern-local or project-local terms before any broader claim or effect or comparison is made. |
| **Qualifier-smuggled load** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the text leaves its load implicit. | The sentence sounds precise without actually stating its comparison basis, relation load, or downstream claim or effect boundary. | Unpack the qualifier into explicit load, criteria, named neighboring FPF pattern, or project-side FPF kind and reference rather than relying on the modifier alone. |
| **Mixed comparison basis** | One sentence compares or ranks publication-form, carrier, process, authority-reference, or project-record values on one basis. | The sentence becomes ontologically incoherent even if each local noun sounds plausible. | First restore head kind, then qualifier load, then rewrite the comparison through a homogeneous load, threshold, or named receiving-pattern/source-relation basis. |
| **Implicit relation shorthand** | Words like “species”, “branch”, or process metaphors do the semantic work without naming the actual governing-pattern relation. | Readers infer the wrong ontology or workflow. | State the governing-pattern relation explicitly and remove shorthand that only makes sense inside project discussions. |
| **Package-form and governing-pattern relation drift** | Words like `bundle`, `cluster`, `profile`, `overlay`, `family`, `suite`, or `kit` are swapped as if they were stylistic variants. | Readers cannot tell whether the text is naming an `authoritySourceRef` target, a navigation grouping, a review role, or a packaged set of defaults. | Pick one role word by ontology, keep the governing-pattern relation explicit, and do not vary the noun unless the ontology really changes. |
| **Reader-role leakage** | Live sections start telling the reader why the pattern was isolated, what landing form is safest, or why freeze/merge is premature. | The pattern stops teaching the user and starts narrating FPF-development decisions. | Move package-development reasoning to companion notes; keep live sections about admissible use, costs, boundaries, and exact neighboring FPF patterns or project-side FPF kinds and references for the intended user. |
| **Editorial/process-plane self-instruction leak** | The live pattern starts saying things like `this draft should ...`, `later authoring will ...`, or `that is the opening this draft must hold`. | The text stops addressing the working reader and starts narrating the current editorial or drafting process. | Move the sentence to the authored-slice carrier or handoff, or rewrite it as one user-facing claim about the governed object, boundary, or practical consequence. |
| **Role-clean but pragmatically foggy** | The pattern addresses the right reader in principle, but a cold practitioner still cannot recognise the working situation, practical payoff, governed object, first useful move, or project-level implication of the `SoTA-Echoing` early enough. | The text passes role hygiene but still fails `E.12`/`E.13`/`E.14` as working guidance. | Bring a manager-first or practitioner-first recognition cue higher, add one minimally viable worked case, state what changes in practice, expose the governed object and any minimal modeling lens in plain user-facing prose, add plain glosses for early load-bearing terms, and keep `SoTA-Echoing` tied to visible practitioner or manager implications plus nearby case linkage rather than lineage alone. |
| **Hybrid audience blob** | One main narrative tries to serve engineers, managers, auditors, architects, and researchers at once with no primary working reader or concern role. | The text becomes globally polite but locally blurry; no reader knows which concern governs the first role. | Make the primary working reader, concern, and viewpoint explicit and assign other audiences to secondary support roles, other faces, or an explicit out-of-scope note. |

### E.8:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Predictable skeleton** – readers instantly know where to find context, forces, and criteria. | Limits author freedom in macro layout; mitigated by flexibility inside the Solution subsection. |
| **Cohesive voice** – S‑principles give FPF a recognisable style, aiding memorability. | Reviewers must read for style, not only semantics; checklists ease load. |
| **Embedded pedagogy** – Tell‑Show‑Show and Hook → Close heuristics turn the spec into a self‑teaching text. | Slightly longer patterns; justified by better comprehension and fewer clarifying DRRs. |

### E.8:10 - Rationale
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

A unified template also improves retrieval: a chunk containing `A.2:<n> - Bias‑Annotation` remains self‑identifying even when parent headings are missing, and the recommended footer marker makes truncation detectable.

International and industry standards often speak in terms of *conformance criteria*. FPF uses the label **Conformance Checklist** to make adoption easier for engineers and managers.

### E.8:11 - SoTA-Echoing  *(normative; lineage and deltas to contemporary State-of-the-Art)*

**Purpose.** Make each pattern's relationship to contemporary best-known practice explicit and comparable without importing tooling or data governance. This section is prose-first and notation-independent. It does not mint an independent second rule source, but it is a load-bearing alignment section: the Solution, Conformance Checklist, Relations, worked cases, and other load-bearing sections must reflect the stance stated here or explicitly justify divergence.

**Action-guidance test.** A SoTA row is accepted only when it changes what the pattern lets a working user do, what the pattern forbids them to over-read, which neighboring FPF pattern must apply, which evidence or validation obligation remains live, or how the Solution is written. A citation that only decorates the pattern or proves that the author has read a tradition does not carry E.8.

**Minimum contents (obligations).**
1) **Evidence binding (no duplicate SoTA).** If a **SoTA Synthesis Pack** exists (G.2), this section **SHALL cite** its **ClaimSheet IDs, CorpusLedger entries, and BridgeMatrix rows** as the governing evidence source for claims and report `adopt`, `adapt`, or `reject` **consistent with those IDs**. Avoid forking an untracked SoTA narrative.
1a) **Accepted basis set, not DRR-only narrowing.** When a pattern is drafted under an accepted `DRR` and other accepted basis materials also exist by value, the `DRR` remains the decision and placement anchor, but `SoTA-Echoing`, neighboring-pattern relations, and any minimal modeling or mathematical lens **MAY** and **SHOULD** inherit non-conflicting material from that accepted basis set.
2) **Sources (post-2015, or current-practice anchor).** For **Architectural patterns**, cite at least 3 primary SoTA sources such as standards, papers, or books, with at least **two independent Traditions**. For **Definitional patterns**, cite at least 1 current source or practice anchor for the reduced issue being governed: terminology work, ambiguity or sense recovery, separation between constraint and ontology, controlled-vocabulary caution, or a comparable definitional problem. If the best source is older but still current, mark it as current practice rather than treating SoTA as not applicable.
3) **Best-known, not merely popular.** Authors **SHALL** distinguish best-known currently defensible practice from merely widespread or fashionable defaults. If the pattern adopts, adapts, or rejects a popular but less defensible practice, that divergence **MUST** be stated explicitly.
3a) **Currentness and lineage status.** Older standards, early papers, and historically important examples may be cited as lineage only when later practice has materially changed the answer. They may carry a live SoTA row only when the pattern states why the anchor is still current for the governed problem or pairs it with a current source that supplies the live practice.
3b) **Problem-domain and practice answerability.** The selected SoTA source family **MUST** answer the governed working problem and the relevant domain or practice tradition. It **MUST NOT** be selected only because it makes package placement, naming neatness, or pattern clustering easier to justify.
4) **Practice alignment.** For each cited item, state **what is adopted, adapted, or rejected** and **why** in 2 to 4 sentences.
5) **Scale admissibility.** If numeric operations are implied, bind to ComparatorSet or CG-Spec and declare partial-order stance with no hidden scalarization.
6) **Cross-Context reuse.** Any reuse across `U.BoundedContext` must expose Bridge id plus CL and, if planes differ, Phi policy ids; penalties affect only `R_eff`.
7) **Lexical hygiene.** Avoid “mapping” unless you mean an explicit Bridge, translation relation, or other named relation with loss notes.

**Writing guidance (readability).**
*Write short paragraphs, not tag lists.* For each Tradition, provide one sentence naming the practice, one sentence comparing it to the pattern's Solution, and one sentence giving adoption status with reason. Where helpful, add one **System** and one **Episteme** micro-example (Tell-Show-Show).

**Format: human-first.** A small table is allowed, but each row **MUST** be accompanied by 1 to 2 sentences as above. Vendor tokens, tool tokens, file formats, or data schemas are out of scope unless the governed problem itself makes them load-bearing.

#### E.8:11.1 - SoTA alignment for this pattern (E.8 self-echo)

| Claim (E.8 need) | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with E.8 | Adoption status |
|---|---|---|---|---|
| Pattern texts must be teachable, not just correct. | Use a stable skeleton with context, problem, forces, solution, actions, and consequences, plus illustration and checks, to keep patterns readable and actionable. | Iba (2021), “How to Write Patterns …” (PLoP 2021 PLoPourri). | Canonical Template mirrors the skeleton and adds Archetypal Grounding plus Conformance Checklist as first-class sections. | **Adopt and adapt.** Adopt the skeleton; adapt by making bias and conformance explicit sections. |
| Pattern quality needs explicit validation beyond folklore. | Critique of ad hoc validation, including the rule of three, and push toward more rigorous discovery and validation methods. | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | E.8 encodes validation as Conformance Checklist plus SoTA-Echoing with adoption status and evidence binding. | **Adopt.** Adopt auditability goals; keep the mechanism lightweight through checks and evidence binding. |
| Governance should constrain structure, not mandate tools. | Specify conformance and structure; do not prescribe processes, notations, tools, or recording media. | Joint ISO, IEC, and IEEE 42010:2022 on architecture description. | E.8 is template-centric and conformance-centric, with guardrails against tool and notation lock-in in core narrative. | **Adopt.** Direct alignment. |
| Pattern languages are networks; visuals often mislead. | Systematic surveys report low consensus on what to visualise and ambiguous or inexpressive visuals; relations need clear definition in text. | Quirino, Barcellos, Falbo (2018), survey of visual notations for software pattern languages. | E.8 requires a Relations section and keeps diagrams optional, placing primacy on textual structure and explicit links. | **Adapt.** Use the finding as rationale for text-first, relation-explicit authoring. |

### E.8:12 - Relations

* **Builds on:** E.6, E.7
* **Constrained by:** Guard‑Rails E.5.1–E.5.4 (lexical firewall, notation independence, etc.)
* **Constrains:** All patterns; the DRR template references the same section order.

### E.8:End
## E.9 - Design‑Rationale Record (DRR) Method

> **Type:** Governance / authoring pattern
> **Status:** Stable
> **Normativity:** Normative

### E.9:0 - Use this when

- one proposed normative change needs an explicit by-value account of what FPF should say, why this decision is preferred, and which neighboring patterns or selected non-pattern FPF kind-reference pairs it affects
- several patterns or selected non-pattern FPF kind-reference pairs must move together and one external decision record is needed to keep one bounded coordinated change set (one mutually dependent change set) semantically complete while enduring Core text is redistributed
- one bounded content decision question would otherwise force authors to decide the same load-bearing answer separately across several patterns or selected non-pattern FPF kind-reference pairs
- one deprecation, narrowing, or cross-pattern amendment must stay reviewable without reconstructing intent from patch history, chat memory, or scattered notes

**Not this pattern when.** Do not use `E.9` as the permanent location of normative Core law, as a campaign/process brief, or as the main vehicle for purely editorial `Δ‑0/Δ‑1` cleanup that fits the lightweight variant in `CC‑DRR.5`.

### E.9:0.1 - What goes wrong if missed

- Core text changes without one explicit rationale account, so later readers cannot recover which alternatives were rejected or which exclusions were intentional
- coordinated multi-pattern amendments drift apart because the temporary selected-answer account survives only in patches, handoffs, or reviewer memory
- future repairs overfit to local wording and silently lose Pillar, taxonomy-lens, impact-graph, practical-use, or pattern-placement discipline

### E.9:0.2 - What this buys

- one external decision record that states the bounded FPF change by value before Core text is rewritten
- one minimum kernel that keeps Problem frame, Decision, Rationale, and Consequences recoverable for later review and replay
- one temporary convergence record for coordinated changes, while keeping enduring Core text in the selected patterns and selected non-pattern FPF kind-reference pairs rather than in the DRR
- one temporary convergence record that fixes the selected answer (the chosen content answer for the bounded content decision question) before later drafting fans out across several selected patterns or selected non-pattern FPF kind-reference pairs

**First useful move.** State the bounded FPF content decision question, the selected answer, the rationale for that answer, and the selected distribution across patterns or selected non-pattern FPF kind-reference pairs before drafting or landing the Core text.

**Cheap stop.** If the live change is ordinary local wording repair, application of an already accepted pattern, or editorial cleanup that does not change FPF semantics, obligations, boundaries, names, admissible uses, or normative force, do not open a full DRR. Use the lighter governing pattern for the local repair: `E.17.AUD.LHR` for one overloaded local lexical head inside one publication unit, `E.10.SEMIO` for one semio-heavy phrase requiring local semantic recovery, `E.10` for general lexical repair, `F.18` only when a durable reusable name is being minted, and `E.8` for authoring-form correction. Leave `E.9` for bounded content decisions that need rationale by value.

**Governed object in plain terms.** The governed object here is one external decision-rationale record for one bounded FPF content decision or one bounded coordinated change set. The minimal lens is simple: the record must keep the problem frame, decision, rationale, consequences, and impact/boundary account recoverable enough that accepted content can be distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs without semantic invention.

**Primary working reader.** The first working reader is an FPF author, reviewer, or steward who must evaluate, challenge, or land one bounded content decision. Downstream pattern readers benefit from the landed Core text; they are not the primary reader of the DRR itself.

### E.9:1 - Problem frame
FPF is engineered for Pillar **P‑10 Open‑Ended Evolution**: its normative
rules must adapt as new calculi and insights arrive. But change without a
record of *why* leads to conceptual erosion and undermines auditability.
Hence FPF requires an explicit **Design‑Rationale Record (DRR)**—a
durable *conceptual record* that precedes every normative change.

### E.9:2 - Problem
Direct edits to the Core, absent a structured rationale, trigger three
systemic hazards:

1. **Lost provenance** – future authors cannot infer the reasoning behind
   a rule; intent decays.
2. **Implicit assumptions** – discarded alternatives vanish from memory,
   so debates resurface and churn repeats.
3. **Conceptual drift** – incremental tweaks slip past the Eleven Pillars
   and Principle Taxonomy lenses, blurring the framework’s foundations.

### E.9:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Rigour** | Evolve swiftly ↔ demonstrate deliberate, Pillar‑aligned decisions. |
| **Transparency vs Efficiency** | Provide a public argument trail ↔ avoid bureaucratic drag on minor edits. |
| **Clarity vs Conciseness** | Capture enough reasoning and coordinated implications ↔ prevent meta‑text from bloating the Core itself. |

### E.9:4 - Solution — the DRR as a structured argument and temporary convergence record
Any proposal to add, modify or deprecate a `NORM`, `A`, `D`, or `GOV`
rule **MUST** be accompanied by a **Design‑Rationale Record**. By default,
a conforming DRR contains at least four conceptual components (below);
these form the minimum decision kernel recoverable by any conforming DRR.
A lightweight editorial variant is permitted by CC‑DRR.5.

In this pattern, a **bounded coordinated change set** means one bounded
group of mutually dependent content decisions whose enduring FPF
expression will be distributed across several patterns or selected non-pattern FPF kind-reference pairs.
In this pattern, the **selected answer** means the current set of chosen
content decisions for that bounded content decision question: what FPF should say, which
selected patterns or selected non-pattern FPF kind-reference pairs carry it, what stays outside, and what support or
loss/recoverability regime applies.
In this pattern, **selected non-pattern FPF kind-reference pair** is a tuple-like instruction, not one new kind: when a DRR selects a non-pattern publication, view, record, or relation to carry durable content, it must name the exact FPF kind and exact reference by value, for example pattern profile, `U.View`, source map, support note, authoritySourceRef target, evidence-basis record, review-basis record, or architecture-basis record.
In this pattern, a **temporary convergence record** means one external
decision record that temporarily holds the selected answer while
the selected Core patterns and selected non-pattern FPF kind-reference pairs are still being updated.

A nontrivial DRR may therefore govern one bounded coordinated change set.
In that case the DRR is the temporary convergence record for the selected
answer until selected Core patterns and selected non-pattern FPF kind-reference pairs are updated; it is not a second
permanent Core-law section.

| Minimum-kernel component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Problem statement, triggering insight, intended FPF use-value, scenario basis, or external change. |
| **Decision** | *What will we do?* | Precise normative text, selected content distribution, explicit outside-current-decision disposition, or other substantive change law to enter the specification. |
| **Rationale** | *Why is this the right thing?* | Comparison of alternatives, Pillar check, taxonomy-lens balance, architecture/usability/SoTA grounds. |
| **Consequences** | *What follows from this choice?* | Expected benefits, trade-offs, impacted patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, and remaining validation evidence obligation. |

#### E.9:4.1 - Minimum decision-support content blocks

A conforming DRR must also make the following decision-support content blocks
recoverable. They may live inside the four kernel components or inside one
dedicated `Basis used` / decision-support block, but they are part of
substantive DRR adequacy rather than later review-only hardening.

| Decision-support content block | What must be recoverable by value | Usual location in the DRR |
|---|---|---|
| **Exact substantive basis and governing inheritance** | Exact basis sources and inherited architecture/audit basis that materially govern the decision, plus any still-live uncertainty not already closed by that basis. | Header or `Basis used`, with Problem frame/Rationale support. |
| **Purpose, utility, and scenario basis** | Intended FPF use-value, first-minute working situation, minimum scenario/anti-case basis, and compact utility/fitness reading. | Problem frame. |
| **Alternatives and current disposition map** | Material alternatives plus one current disposition for each still-live content decision question this DRR must settle: `selected now`, `rejected now`, `inherited unchanged`, or `outside current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record`. When the accepted basis or the DRR itself already names one pattern or selected non-pattern FPF kind-reference pair as part of the live distribution question, that named pattern or selected non-pattern FPF kind-reference pair is already part of the current disposition map and must not remain one conditional watch item. | Decision and Rationale. |

| **Content-distribution and outside-boundary map** | For each load-bearing selected answer: selected patterns and selected non-pattern FPF kind-reference pairs, exact content obligations on each selected pattern or selected non-pattern FPF kind-reference pair, which nearby patterns or selected non-pattern FPF kind-reference pairs stay unamended under the current decision, and any agreement across selected patterns and selected non-pattern FPF kind-reference pairs that those selected patterns and selected non-pattern FPF kind-reference pairs must preserve. Named nearby patterns or selected non-pattern FPF kind-reference pairs must be classified now, not left as tentative `most likely` / `may need` / `if later touched` watch prose. | Decision. |

| **Existing-pattern sufficiency and new-pattern necessity** | For each load-bearing selected answer, whether one already-existing pattern is sufficient, one already-existing selected non-pattern FPF kind-reference pair is sufficient, or one newly selected pattern or selected non-pattern FPF kind-reference pair is necessary, and why rejected options would misplace, overload, or falsely split the pattern or selected non-pattern FPF kind-reference pair that governs the selected answer. | Decision and Rationale. |
| **Naming, ontology, and wrong-carrier-confusion account** | Head/branch/object/move/outside-work separation, tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment, and any load-bearing `F.18` naming obligation needed to keep the selected answer truthful by value. | Problem frame, Decision, and Rationale. |
| **Reusable-support disposition when triggered** | Whether a potentially reusable selected non-pattern FPF kind-reference pair remains local, is generalized now, is rejected, or is placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Decision and Rationale. |
| **Loss and recoverability template when source-loss or scope narrowing is declared** | Preserved distinctions, dropped distinctions, admissible use, non-admissible downstream use, recoverability class, and reopen/exit rule. | Decision and Consequences. |
| **Selected carrier and neighbor-boundary account** | Why the selected patterns and selected non-pattern FPF kind-reference pairs carry the content, which tempting patterns or selected non-pattern FPF kind-reference pairs stay outside, and which neighboring pattern assignments remain authoritative. | Decision and Rationale. |
| **Convergence and overlap account when several content-decision branches touch the same carrier set** | Whether overlap is valid convergence or one reopened architecture smell, what agreement across selected patterns and selected non-pattern FPF kind-reference pairs must hold, and whether a new pattern or selected non-pattern FPF kind-reference pair is actually selected or refused now. | Decision and Consequences. |
| **Selected-answer stability boundary** | Which elements of the selected answer are fixed now for later FPF drafting, and which later elaborations may strengthen wording, examples, or support without reopening the selected answer. | Decision and Consequences. |
| **Impact, practical gains, and remaining validation evidence obligation** | Affected patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, authority or release consequences when they follow from the content decision, and the remaining validation evidence obligation that still constrains later authoring or landing. | Consequences. |
| **SoTA and competitive-positioning account when load-bearing** | Current anchors that discipline the decision, what problem-owning domain or practice they answer to, and what unresolved uncertainty would materially change the selected answer. | Problem frame, Rationale, and Consequences. |

These decision-support content blocks are not separate process paperwork. A DRR that keeps
only the four labels while leaving basis, first-minute use question, naming,
selected content distribution, pattern or selected non-pattern FPF kind-reference pair sufficiency or necessity, overlap handling, impact,
or live uncertainty implicit is structurally labeled but still
substantively immature.

Together these decision-support content blocks let the DRR act as one decision record
for one bounded coordinated change set: enough semantic closure that later
drafting distributes the selected answer into selected patterns and selected non-pattern FPF kind-reference pairs rather than
inventing it for the first time pattern by pattern.

When one bounded decision coordinates several patterns or selected non-pattern FPF kind-reference pairs, or one cluster of mutually dependent pattern edits and selected non-pattern FPF kind-reference pair edits, the DRR **MAY**
carry additional substantive sections beyond that minimum kernel. Typical substantive additions include obligations on selected patterns and selected non-pattern FPF kind-reference pairs, one explicit
new-pattern vs existing-pattern decision, one impact or non-goal map across selected patterns and selected non-pattern FPF kind-reference pairs, coverage or agreement maps across selected patterns and selected non-pattern FPF kind-reference pairs, convergence
classification, and one provisional decision-law account by value that
keeps the bounded change account semantically complete until enduring
Core text is distributed.

Such additions do not change the DRR’s kind. A DRR carrying them remains
conforming only when it stays about the FPF content decision: what FPF should
say, why, what is excluded, how selected patterns and selected non-pattern FPF kind-reference pairs are
affected, and what practical use or authoring action improves. A DRR carrying richer
convergence content **MUST NOT** become a campaign plan, process script,
baton carrier, packet checklist, staging log, or other development-process
brief.

When one selected answer could plausibly fit one already-existing pattern or selected non-pattern FPF kind-reference pair
or require one newly proposed pattern or selected non-pattern FPF kind-reference pair, the DRR must decide that
sufficiency/necessity question by value. It is not enough to list a
tentative carrier list or leave downstream drafting to discover the selected pattern or selected non-pattern FPF kind-reference pair later.

When the accepted basis or the DRR itself already names one pattern or
selected non-pattern FPF kind-reference pair as part of the live distribution question, that
pattern or selected non-pattern FPF kind-reference pair is not a neutral future watch item. The DRR
must classify it now either as one selected pattern or selected non-pattern FPF kind-reference pair
with explicit obligation, one explicit boundary neighbor kept unchanged,
one inherited-unchanged neighbor, or one outside-current-decision item
with named pattern, selected non-pattern FPF kind-reference pair, or decision record. Conditional or
time-relative pattern prose or prose for one selected non-pattern FPF kind-reference pair such as `most likely`, `may need local
hardening`, `if later touched`, `watch later`, or one equivalent
placeholder is non-conforming there because it marks one unmade current
decision rather than one explicit current disposition.


When one accepted basis exposes one potentially reusable selected non-pattern FPF kind-reference pair or neighboring support mechanism, the
DRR must not merely note that such support already exists. It must decide
whether that support is generalized now, kept local with a substantive
reason, rejected, or marked outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record.

When one selected answer involves source-loss mode, simplification, redaction,
summarization, or other declared loss, the DRR must make the admissible-use template explicit by value. Explanation alone is not enough; the decision
must say what remains preserved, what is dropped, which branch reading is admissible and which selected non-pattern FPF kind-reference pair carries it, which uses are unsupported, what recoverability class
applies, and what reopen or exit rule governs cases that exceed the
declared source-loss or scope-narrowing posture.

A nontrivial DRR is mature enough for downstream authoring only when
materially live selected-answer branch choices about the governed object, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition,
and loss/recoverability regime have already been selected, rejected,
inherited unchanged, or placed outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record. If those choices are still missing, the DRR is still basis work
rather than one accepted design-rationale record.

The DRR lives **outside** the normative Core. An accepted DRR **SHALL** be
landed by applying its Decision account and any stabilized enduring
content to the relevant pattern or selected non-pattern Core kind-reference pair as explicit
normative or informative text (the change is "in the Core"; the DRR is
not). A richer DRR **MAY** remain the temporary convergence record while
redistribution into selected Core patterns and selected non-pattern FPF kind-reference pairs is still incomplete, but it
**SHALL NOT** remain the permanent sole semantic carrier once landed Core text
exists.

Authors drafting from an accepted DRR **MAY** elaborate examples,
SoTA‑Echoing, recognition surfaces, local wording inside the selected patterns and selected non-pattern FPF kind-reference pairs, and neighboring fit. They **SHALL NOT** silently revise the selected answer, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition, or
declared loss/recoverability regime. Any such revision **SHALL** be handled
through one successor DRR or other named successor decision record.

To preserve **P‑2 Didactic Primacy** without duplicating meta‑text,
authors landing an accepted DRR **SHOULD** distill stable and reusable
parts of its *Rationale*, *Consequences*, and other valid convergence
sections into the appropriate **informative** sections of the affected
pattern(s) (Rationale, Consequences, SoTA‑Echoing, Archetypal Grounding;
per the Pattern Template, E.8). The full DRR remains external as
provenance.

A substantive DRR is one current content decision object. It may carry
selected content obligations only when they are part of the
Decision or Consequences. It **MUST NOT** carry next-gate posture,
handoff/packet state, process-order state, monolith status, future campaign
planning, or one hidden promise that the same current content decision question will be
decided later inside the same decision object. Any undecided remainder must
be marked outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record.

#### E.9:4.1a - Process-source method admission into FPF

When a `DRR` imports stable method from process-source document-carried method description into `FPF`, it must decide the admission by value rather than treating process prose as a second canon.

The `DRR` names:

- the exact process-source passage or accepted process-source basis being considered;
- the reusable FPF method recovered from that passage;
- the current FPF pattern, section, or accepted `DRR` that already carries the method, if any;
- the remaining delta that current FPF does not yet carry;
- the receiving FPF pattern selected to carry that delta;
- process-control material excluded from FPF pattern prose, such as role dispatch, seam state, helper behavior, Git recovery, packet transport, review transport, chat cadence, and mutable release posture;
- the source-use result for that passage or basis: exact quote, narrowed scope, instantiated case, decision-bearing use, draft-guidance source, example-only use, or retired source use;
- any meaning loss or addition created by that source-use result: changed scope, relation, evidence basis, admissible use, non-admissible use, reader move, or recoverability condition;
- the first improved FPF use that the admitted method gives to an author, reviewer, or downstream FPF user;
- the current disposition: selected now, inherited sufficient, rejected now, or outside the current decision with the named receiving pattern, accepted `DRR`, or accepted basis named by value.


Reusable process-source method is not limited to semio wording or pattern-authoring language. It may enter FPF only when it is separable from local process mechanics, improves FPF use, and has one exact receiving pattern. After the method lands in FPF, process documents should cite the receiving FPF pattern instead of keeping a parallel long-form rule.
### E.9:5 - Archetypal Grounding (System / Episteme)

| Holon flavour | DRR analogue | Minimum kernel illustrated |
|---------------|--------------|-----------------------------|
| **`U.System`** (physical) | Engineering Change Order for pump motor upgrade. | Context: inefficiency and plant-use problem; Decision: switch to brushless DC and update the selected control/maintenance patterns or selected non-pattern FPF kind-reference pairs; Rationale: energy gain vs cost and authority fit; Consequences: new control schema, supplier change, validation evidence obligation. |
| **`U.Episteme`** (knowledge) | Foundational theory revision paper. | Context: conflicting data and explanatory problem; Decision: introduce new axiom and distribute its consequences into the selected theory/teaching patterns or selected non-pattern FPF kind-reference pairs; Rationale: explains legacy & new data, Pillar alignment, alternative rejection; Consequences: fresh predictions, update to curricula, downstream review obligation. |

### E.9:6 - Bias-Annotation

| Lens | Bias risk in DRR use | Mitigation in this pattern |
|---|---|---|
| **Gov** | The DRR can become a bureaucratic approval ritual rather than a decision-rationale record. | Keep `CC-DRR.5` for lightweight editorial changes and require richer DRRs only when the content decision is semantically load-bearing. |
| **Arch** | A rich DRR can become a shadow specification that competes with the selected Core patterns and selected non-pattern FPF kind-reference pairs. | Treat the DRR as temporary convergence support; enduring content is distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs. |
| **Onto/Epist** | Authors can mix content decisions, evidence basis, process state, and provenance into one ambiguous object. | Require exact substantive basis and selected-answer boundaries while excluding process-order state, baton, packet, and mutable status posture from the DRR. |
| **Prag** | The method adds work before editing Core text. | Allow pointer-based DRRs and require only the selected non-pattern FPF kind-reference pairs materially needed for the selected decision. |
| **Did** | Rationale can become too internal for later authors to use. | Distill stable rationale, consequences, anti-cases, and SoTA implications into informative pattern sections when the Core text is updated. |

Scope: this bias annotation is universal for FPF semantic changes governed by `E.9`. It does not turn project-management state, helper state, or review logistics into DRR content.
### E.9:7 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑DRR.1** | Any Δ‑2/Δ‑3 semantic change set against a `NORM`, `A`, `D`, or `GOV` pattern **SHALL** be backed by an accepted DRR containing at least Problem‑frame (Context), Decision, Rationale, and Consequences. | Prevents undocumented semantic edits while setting a minimum kernel rather than an artificial ceiling. |
| **CC‑DRR.1a** | A DRR whose proposed change is expressed as a new or revised pattern written in the standard template (E.8) **MAY** satisfy that minimum kernel by **pointing to** the corresponding pattern sections rather than duplicating prose. | Avoids “double writing” while keeping the argument recoverable. |
| **CC‑DRR.1b (rich convergence content is permitted)** | A DRR that coordinates several patterns or selected non-pattern FPF kind-reference pairs, or mutually dependent pattern and selected non-pattern FPF kind-reference pair changes, **MAY** include additional substantive sections beyond the minimum kernel—for example obligations on selected patterns or selected non-pattern FPF kind-reference pairs, explicit new-pattern vs existing-pattern decisions, boundary/non-goal maps, coverage or agreement maps across selected patterns and selected non-pattern FPF kind-reference pairs, convergence classification, or one provisional decision-law account by value—provided that the DRR stays about the FPF content decision and **MUST NOT** become process management. | Allows one semantically sufficient convergence record for coordinated changes without forcing mid-distribution invention or extra shadow documents. |
| **CC‑DRR.1c (exact basis is recoverable)** | A conforming DRR **MUST** make its exact substantive basis and governing inheritance recoverable by value, either in one dedicated `Basis used` section or one equivalent header/support block. Routing, status, and provenance records do not count unless their substantive content still governs the decision by value. | Prevents anti-telephone drift and keeps the decision inspectable against its real basis. |
| **CC‑DRR.1d (problem-frame adequacy)** | The Problem frame **MUST** make the intended FPF use-value, first-minute working situation, minimum scenario/anti-case basis, compact utility/fitness reading, and any load-bearing current SoTA / competitive-positioning basis or exact inherited-basis justification recoverable by value. | Prevents a DRR from being formally labeled but pragmatically under-specified. |
| **CC‑DRR.1e (current disposition map and content obligations)** | The Decision **MUST** name the selected patterns and selected non-pattern FPF kind-reference pairs and the content obligations each selected pattern or selected non-pattern FPF kind-reference pair must carry by value. For every load-bearing selected answer and for every still-live content decision question explicitly assigned to this DRR by accepted basis, the Decision **MUST** record one current disposition now: `selected now`, `rejected now`, `inherited unchanged`, or `outside current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record`. When one pattern or selected non-pattern FPF kind-reference pair is already named as part of that live distribution question, the Decision **MUST NOT** leave it in conditional or time-relative pattern prose or prose for one selected non-pattern FPF kind-reference pair such as `most likely`, `may need`, or `if later touched`. | Stops hidden deferral, including conditional/time-relative carrier-list wording, and prevents tentative carrier-list prose from replacing real content decisions. |

| **CC‑DRR.1f (reusable-support disposition when triggered)** | When accepted basis exposes a potentially reusable selected non-pattern FPF kind-reference pair or neighboring support mechanism, the DRR **MUST** decide whether it is generalized now, kept local with reason, rejected, or placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Prevents unexamined inheritance of local support publications, records, views, or relations. |
| **CC‑DRR.1g (source-loss and recoverability template when triggered)** | If the decision declares a source-loss mode, simplification, redaction, summarization, or other source-to-rendering loss, the DRR **MUST** make explicit the preserved distinctions, dropped distinctions, admissible uses, non-admissible downstream uses, recoverability class, and reopen or exit rule. | Prevents rhetorical smoothing from masquerading as stable content. |
| **CC‑DRR.1h (naming and ontology adequacy)** | A conforming DRR **MUST** make the selected head/branch/object/move/outside-work separation recoverable by value and **MUST** expose any tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment or load-bearing `F.18` naming obligation that materially affects the decision. | Prevents semantically important naming and typing choices from being rediscovered later during pattern drafting. |
| **CC‑DRR.1i (existing-pattern sufficiency or new-pattern necessity is explicit)** | When a load-bearing selected answer could plausibly live in one already-existing pattern, one already-existing selected non-pattern FPF kind-reference pair, or one newly proposed pattern or selected non-pattern FPF kind-reference pair, the DRR **MUST** make that sufficiency/necessity judgement by value and **MUST** explain why rejected options would misplace, overload, or falsely split the pattern or selected non-pattern FPF kind-reference pair that governs the selected answer. | Prevents carrier selection from being rediscovered during downstream drafting. |
| **CC‑DRR.1j (selected-answer stability boundary is explicit)** | The Decision or Consequences **MUST** make clear which elements of the selected answer are fixed now for later FPF drafting and which later elaborations may strengthen wording, examples, or support without reopening the selected answer. | Prevents later drafting from silently widening or re-deciding the accepted answer. |
| **CC‑DRR.1k (source-use result is explicit).** | When a DRR imports a source-borne method, architecture claim, accepted basis, or other reusable source passage, it **MUST** state how the source is used in the selected answer: exact quote, narrowed scope, instantiated case, decision-bearing use, draft-guidance source, example-only use, or retired source use. It **MUST** also state any meaning loss or addition in scope, relation, evidence basis, admissible use, non-admissible use, reader move, or recoverability condition. | Blocks free paraphrase and makes source movement reviewable without turning source documents into a second canon. |

| **CC‑DRR.2** | A conforming DRR **MUST** include a rationale account that compares the materially live alternatives and assesses the selected proposal against **all Eleven Pillars** and the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Keeps evolution aligned, comparative, and cross‑disciplinary. |
| **CC‑DRR.3** | The DRR **SHALL** list every pattern, selected non-pattern FPF kind-reference pair, or neighboring pattern or selected non-pattern FPF kind-reference pair that it supersedes, amends, excludes from the current decision, assigns to a neighboring pattern or selected non-pattern FPF kind-reference pair, or risks impacting, together with any agreement across selected patterns and selected non-pattern FPF kind-reference pairs the selected patterns and selected non-pattern FPF kind-reference pairs must preserve. It **MUST** also make clear why the selected patterns and selected non-pattern FPF kind-reference pairs carry the content, which tempting patterns or selected non-pattern FPF kind-reference pairs stay outside, and, when several content-decision branches touch the same carrier set, whether that overlap is valid convergence or one reopened architecture smell. | Maintains an explicit impact/boundary graph for coordinated changes. |
| **CC‑DRR.3a (practical and validation consequences are explicit)** | The Consequences account **MUST** expose the practical change in use, practical gains/costs, affected patterns and selected non-pattern FPF kind-reference pairs, and any remaining content-scope validation evidence obligation or authority/release consequence that still constrains the selected decision by value. | Prevents consequences from collapsing into generic optimism or process-order prose. |
| **CC‑DRR.3b (SoTA shapes the decision when load-bearing)** | When SoTA or competitive positioning is load-bearing, the DRR **MUST** make the current SoTA basis and any uncertainty that would materially change the decision recoverable by value. A literature overview that does not shape the selected answer, boundary, or validation evidence obligation is non-conforming. | Keeps SoTA from becoming decorative appendix material. |
| **CC‑DRR.4** | An accepted DRR **SHALL** have its Decision account landed in the Core as the normative change. When that DRR temporarily carries richer convergence content, authors landing it **SHOULD** distribute any part that stabilizes into enduring FPF content into the relevant Core patterns and selected non-pattern FPF kind-reference pairs. Authors **MAY** distill other DRR sections into **informative** pattern sections (Rationale/Consequences/SoTA‑Echoing/Grounding), but they **SHALL NOT** introduce new normative constraints except via explicit `NORM`/`A`/`D`/`GOV` text. | Preserves Core authority while allowing a richer temporary convergence record. |
| **CC‑DRR.4a (separate-law content proliferation is blocked)** | If the DRR needs compact law/check content, it **SHOULD** keep that content as one decision-law section or as obligations on selected existing amendment targets. It **MUST NOT** mint a separate `law sheet`, `profile`, selected non-pattern FPF kind-reference pair, or checklist unless that separate selected non-pattern FPF kind-reference pair is selected by value and shown not to duplicate the DRR or the selected amendment targets. | Prevents unnecessary separate-support proliferation and shadow-law duplication. |
| **CC‑DRR.4b (current decision object remains singular)** | A conforming DRR **MUST** remain one current content decision object. It **MUST NOT** carry process-order/gate/handoff/process posture, mutable status, or hidden same-decision future-planning language; any undecided remainder **MUST** be marked outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Keeps the DRR ontologically about the FPF decision rather than about the development container. |
| **CC‑DRR.4c (downstream authoring stays inside the accepted decision)** | Authors drafting from an accepted DRR **MAY** elaborate examples, SoTA‑Echoing, recognition surfaces, local wording inside the selected patterns and selected non-pattern FPF kind-reference pairs, and neighboring fit, but they **SHALL NOT** silently revise the selected answer, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition, or declared loss/recoverability regime. Any such revision **SHALL** be handled through one successor DRR or other named successor decision record. | Keeps later pattern drafting from re-deciding bounded content by drift. |
| **CC‑DRR.4d (major decision gaps are not left to drafting-time invention)** | A conforming DRR **MUST NOT** leave materially live selected-answer branch choices about the governed object, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition, or loss/recoverability regime to be discovered case-by-case during later pattern drafting or drafting for one selected non-pattern FPF kind-reference pair. Those choices **MUST** already be selected, rejected, inherited unchanged, or placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Ensures the DRR actually coordinates one bounded change set rather than serving as a thin preface to later rediscovery. |
| **CC‑DRR.5** | A DRR for minor, non‑substantive edits (Δ‑0/Δ‑1; e.g., typos, wording clarity, didactic rearrangements) **MAY** use a lightweight variant containing Problem‑frame (Context) + Decision only (“no semantic change”), provided it does not alter semantics. | Avoids bureaucratic drag on editorial work. |
| **CC‑DRR.6 (evidence boundary)** | For Δ‑2/Δ‑3 lexical or authoring-sensitive changes, the DRR **SHALL** state the content-scope evidence or validation evidence obligation that bears on the decision, and it **MAY** summarize already-available decisive evidence by value when that evidence materially shapes the chosen content. The DRR **SHALL NOT** need a LAT id, run-manifest id, gate id, packet id, or other authoring-evidence citation in order to count as complete; those remain in the relevant evidence or authoring record. If later LAT or refresh evidence motivates reopening or revising the decision, that later evidence belongs in a successor DRR or other named successor decision record rather than being retrofitted into the accepted DRR. | Keeps the DRR a design-rationale record while preserving re-runnable evidence in its own evidence or authoring record. |

### E.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | Why it fails | Repair |
|---|---|---|---|
| **Process brief disguised as DRR** | The record explains baton movement, packet posture, review timing, or current campaign state. | It describes development process rather than the FPF content decision. | Remove mutable process state and keep only the substantive basis, selected answer, alternatives, and consequences. |
| **Shadow specification** | The DRR becomes the only place where stable semantics, examples, or support rules live after the Core has moved. | Later FPF readers cannot use the decision because it never became pattern content. | Distribute enduring content into the selected patterns and selected non-pattern FPF kind-reference pairs; leave the DRR as provenance. |
| **Four-label shell** | The record has Problem frame, Decision, Rationale, and Consequences headings, but no basis, use-value, alternatives, content distribution, or impact account by value. | The minimum kernel is labeled but not substantively recoverable. | Fill the decision-support content blocks that are live for the decision, or use the lightweight variant only for true `Delta-0` / `Delta-1` edits. |
| **Tentative carrier list** | The DRR says a pattern may need work later, is most likely affected, or should be watched if touched. | A named live distribution question is postponed while pretending to be decided. | Classify each named pattern or selected non-pattern FPF kind-reference pair now: selected, rejected, inherited unchanged, or outside the current decision with a named record. |
| **Loss without use/reopen rule** | The decision summarizes, redacts, simplifies, or otherwise declares a source-loss mode but does not state admissible use, non-admissible downstream use, recoverability, and reopen conditions. | A representation with undeclared source loss can be used as if it were the full source. | Add the source-loss and recoverability template: preserved distinctions, dropped distinctions, admissible uses, non-admissible uses, recoverability class, and reopen or exit rule. |
| **Free paraphrase import** | The DRR restates a source-borne method, architecture claim, accepted basis, or reusable source passage in smoother prose but does not say whether it quoted, narrowed, instantiated, used as a decision basis, turned into draft guidance, kept example-only, or retired the source use. | The paraphrase can widen, weaken, or redirect the source while appearing to preserve it. | State the source-use result and loss and addition account, or keep the passage as an exact quote or example-only support. |


| **Decorative SoTA appendix** | Sources are listed after the fact but do not shape the selected answer, boundary, or validation evidence obligation. | The record looks researched while the decision remains unchallenged by current practice. | State what each load-bearing source makes the DRR adopt, adapt, or reject, and which uncertainty would materially change the answer. |
### E.9:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Complete audit trail** – every semantic normative change carries a structured “why”. | Adds deliberate friction; mitigated by CC‑DRR.5 (Δ‑0/Δ‑1 lightweight) and CC‑DRR.1a (pointer‑based DRRs). |
| **Higher decision quality** – Pillar, alternatives, scenario, and utility checks surface hidden conflicts early. | Authors must do more real content work up front; the gain is less downstream reinvention and less hidden deferral. |
| **Institutional memory** – prevents re‑litigation of rejected alternatives. | DRR archive grows; index stored in a non‑normative annex. |
| **Executable downstream authoring** – selected patterns and selected non-pattern FPF kind-reference pairs, outside-boundary, reusable-support decisions, selected-answer stability, and remaining validation evidence obligation are explicit enough for later drafting/landing without semantic invention. | Richer DRRs need discipline to avoid becoming shadow specs or process briefs; mitigated by CC‑DRR.1b, CC‑DRR.4a, CC‑DRR.4b, CC‑DRR.4c, and CC‑DRR.4d. |

### E.9:10 - Rationale
FPF evolves by **explicit, reviewable deltas** rather than silent edits.
The DRR is the *minimum structured argument*—and, when several patterns or selected non-pattern FPF kind-reference pairs must move together, an allowed temporary convergence record that keeps **P‑10 Open‑Ended Evolution** compatible with **P‑1
Cognitive Elegance** and **P‑2 Didactic Primacy**.

E.9 sets a **floor, not a ceiling**: every conforming DRR must make
Problem‑frame / Decision / Rationale / Consequences recoverable, but it
may carry richer substantive coordination content when that prevents
shadow documents or semantic invention during distribution into Core patterns and selected non-pattern FPF kind-reference pairs. The same floor also requires the decision-support content that
later authoring and review otherwise reconstruct manually: exact basis,
use-value, first-minute working situation, scenario basis, alternatives,
current disposition map, naming/ontology obligation, selected content distribution,
existing-pattern sufficiency/new-pattern necessity, overlap classification,
selected-answer stability, impact/boundary graph, practical payoff, and
any still-live uncertainty that materially shapes the decision.

Pointer-based DRRs (CC‑DRR.1a) prevent duplicated prose, and distribution
into Core patterns and selected non-pattern FPF kind-reference pairs (CC‑DRR.4) keeps the specification itself learnable
without turning the DRR into a permanent shadow canon. Process-law ordering,
gate, and handoff records stay outside because they are not part of the
content answer that FPF is selecting.

### E.9:11 - SoTA-Echoing

`E.9` aligns with contemporary architecture-decision and rationale-capture practice, but its contribution is not the existence of a decision record. ADR practice already carries compact context, decision, and consequence records. FPF uses the DRR as a decision-rationale record for one bounded FPF content decision, with enough by-value rationale to distribute durable content into selected patterns and selected non-pattern FPF kind-reference pairs.

| Practice source family | Local FPF invariant and practical implication | Popular shortcut rejected |
|---|---|---|
| **Architecture-description standards such as joint ISO, IEC, and IEEE 42010:2022** | Architecture work must make concerns, viewpoints, decisions, and rationale inspectable. A DRR adapts this to FPF content deltas by exposing the concerns and alternatives that shape the FPF change, not only the edited text. | Reject treating a patch or edited wording as self-explanatory architecture rationale. |
| **Markdown ADR practice, including post-2015 lightweight ADR and MADR-style templates** | Context, decision, and consequence records are useful when the live change is local. A semantic FPF amendment needs enough by-value support for later pattern drafting without reinvention. | Reject treating a generic ADR template as sufficient when a multi-pattern FPF change needs Pillar, lens, naming, SoTA, distribution, or loss and recoverability support. |
| **Continuous and evolutionary architecture decision-record practice** | Decision records are revisitable support for evolving systems. FPF keeps mutable process state out of the DRR and handles reopened content with a successor decision record. | Reject turning the DRR into a live status log, gate diary, or permanent shadow law. |
| **Research and design-rationale traditions around alternatives and trade-off capture** | Rejected alternatives and trade-offs must remain recoverable enough that future authors do not re-litigate or silently reverse the selected answer. FPF adapts this through the Eleven Pillars and Principle-Taxonomy lenses. | Reject recording only the selected answer while leaving why-this-not-that implicit. |

The practical gain is content-selection quality under semantic load: the DRR decides the selected answer, alternatives, losses, boundary, and distribution target before pattern drafting begins. Any durable rule, example, or support obligation that remains useful after acceptance belongs in the selected FPF pattern or selected non-pattern FPF kind-reference pair, not in the DRR as a permanent shadow canon.

### E.9:12 - Relations

* **Instantiates:** P‑10 Open‑Ended Evolution, P‑2 Didactic Primacy
* **Template governed by:** `pat:authoring/pattern‑template` (E.8)
* **Interacts with:** `pat:guard/bias‑audit` (E.5.4) via lens check
* **Complemented by:** `pat:authoring/code‑of‑conduct` (E.12) – etiquette for DRR debate

### E.9:End

## E.10 - Unified Lexical Rules for FPF (LEX‑BUNDLE)
*Definitional pattern; normative for all FPF pattern text and for any Context that claims FPF conformance.*

**Status & placement.** Part E.10 (“Lexical Discipline & Stratification”); complements **E.10.D1 (D.CTX)**, **E.10.D2 (I/D/S)**, and the **DesignRunTag / CtxState boundary discipline** (**A.15**; **E.18**), and is referenced by F‑cluster naming practices (F.4–F.8). This bundle consolidates all lexical constraints in one place so authors can cite **“LEX‑BUNDLE”** instead of listing rules scattered across documents.

**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.5 Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Unidirectional Dependency); F.5 **Naming Discipline for U.Types & Roles**.
**Coordinates with.** A.2/A.15 (Role–Method–Work alignment), A.10 (Evidence Graph Referring), B.1/B.3 (Γ‑algebras & assurance), F‑cluster (context of meaning; Bridges).

### E.10:0 - Use this when

Use `E.10` when a word, head, or local phrase in conformant FPF text is starting to hide what kind it names, which register it belongs to, which context of meaning governs it, or which relation or action claim it carries.

**First useful move.** Restore the head kind and register of the local wording, then either keep the lighter ordinary wording with its exact FPF anchor or move to the specific neighboring pattern that governs the live object: `E.10.SEMIO` for semio-heavy episteme/publication wording, `F.18` for durable reusable names, `A.6.P` for relation precision, and the exact domain pattern for work, evidence, gate, decision, or project-side use. `E.10` governs the lexical repair; the recovered object or project-side effect is governed by its own exact FPF pattern.

**Cheap stop.** If one local lexical repair restores kind, relation, and admissible use without changing the normative meaning of FPF, stop with the repaired wording; do not open a Name Card, DRR, review profile, or larger semantic recovery note by habit.




### E.10:1 - Problem context

**Intent.** Provide one **normative** rule-set that makes FPF language **unambiguous, composable across contexts, and teachable** by design. Authors, reviewers, and tooling can point to **LEX-BUNDLE** as the governing lexical pattern for:

* **Vertical stratification** (Kernel ↔ Extensions ↔ Context ↔ Instance);
* **Twin registers** (Tech/Plain) with safe synonyms;
* **Naming morphology** (allowed suffixes & style) for the kernel’s core objects;
* **Minimal Generality** tests (names are neither parochial nor vacuous);
* **Canonical rewrites** for overloaded words (e.g., *process*, *function*, *service*);
* **Conformance checks** and minimal examples.

**Scope.** Applies to:
(a) **Core** (Parts A–G), (b) **Extensions patterns specs** (CAL/LOG/CHR), (c) **Context glossaries** that claim FPF conformity, and (d) **Diagrams/prose** in normative text. It **does not** constrain Tooling or Pedagogy wording other than where they quote Core semantics.


### E.10.2 - Problem

1. **Polysemy drift.** *Process, function, service, agent, activity* slide between structure, recipe, execution, and promise.
2. **Cross‑context collision.** A label (e.g., *Owner*) is assumed “global” though meanings differ per `U.BoundedContext`.
3. **Name bloat vs. parochialism.** Either hyper‑specific domain names leak into core types, or vague umbrella names obscure invariants.
4. **I/D/S collapse.** Authors mix **intension** (the thing), **description** (how we describe it), and **specification** (testable criteria).
5. **Register soup.** Tech terms bleed into Plain pedagogy and vice‑versa, inviting category errors.


### E.10:3 - Forces

| Force                          | Tension to resolve                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Universality vs. local fit** | Kernel must stay universal while allowing domain nuance in a Context of meaning.              |
| **Brevity vs. clarity**        | Short names help, but only if morphology signals the right kernel slot.                    |
| **Stability vs. evolution**    | Names should survive refactors; yet we must accommodate new roles/types without explosion. |
| **Pedagogy vs. precision**     | Plain words aid learners; Tech labels anchor formal checks.                                |


### E.10:4 - Solution — the **LEX‑BUNDLE** rule‑set (overview)

**LEX‑BUNDLE** aka **ULR (Unified Lexical Rules)** is a compact set of **register, naming, and rewrite** rules with conformance checks.

1. **Vertical Stratification** (E.10 -> four strata);
2. **Twin‑Register Discipline** (Tech/Plain pairs);
3. **Minimal Generality (MG)** principle + tests;
4. **Morphology & Style** (suffixes, casing, reserved prefixes);
5. **Canonical Rewrites** for overloaded words (L‑rules);
6. **Conformance Checklist (CC‑LEX)** and **Regression Stubs (RSCR‑LEX)**.

Below are the **normative clauses**

### E.10:5 - Vertical Stratification (four strata; no cross-bleed)

> **Rule V‑0 (Strata).** Every lexical item in a conformant text belongs to exactly one **stratum**:

1. **Kernel** — `U.*` types, kernel relations, invariants (e.g., `U.Holon`, `U.Role`, `U.Method`, `U.Work`, `U.PromiseContent`).
2. **Extension patterns** — CAL/LOG/CHR exports (e.g., **Sys‑CAL**, **KD‑CAL**, **Agency‑CHR**) that **extend** but do not override Kernel.
3. **Context** — a **`U.BoundedContext`** with its **Glossary, Invariants, Roles**, and **Bridges** (local Context of meaning).
4. **Instance** — concrete identifiers (holders, role assignments, works, carriers).

**V‑1 (Unidirectional meaning).** Meaning **flows downward** only: Kernel → Extention patterns → Context → Instance. No stratum may redefine a higher stratum’s term; it may only **specialise** or **bridge** it.

**V‑2 (Strata vs authoring stances).** The four lexical strata above constrain **tokens**. They are independent of a claim-bearing unit's **stance** (its `CtxState` pins such as `DesignRunTag`, `ReferencePlane`, and `Locus`). Strata answer “what words mean here”; stance answers “where this claim lives in the flow” and which evidence‑lane expectations apply.

**V‑3 (Citation style).** When a Context term is used, its **Context** must be visible at first mention (e.g., `OwnerRole:ITIL_2020`). If an author needs Cross‑context reuse, they **MUST** cite a **Bridge** with a stated **Congruence Level (CL)** (see F.9).

**V‑4 (Firewall).** Tooling/Pedagogy idioms shall not leak into Kernel prose (DevOps Lexical Firewall). CI/CD jargon, file formats, or API names **MUST NOT** appear in Core definitions. (Pedagogy may use them **as examples** only, in the **Plain** register, with Tech anchors present.)

### E.10:6 - Ontology Guards

#### E.10:6.1 - Tech register ontology guards

> **Purpose.** This section stabilises the Tech register of the kernel lexicon by enforcing head‑anchored naming, explicit kind naming, I/D/S morphology, disciplined treatment of **Role / Holder**, and Domain usage consistent with **D.CTX** and **UTS**. It aligns with **F.4 Role Description (RCS/RSG)**, **F.11 Method Quartet Harmonisation**, and **F.17 UTS**. **Scope:** Guidance is **register‑agnostic** and applies to the whole FPF; examples are illustrative and MUST pass Minimal Generality & Domain Anchoring (MG-DA) and other rules of lexical governance pattern E*. This guidance applies to kernel and non‑kernel components (including Part G and patterns in Part C) and SHOULD be reused across extensions.
>
**Onto1 — Head‑anchoring**  *(use Kernel heads + pass LEX.TokenClass / I/D/S gates)*
* **Rule:** The **head noun of a term MUST explicitly signal the kind** (`System`, `Holon`, `Role`, `Work`, `Episteme`, `Tradition`, `Lineage`, `Characteristic`, `Method`, `Profile`, `Description`, `Spec`, `Flow`, `Card`, `Pack`, `Dashboard`, …).
* **Figurative heads** with obvious overload (“Tradition”, “family”, “process”, “function”) are **forbidden in the kernel**. Use **plain twins** only with a 1:1 Tech mapping and declare **`LEX.TokenClass`** for the Tech token. They **MAY** appear **only in the Plain register** as 1:1 twin‑mappings to a Tech token, but **MUST NOT** appear in the Tech register. Plain language should minimise lexical error from overloaded terms; use plain‑twin lexical guards.
  * **Do:** `IncidentDashboard`, `MethodSpec`, `TraditionProfile`, `FlowDescription`.
  * **Don’t:** `IncidentBoard`, `TDD Tradition`, `Production Process` (kernel), `Service Function` (kernel).

 **Onto2 — I/D/S in term morphology (Intension/Description/Specification morphology)**  *(ref. E.10.D2)*
* **Rule:** Any **intensional** object is a bare head: `Method`, `Tradition`, `Characteristic`. Any **description** appends **`…Description`**: `MethodDescription`, `TraditionDescription`. Any **testable specification** appends **`…Spec`** and presupposes acceptance criteria and harnesses (normative in **E.10.D2**). E.g., *Algorithm* is a species of `MethodDescription` for a computer (a system in the role of information transformer); **If** expressed in a formal language **and** bundled with acceptance tests, it is **`MethodSpec`** (per **F.11**). **If** expressed as pseudo‑code, it is **`MethodDescription`**.
* **Extension:** Apply the same pattern to non‑method objects where appropriate: `FlowDescription`/`FlowSpec`, `SystemDescription`/`SystemSpec`.
* **Do:** `SamplingMethod` - `SamplingMethodDescription` - `SamplingMethodSpec`.
* **Don’t:** `SamplingAlgorithm` (when it is just prose), `SamplingProcessSpec` (head not signalling kind).

**Onto3 — Roles, Holders, and Carriers (holonic)**  *(ref. F.4 / F.5)*
* **Rule:** The playable intention is named **`…Role`** and described through **F.4 Role Description** (RCS/RSG), e.g., `SafetyOfficerRole`, `ReviewerRole`. The party **assuming a role** is the **Holder**. Use the **`Holder#Role:Context`** pattern to type the assumption (where `Context` is a `U.BoundedContext`), e.g., `Team‑Alpha (U.Holon) is Holder#SafetyOfficerRole:Plant‑Ops`. **Carrier** is **reserved for a system that bears a symbol of episteme** (`U.Episteme`, `Tradition`, `Lineage`, `Profile`, repertoire) **independent of any concrete role assumption**, e.g., `LeanTraditionCarrier`, `CalibrationLineageCarrier`. Avoid **`Artefact`** as a head in the kernel: it is ambiguous between a Carrier (e.g., document), a system “made by” some transformer, or an episteme abstracted from its carrier.
* **Register note:** Job titles (`Reviewer`, `Owner`, `Lead`) belong in the **Plain** register and MUST twin‑map to explicit Tech `…Role` tokens.
* **Why:** This resolves the inconsistent “role carrier vs role holder” usage: **use “Holder” for holonic role assumption**, keep **“Carrier”** for the *system that bears a symbol of episteme*.
* **Migration note.** Legacy `…CarrierRole` **MUST be rewritten** to `Holder#…Role:Context`. Use SCR‑LEX to enforce the rewrite.
* **Do:** `ReviewerRole` (or `AssessorRole`), `Holder#ReviewerRole:Journal‑Issue‑42` (or `Holder#AssessorRole:Procurement‑Lot‑42`); `LeanTraditionCarrier (U.Holon)`, independent of any particular role.
**Don’t:** `Reviewer` (as a kernel type), `ReviewerCarrier` (to mean a role holder), `SystemReviewer` (role collapsed into a type).

**Onto4 — Domain only as a catalog mark**  *(ref. E.10.D1 D.CTX; publish stitching on UTS)*
* **Rule:** `Domain` is **not a kernel kind** and carries **no semantics, inheritance, or reasoning rights**. It is a **catalog mark** that groups several `U.BoundedContext` entries.
* **Required stitching (see D.CTX & UTS).** Any use of `Domain` **MUST** present: 1. the enumerated list of `ContextId` in **D.CTX**, and 2. the corresponding **UTS strings** (F.17) with twin labels.
* **“Discipline ≠ Domain.”** _Domain_ labels are **catalog‑only (D.CTX + UTS)**; **Discipline** is a **CG‑Spec‑governed holon** (`U.Discipline`). Cross‑use requires **Bridge (F.9) + CL**; **LexicalCheck** MUST fail texts that equate Domain with Discipline.
* **Governance.** **No “Domain … governance”.** Rules of comparability/aggregation belong to **Discipline/CG‑Spec** (ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ‑fold, CL‑routing), *not* to `Domain`. Prefer `DomainFamily` + stitching over inventing new “Domain” types.
* **Do:** `DomainBundle: ClinicalSafety → {ContextId: AdverseEvents, DeviceLabelling, …} + UTS twins`.
* **Don’t:** `ClinicalSafetyDomain` as a type with inheritance; `Domain Governance` sections in Tech.

**Onto5 — Always state what the term names**
* **Rule.** The definition or first line of a gloss **MUST state the FPF kind named by the term**: a `U.Holon`, `U.System`, `U.Episteme`, `Tradition`, `Lineage`, `Profile`, `Role`, `U.Work` execution, `Characteristic`, or `Carrier`.
* **Do:** “**Kind named:** `ReviewerRole` — a role intention playable by a holon within an editorial context.”
* **Don’t:** “Reviewer — a person who …” (blurs the kind named).

**Onto6 — Bans and canonical rewrites**  *(mirror E.10 § 9 L‑rules; do not duplicate tables)*
* `process / function / activity` → **`Work` / `MethodDescription` / `Flow`** (context‑dependent).
* `Tradition` → **`Tradition`** (Tech); leave “Tradition” only as a Plain twin with an adjacent Tech label.
* `domain` → **`DomainFamily` + {ContextId list} + UTS twins**.
* legacy `…CarrierRole` → **`Holder#…Role:Context`**.
* ambiguous `Owner` in role names → prefer **`StewardRole` / `CustodianRole` / explicit responsibility head**.
* job titles (`owner`, `lead`, `champion`) in the kernel → **use explicit `…Role` names**; keep titles in Plain with twin‑labels.
* **Do:** `FlowDescription: ReturnsHandling`, `Tradition: Test‑Driven`, `Holder#CustodianRole:Asset‑Ledger`.
* **Don’t:** `Returns Process`, `TDD Tradition` (kernel), `Ledger Owner` (underspecified).

**Worked mini‑examples across arenas**
1. **Software engineering:** `BuildFlowDescription`, `CIHarnessSpec`; `Holder#MaintainerRole:Repo‑X`. Avoid `Build Process`, `Repo Owner`.
2. **Applied research / experimentation:** `SamplingMethodSpec`, `CalibrationLineageCarrier`; `Holder#ReviewerRole:Grant‑Call‑Y`.  Avoid `Sampling Algorithm` (if prose), `Lab Owner`.
3. **Production / service management:** `ShiftWork`, `SafetyOfficerRole`; `Holder#SafetyOfficerRole:Plant‑Ops`.  Avoid `Safety Officer` as a type, `SafetyDomain Governance`.
4. **Operations research / optimisation:**  `RoutingMethodDescription`, `CostCharacteristic`; `Holder#ModelStewardRole:OR‑Program`.  Avoid `Routing Function`, `Model Owner`.
5. **Healthcare / clinical ops:** `CarePathwayFlowDescription`, `MedicationAdministrationWork`; `Holder#AttendingPhysicianRole:Ward‑12`. Avoid `Care Process`, `Ward Owner`.
6. **Finance & accounting:** `ReconciliationMethodSpec`, `JournalPostingWork`; `Holder#TreasuryStewardRole:Liquidity‑Book`. Avoid `Reconciliation Process`, `Account Owner` (underspecified).
7. **Legal / compliance:** `RetentionPolicySpec`, `InvestigationWork`; `Holder#DataProtectionOfficerRole:Org‑X`. Avoid `Compliance Function`, `Data Owner` (underspecified).
8. **Cloud / IT operations:** `IncidentFlowDescription`, `RunbookMethodSpec`; `Holder#OnCallEngineerRole:Service‑Y`. Avoid `Incident Process`, `Service Owner` (underspecified).
9. **Logistics / supply chain:** `PickingWork`, `RoutingMethodSpec`; `Holder#DispatcherRole:Hub‑Z`. Avoid `Picking Process`, `Fleet Owner`.
10. **Construction / civil engineering:** `PermitAcquisitionFlowDescription`, `InspectionMethodSpec`; `Holder#SiteStewardRole:Project‑Lot‑17`. Avoid `Inspection Process`, `Site Owner`.
11. **Emergency response:** `TriageMethodDescription`, `EvacuationFlowDescription`; `Holder#IncidentCommanderRole:Event‑R`. Avoid `Triage Function`, `Incident Owner`.
12. **Agriculture:** `IrrigationFlowDescription`, `SoilSamplingMethodSpec`; `Holder#FieldStewardRole:Plot‑17`. Avoid `Irrigation Process`, `Field Owner`.

**Checklist before minting a KernelToken**
* Head noun signals kind (Onto1).
* I/D/S morphology correct (Onto2).
* If role‑related: **Role vs Holder vs Carrier** separation observed; holonic scope explicit (Onto3).
* Any Domain mention stitched to D.CTX and UTS; **no norms on Domain** (Onto4, Onto6).
* Object‑of‑talk declared (Onto5).
* SCR‑LEX rewrites checked / legacy forms migrated (Onto6).
> **Note on registers.** Keep figurative or business‑casual terms in the **Plain** register only, with strict **twin‑label** links to the Tech token (LEX‑BUNDLE). In the **Tech** register, speak in KL‑CAL: **episteme‑about‑epistemes** (Tradition, Lineage, Profile), not in catalogue‑admin idioms.

* **Onto‑Deon — Deontic lexicon guard (Core register)**
**Rule.** In the Conceptual Core, avoid using **“Standard”** as the head noun of an *intensional object* name unless the object is an explicit **deontic speech-act** under the **Gov** lens (cf. E.3).

For interface/boundary invariants and public commitments of **things** (holons, interfaces, ports), prefer intensional names like **InterfaceContract**, **ComplianceProfile**, **AcceptanceSpec**, **InteropProfile**, etc.

Use the word **standard** for a **Description/Specification publication** that is *intended to be complied with* (and that has explicit compliance checks).

If an intensional object is currently named `… Standard`, rename it to a proper intensional name, and (optionally) add a separate Description/Specification publication that contains the standard text and the intended compliance checks.
 **Rewrite hints (Tech → Tech).**
 `publication Standard` → `publication standard`;
 `frame Standard` → `frame standard`;
 `measurement Standard` → `measurement standard`;
 `Method Interface Standard (MIC)` → `Method Interface Standard (MIS)` *(alias acceptable during transition)*;
 `Boundary‑Inheritance Standard (BIC)` → `Boundary‑Inheritance Standard (BIS)` *(alias acceptable during transition)*.
 **Rationale.** Keeps Core prose centred on **intensional objects** and their boundary invariants; reserves deontic obligations for governance contexts and **U.PromiseContent**‑like promises. Do **not** misuse “plane”: deontic speech‑acts are analysed via the **Gov** lens, while **ReferencePlane** remains `{world | concept | episteme}`.

### E.10:6.2 - Twin‑Register Discipline (Tech / Plain)

**Plain twin (LEX).** A registry entry pairing the **authoritative Tech label** with a **display‑only Plain label** for one `U.Type` **in one `U.BoundedContext`**; governed by **PTG (Plain Twin Governance; in the LEX registry)** and referenced by `Twin‑Map ID (LEX)`. *“Plain twin” ≠ the **Plain register** (the register is where twins may be used; the twin is the 1:1 mapping).*
**Convention.** In this spec, **Plain** (capitalized) names the register; **plain twin** (lowercase) names the 1:1 mapping entry.

> **Rule R‑0 (Registers).** Every Kernel and Extenstion patterns concept has a **Tech label** (the testable semantic token) and an optional **Plain label** (didactic synonym). The **Tech label is authoritative**; the Plain label is permitted *only* in expository text and must map 1:1 to the Tech meaning inside the current **Context**.

#### E.10:6.2.1 - Allowed pairs (normative table; examples)

| **Tech (authoritative)** | **Plain (didactic)**                        | **Notes & guards**                                                                           |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `U.System`               | system, machine, team                        | Bare “service” is **never** a safe Plain twin for `U.System`; treat it as an **always‑unpack** token (L‑SERV, A.6.8). Avoid “service‑instance”; prefer “system instance”, “service access point”, or “service offering” depending on facet. |
| `U.Episteme`             | body of knowledge, document, dataset, model | Pair must respect **Carrier vs Content** (A.7).                                              |
| `U.Method`               | how‑to, procedure (abstract)                | Do **not** call this “process” (L‑PROC).                                                     |
| `U.MethodDescription`    | recipe, SOP, playbook, code, spec‑text      | If testable, call out **Spec** explicitly per E.10.D2 (I/D/S).                               |
| `U.Work`                 | run, execution, activity, job, case         | Never use “process” or “procedure” here.                                                     |
| `U.Role`                 | role, hat, mask                             | Always **context‑indexed** per D.CTX.                                                        |
| `U.PromiseContent`              | promise, offering, service offering         | Never equate to provider system or API (L‑SERV).                                             |
| `U.Capability`           | ability, capacity (within bounds)           | Separate from Role/Method/Work; must carry **envelope & measures**.                          |
| `U.Dynamics`             | law of change, model of evolution           | Not a capability or a method.                                                                |

**R‑1 (Plain first‑use).** At first use in a section, show **Tech label** and (optionally) the Plain twin: *“…a `U.Method` (the **how‑to**), described by a `U.MethodDescription` (the **recipe**) …”*
**R‑2 (No unpaired Plain in CC).** Conformance Checklists must use **Tech labels** only.

Domains can mint aliases inside their `U.BoundedContext` glossary; all aliases must map 1:1 to a Tech label (**SenseCell** row in the Context’s **Concept-Set Table**), and if exported across Contexts, via an **Alignment Bridge** (with **CL/Loss**).

 Make “plain twins” (reader‑friendly labels) **safe by construction**, not just style. The plain twin must **not** change kind, scope, or reader expectations versus the canonical Tech name; it is **display‑only** and **context‑local**.

* **Tech name (tech)** — the canonical, kernel‑conformant label used in **normative** clauses (e.g., `U.RoleAssignment`, `TransformerRole`).
* **Plain twin (plain)** — a didactic **display alias** permitted in **expository** prose and UI display contexts **inside one `U.BoundedContext`**.

> **Principle:** *Meaning lives in the Tech name; the plain twin may never move meaning.* (Locality is enforced by `U.BoundedContext` and Bridges.)

#### E.10:6.2.2 - Plain Twin Safety constraints (normative)

**CC‑TWIN‑1 - One‑to‑one & local.**
Each Tech name has **at most one** plain twin **per `U.BoundedContext`**; the same plain twin **MUST NOT** point at more than one Tech name in the same Context.

**CC‑TWIN‑2 - Sense‑equivalence proof.**
A plain twin **MUST** bind to the **same SenseCell** as its Tech name in that Context (F.3/F.7). Authors **MUST** record at least one **counter‑example test** showing how the twin could be misread and why it still passes **in this Context** (SenseCell notes).

**CC‑TWIN‑3 - Head‑term discipline (HND).**
The plain twin **MUST** preserve the **head term** of the Tech name, or append an explicit bracketed head on **first use**:

* Roles keep **“(role)”**, Services keep **“(service)”**, Methods keep **“(method)”**, Work keeps **“(work record)”**, Capability keeps **“(capability)”**.
  *Examples:*
  `TransformerRole` → “**Transformer (role)**”,
  `U.PromiseContent` → “**Service (service)**”,
  `U.Work` → “**work (work record)**”.

**CC‑TWIN‑4 - Kind‑consistent.**
A plain twin **MUST NOT** map across **Kinds** (C.3). If the twin’s everyday reading could denote a different Kind (e.g., *Tradition* = organization, corpus, domain), it is **forbidden** unless qualified by a bracketed head and **Context gloss** on first use (see CC‑TWIN‑7).

 **CC‑TWIN‑5 - Ambiguity stop‑list.**
The following base nouns are **reserved** and **MUST NOT** be used as unqualified plain twins: *Tradition, service, process, function, model, system, method, standard, library, dataset, evidence, activity, task, action*.
They are allowed **only** with an explicit head per **CC‑TWIN‑3** and a **Context gloss** (CC‑TWIN‑7). *(This list MAY be extended in the registry.)*

**CC‑TWIN‑6 - No cross‑context by label.**
Plain twins are **not portable**. Reuse in another `U.BoundedContext` requires a **Bridge** with CL and loss notes; names alone carry no authority.

**CC‑TWIN‑7 - First‑use gloss.**
At first occurrence in a document or screen, a plain twin **MUST** be shown as **“Plain twin \[Tech name] — Context gloss”**, e.g.:
“**Transformer (role)** \[**TransformerRole**] — *mask borne by a system to enact a method step in OR\_2025*”.

**CC‑TWIN‑8 - Normative surface ban.**
Plain twins **MUST NOT** appear in **Conformance Checklists, predicates, type signatures, or acceptance clauses**. Only Tech names are normative. (Plain twins are strictly didactic.)

**CC‑TWIN‑9 - Twin budget.**
**At most one** plain twin per Tech name per Context. Synonym piles are prohibited (control vocabulary sprawl; see F.14).

**CC‑TWIN‑10 - Registry entry & DRR.**
Every plain twin **MUST** have a **registry entry** (in the LEX registry) recording: `tech`, `plain`, `context`, `head`, **SenseFidelity = {3,2,1,0}**, ambiguity notes, counter‑examples, DRR id. Any change requires a **DRR**.

**CC‑TWIN‑11 - Tests.**
 Twin entries **MUST** pass the **Twin Harness** (see F.15): *Head term*, *Kind consistency*, *SenseCell match*, *Stop‑list compliance*, and *First‑use gloss*.

### E.10:7 - Minimal Generality & Domain Anchoring (MG-DA) — names neither parochial nor vacuous

> **Principle (MG-DA).** A minted name is **as general as necessary and no more**, and its **head noun is anchored to the FPF kind being named**. First classify the **NameToken (name of a concept: term, lexical unit) itself** using **`LEX.TokenClass`**, then apply the guardrails corresponding to that class: kernel tokens must unify **across domains**; discriminator/context tokens must make the **domain legible** *from the name itself*. Names too general to have obvious domain are **banned**.

#### E.10:7.1 - `LEX.TokenClass` (meta‑lexical; not a USM Scope)
**Definition.** `LEX.TokenClass : NameToken → {KernelToken | ContextToken | DiscriminatorToken}`.
This is a **Characteristic on NameTokens** (symbols), used by the LEX registry and MG-DA checks.
It is **not** a USM scope and carries **no** truth/validity semantics.

#### E.10:7.2 - `KernelToken` — Minimal Generality (MG‑K)
**MG‑K1 (Tri‑domain witness, MUST).** Maintain a DRR/Glossary note with **≥ 3 heterogeneous arenas** where the invariants hold (e.g., manufacturing, healthcare, cloud ops). If you cannot, narrow to a Context name or move qualifiers into **RCS** (Role Characterisation Space).
**MG‑K2 (No parochial nouns, MUST).** Kernel names **MUST NOT** contain domain nouns (*Ticket, Microservice, Patient, Developer*). Such nouns belong in **Context** or as **RCS Characteristics**.
**MG‑K3 (No vacuity, MUST).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use existing kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).
**MG‑K4 (Intent over mechanism, MUST).** Kernel type/role names encode **intent**, not mechanism. Mechanisms (algorithms, hardware form, recipe flavors) live in **RCS** or **Capability**.
**MG‑K5 (Notation independence, SHOULD).** The intensional meaning is separable from any one notation/toolchain.
**MG‑K6 (Refactoring safety, MUST).** If a name fails MG, do **not** mutate it silently. Record a DRR and apply F.13 **Lexical Continuity & Deprecation** (aliases; Bridges for Cross‑context mappings).

#### E.10:7.3 - `DiscriminatorToken` / `ContextToken` — Domain Anchoring (DA‑D)
**DA‑D1 (kind anchoring, MUST).** The head noun names the **FPF kind being classified** (e.g., *Sense*, *Context*, *Role*, *Bridge*, *Characteristic*). Readers can answer “**X of what?**” without external context.
**DA‑D2 (Characteristic, not axis, MUST).** Enumerated properties are named as **Characteristic**  within a **CharacteristicSpace** (MM‑CAL). Avoid spatial metaphors (*axis, dimension, plane, lane, tier, layer*) unless the metaphor is a **pattern‑defined primitive** in this spec.
**DA‑D3 (Enum clarity, MUST).** If the term denotes an enumeration, (a) the value set is **small and closed**, (b) membership criteria are obvious from the definition, (c) the **kind being classified** is explicit in the name (e.g., `SenseFamily`, not bare *Family*, *RowPlane* or overly general *Facet*).
**DA‑D4 (Anti‑recipe, MUST).** Do not bake *how-to* or local methods into discriminator names; those belong in `U.Method` or `U.MethodDescription`, or in `U.Capability` when the live object is an ability envelope.
**DA‑D5 (Mapping discipline, MUST).** Cross‑context readings go through a **Bridge** (F.9). Discriminator names must not suggest global identity.
**DA‑D6 (Register discipline, SHOULD).** Keep normative tokens stable; synonyms live in **Plain** register only and must not appear in constraints/tests.
**DA‑D7 (Ban generic combinators, MUST).** Reject vague composites like *NameUseMode*, *NamingScope*, *RowFacet/RowPlane/RowLane*. Each candidate must pass **DA‑D1** and **DA‑D3** (kind-anchored head and explicit **CharacteristicSpace**).

#### E.10:7.4  - Global tests (apply after 7.2/7.3)
**MG-DA‑T1 (Three‑arena witness).** If **`LEX.TokenClass`(t)=KernelToken**, you **MUST** provide the tri‑domain witnesses (7.2‑MG‑K1). Otherwise this is **SHOULD** (document at least one contrasting arena).
**MG-DA‑T2 (Object‑of‑talk).** The head noun uniquely signals the subject area; avoid free‑floating metaphors. **MG-DA‑T3 (Anti‑recipe).** Remove mechanism/implementation words; relocate to Method/Capability/RCS.
**MG-DA‑T4 (Enum clarity).** For enumerations, list the closed value set and its CharacteristicSpace.
**MG-DA‑T5 (Collision & Uniqueness, MUST).** Before merge, run a **full‑text search** over the corpus and the **Reserved‑Names registry**. The candidate **MUST NOT** collide with any existing token used in another sense anywhere in FPF. If a collision exists, either rename or raise a DRR to deprecate the prior token.
**MG-DA‑T6 (Teaching swap).** In didactic prose (E.10.D2), the term can be swapped in **without caveats**.
**MG-DA‑T7 (Intensional ground, MUST).** The definition card states the intensional criterion for membership explicitly; reviewers can check membership without reading external narrative.

#### E.10:7.5 - Compatibility with USM (how tokens and scopes meet)
**USM applies to acts, not tokens.** Mint/rename/use are **LexicalActs** that carry a USM scope. `LEX.TokenClass` constrains **where** a token may be used via an **AllowedScopes** policy:
**Conformance rule.** For any usage `u` of a token `t`: `LEX.TokenClass(t)=c  ⇒  USM.Scope(u) ∈ AllowedScopes(c).`

The LEX registry defines `AllowedScopes(c)` (e.g., `KernelToken` usage in normative kernel constraints is allowed; in Plain register outside a glossary is restricted; Context emissions of `KernelToken` require a Bridge/alias, etc.).

**Audit.** Violations are flagged as **SCR‑LEX‑Sxx** (see acceptance tests below).

#### E.10:7.6 - Metaphor guidance (non‑binding heuristics)
Prefer **object‑anchored heads** to metaphors. If a metaphor is unavoidable, ensure it is (a) explicitly defined by a pattern here, and (b) unambiguous within the **NameClass**. Example families (use sparingly):
* **Progression metaphors** (*level, tier, ladder*): only where a **gate/upgrade** is defined by the pattern.
* **Separation metaphors** (*lane, track*): only where parallel, non‑interfering flows are enforced by rules.
* **Grouping metaphors** (*family, class*): only for **small, closed enumerations** attached to a clearly named classified kind (e.g., `SenseFamily` rather than bare *Family*).

#### E.10:7.7 - Short‑form and acronym discipline
**SF‑1 (First expansion, MUST).** On first use, expand the term; place the short‑form in parentheses (e.g., “Minimal Generality & Domain Anchoring (**MG-DA**)”).
**SF‑2 (Uniqueness, MUST).** Register short‑forms in the **Reserved‑Names** list; run the collision check (7.4‑MG-DA‑T5).
**SF‑3 (Form, SHOULD).** Prefer typographic separators (**MG-DA**) to fused acronyms (**MGDA**). Use the fused form only in code or identifiers where punctuation is disallowed, and only after registration.

#### E.10:7.8 - Examples (illustrative, canonical)
Prefer **`U.PromiseContent`** (promise) over *BusinessService*; **`U.Capability`** over *Function*; **`U.Dynamics`** over *NaturalProcess*; **`U.WorkPlan`** over *ScheduleProcess*.
Do **not** mint *ETLService* at kernel level—model ETL as `MethodDescription`; the **Service** is “data delivered under acceptance.”

#### E.10:7.9 - Acceptance & regression checks (LEX/USM)
**SCR‑LEX‑S01 (TokenClass declaration).** Every normative token has a declared `LEX.TokenClass`.
**SCR‑LEX‑S02 (Collision & uniqueness).** Full‑text + Reserved‑Names check passes (no other meaning in FPF).
**SCR‑LEX‑S03 (kind anchoring).** Heads name the FPF kind classified (DA‑D1).
**SCR‑LEX‑S04 (CharacteristicSpace).** Enumerations declare their value set and space (DA‑D2/3).
**SCR‑LEX‑S05 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
**SCR‑LEX‑S06 (Slot/Ref suffix discipline).** Any token with suffix **`…Slot`** or **`…Ref`** is either (a) a **SlotKind**/**RefKind** declared under A.6.5, or (b) a episteme field whose type is a RefKind; no ValueKind or other type class may end with these suffixes.
**SCR‑LEX‑S07 (Manifest `provides` covers SlotKinds and RefKinds).** If a `SignatureManifest` is present (A.6.0), its `provides` list MUST include any public **SlotKinds** (`…Slot`) and **RefKinds** (`…Ref`) introduced by that signature or mechanism, in addition to types, relations, and operators, so SD and lexical linters can treat them as exported API.
**RSCR‑LEX‑E01 (Banned generics).** Reject tokens matching the banned combinators list (DA‑D7).
**RSCR‑LEX‑E02 (Metaphor hygiene).** If a metaphor is used, show the pattern that defines it; otherwise rename.
**RSCR‑LEX‑E03 (Strategy token minting).** Reject new Kernel tokens named **Strategy**/**Policy** as kinds; model them as **lenses/flows/compositions** inside **G.5** or as **…Description/…Spec** in Contexts. (Prevents kernel overloading; aligns with C.22 “no minted Strategy head”.)

### E.10:8 - Morphology & Lexical Form (LEX.Morph)

> **Principle.** Form follows the **FPF kind being named**. A token’s morphology (suffix/prefix/casing) must (a) express **what kind of thing** it names, (b) respect **MG-DA** (Minimal Generality & Domain Anchoring), and (c) pass **LEX.TokenClass** gates:
> `LEX.TokenClass(token) ∈ {KernelToken | ContextToken | DiscriminatorToken}`.
> Morphological choices never override **I/D/S layers** or **CHR\:ReferencePlane** semantics.

#### E.10:8.0 - Casing & basic forms

**M‑0 (Casing and categories).**
Types & role kinds: **UpperCamelCase** (`IncisionOperatorRole`, `MethodDescription`).
Relations/verbs: **lowerCamelCase** (`performedBy`, `isExecutionOf`, `bindsMethod`).
IDs/instances: **flat with delimiters** (context‑defined) but never collide with type forms (e.g., `W#Seam134`, `ctx:Hospital.OR_2025`).
**Register discipline:** normative tokens use the Technical register; Plain synonyms are allowed in prose only, never in constraints.


#### E.10:8.1 - Reserved suffixes (gated by LEX.TokenClass and I/D/S)

> **Use tables as a whitelist.** Rows indicate **when** a suffix is permitted and **what it means**. “Layer gate” prevents I/D/S confusion; “Examples” are illustrative.

| **Suffix**              | **Kind named by suffix**                   | **Layer gate**                       | **LEX.TokenClass gate**         | **Examples**                                      | **Forbidden misuses (typical)**                                       |
| ----------------------- | ------------------------------------------ | ------------------------------------ | ------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| **`Role`**              | **Role kind** (intensional)                | I‑layer                              | KernelToken/ContextToken        | `TransformerRole`, `ApproverRole`                 | Appearing in BoM/mereology; mixing with run logs.                     |
| **`Method`**            | **Abstract way of doing** (recipe type)    | I‑layer                              | KernelToken/ContextToken        | `SteriliseInstrumentMethod`                       | Versioning on `Method` (version the `MethodDescription` instead).     |
| **`MethodDescription`** | **Recipe/description** (notation‑agnostic) | D‑layer                              | KernelToken/ContextToken        | `JS_Schedule_v4_MethodDescription`                | Calling it “process”; encoding runtime actuals here.                  |
| **`…Spec`**             | **Testable specification** (acceptance‑bound) | S‑layer                              | KernelToken/ContextToken        | `MethodSpec`, `FlowSpec`, `SystemSpec`            | Using “Spec” without acceptance tests/harness; putting runtime actuals here. |
| **`Work`**              | **Execution** (runs or kinds of runs)      | (run record; not I/D/S)            | KernelToken/ContextToken        | `SpeechActWork`, `W#Seam134`                      | Plans/schedules; design‑time recipes.                                 |
| **`WorkPlan`**          | **Schedule of intent**                     | D‑layer (plan record)              | ContextToken                    | `MaintenanceWorkPlan_Q3`                          | Logging actuals; claiming execution.                                  |
| **`Service`**           | **External promise object**                | I‑layer (Standarded intension)       | KernelToken/ContextToken        | `ObjectStorageService`, `PassportIssuanceService` | Naming teams/APIs as “Service”.                                       |
| **`Capability`**        | **System ability**                         | I‑layer                              | KernelToken/ContextToken        | `ScheduleGenerationCapability`                    | Mislabeling roles or methods as capabilities.                         |
| **`Dynamics`**          | **Law/model of change**                    | I‑layer                              | KernelToken/ContextToken        | `LotkaVolterraDynamics`                           | Using for abilities (`Capability`) or recipes (`Method`).             |
| **`Observation`**       | **Observation record/kind**                | (run record; not I/D/S)            | ContextToken/DiscriminatorToken | `VibrationObservation`                            | Mixing with `MethodDescription` or `Evaluation`.                      |
| **`Evaluation`**        | **Evaluation episteme or evaluation record**        | D/S‑layer (epistemic episteme)              | ContextToken/DiscriminatorToken | `CalibrationEvaluation`                           | Using to name roles or methods.                                       |
| **`EvidenceRole`**      | **Role in evidence assembly**              | I‑layer (role kind)                  | KernelToken/ContextToken        | `WitnessStatementEvidenceRole`                    | Using as a generic “evidence”.                                        |
| **`Episteme`**          | **Epistemic knowledge unit** (structural)  | D/S‑layer                            | KernelToken/ContextToken        | `TraceabilityEpisteme`                            | Colliding with CHR **ReferencePlane** (never suffix “Plane”).         |
| **`System`/`Holon`**    | **Substantial entity**                     | I‑layer                              | KernelToken/ContextToken        | `AnesthesiaSystem`, `OrderFulfillmentHolon`       | Using to denote Context or run record.                              |
| **`Boundary`**          | **System boundary**                        | I‑layer                              | KernelToken/ContextToken        | `SterileFieldBoundary`                            | Using as a role or method.                                            |
| **`Objective`**         | **Target state**                           | I/D‑layer (depends on formalization) | KernelToken/ContextToken        | `HemostasisObjective`                             | Encoding acceptance tests here (put tests in Spec/MethodDescription). |
| **`Requirement`**       | **Obligation at acceptance**               | D/S‑layer                            | KernelToken/ContextToken        | `LatencyRequirement`                              | Using as a role or capability.                                        |
| **`BoundedContext`**    | **Context card**                           | (meta‑structural; not I/D/S)         | ContextToken                    | `ITIL_2020_BoundedContext`                        | Treating Context as domain; minting `U.*` inside a Context.           |
| **`Surface`**              | `PublicationSurface` or `InteropSurface` over an episteme   | D and S layer (publication)     | ContextToken                     | PublicationSurface, InteropSurface       | StructureSurface, MechanismSurface, PortfolioSurface |
| **`Card`**                 | UTS/record unit (episteme)               | D-layer (publication)       | ContextToken                     | MethodCard, ExternalIndexCard            | Encoding runtime actuals; using as a ‘Service’  |

| **Suffix** | **Lexical class** | **Meaning / Ontology** | **Where it lives** | **Examples / Notes** |
|--- |--- |--- |--- |--- |
| **Space** | Intensional kind | A typed **state space** (finite product of Characteristic×Scale slots); no procedures | Kernel A.19; CHR/space consumers | `CharacteristicSpace`, `CreativitySpace`. Edition of a Space is a **phase** of the episteme that defines it. |
| **SpaceRef** | Pointer | Registry reference to a Space | Data fields / UTS | `CharacteristicSpaceRef`. Use **`.edition`** on the **Ref** when pinning a historical phase. |
| **Map** | Intensional kind (method) | A **mapping method** from subjects to coordinates in a declared Space (encoder/featurizer) | Kernel/Method family (I‑layer), described/spec’d via I/D/S | `DescriptorMap` (declares invariances, corpus typing). Not a record or file. |
| **MapRef** | Pointer | Registry reference to a **Map** | Data fields / UTS | `DescriptorMapRef`. Pin the method phase via **`DescriptorMapRef.edition`**. |
| **Def** | S‑layer alias (CG‑Spec family) | A **definition/specification publication** that fixes a **formula** or **distance** over a space; *synonym of …Spec* **within CG‑Spec registries only** | Part G (CG‑Spec family) | `DistanceDef` ≍ `DistanceSpec`. Prefer **…Spec** in new normative prose; **…Def** retained where already published. |
| **DefRef** | Pointer | Registry reference to a **…Spec/…Def** | Data fields / UTS | `DistanceDefRef`. Use **`DistanceDefRef.edition`** to pin the exact formula edition. |
| **Spec** | S‑layer | Testable invariants bound to acceptance harnesses | E.10 & A.21 | For stable, testable definitions; **normative** by default; S‑layer, Spec‑gated | Use for normative calculi and scoring/normalization specifications. |
| **Slot** | Structural position | Named **argument position** in a relation/morphism signature (SlotKind in A.6.5) | Kernel A.6.0/A.6.5 | `DescribedEntitySlot`, `GroundingHolonSlot`. Always names a *position*; never used for ValueKinds or episteme fields. |
| **Ref** | Pointer | **Reference/identifier** to a registry item of some ValueKind (RefKind in A.6.5), not the thing itself | Data fields / UTS; RefKind types | `U.EntityRef`, `U.HolonRef`; episteme fields `…Ref : U.EntityRef`. Reserved for **RefKinds** and episteme fields typed as them; `…Ref` **never** carries content and is never used for ValueKinds or SlotKinds. |
| **Series** | Governance object | A **PhaseOf chain** (“editions”) for an episteme | Edition governance | `U.EditionSeries`. Holds immutability and provenance rules. |
| **.edition** | Attribute (on **Ref**) | The **phase id** of the **referenced record**; attaches to `…Ref`, not to the record name | Data fields / UTS | Use `XRef.edition`, **not** bare `XEdition` fields. Lower camelCase for keys. |

**Notes.**
• **Kernel‑only ban list** remains in § 8.3.
• **CHR guard:** the only token that may use the word *plane* is **CHR:ReferencePlane**.
• **Axis and dimension metaphors** are deprecated; use **Characteristic** for a measured aspect and **CharacteristicSpace** for a declared characteristic space where an enumeration is intended (see § 7).

**Not only suffix guard**
* Suffixes are closely related to kinds and **should** be clearly guarded by MG-DA.
* Other morphemes (not only suffixes) also **must** respect kinds. For example, **Space is a geometric concept** — **never** use it as a suffix (`…Space…`) or other morpheme in beginning or in the middle of a term to name non‑geometric entities (e.g. prefer **Set/Kid/Kit** instead of **Space** where membership is intended).

**L-EPI-PUB — episteme, publication, view, carrier, and authority-reference lane discipline**
* Use `U.Episteme` for the claim-bearing unit. Use `U.EpistemePublication` or governed `U.Episteme` publication only when that episteme is available as a published episteme under C.2.1/E.17 discipline.
* Name the exact publication form separately from the episteme: for example `U.PreArticulationCuePack`, `RoutedCueSet`, `U.AbductivePrompt`, typed route-bounded projection, partial normal form, endpoint-pattern-governed publication, or another declared form. A publication form is not itself the governing FPF source.
* Name `U.View` and MVPK face separately from the publication form. A `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane` is an episteme-level view or publication face, not the source claim, not the publication form itself, and not the SCR or RSCR carrier.
* Name the carrier or rendering lane separately. Documents, dashboards, generated screens, trace files, cards, and transport formats hold or render a publication; they are not the `U.Episteme`, not the claim or effect being relied on, and not the governing pattern.
* Name source-finding cues separately from source epistemes. A cue, badge, credential view, dashboard tile, heading, signature-looking mark, or generated explanation may help find a source; it does not by itself create an `authoritySourceRef` target, evidence relation, gate decision, assurance claim, role assignment, status assertion, work occurrence, or permission.
* Use `governingPatternRef` for a named FPF pattern that governs admissible interpretation or use. Use `authoritySourceRef` when a non-pattern `authoritySourceRef` target such as an external standard, editioned register, DRR, gate decision, policy source, or role-assignment or status register carries the relevant authority. Do not use generic semio wording, generic source wording, generic project-work wording, or container-placement wording as solution terms.
* When a published episteme is used for work, name the live P2W chain element: intended method family, selected method/method of work, `U.WorkPlanning` baseline, planned work, actual `U.Work` or `U.WorkEnactment`, work result, result measurement, or non-work reliance on a claim or effect. Do not let generic `action`, `use`, or `material` hide that distinction.
* Use `E.10.SEMIO` when semio-heavy wording carries episteme, publication, view, carrier, relation, admissibility, evidence, work, gate, decision, method, or FPF-pattern-application load. This parent pattern keeps the lexical and naming discipline; `E.10.SEMIO` supplies the semantic-rewrite profile that recovers the exact FPF kind, relation record, relation phrase, tuple-like record, exact project-side FPF kind and reference, or not-triggered disposition before final wording is accepted.

**L‑SURF — disciplined use of *Surface* **
* **Definition.** *Surface* is reserved for `PublicationSurface` and `InteropSurface`: UTS, shipping, and interop publication surfaces that present admissible, plane-aware summaries for a stated audience and purpose. A Surface is a conceptual bundle of views in the ISO 42010 sense, with declared viewpoint. Serialisations live in Annex and Interop. Surfaces package D and S projections produced via `Describe_ID` and `Specify_DS` in `A.7` and do not change object ontology.
* **Allowed:** `PublicationSurface`, `InteropSurface` (G.10/G.13).
* **Forbidden:** `StructureSurface`, `MechanismSurface`, `PortfolioSurface`, and any `…Surface` that denotes a structural, mechanistic, measurement, review, assurance, explanation, comparison, or publication-unit object.
* **Preferred alternatives:** use `…Boundary` (structural border), `…View` (publication view), or `…Card` (UTS record).

**L‑SPACE — disciplined use of *Space* **
* Use *Space* only for **CHR‑grounded measurement and state constructs** such as `CharacteristicSpace` per A.19. Do **not** coin generic `…Space` for sets, portfolios, or publication forms. Publish portfolios and archives as **sets** via admissible selectors; publish them on UTS as **views** or **cards**, not as spaces.
* **Field‑name guard (Kernel blocks).** In **Kernel conceptual blocks** (e.g., A.6.0/A.6.1 lists), **do not** name a field `…Space`; reserve *Space* to the **types** (CHR/ReferencePlane families). Use **BaseType** as the field name and let the referenced `U.Type` carry `…Space` where appropriate; otherwise, for set‑valued universes, use `…Set`.
* Space is geomertic concept, neve use it even not as a suffix for naming non-geometric spaces (e.g. instead of Sets with membership)

**L‑ROLE — disciplined use of *Role***
* **Role** is always **Role Enactment for the `U.Holon`/`U.System` kind** (agentive use).
* **Param‑slot / relation‑endpoint guard.** Do **not** use the morpheme **`Role`** for **formal parameter positions** in operator algebra declarations (`OperationAlgebra`) or Signature arguments. Reserve **`Role`** for **agentive kinds** only (A.2/F.4/F.6). Prefer SlotKinds + SlotSpecs (A.6.5) to type formal slots; if a didactic list is useful, use a `ValueKindView` (name→ValueKind) projection derived from SlotSpecs/SlotIndex. Same for similar situations (table columns, tuple placements): use MG-DA with domain‑**specific** terminology, never “Role”.

#### E.10:8.2 - Forbidden suffixes & the DevOps, Data Governance and Repository-Workflow Lexical Firewall

**M‑F (Forbidden in Kernel tokens).** In KernelToken names, do **not** use: *…Function*, *…Process*, *…Task*, *…Activity*. These are ambiguous or vacuous—map using § 6 typing rules (often to `Method`, `MethodDescription`, or `Work`).

**M‑FW (Tool/file markers).** Tooling/file suffixes (*…API*, *…JSON*, *…YAML*, *…CI*, *…Kafka*, *…Postgres*) are **not** part of conceptual names. Place them in **Context** glossaries or operational configs (DevOps Lexical Firewall). Kernel names never carry tool/format/notation marks. It is pure conceptual, no data management and data governance intended.

#### E.10:8.3 - Prefix discipline

**M‑P1 (Reserved prefixes).** `U.` reserved for **Kernel types**; `Γ_` for algebraic operators; `CAL/LOG/CHR` for **pattern packages**. Never mint `U.*` inside a Context.

**M‑P2 (Edition markers).** Apply explicit edition/version markers to **Contexts** and to `MethodDescription` / `Service`—**not** to `Method` (e.g., `BPMN_2.0_BoundedContext`, `JS_Schedule_v4_MethodDescription`, `PassportIssuanceService_v2025`).  Authors MAY annotate Context or Service names for didactics.
**Norms (edition vs release vs version).**
1) **edition** — the **content phase** of an episteme (Concept/Object/Symbol where Symbol‑only notation swaps do not force a phase). Lives in `U.EditionSeries`. Never embedded in labels (see R‑RD‑7); bind via data: `…Ref.edition`.
2) **release** — a **Work** of making a **Carrier** public; may carry tags/dates; does **not** change episteme identity or phase.
3) **version** — a **tooling/carrier** identifier (file/package/code). Use only in Tooling/Pedagogy families; not in Core names.

**Property discipline.** When a field pins a referenced record’s phase, write it as **`<Thing>Ref.edition`** (dot notation), never as a standalone `…Edition` key. E.g., replace `DHCMethodEdition` with `DHCMethodRef.edition`.

#### E.10:8.4 - Morphology tests (apply with § 7 MG-DA)

**M‑1 (Slot test).** The candidate fits **one** slot in the Strict Distinction lattice (Object ≠ Description ≠ Carrier; Role ≠ Method ≠ Work). If not, **rename** or split.

**M‑2 (Object‑of‑talk anchoring).** The head noun names the **object being classified** (Role/Method/Service/Work/Context/Characteristic). No free‑floating metaphors.

**M‑3 (Family congruence).** Where eligibility clarity is needed, add a **Context‑specific characteristic** (RCS) as a qualifier (e.g., `NormativeStandardRole`). Do **not** fake families with bare metaphors (no `RowPlane`, `senseFamily`, `…Lane`).

**M‑4 (Run vs design).** Use **`Work`** only for executions; use **`MethodDescription`** for recipes; never cross.

**M‑5 (Kernel parochiality).** KernelToken names carry **no domain nouns**; push domain markers to Context or RCS.

**M‑6 (Vacuity ban).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use established kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).

**M‑7 (Notation independence).** Intensional meaning survives notation/tool swaps.

**M‑8 (Collision & uniqueness).** Before merge, run **full‑text** + **Reserved‑Names** checks; the token must not collide with any other meaning anywhere in FPF (cf. § 7 MG-DA‑T5).

#### E.10:8.5 - Alias hygiene

Aliases live **only** inside a **Context Glossary** and map to **one** technical label with an **equivalence** note (≡). No global aliases.

#### E.10:8.5a - Entry lexeme support and lexical-query discipline

Canonical entry-neighborhoods may use one compact **entry lexeme support**
block when the lexical load is real.
That support should not live in every pattern body by default.
Keep it instead in:

* `J.4`,
* `I.2`,
* `Table of Content` query rows,
* or one bounded lexical-support record governed by `F.17`, `UTS`, or `F.18`.

This block remains one editorial lexical-query set.
It does not mint names, aliases, `U.Types`, bridges, or semantic equivalences
by itself.
When visible, it should distinguish at least:

* canonical label,
* plain-language twin,
* domain alias,
* lexical-query cue,
* deprecated cue,
* false friend or forbidden synonym.

Minimal visible lexical-query shape may therefore use one compact field set such
as:

```text
canonical
noncanonical_visible
domain_query_examples
forbidden_aliases
```

Ordinary lexical-query support should stay compact:

* ordinary `Table of Content` rows: prefer `2-5` query phrases;
* ordinary `J.4` neighborhoods: keep only the most discriminating domain phrases and
  false friends;
* fuller lexical sets belong under `F.17, F.18, and E.10` only when one real
  naming, alias, bridge, or collision load exists.

Lexical support should increase entry precision, not maximize keyword recall.
The same boundary should be kept explicit in lexical support:

* `lexical_hook` is not one alias;
* one alias is not one canonical name;
* one search cue is not one semantic equivalence;
* one `entry_orientation_label` is not one `RelationKind`.

Language-specific query cues may be added as entry-lexeme support.
They do not become canonical names, aliases, or semantic equivalents unless
admitted through `F.18` / `E.10`.
One Russian practitioner phrase may therefore help recover one English
canonical pattern while remaining lexical-query support only.

#### E.10:8.6 - Compatibility with USM (acts vs tokens)

**LEX applies to tokens; USM applies to acts.** Mint/rename/use are **LexicalActs** that carry a USM scope (e.g., ClaimScope, WorkScope). LEX constrains **where** a token form may appear via **AllowedScopes** policies:

`LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)`.

Example: using a `KernelToken` in a Context constraint may require a Bridge/alias; logging `Work` inside a MethodDescription violates M‑4 and the policy.

#### E.10:8.7 - Acceptance & regression checks (LEX/USM)

* **SCR‑MOR‑S01 (Suffix whitelist).** Every normative token with a reserved suffix matches § 8.1 row semantics and passes Layer gates.
* **SCR‑MOR‑S02 (Kernel bans).** KernelToken names contain none of the forbidden suffixes (§ 8.2).
* **SCR‑MOR‑S03 (Prefixes).** Reserved prefixes obey § 8.3; no `U.*` minted in Context.
* **SCR‑MOR‑S04 (Run/design gate).** `Work` appears only for executions; `MethodDescription` has no runtime actuals.
* **SCR‑MOR‑S05 (Collision).** Full‑text + Reserved‑Names checks pass (no other sense of the token elsewhere).
* **SCR‑MOR‑S06 (Object‑of‑talk).** Heads pass M‑2; no bare metaphors as heads.
* **RSCR‑MOR‑E01 (DevOps firewall).** Tool/file suffixes quarantined to Context; none leak into KernelToken names.
* **RSCR‑MOR‑E02 (USM compliance).** For each LexicalAct, verify `USM.Scope ∈ AllowedScopes(LEX.TokenClass)` (see § 7.5).

#### E.10:8.8 - Autonomy lexicon (L‑AUTO )
**Forbidden (Core):** bare “validity”, “actor/agent” (as free‑standing nouns), “kill switch”, “process” for behavior, “envelope” when used **as scope**.
**Use instead:** *Scope (G)* for epistemic scope; *WorkScope* for capability bounds; *RoleAssignment* for who acts; *SpeechAct* for overrides; *SafeStop* instead of “kill switch”.
**Named prefixes (policy & registry):**
* `aut:` for AutonomyBudgetDecl fields (e.g., `aut:action_tokens`, `aut:risk_bands`);
* `guard:` for guard checks bound to `AdmissibilityConditionsId`;
* `ovr:` for override SpeechActs (`ovr:PauseAutonomy`, `ovr:ResumeAutonomy`, …).

**Notes.**
1) Scope‑sensitive guards **must** declare the **Γ_time** window selector used for admission checks.
2) Proper names of patterns/components that already include “Agent/Agency” (e.g., *Agency‑CHR*, *Agent‑Tools‑CAL*) are permitted as **titled terms**; avoid re‑introducing “agent” as a free‑standing noun in new prose.

#### E.10:8.9 - LEX-CHR-STRICT — Reserve *Characteristic* for CSLC-measurable aspects

**Intent.** Prevent calling **non-measurable** objects (sets, statuses, scopes, policies, bridges, contexts, guards) “characteristics”.

**Rule L-CHR-S1 (Reservation).** Use **Characteristic** **only** for variables that **declare a CSLC scale** (nominal/ordinal/interval/ratio) with admissible values/units/polarity (Part C.16/A.17–A.18).
**Rule L-CHR-S2 (USM).** `U.Scope` / `U.ClaimScope (G)` / `U.WorkScope` are **USM scope objects**, not Characteristics; they **must not** appear in any `CharacteristicSpace`.
**Rule L-CHR-S3 (Status).** ESG/RSG statuses and deontic/epistemic statuses — **not Characteristics**; its statuses/states.
**Rule L-CHR-S4 (Lexical classifiers).** Lexical classifiers/tags — **Facets**/**attributes**; do not name them as Characteristics, if not declared **CSLC**.
**Checks.**
— **CC-L-CHR-1.** `scope characteristic(s)` is banned in Core/Context.
— **CC-L-CHR-2.** `CharacteristicSpace` near `Scope` — error.
— **CC-L-CHR-3.** Canonical rewrite: `F–G–R characteristics` → `F–G–R components`.

#### E.10:8.10 - LEX‑QA‑1 — Using “‑ility/‑ilities” terms (availability, reliability, …)

**Rule.** Tokens ending with **‑ility/‑ilities** or widely used quality names (**Availability, Reliability, Security, Safety, Scalability, Maintainability, Usability**, …) are **Quality‑Family labels**, not automatically CHR **Characteristics**.

**Authoring choice:**
— To use such a term as a **CHR** characteristic, **bind** it to a **named `U.Characteristic` with one CSLC Scale** (A.18) and refer to that Characteristic in guards/UTS;
— Otherwise **publish a Q‑Bundle** (see **C.25**) that includes **Measures (CHR)** (the measurable slots) and, where relevant, **Scope** (USM set over `U.ContextSlice`) and windows/mechanism/status fields.

**Rationale.** Scope is **set‑valued** (USM) and **not** a CHR measurement; mechanisms/statuses are governance records. Keeping them outside the CHR CSLC avoids illegal scalarisation and preserves set‑algebra semantics for scope. (A.2.6 § 6.2; A.6.1; C.16/A.18).


### E.10:9 - Canonical rewrites for overloaded words (LEX L‑rules; normative)

> **What this section does.** LEX L‑rules standardise **how we speak** in Core/Context by mapping overloaded everyday words to **canonical FPF concepts**.
> **What this section does not do.** It does **not** restate naming (see **§ 7 MG-DA**) or morphology/casing/suffix rules (see **§ 8 LEX.Morph**); it **depends** on them.
> **Guards.** Tokens are classified by **`LEX.TokenClass ∈ {KernelToken, ContextToken, DiscriminatorToken}`** (§ 7.1). Only **CHR:ReferencePlane** may use the bare word *plane*; I/D/S are **layers**; enumerations are **Characteristics** in a **CharacteristicSpace** **only when a CSLC scale is declared; otherwise treat such slots as non-measurable attributes (not Characteristics)**.

#### E.10:9.1 - Hard bans and canonical rewrites (single table; normative)

> **Use this table mechanically.** “Ban” means the listed phrase is **not allowed** in Core prose, identifiers, or diagrams unless the **canonical** appears alongside it (or as a registered Context alias). Layer and token gates prevent I/D/S and TokenClass leaks (cf. § 8.1).

| **L‑rule**   | **Ambiguous or low-precision word (Ban)**                  | **Canonical FPF target(s)**                                                                                                                                                                     | **Layer gate**                                                                       | **TokenClass gate**                         | **Notes**                                                                                            |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **L‑PROC**   | *process*, *procedure*, or *function step*         | `U.Method` (abstract way‑of‑doing); `U.MethodDescription` (recipe/notation‑agnostic); `U.Work` (execution); `U.WorkPlan` (schedule)                                                             | I for `Method`; D for `MethodDescription`; run record for `Work`; D for `WorkPlan` | Kernel/Context for types; Context for runs  | “Industrial process” as **line role** → model system + `…Role`; chemistry in `Method`/`Dynamics`.    |
| **L‑FUNC**   | *function*                                        | `U.Capability` (ability/envelope) **or** `U.PromiseContent` (promise clause or offering) **or** `U.Method` (recipe) **or** `U.Work` (what happened)                                                                       | I for Capability/PromiseContent/Method; run for Work                                        | Kernel/Context                              | Never use *function* as a type name in Core.                                                         |
| **L‑SERV**   | *service* used for team/system/API/ticket/process | Always unpack to the facet: `U.PromiseContent` (service offering or promise clause), `U.Commitment` (SLA obligation), `U.SpeechAct` (promise or offer act), `accessSpec : U.MethodDescription` (API or interface spec), **service access point** (`SystemRef`, addressable endpoint), **service delivery system** (`SystemRef`), **service delivery method** (`U.MethodDescription`), or `U.Work` (delivery run, case, or ticket). | I for PromiseContent/Commitment/Method; D for specs; A for systems; run for Work                                        | Kernel/Context/Discriminator (per facet) | “API = service” is forbidden; name the facet head phrase (A.6.8).                                                           |
| **L‑SLA**    | *SLA* or *service level agreement* used for target, contract, or document | Unpack: (i) targets/SLOs → `U.PromiseContent.acceptanceSpec`; (ii) binding obligation/penalty → `U.Commitment`; (iii) packaged “the SLA” → Contract Bundle (A.6.C); (iv) published terms → `U.SpeechAct` + clause carrier (`U.Episteme`). | I for PromiseContent/Commitment; D for clause carriers/specs; run for Work+evidence | Kernel/Context/Discriminator | Treat “SLA” as polysemic shorthand; never store it as a single type name. |
| **L‑SCHED**  | *schedule*, *plan*, or *calendar* as execution    | `U.WorkPlan` (intent/window) vs `U.Work` (actuals/telemetry)                                                                                                                                    | D vs run                                                                             | Context                                     | Never attach actuals to a plan.                                                                      |
| **L‑ACT**    | *activity*, *action*, or *task* as type           | `U.Work` (execution); **steps** belong to `U.MethodDescription` (with `requiredRoles`, capability bounds)                                                                                       | run vs D                                                                             | Context                                     | Reserve verbs: *enact* (role/RSG), *execute* (Work), *actuate* (System), *approve* (SpeechAct Work). |
| **L‑AGENT**  | *agent / actor / doer* (bare)                     | say “system **bearing** `…Role`”; use `U.AgentialRole` where needed                                                                                                                             | I                                                                                    | Kernel/Context                              | Org titles (Owner/Operator/Reviewer) live as **roles in a Context**.                                 |
| **L‑OWNER**  | *owner of X* (global)                             | Ownership is a **Role** inside a `U.BoundedContext` (e.g., `OwnerRole:ITIL_2020`); SoD via `⊥`                                                                                                  | I                                                                                    | Context                                     | No global “owner” property in Kernel.                                                                |
| **L‑CAP**    | *capability* for assignment, recipe, run, or promise | `U.Capability` only = ability with envelope; assignments are `…Role`; recipes `U.Method` or `U.MethodDescription`; runs `Work`; promises `U.PromiseContent` (service promise clause or offering)                                                       | I vs D vs run                                                                        | Kernel/Context                              | Holder of a Capability is a `U.System`.                                                              |
| **L‑DYN**    | *process of diffusion, growth, or learning*       | `U.Dynamics` (law/model of change)                                                                                                                                                              | I                                                                                    | Kernel/Context                              | Reserve for uncaused change models.                                                                  |
| **L‑EVID**   | “paper/dataset proves/ensures”                    | `…#EvidenceRole:Context` on an **Episteme**; claims/scopes/polarity/timespan; provenance from `Work`                                                                                            | D/S                                                                                  | Context/Discriminator                       | Evidence is a **role binding**, not an actor.                                                        |
| **L‑CTX**    | *context* (fuzzy trope)                           | `U.BoundedContext` (named card)                                                                                                                                                                 | —                                                                                    | Context                                     | Never use “depends on context” in Core; **name** the Context.                                        |
| **L‑BRIDGE** | cross‑context equivalence “by same label” | Explicit **Bridge Card** (F.9): state `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** for disambiguation + licence‑revealing name/verb choice). | — | — | Same label ≠ same concept; umbrella “same/equivalent/align/map/…” must be repaired into a Bridge before it can justify reuse, rows, or substitution. |

> **Red/Green pattern (example).** ✗ “The **process** ensures quality.” → ✓ “The **MethodDescription** defines steps; **Work** is **evaluated** against **RequirementRole**.”


#### E.10:9.2 - Quick substitutions (common rewrite hints)

> Use these as quick rewrite hints; accept only if the transformed sentence passes **§ 7 MG-DA** and **§ 8 LEX.Morph** gates.

| **Ban**                         | **Canonical rewrite**                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| “the process owner approves”    | `SystemX#ApproverRole:Context` **performs a SpeechAct Work** “approve …”                |
| “the document enforces policy”  | `Policy_vN#RequirementRole:Context` **gates** Work; enforcement = **SpeechAct** + audit |
| “our service runs nightly jobs” | Nightly **Work** **claimsPromiseContent**(BatchProcessing); **promise content** defines acceptance     |
| “the API is the service”        | API = `accessSpec : MethodDescription`; **promise content** defines acceptance           |
| “capability assigned to team Y” | Team Y **plays** `Role`; the team (as system) **has Capability** C within envelope E    |
| “process health green”          | StateAssertion for `ObserverRole`/`Service` KPI **passes** acceptance window            |
| “function of component A fails” | **Work** performed by `SystemA#Role` **failed** acceptance (observations show …)        |
| “context is unclear here”       | **Name** the `U.BoundedContext`; else split and Bridge                                  |


#### E.10:9.3 - Acceptance tests (LEX‑AC)

A text **passes** LEX if all answers are **Green**:

1. **Context named.** Polysemous terms appear **inside a named `U.BoundedContext`** (or the page declares a local context card).
2. **Right layer.** I/D/S layer respected: types/roles on I; recipes/docs on D; actuals on runs (cf. § 8.1 gates).
3. **Promise vs ability vs performance.** `PromiseContent` (promise clause), `Capability` (ability), `Work` (performance) are not conflated.
4. **No anthropomorphism.** Documents/datasets/models do not “do”; **Systems** do.
5. **Scheduling hygiene.** No actuals on `WorkPlan`; all actuals live on `Work`.
6. **Cross‑context reuse.** Any reuse across Contexts cites a **Bridge id** with kind, direction, congruence level, loss, and scope. Apply **A.6.9 (RPR‑XCTX)** when the published prose uses “same”, “equivalent”, “align”, “map”, or similar bridge wording.
7. **MG-DA ok.** New or refactored tokens pass **§ 7 MG-DA** (anchored head noun; collision check; CharacteristicSpace for enums).
8. **Morphology ok.** Suffix/prefix/casing respect **§ 8 LEX.Morph** (e.g., `…Role`, `MethodDescription`, `Work`, reserved prefixes).
9. **Banned tokens absent.** No *process/function/task/activity* in Kernel senses; no tooling/file suffixes in Kernel tokens.
10. **State gating present (when needed).** Readiness is expressed via **RSG state** + **StateAssertion**, not vague “approved/ready”.


#### E.10:9.4 - Coordination map (how LEX plugs into the rest of FPF)

* **With E.10.D1 D.CTX (Context discipline).**
  ULR–CTX‑1: Every Core meaning that can vary **names its `U.BoundedContext`**.
  ULR–CTX‑2: Same‑spelled labels are **distinct senses** across Contexts; reuse requires a **Bridge** (F.9) with CL & loss notes.

* **With E.10.D2 (I/D/S discipline).**
  Speak in the **right I/D/S layer**. ULR–IDS‑1..3 apply (types/roles = I; descriptions/specs = D/S; work/state assertions = evaluations/occurrences). Upgrades D→S only when **checkable acceptance** exists.

* **With A.2 / A.15 (Role–Method–Work alignment).**
  Role = **assignment**; Method = **way‑of‑doing**; MethodDescription = **documented recipe**; Work = **dated occurrence**. Sentences must keep this split.

* **With F‑cluster (Unification) & UTS (F.17).**
  Harvest in one Context → **SenseCell** → **Concept‑Set row** with relation (`≡/⋈/⊂/⟂`) and losses. UTS is the human‑readable roll‑up.

> **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance: `LEX.TokenClass(t)=c ⇒ USM.Scope(usage) ∈ AllowedScopes(c)` (see § 7.5).


#### E.10:9.5 - Conformance checklist (LEX‑CC)

1. **LEX‑CC‑1 (Bans).** Any banned token in Core/Arch fails unless the **canonical** appears (or the token is a registered Context alias).
2. **LEX‑CC‑2 (Context).** Each polysemous term names its **`U.BoundedContext`**.
3. **LEX‑CC‑3 (Layer/Morph).** Usage passes **§ 8** gates (suffix/prefix/casing) and I/D/S layer checks.
4. **LEX‑CC‑4 (Bridge).** Cross‑context reuse cites **Bridge id** and CL; same‑spelled labels without a Bridge are non‑conformant.
5. **LEX‑CC‑5 (MG-DA).** New tokens pass **MG-DA** tests, including **full‑text collision** and **Reserved‑Names** checks.
6. **LEX‑CC‑6 (Service & evidence).** Service acceptance computed from **Work**; evidence is an **EvidenceRole** on an **Episteme** with provenance.
7. **LEX‑CC‑7 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
8. **LEX‑CC‑8 (Minting discipline).** If overload cleanup requires one local replacement phrase, the text records the repaired phrase and the governing local repair pattern. If cleanup requires one durable reusable name, the text runs the full **F.18 `MintNew` or `DocumentLegacy`** procedure; intuition-first partial Name Cards are non-conformant.

#### E.10:9.6 - Worked micro‑examples (short, cross‑domain)

**Factory.**
✗ “The **process** failed; the **service** restarted itself.”
✓ `PLC_17#ObserverRole:PipelineOps` logged **Observations**;
`CAB_Chair#ApproverRole:ChangeControl` **performed a SpeechAct** “approve restart”;
`OpsBot#DeployerRole:CD_Pipeline_v7` **executed Work** `RestartRun‑4711` which **claimsPromiseContent**(CoolingUtility);
post‑run **Evaluation** shows the **Service** acceptance **passed**.

**Cloud.**
✗ “The **process owner** approved; the **API service** deployed.”
✓ `ProductLead#AuthorizerRole:Rollout_2025` **performed a SpeechAct**;
`sCG‑Spec_ci_bot#DeployerRole:CD_Pipeline_v7` **performed Work** `Deploy‑F123`;
API = `accessSpec : MethodDescription#REST_v12`; **promise content** “Feature Access” declares acceptance; telemetry **Work** shows **fulfilPromiseContent**.

**Research.**
✗ “Dataset X **proves** the theory; the **process** is reproducible.”
✓ `DatasetX#ModelFitEvidenceRole:Theory_Context` **supports** claim C within scope S;
reproducibility via **StateAssertions** on `ReplicationEvidenceRole`;
procedures are `U.MethodDescription`; re‑runs are **Work**.

**Semioarchitecture.**
✗ “`projection` has one meaning in routing and bridge prose.”
