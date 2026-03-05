**6.6 Name only as much as you will use.**
If a fine-grained split has **no downstream consequence** (Role Descriptions, tables, bridges), prefer the coarser Local-Sense.


### F.3:7 - Outputs (conceptual, not clerical)

F.3 yields, **per Context**:

1. A **small set of Local‑Senses**, each with:

   * **Label pair**: *Tech* (idiomatic) - *Plain* (didactic).
   * **Sense line**: one‑sentence usage statement, in the Context’s voice.
   * **Inside list** (informative): which Units from F.2 it consolidates.
   * **Counter‑example** (optional but powerful): a short use that must **not** be included.
1. A **SenseCell address** for each Local‑Sense: *(Context, Local‑Sense)*.

These are **thinking reference points** (cognitive only), not records or files. Later patterns **cite SenseCells by name**; nothing about storage is implied.


### F.3:8 - Invariants (normative, lightweight)

1. **context‑locality.** Every Local‑Sense belongs to **exactly one context**. No Cross‑context clustering.
2. **Parsimony.** Local‑Senses are **few**; prefer the coarsest partition that preserves the canon’s distinctions.
3. **Idiomatic Tech.** The Tech label **must** stay in the Context’s idiom; no house‑style overrides.
4. **Didactic Plain.** The Plain label **must** aid comprehension **without adding scope**.
5. **Usage‑first.** Sense lines reflect the **canon’s usage**, not imported taxonomies or external theories.
6. **Counter‑examples rule.** If a counter‑example exists that the sense would wrongly include, **split**.
7. **No behaviour math.** Sense lines contain **no** behavioural, deontic, metrological, or type calculus; those live in Part C.
8. **Temporal honesty.** If the Context fixes **DesignRunTag**, the sense line respects it (e.g., PROV *activity* is **run‑time**).


### F.3:9 - Self‑checks (mental probes)

* **Same‑conclusion test.** Do two candidate senses ever lead to **different conclusions** in the canon? If not, merge.
* **Argument‑slot probe.** Replace arguments in canonical sentences; do both candidates still read true? If one fails, split.
* **Label inversion.** Read the Plain label alone: does it tempt you to over‑generalise? If yes, tighten it.
* **Counter‑example ping.** Can you state a **ten‑word** use that the sense must exclude? If you can, write it; if you cannot, your sense may be too broad.
* **Memory rule.** Can you recall the Context’s Local‑Senses **without notes**? If not, you split too finely.

### F.3:10 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in thought                                                            | Why it harms                                            | Remedy (conceptual move)                                                                                          |
| ------- | -------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **A1**  | **String = Sense**         | Treating surface identity (*service*, *SLO*) as sameness of meaning.          | Collapses distinct uses; hides selectional differences. | Compare **selectional frames** and entailments inside the Context; merge only if conclusions never diverge.          |
| **A2**  | **Cross‑context creep**       | Folding BPMN *process* with PROV *activity* while clustering **inside** BPMN. | Imports foreign usage; violates locality.               | Constrain attention to **one context**; postpone Cross‑context talk to F.9.                                             |
| **A3**  | **Over‑granulation**       | Splitting minor orthographic variants (*service‑level‑objective* vs *SLO*).   | Adds friction; no conceptual gain.                      | Consolidate **canon‑blessed aliases** into one Local‑Sense.                                                       |
| **A4**  | **Under‑granulation**      | One sense for incompatible roles (*event* as node‑type vs occurrence).        | Causes contradictory inferences later.                  | Split on **role/entailment** conflict; add a **counter‑example** to sharpen the cut.                              |
| **A5**  | **Imported definitions**   | Borrowing dictionary glosses not used in the canon.                           | Drifts from the Context’s idiom; confuses labels.          | Ground every sense line in **statements the canon actually makes**.                                               |
| **A6**  | **Label drift**            | Tech label in canon idiom; Plain label broadens scope.                        | Teaches the wrong thing; leaks meaning.                 | Keep **Tech** idiomatic; make **Plain** helpful yet strictly **within** the same usage.                           |
| **A7**  | **Behaviour/math leakage** | Sense lines include runtime metrics, deontic rules, type axioms.              | Mixes I/D/S layers; duplicates Part C work.                   | Sense lines are **usage‑only**; no equations, no policies.                                                        |
| **A8**  | **Edition blend**          | Mixing 2011 and 2020 usage under one Local‑Sense.                             | Hidden shifts; brittle bridges later.                   | If usage changed with edition, treat as **different Contexts** (F.1) or distinct Local‑Senses with **edition note**. |
| **A9**  | **Collocate worship**      | Declaring sameness solely from similar nearby words.                          | Correlates ≠ causes; misses entailments.                | Use collocates as **cues**, then decide by **entailment/role** checks.                                            |
| **A10** | **Temporal fudge**         | Treating a design‑time sense as if it were run‑time (or vice versa).          | Category errors at enactment.                           | Respect the Context’s **time stance**; keep senses aligned to *design* or *run* as declared in F.1.                  |


### F.3:11 - Local‑Sense Cards (one‑glance form)

> A **Local‑Sense Card** is a **one‑glance** sketch per sense in a Context. It teaches faster than prose lists and keeps senses crisp.

**Fields (thought‑items, not fields to fill):**

* **Context** (U.BoundedContext, edition)
* **Label pair** — **Tech** (idiomatic) - **Plain** (didactic)
* **Sense line** — one sentence in the Context’s voice
* **Inside** — which F.2 Units it consolidates (names only)
* **Counter‑example** — a short use that must **not** be included


### F.3:12 - Worked examples (all **intra‑Context**)

#### F.3:12.1 - BPMN 2.0 (workflow Context)

**Card A — “process (graph)”**

* **Label**: Tech **process** - Plain **workflow graph**
* **Sense line**: A BPMN **graph of flow nodes and sequence flows** **specifying orchestration among participants** *(design‑time)*.
* **Inside**: *process*, *process model*, *business process* (when used as diagram).
* **Counter‑example**: *“This process took 5 minutes”* ← **runtime** occurrence, **not** this sense.

**Card B — “event (node‑type)”**

* **Label**: Tech **event (node)** - Plain **event symbol**
* **Sense line**: A **node‑type** that marks starts, ends, and intermediates; typed by trigger/result.
* **Inside**: *start event*, *message event*, *end event*.
* **Counter‑example**: *“The outage event happened at 13:05”* ← narrative occurrence, **not** the node‑type.

> **Outcome:** “Process uptime” is rejected as a BPMN sense; Execution belongs to another Context.


#### F.3:12.2 - PROV‑O (provenance Context)

**Card C — “activity (run)”**

* **Label**: Tech **activity** - Plain **time‑bounded execution**
* **Sense line**: An **occurrence** that **uses** and **generates** entities; linked to agents; has start/end.
* **Inside**: *activity*, *execution* (when PROV authors use it).
* **Counter‑example**: *“Sorting algorithm”* ← capability/method, **not** an occurrence.

**Card D — “agent (provenance)”**

* **Label**: Tech **agent** - Plain **provenance actor**
* **Sense line**: Thing that bears **responsibility** for an activity’s effects (person, org, software).
* **Inside**: *agent*.
* **Counter‑example**: *“RBAC role”* ← access status, **not** a PROV agent.


#### F.3:12.3 - ITIL 4 (services Context)

**Card E — “service‑level objective”**

* **Label**: Tech **SLO** - Plain **service target**
* **Sense line**: A **target value/range** for a **service characteristic** used to define acceptable service.
* **Inside**: *service‑level objective*, *SLO*.
* **Counter‑example**: *“Actual availability 99.5%”* ← observation, **not** the target.

**Card F — “incident”**

* **Label**: Tech **incident** - Plain **service disruption**
* **Sense line**: An **unplanned interruption** or reduction in quality of a service.
* **Inside**: *incident*.
* **Counter‑example**: *“Fault in plant sensor”* ← Sys‑CAL fault; different Context.


#### F.3:12.4 - SOSA/SSN (sensing Context)

**Card G — “observation (act)”**

* **Label**: Tech **observation** - Plain **measurement act**
* **Sense line**: An **act** applying a **Procedure** to a **FeatureOfInterest** to yield a **Result** for a property.
* **Inside**: *observation*.
* **Counter‑example**: *“Temperature is 20 °C”* ← **result value**, not the act.


#### F.3:12.5 - OWL 2 (types Context)

**Card H — “subclass‑of”**

* **Label**: Tech **subclass‑of** (⊑) - Plain **is‑a (class)**
* **Sense line**: A **class inclusion**: every instance of **C** is an instance of **D**.
* **Inside**: *SubClassOf*, *is‑a* (when authors use it for classes).
* **Counter‑example**: *rdf\:type* (instance‑of) — not class inclusion.

**Card I — “equivalent‑class”**

* **Label**: Tech **equivalent‑class** - Plain **same class extension**
* **Sense line**: Mutual class identity by extension; two labels for **the same** set of instances.
* **Inside**: *EquivalentClasses*.
* **Counter‑example**: *owl\:sameAs* (individual identity), different predicate.


#### F.3:12.6 - IEC 61131‑3 (control‑runtime Context)

**Card J — “task (runtime)”**

* **Label**: Tech **task** - Plain **program runner**
* **Sense line**: A **cyclic or event‑driven** execution unit that **invokes programs** on schedule or trigger.
* **Inside**: *task*.
* **Counter‑example**: *“Control algorithm”* ← design/method, not the runtime task.


### F.3:13 - Reasoning primitives (judgement schemas, notation‑free)

> Each schema captures a **safe mental move**. It implies no storage, API, or workflow.

1. **Alias‑to‑sense consolidation**
   `Context C ⊢ interchangeable(U₁,…,Uₖ) ⇒ Local‑Sense σ`
   *Reading:* If Units are used interchangeably **by the canon** in **C**, consolidate them into one Local‑Sense **σ**.

2. **Selectional‑frame split**
   `C ⊢ frames(U) = F, frames(V) = G, F ∩ G = ∅ ⇒ split(U,V)`
   *Reading:* In **C**, if the argument/role patterns do not overlap, treat as **different senses**.

3. **Entailment divergence**
   `C ⊢ entail(U) ≠ entail(V) on canonical paraphrases ⇒ split(U,V)`
   *Reading:* If paraphrases lead to **different conclusions** in the canon, split.

4. **Parsimony merge**
   `C ⊢ no‑test distinguishes {U₁,…,Uₖ} ⇒ merge(U₁,…,Uₖ)`
   *Reading:* If no canonical test yields a difference, merge into one sense.

5. **Counter‑example trigger**
   `C ⊢ ∃e: e should not be covered by σ ⇒ refine(σ)`
   *Reading:* A crisp counter‑example forces a narrower sense (split or relabel).

6. **Idiomatic Tech, faithful Plain**
   `C ⊢ labelTech(σ) in idiom(C) ∧ labelPlain(σ) ⊆ usage(σ)`
   *Reading:* Tech label speaks the canon; Plain label does not widen the sense.

7. **SenseCell address**
   `C ⊢ σ ⇒ SenseCell ⟨C,σ⟩`
   *Reading:* Pair each Local‑Sense with its Context to form an address used downstream.

8. **Temporal guard**
   `stance(C)=design ⇒ forbid(run‑claims in σ)` (and symmetrically)
   *Reading:* Sense lines must not cross the Context’s DesignRunTag.

9. **Edition guard**
   `C≠C′ (different editions with usage shift) ⇒ no‑merge(σ@C, τ@C′)`
   *Reading:* Do not merge senses across Contexts when editions shift usage.

10. **Completeness ping (optional)**
    `frequent head w in C ∧ no Local‑Sense on w ⇒ consider(sense for w)`
    *Reading:* If a common head lacks a sense, you may be missing a useful consolidation (within C).


### F.3:14 - Relations

**Builds on:**
F.1 **Domain‑Family Landscape Survey** (Contexts fixed); F.2 **Term Harvesting** (Units ready); E.10.D1 **D.CTX** (Context discipline); A.7 **Strict Distinction**.

**Constrains:**

* **F.4 Role Description.** Role Descriptions **cite SenseCells**; they do **not** invent senses.
* **F.7 Concept‑Set Table.** Rows are built from **SenseCells** (later Cross‑context assembly); intra‑Context clarity here prevents row bloat.
* **F.8 Mint or Reuse Decision.** Decisions compare proposed names to **existing SenseCells** to avoid type inflation.
* **F.9 Alignment & Bridge.** Bridges connect **SenseCell ↔ SenseCell** across Contexts; F.3 provides the stable endpoints.

**Is used by.**
Part C Extention Patterns to ground examples and invariants in **Context‑true** language.


### F.3:15 - Migration notes (conceptual)

1. **Usage clarifies → merge.** If two Local‑Senses never lead to different conclusions in the Context’s canon, **merge** and keep the narrower sense line.
2. **Usage diverges → split.** If new reading reveals incompatible roles/entailments, **split** and attach a counter‑example to each side.
3. **Edition change → new Context.** When a new edition **reframes** usage, treat it as a **separate Context** (F.1) and re‑cluster there.
4. **Label upkeep.** If the Plain label tempts broadening, tighten it; if the Tech label drifts from idiom, restore the canon term.
5. **Dormant sense.** If a Local‑Sense ceases to matter for any active line, leave it listed but mark it **low‑use** in your own notes; do not fold it into another unless rule 1 holds.
6. **Bridge temptation.** Record tensions to bridge **elsewhere**; F.3 never resolves Cross‑context relations.


### F.3:16 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.3:16.1 - Static conformance (SCR)

* **SCR‑F3‑S01 (context‑locality).** Every Local‑Sense is paired with **exactly one context**; no Cross‑context clustering appears.
* **SCR‑F3‑S02 (Label pair).** Each Local‑Sense has **Tech** (idiomatic) and **Plain** (didactic) labels; neither widens usage beyond the sense line.
* **SCR‑F3‑S03 (Sense line fidelity).** Each sense line is **grounded in canonical statements** of the Context; no behaviour/deontic/math content.
* **SCR‑F3‑S04 (Parsimony).** The set of Local‑Senses per Context is small enough to **recall unaided** by a careful mind.
* **SCR‑F3‑S05 (Counter‑example presence).** For any ambiguous head, at least one **counter‑example** is recorded to guard the boundary.
* **SCR‑F3‑S06 (Temporal honesty).** Where the Context has a declared stance, sense lines **respect design/run**.

#### F.3:16.2 - Regression (RSCR)

* **RSCR‑F3‑E01 (Merge soundness).** Every merge is justified by a **failed distinction test** (no selectional or entailment difference).
* **RSCR‑F3‑E02 (Split necessity).** Every split cites a **role/entailment conflict** or a concrete **counter‑example**.
* **RSCR‑F3‑E03 (Edition guard).** No Local‑Sense spans Contexts that differ by edition **with usage shift**.
* **RSCR‑F3‑E04 (Label stability).** Changes to labels do **not** change sense; if they do, the change is treated as a split/merge per E01/E02.
* **RSCR‑F3‑E05 (Downstream continuity).** After splits/merges, **SenseCell** references in F.4/F.7/F.9 remain **referentially clear** (new addresses are explicit; no silent aliasing).


### F.3:17 - Didactic close (60‑second recap)

> **Within one context,** collect how the canon actually **uses** a head, not how we wish it did. **Merge** aliases that never lead to different conclusions; **split** uses that do. Give each consolidated use a crisp **Tech** label in the Context’s idiom and a faithful **Plain** label. The pair *(Context, Local-Sense)* is your **SenseCell**—the address later cited by Role Descriptions, tables, and bridges. No Cross‑context mergers here; that job belongs to F.9. Keep senses few, boundaries sharp, and labels honest.

### F.3:End

## F.4 - Role Description (RCS + RoleStateGraph + Checklists)

**“Name the mask or the badge — and say what it commits to — but only inside a Context.”**
**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **E.10.D2 Intension–Description–Specification Discipline**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering**; A.2.1 **`U.RoleAssignment`**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.5 **Naming Discipline for U.Types & Roles**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge Across Contexts**; B.3 **Trust & Assurance Calculus** (for later status evaluation).
**Aliases (informative).** *Mask/Badge card*; *role card* (plain only).

### F.4:1 - Intent & applicability

**Intent.** Provide a **conceptual template** for two kinds of assignables:

* **Role Template** — a **behavioural mask** that a holder can wear **in a specific Context** (U.BoundedContext), shaping how it **acts** (via Method/Execution relations).
* **Status Template** — an **epistemic or deontic badge** that a holder (or artefact, event, claim) can **bear** inside a Context, shaping how it is **treated** (evaluation, permission, standing).

Each template is **grounded in a SenseCell** `⟨Context, Local‑Sense⟩` from F.3 and declares **minimal invariants** that later **assignments** must satisfy. No Cross‑context meaning is imported here.

**Applicability.** Whenever you need to **speak precisely** about what it means to be *a Participant (BPMN)*, *hold an access‑role (RBAC)*, *be an Incident (ITIL)*, or *carry a Verified status (evidence line)*, before minting U.Types or drawing Cross‑context bridges.

**Non‑goals.** No workflows, no storage, no editors. No equations for assurance or control; those live in Part B/C. This pattern describes **how to think and speak** about assignables — not how to manage files.

### F.4:2 - Problem frame

Without explicit Role Descriptions:

1. **Role/status conflation.** Access **role** (RBAC) treated as behavioural **mask** (BPMN participant); deontic **duty** treated as runtime **effect**.
2. **Context drift.** A “role” quietly starts meaning different things across canons; later assignments contradict each other.
3. **Hidden commitments.** We name a role/status but never state what **must hold** when it is assigned; downstream reasoning becomes arbitrary.
4. **Premature unification.** A single template tries to straddle several Contexts; losses remain implicit.

### F.4:3 - Forces

| Force                         | Tension to resolve                                                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Behaviour vs knowledge**    | A role changes how the holder **acts**; a status changes how the holder is **treated/assessed**. Keep **I/D/S layers** separate (E.10.D2; A.7). |
| **Locality vs reuse**         | We want reusable templates, yet meanings are **context‑local** (E.10.D1, F.1).                                                   |
| **Minimality vs sufficiency** | Invariants must be **few** and **decisive**; too many become pseudo‑procedures.                                              |
| **Didactics vs fidelity**     | A one‑screen card must be **teachable** without betraying the canon.                                                         |


### F.4:4 - Minimal vocabulary (this pattern only)

* **Context** — **U.BoundedContext** (per E.10.D1).
* **Local‑Sense** — a consolidated sense in a Context (F.3).
* **SenseCell** — the address `⟨Context, Local‑Sense⟩`.
* **Role Template** — behavioural mask defined **in** a Context, later bound by **`U.RoleAssignment`**.
* **Status Template** — epistemic/deontic badge defined **in** a Context, later asserted as a **claim** about a holder/artefact.
* **Holder** — the thing that may wear a mask or carry a badge (e.g., a **U.System**, **U.MethodDescription**, **U.Work**, **U.Episteme**).

### F.4:5 - Core idea (didactic)

**A Role Description is a small card that says:**
**(i)** *which Context’s sense it relies on* (**SenseCell**),
**(ii)** *what label we use to speak about it* (Tech & Plain), and
**(iii)** *what must hold* when someone **wears** the mask (Role) or **bears** the badge (Status).

It is **not** a definition by prose alone; it is a **pledge of invariants** — minimal, Context‑true, and later checkable.

### F.4:6 - The Role Description Card (one‑screen sketch)

> Each bullet is a **thought‑item**, not a file field.

**Header**

* **Template kind:** **Role** | **Status**
* **Label pair:** **Tech** (idiomatic) - **Plain** (didactic)  *(naming discipline in F.5)*
* **SenseCell:** `⟨ContextId, Local‑Sense label⟩`

**Applicability**

* **Holder scope:** what can wear/bear it (e.g., *U.System*, *U.Work*, *U.MethodDescription*, *U.Episteme*).
* **Time stance:** **design** / **run** aligned to the Context (F.1).
* **Preconditions (Context‑true):** crisp conditions that must already be true in the Context’s idiom.

**Invariants (minimal)**

* **Behavioural invariants (Role)** *or* **Evaluation invariants (Status)** — 2–5 short lines stating what **must** hold after assignment/assertion, using the Context’s vocabulary and SenseCells where needed.
* **Separation guard:** a one‑line reminder of what this template **does not** imply (prevents senseFamily mixing).

**Consequences (informative)**

* **Typical interactions:** which **Method/Execution/Observation** constructs (by SenseCell) this template usually touches — *names only*.
* **Common misreads (trip‑wire):** 1–2 bullets to prevent known confusions.

> **Memory rule:** If your card can’t be read in **under two minutes**, you are writing a manual, not a template.

**Autonomy hooks (when Role may act autonomously)**
* **RCS additions (illustrative):** `AgencyLevel ∈ {None, Assisted, Delegated, Autonomous}`, `SafetyCriticality ∈ {SC0..SC3}`.
* **RSG gate:** mark which **states are enactable under autonomy** (cf. A.2.5); link to `AutonomyBudgetDeclRef`.
* **References:** If autonomy is claimed for this Role, the Role Description **MUST** reference: `AutonomyBudgetDeclRef` (id, version), `Aut-Guard policy-id (PolicyIdRef)`, `OverrideProtocolRef`.
* **Checklist:** include a **pre‑enactment** checklist item “Autonomy Green‑Gate passed” (guard verdicts present).

### F.4:7 - Normative invariants (template discipline)

1. **context‑local grounding.** Every Role Description **MUST** cite exactly one **SenseCell** as its semantic locus.
2. **I/D/S layer separation.**
   * A **Role Template** **MUST NOT** encode deontic, access, or measurement rules.
   * A **Status Template** **MUST NOT** encode behaviour or control flow.
3. **Time honesty.** The card’s stance (**design/run**) **MUST** match the Context’s stance (F.1).
4. **Minimality.** Invariants **SHOULD** be the **fewest that decide** the assignment; avoid procedural sequences.
5. **No Cross‑context smuggling.** A single card **MUST NOT** import foreign semantics; if two Contexts are needed, the relation is handled later in **F.9**.
6. **Label fidelity.** **Tech** label **MUST** be idiomatic to the Context; **Plain** label **MUST** not widen the sense (F.3).
7. **Binding Standard (roles).** A **Role Template** is the **design‑time mask**; at run‑time, a **`U.RoleAssignment`** creates **System‑in‑Role** instances that are subject to the card’s invariants.
8. **Assertion Standard (statuses).** A **Status Template** is a **badge**; asserting it **commits** to the card’s evaluation invariants and to the Context’s way of checking them (later anchored via SenseCells, not formulas here).

### F.4:8 - Reasoning primitives (judgement schemas, notation‑free)

> Conceptual moves only; no APIs, no data stores.

1. **Template grounding**
   `Template T cites SenseCell ⟨C,σ⟩ ⊢ meaning(T) is local to C`
   *Reading:* The template’s meaning is **context‑local**.

2. **Role assignability**
   `holder h, RoleTemplate T, preconds_T(h) ⊢ assignable(h,T)`
   *Reading:* If the **preconditions** hold for **h**, it is **eligible** to wear the mask **T**.

3. **Role assignment obligation**
   `assignable(h,T) ∧ bind(h,T: C) ⊢ invariants_T(h) must hold`
   *Reading:* Once bound (via **`U.RoleAssignment`**), **h** must satisfy **T**’s behavioural invariants.

4. **Status assertability**
   `StatusTemplate S, evidence_in_C supports S for x ⊢ assertable(x,S)`
   *Reading:* If evidence **in the Context C** supports **S** for **x**, the badge is **assertable** (details of evidence logic live in Part B).

5. **Status consequence**
   `assertable(x,S) ∧ assert(x,S) ⊢ evaluation_invariants_S(x)`
   *Reading:* Once asserted, **S**’s evaluation invariants constrain how **x** is treated.

6. **Separation guard**
   `RoleTemplate T ⊢ not(deontic_implied(T))` - `StatusTemplate S ⊢ not(behaviour_implied(S))`
   *Reading:* Wearing a mask doesn’t grant permissions; carrying a badge doesn’t define behaviour.

7. **Bridge embargo**
   `T cites ⟨C,σ⟩ ∧ C≠C′ ⊢ no‑equivalence(T@C, −) inside F.4`
   *Reading:* No Cross‑context equivalence is asserted here; use **F.9** later.

### F.4:9 - Worked examples (Context‑true)

> Illustrative cards only; names are **tech/plain labels**, not final U.Type IDs (F.5 will govern naming).

#### F.4:9.1 - **Role Template:** *participant (workflow actor)* — Context: **BPMN 2.0 (2011)**

* **Kind:** Role
* **Label:** Tech **participant** - Plain **workflow actor**
* **SenseCell:** `⟨BPMN_2_0, participant (actor in workflow)⟩`
* **Holder scope:** **U.System** (organisation, team, service)
* **Time stance:** **design**
* **Preconditions:** Holder is addressable as a **lane/pool** in the workflow model.
* **Behavioural invariants:**

  1. Activities **assigned to** the participant appear in its lane/pool.
  2. The participant **interacts** through message flows at its boundaries.
  3. The participant **does not** define run‑time occurrence; it **structures** the model.
* **Separation guard:** No permissions implied; no execution logs implied.
* **Typical interactions (informative):** BPMN **process (graph)**; message **event (node)**.
* **Common misreads:** ≠ **RBAC role**; ≠ **PROV Activity**.

#### F.4:9.2 - **Status Template:** *access‑role membership* — Context: **NIST RBAC (2004)**

* **Kind:** Status
* **Label:** Tech **access‑role** - Plain **permission role**
* **SenseCell:** `⟨NIST_RBAC_2004, role (permission grouping)⟩`
* **Holder scope:** **U.System** (user/session)
* **Time stance:** **run**
* **Preconditions:** A defined set of **permissions** exists for the role.
* **Evaluation invariants:**

  1. If **x** carries this badge, **x**’s session inherits exactly the role’s **permissions**.
  2. The badge **does not** describe behaviour in a workflow; it determines **access**.
* **Separation guard:** No commitment about BPMN assignment; no deontic duties.
* **Typical interactions (informative):** **permission**, **session** (RBAC).
* **Common misreads:** ≠ **participant (BPMN)**; ≠ **person** as an ontological type.

#### F.4:9.3 - **Status Template:** *incident (service disruption)* — Context: **ITIL 4 (2020)**

* **Kind:** Status
* **Label:** Tech **incident** - Plain **service disruption**
* **SenseCell:** `⟨ITIL4_2020, incident (service quality drop)⟩`
* **Holder scope:** **U.Work** (recorded occurrence affecting a service)
* **Time stance:** **run**
* **Preconditions:** A **service** exists with declared **SLOs/quality metrics**.
* **Evaluation invariants:**

  1. The occurrence **reduces** service quality below acceptable levels.
  2. It triggers **restoration activities** per service practice (names only).
* **Separation guard:** Not a plant **fault**; not a BPMN **event node**.
* **Typical interactions:** **SLO** (ITIL), **Observation** (SOSA) — names only.
* **Common misreads:** ≠ **problem** (root cause category).

#### F.4:9.4 - **Role Template:** *task runner (control runtime)* — Context: **IEC 61131‑3**

* **Kind:** Role
* **Label:** Tech **task** - Plain **program runner**
* **SenseCell:** `⟨IEC_61131_3, task (runtime execution unit)⟩`
* **Holder scope:** **U.System** (controller CPU/task scheduler)
* **Time stance:** **run**
* **Preconditions:** A program is **registered** for cyclic/event execution.
* **Behavioural invariants:**

  1. Invokes assigned program according to **cycle/trigger**.
  2. Provides **schedule constraints** (period/priority) to its program.
* **Separation guard:** No claim about **deontic** guarantees or **service** targets.
* **Typical interactions:** **Execution** (A.15 family), **Actuation** (Sys‑CAL).
* **Common misreads:** ≠ **workflow task**; ≠ **algorithm** (design).

### F.4:10 - Anti‑patterns & remedies

