`equivalent‑under‑assumptions` - `near‑equivalent` - `overlaps` - `broader‑than` - `narrower‑than` - `design‑spec‑of` - `run‑trace‑of` - `representation‑of` - `member‑of‑set‑in` - `provides‑value‑for`.

#### F.0.1:10.4 - Bridge composition (minimum CL and relation loss)

`Bridge(a,b,rel₁,cl₁) ∧ Bridge(b,c,rel₂,cl₂) ⊢ Bridge*(a,c,rel*,cl*)`

* `cl* := min(cl₁, cl₂)` (do **not** inflate confidence)
* `rel* := conservativeRel(rel₁, rel₂)` (e.g., near‑equiv composed with overlaps yields overlaps)

*Reading:* Chained passages inherit the minimum `CL` and the relation that remains admissible after composition.

#### F.0.1:10.5 - Non‑identity by stance

`SenseCell⟨x@A(design)⟩ ∧ SenseCell⟨y@B(run)⟩ ∧ ¬declared(Bridge(x,y,near‑equiv,_)) ⊢ ¬same‑row(x,y)`
*Different time stances forbid same‑row unless an explicit near‑equiv Bridge exists.*

#### F.0.1:10.6 - Row viability (Concept‑Set candidacy)

`Cells = {c₁…cₙ} ⊢ row‑viable(Cells) ⇔ connected(Cells, Bridges_{rel∈{equiv,near‑equiv}, cl≥k}) ∧ ¬contradiction(Cells)`

*Reading:* A row is viable if its cells form a connected subgraph via Bridges with sufficient CL and contain no mutually exclusive links.

#### F.0.1:10.7 - Contradiction sieve

`Bridge(a,b,broader) ∧ Bridge(a,b,narrower) ⊢ contradiction(a,b)`
*Incompatible relations across the same pair flag a contradiction for review (conceptually).*

#### F.0.1:10.8 - Non‑bridge implication ban

`name(x) = name(y) ∧ A≠B ⊢ ¬Bridge(x@A, y@B, _, _)`
*String equality across Contexts never implies a Bridge.*


### F.0.1:11 - SCR/RSCR acceptance checks (conceptual)

> *These checks are **content‑oriented**; they validate that a manuscript/model respects Part F principles. No process/tool assumptions are implied.*

#### F.0.1:11.1 - SCR — Static conformance

* **SCR‑F01 (Context‑qualified).** Every normative term is Context‑qualified (directly, or via a scoped header that unambiguously fixes the Context).
* **SCR‑F02 (Local cells).** Each SenseCell belongs to **exactly one** Context; no cell aggregates Cross‑context **senses**.
* **SCR‑F03 (senseFamily hygiene).** SenseCell glosses contain no behaviours/deontics/equations; those appear only in their patterns.
* **SCR‑F04 (Bridges explicit).** Every Cross‑context relation appears as a Bridge with `relation` and `CL` and a short **loss/fit** note.
* **SCR‑F05 (No string identity).** There is no use of string equality to stand in for Cross‑context identity.
* **SCR‑F06 (Time stance fidelity).** Where a Context fixes a `DesignRunTag`, the SenseCells and any Bridges reflect that stance explicitly.
* **SCR‑F07 (Row viability).** Any Concept‑Set row shown is supported by a connected subgraph of Bridges with **CL ≥ threshold** and no contradictions.

#### F.0.1:11.2 - RSCR — Regression & evolution

* **RSCR‑F01 (Edition split).** When a source edition changes materially, SenseCells tied to the old edition remain; new cells bind to the new Context; Bridges are re‑assessed.
* **RSCR‑F02 (Bridge stability).** If any Bridge endpoint changes gloss/stance, downgrade or retire the Bridge, documenting the **loss/fit** change.
* **RSCR‑F03 (Composition guard).** When composing Bridges in a chain, the resulting `CL` never exceeds the minimal link; relation `CL` drops monotonically.
* **RSCR‑F04 (Heterogeneity + QD guard):** requires ≥3 domain‑families AND MinInterFamilyDistance ≥ δ_family (per the active F1‑Card edition), with QD‑triad evidence (publish Diversity_P and IlluminationSummary on the declared grid/kernel). Near‑alias pairs (per dSig rule) SHALL be flagged and excluded or merged before the guard is evaluated. Record the F1‑Card edition id.

#### F.0.1:11.3 - Publish‑ready summary

An artefact is **ready** with respect to F.0.1 when:

1. **SCR‑F01…F07** hold for all terms, cells, rows, and bridges it presents;
2. **RSCR‑F01…F04** hold under simulated edition/stance changes;
3. Every Cross-context statement can be read as a **Bridge** or as a composition of Bridges with stated `CL` and relation loss.


### F.0.1:12 - Quick reference (didactic)

* **Context** = a `U.BoundedContext` with edition, scope, and (if inherent) time stance.
* **SenseCell** = the minimal, lexical unit of meaning inside a Context (Tech/Plain labels + gloss).
* **Bridge** = the only Cross‑context relation, labelled with `relation` and **CL**, plus a short loss/fit note.
* **Concept‑Set row** = a didactic table row collecting **SenseCells** that are sufficiently the‑same‑thing under declared Bridges.

> **Mental checklist:** *Name the Context → speak in the Context → connect Contexts only by labelled bridges → build rows from bridged cells.*

### F.0.1:End


## F.1 - Domain‑Family Landscape Survey

**“Fix the context of meaning before you name anything.”**
**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles**; A.7 **Strict Distinction (Clarity Lattice)**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**; **G.0–G.1** *(Scope/describedEntity handoff)*.  *(Bridges live only in F.9.)*

**Aliases (informative).** *Contexts‑first survey*; *Context cut*.

### F.1:1 - Intent & applicability

**Intent.** Establish a **finite set of U.BoundedContext** (“**context of meaning**”), each tied to an authoritative source or canon within a **domain family**, so that all later moves (term harvesting, clustering, role naming, cross‑context bridges) operate on **local meanings** rather than on drifting, globalised words.

**Applicability.** Use **at the start** of any unification effort for **any FPF pattern** (Enactment (`U.RoleAssignment` + `U.RoleEnactment`), Sys-CAL, KD-CAL, Kind-CAL, LCA-CAL…) and **whenever** a discipline canon materially changes (new edition, re-framing, seminal result).

**Non‑goals.** No tooling, workflow, or editorial roles. No global ontology. No cross‑context equations. This pattern describes **how to think**, not how to store.

### F.1:2 - Problem frame

Without explicit context of meaning:

1. **Word‑drift.** Common words (*process*, *role*, *service*, *model*) silently change sense across disciplines.
2. **Scope mirages.** One influential standard is mistaken for *the* domain.
3. **Retro‑lock.** Old editions become the implicit truth simply because they were “there first”.
4. **Category bleed.** Behavioural roles, epistemic statuses, deontic permissions mix because their contexts were never fixed.
5. **Name inflation.** New U.Types appear just to “stabilise” unstable words.


### F.1:3 - Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Universality vs locality** | We want cross‑domain unification, but **meaning is local** to a U.BoundedContext. |
| **Breadth vs parsimony**     | Wide coverage prevents bias; too many Contexts defeats understanding.                |
| **Recency vs continuity**    | New editions matter; but working knowledge often trails by years.                 |
| **Didactics vs fidelity**    | Pedagogically simple summaries must remain faithful to the source.                |


### F.1:4 - Core idea (didactic)

**Think in Contexts, not in words.**
A *Context of meaning* is a **U.BoundedContext** (per D.CTX) that encloses a coherent vocabulary and its rules from a **specific, citable canon** (standard, BoK, seminal paper, textbook tradition). You **name and reason** *inside the Context*. When you must step between Contexts, you will **declare a bridge later** (F.9) with explicit losses or mismatches.


### F.1:5 - Minimal vocabulary (this pattern only)

* **U.BoundedContext** (short: **Context** in Tech register). The formal *Context of meaning*.
* **Context** (Tech register alias for **U.BoundedContext**). Use **Context** for pedagogy, **U.BoundedContext** for formal references.
* **Domain family.** An **informative** shelf‑label grouping related Contexts (e.g., *workflow & provenance*; *services & deontics*; *sensing & measurement*; *types & taxonomies*; *control & actuation*). **No semantics** attach; Domain ≠ Context.
* **Context Card.** A **one‑screen** conceptual sketch of a Context (see §7.2).
* **SenseCell** *(appears downstream)*. A **(Context × Local‑Sense)** address; F.3 will mint these after clustering. Mentioned here only to keep the destination in view.


### F.1:6 - Solution — the Contexts‑first survey (conceptual, notation‑free)

**Step 1 — Declare your unification line(s).**
State which FPF pattern threads are in play (e.g., *Enactment + KD‑CAL sensing + Sys‑CAL execution*). This keeps the cut purposeful.

**Step 2 — Cut the landscape by domain families.**
For each line, **select at least three distinct domain families** (heterogeneity guard). Examples:

* *Workflow & provenance* (BPMN 2.0; W3C PROV‑O)
* *Services & deontics* (ITIL 4; ODRL 2.2)
* *Sensing & measurement* (SOSA/SSN; ISO 80000‑1)
* *Types & taxonomies* (OWL 2; FCA corpus)
* *Control & actuation* (state‑space control texts; IEC 61131‑3)

**Step 3 — For each family, sketch 1–3 Context Cards.**
Prefer canonical, widely cited canons. If a field is fragmented, choose one **exemplar** and one **counter‑voice** to surface heterogeneity.

**Step 4 — Make **locality** explicit.**
Treat words as **context‑local**. *Process (BPMN)* ≠ *process (thermodynamics)* ≠ *process (PROV)*. Do not reconcile. Do not average. **Just fix the Contexts.**

**Step 5 — Bound the set.**
Small enough to hold in working memory. As a rule of thumb:

* per unification line: **≥ 3 families**;
* per family: **1–3 Contexts**.
  More only if a missing Context hides a known sense‑split you will certainly need.

**Step 6 — Postpone bridges.**
If two Contexts seem “close”, **resist** collapsing. Note the tension and leave any bridge claim to **F.9 Alignment & Bridge**.

### F.1:7 - What to record (conceptual, not clerical)

**7.1 The two‑minute memory.**
Everything you need to *think correctly later* fits on an eight‑line card. No registries, no workflows, no storage choices.

**7.2 The Context Card (one‑screen sketch).**
*(Each bullet is a thought, not a field.)*

* **Name & edition.** *“BPMN 2.0 (2011)”* • *“W3C PROV‑O (2013)”* • *“ITIL 4 (2020)”*.
* **Domain family.** *workflow* / *provenance* / *services* / *deontics* / *sensing* / *types* / *control* … *(informative only; never used to infer meaning).*
* **Scope gist** *(didactic; ≠ `USM.ScopeSlice(G)`)*. One line that marks the **inside/outside** (“workflow **graphs & participants**”, “provenance **entities/activities/agents**”).
* **Time stance** *(if inherent)*. Does the canon speak **design** (specifications, models) or **run** (occurrences, acts)?
* **Lexical trip‑wires.** Known homonyms or false friends in this Context (*“process ≠ thermodynamic process”*, *“role (RBAC) ≠ behavioural role”*).
* **Neighbour Contexts** *(informative)*. Close cousins that people often conflate (*BPMN ↔ PROV‑O*, *ITIL ↔ ODRL*).
* **Recency note.** *Current* / *superseded* / *candidate* (only as a reminder to yourself which text you mean).
* **Why this Context matters here.** One sentence linking to your unification line (“we will name Executions later; PROV‑O keeps them run‑time”).
* **Diversity signature (dSig).** A 5-characteristics discrete signature for `U.BoundedContext`: **[Sector, Function, Archetype, Regime, MetricFamily]**. Authors SHOULD pick from local discipline taxonomies. **Publish a `dSigSource` list (five refs/URIs, one per characteristic) on every Card**, falling back to free-text only where no canonical term exists. Two Contexts are flagged as **Near-Duplicate** when ≥3 characteristics match. Publish `dSig` and `dSigSource` on every Card.

> *If your Card spills beyond a screen, you are collecting facts, not fixing meaning.*

F1‑Card (normative artefact): { taxonomyRef, embeddingRef, DistanceDef, δ_family, confidenceBand, calibrationSet, edition, subFamilyDef? }. subFamilyDef (optional): declares the stable partitioning below a domain‑family (e.g., taxonomic sub‑fields or CVT clusters with parent family anchors).  When HET‑FIRST quotas refer to “sub‑family”, they MUST use this declared subFamilyDef.
Declare **DomainDistance** policy (cosine or transport) and δ_family threshold; version as part of DescriptorMapRef. Publish `confidenceBand` (e.g., CI90%) for the calibrated `δ_family`; treat numbers in examples as illustrative, not normative.

### F.1:8 - Invariants (normative, lightweight)

1. **Context ≡ U.BoundedContext.** In this pattern, *Context* always means **U.BoundedContext** (per E.10.D1).
2. **Locality.** Words are **local to their Context**; no global meaning is implied or imported.
3. **Heterogeneity.** Each unification line considers **≥ 3 distinct Domain families** (labels are informative only).
4. **Parsimony.** Prefer few, canonical Contexts per family (1–3) that jointly expose the key sense splits.
5. **No bridging here.** No equivalence or mapping is asserted between Contexts in F.1. (Bridges live in **F.9**.)
6. **DesignRunTag honesty.** If a canon fixes a DesignRunTag, note it. Do not reinterpret.
7. **Didactic primacy.** Each Context Card must be readable by a thoughtful engineer in **under two minutes**.
8. **Domain‑family neutrality.** Domain families **carry no semantics**; they SHALL NOT be used for inheritance, inference, or bridge implication.
9. **Scope naming separation.** `Scope gist` on Cards is **didactic only**; formal *Scope/describedEntity* (=`USM.ScopeSlice(G)` ⊕ `describedEntity(GroundingHolon, ReferencePlane)`) is declared **in G.0–G.1**, not in F.1.
10. **Diversity signature present.** Each Context Card PUBLISHES a `dSig` in the 5‑characteristics form.
11. **Collision rule.** If any pair of Cards has `dSig` matching on ≥3 characteristics, mark **Near‑Duplicate** and either merge  into one slot or replace one by a Context from a different domain‑family. Record action in SCR.