| #       | Anti‑pattern            | Symptom (in a card)                                                       | Why it harms thinking                                    | Remedy (conceptual move)                                                                                        |
| ------- | ----------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Role⇄Status blur**    | A Role card says “grants permission”; a Status card dictates behaviour.   | **senseFamily mixing (Role vs Status)**; incoherent assignments.              | Move permission talk to a **Status**; keep Role invariants purely behavioural. Add a **separation guard** line. |
| **A2**  | **Pan‑Context template**   | One card cites several canons implicitly (“BPMN/PROV process”).           | Imports meaning across Contexts; hides losses.              | Keep **one SenseCell per card**. If Cross‑context relation is needed, defer to **F.9 Bridge**.                     |
| **A3**  | **Silent time flip**    | Card defined in a **design** Context asserts run‑time facts (or vice versa). | Violates F.1 time stance; produces category errors.      | Align **Time stance** to the Context; relocate run‑facts to status/evidence lines or to another Context.              |
| **A4**  | **Procedural template** | Long “steps” instead of minimal invariants.                               | Becomes a method recipe, not an assignable mask/badge.   | Replace sequences with **decisive invariants** (2–5 lines) that must hold regardless of procedure.              |
| **A5**  | **Permission leakage**  | A BPMN Role claims access rights “by wearing the mask”.                   | Conflates access with behaviour; weakens RBAC semantics. | State explicitly: **no permissions implied**. Bind access via a **Status** in the RBAC Context.                    |
| **A6**  | **Evidence bake‑in**    | Status card encodes metrics/formulas.                                     | Smuggles Part B maths; reduces portability.              | Keep only **evaluation invariants** in Context language; actual checks live in Part B/C via SenseCells.            |
| **A7**  | **Global label**        | Tech label chosen for cross‑discipline appeal (“Actor”) not Context idiom.   | Loses local meaning; harms F.3 clustering.               | Use **Context‑idiomatic Tech label**; provide a Plain label for teaching (F.5 governs labels).                     |
| **A8**  | **Concept inflation**   | Multiple near‑duplicate cards for the same SenseCell.                     | Noise; brittle naming.                                   | Prefer **refinement** (see §11) or a single card with tighter invariants; avoid duplicates.                     |
| **A9**  | **Holder sprawl**       | Holder scope lists unrelated kinds (“U.System or U.Work or U.Episteme”).  | Ambiguity at binding time.                               | Shrink **Holder scope** to the real carriers; if truly different, split cards.                                  |
| **A10** | **Anchor relapse**      | Card talks about “anchors” or “global context.”                           | Re‑introduces banned jargon; confuses D.CTX.             | Replace with **Context** / **SenseCell**; never use “anchor”.                                                      |
| **A11** | **Tooling creep**       | Mentions manifests, pipelines, editors.                                   | Violates E.5 guard‑rails; notational dependency.         | Remove all process/tool talk; keep card **concept‑only**.                                                       |
| **A12** | **Bridge‑by‑label**     | Using identical labels to imply Cross‑context sameness.                      | Stealth equivalence; no loss policy.                     | Labels do not bridge. Any Cross‑context claim goes to **F.9** with a declared CL policy.                           |

### F.4:11 - Concept‑level operators (refinement & compatibility)

> **Judgement schemas** — pure reasoning moves over cards. No APIs, no storage, no workflow.

Let **`sense(T)`** denote the **SenseCell** cited by template **T**.
Let **`inv(T)`** denote the set of **invariants** on T.
Let **`senseFamily(T)`** ∈ {**Role**, **Status**}.
Let **`stance(T)`** ∈ {**design**, **run**} (from the Context).

#### F.4:11.1 - Same‑Context equivalence

**Form.**
`sense(T₁) = sense(T₂) ∧ inv(T₁) ⇔ inv(T₂) ⊢ T₁ ≡ T₂`

**Reading.** Two cards in the **same Context** with logically equivalent invariants **co‑designate** the same assignable.

*Tech cue.* Use this to **merge duplicates** conceptually without changing labels.

#### F.4:11.2 - Refinement (strictness order)

**Form.**
`sense(T₁) = sense(T₂) ∧ inv(T₁) ⇒ inv(T₂) ⊢ T₁ ⪯ T₂`

**Reading.** **T₁** is a **refinement** of **T₂** if its invariants **imply** those of **T₂** (same Context).

*Effects.* Assigning **T₁** automatically satisfies **T₂**; the converse need not hold.

#### F.4:11.3 - Incompatibility (mutual exclusion)

**Form.**
`sense(T₁) = sense(T₂) ∧ (inv(T₁) ∧ inv(T₂) ⇒ ⊥) ⊢ incompatible(T₁,T₂)`

**Reading.** Two cards in the same Context are **mutually exclusive** if their invariants cannot co‑hold.

*Use.* A conceptual **Separation‑of‑Duty** signal without governance.

#### F.4:11.4 - Co‑wearability / co‑bearability

**Form.**
+`senseFamily(T₁)=senseFamily(T₂)=Role ∧ stance(T₁)=stance(T₂) ∧ ¬incompatible(T₁,T₂) ⊢ coWearable(T₁,T₂)`
+`senseFamily(T₁)=senseFamily(T₂)=Status ∧ ¬incompatible(T₁,T₂) ⊢ stackable(T₁,T₂)`

**Reading.** Within a Context, two Roles can be worn together (or two Statuses carried) when they **do not** conflict.

#### F.4:11.5 - Time‑stance alignment

**Form.**
`stance(T)=design ⊢ inv(T) may not assert run‑facts`
`stance(T)=run ⊢ inv(T) may not assert design‑commitments`

**Reading.** Invariants must **respect** the Context’s DesignRunTag (F.1).

#### F.4:11.6 - Binding/Assertion admissibility

**Form. (Roles)**
`holder h ∧ preconds_T(h) ⊢ assignable(h,T)`
`assignable(h,T) ∧ bind(h,T) ⊢ inv(T)(h)`

**Form. (Statuses)**
`evidence_in_Context(C) supports S for x ∧ sense(S)=⟨C,σ⟩ ⊢ assertable(x,S)`
`assertable(x,S) ∧ assert(x,S) ⊢ inv(S)(x)`

**Reading.** Preconditions and evidence **gate** the act of wearing a mask or bearing a badge; once done, **invariants apply**.

### F.4:11.7 - Cross‑context embargo (inside F.4)

**Form.**
`sense(T₁)=⟨C,−⟩, sense(T₂)=⟨C′,−⟩, C≠C′ ⊢ no‑relation(T₁,T₂) here`

**Reading.** **F.4** never asserts Cross‑context relations. If a relation is desired, it becomes a **Bridge** in **F.9**.

### F.4:12 - Relations (where this card sits)

**Builds on:**
E.10.D1 **D.CTX** (Context ≡ U.BoundedContext); F.1 (Contexts cut); F.2 (harvested terms); F.3 (Local‑Sense → **SenseCell**); A.2.1 **`U.RoleAssignment`**; A.7 **Strict Distinction**.

**Constrains:**
**F.5** (Naming): pairs **Tech/Plain** must reflect the **Context idiom** and avoid Cross‑context overreach.
**F.7** (Concept-Set Table): rows reference **SenseCells**; Role Description cards **point to** those rows but never **create** cross-context identity.
**F.8** (Mint or Reuse?): prefer **refinement (⪯)** over new cards; split cards rather than mixing senseFamilies.
**F.9** (Alignment & Bridge): any relation across Contexts is **declared there**; Role Description cards remain context-local.

**Is used by.**
A.15 family (Role–Method–Work alignment) to interpret **System‑in‑Role** and **Work**; Part B evidence/status checks to interpret **evaluation invariants**.

### F.4:13 - Migration notes (conceptual playbook)

1. **Context update (edition split).** If the Context’s Local‑Sense changes, **fork** the card per new SenseCell; keep the old card as historically valid.
2. **Family correction (Role/Status).** If a card mixes behaviour and deontics, **split** into one Role and one Status; move permission language to the Status.
3. **Tighten by refinement.** When practice reveals a stricter understanding, prefer **T′ ⪯ T** over replacing **T**; this preserves existing assignments conceptually.
4. **Rename safely (labels only).** If F.5 revises labels, change **Tech/Plain** wording; **SenseCell** and **invariants** remain untouched.
5. **Scope correction.** If Holder scope was too wide, split into **parallel cards** with disjoint Holder scopes; avoid complex conditional invariants.
6. **Bridge discovery.** Do **not** inject Cross‑context text into cards; record the relation as an **F.9 Bridge** (with CL policy), leaving the cards as they are.

### F.4:14 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.4:14.1 - Static conformance (SCR)

* **SCR‑F4‑S01 (Uni‑Context grounding).** Each card cites **exactly one SenseCell**.
* **SCR‑F4‑S02 (Family honesty).** `senseFamily(T)` is **either** Role **or** Status; invariants match the family; a **separation guard** line is present.
* **SCR‑F4‑S03 (Time honesty).** `stance(T)` matches the Context’s stance; no opposing‑stance claims appear.
* **SCR‑F4‑S04 (Minimality).** Card lists **2–5** invariants; none are procedural step lists.
* **SCR‑F4‑S05 (Label fidelity).** Tech label is **idiomatic to the Context**; Plain label does not widen meaning.
* **SCR‑F4‑S06 (No Cross‑context import).** Invariants reference only the Context’s idiom or other **SenseCells** by **name** (no identity claims).
* **SCR‑F4‑S07 (Holder clarity).** Holder scope is a **single coherent kind** (e.g., `U.System` or `U.Work`), not a grab‑bag.
* **SCR‑F4‑S08 (No tooling/governance).** Card contains **no** mentions of manifests, pipelines, editors, or workflows.

#### F.4:14.2 - Regression (RSCR)

* **RSCR‑F4‑E01 (Edition churn).** When a Context edition changes, existing cards are **not overwritten**; new cards are added per SenseCell.
* **RSCR‑F4‑E02 (Refinement safety).** If **T′ ⪯ T** is introduced, prior usages of **T** remain conceptually valid; no backward contradictions arise.
* **RSCR‑F4‑E03 (senseFamily integrity).** No card changes senseFamily across revisions (Role↔Status) without an explicit **split** noted.
* **RSCR-F4-E04 (Bridge discipline).** After adding an **F.9 Bridge**, Role Description cards remain **unchanged**; cross-context meanings do not seep back into cards.
* **RSCR‑F4‑E05 (Label updates).** Label changes per **F.5** preserve SenseCell and invariants; tests treat them as **renames**, not semantic edits.

### F.4:15 - Didactic distillation (60‑second close)

> A Role Description card is a **Context-true** way to speak about an assignable: a **Role** (behavioural mask) or a **Status** (epistemic/deontic badge).
> Each card names **one SenseCell**, gives a **Tech/Plain** label, states **minimal invariants**, and declares what it **does not** imply.
> Cards never mix **Role/Status senseFamilies** and never cross **I/D/S layers**, never flip time stance, and never import other Contexts.
> Inside one context, you can compare cards by **equivalence** (≡), **refinement** (⪯), **incompatibility**, and **co‑wearability**.
> across Contexts, say nothing in the card; use a **Bridge** later.
> Keep cards **one‑screen simple**: enough to decide assignments; nothing procedural; no tools; just clear thought.

### F.4:End

## F.5 - Naming Discipline for U.Types & Roles

**Status.** Definitional pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **E.10.D2 Intension–Description–Specification (I/D/S)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description Definition**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; F.0.1 **context‑local Lexicon Principle (RLP)**.
**Coordinates with.** F.7 **Concept‑Set Table**; F.8 **Mint or Reuse?**; F.9 **Alignment & Bridge**; F.13 **Term Registry & Deprecation**.
**Aliases (informative).** *Context‑true naming*; *Two‑register labels*.


### F.5:1 - Intent & applicability

**Intent.** Provide a **small, normative code of naming** so that **U.Types** (Cross‑context categories) and **Role Descriptions** (context‑local Roles/Statuses) are labelled **clearly, locally faithful, and globally stable**, without importing tooling, workflows, or editorial process. Names are **consequences of meaning** fixed earlier (F.1–F.4), not badges invented to “stabilise” drifting words.

**Applicability.** Use **whenever** you (a) mint or revise a **U.Type** name from a **Concept‑Set row** (F.7), or (b) assign labels to a **Role Description** (F.4). This pattern governs **what a good name must be**, not *how a team produces it*.

**Non‑goals.** No registries, reviews, or hand‑offs. No style‑police for punctuation beyond conceptual clarity. No bridging or synonym decisions across Contexts (F.9 does that).


### F.5:2 - Problem frame

Naming errors cause structural errors:

1. **Context denial.** A label hides its Context, inviting Cross‑context misuse (*“process”* used for both BPMN and PROV senses).
2. **senseFamily blur.** Names conflate **Role** (behavioural mask) with **Status** (epistemic/deontic badge).
3. **Over‑reach.** U.Types inherit jargon from one canon and sound global while being parochial.
4. **Under-reach.** Role Description labels sound so generic that they pretend to be U.Types.
5. **Unstable synonyms.** Labels drift to placate readers rather than reflect meaning fixed in SenseCells.

This code resolves these by **Context fidelity**, **senseFamily‑aware morphology**, and **two‑register pedagogy**.


### F.5:3 - Minimal vocabulary (this pattern only)

* **Tech label** — the **Context‑idiomatic** name engineers expect *inside that Context*.
* **Plain label** — a **teaching gloss** in simple English that does **not broaden** the sense.
* **Symbolic alias** *(optional)* — conventional symbol if the canon uses one (e.g., “≤”).
* **SenseCell** — the **(Context × Local-Sense)** address cited by a Role Description card (F.3–F.4).
* **Concept‑Set row** — the Cross‑context table row that supports minting a **U.Type** name (F.7).


### F.5:4 - Core idea (didactic)

> **Name what the invariants already make true.**
>
> For Role Descriptions, **speak like the Context** (Tech), then **teach it** (Plain).
> For U.Types, **speak like nobody’s Context**: pick the **neutral, minimal‑generality** label that best fits the **intersection** shown by your Concept‑Set row.


### F.5:5 - Normative rules — Role Descriptions (context‑local labels)

Let **T** be a Role Description in Context **C** with SenseCell `sense(T)=⟨C,σ⟩`.

**R‑RD‑1 (Two registers).** Provide **both**:
`Tech(T)` = the **Context‑idiomatic** phrase (exact canon wording if possible).
`Plain(T)` = a brief, neutral explanation *that does not broaden meaning*.
*Symbolic alias* is optional and purely informative.

**R‑RD‑2 (No Context tags in labels).** Do **not** embed the Context name in the label (avoid “(BPMN)” in the label itself). Context is already carried by the **SenseCell**; keep labels clean.

**R‑RD‑3 (senseFamily‑aware morphology).**
— **Role** names are **countable nouns** for masks (e.g., *Participant*, *Operator*, *Reviewer*). Avoid verbs and gerunds. Add the suffix **“Role”** **only** if the Context idiom risks confusion with a substance or a status (e.g., *“Reviewer Role”* in a Context that also has a *“Reviewer Status”*).
— **Status** names are **state nouns** or **adjectival‑noun collocations** (e.g., *Approved*, *Compliant*, *In‑Service*, *Access Role* (RBAC)). If a family of levels exists, encode the **level** (`Assurance L1`, `Readiness L2`) rather than inventing decorative adjectives.

**R‑RD‑4 (Local idiom first).** Prefer the **canon’s term of art** even if it sounds narrower than a cross‑discipline cliché. The Plain label handles pedagogy; the Tech label honours the Context.

**R‑RD‑5 (Minimal generality).** Choose the **narrowest label** whose invariants you actually assert. Do **not** “upgrade” *Task* to *Activity* or *Process* just to sound universal.

**R‑RD‑6 (No permissions by stealth).** Role labels **must not** imply entitlement (*“Privileged Operator”* is a Status+Role mashup). Keep deontics in **Status** names in the **deontics Context**.

**R‑RD‑7 (Edition‑neutral labels).** Do **not** bake edition/profile into labels. Edition lives in the **Context**; the card binds to a SenseCell that already encodes edition where needed.

**R‑RD‑8 (Short and stable).** Favour **1–3 words**. Avoid rhetorical adjectives (*“robust, optimal, best‑practice”*).


### F.5:6 - Normative rules — U.Types (Cross‑context labels)

Let **U** be a U.Type minted from a **Concept‑Set row** (F.7) satisfying A.8 (≥3 domain families) AND MinInterFamilyDistance ≥ δ_family (from F1‑Card).

+**R‑UT‑1 (Witnessed neutrality).** The Tech label **must not** be a term owned by one context when alternatives exist. Prefer **discipline‑neutral head nouns** (*Result, Reading, Execution, Evidence, Requirement, State, Type Node*). **Use** *Characteristic/Scale/Value/Level/Coordinate/Score/ScoringMethod* **only** when the U.Type denotes a **measurement‑sense** kind anchored in a declared **CharacteristicSpace**; otherwise avoid these measurement‑canon terms to prevent semantics bleed.

**R‑UT‑2 (Minimal generality).** Name the **least upper sense** that all row witnesses share. If *Observation* and *Measurement* disagree, perhaps the U.Type is **Result** or **Reading**, not **Observation**.

**R‑UT‑3 (No senseFamily mixing in names).** Do **not** name a U.Type with deontic or behavioural language (*“PermittedService”*, *“ResponsibleAgent”*). **Role/Status/Method/Execution** belong to **Role Descriptions (F.4)** or local senses; U.Types are *what‑it‑is* kinds, not *what‑it‑does* or *what‑is‑allowed*.

**R‑UT‑4 (Head–modifier discipline).** Prefer **head nouns** with **light modifiers** over stacked compounds.
Good: *Evidence Status*, *Requirement Status*, *Type Node*.
Risky: *Multi‑stage‑workflow‑execution‑record* (compresses a scenario into a name).

**R‑UT‑5 (No Context tags in names).** U.Types are **Context‑agnostic**; never append “(BPMN)”/“(PROV)”. Provenance for the row lives in F.7, not in the name.

**R‑UT‑6 (Alias only for pedagogy).** Allow **Plain aliases** for teaching; **Tech label** is unique and stable. Synonym management belongs to **F.13**; do not invent alternates ad hoc.

**R‑UT‑7 (Family coherence).** When minting a **family**, use **parallel shapes** (*… Status*, *… Level*, *… Characteristic* **only for measurement families with a declared CharacteristicSpace**) so related U.Types signal relation by form.

**R‑UT‑8 (Symbolic names sparingly).** Symbols may be listed as *aliases* for readers of formal sections; they are **never** the U.Type’s Tech label.

**R‑UT‑9 (No edition/version in name).** Versions live in the Concept‑Set evidence; the name denotes a **time‑robust kind**.


### F.5:7 - Twin rules

**Mandatory Tech name.** Every `U.Type`/Role **MUST** declare a Tech name; plain twin is optional.
**Role suffix invariant.** Role Tech names **MUST** end with `Role`; plain twin **MUST** keep “(role)” on first use.
**No head elision.** Head terms **MUST NOT** be dropped in a way that changes expected Kind (e.g., _“Approval”_ ≠ _“Approver (role)”_).
**One twin, one context.** At most one plain twin per Context; register in **E.10.P**.


### F.5:8 - Invariants (normative, lightweight)

**INV-F5-1 (Pair).** Every Role Description card and every U.Type **MUST** carry **Tech** and **Plain** labels; symbol is optional and informative.

**INV-F5-2 (Context fidelity for Role Descriptions).** `Tech(T)` **MUST** be idiomatic for its Context; `Plain(T)` **MUST NOT** broaden `sense(T)`.

**INV‑F5‑3 (Neutrality for U.Types).** `Tech(U)` **MUST** be discipline‑neutral with respect to the witness Contexts in its Concept‑Set row.

**INV‑F5‑4 (senseFamily honesty).** Role Description **Role** labels are **behavioural masks**; Role Description **Status** labels are **states/badges**; neither sneaks in the other senseFamily.

**INV‑F5‑5 (Minimality).** Labels **MUST** reflect the **minimal generality** supported by invariants (F.4 for Role Description, F.7 for U.Types).

**INV-F5-6 (No Context tags).** Names **MUST NOT** embed Context/edition tags; that information resides in SenseCells (Role Description) and Concept-Set rows (U.Types).


### F.5:9 - Reasoning primitives (judgement schemas, notation‑free)

> Pure mental checks; no tools implied.

1. **Context-idiom check (Role Description).**
   `T in Context C ⊢ idiomatic(Tech(T), C)`
   *Reading:* The Tech label reads like the Context’s own term of art.

2. **Plain‑safety check.**
   `sense(T)=⟨C,σ⟩ ⊢ ¬broadens(Plain(T), σ)`
   *Reading:* The Plain label explains without enlarging the sense.

3. **Neutral‑witness check (U.Type).**
   `witnessContexts(U)=R ⊢ neutral(Tech(U), R)`
   *Reading:* The Tech label doesn’t privilege one witness Context’s jargon.

4. **senseFamily form check (Role Description).**
  `senseFamily(T)=Role ⊢ nounMask(Tech(T))`
  `senseFamily(T)=Status ⊢ stateForm(Tech(T))`
   *Reading:* The morphology matches the senseFamily.

5. **Minimality proof.**
  `inv(T) ⇒ nameScope(Tech(T)) ⊆ senseScope(sense(T))` (Role Description)
   `rowWitnesses(U) ⇒ nameScope(Tech(U)) ⊆ intersectionScope(row)` (U.Type)
   *Reading:* The name’s scope is **no wider** than what the invariants/witnesses support.

6. **Collision ping.**
  `similar(Tech(X), Tech(Y)) ∧ senseFamily(X)≠senseFamily(Y) ⊢ requireDisambiguatorOrSplit`
  *Reading:* If two labels nearly coincide across senseFamilies, either add a **minimal** disambiguator (Role Description only, within Context idiom) or split concepts.


### F.5:10 - Micro‑examples (illustrative)

**Role Description (BPMN Context).**
Tech: **Participant** - Plain: *actor in a workflow* - senseFamily: **Role**
(*No “BPMN” in label; behaviour mask, not entitlement.*)

**Role Description (RBAC Context).**
Tech: **Access Role** - Plain: *named permission set* - senseFamily: **Status**
(*Deontic badge; not a behavioural mask.*)

**Role Description (ITIL Context).**
Tech: **Service‑Level Objective** - Plain: *service target value* - senseFamily: **Status**
(*Levelable family: SLO \[target], SLI \[indicator] handled in F.10/F.12 semantics, not in the label.*)

**U.Type (from Concept‑Set row: SOSA Observation, PROV Activity (result‑bearing), ML Metric Reading).**
Tech: **Result** - Plain: *the produced value or record of a measurement/assessment*
(*Neutral head noun when “Observation” is too Context‑coloured.*)

**U.Type (from OWL class, FCA concept, taxonomy nodes).**
Tech: **Type Node** - Plain: *a node in a type hierarchy or lattice*
(*Neutral across DL and FCA.)*

### F.5:11 - Anti‑patterns & remedies

| #       | Anti‑pattern                | Symptom in labels                                                  | Why it harms thinking                                              | Remedy (rule‑backref)                                                                                               |
| ------- | --------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Context tag leakage**        | `Participant (BPMN)`, `Activity (PROV)` baked into the label       | Labels pretend to carry provenance; duplicates appear across Contexts | **No Context tags in names.** Context is in the SenseCell / Concept‑Set, not the label. (R‑RD‑2, R‑UT‑5)                 |
| **A2**  | **Globalised jargon**       | U.Type named `Observation` because SOSA uses it                    | Privileges one context; misleads DL/FCA readers                       | Pick neutral **head noun** (e.g., `Result`, `Reading`) when witnesses diverge. (R‑UT‑1, R‑UT‑2)                     |
| **A3**  | **senseFamily mixing**      | `Privileged Operator`, `Compliant Reviewer Role`                   | Role + deontic Status fused; category error                        | Keep **Role** nouns for masks; put deontics in **Status** names, often in a deontics Context. (R‑RD‑3, R‑RD‑6)       |
| **A4**  | **Verbified roles**         | `Observing`, `Controlling`, `Approving` as Role names              | Action words hide mask semantics; temporal confusion               | Use **countable nouns** for Roles: `Observer`, `Controller`, `Approver`. (R‑RD‑3)                                  |
| **A5**  | **Edition coding**          | `SLO‑v4`, `Task‑IEC61131`                                          | Names fossilise an edition; brittle across time                    | Edition belongs to the **Context**; keep labels edition‑neutral. (R‑RD‑7, R‑UT‑9)                                     |
| **A6**  | **Over-reach**              | Role Description `Activity` for a BPMN task, U.Type `Process` for run-time acts | Label outruns invariants; invites cross-context misuse                | Choose **minimal generality** that the invariants actually support. (R-RD-5, R-UT-2, INV-F5-5) |
| **A7**  | **Under‑reach / vagueness** | `Item`, `Thing`, `Record` for specific kins                        | No discriminative power; weak teaching                             | Prefer **discipline‑neutral yet informative** heads (`Type Node`, `Result`, `Requirement Status`). (R‑UT‑1, R‑UT‑4) |
| **A8**  | **Symbol as name**          | U.Type named `λ` or `≤`                                            | Unsearchable; Context‑coloured conventions                            | Keep symbols **only as aliases**; Tech label is words. (R‑UT‑8)                                                     |
| **A9**  | **Synonym spray**           | Multiple Tech labels for one U.Type                                | Fragmentation; alias drift                                         | One **Tech** label; further surface forms live in the **registry** (F.13). (R‑UT‑6, INV‑F5‑1)                       |
| **A10** | **Compound overgrowth**     | `multi‑stage‑workflow‑execution‑record`                            | Encodes scenario in a name; unreadable                             | Use **head + light modifier**: `Execution Record` (if that is the U.Type at all). (R‑UT‑4)                          |
| **A11** | **Context-idiom denial**       | Role Description in BPMN named `Actor` (imported from other Contexts) | Readers misapply foreign semantics                                 | Use the **Context’s term of art** in the Tech label; teach via Plain label. (R-RD-4) |
| **A12** | **Status as event**         | `Approval` status labelled `Approve`                               | Morphology hides state vs act                                      | Status labels are **state nouns** / **adjectival‑noun collocations**: `Approved`, `In Service`. (R‑RD‑3)           |
| **A13** | **Bracketed twins**         | `Participant/Agent`, `Service/SLO` as single label                 | Two senses slipped into one card                                   | Pick **one** label per concept; the other lives as alias (F.13) or as a different card. (INV‑F5‑1, R‑UT‑6)          |
| **A14** | **Family drift**            | `Assurance Rank`, `Assurance Tier`, `Readiness Level` mixed        | Readers fail to see relatedness                                    | Keep **family shape** parallel: `… Level`, `… Status`. (R‑UT‑7)                                                     |
| **A15** | **Decorative adjectives**   | `Robust Process`, `Best‑practice Method`                           | Marketing words displace semantics                                 | Drop rhetoric; name the **kind**, not its quality. (R‑RD‑8)                                                        |


### F.5:12 - Worked examples

> Each example shows the **reasoning move** that leads to the label; no procedures, no tooling.

#### F.5:12.1 - Role Description labels (context-local)

**(a) BPMN Context — behavioural mask vs node word**

* **SenseCell.** ⟨*BPMN 2.0*, local‑sense: lane/pool actor that enacts tasks⟩
* **Decision.** Tech = **Participant** (Context idiom); Plain = *actor in a workflow*
* **Why.** `Participant` is the mask; it is **not** the node (*Task*, *Event*). (R-RD-3, R-RD-4)

**(b) RBAC Context — deontic badge**

* **SenseCell.** ⟨*NIST RBAC*, local‑sense: named permission set assigned to sessions⟩
* **Decision.** Tech = **Access Role**; Plain = *named permission set*
* **Why.** It’s a **Status**, not a behavioural mask; deontic plane kept explicit. (R-RD-3, R-RD-6)

**(c) ITIL Context — service target**

* **SenseCell.** ⟨*ITIL 4*, local‑sense: target value for a service characteristic⟩
* **Decision.** Tech = **Service‑Level Objective**; Plain = *service target value*
* **Why.** Family will carry `… Level`, `… Indicator` in adjacent cards; avoids jargon drift. (R-RD-3, R-UT-7)

**(d) IEC 61131-3 Context — run-time execution notion as Role Description?**

* **SenseCell.** ⟨*IEC 61131‑3*, local‑sense: cyclic/event‑driven task unit⟩
* **Decision.** For a Role Description **Status** of a run, label **Completed**, **Failed**, **Skipped** (Context idiom); avoid naming the **Work** itself here.
* **Why.** The *record of work* is a **U.Type** elsewhere (A.15.1); Role Description in this Context carries **badges** of runs. (A.7 stance split; R-RD-3)

#### F.5:12.2 - U.Type labels (from Concept‑Set rows)

**Row R₁ (measurement‑sense):**
SOSA: *Observation* • ML practice: *metric reading* • Metrology: *measurement result*