### F.1:9 - Self‑checks (mental, not procedural)

* **The mirror test.** Can you explain *why each Context is inside* your cut **in one breath**? If not, you are surveying for comfort, not for meaning.
* **The homonym ping.** For each frequent word (*process*, *role*, *service*, *model*, *execution*), can you immediately list **the Contexts where it differs**? If not, add the missing Context.
* **The bridge itch.** Feel the temptation to say “these are the same”? Good. **Write the itch down** and refuse to scratch it here. That’s F.9’s job.
* **The memory rule.** If your entire survey cannot be recalled **without opening a document**, it is too large.


### F.1:10 - Micro‑examples (illustrative only)

*One unification line: Enactment (`U.RoleAssignment` + `U.RoleEnactment`) with sensing and execution.*

* **BPMN 2.0 (2011)** — *workflow family*.
  *Scope gist:* flow nodes, sequence flows, participants (design‑time).
  *Trip‑wires:* “process” here is a **graph**; not a run.
* **W3C PROV‑O (2013)** — *provenance family*.
  *Scope gist:* **Activity** that uses/generates entities (run‑time).
  *Trip‑wires:* “activity/process” here is a **temporal occurrence**.
* **ITIL 4 (2020)** — *services family*.
  *Scope gist:* service as value co‑creation; SLO/SLA (deontic talk nearby).
  *Trip‑wires:* “incident/problem/practice” don’t equal workflow tasks.
* **ODRL 2.2** — *deontics family*.
  *Scope gist:* permissions, prohibitions, duties (design).
  *Trip‑wires:* “duty/obligation” ≠ service guarantee mechanics.
* **SOSA/SSN (2017)** — *sensing family*.
  *Scope gist:* Observation as an act yielding a Result for a property.
  *Trip‑wires:* “observation” ≠ “state”; it’s an **act** with a **procedure**.
* **IEC 61131‑3** — *control languages family*.
  *Scope gist:* tasks that **execute** programs (run‑time).
  *Trip‑wires:* “task/execution” ≠ “workflow process”.

> With only these Contexts fixed, later steps become almost mechanical: F.2 harvests terms **inside** each Context; F.3 clusters **within** each Context; F.4 names roles or statuses pointing to **SenseCells**; F.9 draws the bridges you refused to draw here.

### F.1:11 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in practice                                                                  | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                |
| ------- | -------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **“One‑Book Domain”**      | Everything is justified from a single canon (“X is the domain”).                     | Projectionism; blinds heterogeneity; brittle to new editions.  | Enforce **heterogeneity**: pick **≥ 3 distinct domain families** per unification line (§6 Step 2, §8‑3).                |
| **A2**  | **Context‑less talking**   | Words like *process*, *role*, *service* used without naming a Context.                  | Global words drift; later steps must guess meaning.            | Always **prefix with the Context** in thought and prose: *process (BPMN)*, *activity (PROV)*, *service (ITIL)* (§4, §7.2). |
| **A3**  | **Edition blur**           | “BPMN” or “ITIL” cited with no year or profile.                                      | Inadvertent sense shifts; debates about “what the book says.”  | Cards keep **name + edition** on the first line; think with the exact edition (§7.2).                                   |
| **A4**  | **Phonebook survey**       | Dozens of Contexts; no one can recall the cut.                                          | Violates didactic primacy; people default to global talk.      | **Parsimony rule**: 1–3 Contexts per family, just enough to reveal key sense‑splits (§6 Step 5, §8‑4, §9 “memory rule”).   |
| **A5**  | **Bridge‑by‑stealth**      | Phrases like “these are basically the same” inside the survey.                       | Hides losses; imports meaning across Contexts without scrutiny.   | **No bridging here**; write the *itch to bridge* down as an **F.9** bridge question (§6 Step 6, §8‑5).                           |
| **A6**  | **Role/status conflation** | *Role (RBAC)* treated as behavioural mask; *duty (ODRL)* treated as service runtime. | Category bleed across families.                                | Cards carry **lexical trip‑wires** (“RBAC role ≠ behavioural role”; “duty ≠ runtime guarantee”) (§7.2).                 |
| **A7**  | **Temporal fudge**         | *Activity* or *execution* discussed without run/design stance.                       | Misplaced assertions; design-time descriptions treated as occurrences. | Cards note **time stance** when inherent (design vs run) (§7.2, §8‑6).                                                  |
| **A8**  | **Domain = Context**       | A “domain” label used as if it were a Context (e.g., “control” == one context).         | Shelf label mistaken for a canon; sense becomes fuzzy.         | **Domain family is informative only**; Contexts are **U.BoundedContext** tied to specific canons (§5, §7.2).               |
| **A9**  | **Context inheritance**    | Arranging Contexts in is‑a hierarchies (“PROV is‑a BPMN”).                              | Suggests meaning flows by inheritance; erases locality.        | **No is‑a among Contexts**; relations between Contexts live in **F.9 bridges** (§8‑5).                                        |
| **A10** | **Didactic bloat**         | Context Card spills into pages of notes.                                             | Teaching load overwhelms the core idea.                      | **One-screen Card**; everything else belongs to later patterns (§7.1-§7.2).                                             |
| **A11** | **Family‑based inference** | Treating Domain‑family membership as implying similarity/equivalence. | Smuggles semantics via shelf labels; breaks locality. | **Domain family is informative only**; locality and any Cross‑context relation must be explicit (F.9). |

### F.1:12 - Worked examples

> Each example shows **the cut** (the Contexts you keep in view) and the **thinking pay‑off** you get *before* any harvesting, clustering, or bridging.

#### F.1:12.1 Enactment (`U.RoleAssignment` + `U.RoleEnactment`) with sensing & execution (service acceptance)

**Unification line.** Enactment + KD‑CAL (sensing) + Sys‑CAL (execution).

**Contexts (six Cards).**

1. **BPMN 2.0 (2011)** — workflow family; **design**; *graph of flow nodes, participants*.
2. **PROV‑O (2013)** — provenance family; **run**; *Activity uses/generates Entities; Agents*.
3. **ITIL 4 (2020)** — services family; **design**; *service, SLO/SLA vocabulary*.
4. **ODRL 2.2** — deontics family; **design**; *permission / prohibition / duty*.
5. **SOSA/SSN (2017)** — sensing family; **run**; *Observation as act with Result*.
6. **IEC 61131‑3** — control languages; **run**; *tasks execute control programs*.

**Thinking pay‑off (examples).**

* You stop saying “*process uptime*” and think **Execution (IEC)** measured by **Observation (SOSA)** compared against **SLO (ITIL)**—three Contexts, three senses.
* You mark a trip‑wire: **RBAC role** (not in this cut) is *not* a **behavioural role (BPMN participant)**.
* You resist equating **PROV Activity** with **BPMN workflow**; later **F.9** may relate them with explicit loss.


#### F.1:12.2 Method quartet with types & measurement (model state graph)

**Unification line.** Method‑CAL + Kind-CAL + KD‑CAL.

**Contexts (five Cards).**

1. **SPEM 2.0 / ISO 24744** — methods family; **design**; *Method and MethodDescription language*.
2. **OWL 2 (profiles)** — types family; **design**; *class, subclass, equivalent class*.
3. **FCA corpus** — types family; **design**; *concept lattices*.
4. **SOSA/SSN (2017)** — sensing family; **run**; *Observation / Procedure*.
5. **ISO 80000‑1 (2022)** — metrology family; **design**; *quantity kinds, units*.

**Thinking pay‑off.**

* You keep **Method** (abstract how‑to) separate from **MethodDescription** (epistemic recipe) and **Execution** (run) because the Contexts already split design vs run.
* You avoid treating **FCA “concept”** as a **U.Type**; later F.9 can bridge OWL classes to FCA concepts with cautions.


#### F.1:12.3 Control & actuation with services (operational SLOs in plants)

**Unification line.** Sys‑CAL + LCA‑CAL (planned) + services/deontics.

**Contexts (five Cards).**

1. **State‑space control texts** — control family; **design**; *controller/plant, feedback*.
2. **IEC 61131‑3** — control languages; **run**; *task, program execution*.
3. **ISA‑95** — integration family; **design**; *levelled layers, interfaces*.
4. **ITIL 4 (2020)** — services family; **design**; *SLO/SLA*.
5. **SOSA/SSN (2017)** — sensing family; **run**; *Observation*.

**Thinking pay‑off.**

* “**Actuation**” is recognised as **control output** (Sys‑CAL), not a *service promise*.
* “**Incident**” (ITIL) is not a plant *fault* (Sys‑CAL); Contexts deter category errors.


### F.1:13 - Reasoning primitives (judgement schemas, notation‑free)

> These are **mental moves**, not queries. They read “given these thoughts, this conclusion is safe to hold (conceptually).”

1. **Context set for a line**
   `line L declared ⊢ Contexts(L) = {C₁,…,Cₙ}`
   *Reading:* For a unification line **L**, the Contexts you deliberately keep in view are `{C₁,…,Cₙ}` (from your Cards).

2. **Heterogeneity check**
   `families(L) = F ⊢ heterogeneous(L) ≡ (|distinct(F)| ≥ 3)`
   *Reading:* Your cut is heterogeneous if it spans at least three **domain families**.

3. **Parsimony check**
   `Contexts(L)=R, families(L)=F ⊢ parsimonious(L) ≡ (∀f∈F: 1≤|R∩f|≤3)`
   *Reading:* Each family contributes a few Contexts, not a phonebook.

4. **Locality assertion**
   `term w, C∈Contexts(L) ⊢ meaning(w)@C is local`
   *Reading:* A word’s sense is **context‑local**; no global meaning is implied.

5. **Time‑stance guard**
   `C has stance s∈{design,run} ⊢ claims@C must respect s`
   *Reading:* If a Context is design‑time, do not make run‑time claims in it (and vice versa).

6. **Trip‑wire recall**
   `C lists tripWires T ⊢ for any w∈T, require Context‑prefix when speaking`
   *Reading:* Words on the trip‑wire list must be spoken with the Context name.

7. **Bridge embargo**
   `C₁≠C₂ ⊢ no‑equivalence(C₁,C₂) within F.1`
   *Reading:* F.1 never asserts equivalence across Contexts; postponement is principled, not procrastination.

8. **Context sufficiency probe**
   `common‑word w used in L ∧ w not covered by any trip‑wire ⊢ consider adding a Context that makes w differ`
   *Reading:* If a frequent word has no deliberate sense‑split in your cut, you may be missing a Context.

9. **Memory rule**
   `|Contexts(L)| too large ⊢ reduce until a careful mind can recite them unaided`
   *Reading:* The survey should live in memory, not in a registry.

### F.1:14 - F1‑Card example (informative)
```
F1-Card v2025‑Q3:
  taxonomyRef: OpenAlex topics/fields (snapshot 2025‑08)
  embeddingRef: SPECTER2(2023) fine‑tuned@OA‑2025‑08
  DistanceDef: cosine on centroid embeddings (window 36 mo)
  δ_family: 0.35 (calibrated on control set; CI90% [0.33,0.37])
  calibrationSet: 120 labeled pairs (same vs different families)
  edition: 2025‑Q3
```
### F.1:15 - Relations (with other patterns)

**Builds on:**
E.10.D1 **Lexical Discipline for “Context” (D.CTX)** — ensures *Context* ≡ *U.BoundedContext* and reserves “Problem Frame” for narrative use.
A.7 **Strict Distinction** — guards object/description/carrier and DesignRunTag splits while you cut Contexts.
A.11 **Ontological Parsimony** — motivates the small cut.

**Constrains:**
**F.2** (Term Harvesting): harvest **inside** Contexts named here; every occurrence carries a Context name.
**F.3** (Intra‑Context Sense Clustering): cluster **per Context**; no Cross‑context sense claims.
**F.4** (Role Descriptions): any role template or status template must cite a **SenseCell** that lives in a Context from this cut.
**F.9** (Alignment & Bridge): only F.9 may relate Contexts; never F.1–F.4.

**Used by.**
Extention patterns in Part C (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL, LCA‑CAL) as the *lexical starting grid* for their examples and definitions.


### F.1:16 - Migration notes (conceptual)

1. **New edition appears.** Keep the old Card; add a new Card with the new edition. If the sense shifts, treat it as a **new Context**; if it is strictly editorial, mark recency but keep one context.
2. **New family emerges.** If a missing family explains recurrent confusion in your line, admit it with **one exemplar** Context; remove a less informative Context to keep parsimony.
3. **Language variants.** Treat language editions as **separate Contexts** unless the canon itself declares a single normative bilingual mapping.
4. **Trip‑wire growth.** When you notice a recurring confusion, add a crisp trip‑wire to the relevant Card (one line; no essays).
5. **Bridges discovered later.** Do not back‑port bridges into F.1; leave the Cards untouched and record the mapping in **F.9**.
6. **Dormant Contexts.** If a Context no longer contributes to any active line, move it to a *parking shelf* (informative note on the Card) rather than deleting it.


### F.1:17 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.1:17.1 - Static conformance checks (SCR)

* **SCR‑F1‑S01 (Heterogeneity).** For each unification line, the set of Cards spans **≥ 3 distinct domain families**.
* **SCR‑F1‑S02 (One‑screen Cards).** Each Card fits on one screen: name+edition; family; scope gist; time stance (if inherent); 1–3 trip‑wires; neighbour Contexts (optional); recency note.
* **SCR‑F1‑S03 (Locality pledge).** Nowhere in F.1 are Cross‑context equivalences or merges asserted.
* **SCR‑F1‑S04 (Parsimony).** In every family, **1–3** Contexts are kept; if more, a clear sentence justifies each extra Context’s unique sense contribution.
* **SCR‑F1‑S05 (Context discipline).** “Context” is used only as a synonym of **U.BoundedContext**; “domain” appears only as an informative family label.
* **SCR‑F1‑S06 (Temporal honesty).** If a canon fixes DesignRunTag, the Card states it.
* **SCR‑F1‑S07 (Family neutrality).** No claim, classification, or relation in F.1 relies on Domain‑family membership; families appear only as shelf labels on cards.
* **SCR‑F1‑S08 (dSig present).** Every Context Card has a 5‑characteristics `dSig`.
* **SCR‑F1‑S09 (Collision policy).** Any pair with `dSig` match on ≥3 characteristics is either merged or replaced; SCR records the action.

#### F.1:17.2 - Regression checks (RSCR)

* **RSCR‑F1‑E01 (Edition churn).** When a new edition is added, prior Cards remain; no silent replacement.
* **RSCR‑F1‑E02 (Family balance).** Adding/removing Cards does not drop any line below **three families**.
* **RSCR‑F1‑E03 (Trip‑wire coverage).** After introducing a new Context, the trip‑wire lists of neighbouring Contexts are reconsidered and updated if needed.
* **RSCR‑F1‑E04 (No creep).** Periodically apply the **memory rule**: if the cut no longer fits in working memory, shrink it.


### F.1:18 - Didactic distillation (90‑second teaching script)

> “Before you name anything, **fix the context of meaning**. A *Context* is a **U.BoundedContext** tied to a specific canon—*BPMN 2.0*, *PROV‑O*, *ITIL 4*, *SOSA/SSN*, *IEC 61131‑3*, *OWL 2*. Words are **local to Contexts**: *process (BPMN)* is a workflow graph, *activity (PROV)* is a run‑time occurrence, *service (ITIL)* is a promise vocabulary. Cut the landscape so each unification line sees **at least three domain families**, with **one‑screen Cards** per Context (scope gist, time stance, trip‑wires). **Do not bridge** Contexts here—just write down the itch to bridge as an **F.9** bridge question. Keep the cut **small enough to remember**. With Contexts fixed, harvesting (F.2), local clustering (F.3), role template or status templates (F.4), and explicit Cross‑context bridges (F.9) become straightforward—and you avoid naming ghosts that come from words floating without walls.”

### F.1:End

## F.2 — Term Harvesting & Normalisation

**“Harvest words *inside Contexts*, name them in the Context’s own idiom, and stop there.”**
**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles** (Source - Local Meaning - Bridge‑Only Crossing); A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.1 **Context Map via Context Cards**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local harvesting*; *Local normalisation*.


### F.2:1 - Intent & applicability

**Intent.** Provide a **conceptual** (notation‑free) discipline for turning *Context‑internal usage* into **context‑local lexical units** ready for later reasoning—without Cross‑context merging and without slipping into governance or tooling. The result is a **small, auditable set of context‑local names and glosses** that faithfully reflect how the canon speaks.

**Applicability.** Use whenever a unification line (from F.1) needs **actual words** to be referenced by patterns in Part C (Extention patterns) or by Role Descriptions (F.4). Re‑enter F.2 when a canon/edition changes or when a new Context is admitted in F.1.

**Non‑goals.** No global labels; no Cross‑context equivalence; no workflow or role descriptions; no storage/API talk. F.2 specifies **how to think**, not how to “run a pipeline”.


### F.2:2 - Problem Frame

Even with Contexts fixed (F.1), three mistakes recur:

1. **Word‑centrism.** Treating a string as if it carried its meaning across Contexts (*process*, *role*, *service*).
2. **Over‑normalisation.** Forcing one spelling/morphology across different canons, erasing Context‑specific cues.
3. **Premature structure.** Smuggling behaviour, deontics, or type structures into what should remain **lexical**.

F.2 prevents these by **localising** meaning and **naming** strictly **inside** each Context.


### F.2:3 - Forces

| Force                      | Tension to resolve                                                               |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Uniformity vs locality** | Desire for consistent names vs Context‑specific idioms that must be preserved.      |
| **Parsimony vs recall**    | Keep the harvested set small vs keep rare but pivotal terms that unlock bridges. |
| **Didactics vs fidelity**  | Two‑register labels (tech/plain) vs fidelity to the canon’s own phraseology.     |
| **Speed vs safety**        | Move fast to enable F.3/F.4 vs avoid any Cross‑context conclusion in F.2.           |


### F.2:4 - Core idea (didactic)

**Harvest *inside* each Context; name *in that Context’s idiom*; do not cross Contexts.**
For every Context (a **U.BoundedContext** from F.1), you gather **attested phrases** as *thought‑cues*, choose a **Local Normal Form (LNF)** that matches the Context’s idiom, attach a **two‑register label** (Tech/Plain), and write a **one‑sentence gloss**. That’s all. You do **not** claim sameness with any other Context; you do **not** embed behaviour or deontics; you do **not** mint U.Types here. These *local lexical units* will become **Local‑Senses** in F.3 and later addressable **SenseCells** (Context × Local‑Sense).


### F.2:5 - Minimal vocabulary (this pattern only)

* **Context** — Tech‑register alias for **U.BoundedContext** (per E.10.D1).
* **Attested phrase** — A short, verbatim cue from the canon that shows how a word is used **in this Context** (citation idea, not a record format).
* **Local Normal Form (LNF)** — The Context‑specific canonical surface you will use when referring to the term in this Context (minimal editing: spelling/hyphenation/casing per the canon).
* **Two‑register label** — **Tech** (engineer‑facing) and **Plain** (pedagogic) forms for the same Context‑local meaning.
* **Gloss (one‑sentence)** — A **Context‑faithful** description of how the canon uses the term, at **minimal generality**.
* **Local lexical unit** — The quintet *(Context, LNF, Tech, Plain, Gloss)*. This is F.2’s only outcome.
* **Homonymy (signal)** — Awareness that the **same string** has **different local lexical units** across Contexts (no relation asserted).
* **SenseCell** *(appears downstream)* — Address **(Context × Local‑Sense)** minted in F.3; mentioned here so you know what you’re preparing.

> *Everything above is a way of thinking. None of it implies a database, statuses, or roles.*


### F.2:6 - Solution — three mental moves (notation‑free)

#### F.2:6.1 - Move A — **Localise the word**

**Question to ask.** *“In which Context am I hearing this word?”*
**Action (mental).** Point to a specific **Context** (from F.1). Grab 1–2 **attested phrases** that are representative **in this Context**.
**Outcome.** You stop thinking “global word” and start thinking “context‑local usage”.

*Micro‑cue.* If you cannot name the Context, do not harvest the word.


#### F.2:6.2 -Move B — **Name it in the Context’s idiom**

**Question to ask.** *“How would this Context itself write it?”*
**Action (mental).** Choose the **LNF** (Context‑conformant spelling/hyphenation). Then write the **two‑register label** and a **one‑sentence gloss** that says **what the canon means here**—nothing more.
**Outcome.** You have a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.

*Micro‑cues.*
• Prefer the canon’s head noun; keep canonical hyphens; avoid invented compounds.
• The **Plain** label should help a non‑specialist; the **Tech** label should match engineers’ eyes.
• The **Gloss** must fit on a single line; put details in F.3.


#### F.2:6.3 - Move C — **Fence it off**

**Question to ask.** *“What must I refuse to conclude here?”*
**Action (mental).** Explicitly **refuse** to: (1) compare across Contexts, (2) fold morphology that the canon treats as meaningful, (3) embed behaviour, deontics, or type structure.
**Outcome.** A clean, **context‑local** lexical unit that will be safe to cluster in F.3 and safe to bridge (or not) in F.9.


### F.2:7 - Guard‑rails (normative, lightweight)

1. **context‑locality.** Every local lexical unit **MUST** cite a Context (U.BoundedContext from F.1).
2. **Context‑idiom normalisation.** LNF **MUST** respect the Context’s idiom (spelling/hyphenation/casing) and use **minimal edits**.
3. **Two registers.** Each unit **SHOULD** carry both **Tech** and **Plain** labels for didactics; if one is missing, justify.
4. **Minimal generality (G‑1).** The gloss **MUST** be as specific as the Context’s canon requires—no broader.
5. **I/D/S layer hygiene (A.7).** **MUST NOT** include behaviour equations, deontic rules, measurement math, or type axioms; those belong to patterns.
6. **No Cross‑context claims.** **MUST NOT** assert equivalence, subsumption, or similarity with terms in other Contexts (F.9 only).
7. **Edition honesty.** If the Context’s canon has multiple editions with shifting usage, treat them as distinct Contexts in F.1 before harvesting.
8. **Parsimony.** Prefer **few, telling** lexical units over long tails; keep head terms that will power F.3/F.4/F.9.


### F.2:8 - Micro‑examples (illustrative, context‑local)

> Each line is *one* local lexical unit. No relations are implied across lines.

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` - **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` - **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and is linked to agents.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` - **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

* **Context:** *NIST RBAC (2004)* — **LNF:** `role`
  **Tech:** `access‑role` - **Plain:** `permission role`
  **Gloss:** “Named grouping of permissions assignable via sessions.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` - **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` - **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”


### F.2:9 - Didactic heuristics (informative)

* **Keep the Context prefix in your inner speech.** Say “*process (BPMN)*”, “*activity (PROV)*”.
* **Prefer head nouns.** If the canon says “service‑level objective”, do not shorten it to “objective”.
* **Resist elegance that erases signal.** Hyphens and case often carry the Context’s culture; keep them.
* **Gloss from use, not from opinion.** Quote in your mind, then compress; avoid importing definitions from neighbouring Contexts.

### F.2:10 - Anti‑patterns & remedies

| #       | Anti‑pattern                 | Symptom (in thought or prose)                                        | Why harmful                                                  | Remedy (conceptual move)                                                                                |
| ------- | ---------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **A1**  | **Global normal form**       | One “canonical” label reused across Contexts.                           | Erases local meaning; invites stealth bridges.               | Keep **LNF per Context**; any Cross‑context relation belongs to **F.9** only.                                 |
| **A2**  | **String = meaning**         | Assuming identical strings denote one concept across Contexts.          | Homonym collision (*process*, *role*, *service*).            | Always prefix mentally with the **Context**; treat same string in different Contexts as **different units**.  |
| **A3**  | **Over‑normalisation**       | Folding hyphens/case/morphology “for consistency”.                   | Loses the canon’s idiom; breaks citations.                   | **Minimal edits** toward the Context’s idiom; never toward a global house‑style.                           |
| **A4**  | **Headless multiword**       | Truncating to a head (“objective” for “service‑level objective”).    | Ambiguity; collapses scope.                                  | Preserve canonical **head‑modifier** as LNF when meaningful.                                            |
| **A5**  | **Premature structure**      | Embedding behaviour, deontics, units, or type axioms into the gloss. | I/D/S layer mixing (violates A.7); biases later patterns.          | Gloss **usage**, not calculus; structural content belongs to Extention Patterns in Part C.                   |
| **A6**  | **Cross‑context folding**       | “BPMN workflow ≈ PROV activity” written inside F.2.                   | Hidden bridge; unpriced losses.                              | No Cross‑context claims in F.2; write the **itch to bridge** for **F.9**.                                  |
| **A7**  | **Edition blur**             | “BPMN” without year/profile; mixing excerpts across editions.        | Silent sense shift; unrepeatable reasoning.                  | Treat distinct editions as **distinct Contexts** in F.1, then harvest.                                     |
| **A8**  | **Vendor‑dialect elevation** | Treating a DSL/keyword list as “the domain”.                         | Projectionism; narrow idiom dominates.                       | If needed, model the DSL as **one context among others**; keep heterogeneity from F.1.                     |
| **A9**  | **Tail chasing**             | Harvesting hundreds of rare terms.                                   | Cognitive overload; dilutes signal.                          | Keep **head terms** that feed F.3/F.4/F.9; justify rare units by their bridging value.                  |
| **A10** | **Fake symmetry**            | Tech and Plain labels are identical jargon.                          | Didactic failure.                                            | Make **Plain** genuinely explanatory; keep **Tech** faithful to the canon.                              |
| **A11** | **Temporal fudge**           | Using run‑time words in design Contexts (or vice versa).                | Category drift; later contradictions.                        | Respect the Context’s **DesignRunTag** from its Card (F.1 §7.2).                                      |
| **A12** | **Cross‑language collapse**  | Merging bilingual terms as one unit.                                 | Erases idiom‑specific signals; hides normative mapping gaps. | Treat each language edition as its **own Context** unless the canon declares a normative mapping.          |
| **A13** | **Alias inflation**          | Inventing new local names “for clarity”.                             | Strays from the canon; hinders bridging.                     | Prefer the canon’s idiom; keep invented phrasings to the **Plain** register only.                       |
| **A14** | **Role/status conflation**   | RBAC “role” glossed as behavioural role.                             | Cross‑family bleed; wrong assignment later.                         | Call out the Context in the label: **access‑role (RBAC)** vs **participant (BPMN)**; keep senses disjoint. |


### F.2:11 - Worked examples (context‑local only)

> Each line is a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.
> No Cross‑context relation is implied. Later clustering (F.3) and bridges (F.9) may connect them.

#### F.2:11.1 Enactment + sensing

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` - **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` - **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and links to agents.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` - **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` - **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

*Thinking pay‑off:* you can phrase “compare **observation** to **service‑level‑objective**” without importing workflow or provenance semantics.


#### F.2:11.2 Sys‑CAL / LCA‑CAL + services

* **Context:** *State‑space control texts* — **LNF:** `actuation`
  **Tech:** `actuation` - **Plain:** `control output`
  **Gloss:** “Signal applied to the plant to influence state or output.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` - **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `incident`
  **Tech:** `incident` - **Plain:** `reported disruption`
  **Gloss:** “Unplanned interruption or reduction in the quality of a service.”