* **Witness Contexts.** sensing; ML metrics; metrology
* **Decision.** U.Type Tech = **Result**; Plain = *the produced value or record of a measurement/assessment*
* **Why.** Neutral head noun covering all witnesses; avoids privileging SOSA’s *Observation*. (R‑UT‑1, R‑UT‑2)

**Row R₂ (type‑structure):**
OWL: *class* / *subclass* • FCA: *formal concept* (node in concept lattice)

* **Witness Contexts.** DL; FCA
* **Decision.** U.Type Tech = **Type Node**; Plain = *a node in a type hierarchy or lattice*
* **Why.** Neutral over DL vs FCA; head‑modifier shape is stable. (R‑UT‑1, R‑UT‑4, R‑UT‑7)

**Row R₃ (status family):**
ITIL: *incident status* • Safety cert.: *assurance level* • QA: *readiness level*

* **Witness Contexts.** services; assurance; QA
* **Decision.** Two U.Types: **Assurance Level**, **Readiness Level** (family‑coherent), plus **Requirement Status** (for normative clauses)
* **Why.** Separates families; preserves level vs status distinction. (R‑UT‑7, R‑UT‑3)


#### F.5:12.3 - Mixed scenario (service acceptance over execution traces)

**Contexts in play.** IEC 61131‑3 (run), SOSA/SSN (sensing), ITIL 4 (services).

1. **Role Description (ITIL)** — Tech: **Service-Level Objective**; Plain: *service target value*.
2. **U.Type (from R₁)** — Tech: **Result** (to host measured values).
3. **Role Description (IEC)** — Tech: **Completed** / **Failed** (Status on a run).
4. **Name discipline payoff.** The sentence “*Compare IEC run **Results** against the ITIL **Service‑Level Objective***” is Context‑true without tags, because each label encodes its **senseFamily** and neutrality.


### F.5:13 - Migration notes (conceptual)

1. **When a Context changes edition.** Names stay; the **SenseCell** shifts to the new edition. Only change a label if the **sense** has changed; then **split** the card rather than mutate the name. (INV‑F5‑2, R‑RD‑7)

2. **When a Concept‑Set row gains a new witness Context.** Re‑ask neutrality: if the Tech label now privileges a Context, **refactor to a more neutral head** (e.g., `Observation` → `Result`). (R‑UT‑1, R‑UT‑2)

3. **Collision emergence.** If a **Role card** and a **Status card** converge phonetically (`Approver` vs `Approved`), keep both but add the **minimal morphological disambiguator** only where the Context idiom demands it (`Reviewer Role`). (R-RD-3)

4. **Family hygiene.** As families grow, keep **parallel shapes** (`… Level`, `… Status`). If a legacy label breaks shape, add a **Plain alias** for teaching; don’t rename the Tech label without Concept‑Set pressure. (R‑UT‑7, R‑UT‑6)

5. **Language variants.** Non-English canons keep **their own Tech labels** (idiomatic in that Context); the **Plain** label remains English in FPF unless the Part mandates localisation. (R-RD-4, INV-F5-1)

6. **Symbol addition.** You may add a **symbolic alias** later for readers of formal sections; never promote a symbol to the Tech label. (R‑UT‑8)

7. **De‑jargonising the Plain label.** If readers stumble, adjust **Plain** wording only; do **not** widen the sense. (Plain‑safety check)

8. **Deprecation path.** If a label must change, publish the **new Tech + Plain**, keep the old as an **alias** in the registry (F.13), and leave the reasoning trail in the Concept‑Set row that forced the rename. (R‑UT‑6, F.13 linkage)

### F.5:14 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.5:14.1 - Static conformance (SCR)

* **SCR-F5-S01 (Two registers).** Every Role Description card and U.Type **has both** Tech and Plain labels; any symbol is marked **alias**.
* **SCR-F5-S02 (Context fidelity for Role Descriptions).** For any Role Description `T` in Context `C`, `Tech(T)` appears idiomatic **in C**; `Plain(T)` does **not** broaden `sense(T)`.
* **SCR‑F5‑S03 (Neutrality for U.Types).** For any U.Type `U`, its Tech label does **not** coincide with a witness Context’s proprietary term when alternatives exist.
* **SCR‑F5‑S04 (senseFamily morphology).** Role labels are **countable nouns**; Status labels are **state nouns** / adjectival‑noun forms.
* **SCR-F5-S05 (Minimal generality).** For each label, there exists a reading where the **name’s scope ⊆ invariant scope** (Role Description) or **⊆ row intersection** (U.Type).
* **SCR‑F5‑S06 (No Context tags).** No label embeds Context or edition strings.
* **SCR‑F5‑S07 (Family coherence).** Families that claim parity (e.g., Levels) show **parallel shapes** across members.

#### F.5:14.2 - Regression checks (RSCR)

* **RSCR‑F5‑E01 (Witness drift).** When a Concept‑Set row gains/removes a witness Context, re‑evaluate **neutrality**; if violated, refactor the Tech label to a more neutral head.
* **RSCR-F5-E02 (Edition churn).** When a Context updates, Role Description labels remain stable unless the **sense** changed; if sense changed, **split** the card and keep aliases in F.13.
* **RSCR‑F5‑E03 (Collision guard).** If two labels become confusable across **senseFamilies**, either add the **minimal** disambiguator (Role Description only, Context‑idiom) or separate the concepts.
* **RSCR‑F5‑E04 (Rhetoric creep).** Periodic skim for decorative adjectives; remove them unless they encode formal levels or families.

### F.5:15 - Didactic distillation (60‑second recap)

> **Name what is already true.**
> Role Description labels **speak like the Context** (Tech) and **teach without widening** (Plain).
> U.Type labels **speak like nobody’s Context**: neutral head nouns at **minimal generality**, shaped in **parallel families**.
> **Never** glue Context tags or editions into names. **Never** mix senseFamilies in morphology.
> If witnesses change, reconsider neutrality; if senses split, **split names**, don’t stretch them.
> The label is the **last step of understanding**, not the first.


### F.5:End

## F.6 - Role Assignment & Enactment Cycle (Six-Step)

**“Assign only what you can later justify by local meaning and observable facts.”**
**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**.
**Coordinates with.** F.7 **Concept‑Set Table**; F.8 **Mint or Reuse?**; F.9 **Alignment & Bridge**; F.10 **Epistemic Status Mapping**; A.2.1 **U.RoleAssignment**; A.15.\* **Role–Method–Work alignment**; KD‑CAL (observations, results).
**Aliases (informative).** *Assign-and-verify mental loop*; *six-step role cycle*.

### F.6:1 - Intent & applicability

**Intent.** Provide a **minimal set of reasoning moves** that turn a **Role Description** (F.4), anchored in a **SenseCell**, into a **sound claim** about a concrete **holder**—either a **Role assignment** or a **Status assertion**—with **local meaning** (within one context) and a **clear path to evidence** (KD‑CAL). These are **mental moves**, not workflows or tools.

**Applicability.** Any time you (a) bind a system to a **Role** mask, or (b) assert a **Status** about a system/artefact, **inside one U.BoundedContext**. Use when drafting models, reconciling vocabularies, or reading external canons.

**Non‑goals.** No process charts, no registries, no governance roles. No Cross‑context equivalences (that is F.9). No operational runbooks—only conceptual judgements.

### F.6:2 - Problem frame

Without disciplined Role Assignment & Enactment reasoning:

1. **Sense‑family slippage.** Behavioural **Roles** and deontic/epistemic **Statuses** get mixed (keep them on distinct **senseFamilies**, per F.0.1).
2. **Context drift.** A label is lifted from one canon and used as if universal.
3. **Evidence vacuum.** Assignments are asserted with no thought to what could **show** they hold.
4. **Time blur.** Design‑time masks are judged by run‑time traces (or vice versa).
5. **Name inflation.** New labels are minted to patch noisy assignments.

### F.6:3 - Forces

| Force                       | Tension to resolve                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------ |
| **Locality vs reuse**       | Keep meaning inside one context while still naming things once across examples.         |
| **Clarity vs completeness** | State enough to be checkable without burying the reader in conditions.               |
| **Design vs run**           | Keep **stance** coherent: design‑time bindings are judged by design artefacts; if you need run‑time verification, express it as a **run‑Status/Role** Template—without confusing **stances** (A.7). |
| **Fact vs promise**         | Evidence (KD‑CAL) vs deontic expectations (service, policy) must not collapse.       |

### F.6:4 - Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell σ** — **address** **⟨Context C × Local‑Sense ℓ⟩** per F.3. (Informative: we write simply **σ**; it already contains **C**.)
* **Role Description** — a **Role** or **Status** card anchored in a SenseCell (F.4).
* **Holder** — the concrete system/artefact considered for a **Role** binding.
* **Subject** — the referent of a **Status** assertion; determined by the Template (may or may not be the Holder).
* **subject_of(τ, H)** — function yielding the **Subject** for Status assertions given Template **τ** (and, if needed, candidate **H**).
* **Eligibility** — conditions on the Holder that *must* hold to apply the Template (F.4 invariants).
* **Window** — the DesignRunTag or interval relevant to the claim (design/run; instant/period).
* **Evidence shape** — the **Observation/Result/Procedure/Feature** pattern (KD‑CAL) that could confirm/refute the claim in its Context.

### F.6:5 - Pre‑conditions (lightweight)

1. The **Context** is in your F.1 cut; **Context ≡ U.BoundedContext**.
2. The **Template** references a **SenseCell** in that Context (F.4).
3. The **Holder** is identified (by type or instance) without relying on Cross‑context mappings.

### F.6:6 - The six moves (judgement schemas, notation‑free)

Each move is a **thought you can justify**, expressed as `premises ⊢ conclusion`.
All moves are **context‑local** and **side‑effect free** (they assert knowledge; they do not modify artefacts).

#### F.6:6.1 - M1 - Locate — *Fix the Context and the Template*

**Form.**
`Template τ anchored at SenseCell σ≡⟨C, ℓ⟩ ⊢ address(τ) = σ`

**Reading.** Name the Context and the exact SenseCell that gives **local meaning** to the Template.
**Note.** This forbids “floating” Roles/Statuses and prevents Context drift.

#### F.6:6.2 - M2 - Stance — *Respect DesignRunTag*

**Form.**
`stance(C)=s ∧ stance(τ)∈{s, both} ⊢ compatible_stance(τ,C)`

**Reading.** The Template’s DesignRunTag is **compatible** with its Context’s stance (design vs run).
**Note.** Guards against judging a design‑mask by run‑traces or judging a run‑status by design artefacts.

#### F.6:6.3 - M3 - Qualify — *Check Holder eligibility*

**Form.**
`Holder H ∧ eligibility(τ) holds in C ⊢ eligible(H, τ @ C)`

**Reading.** Given the Template’s eligibility predicates (F.4), the Holder qualifies to be bound/assessed **in this Context**.
**Note.** Typical predicates: **type membership**, **capability present**, **scope fit**; all context‑local.

#### F.6:6.4 - M4 - Bind/Assert — *Make the Role Assignment / Status claim*

**Role assignment (behavioural mask).**
`eligible(H, τ @ C) ∧ window W ⊢ plays_role(H, τ : C) @ W`

**Status assertion (epistemic/deontic state).**
`eligible(H, τ @ C) ∧ window W ∧ S = subject_of(τ, H) ⊢ has_status(S, τ : C) @ W`

**Reading.** Assert either a **Role** binding or a **Status** about the appropriate subject (system, artefact, service), within a **Window**.
**Note.** The **subject** of a Status may differ from the Role holder (e.g., a *service* has SLO status; a *team* plays a Role).

#### F.6:6.5 - M5 - Evidence — *Shape what would make it true/false*

**Form.**
`plays_role/has_status κ in C ⊢ evidence_shape(κ) = Σ(C)`

**Reading.** From the Context’s semantics, state the **Observation/Result** pattern (KD‑CAL) that would confirm or refute the claim (**what**, **where**, **when**).
**Note.** This is not an execution plan: it is a **conceptual test** tied to the Context’s vocabulary.

#### F.6:6.6 - M6 - Conclude — *Issue a defensible verdict with confidence*

**Form.**
`evidence E fits Σ(C) ∧ invariants(τ) hold ⊢ holds(κ) with confidence γ ∈ [0,1]`

**Reading.** If observed facts match the expected evidence shape and Template invariants stand, the assignment/status claim **holds** with some confidence (cf. B.3).
**Note.** Confidence combines measurement adequacy (KD‑CAL) with any Context‑specific uncertainty; no Cross‑context boost is implied.

#### F.6:6.7 - Autonomy admission (Green‑Gate) and ledger
* **Before enactment:** If the Method step lists `requiresAutonomyBudget`, the enacting `U.RoleAssignment` **MUST** pass the **Autonomy Green‑Gate**: (i) active/enactable RSG state, (ii) budget tokens/envelope remain in the declared **Γ_time** window, (iii) all guards `pass`.
* **On enactment:** Write an **AutonomyLedgerEntry** attached to the `U.Work`, with deltas and guard verdicts.
* **On depletion:** Block further autonomy‑gated steps; emit a **DepletionNotice** (SpeechAct) and follow the `OverrideProtocolRef`.
* **SoD:** Enforce `⊥` between autonomy consumer Role and override caller Role.

### F.6:7 - Core invariants (normative)

1. **Locality.** Every judgement is **about one context**. No Cross‑context equivalence is presumed or implied (that is F.9’s remit).
2. **Strict splits.** (**a**) **senseFamily split:** **Role** ≠ **Status** (per F.0.1); (**b**) **stance split:** **design** ≠ **run** (A.7). Each judgement names its **senseFamily** and **stance**.
3. **Eligibility before claim.** No binding or status without **eligible(H, τ @ C)**.
4. **Window honesty.** Every claim states or inherits a **Window** consistent with `stance(τ)` and `stance(C)`.
5. **Evidence‑ability.** Every claim must admit at least one **evidence shape** Σ in its Context (KD‑CAL compatible).
6. **Name discipline.** Labels used in judgements follow F.5 (Tech/Plain registers; no Context tags inside names).

### F.6:8 - Reasoning aides (didactic)

* **Context‑prefix speech.** Think and speak with the **Context prefix** when ambiguity lurks: *participant (BPMN)*, *role (RBAC)*, *activity (PROV)*.
* **Window templates.** Prefer short phrases: *“during release‑R3 cutover”*, *“for the Q3 service period”*, *“at 2025‑08‑12T14:30Z”*.
* **Evidence as shape words.** *Result of Observation of ⟨Characteristic⟩ on ⟨Feature⟩ by ⟨Procedure⟩ within W*—not a measurement script.  

**“Assign only what you can later justify by local meaning and observable facts.”**

### F.6:9 - Anti‑patterns & remedies

| #         | Anti‑pattern                   | Symptom                                                                                     | Why it harms reasoning                                                     | Remedy (conceptual move)                                                                                                     |
| --------- | ------------------------------ | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **AP-1**  | **cross-context Binding**      | A single binding/assertion mixes two Contexts (status/role in C₁ justified by semantics in C₂) without an explicit Bridge. | Violates **Locality**; smuggles a Bridge (kind/CL/Loss) into the claim, making it hard to replay and easy to treat as free substitution. | Re-formulate strictly in one context. If cross-context support is essential, defer to **F.9 Bridge** and keep the assignment/status claim local. |
| **AP‑2**  | **Role/Status Conflation**     | “Operator” modeled as a deontic grant; “SLO met” modeled as a Role.                         | Collapses **behavioural mask** and **epistemic/deontic state** (A.7).      | Re‑type the Template: **Role** for “can/does”, **Status** for “is/has (as a claim)”. Use **M4** accordingly.                 |
| **AP‑3**  | **Window‑less Claims**         | Binding/assertion with no time stance or interval.                                          | Uncheckable; invites retrospective reinterpretation.                       | Make **Window** explicit (§6 M4). Inherit stance from the Context/Template if fixed; otherwise state it.                        |
| **AP‑4**  | **Eligibility‑after‑the‑fact** | Declaring the claim, then back‑fitting eligibility to observed traces.                      | Confuses **necessary conditions** with **diagnostics**; risks circularity. | Perform **M3 Qualify** *before* **M4 Bind/Assert**; treat evidence only in **M5**/**M6**.                                    |
| **AP‑5**  | **Global Label Illusion**      | Using bare labels (“process”, “agent”, “role”) as if universal.                             | Hides the Context; fuels homonym errors.                                      | Always recover **M1 Locate**: `address(τ)=⟨Context, SenseCell⟩`. Use F.5 naming discipline (Tech/Plain registers).              |
| **AP‑6**  | **Evidence by Prestige**       | “Industry practice says …” offered instead of KD‑CAL‑shaped facts.                          | Replaces observable Results with authority talk.                           | State an **evidence shape Σ(Context)** in **M5**; later fill it with **Observation/Result** facts (KD‑CAL).                     |
| **AP‑7**  | **Design/Run Inversion**       | Verifying a design‑time mask by design documents; verifying a run‑status with design specs. | Violates DesignRunTag; yields non‑falsifiable claims.                   | Apply **M2 Stance**: the Template’s stance must be compatible with the Context. Evidence follows the stance.                    |
| **AP-8**  | **Premature Bridge**           | A Bridge is introduced as a shortcut (“align first, then claim”), instead of stating the assignment/status locally and adding a Bridge only when actually needed. | Makes the verdict hostage to an uncertain translation; Bridge Loss and CL penalties leak into the claim and can unnecessarily lower confidence. | Keep the assignment/status claim local; if needed, create an **F.9 Bridge** with loss notes and CL penalty. |
| **AP‑9**  | **Token Proofs**               | Single anecdotal event taken as universal confirmation.                                     | Over‑generalises; ignores evidence windows and procedures.                 | In **M5**, include **Procedure** and **Window**; in **M6**, roll confidence γ from adequacy of sampling (KD‑CAL).            |
| **AP‑10** | **Role Explosion as Patch**    | New Role minted for every exception.                                                        | Name bloat; brittle semantics.                                             | Re‑examine **eligibility** and **Window**; consider a **Status** to mark exceptions instead of new Roles.                    |
| **AP‑11** | **Subject Drift**              | Status asserted on the wrong subject (team vs service; asset vs dataset).                   | Breaks referent clarity; evidence no longer matches.                       | Use **M4**’s split: **plays\_role(H, …)** vs **has\_status(subject(H), …)**; pick the correct subject kind.                  |
| **AP‑12** | **Spec‑in‑Name**               | Cramming constraints into the label (“24x7‑Operator‑With‑Pager”).                           | Names become brittle; invariants become invisible.                         | Keep the label minimal (F.5); move constraints into **eligibility**/**invariants**.                                          |
| **AP‑13** | **Non‑Local Evidence Shape**   | Evidence shape mentions constructs from another Context.                                       | Hidden Cross‑context import.                                                  | Rewrite Σ using only this Context’s vocabulary; if impossible, use **F.9** Bridge and keep Σ local.                             |

### F.6:10 - Worked examples

> Each example is a **context-local** assignment/status reasoning trace using **M1…M6**. cross-context relations, if any, are noted as *optional* bridges (F.9) but not relied upon.

#### F.6:10.1 - Service availability status (ITIL + KD‑CAL)

**Context.** *ITIL 4 (services family; design)*
**Template (Status).* `SLO:availability≥99.9%` anchored at **SenseCell** ⟨ITIL4, “SLO (availability)”⟩.

**M1 Locate.** `address(τ)=⟨ITIL4, SLO(availability)⟩`
**M2 Stance.** `stance(ITIL4)=design`, `stance(τ)=design` ⇒ `compatible_stance(τ, ITIL4)`
**M3 Qualify.** `eligible(Service S, τ@ITIL4)` if S is a published service with declared availability target.
**M4 Assert.** `has_status(S, τ:ITIL4) @ W` where `W = Q1‑2025` (the evaluation period).
**M5 Evidence shape Σ(ITIL4).** *Observation* of **availability characteristic** (MM‑CHR) for S, produced by a **Procedure** that samples uptime and computes the **Result** as ratio over `W`. (KD‑CAL/MM‑CHR terms only; no tool implied.)
**M6 Conclude.** If Results across `W` give ≥ 99.9 % with adequate sampling and declared exclusions applied, `holds( has_status(S, τ:ITIL4) @ W ) with γ≈0.9`.
*Optional bridge.* If uptime sensing vocabulary is expressed in **SOSA/SSN**, an **F.9 Bridge** may map ITIL’s “availability metric” to **ObservableProperty(availability)** with a declared CL penalty; the assignment/status claim itself remains ITIL-local.

#### F.6:10.2 - Behavioural operator role (IEC 61131‑3 + Enactment)

**Context.** *IEC 61131‑3 (control languages; run)*
\**Template (Role).* `Control‑Task‑Executor` anchored at **SenseCell** ⟨IEC61131‑3, “task executes program”⟩.

**M1 Locate.** `address(τ)=⟨IEC61131‑3, task‑execution⟩`
**M2 Stance.** `stance(IEC61131‑3)=run`, `stance(τ)=run` ⇒ compatible.
**M3 Qualify.** Holder `PLC_7` qualifies if it hosts program `P` and is scheduled by task `T`.
**M4 Bind.** `plays_role(PLC_7, τ:IEC) @ W` where `W = [08:00, 18:00] 2025‑06‑05`.
**M5 Evidence shape Σ(IEC).** **Observation** of task schedule and program invocation logs as **Results** for features `T`/`P` during `W`; presence of expected cyclic/event‑driven triggers.
**M6 Conclude.** If Results show the expected executions with no missed cycles beyond tolerance, `holds( plays_role(PLC_7, τ:IEC) @ W ) with γ≈0.8`.
*Trip-wire.* Do **not** restate this as “PROV Activity” without **F.9**; keep the assignment/status claim IEC-local.

#### F.6:10.3 - Dataset accuracy status (ISO/IEC 25024 + KD‑CAL)

**Context.** *ISO/IEC 25024 (data‑quality; design)*
\**Template (Status).* `accuracy≥0.98` anchored at **SenseCell** ⟨ISO25024, “data accuracy”⟩.

**M1 Locate.** `address(τ)=⟨ISO25024, data‑accuracy⟩`
**M2 Stance.** `stance(Context)=design`, `stance(τ)=design` ⇒ compatible.
**M3 Qualify.** Subject `Dataset D` has a defined **reference set** and sampling protocol.
**M4 Assert.** `has_status(D, τ:ISO25024) @ W` where `W = “snapshot v2025‑04”`.
**M5 Evidence shape Σ(ISO25024).** **Observation** of correctness of sampled records vs reference, **Procedure** per standard, **Result** as proportion correct with confidence interval.
**M6 Conclude.** If CI lower bound ≥ 0.98, `holds( has_status(D, τ) @ W ) with γ≈0.85`.

#### F.6:10.4 - Access vs behavioural: two claims, two Contexts

**Contexts.** *NIST RBAC (access; design)* and *BPMN 2.0 (workflow; design)*.
**Templates.** `DB‑Admin (RBAC status)` vs `Participant (BPMN role)`.

**RBAC claim (Status).**
M1…M6 yield `has_status(User U, RBAC:DB‑Admin) @ W_dir` with Σ(RBAC) = **Observation** of assignment state in the access model at time `W_dir`.

**BPMN claim (Role).**
M1…M6 yield `plays_role(Team T, BPMN:Participant) @ W_proc` with Σ(BPMN) = **Observation** that lanes/pools enact tasks during `W_proc`.

**Lesson.** Two separate **context-local** claims — one **Status assertion** and one **Role assignment**; **no** implication that holding RBAC status entails playing the BPMN Role.

### F.6:11 - Relations (with other patterns)

**Builds on:**
F.1 **Domain‑Family Landscape Survey** (Contexts fixed); F.2 **Term Harvesting** (local terms); F.3 **Intra‑Context Clustering** (SenseCells); F.4 **Role Description** (invariants, stance); F.5 **Naming Discipline** (labels).

**Constrains:**
**F.7** (Concept-Set Table): rows reference **SenseCells**; Role Description cards **point to** those rows but never **create** cross-context identity.
**F.8 Mint or Reuse?** Uses outcomes of **Role/Status** claims to decide: a new **Role/Status** label only when existing Templates cannot express the claim with eligibility/Window adjustments.
**F.9** (Alignment & Bridge): any relation across Contexts is **declared there**; Role Description cards remain context-local.
**F.10 Epistemic Status Mapping.** Consumes **M6** confidences γ and Σ‑adequacy to roll up assurance.

**Coordinates with.** **MM‑CHR** (characteristics, scales) wherever *Characteristic/Scale* is used in evidence shapes.

**Used by.**
Patterns (Part C) to anchor their examples: Sys‑CAL (execution/actuation roles), KD‑CAL (measurement statuses), Method‑CAL (execution claims for Methods/MethodDescription), Kind-CAL (typing claims remain outside Role Assignment & Enactment, but may inform eligibility predicates).

### F.6:12 - Migration notes (conceptual)

1. **Template refactor.** If a Template’s invariants change, **claims remain as‑is**; re‑evaluate **M6** on demand. Do not silently rewrite past claims.
2. **Edition updates.** When a Context’s canon updates, treat it as a **new Context** if sense shifts; Claims anchored to the old Context stay valid for their Window.
3. **Name revisions.** Renaming per F.5 does not alter **address(τ)=⟨Context, SenseCell⟩**; claims reference the address, not surface form.
4. **Bridge introduction.** Adding an **F.9 Bridge** never upgrades an existing Role/Status claim; at most it enables *separate* translations with declared loss.
5. **From exception to Status.** If recurring exceptions to a Role appear, prefer minting a **Status** Template that marks the exception rather than proliferating Roles.
6. **Window tightening.** If evidence shows drift, narrow future **Windows**; past claims remain tied to their original Windows.

### F.6:13 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.6:13.1 - Static conformance (SCR)

* **SCR-F6-S01 (Local address).** Every assignment/status claim states `address(τ)=σ` where `σ` is a **SenseCell** (per F.3); no bare labels.
* **SCR‑F6‑S02 (SenseFamily clarity).** Each claim is typed **Role** or **Status**, never both; subjects are of the correct kind. Claim records both **senseFamily** and **stance** explicitly or by inheritance.
* **SCR‑F6‑S03 (Stance compatibility).** `stance(Context)` and `stance(τ)` are compatible (design/run).
* **SCR‑F6‑S04 (Eligibility first).** For each claim, `eligible(H, τ@context)` is derivable prior to assertion.
* **SCR‑F6‑S05 (Window explicit).** Each claim has a Window (explicit or inherited) consistent with stance.
* **SCR‑F6‑S06 (Evidence‑ability).** For each claim, an **evidence shape Σ(Context)** is stated using only that Context’s vocabulary plus KD‑CAL/MM‑CHR primitives.
* **SCR‑F6‑S07 (Locality guard).** No Cross‑context terms appear inside a claim; any reference to other Contexts is flagged as **F.9 Bridge (informative)**, not used to justify the claim.

#### F.6:13.2 - Regression (RSCR)

* **RSCR‑F6‑E01 (Edition stability).** Adding a new edition/Context does not mutate existing claims’ Contexts or Windows.
* **RSCR‑F6‑E02 (Name stability).** Changing labels per F.5 leaves addresses and conclusions invariant.
* **RSCR‑F6‑E03 (Bridge neutrality).** Introducing or revising an **F.9 Bridge** does not auto‑flip claim truth values; at most it enables explicit translations with loss notes.
* **RSCR‑F6‑E04 (Evidence refresh).** When KD‑CAL procedures or **MM‑CHR characteristic scales** change, only **γ** is re‑evaluated; the claim’s semantics remain.

### F.6:14 - Didactic distillation (60‑second recap)

> **Six moves.** (M1) *Locate* the Context & SenseCell; (M2) check **stance**; (M3) test **eligibility**; (M4) **bind/assert** with a **Window**; (M5) sketch the **evidence shape** in that Context; (M6) **conclude** with confidence γ.
> **Two iron rules.** Keep it **context‑local**; keep **Role** and **Status** on their senseFamily.
> **Pay-off.** Assignment/status claims become small, auditable thoughts: easy to teach, easy to check, and easy to relate—later—via explicit Bridges when you truly must step between Contexts.

### F.6:End

## F.7 - Concept‑Set Table

**“Show one thing across Contexts—only where explicit bridges allow it.”**

**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for ‘Context’** (Context ≡ `U.BoundedContext`); **F.0.1 senseFamily (normative)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering** (SenseCells); F.5 **Naming Discipline**; F.9 **Alignment & Bridge Across Contexts**.
**Coordinates with.** F.4 **Role Description**; F.6 **Role Assignment & Enactment Cycle (Six-Step)**; Part C patterns (for examples), **MM‑CHR (for Characteristic)**; A.6.9 (RPR‑XCTX for repairing umbrella cross‑Context sameness/alignment prose before it justifies rows).
**Aliases (informative).** *Concept‑Set table*, *comparison grid*.