*Thinking pay‑off:* avoids calling a plant fault an “incident” unless you **cross Contexts later** with an explicit bridge.


#### F.2:11.3 Kind-CAL + Method‑CAL + KD‑CAL

* **Context:** *OWL 2 (profiles)* — **LNF:** `subclass‑of`
  **Tech:** `subclass‑of` - **Plain:** `is‑a (type hierarchy)`
  **Gloss:** “C ⊑ D: every instance of C is an instance of D.”

* **Context:** *FCA corpus* — **LNF:** `formal‑concept`
  **Tech:** `formal‑concept` - **Plain:** `extent–intent node`
  **Gloss:** “Maximal (objects, attributes) pair under a Galois connection.”

* **Context:** *SPEM 2.0 / ISO 24744* — **LNF:** `method`
  **Tech:** `method` - **Plain:** `abstract way of doing`
  **Gloss:** “Abstract how‑to independent of specification or execution.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `procedure`
  **Tech:** `procedure` - **Plain:** `measurement recipe`
  **Gloss:** “Specification guiding how an observation is produced.”

*Thinking pay‑off:* discourages treating an FCA “concept” as a `U.Type`, or a **procedure** as a **method** without later proof.


### F.2:12 - Reasoning primitives (judgement schemas, notation‑free)

> Read each as a **permitted mental move** over the outcomes of F.2.
> Symbols: `R` = Context (U.BoundedContext), `u` = local lexical unit, `s` = lexical string.

1. **Localisation**
   `heard(s) ∧ R chosen ⊢ localize(s,R)`
   *You decide to hear `s` only **in** Context `R`.*

2. **Context‑idiom normalisation**
   `localize(s,R) ⊢ LNF_R(s) = ℓ`
   *Within `R`, the **Local Normal Form** for `s` is `ℓ`.*

3. **Unit formation**
   `LNF_R(s)=ℓ ∧ labelTech=t ∧ labelPlain=p ∧ gloss=g ⊢ unit(u) = ⟨R,ℓ,t,p,g⟩`
   *A **local lexical unit** is formed (quintet).*

4. **Lexical‑only guard**
   `unit(u) ⊢ lexicalOnly(u)`
   *No behavioural/deontic/type math is attached to the gloss.*

5. **Homonymy signal (Cross‑context)**
   `LNF_Ra(s)=ℓa ∧ LNF_Rb(s)=ℓb ∧ Ra≠Rb ⊢ homonymy(s) ⊇ {Ra,Rb}`
   *Same string across Contexts is flagged as **different** by default.*

6. **Minimal generality check**
   `unit(u) ⊢ minimal(u) ⇔ gloss(u) says no more than the Context’s usage requires`
   *The gloss fits the Context; broader claims are withheld.*

7. **Two‑register adequacy**
   `unit(u) ⊢ didactic(u) ⇔ (tech(u) faithful) ∧ (plain(u) explanatory)`
   *Tech stays canonical; Plain helps non‑specialists.*

8. **No Cross‑context conclusion**
   `unit(u@Ra), unit(v@Rb), Ra≠Rb ⊢ ¬(u ≡ v) (within F.2)`
   *F.2 never asserts Cross‑context equivalence.*

9. **Ready‑for‑F.3 signal**
   `lexicalOnly(u) ∧ minimal(u) ∧ didactic(u) ⊢ readyF3(u)`
   *A unit is suitable input for **intra‑Context clustering** in F.3.*


### F.2:13 - Relations

**Builds on:**
**F.1** (Contexts fixed; heterogeneity/parsimony in place).
**E.10.D1 D.CTX** (Context ≡ U.BoundedContext; “Problem Frame” reserved for narrative).
**F.0.1** (Source - Local Meaning - Bridge‑Only Crossing).

**Constrains:**
**F.3** (Intra‑Context Sense Clustering): operates **only** on units **from one Context**; produces Local‑Senses and addressable **SenseCells**.
**F.4** (Role Description Definition): may **cite SenseCells**, not raw strings.
**F.9** (Alignment & Bridge): consumes **homonymy signals**; declares explicit Cross‑context mappings with loss policies.

**Used by.**
Extention patterns in Part C when referencing domain idioms (labels stay **context‑local**).


### F.2:14 - Migration notes (conceptual)

1. **New edition appears.** Add a Context in F.1; harvest afresh in F.2 using that Context; do not overwrite earlier units.
2. **Idiomatic update discovered.** If your LNF fought the canon’s idiom, **re‑LNF** within the same context; keep labels/glosses steady unless the canon itself differs.
3. **Ambiguity inside a Context.** If use splits, **mint two units** with distinct glosses; F.3 will sort their relation (same/different Local‑Sense).
4. **Language split.** Treat each language canon as its **own Context**; resist cross‑language merges in F.2.
5. **Tail pruning.** If units accumulate without feeding F.3/F.4/F.9, drop them from the working set; keep head terms that carry bridges.
6. **DSL quarantine.** If a tool dialect is unavoidable, keep it as one context among others; never let it define the idiom for other Contexts.


### F.2:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.2:15.1 - Static conformance (SCR)

* **SCR‑F2‑S01 (context‑locality).** Every unit cites a Context from F.1.
* **SCR‑F2‑S02 (Idiomatic LNF).** Each LNF reflects the Context’s spelling/hyphenation/casing with **minimal edits**.
* **SCR‑F2‑S03 (Two registers).** Each unit carries both **Tech** and **Plain** labels; if not, a reason exists tied to didactics.
* **SCR‑F2‑S04 (Lexical‑only).** No gloss contains behaviour, deontics, measurement math, or type axioms.
* **SCR‑F2‑S05 (No Cross‑context claims).** Nowhere does F.2 assert equivalence/similarity/subsumption across Contexts.
* **SCR‑F2‑S06 (Minimal generality).** Glosses match the Context’s use; no globalisation.
* **SCR‑F2‑S07 (Temporal honesty).** For Contexts with fixed DesignRunTag, units and glosses respect it.

#### F.2:15.2 - Regression (RSCR)

* **RSCR‑F2‑E01 (Edition split).** Introducing a new edition yields new units under a new Context; earlier units persist unchanged.
* **RSCR‑F2‑E02 (Normaliser stability).** Adjusting an LNF does not silently widen/narrow the gloss.
* **RSCR‑F2‑E03 (Language split).** Adding a second language yields a second Context; no bilingual collapse in F.2.
* **RSCR‑F2‑E04 (No stealth bridges).** After updates, F.2 still contains **zero** Cross‑context identity claims; any mapping appears only in F.9.
* **RSCR‑F2‑E05 (Head‑term focus).** Periodic check shows the unit set remains small and oriented to F.3/F.4/F.9 needs.


### F.2:16 - Didactic distillation (60‑second script)

> “In F.2 you **harvest inside Contexts**. For each Context, pick the canon’s own phrasing, choose a **Local Normal Form** in that idiom, add **Tech** and **Plain** labels, and write a one‑sentence **Gloss** that matches how that Context talks. Stop there. No bridging, no behaviour, no equations. If the same string appears in another Context, treat it as a **different unit**. These units feed F.3, where you’ll sort senses **within** a Context, and F.9, where you’ll relate Contexts explicitly. This keeps meaning local, names faithful, and later reasoning clean.”

### F.2:End

## F.3 - Intra‑Context Sense Clustering

**“Within one context, decide what ‘the same sense’ really is—before you ever cross Contexts.”**
**Status.** Architectural pattern.
**Depends on.** F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.4 **Role Description**; F.7 **Concept‑Set Table**; F.8 **Mint or Reuse Decision**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local clustering*; *Sense consolidation*.


### F.3:1 - Intent & applicability

**Intent.** Consolidate the **context‑local lexical units** from F.2 into a **small set of Local‑Senses** that actually operate in that **one context (U.BoundedContext)**. Each Local‑Sense receives a crisp, didactic label pair (Tech/Plain) and a short sense statement. The result is an **addressable basis** for later uses (Role Assignment, tables, bridges) that is **still strictly context‑local**.

**Applicability.** Apply **after** F.2 for any Context that will feed naming (F.4/F.5), decision gates (F.8), Cross‑context bridges (F.9), or exemplars in Part C. Use again whenever the canon (edition) **shifts usage** enough to split or merge senses **within the same context**.

**Non‑goals.** No Cross‑context comparison or merging. No behaviour/deontics/type mathematics. No storage schemas or workflows. This is **pure sense‑making** inside one context.


### F.3:2 - Problem Frame

context‑local units (LNF + labels + gloss) from F.2 often **over‑ or under‑differentiate** meaning:

1. **Over‑split:** superficial variants (*service‑level‑objective* vs *SLO*) treated as different “things”.
2. **Under‑split:** one gloss covering **two selectional frames** or incompatible use‑cases.
3. **Drift within a canon:** multi‑chapter texts use the same head differently unless the reader **consolidates** the intended sense.
4. **Didactic mismatch:** engineer‑friendly label and plain label drift apart when units remain too granular.

F.3 repairs this **inside the Context** by clustering “same sense” and distinguishing “different sense”, with **parsimony**.


### F.3:3 - Forces

| Force                     | Tension to resolve                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs fidelity** | Few Local‑Senses ease teaching; too few dilute real distinctions the canon relies on.                            |
| **Usage vs definition**   | Glosses should reflect **how the canon uses the word**, not an imported dictionary definition.                   |
| **Labels vs idiom**       | Tech label must stay in the canon’s idiom; Plain label must help newcomers—without inventing a new sense.        |
| **Stability vs openness** | Consolidated senses must be stable enough for Role Descriptions and tables, yet revisable when the canon’s use clearly splits. |

### F.3:4 - Core idea (didactic)

**Cluster by usage, not by string.**
Inside one context:

* **Same sense** → **Local‑Sense**: a small, coherent usage‑region the canon treats as one idea (even if it has aliases or minor surface variation).
* **Different sense** → **two Local‑Senses**: incompatible selectional frames, entailments, or role in the canon’s own statements.

Each Local‑Sense becomes **addressable** when paired with its Context: **SenseCell = (Context × Local‑Sense)**. SenseCells are **context‑local coordinates**; they do not pre‑judge any Cross‑context mapping.


### F.3:5 - Minimal vocabulary (this pattern only)

* **Context** — short for `U.BoundedContext` (per D.CTX).
* **Unit** — a context‑local lexical unit from F.2 (LNF + Tech/Plain + gloss).
* **Local‑Sense** — the **conceptual cluster** of Units deemed “same sense” **within that Context**.
* **SenseCell** — the **address** for a Local‑Sense: *(Context, Local‑Sense)*. This is what later patterns will **cite**.
* **Counter‑example** — a short, canonical sentence or use that **must not** be covered by the Local‑Sense; it sharpens the boundary.
* **Usage cue** *(informative)* — a clue from usage (collocational patterns, paraphrases, entailments in the canon) that **suggests** merge or split. Cues **do not decide**; the canon’s intent does.


### F.3:6 - Solution — how to think the clustering (notation‑free)

> What follows are **mental moves**, not steps for a team. Use them as probes until the Context’s usage partitions itself naturally.

**6.1 Consolidate aliases into one Local‑Sense.**
If Units differ only by **orthography, abbreviation, or canon‑blessed synonymy** and are **used interchangeably** in the Context’s own sentences, treat them as **one Local‑Sense**.
*Example (ITIL):* *service‑level‑objective* and *SLO* → one Local‑Sense.

**6.2 Split on incompatible selectional frames.**
If the same head pairs with **different kinds of arguments** or plays **different roles** in the canon’s statements (and those roles cannot both be true at once), split.
*Example (BPMN):* *event* as **node type** vs as **occurrence narrative** in a tutorial → two Local‑Senses; adopt the **node type** sense if that is the normative layer.

**6.3 Split on entailments that pull apart.**
If paraphrases lead to **different entailments** (e.g., one implies temporality, another structural position), you have two senses.
*Example (PROV):* *activity* implies **time‑bounded use/generate**; it cannot be the same sense as a **static capability**.

**6.4 Prefer sense minimality.**
If two candidate Local‑Senses never lead to **different conclusions** in the Context’s own use, merge them. If they sometimes do, split them—and record a **counter‑example** to keep the boundary crisp.

**6.5 Keep Tech label idiomatic; Plain label helpful.**
Tech label stays as the canon speaks; Plain label conveys the **function** of the sense to a careful newcomer. Neither label may **broaden** the sense beyond usage.

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
* **Sense line**: A **node-type** that marks starts, ends, and intermediates; typed by trigger and result.
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
* **SCR‑F3‑S06 (Temporal honesty).** Where the Context has a declared stance, sense lines **respect the DesignRunTag**.

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
3. **Hidden commitments.** We name a role assignment or status assertion but never state what **must hold** when it is assigned; downstream reasoning becomes arbitrary.
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

1. **context‑local grounding.** Every Role Description **MUST** cite exactly one **SenseCell** as its semantic anchor.
2. **I/D/S layer separation.**
   * A **Role Template** **MUST NOT** encode deontic, access, or measurement rules.
   * A **Status Template** **MUST NOT** encode behaviour or control flow.