### F.7:1 - Intent & applicability

**Intent.** Provide a **single, didactic page** where each **row** presents **one Concept‑Set**—a *set of SenseCells from different Contexts that we are licensed (by explicit Bridges) to treat as “the same for a stated scope”*. Columns are **Contexts**; cells carry **local labels**. The table **does not invent equivalences**: it **summarises** already declared **F.9 Bridges**, exposing *scope, losses, and counter‑examples* at a glance.

**Applicability.** Use whenever cross-context reading is necessary (naming U.Types, teaching contrasts, assignment/enactment-adjacent terminology). It is a **reading lens**, not a data model: **notation-free**, **governance-free**, **Context-loyal**.

**Non‑goals.** No hidden merges. No “global terms”. No workflows or tool schemas. The table is a **conceptual display** of *licensed sameness* and *honest non‑sameness*.


### F.7:2 - Problem frame

Without a disciplined Cross‑context view:

1. **Silent equivalence.** Readers assume sameness by name alone (e.g., *process*).
2. **Loss denial.** Mappings hide what is dropped (DesignRunTag, units, agency).
3. **Name inflation.** New U.Types are coined to avoid facing heterogeneity.
4. **Cognitive scatter.** Concepts drift across documents without one compact, teachable “where‑what‑how‑same” view.


### F.7:3 - Forces

| Force                          | Tension to resolve                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Locality vs comparison**     | Meaning lives in Contexts; yet we must **compare** Contexts to reason across disciplines.                           |
| **Didactics vs fidelity**      | A compact row is easy to grasp; it must still show **scope and loss** honestly.                               |
| **Simplicity vs completeness** | A minimal grid aids memory; temptation to overload it with proofs and procedures must be resisted.            |
| **Sameness vs difference**     | Some families **cannot** be unified; the table must support **contrast rows** without pretending equivalence. |


### F.7:4 - Core idea (didactic)

A **Concept‑Set** is a **finite set of addresses**

$$
\text{CS}=\{\langle \text{Context}_i,\ \text{SenseCell}_i\rangle\}_{i=1..n}
$$

that FPF **treats as one** *for a declared scope* because there exist **F.9 Bridges** connecting these SenseCells pairwise (directly or via a short chain) with **congruence level** $\text{CL}$ above a **threshold** suitable for that scope. The **table row** shows:

* **FPF Label** *(Tech/Plain)* — the *didactic, FPF‑level* name chosen per F.5.
* **Row Scope** — where “being one” is safe (e.g., *Naming-only*, *assignment/enactment-eligibility*, *KD-CAL metric*, *Type‑structure*).
* **Row CL(min)** — the **minimum CL** of the Bridges that justify the row.
* **Context columns** — each cell: the **local label** + (optional) short cue.
* **Rationale (one line)** — why sameness is warranted *for this scope*.
* **Counter‑examples (one line)** — where/why sameness **breaks**.

> **Memory hook.** *A Concept‑Set row is a promise:* “You may **read across** these Contexts **this far—and no farther**.”


### F.7:5 - Minimal vocabulary (this pattern only)

* **Context** — shorthand for `U.BoundedContext` (per E.10.D1).
* **senseFamily** — **referenced from F.0.1**; not redefined here; used to **type** rows and to require **uniformity** within a row.
* **SenseCell** — a **(Context × Local‑Sense)** address from F.3.
* **Bridge (F.9)** — an explicit, declarative Cross‑context mapping with a **congruence level** **CL** and **loss note**.
* **Characteristic (MM‑CHR)** — measurable comparandum defined in **MM‑CHR**; may be referenced in **Measurement/KD‑metric** rows; **do not** use “axis” only as a euphemism.
* **Concept‑Set (row)** — a *licensed sameness* across Contexts, bounded by **Row Scope** and **Row CL(min)**.
* **Contrast row** — a *non‑sameness* row: same surface across Contexts with **no** sufficient Bridges; teaches **difference**, not unity.


### F.7:6 - The table (conceptual layout)

> One page. Fixed column order by Context. Each row fits in **five lines** max.

```
FPF Label (Tech / Plain) | Row Scope | Row CL(min) | [Context A] local label | [Context B] local label | [Context C] local label | Rationale | Counter‑examples
```

**Reading rules (didactic):**

1. **Cells are local.** A cell is **not** a translation; it is the Context’s **own** label for its SenseCell.
2. **Scope is king.** The FPF label only licenses sameness **within its Row Scope**. Outside that scope, treat cells as **different**.
3. **Row CL(min) governs trust.** Lower CL ⇒ narrower applicability; **never** up‑scope a row without revisiting Bridges.
4. **Rationale & counter‑examples** are **obligatory one‑liners**; if you need paragraphs, you need an F.9 walkthrough, not a row.

**Didactic name rationale** “Giants' table’” that alludes to *standing on the shoulders of giants*: each row explicitly leans on authoritative context of meaning (**U.BoundedContext**) established by prior disciplines and not imagined. It does **not** mean a physically large table; the name signals epistemic humility and traceable reliance on those sources. "We are like dwarfs on the shoulders of giants, so that we can see more than they, and things at a greater distance, not by virtue of any sharpness of sight on our part, or any physical distinction, but because we are carried high and raised up by their giant size." by Bernard of Chartres , d. c.1130, French philosopher.

### F.7:7 - Conceptual construction (thought moves, not workflow)

> The table is derived from earlier patterns; it **creates nothing new**.

* **Sourcing.** Candidate cells come **only** from **SenseCells** (F.3).
* **Licensing.** A row exists **iff** the relevant **Bridges (F.9)** already justify sameness at the chosen **Row Scope**.
* **Bounding.** Prefer **2–4 Contexts** per row (parsimony); add more only if each adds a *distinct necessity* for the sameness claim.
* **Typing.** A row is **typed by senseFamily**: Role, Status, Type‑structure, Measurement, etc. **Do not mix senseFamilies** in one row.
* **Temporal honesty.** A row’s cells must share **compatible DesignRunTag**; if not, either split into two rows or mark a **contrast row**.


### F.7:8 - Invariants (normative)

1. **Context‑loyal cells.** Every non‑empty cell is a **SenseCell** address; no minted paraphrases.
2. **Bridge sufficiency.** For a *Concept‑Set* row, **every pair** of filled cells is connected by an **F.9 Bridge path** whose **bottleneck CL** ≥ **Row CL(min)** printed for the row.
3. **Scope declaration.** Each row **MUST** declare a **Row Scope** chosen from a small controlled set (e.g., *Naming-only*, *assignment/enactment-eligibility*, *KD-metric*, *Type-structure*).
4. **senseFamily uniformity.** All cells in a row belong to the **same senseFamily** (Role **or** Status **or** Type-structure **or** Measurement…).
5. **Temporal compatibility.** Either all cells share the **same stance**, or the row is a **contrast row** (no sameness claim).
6. **Loss disclosure.** If any Bridge in the row has a **loss note**, the row **MUST** include a **counter‑example** that illustrates that loss in one line.
7. **No stealth expansion.** Adding a new cell to a row **MUST NOT** lower the printed **Row CL(min)** without updating **Row Scope** or splitting the row.
8. **Parsimony.** A row with only one filled cell is **forbidden** (that would be local talk, not a Cross‑context concept).
9. **Didactic bound.** A row that cannot be read in **≤ 30 seconds** violates didactic primacy and must be split.


### F.7:9 - Micro‑illustrations (safe patterns)

> Illustrative only; these presume corresponding **F.9 Bridges** exist with stated CL and losses.

**(a) Subtyping across type‑formalisms (Type‑structure row)**

| FPF Label                                  | Row Scope      | Row CL(min) | OWL 2             | Kind-CAL            | Rationale                                                        | Counter‑examples                                                         |
| ------------------------------------------ | -------------- | ----------- | ----------------- | ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **is‑a (Tech)** / *type hierarchy* (Plain) | Type‑structure | CL = 3      | `rdfs:subClassOf` | `U.SubtypeRelation` | Both are partial‑order *class* subsumption used for inheritance. | FCA *concept* order is not a class subsumption; keep it out or CL drops. |

**(b) “Observation result value” (Measurement row)**

| FPF Label                           | Row Scope | Row CL(min) | SOSA/SSN                | ISO 80000‑1                    | ITIL 4                       | Rationale                                                                                           | Counter‑examples                                                |
| ----------------------------------- | --------- | ----------- | ----------------------- | ------------------------------ | ---------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **result‑value** / *measured value* | KD‑metric | CL = 2      | `sosa:Result` (literal) | `QuantityValue` (unit‑bearing) | *metric value* (service KPI) | Values can be read as numbers tied to a Characteristic; ITIL metric uses same notion when unitised. | ITIL “metric” may be composite indices (loss of unit fidelity). |

**(c) Contrast row: “process” (no sameness)**

| FPF Label              | Row Scope | Row CL(min) | BPMN 2.0              | PROV‑O                  | Thermodynamics           | Rationale                                                 | Counter‑examples                                                                   |
| ---------------------- | --------- | ----------- | --------------------- | ----------------------- | ------------------------ | --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **process** (contrast) | —         | —           | *graph of flow nodes* | *time‑bounded activity* | *state‑space trajectory* | Same surface, **different** senses; no licensed sameness. | Any attempt to equate design‑graph with run‑occurrence fails stance compatibility. |


### F.7:10 - Anti‑patterns & remedies

| #         | Anti‑pattern                | Symptom in a row                                                               | Why it breaks thinking                                               | Remedy (conceptual move)                                                                                          |
| --------- | --------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **Bridge‑free sameness**    | Cells listed as “same” because their labels look alike; no cited Bridges.      | Violates locality; imports meaning across Contexts by name.             | A row **exists only** if backed by **F.9 Bridges**. Otherwise produce a **contrast row**.                         |
| **AP-2**  | **Scope creep**             | Row labelled “Type-structure” but used to justify **assignment/enactment-eligibility** or KD metrics. | Scope licences are not transferable; inference leaks.                | Keep a **small controlled set of Row Scopes**. If use widens, **mint a new row** or **re-bridge** with higher CL. |
| **AP‑3**  | **senseFamily mixing**      | One row mixes Role, Status, Measurement, and Type‑structure cells.             | Conflates senseFamily (F.0.1); readers cannot tell “what kind of sameness”. | **Type each row.** If two senseFamilys are needed, **split** into two rows.                                             |
| **AP‑4**  | **Temporal blur**           | Cells with incompatible DesignRunTag declared “same”.                     | Design artefacts ≠ run occurrences; claims invert.                   | Either **harmonise stance** (choose only compatible cells) or publish a **contrast row**.                         |
| **AP‑5**  | **Loss denial**             | Bridges carry loss notes, but the row omits counter‑examples.                  | Readers over‑trust; misuse outside safe scope.                       | Add a **one‑line counter‑example** that illustrates the loss.                                                     |
| **AP‑6**  | **CL averaging**            | Row CL(min) computed as an average of heterogeneous Bridges.                   | The weakest link governs; averages overstate safety.                 | Row CL(min) is the **bottleneck** (minimum along connecting paths).                                               |
| **AP‑7**  | **Overwide rows**           | 6–8 Contexts in one row; hard to read; subtle mismatches hide.                    | Violates didactic primacy; invites hidden losses.                    | **Parsimony**: 2–4 Contexts per row unless each extra cell has a **distinct necessity** you can state in one line.   |
| **AP‑8**  | **Minted paraphrases**      | Cells reword a Context’s label instead of citing the SenseCell.                   | Hides locality; future drift becomes invisible.                      | **Cells are Context‑loyal.** Use the Context’s own SenseCell label.                                                     |
| **AP‑9**  | **Duplicate rows by style** | Two rows with the same cell set but different FPF labels.                      | Name inflation; readers assume two distinct concepts.                | Keep **one row** per Concept‑Set per scope. Alternative labels appear as **aliases** in F.5, not new rows.        |
| **AP‑10** | **Implied transitivity**    | A↔B and B↔C Bridges exist; row silently assumes A↔C at the same CL.            | Paths can reduce CL; semantics might not compose.                    | Compute CL for **A↔C via bottleneck**; if too low, either reduce **Row Scope** or **omit** the cell.              |


### F.7:11 - Worked examples

> Each example gives a **row** (compact), then a **reading** explaining scope and limits. All sameness claims presuppose suitable **F.9 Bridges** with the stated CL.

#### F.7:11.1 - Behavioural actor across Contexts (naming‑only)

| FPF Label (Tech / Plain)              | Row Scope   | Row CL(min) | BPMN 2.0        | PROV‑O    | Rationale                                                                               | Counter‑examples                                                                                      |
| ------------------------------------- | ----------- | ----------- | --------------- | --------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **actor** / *party that participates* | Naming‑only | CL = 2      | **Participant** | **Agent** | Both denote a bearer that can be named as the party to which activities are attributed. | PROV **Agent** includes software agents; BPMN **Participant** is typically an organisation lane/pool. |

**Reading.** The row licenses a **glossary‑level sameness** for didactic prose (“the actor”). It does **not** license modelling **identity** or inference across Contexts.


#### F.7:11.2 - Execution occurrence (assignment/enactment-eligibility)

| FPF Label                                       | Row Scope       | Row CL(min) | PROV‑O                                                           | IEC 61131‑3                                          | Rationale                                                                       | Counter‑examples                                                   |
| ----------------------------------------------- | --------------- | ----------- | ---------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **execution-occurrence** / *a run that happens* | assignment/enactment-eligibility | CL = 2      | **Activity** (time-bounded occurrence using/generating entities) | **Task execution** (cyclic/event-driven program run) | Both are **run-time** occurrences that can be referenced by `U.RoleEnactment` to ground **Work performed under an assignment**. | BPMN **Process** is a **design** graph; not an occurrence—exclude. |

**Reading.** Safe to use as the **run-time occurrence that `U.RoleEnactment` points to** when we say “this Work was performed under an assignment”. Not safe to equate **all** PROV Activities with **all** PLC task runs for analytics.


#### F.7:11.3 - Result value as KD‑metric (measurement)

| FPF Label                           | Row Scope | Row CL(min) | SOSA/SSN             | ISO 80000‑1                      | ITIL 4           | Rationale                                                                                                | Counter‑examples                                               |
| ----------------------------------- | --------- | ----------- | -------------------- | -------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **result‑value** / *measured value* | KD‑metric | CL = 2      | **Result** (literal) | **QuantityValue** (unit‑bearing) | **metric value** | A number representing a **Characteristic** at observation time; can be unitised and compared to targets. | ITIL “metric” may be a composite index; units may be implicit. |

**Reading.** Licences **metric tables** that join observations to service targets; warns that composite KPIs may violate unit fidelity.


#### F.7:11.4 - Subtype relation (type‑structure)

| FPF Label                   | Row Scope      | Row CL(min) | OWL 2             | Kind-CAL            | Rationale                                     | Counter‑examples                                                                 |
| --------------------------- | -------------- | ----------- | ----------------- | ------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| **is‑a** / *type hierarchy* | Type‑structure | CL = 3      | `rdfs:subClassOf` | `U.SubtypeRelation` | Both are partial orders used for inheritance. | FCA **concept order** is not a class subsumption—exclude or publish another row. |


#### F.7:11.5 - Contrast: “role” (access vs behaviour)

| FPF Label           | Row Scope | Row CL(min) | NIST RBAC                 | BPMN 2.0                                 | Rationale                                                      | Counter‑examples                                                                   |
| ------------------- | --------- | ----------- | ------------------------- | ---------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **role** (contrast) | —         | —           | **Role** (permission set) | **Participant/Actor** (behavioural mask) | Same surface; **different senseFamilys** (Status vs Role/behaviour). | Any attempt to unify collapses deontics into behaviour; stance and effects differ. |

**Reading.** This row **teaches difference**; it deliberately **does not** license sameness.


### F.7:12 - Reasoning primitives (judgement schemas, notation‑free)

> All judgements are **pure** (no side effects). “Contexts” are `U.BoundedContext`. `SC(C)` denotes a SenseCell in Context `C`. `CL(X↔Y)` is the congruence level of the **best** Bridge path (F.9) between SenseCells `X` and `Y` (bottleneck along that path).

#### F.7:12.1 - Row licensing

**Form.**
`S = {SC(C₁), …, SC(Cₙ)}, Scope = s, τ(s) = requiredCL ⊢ licensable(S,s) ⇔ (∀ i<j: CL(SC(Cᵢ)↔SC(Cⱼ)) ≥ requiredCL ∧ senseFamily (S) is uniform ∧ stance(S) compatible)`

**Reading.** A set of cells **licenses** a row of scope `s` iff every pair is bridged at or above the **required CL** for that scope, all cells sit in the **same senseFamily**, and **DesignRunTag** is compatible.


#### F.7:12.2 - Bottleneck CL for a row

**Form.**
`RowCL(S) = min_{i<j} CL(SC(Cᵢ)↔SC(Cⱼ))`

**Reading.** The row’s CL is the **minimum** congruence level across all pairs (the weakest link).


#### F.7:12.3 - Scope guard

**Form.**
`licensable(S,s) ∧ s ⊑ s' ⊢ licensable(S,s') only if RowCL(S) ≥ τ(s')`

**Reading.** You may **tighten scope** (use the row for a stronger purpose) only if the row’s CL meets the **higher threshold** for that scope.


#### F.7:12.4 - Contrast decision

**Form.**
`(∃ i<j: CL(SC(Cᵢ)↔SC(Cⱼ)) < τ(Naming‑only)) ⊢ publish‑contrast(S)`

**Reading.** If even **Naming‑only** cannot be licensed, publish a **contrast row** instead of forcing sameness.


#### F.7:12.5 - Row extension guard

**Form.**
`licensable(S,s) ∧ add SC(Cₖ) ⊢ licensable(S∪{SC(Cₖ)}, s) iff ∀ i: CL(SC(Cᵢ)↔SC(Cₖ)) ≥ τ(s)`

**Reading.** You may add a new cell only if it bridges to **every existing cell** at the row’s scope.


#### F.7:12.6 - Loss disclosure obligation

**Form.**
`licensable(S,s) ∧ (∃ i<j: lossNote on Bridge(SC(Cᵢ),SC(Cⱼ))) ⊢ row must carry ≥1 counter‑example`

**Reading.** Any loss note on any supporting Bridge obliges the row to include a **counter‑example one‑liner**.


### F.7:13 - Relations (with other patterns)

**Builds on:**
F.1 **Contexts fixed** → defines the column set; F.2 **Harvest** → supplies term material; F.3 **SenseCells** → provide cell addresses; F.5 **Naming Discipline** → provides the two‑register **FPF labels**; F.9 **Bridges** → legally justify each row.

**Constrains:**
F.4 **Role Description** — when a template cites an FPF label from the table, it **inherits the Row Scope**; no template may claim semantics beyond the row’s licence.
F.6 **Role Assignment & Enactment Cycle (Six-Step)** — Move M‑4 (“choose label”) must reference a row if it wants Cross‑context reading.

**Used by.**
Part C patterns for didactic alignment pages; Part B trust calculus (B.3) may consume **Row CL(min)** when computing translation penalties.


### F.7:14 - Migration notes (conceptual)

1. **Bridge update.** If any supporting Bridge’s CL changes, recompute **Row CL(min)**. If it drops below the printed value, either **lower Row Scope**, **split** the row, or **retire** it.
2. **New Context appears.** Do **not** auto‑expand rows. Test with **12.5**; add only if it brings a **distinct necessity**.
3. **Sense revision inside a Context.** If a SenseCell splits (F.3), decide which child cell (if any) remains in the row; the rest may require **new rows** or a **contrast**.
4. **Scope promotion.** To use a row for a stronger purpose (e.g., from **Naming-only** to **assignment/enactment-eligibility**), first ensure **Row CL(min) ≥ τ(new scope)**; otherwise construct **new Bridges** or **decline** promotion.
5. **Deprecation.** If a row no longer meets its invariant, mark its FPF label as **retired** in F.5 and point to successor rows (if any).
6. **Edition churn.** When a Context is superseded (F.1), either keep the cell (if semantics stable) or treat the successor as a **new Context** and re‑evaluate licensability.


### F.7:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.7:15.1 - Static conformance checks (SCR)

* **SCR‑F7‑S01 (Context‑loyal cells).** Every non‑empty cell references an existing **SenseCell** (F.3) in a declared Context (F.1).
* **SCR‑F7‑S02 (Closure & bottleneck).** For each Concept‑Set row, **every pair** of cells has a Bridge path with CL ≥ **Row CL(min)** printed; **Row CL(min)** equals the **minimum** pairwise CL.
* **SCR‑F7‑S03 (Typed & scoped).** Each row declares a **Row Scope** from the controlled set and is **senseFamily‑uniform** (Role **or** Status **or** Measurement **or** Type‑structure…).
* **SCR‑F7‑S04 (Temporal compatibility).** Non‑contrast rows have **compatible** DesignRunTag across cells.
* **SCR‑F7‑S05 (Loss disclosure).** If any supporting Bridge has a recorded loss, the row includes **≥1 counter‑example** line.
* **SCR‑F7‑S06 (Parsimony).** Rows contain **2–4 Contexts** unless a one‑line necessity is stated for each extra Context.

#### F.7:15.2 - Regression checks (RSCR)

* **RSCR‑F7‑E01 (Bridge drift).** After any Bridge change (F.9), recompute **Row CL(min)**; flag rows whose scope is now overstated.
* **RSCR‑F7‑E02 (Sense split).** After a SenseCell splits (F.3), ensure rows referencing it either pick a child cell or retire.
* **RSCR‑F7‑E03 (Scope integrity).** No consumer pattern uses a row outside its declared **Row Scope**.
* **RSCR‑F7‑E04 (No stealth growth).** Additions of cells never lower **Row CL(min)** silently; if they do, either split the row or reduce scope.


### F.7:16 - Didactic distillation (60‑second teaching script)

> “A **Concept-Set row** shows **one idea across Contexts**—but only where explicit **Bridges** license it. Columns are Contexts; cells are **their own labels**. The row prints a **scope** (‘Naming-only’, ‘assignment/enactment-eligibility’, ‘Type-structure’, ‘KD-metric’) and the **weakest CL** that justifies reading across. A **one‑line rationale** says why sameness is safe **here**; a **counter‑example** warns where it breaks. Keep rows small (2–4 Contexts), typed (don’t mix senseFamilies), and temporally honest (design vs run stance). If Bridges don’t suffice, publish a **contrast row** instead. The table doesn’t invent meaning; it **summarises licensed sameness** so readers can cross disciplines without smuggling assumptions.”

### F.7:End

## F.8 - Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)

**“Name only what thinking **requires**, and reuse everything else.”**

**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; A.8 **Universal Core**.
**Coordinates with.** F.1 **Contexts (Contexts)**; F.2 **Harvest**; F.3 **SenseCells**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge**.
**Aliases (informative).** *Mint‑vs‑Reuse gate*; *Naming governor*.


### F.8:1 - Intent & applicability

**Intent.** Provide a **minimal, conceptual decision lattice** that answers, for any modelling need:

> “Do I **reuse** an existing label, add an **alias**, reference a **Concept‑Set row**, define a **Role Description**, or mint a **new U.Type**?”

The lattice enforces **locality of meaning** (Contexts), **senseFamily separation** (A.7), and **parsimony** (A.11) while remaining didactically simple.

**Applicability.** Use whenever a new name seems “needed” in any FPF pattern thread (**Role Assignment & Enactment**, Sys-CAL, KD-CAL, Kind-CAL, Method-CAL, LCA-CAL…).

**Non‑goals.** No workflows, no roles, no storage. This is **thinking discipline**, not process guidance.


### F.8:2 - Problem frame

Modellers tend to **mint names** when they actually need **reuse**, **aliasing**, or **explicit Cross‑context reading**. Consequences:

1. **Name inflation.** Parallel labels for the same idea across Contexts.
2. **senseFamily mixing.** Behavioural **Role** names that smuggle in deontic **Status** or measurement talk.
3. **Hidden bridges.** Cross‑context sameness is implied by look‑alike words rather than declared (F.9).
4. **Kernel sprawl.** New **U.Types** appear to plaster over local vocabulary gaps.


### F.8:3 - Forces

| Force                       | Tension to resolve                                                                            |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| **Parsimony vs coverage**   | Avoid new names unless necessary, yet cover recurring Cross‑context readings.                    |
| **Locality vs unification** | Keep senses **in‑Context**; when reading across, do it **explicitly** and only as far as needed. |
| **Didactics vs fidelity**   | Give readers one label to hold, but never over‑state sameness (respect CL and scope).         |


### F.8:4 - Minimal vocabulary (used in this pattern only)

* **Context** — `U.BoundedContext` (per D.CTX).
* **SenseCell** — address of a **local sense** produced by F.3 (one context × one clustered sense).
* **Concept‑Set row** — a **licensed Cross‑context reading** (F.7) of cells in one senseFamily with a declared **Row Scope** and **Row CL(min)**.
* **senseFamily** — as defined in **F.0.1**; here used as the **typed discriminator for rows** restricted to {Role | Status | Measurement | Type‑structure | Method | Execution}. 
* **Role Description** — a **Role/Status** template anchored to a **single SenseCell** (F.4).
* **Alias** — an **additional label** for an existing FPF label (within F.5), no new semantics.
* **CL threshold τ(scope)** — the **minimum congruence level** needed for a row’s scope (e.g., τ(Naming-only) < τ(Assignment-eligibility) < τ(Type-structure)).


### F.8:5 - The decision lattice (conceptual, notation‑free)

> Read top‑to‑bottom; the **first satisfied** branch decides. At every step, **state the senseFamily** (Role / Status / Measurement / Type‑structure / Method / Execution) before you proceed.

#### F.8:5.1 - Q0 — What is the **senseFamily** of your need?

* If **uncertain**, return to F.1/F.3: stabilise the Context(s) and the local sense.
* If **mixed**, split the need: one decision **per senseFamily** (A.7).

#### F.8:5.2 - Q1 — Is there a **single Context** whose SenseCell already expresses it?

* **Yes →** **Reuse** the **SenseCell**’s label **inside that Context**.

  * If you need assignable behaviour or deontics on that sense: **define a Role Description** **anchored to that SenseCell** (F.4).
* **No →** go to Q2.

> *Example (engineer).* You want “**task execution**” in control software. In `IEC 61131‑3` there is a clear SenseCell for **task execution**. **Reuse** that label; if you need responsibilities (“who monitors runs”), define a **Role Description** anchored to this SenseCell.

#### F.8:5.3 - Q2 — Do you need to **read across Contexts** (same senseFamily)?

* **No →** stay within one context; if your desire is merely a nicer label, consider an **Alias** (Q3).
* **Yes →** check F.7 for a **Concept‑Set row** covering your cells **in this senseFamily** with adequate **Row Scope** and **Row CL(min)**.

  * **Found & sufficient →** **Reuse the row’s FPF label** at that scope.
  * **Not found or insufficient →** either (a) **publish a contrast** (teach difference), or (b) propose a **new row** but only after F.9 Bridges exist at **τ(scope)**.

> *Example (manager).* You want one label for the **actor** in workflow and provenance prose. F.7 has a **Naming‑only** row mapping *BPMN Participant* ↔ *PROV Agent* at CL = 2. **Reuse** “actor” **at Naming‑only** scope; do **not** infer identity in models.

#### F.8:5.4 - Q3 — Is this **only a wording preference** for an existing FPF label?

* **Yes →** add an **Alias** in F.5 (Tech register and/or Plain register), no semantics changed.
* **No →** go to Q4.

> *Example (researcher).* You prefer “**is‑a**” to “**subclass‑of**” in Type pages. That is an **Alias** for the same concept; no new row, no new U.Type.

#### F.8:5.5 - Q4 — Does your need recur across Contexts in a way **not captured** by current rows, **with Bridges** already available at the required CL?

* **Yes →** propose a **new Concept‑Set row** (F.7): small (2–4 Contexts), **one senseFamily**, declare **Row Scope** and **Row CL(min)**, include a **counter‑example** if any Bridge has loss notes.
* **No →** go to Q5.

> *Example (engineer).* You repeatedly compare **runtime occurrence** in PROV with **PLC task runs**. F.9 Bridges exist at CL = 2. Propose **row “execution-occurrence”** at **assignment/enactment-eligibility** scope (not Type-structure).

#### F.8:5.6 - Q5 — Are you describing a **kernel‑level notion** missing from the catalogue, **not** reducible to existing rows or Role Descriptions, and **present across ≥ 3 domain families** (A.8)?

* **Yes →** propose a **new U.Type** (rare). Supply:
  (i) the minimal **intensional definition**; (ii) cross‑family evidence (≥ 3 Contexts, **distinct families**); (iii) how it **doesn’t** duplicate an existing U.Type.
* **No →** you **do not mint** a new type. Re‑express the need in terms of **Context reuse**, **row reuse**, **Alias**, or a **Role Description**.

> *Example (researcher).* You think we need **U.InfluenceEdge** (causal tendency). If it appears as a stable, **senseFamily‑specific** notion across **control**, **epistemic inference**, and **methods** (≥ 3 families), and cannot be formed from existing `U.Relation` subtypes, it **may** qualify. Otherwise, treat it as a **pattern** or a **row**.


### F.8:6 - Scope thresholds (default τ) — **how much sameness** you’re allowed to claim

| Row / Use Scope     | What it licenses                                                                              | Default τ (minimum CL) | Typical consumers                         |
| ------------------- | --------------------------------------------------------------------------------------------- | ---------------------: | ----------------------------------------- |
| **Naming‑only**     | Shared label in prose, diagrams, and primers; **no inference**.                               |                  **1** | Pedagogy, glossary, didactic figures.     |
| **Assignment-eligibility** | Safe to reference the row’s target as the **thing a `U.RoleAssignment` may point to** (e.g., a run, a value). | **2** | F.4 Role Description, acceptance narratives. |
| **KD‑metric**       | Treat cells as the **same measured outcome** (unit‑compatible, procedure‑compatible).         |                  **2** | Measurement summaries, SLO tables.        |
| **Type‑structure**  | Treat cells as the **same structural relation** (e.g., subtyping) with inheritance semantics. |                  **3** | Kind-CAL pages, structural proofs.        |

> **Guard.** You may **tighten** scope (e.g., from Naming-only → Assignment-eligibility) **only** if the **Row CL(min)** meets the **higher τ**.


### F.8:7 - Micro‑examples (didactic triad)

#### F.8:7.1 - For engineers — “Do we need a new **Execution** label?”

* **Need.** “We want to refer to **what actually happened** in both provenance logs and PLC runtime.”
* **senseFamily.** Execution - **stance.** run.
* **Contexts.** `PROV‑O` (Activity), `IEC 61131‑3` (task run).
* **Row?** F.7 has **execution-occurrence** at **assignment/enactment-eligibility**, CL = 2.
* **Decision.** **Reuse** that row’s label at **Assignment-eligibility**; **no** new U.Type; define Role Descriptions **anchored to each Context** as needed.

#### F.8:7.2 - For managers — “Can we call them all **actors**?”

* **Need.** A single everyday word in the spec to denote “the responsible party”.
* **senseFamily.** Role (behavioural mask in prose).
* **Contexts.** `BPMN 2.0` (Participant), `PROV‑O` (Agent).
* **Row?** **Naming‑only** row “actor”, CL = 2.
* **Decision.** **Reuse** “actor” **in prose only**; keep Context‑loyal labels in formal sections. No Role Description minted unless tied to one context.

#### F.8:7.3 - For researchers — “New **U.Type** for ‘Work Scope’?”

* **Need.** Kernel notion capturing **feasible performance region** across systems.
* **Test A.8.** Appears in **control** (reachable sets), **services** (operating envelope), **measurement** (confidence bands): **≥ 3 families?**
* **Reduction test.** Can it be expressed as a **row** + existing `U.Relation` + KD‑CAL constructs?
* **Decision.** If **not reducible** and **cross‑family stable**, propose **new U.Type** with minimal definition; otherwise, prefer a **row** or a **pattern**.


### F.8:8 - Invariants (normative, lightweight)

1. **Context‑first.** Every decision cites at least one **Context**; no global senses.
2. **senseFamily purity.** A single decision covers **one senseFamily**. Mixed needs are split.
3. **Row honesty.** Any Cross‑context reuse occurs **via a Concept‑Set row** at or above **τ(scope)**; no stealth equivalence.
4. **Role Description anchoring.** Role Descriptions are **single-Context**, **single-cell** anchors (F.4).
5. **Alias modesty.** Aliases **never** change semantics and live under F.5.
6. **Kernel restraint.** New **U.Types** are **rare**; A.8 **(≥ 3 families)** is mandatory, and duplication with existing U.Types must be ruled out.


### F.8:8.1 - Mint/Reuse discipline for **policy-ids** (normative addendum)