3. **Time honesty.** The card’s stance (**DesignRunTag**) **MUST** match the Context’s stance (F.1).
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
| **A2**  | **Pan‑Context template**   | One card cites several canons implicitly (“BPMN/PROV process”).           | Imports meaning across Contexts; hides losses.              | Keep **one SenseCell per card**. If Cross‑context relation is needed, apply **F.9 Bridge**.                     |
| **A3**  | **Silent time flip**    | Card defined in a **design** Context asserts run‑time facts (or vice versa). | Violates F.1 time stance; produces category errors.      | Align **Time stance** to the Context; relocate run‑facts to status/evidence lines or to another Context.              |
| **A4**  | **Procedural template** | Long “steps” instead of minimal invariants.                               | Becomes a method recipe, not an assignable mask/badge.   | Replace sequences with **decisive invariants** (2–5 lines) that must hold regardless of procedure.              |
| **A5**  | **Permission leakage**  | A BPMN Role claims access rights “by wearing the mask”.                   | Conflates access with behaviour; misstates RBAC semantics. | State explicitly: **no permissions implied**. Bind access via a **Status** in the RBAC Context.                    |
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
`senseFamily(T₁)=senseFamily(T₂)=Role ∧ stance(T₁)=stance(T₂) ∧ ¬incompatible(T₁,T₂) ⊢ coWearable(T₁,T₂)`
`senseFamily(T₁)=senseFamily(T₂)=Status ∧ ¬incompatible(T₁,T₂) ⊢ stackable(T₁,T₂)`

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
2. **Family correction (Role and Status).** If a card mixes behaviour and deontics, **split** into one Role and one Status; move permission language to the Status.
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
> Cards never mix **Role and Status senseFamilies** and never cross **I/D/S layers**, never flip time stance, and never import other Contexts.
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

**Intent.** Provide a **small, normative code of naming** so that **U.Types** (Cross‑context categories) and **Role Descriptions** (context‑local Roles or Statuses) are labelled **clearly, locally faithful, and globally stable**, without importing tooling, workflows, or editorial process. Names are **consequences of meaning** fixed earlier (F.1–F.4), not badges invented to “stabilise” drifting words.

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

**R‑UT‑1 (Witnessed neutrality).** The Tech label **must not** be a term bound to one context when alternatives exist. Prefer **discipline‑neutral head nouns** (*Result, Reading, Execution, Evidence, Requirement, State, Type Node*). **Use** *Characteristic/Scale/Value/Level/Coordinate/Score/ScoringMethod* **only** when the U.Type denotes a **measurement‑sense** kind anchored in a declared **CharacteristicSpace**; otherwise avoid these measurement‑canon terms to prevent semantics bleed.

**R‑UT‑2 (Minimal generality).** Name the **least upper sense** that all row witnesses share. If *Observation* and *Measurement* disagree, perhaps the U.Type is **Result** or **Reading**, not **Observation**.

**R‑UT‑3 (No senseFamily mixing in names).** Do **not** name a U.Type with deontic or behavioural language (*“PermittedService”*, *“ResponsibleAgent”*). **Role, Status, Method, and Execution** belong to **Role Descriptions (F.4)** or local senses; U.Types are *what‑it‑is* kinds, not *what‑it‑does* or *what‑is‑allowed*.

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
| **A7**  | **Under‑reach / vagueness** | `Item`, `Thing`, `Record` for specific kins                        | No discriminative power; low teaching value                             | Prefer **discipline‑neutral yet informative** heads (`Type Node`, `Result`, `Requirement Status`). (R‑UT‑1, R‑UT‑4) |
| **A8**  | **Symbol as name**          | U.Type named `λ` or `≤`                                            | Unsearchable; Context‑coloured conventions                            | Keep symbols **only as aliases**; Tech label is words. (R‑UT‑8)                                                     |
| **A9**  | **Synonym spray**           | Multiple Tech labels for one U.Type                                | Fragmentation; alias drift                                         | One **Tech** label; further lexical forms live in the **registry** (F.13). (R‑UT‑6, INV‑F5‑1)                       |
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
2. **U.Type (from R₁)** — Tech: **Result** (to carry measured values).
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
| **Design vs run**           | Keep **stance** coherent: design-time bindings are judged by design-time descriptions and their carriers; if you need run-time verification, express it as a **run-Status** or **run-Role** Template without confusing **stances** (A.7). |
| **Fact vs promise**         | Evidence (KD‑CAL) vs deontic expectations (service, policy) must not collapse.       |

### F.6:4 - Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell σ** — **address** **⟨Context C × Local‑Sense ℓ⟩** per F.3. (Informative: we write simply **σ**; it already contains **C**.)
* **Role Description** — a **Role** or **Status** card anchored in a SenseCell (F.4).
* **Holder** — the concrete entity admitted by the Role or Status Template; when the holder is semio-side, name the exact kind, such as system, episteme, publication, or carrier.
* **Subject** — the referent of a **Status** assertion; determined by the Template (may or may not be the Holder).
* **subject_of(τ, H)** — function yielding the **Subject** for Status assertions given Template **τ** (and, if needed, candidate **H**).
* **Eligibility** — conditions on the Holder that *must* hold to apply the Template (F.4 invariants).
* **Window** — the DesignRunTag or interval relevant to the claim (DesignRunTag; instant or period).
* **Evidence shape** — the **Observation/Result/Procedure/Feature** pattern (KD‑CAL) that could confirm/refute the claim in its Context.

### F.6:5 - Pre‑conditions (lightweight)

1. The **Context** is in your F.1 cut; **Context ≡ U.BoundedContext**.
2. The **Template** references a **SenseCell** in that Context (F.4).
3. The **Holder** is identified (by type or instance) without relying on Cross‑context mappings.

### F.6:6 - The six moves (judgement schemas, notation‑free)

Each move is a **thought you can justify**, expressed as `premises ⊢ conclusion`.
All moves are **context-local** and **side-effect free**: they assert knowledge; they do not modify the project entities they describe.

#### F.6:6.1 - M1 - Locate — *Fix the Context and the Template*

**Form.**
`Template τ anchored at SenseCell σ≡⟨C, ℓ⟩ ⊢ address(τ) = σ`

**Reading.** Name the Context and the exact SenseCell that gives **local meaning** to the Template.
**Note.** This forbids “floating” Roles or Statuses and prevents Context drift.

#### F.6:6.2 - M2 - Stance — *Respect DesignRunTag*

**Form.**
`stance(C)=s ∧ stance(τ)∈{s, both} ⊢ compatible_stance(τ,C)`