FPF treats **policy-ids** (e.g., `Φ(CL)`, `Φ_plane`, `Ψ(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, `InsertionPolicyRef`, Acceptance clause ids) as **first-class, versioned tokens**. They are not “just strings”, and they are not governed by tier ladders or implied authority.

**PolicySpecRef.** A **resolvable reference** to the normative definition of a policy-id (“what does this policy-id mean?”). At minimum it:
* identifies the policy-id,
* pins an immutable edition (or equivalent digest), and
* can be located from the same publication bundle (MVPK / UTS / EvidenceGraph anchors).

**MintDecisionRef.** A **resolvable reference** to the decision record that introduced (minted) a policy-id into a declared namespace/registry. For **normative** policy-ids this is typically a **DRR id** (E.9) or an equivalent change decision record. For **purely local, non-exported** policy-ids it MAY be a Gate `DecisionLog` entry (A.21) if that local-only scope is explicit.

**PolicyIdRef (canonical bundle).**  
`PolicyIdRef := { policy_id, PolicySpecRef, MintDecisionRef? }`.

**Rules.**
1. **No silent policy-id minting.** If a publication introduces a *new* policy-id (not previously present in the declared namespace/registry), it **MUST** surface a `PolicyIdRef` whose:
   * `PolicySpecRef` is edition-pinned, and
   * `MintDecisionRef` is resolvable from the publication’s DRR/DecisionLog links.
2. **Reuse is reference-only.** If a publication **reuses** an existing policy-id, it **MUST** surface a `PolicySpecRef` (and **SHOULD** preserve the prior mint decision link where available). It **MUST NOT** restate policy semantics *as if* minting a new policy-id.
3. **GateCrossing checkability.** Any GateCrossing/CrossingSurface that surfaces policy-ids **MUST** include `PolicyIdRef` (or an equivalent “policy-id + resolvable refs” structure) so GateChecks can verify resolvability and pin consistency (E.18/A.21/G.6:7.5.8).
4. **Authority is policy, not tiers.** “Who may mint” vs “who may reuse” is expressed by the referenced **policy specs** and **mint decisions** (and enforced by the active GateProfile/GateChecks), not by fixed tier labels.



### F.8:9 - Quick reference (one‑glance map)

| You feel you need…                          | Likely action                  | Why                                              |
| ------------------------------------------- | ------------------------------ | ------------------------------------------------ |
| A convenient everyday word across two Contexts | **Reuse a Naming‑only row**    | Keeps prose simple without smuggling inference.  |
| An assignable mask with invariants          | **Role Description (single Context)** | Roles/Statuses attach to **local** senses.       |
| The same measured outcome across Contexts      | **Reuse a KD‑metric row**      | Units/procedures aligned at CL ≥ 2.              |
| A unifying schema relation (e.g., is‑a)     | **Reuse a Type‑structure row** | Structural inference preserved at CL ≥ 3.        |
| A nicer label for the same FPF concept      | **Alias in F.5**               | Style only; zero semantics.                      |
| A brand‑new primitive concept               | **New U.Type (rare)**          | Only if cross‑family, irreducible, kernel‑level. |

### F.8:10 - Anti‑patterns & remedies

| #         | Anti‑pattern               | Symptom                                                                            | Why it harms thinking                              | Remedy (conceptual move)                                                                                                                         |
| --------- | -------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AP‑1**  | **Row‑less sameness**      | Declaring “these mean the same” across Contexts without citing a **Concept‑Set row**. | Imports meaning implicitly; no CL guard.           | If Cross‑context reuse is desired, **reuse an existing row** at a declared **scope** (F.7), else **publish the contrast** and defer to F.9 Bridges. |
| **AP-2**  | **Scope creep**            | Using a **Naming-only** row to justify **Assignment-eligibility** or structural inferences. | Over-claims sameness; breaks τ(scope).             | Respect **scope thresholds** (τ). Upgrade only when **Row CL(min) ≥ τ(new scope)**; otherwise stay Naming-only.                                  |
| **AP‑3**  | **Alias with payload**     | Introducing an Alias that subtly changes intent or senseFamily.                          | Hides semantics behind wording; confuses senseFamilies.   | Aliases (F.5) are **style only**. If semantics change, choose **row reuse** or **Role Description** instead.                                         |
| **AP-4**  | **Role-Description-to-row anchoring** | Role Description points to a **row** rather than a **single SenseCell**.       | Masks locality; **assignments** become cross-context by stealth. | Role Descriptions **must anchor to one SenseCell** (F.4). Use rows only in prose or aggregated views.                                                |
| **AP‑5**  | **Kernel inflation**       | Proposing a new **U.Type** because a convenient label is missing.                  | Duplicates the kernel; violates parsimony.         | Apply A.8: require **≥ 3 domain families** and **irreducibility**; otherwise **Alias** or **row**.                                               |
| **AP‑6**  | **senseFamily mixing**           | One name that conflates Role, Status, Measurement, or Type‑structure.              | Collapses A.7 Strict Distinction.                  | **Split by senseFamily** first (Q0). Decide **per senseFamily**.                                                                                             |
| **AP‑7**  | **Bridge‑by‑string**       | Treating identical surface forms as equivalent senses across Contexts.                | Homonym trap; ignores local sense.                 | Equivalence only via **F.9 Bridge** + **row**; never by string.                                                                                  |
| **AP‑8**  | **Row without loss notes** | Publishing a row where Bridges indicate mismatches, but row text is silent.        | Readers assume full equivalence.                   | Include **counter‑example** and **loss sketch** in the row’s narrative (F.7).                                                                    |
| **AP‑9**  | **CL laundering**          | Citing a high‑scope row based on old high CL while Bridges have since weakened.    | Invalidates downstream claims.                     | When CL falls below τ(scope), **downgrade row scope** (e.g., to Naming‑only) or **split row**.                                                   |
| **AP‑10** | **Global normal form**     | Seeking one canonical wording across all Contexts **as if** meaning were global.      | Erases locality; fuels hidden merges.              | Keep normalisation **per Context** (F.2/F.3). Cross‑context sameness lives in **rows** with scope.                                                     |


### F.8:11 - Reasoning primitives (judgement schemas, notation‑free)

> Each item states a **mental entailment**. No storage, no roles, no workflows. Symbols: `C` = Context, `σ` = SenseCell, `R` = Concept‑Set row, `SF` = senseFamily, `τ` = scope threshold, `CL` = congruence level.

1. **senseFamily split**
   `need(n) ∧ mixedSF(n) ⊢ split(n) into {n₁…nₖ} by senseFamily`
   *You cannot decide for mixed senseFamilies; decide per senseFamily.*

2. **Cell reuse**
   `∃ C,σ : expresses(n,SF)@σ ⊢ reuseLabel(σ) in C`
   *If a single Context’s SenseCell already says it, reuse it locally.*

3. **Assignment-eligibility**
   `reuseLabel(σ) ∧ needAssignable(SF ∈ {Role,Status}) ⊢ mintRoleDescription(σ)`
   *When you need assignable behaviour/deontics for a local sense, mint a Role Description anchored to that sense.*

4. **Row reuse**
   `crossContexts(n,SF) ∧ ∃ R: covers(R,SF) ∧ CL(R) ≥ τ(scope) ⊢ reuseRow(R,scope)`
   *For Cross‑context readings, reuse a row at a scope whose τ is met.*

5. **Alias suffices**
   `sameIntent(n,label₀) ∧ stylePreference(n,label₁) ⊢ alias(label₀,label₁)`
   *If it’s only wording, add an Alias; no semantics move.*

6. **Row proposal**
   `recurrentCross(n,SF) ∧ bridgesCL(cells(n)) ≥ τ(scope) ∧ ¬∃R ⊢ proposeRow(cells,scope)`
   *If the need recurs and Bridges support the scope, propose a new row.*

7. **Kernel minting (rare)**
   `kernelCandidate(n) ∧ crossFamily≥3 ∧ irreducible(n) ⊢ proposeUType(n)`
   *Only if the notion is cross‑family and cannot be reduced to cells+rows+existing U.Types.*

8. **Scope downgrade**
   `reuseRow(R,scope) ∧ CL(R)↓ < τ(scope) ⊢ downgradeScope(R)`
   *If CL falls, lower the row’s licensed scope.*

9. **Row rejection**
   `conflictEvidence(rowCells) ∧ lossUnbounded ⊢ rejectRow`
   *If bridges show open‑ended loss, do not publish a row; teach the contrast.*


### F.8:12 - Extended worked examples

#### F.8:12.1 - **Execution, observation, and acceptance** (engineers)

**Need.** A reusable label for “what actually happened and how it was checked against the promise”.
**senseFamilies.** Execution (stance: run); Measurement (KD); Status (accept/reject).

**Contexts.**
`IEC 61131‑3` (task run), `PROV‑O` (Activity), `SOSA/SSN` (Observation), `ITIL 4` (SLO/SLA).

**Reasoning.**

* `Execution`: `IEC` SenseCell (task run) and `PROV` SenseCell (Activity). There exists a **row** *execution-occurrence* at **Assignment-eligibility** with CL = 2 → **reuse row** at **Assignment-eligible** scope; do not infer Type-structure.
* `Measurement`: `SOSA` Observation cell; no Cross‑context needed → **reuse cell**.
* `Status`: `ITIL` SLO/SLA cell; **Role Description** “SLO‑Target” anchored to ITIL cell.

**Outcome.** Prose may say: “This **execution-occurrence** (row\@assignment/enactment-eligibility) was **observed** (SOSA cell) and **evaluated against the SLO** (ITIL cell).” No new U.Type; no hidden merges.


#### F.8:12.2 - **Actor across workflow and provenance** (managers)

**Need.** A single everyday label for “the responsible party” in diagrams.
**senseFamily.** Role (behavioural mask in prose/diagrams).

**Contexts.** `BPMN 2.0` (Participant), `PROV‑O` (Agent).

**Reasoning.** A **Naming‑only** row “actor” exists, CL = 2. **Reuse the row** at Naming‑only.
If assignable behaviour is needed in a model, **mint Role Description** anchored to **BPMN Participant** (not to the row).

**Outcome.** Diagrams show “actor”; formal sections reference `Participant` or `Agent` as appropriate.


#### F.8:12.3 - **Accuracy across metrology and data quality** (researchers)

**Need.** Treat “accuracy” consistently across ISO 80000 (metrology) and ISO/IEC 25024 (data quality).
**senseFamily.** Measurement.

**Contexts.** `ISO 80000‑1` (quantity/units), `ISO/IEC 25024` (data quality).

**Reasoning.** Bridges indicate **related but not identical** definitions; procedures differ. Existing **KD‑metric** row “accuracy” has CL = 2 with **loss note**: *population vs instrument focus*. **Reuse row** at KD‑metric scope for dashboards; **do not** use the row to justify interchange of procedures.

**Outcome.** One label in reports; method sections still cite the context‑local procedure.


#### F.8:12.4 **Subtype relation across OWL and a curated taxonomy** (formalists)

**Need.** Present “is‑a” uniformly across OWL 2 classes and a domain taxonomy.
**senseFamily.** Type‑structure.

**Contexts.** `OWL 2` (SubClassOf), `Taxonomy_X` (curated “is‑a” edges).

**Reasoning.** F.7 row “subtype‑order” exists at **Type‑structure scope** with CL = 3 (only after verifying acyclicity & anti‑symmetry in `Taxonomy_X`). If the curated taxonomy contains cycles, **downgrade** to Naming‑only or reject the row.

**Outcome.** When CL≥3, you may **reuse row** for structural proofs; else teach differences.


### F.8:13 - Relations (with other patterns)

* **Builds on:** E.10.D1 (D.CTX) **Context ≡ U.BoundedContext**; F.1 Contexts; F.2 Harvest; F.3 SenseCells.
* **Constrains:**

  * **F.4 Role Description:** **one SenseCell per Role Description**; no row anchoring.
  * **F.5 Naming:** Aliases are style‑only; no semantics movement.
  * **F.7 Concept‑Set:** rows must declare **Scope** & **Row CL(min)** and carry **loss notes**.
  * **F.9 Bridges:** any row proposal presupposes Bridges at or above τ(scope).
* **Used by.** All patterns (Part C) whenever new labels are contemplated.


### F.8:14 - Migration notes (conceptual)

1. **Old “anchor” language.** Replace legacy “anchor” with: **SenseCell** (local sense) + **Role Description** (assignable Standard) + (optionally) **Concept‑Set row** (Cross‑context reading).
2. **Over-strong rows.** If a row was used for **assignment/enactment-eligibility** or **Type-structure** but **CL drops**, **downgrade row scope** to **Naming-only** in prose; adjust examples.
3. **Split rows.** If one row covers cells whose Bridges diverge, **split** into two narrower rows with explicit loss notes.
4. **Alias proliferation.** Collapse redundant Aliases under a single F.5 entry; keep both registers (Tech/Plain).
5. **Proto‑types.** Suspect kernel inflation? Attempt **reduction**: SenseCell + row + existing U.Type. Only if irreducible across ≥ 3 families, reopen as a U.Type candidate.


### F.8:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.8:15.1 - Static conformance (SCR)

* **SCR‑F8‑S01 (senseFamily purity).** Every decision record names **one senseFamily**; mixed needs are split.
* **SCR‑F8‑S02 (Proper anchoring).** Every Role Description cites **one SenseCell**; **no row** is used as a assignment/enactment anchor.
* **SCR‑F8‑S03 (Row scope).** Whenever a row is reused, its **Scope** is stated and **Row CL(min) ≥ τ(scope)** holds.
* **SCR‑F8‑S04 (Alias modesty).** Aliases introduced in F.5 do **not** claim new semantics or change senseFamily.
* **SCR‑F8‑S05 (Kernel restraint).** Any new U.Type proposal includes **≥ 3 domain families** of evidence and an **irreducibility** note.

#### F.8:15.2 - Regression (RSCR)

* **RSCR‑F8‑E01 (CL drift).** If any Bridge’s CL changes, re‑evaluate dependent rows; **downgrade or split** where τ(scope) is no longer met.
* **RSCR-F8-E02 (Row overuse).** Scan examples: no case uses **Naming-only** rows to justify **Assignment-eligibility** or **Type-structure** claims.
* **RSCR‑F8‑E03 (Alias creep).** Ensure no Alias has accreted senseFamily‑specific semantics; if it has, migrate to a **row** or **Role Description**.
* **RSCR‑F8‑E04 (Kernel hygiene).** New U.Type proposals are rejected if a **SenseCell + row** construction suffices.


### F.8:16 - Didactic distillation (90‑second teaching script)

> “When you feel like coining a new name, pause. **Which senseFamily** are you in—Role, Status, Measurement, Type‑structure, Method, or Execution? If a **single Context’s SenseCell** already says it, **reuse** that label. If you need an assignable Standard, **mint a Role Description** anchored to that SenseCell. If you must read **across Contexts**, reuse a **Concept‑Set row**—but only **at a stated scope** and only if its **CL meets the threshold** (τ). If it’s just a nicer wording, add an **Alias** (style only). Only in the rare case of a cross‑family, **irreducible** notion do you **mint a new U.Type**. Never let Naming‑only rows justify  **Assignment-eligibility** or structural inference, and never let identical strings force equivalence. This is not process—it’s **discipline of thought**: reuse what exists, declare scope when you bridge, and mint new primitives only when the kernel truly needs them.”

### F.8:End

## F.9 - Alignment & Bridge across Contexts

**“Translate across Contexts; never collapse them.”**
**Status.** Architectural pattern.
**Builds on:** E.10.D1 (Context discipline: Context ≡ U.BoundedContext); **F.0.1 (senseFamily & StatusModality guard; Bridge‑only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds τ).

**Coordinates with.** B.3 **Trust & Assurance Calculus** (uses CL penalties); **A.6.1 U.Mechanism** (Transport clause for cross‑context use; penalties route to **R/R_eff** only; **F/G** invariant); Part C patterns (apply Bridges in formal claims); A.6.9 (RPR‑XCTX for repairing umbrella “same/equivalent/align/map” prose into explicit Bridge Cards).
**Aliases (informative).** *Context‑to‑Context translator*; *Sense bridge*.

### F.9:1 - Intent & applicability

**Intent.** Provide a **conceptual discipline** for relating **SenseCells** from **different Contexts (U.BoundedContext)**. A **Bridge** states *what kind* of relationship holds, *how far* it holds (via **CL: Congruence Level**), and *what is lost* during the translation. Bridges **permit carefully scoped reuse** (e.g., a Concept‑Set row) while **forbidding silent equivalence**.

**Applicability.** Use **whenever** an author needs to **read across Contexts**—to reuse a familiar label, to connect design‑time and run‑time notions, to compare two standards’ terms, or to justify a row in the Concept‑Set table. This pattern is **not** storage, workflow, or governance; it codifies **thinking moves**.

**Non‑goals.** No global meaning; no tool/API; no editor roles. Bridges are **semantic relations between local senses**, not pipelines, not processes.

### F.9:2 - Problem frame

Cross‑context work fails in predictable ways:

1. **String‑equals fallacy.** Identical surfaces (“process”, “role”, “accuracy”) taken as identical meaning.
2. **Scope creep.** A naming convenience is stretched to assignment or structural claims.
3. **DesignRunTag jumping.** Design artefacts are substituted for run‑time occurrences (or vice‑versa).
4. **Direction amnesia.** Narrower/broader relations treated as symmetric.
5. **Loss blindness.** Differences (units, granularity, preconditions) are left unstated, contaminating downstream reasoning.

Bridges cure these by **making relation, direction, loss, and strength explicit**.


### F.9:3 - Forces

| Force                           | Tension to resolve                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| **Locality vs reuse**           | Senses are context‑local, yet people need a common label to talk across Contexts.              |
| **Simplicity vs fidelity**      | Few Bridge kinds are teachable; too few will hide real mismatches.                       |
| **Safety vs utility**           | Allow some substitution when safe; forbid it when loss is unbounded.                     |
| **senseFamily purity vs explanation** | Substitution must preserve **senseFamily**; explanation may span **senseFamilies** without implying sameness. |


### F.9:4 - Core idea (didactic)

**A Bridge is a declared translator between two local senses.**
It always names **(a)** the two **SenseCells**, **(b)** a **Bridge‑kind** (what relation), **(c)** a **direction** (if non‑symmetric), **(d)** a **CL** (how strong), and **(e)** **Loss Notes** (what fails to carry). Some Bridges **permit substitution** in limited scopes; others **permit only explanation**.


### F.9:5 - Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell** — the pair *(Context × Local‑Sense)* from F.3.
* **Bridge** — a conceptual relation between two SenseCells with kind, direction, CL, and loss notes.
* **CL (Congruence Level)** — ordinal strength (0…3) of a Bridge (see §7).
* **Scope** — the **licensed use** of a Cross‑context reading (as in F.7/F.8):

* **Naming‑only** (talk consistently),
* **Role Assignment & Enactment-eligibility** (assignable constraints/roles/status reuse),
* **Type‑structure** (safe structural inference).
* **senseFamily** — the semantic category (Role, Status, Measurement, Type‑structure, Method, Execution…) per F.0.1 (normative Part F guard).


### F.9:6 - Bridge kinds (senseFamily‑aware)

> **Two families** of Bridges: **Substitution Bridges** (senseFamily‑preserving; can support Concept‑Set rows) and **Interpretation Bridges** (explanatory; **not** for substitution).

#### F.9:6.1 - Substitution Bridges (sense‑preserving)

These relate **SenseCells of the same senseFamily** and may license **limited substitution**:

1. **Equivalence (≈)** — *near‑identity of sense*. Symmetric. Rare.
   *Use:* May support **Type‑structure** rows when CL=3 and invariants match.
   *Loss Notes:* usually “none” or “profiling differences”.

2. **Narrower‑than (⊑)** / **Broader‑than (⊒)** — *proper inclusion of sense*. Directional.
  *Use:* Safe to substitute **narrower → broader** in **Naming-only** and sometimes **Role Assignment & Enactment**; **broader → narrower** is unsafe.
   *Loss Notes:* “loses special cases X”.

3. **Partial‑overlap (⋂)** — *non‑empty intersection, neither includes the other*.
  *Use:* **Naming-only** at best. **Never** justifies Role Assignment & Enactment / Type-structure.
   *Loss Notes:* “A-only senseFamily”, “B-only senseFamily”.

4. **Disjoint (⊥)** — *explicit contrast*.
   *Use:* For **didactic warnings**; not a reuse license.
   *Loss Notes:* n/a (it asserts incompatibility).

#### F.9:6.2 - Interpretation Bridges (cross‑senseFamily, explanatory)

These **do not allow substitution** but **explain connections** across senseFamilies:

5. **Design‑spec ↔ Run‑trace (⇄ᴅʀ)** — a design concept relates to its run‑time occurrence.
   *Example:* *BPMN\:Process* ⇄ᴅʀ *PROV\:Activity*.
   *Use:* Explain pipelines (design → execution → provenance). No Concept‑Set rows.
   *Loss Notes:* “graph vs event”, “control‑flow vs temporal extent”.

6. **Measure‑of / Evidence‑for (→ᴍᴇᵃ)** — a measurement SenseCell evidences or quantifies another **senseFamily** (e.g., a Requirement clause).
   *Example:* *SOSA\:Observation* →ᴍᴇᵃ *ITIL\:SLO fulfilment*.
   *Use:* Explain evaluation. No substitution.

7. **Policy‑implies / Obliges (→ᴅᵉᵒ)** — a deontic statement constrains another **senseFamily**.
   *Example:* *ODRL\:Duty* →ᴅᵉᵒ *Service behaviour*.
   *Use:* Explain constraint propagation.

> **Rule of thumb.** If you want **rows** or **substitution**, you need a **Substitution Bridge** on the **same senseFamily**. If you want to **explain** why artefacts relate without claiming sameness, use **Interpretation Bridges**.


### F.9:7 - CL scale and scope thresholds

CL expresses how safely meaning carries over.

| CL    | Name              | Intuition                                            | Typical loss         | Row scope allowed (τ thresholds) |
| ----- | ----------------- | ---------------------------------------------------- | -------------------- | -------------------------------- |
| **0** | **Opposed**       | Intentionally contrastive or disjoint                | n/a                  | none                             |
| **1** | **Comparable**    | Talk under a shared label; senses differ materially  | material sense divergence | **Naming‑only** (τₙₐₘₑ=1)        |
| **2** | **Translatable**  | Bounded loss; consistent examples & counter-examples | small, stated losses | **Role Assignment & Enactment-eligibility** (τRAE=2)     |
| **3** | **Near‑identity** | Invariants match; no material counter‑example        | profile‑level only   | **Type‑structure** (τᵗʏᴘᴇ=3)     |

* **Thresholds (normative):**

  * Publishing a **Naming‑only** row requires **CL ≥ 1** across the row’s Cells.
 * Publishing a **Role Assignment & Enactment-eligible** row requires **CL ≥ 2** and **same senseFamily**, and **compatible stance**..
  * Publishing a **Type‑structure** row requires **CL = 3** **and** matched invariants (acyclicity, anti‑symmetry, units, etc.).

* **Penalty use (informative):** B.3 may convert **CL** into an assurance **penalty** when a Cross‑context claim is made.


### F.9:8 - The Bridge Card (one‑screen sketch)

> A **thought‑format** (not a form). Every bullet can be said in a sentence.

* **Cells.** `σA@contextA` ↔ `σB@contextB`.
* **senseFamily.** *Role / Status / Measurement / Type‑structure / Method / Execution …*
* **Kind.** *≈ / ⊑ / ⊒ / ⋂ / ⊥ / ⇄ᴅʀ / →ᴍᴇᵃ / →ᴅᵉᵒ*.
* **Direction.** *A→B* (if non‑symmetric) or *A↔B*.
* **CL.** *0–3* with a short **why**.
* **Loss Notes (bullets).** What fails to carry (units, scope, granularity, preconditions, time stance).
* **Counter‑example.** The crispest case where substitution would mislead.
* **Allowed use.** *Naming-only / Role Assignment & Enactment-eligible / Type-structure / Explanation-only*.
* **Didactic hook.** The helpful sentence a careful engineer can remember.

*If your Bridge Card doesn’t fit on a screen, you’re describing the Contexts, not the Bridge.*

**Registry-reference note (normative).** `BridgeId` and any policy/edition identifiers cited by a Bridge Card are **registry references** (keys into registries), not semantic symbols exported by signatures. Therefore they MUST NOT be demanded via `SignatureManifest.provides` (or “satisfied” via `imports` closure); conformance is checked by validating that the referenced registry entries exist and, where required, are edition‑pinned (see F.15).


### F.9:9 - Invariants (normative)

1. **Locality first.** A Bridge relates **SenseCells**, never Contexts or strings.
2. **senseFamily discipline.** **Substitution Bridges must be senseFamily‑preserving**. **Interpretation Bridges** may cross senseFamilies but **never** license substitution.
3. **Direction clarity.** If the kind is non‑symmetric (⊑/⊒), **state direction** explicitly.
4. **CL honesty.** Assign **CL** only if you can state at least one **counter‑example** (CL≤2) or explain its absence (CL=3).
5. **Loss visibility.** Every Bridge carries **Loss Notes** (even “none”).
6. **Row dependence.** A Concept‑Set row’s **scope** is **bounded by the weakest CL** among its participating Bridges (F.7/F.8).
7. **No senseFamily jump by stealth.** You **must not** use an Interpretation Bridge to justify a **row** or **substitution**.
8. **Time DesignRunTag honesty.** If a Context fixes **design/run**, the Bridge must respect or explicitly declare stance relations (e.g., ⇄ᴅʀ).
9. **Kernel restraint.** Bridges **cannot** be used to promote ad‑hoc sameness into a new **U.Type**; A.11 applies.
10. **Non‑inheritance of Contexts.** Bridges **do not** imply “is‑a” between Contexts (E.10.D1).


### F.9:10 - Micro‑examples (illustrative, one‑liners)

1. **Participant vs Agent (workflow vs provenance)**
   *Cells:* `BPMN:Participant` ↔ `PROV:Agent` • *senseFamily:* Role • *Kind:* ⋂ (overlap) • *CL:* 2 • *Loss:* participation vs attribution scopes differ • *Use:* **Naming‑only** (“actor”).

2. **Process (design) vs Activity (run)**
   *Cells:* `BPMN:Process` ⇄ᴅʀ `PROV:Activity` • *senseFamily:* Method ↔ Execution • *Kind:* **Design‑spec ↔ Run‑trace** • *CL:* 2 • *Loss:* graph vs event; concurrency vs temporalization • *Use:* **Explanation‑only**.

3. **Observation vs SLO check**
   *Cells:* `SOSA:Observation` →ᴍᴇᵃ `ITIL:SLO‑fulfilment` • *senseFamily:* Measurement → Status • *Kind:* Measure‑of • *CL:* 2 • *Loss:* sampling window; target definition • *Use:* **Explanation‑only**.

4. **Subtype across OWL and curated taxonomy**
   *Cells:* `OWL:SubClassOf` ≈ `TaxonomyX:is‑a` • *senseFamily:* Type‑structure • *Kind:* ≈ • *CL:* 3 *(only if TaxonomyX is acyclic & anti‑symmetric)* • *Loss:* profile differences • *Use:* **Type‑structure** rows allowed.

5. **Accuracy (metrology vs data‑quality)**
   *Cells:* `ISO80000:accuracy` ⋂ `ISO25024:accuracy` • *senseFamily:* Measurement • *Kind:* overlap • *CL:* 2 • *Loss:* instrument vs dataset perspective • *Use:* **Naming‑only** row “accuracy”; methods stay context‑local.

### F.9:11 - Anti‑patterns & remedies

| ID        | Anti‑pattern                     | Symptom                                                                           | Why it breaks thinking                              | Remedy (conceptual move)                                                                                    |
| --------- | -------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **String‑equals ≡ sense‑equals** | Same surface used across Contexts with silent identity claims.                       | Violates locality; invites false substitution.      | Always state a **Bridge kind**; if unsure, default to **⋂ overlap** with **Naming‑only** scope.             |
| **AP-2**  | **Stealth substitution**         | “We’ll just treat A like B for now.”                                              | Hidden policy with unknown loss; leaks into Role Assignment & Enactment.    | Publish a **Bridge Card** with **Loss Notes** and **CL**; if CL<2, substitution remains **forbidden**.      |
| **AP‑3**  | **Stance jump by wording**        | “Activity (PROV) is a Process (BPMN).”                                            | Design ↔ run confusion; swaps graphs for events.    | Use **⇄ᴅʀ design↔run Interpretation Bridge**, **not** ≈/⊑; keep **Explanation‑only** scope.                 |
| **AP‑4**  | **Symmetry hallucination**       | Treating ⊑/⊒ as if they were symmetric.                                           | Narrows broadened, broadens narrowed; unsafe reuse. | Record **direction** explicitly; only **≈** is symmetric.                                                   |
| **AP-5**  | **Disjoint but reused**          | Declare ⊥ then still borrow labels or Role Description constraints (RCS/RSG).     | Contradiction between declaration and use.          | Either retract ⊥ or stop reuse; if a thin thread exists, rename as **contrastive explanation** (no row).    |
| **AP‑6**  | **CL without counter‑example**   | “These are CL=3” with no invariant check.                                         | Inflates trust; permits structural rows wrongly.    | For **CL=3**, cite the **matching invariants**; otherwise, demote to **CL=2** and add counter‑example.      |
| **AP‑7**  | **Bridge inflation**             | Dozens of nearly identical Bridges between the same Contexts.                        | Noise masks the few material alignments.            | Prefer **one Bridge per pair of Cells per senseFamily**; fold variants into **Loss Notes**.                       |
| **AP-8**  | **Row outruns Bridge**           | Concept-Set row claims Role Assignment & Enactment-eligibility where some participating Bridges are CL=1. | Row scope exceeds weakest link.                     | Apply **weakest-link rule** (F.7/F.8): row scope ≤ **min(CL)**; otherwise split the row.                    |
| **AP‑9**  | **Bridge as new U.Type**         | Using a Bridge to justify minting a new universal Type.                           | Re‑globalises meaning; breaks A.11 parsimony.       | Keep Types context‑local; where reuse is needed, use **rows** + Bridges, not new primitives.                   |
| **AP‑10** | **Silent unit/scale mismatch**   | Mapping measurements without unit/scale notes.                                    | Hidden dimensional error.                           | Record units/scales in **Loss Notes**; if units can’t be related, the kind is **⊥** or **⋂ (Naming‑only)**. |


### F.9:12 - Worked examples (didactic)

#### F.9:12.1 - Service acceptance (design) vs executions & observations (run)

* **Cells & Contexts**
  `ITIL4:SLO` *(Status, design)* ← **→ᴍᴇᵃ** — `SOSA:Observation(availability)` *(Measurement, run)*
  `BPMN:Process` *(Method, design)* ⇄ᴅʀ — `IEC61131:Task‑Execution` *(Execution, run)*
* **Narrative**
  Availability SLOs are **evaluated** by observations of task executions. No substitution: SLO ≠ observation; process ≠ execution.
* **Bridge Cards (sketch)**
  *ITIL\:SLO ←→ᴍᴇᵃ SOSA\:Observation* • **CL=2** • Loss: sampling window, clock skew.
  *BPMN\:Process ⇄ᴅʀ IEC\:Execution* • **CL=2** • Loss: control‑flow vs temporalization, concurrency collapse.
* **Permitted use**
  Explanation‑only; Concept‑Set rows may be **Naming‑only** (“availability”) with **CL≥1** label coherence across Contexts.


#### F.9:12.2 - Behavioural role vs access role

* **Cells & Contexts**
  `BPMN:Participant` *(Role)* ⋂ `NIST‑RBAC:Role` *(Status)*
* **Narrative**
  Both talk about “who acts”, but one is **behavioural mask** in a workflow, the other **permission grouping**.
* **Bridge**
  **Kind:** overlap (⋂), **CL=2**; Loss: assignment moment, enforcement locus, multiplicity.
* **Permitted use**
* **Naming-only** row “actor”; **no Role Assignment & Enactment reuse** across senseFamilies.


#### F.9:12.3 - Equivalence of subtype notions for structural rows

* **Cells & Contexts**
  `OWL2:SubClassOf` *(Type‑structure)* ≈ `TaxX:is‑a` *(Type‑structure curated)*
* **Bridge**
  **Kind:** ≈, **CL=3** **iff** curated taxonomy is **acyclic & anti‑symmetric** and uses class‑level reasoning.
* **Permitted use**
  **Type‑structure** rows allowed (τᵗʏᴘᴇ); Loss: OWL profile limitations (RL/EL/QO).


#### F.9:12.4 - Accuracy (metrology) vs accuracy (data‑quality)

* **Cells & Contexts**
  `ISO80000:measurement‑accuracy` *(Measurement)* ⋂ `ISO25024:data‑accuracy` *(Measurement)*
* **Bridge**
  **Kind:** overlap, **CL=2**; Loss: “true value” notion differs (instrument vs dataset), scale transformations.
* **Permitted use**
  **Naming‑only** row “accuracy” used for reports; no shared methods.


#### F.9:12.5 - Setpoint (control) vs target (service)

* **Cells & Contexts**
  `CTRL:text:setpoint` *(Status/Control)* ⊥ `ITIL:target` *(Status/Service)*
* **Bridge**
  **Kind:** disjoint (⊥) • Rationale: physical reference value vs business objective; different target kinds (control parameters vs requirement clause).
* **Permitted use**
  Didactic contrast only; prevents accidental substitution in SLO calculus.

#### F.9:12.6 - Role substitution & CL gating (RoleAssignment/enactment scope)

> **Use.** A worked, role‑focused restatement of Bridge usage for the recurring question:
> “May `Role_B@B` satisfy `Role_A@A` for `requiredRoles` / enactment checks?”

**Rule.** **No Cross‑context substitution by name.** If a step in **Context A** needs `Role_A`, and the performer only holds `Role_B` in **Context B**, an explicit **Bridge** **MUST** be used that states how `Role_B@B` relates to `Role_A@A`, with direction, **CL**, and **loss notes**.

##### F.9:12.6.1 - Directional substitution (role‑oriented shorthand)

A Bridge may assert, *directionally*:

* **`substitutesFor(Role_B@B → Role_A@A)`** with a CL and a list of **kept** and **lost** characteristics (for roles: typical losses are RCS characteristics and/or RSG nuances).
* The reverse direction **does not** follow unless declared (F.9:13.7).

##### F.9:12.6.2 - CL → gating policy (didactic default)

| **CL** | Meaning (intuitive)                     | **Permit** | **Guard**                                                                            | **Block** |
| :----: | --------------------------------------- | :--------: | ------------------------------------------------------------------------------------ | :-------: |
|  **3** | Near‑isomorphic sense; no material loss |    Yes     | None beyond ordinary gates (e.g., window + RSG state)                                |     —     |
|  **2** | Close but with stated losses            |    Yes     | Require **extra evidence** (e.g., additional checklist item) **or** a named reviewer |     —     |
|  **1** | Distant analogy; risky                  | Exception  | Only by explicit **Waiver SpeechAct** naming the Bridge + loss rationale             |  Default  |
|  **0** | Incompatible                            |     No     | —                                                                                    |    Yes    |

*Notes.* The **substitution licence** is defined in **F.9:13.2–13.3** (Role‑Assignment/Enactment‑eligible substitution requires **CL≥2**; naming‑only is **CL≥1**).  
CL penalties route to assurance (R) per **B.3**; safety‑critical policies may require CL≥2 by default (D.2).

##### F.9:12.6.3 - Typical bridges (worked patterns)

* **BPMN Task ↔ PROV Activity.**  
  `substitutesFor(Task@BPMN → Activity@PROV)` with **CL=2**; **lost:** BPMN control‑flow guards; **kept:** “bounded occurrence consuming/producing entities.”  
  *Effect.* A Work logged as `Activity@PROV` may satisfy a step requiring a `Task@BPMN` **iff** an extra guard enforces the BPMN pre‑/post‑conditions.

* **Essence Alpha‑State ↔ RoleStateGraph state.**  
  `substitutesFor(“Alpha.State:Ready”@Essence → “Ready”@RSG)` with **CL=2**; **lost:** Alpha‑specific narrative criteria; **kept:** checklist‑based readiness.  
  *Effect.* A team may reuse Essence states as labels in RSG, but still maintains local checklists as **StateAssertions**.

* **ITIL Service Owner ↔ RBAC Administrator.**  
  Typically **CL=1** and **directional** (Administrator\@RBAC → ServiceOwner\@ITIL) **rejected** unless a policy Bridge enumerates compensating controls.  
  *Effect.* Prevents “ops admin = service owner” conflations without an explicit waiver.

##### F.9:12.6.4 - Bridge invariants (role‑relevant reminders)

* **Local first.** Substitution never overrides in‑Context role algebra (`≤`, `⊥`, `⊗`).
* **Loss honesty.** If a Bridge’s loss notes indicate that a dropped characteristic is required by a step, substitution is invalid (regardless of CL).
* **No silent inversion.** Direction is explicit; substitution does not reverse unless declared (F.9:13.7).

### F.9:13 - Reasoning primitives (judgement schemas)

> **All judgements are conceptual.** They license or forbid specific *thinking moves*—not API calls, not workflows.

#### F.9:13.1 - Bridge declaration

`⊢ Bridge(σA@RA, σB@RB) : ⟨senseFamily, kind, dir, CL, Loss, scope⟩`

*Reading:* There exists a declared Bridge between SenseCells `σA` and `σB` with stated attributes.


#### F.9:13.2 - Substitution licence (senseFamily‑preserving)

`Bridge(σA,σB): ⟨senseFamily f, kind∈{≈,⊑,⊒}, dir A→B, CL≥2, Loss L⟩ ⊢ A↠B @f (Role Assignment & Enactment-eligible)`

*Reading:* A **Substitution Bridge** on the same senseFamily with **CL≥2** licenses **Role-Assignment/Enactment-level** substitution **in the stated direction**. (Type-structure requires **CL=3**.)


#### F.9:13.3 - Naming‑only licence

`Bridge(σA,σB): ⟨kind∈{≈,⊑,⊒,⋂}, CL≥1⟩ ⊢ A⇝B (Naming‑only)`

*Reading:* A Bridge with **CL≥1** supports using a shared label in prose or Concept-Set **Naming-only** rows, without structural or Role Assignment & Enactment commitments.


#### F.9:13.4 - Prohibition by kind

`Bridge(σA,σB): ⟨kind=⊥⟩ ⊢ ¬(A↠B) ∧ ¬(row(A,B))`

*Reading:* **Disjoint** forbids substitution and rows; only contrastive teaching is allowed.


#### F.9:13.5 - Interpretation embargo

`Bridge(σA,σB): ⟨kind∈{⇄ᴅʀ,→ᴍᴇᵃ,→ᴅᵉᵒ}⟩ ⊢ Explanation‑only`

*Reading:* **Interpretation Bridges** never license substitution or rows.


#### F.9:13.6 - Weakest‑link rule for rows

`row R uses {Bridge_i} ⊢ scope(R) = min_i(scopeAllowed(Bridge_i)) ∧ CL(R)=min_i(CL_i)`

*Reading:* The **row scope** and **row CL** are bounded by the weakest participating Bridge.


#### F.9:13.7 - Direction guard

`Bridge kind=⊑ with dir A→B ⊢ ¬(B↠A)`

*Reading:* Narrower→Broader does **not** invert; only A may substitute into B under the stated scope.


#### F.9:13.8 - SenseFamily purity

`Bridge scope=Role Assignment & Enactment-eligible ⊢ senseFamily(A)=senseFamily(B) ∧ stance(A)=stance(B)`

*Reading:* Role Assignment & Enactment-level substitution requires **same senseFamily** and same stance (run-time or design time).


#### F.9:13.9 - Loss accumulation

`A↠B with Loss L₁ ∧ B↠C with Loss L₂ ⊢ A↠C allowed only if same senseFamily ∧ CL=min(CL₁,CL₂) ∧ Loss ⊇ (L₁∪L₂)`

*Reading:* Chained substitution is rarer; if used, **accumulate Loss** and respect the **minimum CL**. When in doubt, avoid chaining across Contexts.


### F.9:14 - Relations

**Builds on:** E.10.D1 (Context discipline: Context ≡ U.BoundedContext); **F.0.1 (senseFamily guard; Bridge‑only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds τ).

**Constrains:**

* **F.7 Concept‑Set Table:** each Cross‑context row must name supporting **Bridges**; row scope ≤ weakest Bridge.
* **F.8 Mint or Reuse?:** reuse choices reference **CL** and **kind**; no reuse without a Bridge.
* **Part C patterns:** formal claims that span Contexts cite Bridges and respect senseFamily/StatusModality & CL constraints.
* **B.3 Trust & Assurance Calculus:** may interpret **CL** as a penalty factor in Cross‑context reasoning.


### F.9:15 - Migration notes (conceptual)

1. **Edition shift in a Context.** Re‑read affected **Cells**; if sense moved, split the Bridge or **lower CL**; keep the older Bridge for historical claims.
2. **New evidence of mismatch.** Add a **counter‑example**; **decrease CL** or change **kind** (e.g., from ≈ to ⊑ or ⋂).
3. **Convergence over time.** When invariants demonstrably match, and counter‑examples evaporate, **raise CL** cautiously; for **CL=3**, cite invariants.
4. **senseFamily refactor.** If a Cell’s senseFamily was mis‑typed, fix the senseFamily first in F.3, then revisit Bridges; **Interpretation** is safer than forced substitution.
5. **Row under‑protected.** If a row’s scope exceeds the weakest Bridge, either **split the row** by Context or **downgrade scope** to Naming‑only.
6. **Bridge sprawl.** Consolidate near‑duplicates into one Bridge with richer **Loss Notes**; retire the rest.


### F.9:16 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.9:16.1 - Static conformance (SCR)

* **SCR‑F9‑S01 (Well‑typed).** Every Bridge names **two SenseCells**, each bound to a **Context** from F.1, and states **senseFamily**, **kind**, **dir** (if needed), **CL**, **Loss**, **scope**.
* **SCR‑F9‑S02 (senseFamily discipline).** Any Bridge that licenses **Role/Enactment-eligible** substitution is **senseFamily‑preserving** and **kind ∈ {≈,⊑,⊒}**.
* **SCR‑F9‑S03 (Loss visibility).** Every Bridge has **non‑empty Loss Notes** (the word “none” is allowed only with **CL=3** and stated invariants).
* **SCR‑F9‑S04 (Counter‑example hygiene).** Bridges with **CL≤2** carry at least one **counter‑example**; Bridges with **CL=3** cite **matching invariants**.
* **SCR‑F9‑S05 (Row compliance).** Every Concept‑Set row shows a **scope** no greater than the **minimum CL** across its supporting Bridges; no row relies on **Interpretation** Bridges.

#### F.9:16.2 - Regression (RSCR)

* **RSCR‑F9‑E01 (Edition churn).** When a Context’s edition changes, re‑validate all Bridges touching it; **flag CL drift** and update rows’ scopes if needed.
* **RSCR‑F9‑E02 (Counter‑example drift).** New counter‑examples lower **CL**; deletions do not automatically raise **CL**.
* **RSCR‑F9‑E03 (senseFamily drift).** If a Cell’s senseFamily is corrected, all Bridges crossing that Cell are re‑typed; any substitution that would now cross senseFamilies is **invalidated**.
* **RSCR‑F9‑E04 (Weakest‑link enforcement).** Adding a low‑CL Bridge to a row **reduces** the row’s scope; if the row’s published scope would exceed the new minimum, **split** or **downgrade** the row.


### F.9:17 - Didactic distillation (90‑second script)

> “A **Bridge** translates between **local senses** from different **Contexts**. It always declares **what relation** (≈, ⊑, ⋂, ⊥, or an **interpretation** like design↔run), **how strong** (CL 0–3), **which way** (for ⊑/⊒), and **what is lost**. **Substitution** is allowed only on the **same senseFamily** and only with **CL≥2**; **Type‑structure** needs **CL=3**. **Interpretation Bridges** explain, never substitute. Rows in the Concept‑Set table obey the **weakest‑link**: their scope cannot exceed the lowest CL among their Bridges. When editions change or counter‑examples surface, **lower CL** or change **kind**; if two senses truly converge and invariants match, raise to **CL=3**—rarely, and with reasons. Translate across Contexts; never collapse them.”

### F.9:End

## F.10 - Status Families Mapping (Evidence • Standard • Requirement)

**“Keep statuses in their native modality; translate between Contexts explicitly.”**
**Status.** Architectural pattern.
**Builds on:** E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); F.1 (Contexts), F.2 (Seeds), F.3 (Local‑Senses → SenseCells), F.4 (Role Description **Status** templates), F.9 (Bridges).
**Coordinates with.** B.3 **Trust & Assurance Calculus** (interprets CL penalties); Part C patterns: **KD‑CAL** (measurement semantics), **Norm‑CAL** (deontic logic), **Method‑CAL** (DesignRunTag).


### F.10:1 - Intent & applicability

**Intent.** Provide a **simple, Context‑first way** to express and compare **status meanings** across disciplines **without collapsing modalities** (*epistemic* vs *deontic*). We focus on three pervasive **status families**:

1. **EvidenceStatus** (what the world **shows**) — epistemic modality.
2. **StandardStatus** (what a canon **sanctions**) — deontic (curatorial) modality.
3. **RequirementStatus** (what an obligation is **doing**) — deontic (compliance) modality.

Each status meaning is **local to a Context** (`U.BoundedContext`). Cross‑context relationships appear **only** via **Bridges** (F.9) with a declared **kind** and **CL** (congruence level).

**Applicability.** Whenever models mix observations, standards, and obligations: service acceptance from uptime measurements; safety proofs against normative checklists; ML model “validated” vs “approved for use”.

**Non‑goals.** No workflows, no tool states, no editorial lifecycles. This pattern defines **conceptual meaning and safe reasoning moves**, not procedures.


### F.10:2 - Problem frame

Without a modality‑aware mapping of statuses:

* **Homonym traps.** *Validated* in metrology ≠ *validated* in software QA; *approved* in a standard ≠ *compliant* to a requirement.
* **Design/run bleed.** Design‑time “approved method” is used as if it proved run‑time “meets SLO”.
* **False substitution.** *Observed availability 99.95%* is silently treated as *SLO satisfied* without declaring the translation.
* **Name inflation.** New U.Types minted to stabilise drifting status words instead of fixing Contexts and Bridges.


### F.10:3 - Forces

| Force                                     | Tension to resolve                                                                             |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Local fidelity vs Cross‑context reuse**    | Keep native Context meanings, yet enable explanation and (sometimes) substitution.                |
| **Didactic simplicity vs status variety** | Many status schemes exist; we need a **small spine** that admits Context synonyms.                |
| **Design vs run**                         | Standards speak design; evidence speaks run; requirements span both; do not swap them.         |
| **Safety vs utility**                     | Substitution is powerful but risky; explanation is safer but weaker. Make the choice explicit. |


### F.10:4 - Core idea (didactic)

**Three families, two modalities, one habit.**
Treat every status word as a **SenseCell with a declared StatusModality** and **inside one Context**. When you must relate statuses across Contexts, **declare a Bridge** (F.9) that says *what kind of relation*, *how strong (CL)*, *which way (if narrower/broader)*, and *what is lost*. Prefer **explanation** Bridges; permit **substitution** only when kind/CL allow it.

**Reading an Episteme.** For every `U.Episteme`, read _Object_ (what it is about), _Concept_ (model/postulates), _Symbol_ (carriers). **Statuses classify the Episteme;** enactment remains with `U.System` and `U.Work`. (Formal identity rules: see **KD‑CAL**.)

### F.10:5 - Minimal vocabulary (this pattern only)

* **StatusFamily.** Sub‑typing inside **senseFamily=Status**: one of **EvidenceStatus**, **StandardStatus**, **RequirementStatus**.
* **StatusCell.** A **SenseCell** whose meaning is a status with a declared **StatusModality ∈ {epistemic, deontic}**
* **StatusModality.** The mode of a StatusCell: **epistemic** or **deontic**. Use this term instead of the bare word *modality* per E.10 LEX rules.
* **Polarity.** The orientation of a status relative to a claim/obligation: **Positive** (supports/satisfies), **Negative** (contradicts/violates), **Neutral/Undetermined**.
* **Window.** The **applicability span** of a status (temporal or conditional), e.g., “Q3‑2025”, “under load ≥ 70%”.
* **Target.** What the status is **about**: a **claim** (epistemic), an **artefact or method** (standard), a **clause** (requirement).
* **Bridge (F.9).** The only legal way to relate StatusCells across Contexts; declares **kind** (≈, ⊑, ⊒, ⋂, ⊥, or an Interpretation arrow), **CL**, and **Loss**; **substitution is modality‑preserving**.

> **StatusModality guard.** EvidenceStatus is **epistemic**; StandardStatus & RequirementStatus are **deontic**. **Role Description Status** templates (F.4) bind to these **StatusModalities**; **no mixing**. The bare token *modality* is against E.10/LEX); this pattern uses **StatusModality**.


### F.10:6 - The spine: three local ladders (Context‑native, small and renameable)

> The following ladders are **didactic spines**. Each Context may rename levels or insert thin sub‑levels, but Bridges must state how they align to this spine (kind & CL). Names appear in **Tech** / **Plain** register.

 -   **Episteme‑as‑actor (forbidden).** Never attribute **Work** to an Episteme; only Systems act.
    
-   **Requirement vs Hypothesis.** “Desired property/goal” is **not** `Requirement` status; use hypothesis/target + evaluation.
    
-   **Mereology ≠ Provenance.** Part‑whole edges never justify claims; use EPV‑DAG with carriers.


#### F.10:6.1 - EvidenceStatus (epistemic statusModality)

**Levels (from weaker to stronger):**

1. **Observed** / *Seen once.*
2. **Measured** / *Quantified under a declared procedure.*
3. **Corroborated** / *Seen independently (≥ 2 distinct sources/procedures).*
4. **Replicated** / *Repeated by others under varied conditions.*
5. **Refuted** *(negative polarity)* / *Counter‑evidence overrides prior levels.*
6. **Inconclusive** *(neutral)* / *Insufficient signal.*

**Context alignment examples (illustrative):**
`SOSA/SSN:Observation` ↦ **Observed/Measured**; `GxP validation datapack` may map to **Replicated** (if protocol diversity holds) with **CL stated**.

**Invariants (context‑local):**
*Replicated ⇒ Corroborated ⇒ Measured ⇒ Observed.* Negative (**Refuted**) cancels positives **within the same Window**.


#### F.10:6.2 - StandardStatus (deontic/curatorial statusModality)

**Levels (design‑time stance):**

1. **Candidate** / *Proposed, under review.*
2. **Draft** / *Working text, not normative.*
3. **Approved** / *Normative in this Context/edition.*
4. **Deprecated** *(negative)* / *Discouraged; may be removed.*
5. **Superseded** *(negative)* / *Replaced by a newer edition/profile.*

**Context alignment examples:**
`ISO profile: Published International Standard` ↦ **Approved**; `IETF RFC (Proposed Standard)` ↦ **Draft/Approved** depending on local policy; **CL must be declared** on the Bridge.

**Invariants:**
At most one positive stance at a time **per Context & edition**; **Superseded** implies **Approved** held in a prior Window.


#### F.10:6.3 - RequirementStatus (deontic/compliance statusModality)

**Levels (run‑aware stance toward an obligation):**

1. **Applicable** / *The clause binds in this Window.*
2. **Inapplicable** / *Clause does not bind under stated conditions.*
3. **Satisfied** *(positive)* / *Met within Window.*
4. **Violated** *(negative)* / *Not met within Window.*
5. **Waived** *(neutral/administrative)* / *Binding suspended with justification.*
6. **Pending** *(neutral)* / *Awaiting evaluation or evidence.*

**Context alignment examples:**
`ITIL4:SLO achieved` ↦ **Satisfied**; `ODRL:Duty fulfilled` ↦ **Satisfied**; `ODRL:Prohibition breached` ↦ **Violated**.

**Invariants:**
For the **same clause and Window**, **Satisfied** and **Violated** are **mutually exclusive**. **Applicable** is a **precondition** for either; **Waived** switches off the precondition temporarily.

#### F.10:6.4 - Contextual Citation Operators (pointer)

**Citation operators (context‑scoped).** Authors MAY use the **typed edges** `supports`, `refutes`, `dependsOn`, `supersedes` **inside a single Context** when expressing how an `Evidence`/`Standard` status applies. **Formal semantics live in B.3.2 (Evidence & Validation Logic).** Cross‑Context use requires a declared **Bridge** (F.9) and carries CL/Loss penalties.


### F.10:7 - Solution — how meanings connect (conceptual, notation‑free)

**S‑1. Anchor status meanings per Context.**
Every status word (*validated*, *approved*, *compliant*) is treated as a **StatusCell** inside a specific Context. The **ladder position** is determined **locally** (e.g., “validated (metrology)” aligns to **Replicated** with CL stated; “validated (software)” may align to **Corroborated**).

**S‑2. Attach statuses to the right Targets.**
*EvidenceStatus → Claim or Quantity; StandardStatus → Method/Artefact; RequirementStatus → Clause.*
This prevents swapping “how we measure” with “what we promise”.

**S‑3. Translate via Bridges, not by name.**
Example: **Measured availability (SOSA)** →ᴍᴇᵃ **SLO clause (ITIL)** with **CL=2**, Loss: sampling window & clock skew. This supports **explanation**; **substitution** (“Satisfied”) requires **same StatusModality**, a stricter Bridge kind (F.9) **and** a declared evaluation rule (from the Service pattern), not from F.10.

**S‑4. Keep design/run honest.**
**StandardStatus** is design‑stance; **EvidenceStatus** is run‑signal; **RequirementStatus** spans both. Use **Interpretation Bridges** (F.9) for design↔run readings, not equivalence.

**S‑5. Prefer explanation over substitution.**
If a Bridge cannot reach **CL≥2** on the **same senseFamily**, do **not** substitute. Use **Naming‑only** rows or **explanations**; keep Role Descriptions (F.4) out of harm’s way.


### F.10:8 - Invariants (normative, lightweight)

1. **Modality purity.** A StatusCell’s **StatusModality** is explicit and **must not change** during reasoning; cross‑modality claims require an **Interpretation Bridge** (F.9).
2. **Target typing.** A status **must name its Target kind** (claim / artefact / clause). Inferences that ignore the Target kind are invalid.
3. **Window discipline.** Every positive/negative status **names a Window**; contradictions are detected **within the same Window** only.
4. **Local monotonicity.** Within one context, **stronger** EvidenceStatus implies all **weaker** positives for the same Target & Window.
5. **Mutual exclusivity (requirement).** For a given clause & Window: **not** (Satisfied ∧ Violated).
6. **No free promotion.** **StandardStatus** (Approved) **does not** entail **RequirementStatus** (Applicable or Satisfied).
7. **Bridge gate.** Any Cross‑context comparison or reuse of a status **must cite a Bridge** (kind, CL, Loss); otherwise only **context‑local** reading is permitted.
8. **Weakest‑link propagation.** When multiple Bridges contribute to a Cross‑context interpretation, the **effective CL** is the **minimum** (cf. F.7/F.9).
9. **Naming restraint.** Status labels used across Contexts **without** a Bridge are **Naming-only** and **non-operative** for Role Assignment & Enactment decisions.

### F.10:9 - Micro‑illustrations (snapshots, not procedures)

* **Metrology → Service.**
  *Observed uptime (SOSA)* with Window “July” plus Bridge **→ᴍᴇᵃ** to *SLO clause (ITIL)* yields: **we can explain** why “Satisfied” might hold **if** the Service pattern’s evaluation rule says so. F.10 itself **does not** declare “Satisfied”.

* **QA vs GxP “validation”.**
  *Validated (software QA Context)* aligns to **Corroborated** (CL=1–2).
  *Validated (GxP Context)* aligns to **Replicated** (CL=2–3) with Loss: environment diversity.
  Equating them needs **≈** with **CL stated** or they remain separate.

* **“Approved model” ≠ “Compliant outcome”.**
  **StandardStatus: Approved** for a **MethodDescription** does **not** imply **RequirementStatus: Satisfied** for a production clause. It only permits use; evidence must still speak.

### F.10:10 - Anti‑patterns & remedies

| #         | Anti‑pattern                                 | Symptom                                                                        | Why it harms reasoning                                                               | Remedy (conceptual move)                                                                                                                                                                                                                       |
| --------- | -------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **“Validated ⇒ Approved ⇒ Compliant” chain** | A single word *validated* is treated as proving approval and compliance.       | Collapses **statusModalities** (epistemic → deontic); ignores Targets & Windows.               | Keep **EvidenceStatus** about **claims**, **StandardStatus** about **artefacts/methods**, **RequirementStatus** about **clauses**. Use **two Bridges** (evidence→requirement via interpretation + standard→requirement via policy), never one. |
| **AP‑2**  | **Run‑time proves design‑time**              | A month of logs is cited as “therefore the method is approved.”                | Directional fallacy; design‑time approval is curatorial, not measured.               | Separate **design vs run**. Evidence may justify a **proposal** Bridge to *Approved* only in Contexts where such promotion exists; otherwise keep **explanation‑only**.                                                                           |
| **AP‑3**  | **“Approved model” ⇒ “SLO satisfied”**       | Governance stamp is cast as automatic service compliance.                      | **StandardStatus** does not entail **RequirementStatus**; the latter needs evidence. | Require **EvidenceStatus** on the clause’s **Window**, then apply the **evaluation rule** (Service pattern).                                                                                                                                   |
| **AP‑4**  | **Synonym drift of status labels**           | *Verified/validated/approved* used interchangeably across Contexts.               | Homonymy across Contexts; weakens claims.                                               | Treat each status word as a **StatusCell** tied to its Context; relate only via **Bridge(kind, CL, Loss)**.                                                                                                                                       |
| **AP‑5**  | **No Window**                                | Status claimed without time/condition (“Compliant.”).                          | Unfalsifiable; blocks conflict detection.                                            | Every positive/negative status **names a Window**; contradictions checked per Window.                                                                                                                                                          |
| **AP‑6**  | **Double truth**                             | *Satisfied* and *Violated* asserted for same clause silently.                  | Violates mutual exclusivity; hides differing Windows.                                | Force **Window discipline**; if Windows coincide, at least one assertion must retract.                                                                                                                                                         |
| **AP‑7**  | **Substitute by name**                       | “SOSA Observation = ITIL SLO check”.                                           | Cross‑context equality without Loss accounting.                                         | Prefer **explanation Bridges**; allow **substitution** only when **same statusModality**, **kind ∈ {≈,⊑,⊒}**, **CL≥project threshold**, **Windows aligned**.                                                                                            |
| **AP‑8**  | **Evidence escalation without diversity**    | One lab repeats itself and calls it “replicated”.                              | Confuses **repetition** with **independent replication**.                            | In EvidenceStatus, **Replicated** demands **independent** settings/sources; else keep at **Corroborated**.                                                                                                                                     |
| **AP‑9**  | **Clause‑less compliance**                   | “Compliant” with no clause named.                                              | Target missing; cannot evaluate.                                                     | Every RequirementStatus **points to a clause** (Target).                                                                                                                                                                                       |
| **AP‑10** | **Negative erased by summary**               | A later summary lists *Satisfied* but omits earlier *Violated* in same Window. | Cherry‑picks; breaks auditability.                                                   | Apply **Weakest‑link**: within a Window, **negative outranks** prior positives for the same clause.                                                                                                                                            |
| **AP‑11** | **Bridge‑free roll‑up**                      | Cross‑context dashboards aggregate statuses as if native.                         | Hidden Cross‑context semantics; CL unknown.                                             | Each Cross‑context line **must cite Bridges**; roll‑up shows the **effective CL (min)**.                                                                                                                                                          |
| **AP‑12** | **Status explosion**                         | New bespoke statuses minted to match every tool state.                         | Pollutes lexicon; blurs statusModalities.                                                      | Map tool states to the **nearest ladder level** in the local context; keep tool terms as **Naming‑only** where needed.                                                                                                                            |

### F.10:11 - Worked examples

> Each example names **Contexts**, shows **StatusCells** on their native ladders, and draws **only the Bridges that F.10 allows**.

#### F.10:11.1 - Service acceptance from run‑time evidence

**Contexts.** *SOSA/SSN (2017)* — sensing; *ITIL 4 (2020)* — services; *ODRL 2.2* — deontics (optional).

**Local statuses.**

* `SOSA:Observation(uptime)` → **EvidenceStatus: Measured**, Window **July**.
* `ITIL:SLO("99.9% monthly")` → **RequirementStatus** Target = clause *SLO‑99.9*, Window **July**.
* `ITIL:Practice("Monitoring pipeline")` → **StandardStatus: Approved** (design‑time).

**Bridges.**

* **Interpretation**: `Measured(uptime@July)` **→ᴍᴇᵃ** `SLO‑99.9` (kind = ⊑, CL = 2, Loss: sampling bias, clock skew).
* **Evaluation rule** (Service pattern, local to ITIL Context): returns **Satisfied** iff *mean uptime ≥ threshold* across Window.

**Result.** We may **explain** the **Satisfied** conclusion for *SLO‑99.9\@July*; we **do not** assert StandardStatus⇒RequirementStatus. If logs later show outages, a **Violated\@July** replaces **Satisfied\@July** (mutual exclusivity + Window discipline).


#### F.10:11.2 - Safety controller: design approval vs run‑time duty

**Contexts.** *State‑space control texts* — design; *IEC 61131‑3* — run; *Norm‑CAL profile (safety layer)* — deontics.

**Local statuses.**

* `ControllerSpec(v3)` — **StandardStatus: Approved** in the **Norm‑CAL** Context.
* `PLC:Task(log@Q3)` — **EvidenceStatus: Corroborated** for *response time ≤ 50 ms*, Window **Q3**.
* `Duty("Emergency stop ≤ 100 ms")` — **RequirementStatus** clause in Norm‑CAL.

**Bridges.**

* **Interpretation**: `Corroborated(response@Q3)` **→** `Duty` check (kind = ⊑, CL = 2, Loss: sensor latency).

**Result.** The **duty** may be **Satisfied\@Q3** with explanation. *Approved spec* **alone** never yields *Satisfied*; it authorises deployment but does not prove compliance.


#### F.10:11.3 - ML model: validation vs fairness requirement

**Contexts.** *ML validation canon* — design/run hybrid; *Policy Context (fairness charter)* — deontics; *SOSA/metrics* — sensing.

**Local statuses.**

* `Model v12: cross‑val AUC=0.92` → **EvidenceStatus: Corroborated** (Windows: CV folds).
* `Policy: “Demographic parity Δ ≤ 0.1”` → **RequirementStatus** clause.
* `“Validation SOP v5”` → **StandardStatus: Approved** (governance method).

**Bridges.**

* `Measured(Δ@Aug)` **→ᴍᴇᵃ** `Policy clause` (⊑, CL = 2, Loss: sampling variance).

**Result.** **Satisfied\@Aug** (if Δ≤ 0.1 in production Window) is justifiable. Cross‑val AUC does **not** decide fairness; only **production Δ** does.


#### F.10:11.4 - Medical device log: refutation

**Contexts.** *SOSA/clinical observations*; *Regulatory profile*.

**Local statuses.**

* `Observation: adverse event` → **EvidenceStatus: Observed\@Week 34**.
* `Requirement: “No AE in first 30 days”` → **RequirementStatus** clause.

**Bridge & outcome.**

* Observation **→ Interpretation Bridge** to clause check (**kind: Interpretation**, **CL=3**).
* **Violated\@Week 34** overrides any earlier **Satisfied\@Week 34** (Weakest‑link; same Window).


### F.10:12 - Reasoning primitives (judgement schemas, notation‑free)

> **Premises ⊢ conclusion.** No side effects. All moves are **mental** and **Context‑aware**.

1. **StatusModality classification**
   `σ is a StatusCell ⊢ statusModality(σ) ∈ {epistemic, deontic}`
   *Reading:* Every status sits on exactly one statusModality.

2. **Target typing**
   `σ ⊢ targetKind(σ) ∈ {claim, artefact/method, clause}`
   *Reading:* Evidence→claim; Standard→artefact/method; Requirement→clause.

3. **Window requirement**
   `σ has polarity ∈ {positive, negative} ⊢ window(σ) ≠ ∅`
   *Reading:* Pos/neg statuses must name a Window.

4. **Local ladder monotonicity (evidence)**
   `Replicated(τ,W) ⊢ Corroborated(τ,W) ⊢ Measured(τ,W) ⊢ Observed(τ,W)`
   *Reading:* Stronger implies weaker within the same Window.

5. **Requirement exclusivity**
   `clause κ, window W ⊢ ¬(Satisfied(κ,W) ∧ Violated(κ,W))`
   *Reading:* A clause cannot be both satisfied and violated in one Window.

6. **Windowed refutation**
   `Refuted(τ,W) ⊢ cancels {Observed,Measured,Corroborated,Replicated}(τ,W)`
   *Reading:* Negative evidence cancels positives only in the same Window.

7. **Explanation Bridge**
   `σ@C, τ@D, Bridge(C,D, kind∈{≈,⊑,⊒,⋂}, CL, Loss), sameStatusModality ⊢ explains(σ ⇒ τ) with ⟨CL,Loss⟩`
   *Reading:* Cross‑context explanation is permitted when statusModalities match.

8. **Substitution permission (guarded)**
   `explains(σ ⇒ τ) ∧ kind∈{≈,⊑,⊒} ∧ CL≥θ ∧ windowsAligned ⊢ maySubstitute(σ→τ)`
   *Reading:* Substitution is allowed only above a **project‑declared threshold θ** (see F.7) and aligned Windows.

9. **Cross‑statusModality embargo**
   `statusModality(σ) ≠ statusModality(τ) ⊢ explains(σ ⇒ τ) requires Interpretation kind`
   *Reading:* Crossing statusModalities is **interpretation** only; no direct substitution.

10. **Observation→Requirement clause (SOSA, Work outcomes)**
   `SOSA:Observation about Work outcomes ⊢ may interpret(RequirementClause κ) via Bridge(kind=Interpretation, CL, Loss); produces Evaluation(κ, Window); substitution forbidden`
   *Reading:* Observations inform clause evaluation within a Window; they never become RequirementStatus. Use F.12 for the verdict pipeline.

11. **Weakest‑link CL**
   `{explains(σᵢ ⇒ τ) with CLᵢ} ⊢ effectiveCL(⋀ᵢ σᵢ ⇒ τ) = minᵢ(CLᵢ)`
   *Reading:* Multiple Bridges compose by the minimum CL.

12. **Naming‑only safeguard**
   `noBridge(C,D) ⊢ crossContextUse(σ@C ⇒ τ@D) = namingOnly`
   *Reading:* Without a Bridge, only **explanatory prose** is allowed—no status inferences.

13. **DesignRunTag honesty**
   `statusModality=deontic ∧ targetKind=artefact/method ∧ window=W ⊢ doesNotDecide(clause κ @ W)`
   *Reading:* Approval of a method never decides a clause’s satisfaction for a run‑time Window.

### F.10:13 - Relations

**Builds on:**
E.10.D1 **D.CTX** (Context discipline); F.1 (Contexts in view); F.2–F.3 (Seeds→Local‑Senses→SenseCells); F.4 (Role Description **Status** template with statusModality/target/window slots); F.7 (Bridge taxonomy & CL semantics); F.9 (Bridge artefact).

**Constrains:**

* **F.4 (Role Description Status):** a Role Description Status **must** select a **StatusFamily**, **StatusModality**, **target kind**, and **Window**.
* **F.8 (Naming):** status labels reused across Contexts **must** be marked as **Context‑scoped**; global synonyms forbidden.
* **Part C patterns:** KD‑CAL provides measurement semantics for EvidenceStatus; Norm‑CAL provides clause logic for RequirementStatus; Method‑CAL frames DesignRunTag for StandardStatus.

**Used by.**
Service Acceptance (F.12), Assurance roll‑ups (B.3), any cross‑domain conformance narrative.


### F.10:14 - Migration notes (conceptual)

1. **New status word appears.** Treat it as a **StatusCell** in its Context; place it on the local ladder; only then consider Bridges.
2. **Edition changes.** If a Context redefines a status, **fork the StatusCell** (new SenseCell) and relate old↔new via a **Bridge** (often ⊑/⊒ with Loss).
3. **Threshold tuning.** The project sets **θ** (minimum CL for substitution). Lowering θ widens reuse but increases risk; document the choice in F.7 terms.
4. **Clause redesign.** If a requirement clause changes, keep old **Windows** intact; new clause starts a new Target; do **not** rewrite history.
5. **Explode→compress.** When many bespoke tool statuses pile up, **map** them to the nearest ladder level in their Contexts; keep tool labels as **Naming‑only**.
6. **Bridge hardening.** If explanation Bridges are used frequently, reconsider experiments that could raise **CL** enough to permit substitution—or accept explanation as sufficient and stop short of substitution.


### F.10:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.10:15.1 - Static conformance (SCR)

* **SCR‑F10‑S01 (Modality & Target).** Every StatusCell declares **StatusModality** and **target kind**; none cross modalities.
* **SCR‑F10‑S02 (Windowed polarity).** Every positive/negative StatusCell instance bears a **Window**.
* **SCR‑F10‑S03 (Local order).** EvidenceStatus instances satisfy **monotonicity**; RequirementStatus enforces **mutual exclusivity** per clause+Window.
* **SCR‑F10‑S04 (Bridge citation).** Any Cross‑context comparison cites a **Bridge(kind, CL, Loss)**; absent that, mark as **naming‑only**.
* **SCR‑F10‑S05 (Substitution guard).** Any substitution claim checks **same StatusModality**, **kind ∈ {≈,⊑,⊒}**, **CL≥θ**, **Windows aligned**.
* **SCR‑F10‑S06 (Weakest‑link).** Where multiple Bridges feed one conclusion, the displayed **effective CL** is the **minimum**.

#### F.10:15.2 - Regression (RSCR)

* **RSCR‑F10‑E01 (Edition churn).** Adding a new edition of a Context **does not** retro‑change past status conclusions; only new Windows see new meanings.
* **RSCR‑F10‑E02 (Threshold change).** If θ changes, re‑evaluate only **substitution** conclusions; **explanations** remain valid.
* **RSCR‑F10‑E03 (Bridge drift).** When a Bridge’s CL/Loss changes, recompute affected **effective CL**; substitution conclusions below θ revert to **explanation**.
* **RSCR‑F10‑E04 (Contradiction catch).** Adding a negative status within a Window **cancels** prior positives for the same clause (or raises a flagged contradiction if both persist).


### F.10:16 - Didactic distillation (90‑second script)

> **Three families, two modalities.** *Evidence* tells us what the world **shows** (Observed→Measured→Corroborated→Replicated; Refuted cancels) — **epistemic**; *Standard* tells us what a canon **sanctions** (Candidate→Draft→Approved→Deprecated→Superseded) — **deontic**; *Requirement* tells us what an obligation is **doing** (Applicable/Inapplicable; Satisfied/Violated; Waived/Pending) — **deontic**.
> Every status is a **StatusCell inside one Context** with exactly one **StatusModality**, a **Target**, and a **Window**.
> When you must relate status meanings across Contexts, **draw a Bridge** that states the **kind** (≈, ⊑/⊒, ⋂, ⊥ or Interpretation), the **CL** (strength), and the **Loss** (what you ignore). Prefer **explanation**; allow **substitution** only when statusModalities match, kind permits, **CL≥θ**, and Windows align.
> Keep **design vs run** stance honest: approval is **design‑time**, evidence is **run‑time**, requirements **span both**. With this habit, “validated”, “approved” and “compliant” stop being a muddle of synonyms and become **precise, local meanings** you can compare **safely** and **audibly**.

### F.10:End

## F.11 - Method Quartet Harmonisation

**“Keep the *how* (Method), the *recipe* (MethodDescription), the *happening* (Work/Execution), and the *control push* (Actuation) in their own Contexts—then relate them explicitly.”**

**Status.** Architectural pattern.
**Builds on:** E.10.D1 **D.CTX** (Context discipline); A.3/**A.3.1**/**A.3.2** (Transformer Constitution; `U.Method`, `U.MethodDescription`); A.15/**A.15.1** (`U.Work` as record of occurrence); Sys‑CAL (control/actuation semantics); KD‑CAL (observation).
**Coordinates with.** F.1–F.3 (Contexts, Seeds → SenseCells), F.4 (Role Description), F.5 (Naming), F.6 (Role Assignment & Enactment Cycle (Six-Step)), F.7/F.9 (Bridges), F.10 (Status families & Windows).
**Aliases (informative).** *Method/Spec/Work/Actuation split*; *design/run harmonisation*.


### F.11:1 - Intent & applicability

**Intent.** Provide a **notation‑free, Context‑aware map** that keeps four notions distinct and connectable:

* **`U.Method`** — the abstract **way of doing** (design‑time concept).
* **`U.MethodDescription`** — the **recipe** that describes a Method (epistemic artefact).
* **`U.Work`** (informal: *Execution*) — the **run‑time occurrence** of doing (recorded event).
* **`U.Actuation`** — the **control output** applied to a plant (domain‑specific Work in Sys‑CAL).

The pattern makes the split **usable across FPF patterns** (Role Assignment & Enactment, Sys-CAL, KD-CAL, Kind-CAL, planned LCA-CAL) and **legible across Contexts** (SPEM/BPMN for design; PROV-O/SOSA for run; IEC 61131-3/state-space for control).

**Applicability.** Any time a discussion risks **mixing designs with executions**, **recipes with runs**, or **workflow with control signals**; whenever you need to **name** or **reason** about “how we do X”, “the SOP/script/model”, “the actual run”, or “the actuator push”.

**Non‑goals.** No team workflow, no editors, no tools. No prescriptive file formats. **Only** conceptual distinctions and safe reasoning moves.


### F.11:2 - Problem frame

When Method, MethodDescription, Work, and Actuation **collapse into one another**, models drift:

1. **Design/run blur.** A BPMN *process* (design graph) is cited as if it had *happened*.
2. **Recipe/approval fallacy.** An *approved* SOP (MethodDescription) is treated as proof that the service met its SLO.
3. **Execution ≟ control.** PLC *task execution* logs are conflated with *control outputs* (actuation), hiding stability issues.
4. **Cross‑context homonymy.** *Activity, task, execution, process, command* change sense across Contexts; inferences quietly break.


### F.11:3 - Forces

| Force                        | Tension to resolve                                                                                             |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Fidelity vs didactics**    | We must honour domain nuance yet teach a split that fits in working memory.                                    |
| **Universality vs locality** | Quartet must be reusable across FPF patterns, while meanings stay **context‑local**.                             |
| **Evidence vs approval**     | Evidence (run‑time) should support decisions, but must **not** be mistaken for deontic approval (design‑time). |
| **Action vs signal**         | Executing a method is not the same as emitting a control signal; both can co‑occur in one scenario.            |


### F.11:4 - Core idea (didactic)

**Four boxes, four arrows, zero leakage.**

* **Box 1 — Method (design).** The **idea** of how to achieve an effect (algorithm, clinical pathway, welding technique).
* **Box 2 — MethodDescription (design, epistemic).** The **written/encoded recipe** that *describes* a Method (SOP, code, BPMN/SPEM model, theorem‑prover script).
* **Box 3 — Work (run).** The **occurrence** where a System‑in‑Role enacts (some version of) the Method. *`U.Work` is the record of this event.*
* **Box 4 — Actuation (run, Sys‑CAL).** The **control output** (setpoint/command) issued to influence a plant during Work.

**Arrows (conceptual relations).**

* `MethodDescription ↦ Method` (**describes**) — design stance.
* `Work ↦ MethodDescription` (**followedRecipe?** yes/no/variant) — run stance referencing design.
* `Work ↦ Method` (**enacts**) — run stance referencing the abstract way.
* `Actuation ↦ Work` (**part‑of / occurs‑during**) — control output inside execution.

Each box/arrow is **context‑local** (SPEM, PROV‑O, IEC…). **Cross‑context relations use Bridges** (F.7/F.9) with CL/Loss.


### F.11:5 - Minimal vocabulary (this pattern only)

* **Context** = `U.BoundedContext` (per D.CTX).
* **Local‑Sense** → **SenseCell** (F.3): the address *(Context × sense)* for a term like *process*, *task*, *activity*, *command*.
* **Concept‑Set** (F.7/F.8): row aligning multiple SenseCells as “what we regard as the same” (after Bridges & losses are declared).
* **Window** (F.10): temporal/conditional envelope (e.g., *July*, *during test run T42*, *under load ≥ 70%*).
* **StatusCell** (F.10): laddered status **about** methods/specs/works (e.g., *Approved (spec)*; *Observed/Measured (work)*).


### F.11:6 - Solution — the quartet lens (notation‑free)

> *Not steps for a team—**lenses for a thinker**. Use them to sanity‑check any statement about “how”, “script”, “run”, or “signal”.*

#### F.11:6.1 - The **stance split** (design vs run)

* If the claim is about **what should be done** or **how it is described**, you are on the **design stance** (Method/MethodDescription).
* If the claim is about **what happened** or **what was emitted**, you are on the **run stance** (Work/Actuation).
* **Guard rule.** Never let a conclusion cross stances without (a) an explicit Bridge kind (*interpretation* vs *substitution*), and (b) an acceptable CL (F.7/F.9, F.10).

#### F.11:6.2 - The **recipe/idea split**

* **Method** is the **idea**; **MethodDescription** is the **recipe** describing that idea.
* Different recipes may describe the **same** method (profiles, languages, levels of detail); one recipe may encode **several** methods (composite SOP).
* **Naming guard.** Keep labels distinct: *compressive‑strength test* (Method) vs *ASTM C39‑18* (MethodDescription).

#### F.11:6.3 - The **happening** (Work) with **signal** (Actuation)

* **Work** is the **occurrence** (a PROV *Activity*, an IEC *Task* executing a program, a lab run).
* **Actuation** is the **control output** (setpoint, PWM command, valve open %) emitted **during** Work.
* You can have Work **without** Actuation (analysis job), or Actuation **without** a complex Method (manual push). Many scenarios have **both**.

#### F.11:6.4 - The **Role Assignment & Enactment touch-points**

* **Roles** (F.4) bind **who enacts** the Method at run‑time (behavioural masks), **not** what permissions they hold (RBAC is a different Context).
* **Statuses** (F.10) bind to the right box: *Approved* → MethodDescription; *Measured/Observed* → Work; *Satisfied/Violated* → Requirement clause about the Work’s outcomes within a **Window**.


### F.11:7 - Harmonisation map (Context‑first)

> Examples of **local SenseCells** and **safe Bridges**. *You may keep the exact Contexts from your F.1 cut.*

**Design (ideas & recipes).**

* *SPEM/ISO 24744 Context*: `SenseCell{Method}` = *Activity Definition / Task Definition*; `SenseCell{MethodDescription}` = *Process Description / WorkProduct* (as recipe).
* *BPMN 2.0 Context*: `SenseCell{MethodDescription}` = *Process (diagram)* as **design‑time** recipe (do not confuse with run).
* *OWL/Kind-CAL Context*: labels for Method kinds (type taxonomies) when needed (naming, not behaviour).

**Run (occurrences & outputs).**

* *PROV‑O Context*: `SenseCell{Work}` = *Activity* (time‑bounded occurrence).
* *SOSA/SSN Context*: Observations **about** Work results (feeds EvidenceStatus).
* *IEC 61131‑3 Context*: `SenseCell{Work}` = *Task executes Program* (runtime); `SenseCell{Actuation}` = *Output command / setpoint* emitted by the program.

**Typical Bridges (with intent).**

* `BPMN:Process (design)` **≈** `SPEM:Process Definition` (design↔design; CL depends on modelling profile; Loss: expressiveness gaps).
* `IEC:Task execution` **⊑** `PROV:Activity` (run↔run; Loss: control‑specific timing semantics, scan cycles).
* `Actuation (IEC)` **⋂** `Activity (PROV)` (intersection: the *sub‑intervals* where outputs are emitted).
* `SOSA:Observation` **interprets** `Requirement clause` (F.10) about **Work outcomes** (**cross‑StatusModality: epistemic→deontic; never substitution**; declare **Bridge(kind=Interpretation, CL, Loss)**).


### F.11:8 - Invariants (normative)

1. **DesignRunTag honesty.** Statements about **Method/MethodDescription** (design) **MUST NOT** be used as if they were statements about **Work/Actuation** (run) without an explicit Bridge and Window.
2. **Box discipline.** Every claim about “how”, “recipe”, “run”, or “control output” **MUST** point to the correct box in the quartet.
3. **Context locality.** Terms (*process*, *activity*, *task*, *command*) **MUST** be read as **SenseCells** in their Contexts (F.3); Cross‑context equivalence is a matter for F.7/F.9 Bridges.
4. **Status placement.** *Approved* attaches to MethodDescription; *Observed/Measured* attach to Work; *Satisfied/Violated* attach to clauses about Work outcomes within a **Window** (F.10).
5. **Actuation as Work‑part.** Actuation **MUST** be modelled as **occurring within** (or as a specialised form of) Work on the run stance; it does **not** replace Work.
6. **Naming clarity.** Technical/Plain labels for the quartet **SHOULD** be distinct (F.5); avoid homonymous single‑word labels when Contexts collide.
7. **Bridge guard.** Cross‑context moves **MUST** declare **kind** (≈, ⊑, ⊒, ⋂, ⊥, Interpretation), **CL**, and **Loss** (F.7/F.9).


### F.11:9 - Micro‑examples (didactic)

1. **Data pipeline deploy (software).**
   *Method*: “Delta‑load transform”. *MethodDescription*: `etl_delta.py@v3`. *Work*: nightly run 2025‑07‑14. *Actuation*: none.
   *Statuses*: Spec **Approved** (governance Context); Work **Measured** (rows processed) → Evidence for SLO (F.10).

2. **Valve control (industrial).**
   *Method*: PID tuning heuristic. *MethodDescription*: SOP sheet + IEC program. *Work*: PLC task cycle 18:00–18:30. *Actuation*: PWM duty sequence.
   *Bridge*: `IEC:Task` ⊑ `PROV:Activity` (CL=2). Observed setpoint tracking **interprets** requirement “settling time ≤ 5 s”.

3. **Clinical assay (lab).**
   *Method*: ELISA. *MethodDescription*: Kit IFU v7. *Work*: run batch #B217. *Actuation*: pipetting robot commands.
   *Statuses*: Spec **Approved** ≠ batch **Satisfied** (requires evidence at batch Window).

### F.11:10 - Anti‑patterns & remedies

| #       | Anti‑pattern                   | Symptom in prose/models                                               | Why it harms thinking                                                       | Remedy (conceptual move)                                                                                                                                                                                             |
| ------- | ------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Design→Run Substitution**    | “The process **achieved** X” while pointing to a design diagram.      | Treats a **MethodDescription** as if it were **Work**; collapses stances.           | Apply the **stance split**: restate as “The **diagram describes** how X **should** be achieved.” To claim it **happened**, reference a **Work** SenseCell in a run‑time Context and, if needed, add a **Window** (F.10). |
| **A2**  | **Approval = Evidence**        | “Approved SOP ⇒ requirement satisfied.”                               | A **StatusCell** about a **MethodDescription** does not entail a run‑time outcome. | Keep **Approved** on Spec; place **Satisfied/Violated** on clauses **about Work** within a **Window**; require Observation/Evidence (KD‑CAL) for the run side.                                                       |
| **A3**  | **Execution = Actuation**      | PLC log of setpoints recorded as the whole execution history.         | Loses non‑signal aspects (delays, conditions, context); weakens reasoning.  | Model **Actuation** as **within** **Work**. Keep both SenseCells: *Task execution* (Work) and *Command/Setpoint* (Actuation).                                                                                        |
| **A4**  | **BPMN‑as‑Run**                | BPMN *Process* treated as “the thing that ran.”                       | BPMN’s meaning is context‑local and design‑time.                               | Use a **Bridge** (F.7/F.9) from *BPMN\:Process (design)* → *PROV\:Activity (run)* with kind **Interpretation**, CL/Loss declared.                                                                                    |
| **A5**  | **Spec Drift Retroactivity**   | Update to a recipe is assumed to modify past executions.              | Violates temporal honesty; breaks auditability.                             | Past **Work** remains as‑was. New **MethodDescription** versions describe future **Work** only; record variant relations if a run deviated.                                                                                 |
| **A6**  | **Homonym Collapse**           | *Task*, *activity*, *process* used interchangeably across Contexts.      | Imports meaning implicitly; masks losses.                                   | Prefix with **Context** and use **SenseCells**: e.g., *task (IEC)*, *activity (PROV)*, *process (BPMN)*. Any relation uses **Bridges** with CL/Loss.                                                                    |
| **A7**  | **Signal‑Only Compliance**     | SLO judged solely from actuator traces.                               | Ignores measured outcomes; risks false positives.                           | Tie **SLO** clauses to **Observations** (KD‑CAL) **about Work outcomes**; treat Actuation as an input, not proof.                                                                                                    |
| **A8**  | **Recipe-as-Role**             | “The Spec assigns responsibility” (mixes MethodDescription with Role constructs — `U.RoleDescription`/`U.RoleAssignment`).  | Conflates epistemic artefact with behavioural masks.                        | Use **F.4 Role Description; let **MethodDescription** only **describe** a Method.                                                                              |
| **A9**  | **One‑Context Scope**        | A single Context (e.g., BPMN) used as if it covered control/measurement. | Scope mirage; silent cross‑domain generalisation.                           | Re‑cut Contexts (F.1) to include control and sensing. Re‑express statements with the quartet across those Contexts.                                                                                                        |
| **A10** | **Lossless Bridge Assumption** | Claiming “equivalent” across Contexts without Loss.                      | Hides mismatches; unsafe transfer of inferences.                            | In **F.7/F.9** declare Bridge **kind**, **CL**, and explicit **Loss** notes.                                                                                                                                         |
| **A11** | **Recipe‑as‑Type**             | Treating a MethodDescription vocabulary as a type taxonomy.                  | Category error; misuses Kind-CAL.                                           | If a stable hierarchy of **kinds** of Methods is needed, mint **U.Type** nodes in Kind-CAL; keep MethodDescription as *description* only.                                                                                   |
| **A12** | **Actuation Outside Work**     | Commands modeled without enclosing Work.                              | Severs signal from enactment context; breaks traceability.                  | Embed **Actuation** **within** **Work** intervals; relate to the enacting Role and Method/MethodDescription references.                                                                                                     |


### F.11:11 - Worked examples (extended)

> Each scenario names Contexts (from your F.1 cut), identifies the quartet boxes, and shows safe Cross‑context moves.

#### F.11:11.1 - ML service rollout (software + services + sensing)

* **Contexts:** *SPEM/ISO 24744* (design), *PROV‑O* (run), *SOSA/SSN* (sensing), *ITIL 4* (services).
* **Quartet:**

  * **Method:** *Canary deployment strategy*.
  * **MethodDescription:** *Canary plan document with traffic slices and rollback rules* (design Context).
  * **Work:** *Two canary runs 2025‑08‑02 10:00–12:00* (PROV‑Activities).
  * **Actuation:** *Traffic‑shifting commands* (if modeled, they are outputs inside Work; optional in pure software).
* **Statuses (F.10):** *Spec Approved*; *Work Observed* (latency/err‑rate via SOSA Observations); *SLO clause Satisfied* in Window if measured ≤ thresholds.
* **Bridge(s):** *BPMN (if used) Process (design)* → *PROV Activity (run)* **Interpretation**, CL=2, **Loss:** path vs time granularity.

**Pay‑off:** No one infers SLO satisfaction from a plan. Evidence is about **Work**; the plan stays design‑time.


#### F.11:11.2 - Industrial furnace control (control + sensing + services)

* **Contexts:** *State‑space control texts* (design), *IEC 61131‑3* (run), *PROV‑O* (run), *SOSA/SSN* (sensing), *ITIL 4* (services).
* **Quartet:**

  * **Method:** *PID with feed‑forward*.
  * **MethodDescription:** *Controller tuning sheet + program description*.
  * **Work:** *PLC task cycles 14:00–14:30* (IEC *Task executes Program*), **Bridged** as **PROV Activity**.
  * **Actuation:** *Setpoint & valve duty cycle outputs* emitted during Work.
* **Statuses:** *Spec Approved*; *Work Observed* (temperature curve); requirement *settling time ≤ 5 s* **Satisfied** if the observation within Window meets it.
* **Bridge(s):** `IEC:Task` ⊑ `PROV:Activity` (CL=2, **Loss:** scan‑cycle semantics). `SOSA:Observation` **interprets** requirement clause (CL=3).

**Pay‑off:** Separates **doing** from **pushing**, and both from **measuring**; compliance judged where it belongs.


#### F.11:11.3 - Clinical assay

* **Contexts:** *SPEM/ISO 24744* (design), *Lab assay canon* (design/run split as per discipline), *PROV‑O* (run), *SOSA/SSN* (sensing).
* **Quartet:**

  * **Method:** *ELISA*.
  * **MethodDescription:** *Kit IFU v7 (instructions for use)*.
  * **Work:** *Batch B217 performed 2025‑06‑21* (PROV Activity).
  * **Actuation:** *Pipetting robot commands* (optional detail).
* **Statuses:** *Spec Approved*; *Work Observed* (absorbance readings); *Quality gate Satisfied* within batch Window.
* **Bridge(s):** IFU (design) **interprets** Activity (run) for acceptance (CL=2, **Loss:** deviations allowed per kit tolerances).

**Pay‑off:** A clean line from recipe → run → measurement → decision, without role/status conflation.


#### F.11:11.4 Incident response (services + enactment)

* **Contexts:** *ITIL 4* (services/design), *BPMN 2.0* (design), *PROV‑O* (run).
* **Quartet:**

  * **Method:** *Triage‑first incident handling*.
  * **MethodDescription:** *Incident workflow diagram + playbook*.
  * **Work:** *Handling INC‑3421, 09:10–10:02* (PROV Activity).
  * **Actuation:** none (unless modeling command invocations as outputs).
* **Statuses:** *Spec Approved*; *Work Observed* (timestamps, response time); *SLO “MTTR ≤ 60 min”* **Satisfied** within the incident Window.
* **Bridge(s):** BPMN (design) → PROV (run) **Interpretation**, CL=2, **Loss:** gateways vs real‑time branching.

**Pay‑off:** MTTR claims are tied to **Work**, not to the playbook.


### F.11:12 - Reasoning primitives (judgement schemas)

> Pure **mental moves**; no storage or workflow is implied.

1. **Box classifier**
   `statement s, Contexts fixed ⊢ box(s) ∈ {Method, MethodDescription, Work, Actuation}`
   *Reading:* Classify any claim by its **box** (design idea, design recipe, run occurrence, control output).

2. **Stance firewall**
   `box(s) ∈ {Method,MethodDescription} ⊢ s ∉ {claims about Work outcomes}`
   *Reading:* A design‑time (stance) statement does **not** assert a run‑time (stance) outcome.

3. **Followed‑recipe judgement**
   `Work w, MethodDescription m ⊢ follows(w,m) ∈ {exact, variant, none}`
   *Reading:* A Work may follow a recipe **exactly**, with a **variant**, or **not at all**; later inferences must respect this value.

4. **Enactment link**
   `Work w, Method h ⊢ enacts(w,h)`
   *Reading:* The occurrence enacts the abstract Method (even if several specs describe it).

5. **Actuation inclusion**
   `Actuation a, Work w ⊢ occursWithin(a,w)`
   *Reading:* Control outputs are **within** (or are parts of) a Work interval.

6. **Observation binding** (KD‑CAL handshake)
   `Observation o about outcome(x) during Window W of Work w ⊢ evidenceFor(w, clause(x,W))`
   *Reading:* Measurements about a Work outcome within a Window serve as evidence for clauses **about that Work**.

7. **Clause evaluation** (F.10 handshake)
   `evidenceFor(w,clause) ⊢ status(clause,w) ∈ {Satisfied, Violated, Inconclusive}`
   *Reading:* A clause about Work yields a status via the observation set.

8. **Context locality**
   `term t, Context C ⊢ meaning(t)@C is local`
   *Reading:* A term’s sense is **local** to its Context; Cross‑context claims require Bridges.

9. **Bridge application** (F.7/F.9)
   `Bridge B: (X@A) ~kind,CL,Loss~ (Y@B); fact about X ⊢ transferableTo(Y) with penalty(CL,Loss)`
   *Reading:* Facts may transfer across Contexts only along a declared Bridge, with the stated penalty.

10. **Version non‑retroactivity**
    `MethodDescription m updated → m' ⊢ ∀ past Work w: follows(w,m')=none (unless w references m')`
    *Reading:* New recipes don’t rewrite history.

11. **Composite reasoning**
    `MethodDescription m = m1 ; m2, Work w executes steps w1,w2 ⊢ enacts(w1,m1) ∧ enacts(w2,m2)`
    *Reading:* Composition on design does not force composition on run, but when it aligns you may relate sub‑runs to sub‑methods.

12. **SLO locus guard**
    `SLO clause about service outcome ⊢ attachesTo(Work-window), not MethodDescription`
    *Reading:* Service obligations concern **what happened** within a Window, not the existence of a plan.


### F.11:13 - Relations

**Builds on:**
E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); A.3/**A.3.1**/**A.3.2**/**A.15** (Method/Spec/Work foundations); Sys‑CAL (Actuation semantics); KD‑CAL (Observation); F.1–F.3 (Contexts → SenseCells); F.10 (Status families & Windows).

**Constrains:**

* **F.4 Role Description:** Roles/Statuses **must** point to the right box (e.g., *Approved* → MethodDescription; *Observed* → Work).
* **F.5 Naming:** Enforce distinct Tech/Plain labels for Method/Spec/Work/Actuation where homonyms threaten.
* **F.7/F.9 Bridges:** All Cross‑context assertions among quartet terms **must** go through explicit Bridges with **kind/CL/Loss**.

**Used by.**
Part C patterns (Sys‑CAL, KD‑CAL, Method‑CAL, Kind-CAL, LCA‑CAL) when describing examples, proofs, and cross‑disciplinary mappings.


### F.11:14 - Migration notes (conceptual)

1. **Split conflated “process”.** Where a single “process” node stands for both plan and run, refactor into **MethodDescription** (design) and **Work** (run); add a Bridge if the prose relied on identity.
2. **Re‑home statuses.** Move any *Approval*‑like statuses from Work to MethodDescription; move *Satisfied/Violated* from Spec to clauses about Work within **Windows**.
3. **Expose actuation.** If control outputs are buried in “execution logs,” mint **Actuation** SenseCells and relate them **within** Work.
4. **Version fences.** Past Works keep references to the **version** of MethodDescription they attempted to follow; don’t update those links retroactively.
5. **Name collisions.** Where *task/activity/process* appear with mixed meanings, prefix with Contexts and relabel per **F.5** (Tech/Plain).
6. **Backfill Bridges.** If earlier text implied Cross‑context equivalence, add explicit Bridges (F.7/F.9) declaring **kind/CL/Loss**.


### F.11:15 - Acceptance tests (SCR/RSCR — concept level)

#### F.11:15.1 - Static conformance checks (SCR)

* **SCR‑F11‑S01 (DesignRunTag honesty).** Every normative claim about outcomes is attached to **Work** (with Window), not to **Method/MethodDescription**.
* **SCR‑F11‑S02 (Box placement).** Labels and statuses appear on the correct box (e.g., *Approved* on MethodDescription only).
* **SCR‑F11‑S03 (Actuation inclusion).** All Actuation statements are modeled as **within** a Work interval.
* **SCR‑F11‑S04 (Context discipline).** Each quartet term is expressed as a **SenseCell** with its Context; no Cross‑context identity is asserted here.
* **SCR‑F11‑S05 (Bridge guard).** Any Cross‑context reasoning among quartet terms references an explicit **Bridge** with **kind/CL/Loss**.

#### F.11:15.2 - Regression checks (RSCR)

* **RSCR‑F11‑E01 (Spec update).** When a MethodDescription changes, previous Works remain valid and unchanged; their statuses don’t shift unless re‑evaluated with explicit rationale.
* **RSCR‑F11‑E02 (Bridge drift).** If a Context updates, revisit Bridges that touch quartet terms; adjust **CL/Loss** only via F.7/F.9.
* **RSCR‑F11‑E03 (Status drift).** Adding new statuses does not move them across boxes (e.g., no new “Work‑Approved”).
* **RSCR‑F11‑E04 (Signal creep).** Introducing new Actuation details does not erase or replace Work context.


### F.11:16 - Didactic distillation (90‑second script)

> “When you talk about *how something is done*, decide which of the **four boxes** you mean.
> **Method** is the **idea** (the way). **MethodDescription** is the **recipe** (the description). **Work** is the **happening** (what actually occurred). **Actuation** is the **control push** (signals emitted during Work).
> Keep **design** and **run** as distinct **stances**. Plans and approvals live in the **design stance**; measurements and obligations live in the **run stance** within **Windows**.
> Words like *process*, *task*, *activity*, *command* are **context‑local**—say *process (BPMN)*, *activity (PROV)*, *task (IEC)*. If you must relate them, draw a **Bridge** and declare its **kind**, **CL**, and **Loss**.
> For compliance, don’t point at the plan—point at **Work**, show **Observations**, and judge clauses in **F.10**.
> Hold this quartet in your head and you’ll stop mixing plans with facts, signals with outcomes, and names across Contexts. + Everything else—naming (F.5), `U.RoleDescription` (F.4) and `U.RoleAssignment`/`U.RoleEnactment` (A.2.1/F.6), Bridges (F.7/F.9)—falls into place.

### F.11:End

## F.12 — Service Acceptance–Work Evidence Link

**“Judge promises on what happened, not on what was planned.”**
**Status.** Architectural pattern.
**Builds on:** F.1 **context of meaning (U.BoundedContext)**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering**; F.5 **Naming Discipline**; F.7/F.9 **Bridges & CL**; F.10 **Status Families & Windows**; F.11 **Method Quartet Harmonisation**; A.2.3 **U.PromiseContent**.
**Coordinates with.** KD‑CAL (Observation/Characteristic/Scale); Sys‑CAL (Work/Actuation contexts).
**Non‑goals.** No team workflows, no tooling, no editorial procedures. This pattern specifies **how to think** about acceptance, not how to store or operate systems.


### F.12:1 - Intent & applicability

**Intent.** Provide a **conceptual binding** that turns a *service promise* (SLO/SLA clause) into a **clear, local, time‑bounded judgement** about **actual Work**, using **Observations** as evidence and **explicit Bridges** where Cross‑context notions must meet. The result is a **Status** (Satisfied/Violated/Inconclusive) that attaches to the **clause‑about‑that‑Work‑in‑that‑Window**.

**Applicability.** Any situation where a **service promise clause** (promise content) is published (availability, latency, safety margin, response time, quality gate, compliance duty) and its fulfilment must be decided from what occurred. Works across digital services, industrial control, laboratory processes, clinical pathways, logistics, etc.


### F.12:2 - Problem frame

1. **Plan ≠ proof.** Diagrams and playbooks are treated as if they demonstrated fulfilment.
2. **Signal ≠ outcome.** Control signals (Actuation) are mistaken for the consumer‑perceived outcome (the outcome promised by the clause).
3. **Global meanings.** *Availability*, *incident*, *latency* are used as if universal, ignoring context‑local senses.
4. **Unstated translation.** Metrics from one canon are mapped to clauses from another without declaring losses.
5. **Timeless verdicts.** Judgements are asserted with no explicit Window (day, month, batch).


### F.12:3 - Forces

| Force                                | Tension to resolve                                                                                        |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Promise vs. occurrence**           | A service **promise clause** (`U.PromiseContent`) is an external promise, yet acceptance must reference **Work** (run‑time). |
| **Locality vs. integration**         | Meanings are **context‑local**; still we must compare across **service situations**, plants, and monitors.                 |
| **Parsimony vs. realism**            | We want a small binding scheme, yet domains differ (percentiles, downtime minutes, control margins).      |
| **Evidence vs. privacy/feasibility** | Observations prove outcomes; sometimes only proxies exist.                                                |


### F.12:4 - Core idea (didactic)

**Bind promises to runs with measurements in time.**
Acceptance is a **quadruple of anchors** (all context‑local):

1. **ClauseCell** — a deontic/Standardual **SenseCell** stating the promise (*availability ≥ 99.9%*, *MTTR ≤ 60 min*, *temperature within band*).
2. **WorkCell** — a **SenseCell** for the **Work** that enacted **service delivery work** in the relevant situation.
3. **MeasureCell** — a **SenseCell** for the **Observation/Characteristic** used as evidence (KD‑CAL).
4. **Window** — the explicit period in which the judgement is made (F.10).

A **Predicate** compares the **Measure** against the **Clause** within the **Window**.
The **Status** (Satisfied/Violated/Inconclusive) attaches to **ClauseCell\@Window about WorkCell**, never to a plan.


### F.12:5 - Minimal vocabulary (this pattern only)

* **ClauseCell.** A context‑local deontic/Standardual concept (*SLO*, *obligation*, *target*), typically from *services/deontics* Contexts (e.g., **ITIL 4**, **ODRL**).
* **WorkCell.** A context‑local run‑time occurrence (PROV **Activity**, IEC **Task Execution**, etc.).
* **MeasureCell.** A context‑local observation concept (KD‑CAL **Observation** over a **Characteristic** with a **Scale/Unit**).
* **Window.** A time envelope (calendar month, batch, incident interval, shift) per F.10.
* **Predicate.** A clause‑shape: threshold, percentile, count‑within‑limit, band‑conformance, etc.
* **Bridge.** An explicit Cross‑context relation with **kind/CL/Loss** (F.7/F.9).

> **Context discipline.** Terms like *availability*, *activity*, *task*, *observation* are always read as **context‑local**. Cross‑use requires a **Bridge**.


### F.12:6 - The binding, as five mental rules (notation‑free)

**R1 — Locus rule.**
An acceptance verdict **attaches to the Clause**, scoped by a **Window**, **about a specific Work**:
`status(ClauseCell, WorkCell, Window) ∈ {Satisfied, Violated, Inconclusive}`.
*Reading:* We do not place “Satisfied” on the plan or on the whole service concept.

**R2 — Evidence rule.**
Only **Observations** (MeasureCell) that **refer to the outcome of the same Work** and **lie within the Window** may support the verdict.
*Reading:* Control commands and approvals are not evidence of outcome.

**R3 — Predicate rule.**
Every ClauseCell is read with a **Predicate** schema that defines how Measures decide:

* **Threshold:** `value ≥/≤ target`.
* **Percentile:** `Pₚ(value) ≤ target`.
* **Ratio/Share:** `good_time / total_time ≥ target`.
* **Count‑within‑limit:** `count(events of type E) ≤ target`.
* **Band:** `min(value) ≥ L ∧ max(value) ≤ U`.

**R4 — Bridge rule.**
If Clause, Work, and Measure live in **different Contexts**, apply declared **Bridges** with **kind**, **CL**, and **Loss** notes.
*Reading:* Without a Bridge, do not presume transferability of meanings.

**R5 — Window rule.**
Every verdict is **time‑bounded**. Changing the Window can change the result; **no retroactivity** from new clauses or specs (cf. F.10).


### F.12:7 - Clause templates (conceptual schemata)

> These are **shapes of meaning**, not data fields.

1. **Availability (share‑of‑time)**

* **ClauseCell:** *service availability ≥ 99.9% monthly* (services Context).
* **MeasureCell:** *uptime indicator* over **Work** (KD‑CAL).
* **Predicate:** `good_time/total_time ≥ 0.999`.
* **Window:** calendar month.
* **Bridge:** from monitor semantics → consumer‑perceived availability (**kind:** proxy; **CL:** 2; **Loss:** blind to partial degradations).

2. **Latency (percentile)**

* **ClauseCell:** *p95 latency ≤ 120 ms during incidents* (services Context).
* **MeasureCell:** *response time observation* for the same **Work episode** (KD‑CAL).
* **Predicate:** `P95(latency) ≤ 120ms`.
* **Window:** incident interval.
* **Bridge:** from request‑level telemetry → service‑level promise (**kind:** aggregation; **CL:** 2; **Loss:** sampling bias).

3. **Safety margin (band)**

* **ClauseCell:** *temperature ∈ \[L,U] during batch* (deontics/quality Context).
* **MeasureCell:** *process temperature observation* (KD‑CAL).
* **Predicate:** `min ≥ L ∧ max ≤ U`.
* **Window:** batch run interval (Work).
* **Bridge:** not needed if Measure and Clause are in the same Context; otherwise declare.

4. **MTTR (count‑within‑limit + duration)**

* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **MeasureCell:** *timestamps of Work phases* (start fix → restore).
* **Predicate:** `restore_time − start_fix ≤ 60 min`.
* **Window:** each incident’s **Work** interval.
* **Bridge:** BPMN design steps → PROV Work **Interpretation** (CL=2; **Loss:** gateways ≠ real branching).


### F.12:8 - Invariants (normative)

1. **Design/run split.** Clauses live on the **design stance**; judgements live on the **run stance** about **Work** (F.11).
2. **Context locality.** All terms are **context‑local**; Cross‑context meaning flows **only** across declared **Bridges**.
3. **Observation‑only evidence.** Verdicts require **Observations** that **about‑refer** to Work outcomes; **Actuation** and **Approvals** are not sufficient.
4. **Window explicitness.** Every verdict carries a **Window**; no timeless acceptance.
5. **Predicate declared.** The Clause’s **Predicate** is explicit; no hidden aggregation or default percentile.
6. **Non‑retroactivity.** Updating clauses or specs does not alter past verdicts; re‑evaluation must be explicit.
7. **One‑Work focus.** A verdict references a **specific Work** (or a defined population of Works) matched to the Clause’s scope.
8. **Loss honesty.** Each Bridge states **kind/CL/Loss**; stronger claims require stronger Bridges or same‑Context alignment.
9. **No detached pass.** When the ClauseCell is a `U.PromiseContent` (service promise clause), `Satisfied` about a Work is admissible only if that Work also **delivers** the promised outcome spec for the clause (A.2.3:8.1 `fulfilsPromiseContent`). This keeps acceptance on the **same delivery evidence base** (Work facts + Δ anchors + Observations) and prevents “pass verdict separate from delivery”.


### F.12:9 - Micro‑examples (didactic, multi‑domain)

#### F.12:9.1 - SaaS uptime (services + sensing)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure).
* **ClauseCell:** *availability ≥ 99.9% monthly*.
* **WorkCell:** *service delivery work* Activities during June.
* **MeasureCell:** *uptime observation* from synthetic probes.
* **Predicate:** share‑of‑time ≥ 0.999.
* **Bridge:** probe result → user availability (**kind:** proxy; **CL:** 2; **Loss:** regional gaps).
* **Verdict:** *Satisfied (June)* if the ratio holds; **attaches to Clause\@June about those Works**.

#### F.12:9.2 - Furnace band (industrial control)

* **Contexts:** *quality/deontics canon* (Clause), *IEC 61131‑3/PROV* (Work), *KD‑CAL* (Measure).
* **ClauseCell:** *product temperature within \[720,740] °C during soak*.
* **WorkCell:** *soak phase* Work interval.
* **MeasureCell:** thermocouple Observations (KD‑CAL).
* **Predicate:** band conformance.
* **Bridge:** IEC task interval → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Violated* if any measured value exits the band.

#### F.12:9.3 - Incident MTTR (services + enactment)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work).
* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **WorkCell:** each incident’s handling Activity.
* **MeasureCell:** timestamps (Observed facts) of start‑fix and restore events.
* **Predicate:** duration ≤ 60 min.
* **Bridge:** BPMN steps → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Satisfied* if the measured interval meets the target.

### F.12:10 - Anti‑patterns & remedies

| #       | Anti‑pattern                    | Symptom in practice                                                                          | Why it breaks thinking                          | Remedy (conceptual move)                                                                                                                                 |
| ------- | ------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Plan‑as‑proof**               | A BPMN or runbook is cited as if it proved the SLO was met.                                  | Design artefacts are **not** occurrences.       | Apply **R1 locus** + **R2 evidence**: attach the verdict to **ClauseCell\@Window about WorkCell** and require **Observations** of outcomes.              |
| **A2**  | **Signal‑as‑outcome**           | Control **Actuation** (setpoint writes, approvals) treated as evidence of delivered service. | Commands are intentions, not results.           | Accept only **MeasureCell** that **about‑refer** to the **same Work**; if a control signal is used as proxy, declare a **Bridge(kind=proxy, CL, Loss)**. |
| **A3**  | **Windowless verdict**          | “We met the SLA” with no stated period or scope.                                             | Unfalsifiable; mixes populations.               | Enforce **R5 Window**: every verdict names a **Window** (month, batch, incident interval).                                                               |