**Reading.** The Template’s DesignRunTag is **compatible** with its Context’s stance (design vs run).
**Note.** Guards against judging a design-mask by run-traces or judging a run-status by design-time descriptions.

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
| **AP-1**  | **cross-context Binding**      | A single binding/assertion mixes two Contexts (status/role in C₁ justified by semantics in C₂) without an explicit Bridge. | Violates **Locality**; smuggles a Bridge (kind/CL/Loss) into the claim, making it hard to replay and easy to treat as free substitution. | Re-formulate strictly in one context. If cross-context support is essential, apply **F.9 Bridge** and keep the assignment/status claim local. |
| **AP‑2**  | **Role and Status Conflation**     | “Operator” modeled as a deontic grant; “SLO met” modeled as a Role.                         | Collapses **behavioural mask** and **epistemic/deontic state** (A.7).      | Re‑type the Template: **Role** for “can/does”, **Status** for “is/has (as a claim)”. Use **M4** accordingly.                 |
| **AP‑3**  | **Window‑less Claims**         | Binding/assertion with no time stance or interval.                                          | Uncheckable; invites retrospective reinterpretation.                       | Make **Window** explicit (§6 M4). Inherit stance from the Context/Template if fixed; otherwise state it.                        |
| **AP‑4**  | **Eligibility‑after‑the‑fact** | Declaring the claim, then back‑fitting eligibility to observed traces.                      | Confuses **necessary conditions** with **diagnostics**; risks circularity. | Perform **M3 Qualify** *before* **M4 Bind/Assert**; treat evidence only in **M5**/**M6**.                                    |
| **AP‑5**  | **Global Label Illusion**      | Using bare labels (“process”, “agent”, “role”) as if universal.                             | Hides the Context; fuels homonym errors.                                      | Always recover **M1 Locate**: `address(τ)=⟨Context, SenseCell⟩`. Use F.5 naming discipline (Tech/Plain registers).              |
| **AP‑6**  | **Evidence by Prestige**       | “Industry practice says …” offered instead of KD‑CAL‑shaped facts.                          | Replaces observable Results with authority talk.                           | State an **evidence shape Σ(Context)** in **M5**; later fill it with **Observation/Result** facts (KD‑CAL).                     |
| **AP‑7**  | **DesignRunTag Inversion**       | Verifying a design‑time mask by design documents; verifying a run‑status with design specs. | Violates DesignRunTag; yields non‑falsifiable claims.                   | Apply **M2 Stance**: the Template’s stance must be compatible with the Context. Evidence follows the stance.                    |
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
**M3 Qualify.** Holder `PLC_7` qualifies if program `P` is loaded on it and task `T` schedules it.
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
**F.8 Mint or Reuse?** Uses outcomes of **Role or Status** claims to decide: a new **Role or Status** label only when existing Templates cannot express the claim with eligibility/Window adjustments.
**F.9** (Alignment & Bridge): any relation across Contexts is **declared there**; Role Description cards remain context-local.
**F.10 Epistemic Status Mapping.** Consumes **M6** confidences γ and Σ‑adequacy to roll up assurance.

**Coordinates with.** **MM‑CHR** (characteristics, scales) wherever *Characteristic/Scale* is used in evidence shapes.

**Used by.**
Patterns (Part C) to anchor their examples: Sys‑CAL (execution/actuation roles), KD‑CAL (measurement statuses), Method‑CAL (execution claims for Methods/MethodDescription), Kind-CAL (typing claims remain outside Role Assignment & Enactment, but may inform eligibility predicates).

### F.6:12 - Migration notes (conceptual)

1. **Template refactor.** If a Template’s invariants change, **claims remain as‑is**; re‑evaluate **M6** on demand. Do not silently rewrite past claims.
2. **Edition updates.** When a Context’s canon updates, treat it as a **new Context** if sense shifts; Claims anchored to the old Context stay valid for their Window.
3. **Name revisions.** Renaming per F.5 does not alter **address(τ)=⟨Context, SenseCell⟩**; claims reference the address, not lexical form.
4. **Bridge introduction.** Adding an **F.9 Bridge** never upgrades an existing Role or Status claim; at most it enables *separate* translations with declared loss.
5. **From exception to Status.** If recurring exceptions to a Role appear, prefer minting a **Status** Template that marks the exception rather than proliferating Roles.
6. **Window tightening.** If evidence shows drift, narrow future **Windows**; past claims remain tied to their original Windows.

### F.6:13 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.6:13.1 - Static conformance (SCR)

* **SCR-F6-S01 (Local address).** Every assignment/status claim states `address(τ)=σ` where `σ` is a **SenseCell** (per F.3); no bare labels.
* **SCR‑F6‑S02 (SenseFamily clarity).** Each claim is typed **Role** or **Status**, never both; subjects are of the correct kind. Claim records both **senseFamily** and **stance** explicitly or by inheritance.
* **SCR‑F6‑S03 (Stance compatibility).** `stance(Context)` and `stance(τ)` are compatible by `DesignRunTag`.
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

**Reading.** You may **tighten scope** (use the row for a higher-scope purpose) only if the row’s `CL` meets the **higher threshold** for that scope.


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
F.1 **Contexts fixed** → defines the column set; F.2 **Harvest** → supplies harvested terms; F.3 **SenseCells** → provide cell addresses; F.5 **Naming Discipline** → provides the two‑register **FPF labels**; F.9 **Bridges** → justify each row.

**Constrains:**
F.4 **Role Description** — when a template cites an FPF label from the table, it **inherits the Row Scope**; no template may claim semantics beyond the row’s licence.
F.6 **Role Assignment & Enactment Cycle (Six-Step)** — Move M‑4 (“choose label”) must reference a row if it wants Cross‑context reading.

**Used by.**
Part C patterns for didactic alignment pages; Part B trust calculus (B.3) may consume **Row CL(min)** when computing translation penalties.


### F.7:14 - Migration notes (conceptual)

1. **Bridge update.** If any supporting Bridge’s CL changes, recompute **Row CL(min)**. If it drops below the printed value, either **lower Row Scope**, **split** the row, or **retire** it.
2. **New Context appears.** Do **not** auto‑expand rows. Test with **12.5**; add only if it brings a **distinct necessity**.
3. **Sense revision inside a Context.** If a SenseCell splits (F.3), decide which child cell (if any) remains in the row; the rest may require **new rows** or a **contrast**.
4. **Scope promotion.** To use a row for a higher-scope purpose (e.g., from **Naming-only** to **assignment/enactment-eligibility**), first ensure **Row CL(min) ≥ τ(new scope)**; otherwise construct **new Bridges** or **decline** promotion.
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
* **Role Description** — a **Role or Status** template anchored to a **single SenseCell** (F.4).
* **Alias** — an **additional label** for an existing FPF label (within F.5), no new semantics.
* **CL threshold τ(scope)** — the **minimum congruence level** needed for a row’s scope (e.g., τ(Naming-only) < τ(Assignment-eligibility) < τ(Type-structure)).


### F.8:5 - The decision lattice (conceptual, notation‑free)

> Read top‑to‑bottom; the **first satisfied** branch decides. At every step, **state the senseFamily** (Role, Status, Measurement, Type-structure, Method, or Execution) before you proceed.

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
3. **GateCrossing checkability.** Any GateCrossing/CrossingBundle that surfaces policy-ids **MUST** include `PolicyIdRef` (or an equivalent “policy-id + resolvable refs” structure) so GateChecks can verify resolvability and pin consistency (E.18/A.21/G.6:7.5.8).
4. **Authority is policy, not tiers.** “Who may mint” vs “who may reuse” is expressed by the referenced **policy specs** and **mint decisions** (and enforced by the active GateProfile/GateChecks), not by fixed tier labels.


### F.8:9 - Quick reference (one‑glance map)

| You feel you need…                          | Likely action                  | Why                                              |
| ------------------------------------------- | ------------------------------ | ------------------------------------------------ |
| A convenient everyday word across two Contexts | **Reuse a Naming‑only row**    | Keeps prose simple without smuggling inference.  |
| An assignable mask with invariants          | **Role Description (single Context)** | Roles or Statuses attach to **local** senses.       |
| The same measured outcome across Contexts      | **Reuse a KD‑metric row**      | Units/procedures aligned at CL ≥ 2.              |
| A unifying schema relation (e.g., is‑a)     | **Reuse a Type‑structure row** | Structural inference preserved at CL ≥ 3.        |
| A nicer label for the same FPF concept      | **Alias in F.5**               | Style only; zero semantics.                      |
| A brand‑new primitive concept               | **New U.Type (rare)**          | Only if cross‑family, irreducible, kernel‑level. |

### F.8:10 - Anti‑patterns & remedies

| #         | Anti‑pattern               | Symptom                                                                            | Why it harms thinking                              | Remedy (conceptual move)                                                                                                                         |
| --------- | -------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AP‑1**  | **Row‑less sameness**      | Declaring “these mean the same” across Contexts without citing a **Concept‑Set row**. | Imports meaning implicitly; no CL guard.           | If Cross‑context reuse is desired, **reuse an existing row** at a declared **scope** (F.7), else **publish the contrast** and apply F.9 Bridges only when the bridge relation is live. |
| **AP-2**  | **Scope creep**            | Using a **Naming-only** row to justify **Assignment-eligibility** or structural inferences. | Over-claims sameness; breaks τ(scope).             | Respect **scope thresholds** (τ). Upgrade only when **Row CL(min) ≥ τ(new scope)**; otherwise stay Naming-only.                                  |
| **AP‑3**  | **Alias with payload**     | Introducing an Alias that subtly changes intent or senseFamily.                          | Hides semantics behind wording; confuses senseFamilies.   | Aliases (F.5) are **style only**. If semantics change, choose **row reuse** or **Role Description** instead.                                         |
| **AP-4**  | **Role-Description-to-row anchoring** | Role Description points to a **row** rather than a **single SenseCell**.       | Masks locality; **assignments** become cross-context by stealth. | Role Descriptions **must anchor to one SenseCell** (F.4). Use rows only in prose or aggregated views.                                                |
| **AP‑5**  | **Kernel inflation**       | Proposing a new **U.Type** because a convenient label is missing.                  | Duplicates the kernel; violates parsimony.         | Apply A.8: require **≥ 3 domain families** and **irreducibility**; otherwise **Alias** or **row**.                                               |
| **AP‑6**  | **senseFamily mixing**           | One name that conflates Role, Status, Measurement, or Type‑structure.              | Collapses A.7 Strict Distinction.                  | **Split by senseFamily** first (Q0). Decide **per senseFamily**.                                                                                             |
| **AP‑7**  | **Bridge‑by‑string**       | Treating identical lexical forms as equivalent senses across Contexts.                | Homonym trap; ignores local sense.                 | Equivalence only via **F.9 Bridge** + **row**; never by string.                                                                                  |
| **AP‑8**  | **Row without loss notes** | Publishing a row where Bridges indicate mismatches, but row text is silent.        | Readers assume full equivalence.                   | Include **counter‑example** and **loss sketch** in the row’s narrative (F.7).                                                                    |
| **AP‑9**  | **CL laundering**          | Citing a high-scope row based on old high `CL` while the relevant Bridge `CL` has since dropped.    | Invalidates downstream claims.                     | When `CL` falls below `τ(scope)`, **downgrade row scope** (e.g., to Naming-only) or **split row**.                                                   |
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
2. **Overclaiming rows.** If a row was used for **assignment/enactment-eligibility** or **Type-structure** but **CL drops**, **downgrade row scope** to **Naming-only** in prose; adjust examples.
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
**Type.** Architectural pattern.
**Status.** Stable.
**Normativity.** Normative.
**Builds on:** E.10.D1 (Context discipline: Context = U.BoundedContext); **F.0.1 (senseFamily & StatusModality guard; Bridge-only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds and reuse choice).

**Coordinates with:** B.3 **Trust & Assurance Calculus** (uses CL penalties); **A.6.1 U.Mechanism** (Transport clause for cross-context use; penalties feed **R/R_eff** only; **F/G** invariant); Part C patterns (apply Bridges in formal claims); A.6.9 (RPR-XCTX for repairing umbrella “same/equivalent/align/map” prose into explicit Bridge Cards).
**Aliases (informative).** *Context-to-Context translator*; *Sense bridge*.

### F.9:1 - Intent & applicability

**Intent.** Provide a **conceptual discipline** for relating **SenseCells** from **different Contexts (U.BoundedContext)**. A **Bridge** states *what kind* of relationship holds, *how far* it holds (via **CL: Congruence Level**), and *what is lost* during the translation. Bridges **support carefully scoped reuse** (e.g., a Concept-Set row) while **rejecting silent equivalence**.

**Applicability.** Use **whenever** an author needs to **read across Contexts**—to reuse a familiar label, to connect design-time and run-time notions, to compare two standards’ terms, or to justify a row in the Concept-Set table. This pattern is **not** storage, enactment protocol, or governance; it codifies **thinking moves**.

**Non-goals.** No global meaning; no `PublicationSurface` semantics; no editor roles. Bridges are **semantic relations between local senses**, not transport chains, not processes.
**Governed object in plain terms.** One bridge card relating two `SenseCells` across different `U.BoundedContext`s; not a transport chain, not a workflow, and not one global meaning layer.
**Governing move in plain terms.** Declare relation kind, direction, `CL`, and loss between local senses so cross-context reading stays inspectable without collapsing them into silent equivalence.
**Primary working reader.** The primary working reader is an author, checker, or practitioner preparing one bridge card, one comparative mapping note, or one concept-set row that depends on cross-context reading without pretending the contexts have already collapsed.
**Use this when.** Use this pattern when two local senses from different contexts need one explicit bridge card before a team can admissibly reuse a label, justify a row, or compare the cases without pretending the senses are equivalent or substitutable.
**Start here when.** The same term, role, quality, or status label appears in more than one context and the team is about to treat that overlap as if it were already equivalence, safe substitution, or structure-preserving reuse.
**What goes wrong if missed.** Teams fall back to shared labels, string-equals shortcuts, or informal analogies, then quietly smuggle equivalence, substitution, or structure across contexts without publishing relation kind, `CL`, or loss.
**What this buys.** One explicit bridge discipline that lets a team reuse names, compare contexts, and publish bounded cross-context support without losing track of direction, loss, and the limits of admissible substitution.
**Not this pattern when.** Not this pattern when the case is still only a coarsened source-pinned rendering with no bridge claim yet, or when the real job is storage, enactment, governance, or one single local context rather than explicit cross-context alignment.

**Boundary to controlled coarsening.** This pattern is also the explicit boundary pattern when a simplified or coarsened cross-context rendering starts to imply equivalence, substitution, projection, or interoperability scope. If the case is still only a coarsened source-pinned rendering for narrower use, keep it with that rendering's own source tether, non-admissible-use line, and reopen condition, using `A.6.3.CSC Controlled Semantic Coarsening` when that narrower-use card is primary. A lighter cross-context note may support informal orientation talk, but that is not a formal `F.9` `Naming-only` row. Any bridge, substitution, row, or interoperability claim must reopen the source-bearing episteme or source publication needed for bridge support before a Bridge Card may be published under `F.9`.
**Recognition vs assurance note.** Read **Intent**, **Applicability**, **Non-goals**, and the `A.6.3.CSC` neighbor boundary above as the ordinary recognition block. Read Bridge kinds, `CL`, conformance, and Relations below as assurance blocks that tighten the same bridge-card claim; they do not widen the pattern into transport, workflow, or one global meaning layer.

### F.9:2 - Problem frame

Cross-context work fails in predictable ways:

1. **String-equals fallacy.** Identical spellings (“process”, “role”, “accuracy”) taken as identical meaning.
2. **Scope creep.** A naming convenience is stretched to assignment or structural claims.
3. **DesignRunTag jumping.** Design artefacts are substituted for run-time occurrences (or vice-versa).
4. **Direction amnesia.** Narrower/broader relations treated as symmetric.
5. **Loss blindness.** Differences (units, granularity, preconditions) are left unstated, contaminating downstream reasoning.

Bridges cure these by **making relation, direction, loss, and `CL` explicit**.


### F.9:3 - Forces

| Force                           | Tension to resolve                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| **Locality vs reuse**           | Senses are context-local, yet people need a common label to talk across Contexts.              |
| **Simplicity vs fidelity**      | Few Bridge kinds are teachable; too few will hide real mismatches.                       |
| **Safety vs utility**           | Support bounded substitution when the bridge kind and `CL` license it; leave substitution unsupported when loss is unbounded. |
| **senseFamily purity vs explanation** | Substitution must preserve **senseFamily**; explanation may span **senseFamilies** without implying sameness. |


### F.9:4 - Core idea (didactic)

**A Bridge is a declared translator between two local senses.**
It always names **(a)** the two **SenseCells**, **(b)** a **Bridge kind** (what relation), **(c)** a **direction** (if non-symmetric), **(d)** a **CL** value, and **(e)** **Loss Notes** (what fails to carry). Some Bridges **support substitution** in limited scopes; others **support only explanation**.


### F.9:5 - Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell** - the pair *(Context, Local-Sense)* from F.3.
* **Bridge** — a conceptual relation between two SenseCells with kind, direction, CL, and loss notes.
* **CL (Congruence Level)** — ordinal congruence class (0…3) of a Bridge (see §7).
* **Scope** — the **Bridge-supported use** of a cross-context reading (as in F.7/F.8):

* **Naming-only** (talk consistently),
* **Role Assignment & Enactment-eligibility** (assignable constraints/roles/status reuse),
* **Type-structure** (safe structural inference).
* **senseFamily** — the semantic category (Role, Status, Measurement, Type-structure, Method, Execution…) per F.0.1 (normative Part F guard).


### F.9:6 - Bridge kinds (senseFamily-aware)

> **Two families** of Bridges: **Substitution Bridges** (senseFamily-preserving; can support Concept-Set rows) and **Interpretation Bridges** (explanatory; **not** for substitution).

#### F.9:6.1 - Substitution Bridges (sense-preserving)

These relate **SenseCells of the same senseFamily** and may support **limited substitution**:

1. **Equivalence** - *near-identity of sense*. Symmetric. Rare.
   *Use:* May support **Type-structure** rows when CL=3 and invariants match.
   *Loss Notes:* usually “none” or “profiling differences”.

2. **Narrower-than / Broader-than** - *proper inclusion of sense*. Directional.
  *Use:* Safe to substitute **narrower > broader** in **Naming-only** and sometimes **Role Assignment & Enactment**; **broader > narrower** is unsafe.
   *Loss Notes:* “loses special cases X”.

3. **Partial-overlap** - *non-empty intersection, neither includes the other*.
  *Use:* **Naming-only** at best. **Never** justifies Role Assignment & Enactment / Type-structure.
   *Loss Notes:* “A-only senseFamily”, “B-only senseFamily”.

4. **Disjoint** - *explicit contrast*.
   *Use:* For **didactic warnings**; not reuse support.
   *Loss Notes:* n/a (it asserts incompatibility).

#### F.9:6.2 - Interpretation Bridges (cross-senseFamily, explanatory)

These **do not support substitution** but **explain connections** across senseFamilies:

5. **Design-spec -> Run-trace** - a design concept relates to its run-time occurrence.
   *Example:* *BPMN\:Process* -> *PROV\:Activity*.
   *Use:* Explain design-to-execution correspondence. No Concept-Set rows.
   *Loss Notes:* “graph vs event”, “control-flow vs temporal extent”.

6. **Measure-of / Evidence-for (->)** — a measurement SenseCell evidences or quantifies another **senseFamily** (e.g., a Requirement clause).
   *Example:* *SOSA\:Observation* -> *ITIL\:SLO fulfilment*.
   *Use:* Explain evaluation. No substitution.

7. **Policy-implies / Obliges (->)** — a deontic statement constrains another **senseFamily**.
   *Example:* *ODRL\:Duty* -> *Service behaviour*.
   *Use:* Explain constraint propagation.

> **Rule of thumb.** If you want **rows** or **substitution**, you need a **Substitution Bridge** on the **same senseFamily**. If you want to **explain** why artefacts relate without claiming sameness, use **Interpretation Bridges**.


### F.9:7 - CL scale and scope thresholds

CL expresses how safely meaning carries over.

| CL    | Name              | Intuition                                            | Typical loss             | Row scope supported (thresholds) |
| ----- | ----------------- | ---------------------------------------------------- | -------------------- | -------------------------------- |
| **0** | **Opposed**       | Intentionally contrastive or disjoint                | n/a                  | none                             |
| **1** | **Comparable**    | Talk under a shared label; senses differ materially  | material sense divergence | **Naming-only** (`CL >= 1`) |
| **2** | **Translatable**  | Bounded loss; consistent examples & counter-examples | small, stated losses     | **Role Assignment & Enactment-eligibility** (`CL >= 2`) |
| **3** | **Near-identity** | Invariants match; no material counter-example        | profile-level only       | **Type-structure** (`CL = 3`) |

* **Thresholds (normative):**

  * Publishing a **Naming-only** row requires **CL >= 1** across the row's Cells.
  * Publishing a **Role Assignment & Enactment-eligible** row requires **CL >= 2**, the **same senseFamily**, and compatible stance.
  * Publishing a **Type-structure** row requires **CL = 3** **and** matched invariants (acyclicity, anti-symmetry, units, etc.).

* **Penalty use (informative):** B.3 may convert **CL** into an assurance penalty when a cross-context claim is made.


### F.9:8 - The Bridge Card (compact sketch)

> A **thought-format** (not a form). Every bullet can be said in a sentence.

* **Cells.** `A@contextA` - `B@contextB`.
* **senseFamily.** *Role, Status, Measurement, Type-structure, Method, or Execution ...*
* **Kind.** *Equivalence / Narrower-than / Broader-than / Partial-overlap / Disjoint / Design-spec -> Run-trace / Measure-of / Policy-implies*.
* **Direction.** *A -> B* (if non-symmetric) or *A <-> B*.
* **CL.** *0–3* with a short **why**.
* **Loss Notes (bullets).** What fails to carry (units, scope, granularity, preconditions, time stance).
* **Counter-example.** The crispest case where substitution would mislead.
* **Supported use.** *Naming-only / Role Assignment & Enactment-eligible / Type-structure / Explanation-only*.
* **Didactic hook.** The helpful sentence a careful engineer can remember.

*If it does not fit on a screen, you are describing the Contexts, not the Bridge.*

**Registry-reference note (normative).** `BridgeId` and any policy/edition identifiers cited by a Bridge Card are **registry references** (keys into registries), not semantic symbols exported by signatures. Therefore they MUST NOT be demanded via `SignatureManifest.provides` (or "satisfied" via `imports` closure); conformance is checked by validating that the referenced registry entries exist and, where required, are edition-pinned (see F.15).


### F.9:8a - State export and quantum-like boundary note

Use F.9 first when meaning, label, relation, field, record, model output, report, or representation crosses a bounded context or publication plane. A bridge does not become quantum-like because it is lossy, approximate, contextual, or hard to translate. It becomes quantum-like only when the bridge/export claim still depends on order sensitivity, incompatible frames, a probe that changes the represented state, or no faithful-enough export supports the intended use.

Action path:

1. Build the ordinary Bridge Card first: cells, sense family, kind, direction, CL, loss notes, counter-example, and Bridge-supported use.
2. Ask what state, relation, evidence, metric, option, or viability reading is claimed to survive the crossing.
3. State what the crossing omits, coarsens, re-keys, reframes, makes incomparable, or makes unsafe for the intended downstream use.
4. If the bridge or export claims to preserve action, intervention, manipulation, explanation, or cross-scale structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the coarsened bridge as a QL issue.
5. Ask whether asking, measuring, exporting, rendering, or bridging changes the represented state itself. If yes, coordinate with `C.26.1`.
6. Ask whether coordinated work or live state is not exported faithfully enough for the intended use by any one report or bridge. If yes, coordinate with `C.26.2`.
7. Ask whether the crossing is a state representation with declared source-loss mode or reduced recoverability. If yes, coordinate with CSC/RT and the C.26 coarsening support section.
8. State Bridge-supported use and return-to-source trigger before the bridge result is reused.

Add this row to the Bridge Card only when the bridge result will be reused for decision, comparison, assurance, release, audit, or cross-context action. For a local orientation note, state the export loss and return-to-source trigger in prose without treating the note as a Bridge Card extension.


| Field | Question |
| --- | --- |
| State reading claimed to survive | What state, relation, evidence, metric, option, or viability reading is claimed to survive the crossing |
| State lost or transformed | What is omitted, coarsened, re-keyed, re-framed, made incomparable, or no longer decision-safe |
| Probe / frame condition | Whether the act of asking, measuring, exporting, or rendering changes the represented state |
| Bridge-supported use | Which decision, explanation, triage, comparison, or orientation use remains supported after the crossing |
| Bridge-non-admissible use | Which substitution, release, audit, assurance, or action use requiring additional support is not supported by the Bridge card |
| Return-to-source trigger | When the bridge result is no longer enough and the source context, evidence carrier, or fuller representation must be reopened |

Useful outputs:

- an ordinary Bridge Card when translation/loss is the whole issue;
- a C.26.1 note when the export/probe changes represented state;
- a C.26.2 note when coordinated state has no faithful-enough export for the intended use;
- a CSC, RT, or C.26 coarsening handoff when the exported representation intentionally carries reduced detail, reduced recoverability, or narrower use.

### F.9:9 - Invariants (normative)


1. **Locality first.** A Bridge relates **SenseCells**, never Contexts or strings.
2. **senseFamily discipline.** **Substitution Bridges must be senseFamily-preserving**. **Interpretation Bridges** may cross senseFamilies but **never** support substitution.
3. **Direction clarity.** If the kind is directional, state direction explicitly.
4. **CL honesty.** Assign **CL** only if you can state at least one **counter-example** for `CL <= 2` or explain its absence with invariants for `CL = 3`.
5. **Loss visibility.** Every Bridge carries **Loss Notes** (even “none”).
6. **Row dependence.** A Concept-Set row’s **scope** is **bounded by the weakest CL** among its participating Bridges (F.7/F.8).
7. **No senseFamily jump by stealth.** You **must not** use an Interpretation Bridge to justify a **row** or **substitution**.
8. **Time DesignRunTag honesty.** If a Context fixes **DesignRunTag**, the Bridge must respect that distinction or explicitly declare a bridge such as `Design-spec -> Run-trace`.
9. **Kernel restraint.** Bridges **cannot** be used to promote ad-hoc sameness into a new **U.Type**; A.11 applies.
10. **Non-inheritance of Contexts.** Bridges **do not** imply -is-a- between Contexts (E.10.D1).
11. **Coarsened-note restraint.** A lighter cross-context note, comparative aid, redacted view, or surrogate **SHALL NOT** be treated as a Bridge Card or as bridge or substitution support by convenience. If bridge-bearing use is still wanted, the source-bearing episteme or source publication needed for bridge support must be reopened and the bridge must be declared explicitly with kind, direction, `CL`, and loss notes.


### F.9:10 - Micro-examples (illustrative, one-liners)

1. **Participant vs Agent (process model vs provenance)**
   *Cells:* `BPMN:Participant` - `PROV:Agent` - *senseFamily:* Role - *Kind:* `Partial-overlap` - *CL:* 2 - *Loss:* participation vs attribution scopes differ - *Use:* **Naming-only** ("actor").

2. **Process (design) vs Activity (run)**
   *Cells:* `BPMN:Process` -> `PROV:Activity` - *senseFamily:* Method / Execution - *Kind:* **Design-spec -> Run-trace** - *CL:* 2 - *Loss:* graph vs event; concurrency vs temporalization - *Use:* **Explanation-only**.

3. **Observation vs SLO check**
   *Cells:* `SOSA:Observation` -> `ITIL:SLO-fulfilment` - *senseFamily:* Measurement / Status - *Kind:* `Measure-of` - *CL:* 2 - *Loss:* sampling window; target definition - *Use:* **Explanation-only**.

4. **Subtype across OWL and curated taxonomy**
   *Cells:* `OWL:SubClassOf` - `TaxonomyX:is-a` - *senseFamily:* Type-structure - *Kind:* `Equivalence` - *CL:* 3 *(only if TaxonomyX is acyclic and anti-symmetric)* - *Loss:* profile differences - *Use:* **Type-structure** rows supported.

5. **Accuracy (metrology vs data-quality)**
   *Cells:* `ISO80000:accuracy` - `ISO25024:accuracy` - *senseFamily:* Measurement - *Kind:* `Partial-overlap` - *CL:* 2 - *Loss:* instrument vs dataset perspective - *Use:* **Naming-only** row -accuracy-; methods stay context-local.

### F.9:11 - Anti-patterns & remedies

| ID    | Anti-pattern | Symptom | Why it breaks thinking | Remedy (conceptual move) |
| --------- | -------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AP-1** | **String-equals = sense-equals** | Same spelling used across Contexts with silent identity claims. | Violates locality; invites false substitution. | Always state a **Bridge kind**; if unsure, default to **Partial-overlap** with **Naming-only** scope. |
| **AP-2**  | **Stealth substitution**         | “We’ll just treat A like B for now.”                                              | Hidden policy with unknown loss; leaks into Role Assignment & Enactment.    | Publish a **Bridge Card** with **Loss Notes** and **CL**; if CL<2, substitution remains **unsupported**.      |
| **AP-3** | **Stance jump by wording** | -Activity (PROV) is a Process (BPMN).- | DesignRunTag confusion; swaps graphs for events. | Use a **Design-spec -> Run-trace** Interpretation Bridge, not a substitution bridge; keep **Explanation-only** scope. |
| **AP-4** | **Symmetry hallucination** | Treating directional bridges as if they were symmetric. | Narrows broadened, broadens narrowed; unsafe reuse. | Record **direction** explicitly; only **Equivalence** is symmetric. |
| **AP-5** | **Disjoint but reused** | Declare `Disjoint` and still borrow labels or Role Description constraints (RCS/RSG). | Contradiction between declaration and use. | Either retract `Disjoint` or stop reuse; if a thin thread exists, rename it as **contrastive explanation** (no row). |
| **AP-6** | **CL without counter-example** | -These are CL=3- with no invariant check. | Inflates trust; over-supports structural rows. | For **CL=3**, cite the **matching invariants**; otherwise, demote to **CL=2** and add a counter-example. |
| **AP-7** | **Bridge inflation** | Dozens of nearly identical Bridges between the same Contexts. | Noise masks the few material alignments. | Prefer **one Bridge per pair of Cells per senseFamily**; fold variants into **Loss Notes**. |
| **AP-8** | **Row outruns Bridge** | A Concept-Set row claims Role Assignment & Enactment-eligibility where some participating Bridges are `CL = 1`. | Row scope exceeds the weakest link. | Apply the **weakest-link rule** (F.7/F.8): row scope <= `min(CL)`; otherwise split the row. |
| **AP-9** | **Bridge as new U.Type** | Using a Bridge to justify minting a new universal Type. | Re-globalises meaning; breaks A.11 parsimony. | Keep Types context-local; where reuse is needed, use **rows** + Bridges, not new primitives. |
| **AP-10** | **Silent unit-and-scale mismatch** | Transporting measurements without unit and scale notes. | Hidden dimensional error. | Record units and scales in **Loss Notes**; if units cannot be related, use **Disjoint** or **Partial-overlap** with **Naming-only** scope. |
| **AP-11** | **Coarsened note treated as bridge support** | A summary, redacted comparison, or partner-facing simplification is used as if it already supported substitution or interoperability claims. | A bridge claim is being smuggled through a coarsened rendering that only made lighter review or orientation admissible. | Reopen the source-bearing episteme or source publication needed for bridge support and publish the actual Bridge Card before any bridge-bearing or substitution use. |


### F.9:12 - Worked examples (didactic)

#### F.9:12.1 - Service acceptance (design) vs executions & observations (run)

* **Cells & Contexts**
  `ITIL4:SLO` *(Status, design)* <- `SOSA:Observation(availability)` *(Measurement, run)*
  `BPMN:Process` *(Method, design)* -> `IEC61131:Task-Execution` *(Execution, run)*
* **Narrative**
  Availability SLOs are **evaluated** by observations of task executions. No substitution follows: an SLO is not an observation, and a process is not an execution occurrence.
* **Bridge Cards (sketch)**
  *ITIL\:SLO <- SOSA\:Observation* - **CL=2** - Loss: sampling window, clock skew.
  *BPMN\:Process -> IEC\:Execution* - **CL=2** - Loss: control-flow vs temporalization, concurrency collapse.
* **Supported use**
  Explanation-only; Concept-Set rows may be **Naming-only** ("availability") with **CL >= 1** label coherence across Contexts.


#### F.9:12.2 - Behavioural role vs access role

* **Cells & Contexts**
  `BPMN:Participant` *(Role)* - `NIST-RBAC:Role` *(Status)*
* **Narrative**
  Both talk about -who acts-, but one is a **behavioural mask** in a process model, while the other is an **authorization grouping**.
* **Bridge**
  **Kind:** `Partial-overlap`, **CL=2**; Loss: assignment moment, enforcement placement, multiplicity.
* **Supported use**
* **Naming-only** row “actor”; **no Role Assignment & Enactment reuse** across senseFamilies.


#### F.9:12.3 - Equivalence of subtype notions for structural rows

* **Cells & Contexts**
  `OWL2:SubClassOf` *(Type-structure)* - `TaxX:is-a` *(Type-structure curated)*
* **Bridge**
  **Kind:** `Equivalence`, **CL=3** **iff** the curated taxonomy is **acyclic and anti-symmetric** and uses class-level reasoning.
* **Supported use**
  **Type-structure** rows supported (`CL = 3`); Loss: OWL profile limitations (RL/EL/QO).


#### F.9:12.4 - Accuracy (metrology) vs accuracy (data-quality)

* **Cells & Contexts**
  `ISO80000:measurement-accuracy` *(Measurement)* - `ISO25024:data-accuracy` *(Measurement)*
* **Bridge**
  **Kind:** overlap, **CL=2**; Loss: “true value” notion differs (instrument vs dataset), scale transformations.
* **Supported use**
  **Naming-only** row “accuracy” used for reports; no shared methods.


#### F.9:12.5 - Setpoint (control) vs target (service)

* **Cells & Contexts**
  `CTRL:text:setpoint` *(Status/Control)* - `ITIL:target` *(Status/Service)*
* **Bridge**
  **Kind:** `Disjoint` - Rationale: physical reference value vs business objective; different target kinds (control parameters vs requirement clause).
* **Supported use**
  Didactic contrast only; prevents accidental substitution in SLO calculus.

#### F.9:12.6 - Role substitution & CL gating (RoleAssignment/enactment scope)

> **Use.** A worked, role-focused restatement of Bridge usage for the recurring question:
> “May `Role_B@B` satisfy `Role_A@A` for `requiredRoles` / enactment checks-”

**Rule.** **No cross-context substitution by name.** If a step in **Context A** needs `Role_A`, and the performer only holds `Role_B` in **Context B**, an explicit **Bridge** **MUST** state how `Role_B@B` relates to `Role_A@A`, with direction, **CL**, and Loss Notes.

##### F.9:12.6.1 - Directional substitution (role-oriented shorthand)

A Bridge may assert, *directionally*:

* **`substitutesFor(Role_B@B > Role_A@A)`** with a CL and a list of **kept** and **lost** characteristics (for roles: typical losses are RCS characteristics and/or RSG nuances).
* The reverse direction **does not** follow unless declared (F.9:13.7).

##### F.9:12.6.2 - CL > gating policy (didactic default)

| **CL** | Meaning (intuitive)                     | **Supported scope** | **Extra condition**                                                                  | **Unsupported by default** |
| :----: | --------------------------------------- | :--------: | ------------------------------------------------------------------------------------ | :-------: |
|  **3** | Near-isomorphic sense; no material loss | Yes | None beyond ordinary gates (e.g., window + RSG state) | - |
|  **2** | Close but with stated losses            |    Yes     | Require **extra evidence** (e.g., additional checklist item) **or** a named checker |     —     |
|  **1** | Distant analogy; risky                  | Exception  | Only by explicit **Waiver SpeechAct** naming the Bridge + loss rationale             |  Default  |
|  **0** | Incompatible                            |     No     | —                                                                                    |    Yes    |

*Notes.* The **substitution scope** is defined in **F.9:13.2-13.3** (Role-Assignment/Enactment-eligible substitution requires **CL >= 2**; Naming-only is **CL >= 1**).
CL penalties feed assurance (R) per **B.3**; safety-critical policies may require **CL >= 2** by default (D.2).

##### F.9:12.6.3 - Typical bridges (worked patterns)

* **BPMN Task - PROV Activity.**
  `substitutesFor(Task@BPMN > Activity@PROV)` with **CL=2**; **lost:** BPMN control-flow guards; **kept:** “bounded occurrence consuming/producing entities.”
  *Effect.* A Work logged as `Activity@PROV` may satisfy a step requiring a `Task@BPMN` **iff** an extra guard enforces the BPMN pre-/post-conditions.

* **Essence Alpha-State - RoleStateGraph state.**
  `substitutesFor(“Alpha.State:Ready”@Essence > “Ready”@RSG)` with **CL=2**; **lost:** Alpha-specific narrative criteria; **kept:** checklist-based readiness.
  *Effect.* A team may reuse Essence states as labels in RSG, but still maintains local checklists as **StateAssertions**.

* **ITIL Service Owner - RBAC Administrator.**
  Typically **CL=1** and **directional** (Administrator\@RBAC > ServiceOwner\@ITIL) **rejected** unless a policy Bridge enumerates compensating controls.
  *Effect.* Prevents “ops admin = service-accountability role” conflations without an explicit waiver.

##### F.9:12.6.4 - Bridge invariants (role-relevant reminders)

* **Local first.** Substitution never overrides in-Context role algebra (its own role relations, guards, and exclusions).
* **Loss honesty.** If a Bridge’s loss notes indicate that a dropped characteristic is required by a step, substitution is invalid (regardless of CL).
* **No silent inversion.** Direction is explicit; substitution does not reverse unless declared (F.9:13.7).

### F.9:13 - Reasoning primitives (judgement schemas)

> **All judgements are conceptual.** They support or reject specific *thinking moves*-not enactment steps and not process-enactment records.

#### F.9:13.1 - Bridge declaration

`Bridge(A@RA, B@RB) : senseFamily, kind, dir, CL, Loss, scope`

*Reading:* There exists a declared Bridge between SenseCells `A` and `B` with stated attributes.


#### F.9:13.2 - Substitution scope (senseFamily-preserving)

`Bridge(A,B): same senseFamily f, kind in {Equivalence, Narrower-than, Broader-than}, dir A->B, CL>=2, Loss L -> A may stand in for B at senseFamily f (Role-Assignment/Enactment-eligible)`

*Reading:* A **Substitution Bridge** on the same senseFamily with **CL >= 2** supports **Role-Assignment/Enactment-level** substitution **in the stated direction**. (`Type-structure` requires **CL = 3**.)


#### F.9:13.3 - Naming-only scope

`Bridge(A,B): kind in {Equivalence, Narrower-than, Broader-than, Partial-overlap}, CL>=1 -> A and B may share a label (Naming-only)`

*Reading:* A Bridge with **CL >= 1** supports using a shared label in prose or Concept-Set **Naming-only** rows, without structural or Role Assignment & Enactment commitments.


#### F.9:13.4 - Prohibition by kind

`Bridge(A,B): kind=Disjoint -> no substitution and no shared row`

*Reading:* **Disjoint** supports neither substitution nor rows; only contrastive teaching remains supported.


#### F.9:13.5 - Interpretation embargo

`Bridge(A,B): kind in {Design-spec -> Run-trace, Measure-of, Policy-implies} -> Explanation-only`

*Reading:* **Interpretation Bridges** never support substitution or rows.


#### F.9:13.6 - Weakest-link rule for rows

`row R uses {Bridge_i} -> scope(R) = min_i(scopeSupported(Bridge_i)) and CL(R) = min_i(CL_i)`

*Reading:* The **row scope** and **row CL** are bounded by the weakest participating Bridge.


#### F.9:13.7 - Direction guard

`Bridge kind=Narrower-than with dir A->B -> not(B may stand in for A)`

*Reading:* Narrower>Broader does **not** invert; only A may substitute into B under the stated scope.


#### F.9:13.8 - SenseFamily purity

`Bridge scope=Role Assignment & Enactment-eligible -> same senseFamily(A,B) and same stance(A,B)`

*Reading:* Role Assignment & Enactment-level substitution requires **same senseFamily** and same stance (run-time or design time).


#### F.9:13.9 - Loss accumulation

`A->B with Loss L1 and B->C with Loss L2 -> A->C is supported only if the same senseFamily is preserved, CL=min(CL1,CL2), and Loss accumulates as L1 union L2`

*Reading:* Chained substitution is rarer; if used, **accumulate Loss** and respect the **minimum CL**. When in doubt, avoid chaining across Contexts.


### F.9:14 - Relations

**Builds on:** E.10.D1 (Context discipline: Context = U.BoundedContext); **F.0.1 (senseFamily guard; Bridge-only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds and reuse choice).

**Coordinates with:** `F.9.1` for stance overlays that remain subordinate to bridge cards; `E.17.1` when viewpoint bundles need explicit cross-family correspondence; `A.6.Q` / `C.25` when evaluative endpoints or bundle-shaped quality families cite bridge cards without absorbing bridge semantics.

**Constrains:**

* **F.7 Concept-Set Table:** each cross-context row must name supporting **Bridges**; row scope <= the weakest supporting Bridge.
* **F.8 Mint or Reuse:** reuse choices reference **CL** and **kind**; no reuse without a Bridge.
* **Part C patterns:** formal claims that span Contexts cite Bridges and respect senseFamily/StatusModality & CL constraints.
* **B.3 Trust & Assurance Calculus:** may interpret **CL** as a penalty factor in Cross-context reasoning.


### F.9:15 - Migration notes (conceptual)

1. **Edition shift in a Context.** Re-read affected **Cells**; if sense moved, split the Bridge or **lower CL**; keep the older Bridge for historical claims.
2. **New evidence of mismatch.** Add a **counter-example**; decrease `CL` or change bridge kind (for example from `Equivalence` to `Partial-overlap` or `Disjoint`).
3. **Convergence over time.** When invariants demonstrably match, and counter-examples evaporate, **raise CL** cautiously; for **CL=3**, cite invariants.
4. **senseFamily refactor.** If a Cell’s senseFamily was mis-typed, fix the senseFamily first in F.3, then revisit Bridges; **Interpretation** is safer than forced substitution.
5. **Row under-protected.** If a row’s scope exceeds the weakest Bridge, either **split the row** by Context or **downgrade scope** to Naming-only.
6. **Bridge sprawl.** Consolidate near-duplicates into one Bridge with richer **Loss Notes**; retire the rest.


### F.9:16 - Acceptance tests (SCR/RSCR — concept-level)

#### F.9:16.1 - Static conformance (SCR)

* **SCR-F9-S01 (Well-typed).** Every Bridge names **two SenseCells**, each bound to a **Context** from F.1, and states **senseFamily**, **kind**, **dir** (if needed), **CL**, **Loss**, and **scope**.
* **SCR-F9-S02 (senseFamily discipline).** Any Bridge that supports **Role/Enactment-eligible** substitution is **senseFamily-preserving** and has kind in {`Equivalence`, `Narrower-than`, `Broader-than`}.
* **SCR-F9-S03 (Loss visibility).** Every Bridge has **non-empty Loss Notes** (the word "none" is valid only with **CL=3** and stated invariants).
* **SCR-F9-S04 (Counter-example hygiene).** Bridges with **CL <= 2** carry at least one **counter-example**; Bridges with **CL=3** cite **matching invariants**.
* **SCR-F9-S05 (Row compliance).** Every Concept-Set row shows a **scope** no greater than the **minimum CL** across its supporting Bridges; no row relies on **Interpretation** Bridges.

#### F.9:16.2 - Regression (RSCR)

* **RSCR-F9-E01 (Edition churn).** When a Context's edition changes, re-validate all Bridges touching it; flag `CL` drift and update rows' scopes if needed.
* **RSCR-F9-E02 (Counter-example drift).** New counter-examples lower **CL**; deletions do not automatically raise **CL**.
* **RSCR-F9-E03 (senseFamily drift).** If a Cell's `senseFamily` is corrected, all Bridges crossing that Cell are re-typed; any substitution that would now cross senseFamilies is invalidated.
* **RSCR-F9-E04 (Weakest-link enforcement).** Adding a low-CL Bridge to a row reduces the row's scope; if the row's published scope would exceed the new minimum, split or downgrade the row.


### F.9:17 - Didactic distillation (90-second script)

> A **Bridge** translates between **local senses** from different **Contexts**. It always declares **what relation** holds (`Equivalence`, `Narrower-than`, `Broader-than`, `Partial-overlap`, `Disjoint`, or an interpretation such as `Design-spec -> Run-trace`), **which CL value applies** (`CL 0-3`), **which way** (when direction matters), and **what is lost**. **Substitution** is supported only on the **same senseFamily** and only with **CL >= 2**; **Type-structure** needs **CL = 3**. **Interpretation Bridges** explain, never substitute. Rows in the Concept-Set table obey the **weakest-link**: their scope cannot exceed the lowest `CL` among their Bridges. When editions change or counter-examples appear, lower `CL` or change bridge kind; if two senses truly converge and invariants match, raise to **CL = 3**, rarely and with reasons. Translate across Contexts; never collapse them.

#### F.9:17.1 - Bridge stance overlay compatibility
A bridge card may carry a `F.9.1` Bridge Stance Overlay such as `localRename`, `operationalizes`, `partialAnalogy`, `projection`, or `nonEquivalent`. The overlay is a local interpretive annotation and **does not replace** the underlying bridge kind, direction, `CL`, or loss notes.

### F.9:18 - Archetypal Grounding

#### F.9:18.1 - Tell

A Bridge is not a synonym claim and not an enactment edge. It is a context-bounded correspondence record that tells a reader what may be reused, what may only be explained, and what is lost when meaning is transported.

#### F.9:18.2 - Show (System lane)

A service team may reuse the word *availability* across monitoring, SLO review, and architecture discussion. F.9 requires the team to publish Bridge Cards that separate observation, status target, and architectural concern rather than treating the shared label as silent sameness. The benefit is that naming convenience survives while substitution rights stay bounded by `senseFamily`, `CL`, and Loss Notes.

#### F.9:18.3 - Show (Episteme lane)

A comparative bundle may say that two traditions both discuss *readiness* or *capability*. Under F.9, that statement is only explanatory until the author publishes the two SenseCells, the Bridge kind, direction, `CL`, and the counter-example that marks where the comparison stops. The Bridge then becomes an auditable correspondence rather than a rhetorical shortcut.

#### F.9:18.4 - Coarsened cross-context note is not yet a Bridge Card

A service or review bundle may circulate a short cross-context note such as `the vendor bulletin is basically the same readiness signal as our rollback worksheet`. That note may be useful as informal orientation talk, but it is not yet an admissible Bridge Card and not yet a formal `F.9` `Naming-only` row.

Before any substitution, equivalence, `Naming-only` row, or interoperability claim is made, the source-bearing episteme or source publication needed for bridge support must be reopened and an explicit Bridge Card must publish the two SenseCells, bridge kind, direction, `CL`, Loss Notes, and admissible use. Friendly summary prose does not carry bridge support by itself.

### F.9:19 - Bias-Annotation


Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for cross-context correspondence and reuse.

* **Gov bias:** F.9 raises the declaration bar by requiring explicit Bridge Cards.
  *Mitigation:* keep the card compact and teach weakest-link discipline as the default review heuristic.
* **Arch bias:** the pattern prefers typed bridge declarations over friendly synonym prose.
  *Mitigation:* allow Naming-only scope and explanatory Interpretation Bridges so useful comparisons are not blocked.
* **Onto/Epist bias:** F.9 is local-first and resists global meaning claims.
  *Mitigation:* reuse remains possible, but only through explicit correspondence, direction, and Loss Notes.
* **Prag bias:** conservative `CL` assignment may feel slower than informal reuse.
  *Mitigation:* the pattern still supports bounded substitution when the evidence is good enough; it only blocks silent overreach.
* **Did bias:** the didactic script can make Bridge Cards look simpler than they are.
  *Mitigation:* Conformance, counter-examples, and weakest-link rules keep the teaching explanation tied to real constraints.

### F.9:20 - Conformance Checklist (CC-F.9)

A Bridge publication conforms to F.9 iff:

1. **CC-F.9-1 - Well-typed Bridge declaration.**
