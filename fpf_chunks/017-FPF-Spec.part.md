| **A4**  | **Global words**                | *Availability*, *latency* used without a Context.                                               | Collides senses across disciplines.             | Speak with **Context prefixes** (F.1). Cross‑context reuse demands a **Bridge** (F.9).                                                                         |
| **A5**  | **Percentile mirage**           | p95 computed on a pooled year while the clause is monthly.                                   | Predicate and Window misaligned.                | **R3 Predicate** + **R5 Window**: compute the statistic **per Clause’s Window**.                                                                         |
| **A6**  | **Proxy blindness**             | Synthetic probes stand in for user experience with no limitations stated.                    | Proxies miss geography, jitter, or pathologies. | Declare **Bridge(kind=proxy, CL, Loss)**. If proxy coverage is too weak, the verdict is **Inconclusive**.                                                |
| **A7**  | **Scope drift (Work mismatch)** | Measured another product’s or region’s traffic but judged the whole service.                 | Evidence is about the wrong **Work**.           | Tie **MeasureCell** to the **same WorkCell** (or a stated population‑of‑Works) as the Clause scopes.                                                     |
| **A8**  | **Retroactive renorm**          | A new clause or recalibrated monitor silently rewrites past verdicts.                        | Violates temporal honesty.                      | Enforce **Non‑retroactivity** (Inv‑6): past verdicts stand; new rules apply forward.                                                                     |
| **A9**  | **Silent units**                | “Latency ≤ 120” with no unit or scale.                                                       | Ambiguous thresholds.                           | **KD‑CAL discipline**: state **Characteristic, Scale, Unit** on **MeasureCell**.                                                                         |
| **A10** | **Hidden aggregation**          | “Global availability” but only a subset of regions/slices was covered.                       | Over‑claims evidence.                           | State the **aggregation scope** explicitly or confine the verdict to the observed subset; otherwise **Inconclusive**.                                    |
| **A11** | **Status on “the service”**     | Tagging an abstract umbrella like *“the service”* as “Satisfied”.                            | Loses the describedEntity of the judgement.           | Attach to **ClauseCell\@Window about WorkCell**; the service concept remains a promise vocabulary (A.2.3).                                               |
| **A12** | **Bridge‑by‑name**              | Equating *Activity* ≡ *Process* because both say “process”.                                  | Assumes global meaning.                         | Use **F.9 Bridge** with **kind/CL/Loss**; or keep them distinct.                                                                                         |
### F.12:11 - Extended worked examples

> Each example identifies **Contexts**, the **quadruple** ⟨ClauseCell, WorkCell, MeasureCell, Window⟩, any **Bridge(s)**, and the **Predicate**. The verdict attaches to *ClauseCell\@Window about WorkCell*.

#### F.12:11.1 - CDN latency across regions (services + sensing + types)

* **Contexts.** *ITIL 4* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure), *OWL 2* (type labels).
* **ClauseCell.** *p95 end‑user latency ≤ 200 ms per region per month*.
* **WorkCell.** *delivery Activities* per region during the month (PROV).
* **MeasureCell.** *response‑time Observations* tagged by region and path (SOSA/SSN).
* **Predicate.** For each region in the Window, `P95(latency) ≤ 200 ms`.
* **Bridges.** *probe→user* (**kind**: proxy; **CL** 2; **Loss**: last‑mile bias).
* **Verdict.** Region‑wise statuses; a global “all‑regions met” is the **logical AND** of region statuses (declare this aggregation explicitly).
* **Manager cue.** “Green map ≠ one green verdict”; acceptance is **per Clause per Window per Work population**.

#### F.12:11.2 - Stroke care: door‑to‑needle (method + enactment + status)

* **Contexts.** *clinical guideline canon* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure), *F.10* (status windows).
* **ClauseCell.** *90% of ischemic‑stroke episodes achieve door‑to‑needle ≤ 30 min per quarter*.
* **WorkCell.** Population of **patient‑episode Activities** started in the quarter.
* **MeasureCell.** Timestamps **Observation** of *door* and *needle* events (KD‑CAL).
* **Predicate.** `|{episodes with (needle−door ≤ 30)}| / |{episodes}| ≥ 0.9`.
* **Bridges.** *EHR event semantics → PROV Activity* (**Interpretation**, **CL** 2; **Loss**: missing triage tags).
* **Verdict.** If data gaps exceed a declared tolerance, status is **Inconclusive** rather than “Satisfied by assumption”.

#### F.12:11.3 - Cold‑chain warehouse (control + sensing + deontics)

* **Contexts.** *quality/deontics canon* (Clause), *IEC 61131‑3/PROV* (Work), *SOSA/SSN + ISO 80000‑1* (Measure).
* **ClauseCell.** *temperature ∈ \[2,8] °C for ≥ 99.5% of each day*.
* **WorkCell.** The warehouse’s **daily storage Activity**.
* **MeasureCell.** Thermistor **Observations** with calibrated units (KD‑CAL/ISO 80000‑1).
* **Predicate.** `(good_time / 24h) ≥ 0.995`.
* **Bridges.** *sensor position → product exposure* (**kind**: proxy; **CL** 2; **Loss**: stratification).
* **Verdict.** *Violated* if any day fails; annotate **Loss** to communicate assurance limits.

#### F.12:11.4 - SaaS incident MTTR (services + enactment)

* **Contexts.** *ITIL 4* (Clause), *PROV‑O* (Work).
* **ClauseCell.** *MTTR ≤ 60 min per incident*.
* **WorkCell.** Each incident’s handling **Activity**.
* **MeasureCell.** **Observations** of start‑fix and restore timestamps.
* **Predicate.** `(restore − start_fix) ≤ 60 min`.
* **Verdict.** Per incident; a quarter’s report is an explicit aggregation of incident‑scoped verdicts.


### F.12:12 - Reasoning primitives (judgement schemas, notation‑free)

> These are **mental inferences**; they neither read nor write artefacts. Each reads “if these thoughts hold, you may safely conclude …”.

1. **Clause–Work match**
   `covers(ClauseCell, WorkCell) ⊢ admissible(ClauseCell, WorkCell)`
   *Reading:* The Clause speaks **about** the kind of Work under judgement (scope alignment).

2. **Window adequacy**
   `Window is explicit ∧ Window intersects WorkCell-occurrence ⊢ admissible(Window)`
   *Reading:* There is a concrete time envelope; the Work actually occurred within it.

3. **Evidence sufficiency**
   `Observations E about WorkCell within Window ⊢ sufficient(E)`
   *Reading:* There exists a non‑empty set of outcome **Observations** relevant to the Work and Window.

4. **Evidence insufficiency → Inconclusive**
   `¬sufficient(E) ⊢ status = Inconclusive(ClauseCell, WorkCell, Window)`
   *Reading:* Absent admissible evidence, do not guess; mark **Inconclusive**.

5. **Predicate evaluation**
   `sufficient(E) ∧ eval(Predicate, E) = true ⊢ status = Satisfied(ClauseCell, WorkCell, Window)`
   `sufficient(E) ∧ eval(Predicate, E) = false ⊢ status = Violated(ClauseCell, WorkCell, Window)`
   *Reading:* The **Predicate** (threshold/percentile/share/band/…) decides directly from E.

6. **Bridge discipline**
   `usesCrossContexts(ClauseCell, WorkCell, MeasureCell) ∧ Bridges B declared ⊢ admissible(B)`
   `usesCrossContexts … ∧ ¬admissible(B) ⊢ status = Inconclusive`
   *Reading:* Cross‑context comparisons require explicit **Bridges**; without them, **Inconclusive**.

7. **CL aggregation (assurance hint)**
   `Bridges B = {b₁…bₖ} ⊢ effectiveCL = min(CL(bᵢ))`
   *Reading:* The weakest Bridge governs the assurance level communicated with the verdict (advisory to B.3 calculus).

8. **Population clauses**
   `Clause quantifies over population W = {w₁…wₙ} ⊢ status = agg({status(Clause, wᵢ, Window)})`
   *Reading:* For “≥ p%”‑style clauses, compute per‑Work verdicts, then apply the Clause’s quantifier.

9. **Non‑retroactivity**
   `newClause or newMonitor after Window ⊢ doesNotAlter(status@Window)`
   *Reading:* Later changes do not rewrite past verdicts.

10. **Conflict exposure**
    `two admissible Bridge sets ⇒ conflicting statuses ⊢ escalate as Inconclusive, expose Loss notes`
    *Reading:* If equally defensible translations disagree, the honest outcome is **Inconclusive** plus an explanation.


### F.12:13 - Relations (with other patterns)

* **Builds on:**
  **F.1** (Contexts): keeps all meanings **local**.
  **F.2–F.3**: provide the **SenseCells** that become Clause/Work/Measure anchors.
  **F.5**: ensures labels for Clause/Work/Measure and Windows are didactically clear.
  **F.7–F.9**: supply **Bridge** kinds / **CL** and loss semantics.
  **F.10**: defines **Status** families and **Window** constructs.
  **F.11**: protects **Method / MethodDescription / Work / Actuation** distinctions.

* **Uses (Part C patterns).**
  **KD‑CAL** (Observation/Characteristic/Scale/Unit).
  **Sys‑CAL** (Work/Actuation Contexts).
  **Kind-CAL** (type labels for populations or cohort selection).

* **Constrains:**
  Later reporting and assurance rules (B.3) must **not** collapse CL/Loss; they report them alongside status.


### F.12:14 - Migration notes (conceptual)

1. **Clause revisions.** Introduce a **new ClauseCell**; keep old verdicts intact (Non‑retroactivity).
2. **Monitor changes.** Update or replace **Bridges** (kind/CL/Loss). Future verdicts use the new Bridge; past ones are annotated, not rewritten.
3. **Scope corrections.** If evidence was about the wrong **Work**, retire the verdict and restate the quadruple; do **not** patch by redefining the Clause.
4. **Unit harmonisation.** When scales/units change, apply **KD‑CAL** conversions inside the Measure’s Context; if Cross‑context mapping is needed, declare a **Bridge**.
5. **Population refinement.** If a Clause’s quantifier is refined (e.g., per‑region → per‑AZ), treat each as a new ClauseCell or a new Window partition; avoid hidden re‑baselining.
6. **Proxy retirement.** When direct Observations become available, prefer them; keep earlier proxy‑based verdicts with their CL/Loss notes.


### F.12:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.12:15.1 - Static conformance (SCR)

* **SCR‑F12‑S01 (Quadruple present).** Every acceptance statement names **ClauseCell**, **WorkCell**, **MeasureCell**, and **Window**.
* **SCR‑F12‑S02 (context‑locality).** Each of the three Cells cites a **Context** (U.BoundedContext).
* **SCR‑F12‑S03 (Evidence admissibility).** The **Observation(s)** are **about** the **same Work** and lie within the **Window**.
* **SCR‑F12‑S04 (Predicate explicit).** The **Predicate** shape is stated (threshold/percentile/share/band/…) with any needed aggregation scope.
* **SCR‑F12‑S05 (Bridge discipline).** Any Cross‑context use declares **Bridge(kind, CL, Loss)**.
* **SCR‑F12‑S06 (Status trichotomy).** The verdict is exactly one of **{Satisfied, Violated, Inconclusive}** and attaches to **ClauseCell\@Window about WorkCell**.
* **SCR‑F12‑S07 (Unit honesty).** MeasureCell specifies **Characteristic, Scale, Unit** (KD‑CAL).
* **SCR‑F12‑S08 (Temporal honesty).** No verdict is asserted without a **Window**; no clause retroactively changes past verdicts.

#### F.12:15.2 - Regression checks (RSCR)

* **RSCR‑F12‑E01 (Bridge update).** When a **Bridge CL** changes, past verdicts stand; future verdicts **reference the new CL**; reports surface the difference.
* **RSCR‑F12‑E02 (Edition churn).** When a Context’s canon updates, Cells reference the **edition**; old verdicts remain bound to their original editions.
* **RSCR‑F12‑E03 (Scope drift guard).** If the Work population definition changes, verdicts are not silently re‑interpreted; new verdicts cite the new population.
* **RSCR‑F12‑E04 (Window partition).** Changing from monthly to weekly windows creates **new** verdicts; monthly summaries are expressed as explicit aggregations of weekly statuses.
* **RSCR‑F12‑E05 (Proxy retirement).** When direct Observations replace proxies, the status computation is re‑run **forward‑only**; past proxy‑based verdicts retain their CL/Loss annotations.


#### F.12:15.3 Didactic distillation (60‑second recap)

> **Bind promises to runs with measurements in time.**
> Name the **Clause**, the **Work** it talks about, the **Measure** of what actually happened, and the **Window**. Evaluate the Clause’s **Predicate** on Observations **about that Work in that Window**. If any concept crosses Contexts, declare a **Bridge** with **kind/CL/Loss**. The verdict (**Satisfied/Violated/Inconclusive**) attaches to **Clause\@Window about Work**, never to a plan or to the abstract service.

### F.12:End

## F.13 - Lexical Continuity & Deprecation

**“Change names without changing history.”**
**Status.** Architectural pattern.
**Builds on:** F.1 **context of meaning**; F.2 **Term Harvesting**; F.3 **Intra‑Context Clustering (SenseCell)**; F.5 **Naming Discipline**; F.7 **Concept‑Set (row) construction**; F.8 **Mint‑or‑Reuse decision**; F.9 **Bridges**; F.10 **Status windows**.
**Coordinates with.** Part C CALs when canon editions change (Sys/KD/Type/Method/LCA).
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No silent rewrites of old texts.


### F.13:1 - Intent & applicability

**Intent.** Provide a **conceptual discipline** for evolving labels (for **SenseCells**, **Concept‑Set rows**, and **Role Description names**) so that:

* new names **clarify** without erasing what earlier texts meant;
* aliases remain **local to Contexts**;
* genuine sense changes cause **explicit splits/merges** (F.7/F.9), not cosmetic renames.

**Applicability.** Whenever you consider **renaming**, **aliasing**, **deprecating**, or **retiring** any label in FPF: a SenseCell label in a Context, a Concept‑Set row label, or a Role Description name.


### F.13:2 - Problem frame

Unification efforts rot when names drift faster than senses or, worse, when senses change under a constant name.

* **Silent relabeling.** A new label is introduced as if nothing changed; readers cannot connect past to present.
* **Alias bloat.** Synonyms accumulate without discipline; reading becomes guesswork.
* **Cross‑context aliasing.** A single alias is made to stand for different Contexts (“global slang”), defeating locality.
* **Retroactive edits.** Old texts are silently rewritten to today’s names, corrupting provenance.


### F.13:3 - Forces

| Force                          | Tension to resolve                                                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| **Continuity vs truthfulness** | Preserve readers’ continuity yet surface real sense changes (no paint‑over).                 |
| **Locality vs convenience**    | Keep aliases **inside Contexts** even when a catchy global name tempts reuse.                   |
| **Simplicity vs coverage**     | Avoid giant synonym lists while still catching the one or two legacy names people will meet. |
| **Didactics vs formality**     | Make the mapping teachable without inventing new low‑level artefacts or processes.           |


### F.13:4 - Core idea (didactic)

**Treat names as lenses, not objects.**
The **thing that persists** is the *sense* (a **SenseCell** inside a Context, or the *Cross‑context alignment* embodied by a **Concept‑Set row**, or a **Role Description** that points to such sense). Names are **lenses** we look through. When the lens improves, we **record a continuity relation** between lenses; when the underlying sense changes, we **split/merge the thing**, then name accordingly.

> **Contexts keep names local.**
> A label (including aliases) always belongs to **one context** or to **one Concept‑Set row**. Cross‑context similarity is handled by **Bridges** (F.9), never by shared names.


### F.13:5 - Minimal vocabulary (this pattern only)

* **Legacy label** — a previously used label in the same Context (or same Concept‑Set row / Role Description).
* **Preferred label** — the current **F.5‑conformant** label for that item.
* **Alias** *(context‑local)* — a **read‑path** from a legacy label to the preferred one **inside the same Context** (or the same row/template). For writing, prefer the current label.
* **Continuity relation** — a small set of **relations over labels** (below) that capture whether a change is *just wording* or a *real sense change*.
* **Epoch note** — an **informative** time marker (“used before 2024‑07”) attached to a legacy label to help readers of old texts. (No storage format implied.)


### F.13:6 - Solution — Continuity, not “registries”

Rather than maintain a tool or workflow, **think with five continuity relations**. Use the *least strong* relation that tells the truth.

#### F.13:6.1 - Continuity relations (normative meanings)

1. **`renames(label_old → label_new)`** — *wording improved, sense unchanged*.
   *Use when:* Same **SenseCell** / same **Concept‑Set row** / same **Role Description**; only the surface form changed to satisfy F.5 (morphology, disambiguation, plain/tech harmony).
   *Effect:* `label_old` becomes a **context‑local alias** of `label_new`; both resolve to the **same thing**. Past texts remain valid.

2. **`aliases(label_legacy ↔ label_pref)`** — *legacy synonym kept for reading*.
   *Use when:* A common historical synonym exists **in the same Context** for the **same SenseCell**.
   *Effect:* Two‑way **read‑path** only; **writing uses `label_pref`**. Keep at most **one** legacy alias per register to avoid bloat.

3. **`splits(label_old ⇒ {label_A, label_B})`** — *one label covered multiple senses; now separated*.
   *Use when:* Your **SenseCell** was really two local senses; F.3 has **split** them; or a **Concept‑Set row** is refactored into two rows.
   *Effect:* `label_old` is **deprecated** (read‑path allowed to a **disambiguation note**); new writing uses `label_A`/`label_B`. No claim that either *continues* the old label wholesale.

4. **`merges({label_A, label_B} ⇒ label_new)`** — *two labels now recognized as one sense*.
   *Use when:* F.3 shows **same SenseCell**; or two Concept‑Set rows collapse after F.9 raised CL sufficiently.
   *Effect:* `label_A` and `label_B` become **aliases** of `label_new`. Keep one **epoch note** on each legacy label.

5. **`retires(label_old)`** — *name withdrawn without successor*.
   *Use when:* The label proved misleading and **no single successor** exists (e.g., it spanned different Contexts, or it was metaphorical).
   *Effect:* Only a **read‑warning** remains (“avoid in new writing; see Contexts X/Y”). Readers are pointed to **Bridges** or to multiple rows.

> **Important:** All five relations are **context‑local** (SenseCell level) or **row‑local** (Concept‑Set). **Never** use them to “alias” across Contexts. If a change crosses Contexts, it is not a rename; it requires a **Bridge** (F.9) and often a **split/merge of rows** (F.7).


### F.13:7 - Invariants (normative)

1. **Locality of alias.** `aliases(-)` and `renames(-)` operate **within one context** (SenseCell) or **within one Concept‑Set row / Role Description**.
2. **Truth over comfort.** If the **sense changed**, use `splits`/`merges` (and possibly adjust rows/Bridges), **not** `renames`.
3. **Non‑retroactivity.** Past texts remain phrased as written; continuity only **adds read‑paths**, never rewrites.
4. **Alias parsimony.** per Context and per row, keep **≤ 1** legacy alias per register (Tech/Plain); prefer the one readers will most likely encounter.
5. **Prefer present for writing.** In normative writing, use the **current preferred label** (F.5). Aliases are for **reading comprehension**.
6. **Bridge discipline.** If a label shift would require crossing Contexts to “explain”, it is **not a rename**; use **F.9 Bridge** and, if needed, refactor the **Concept‑Set row(s)**.
7. **Epoch honesty.** When declaring continuity, attach a **succinct epoch note** (“pre‑2023 usage”) if it aids readers.


### F.13:8 - Self‑checks (mental, not procedural)

* **Same‑sense test.** Can you point to the **same SenseCell** (or same row) before and after? If yes → `renames`/`aliases`. If no → `splits`/`merges`.
* **Context test.** Does the change stay **inside one context**? If it needs two Contexts to explain, it’s a **Bridge**, not a rename.
* **Reader test.** What two legacy strings would a newcomer actually meet in old texts? Keep **those two** as aliases; drop the rest.
* **History test.** Does your “continuity” require editing old claims? If yes, you’re attempting a **retroactive rewrite**—stop.
* **Didactic test.** Can you explain the continuity relation in **one sentence**? If not, you are hiding a sense change.


### F.13:9 - Micro‑examples (illustrative)

#### F.13:9.1 - Pure rename inside a Context (ITIL → clearer plain label)

*Context:* **ITIL 4 (services)**.
Old: **“SLO” (plain: *service target*)** → New: **“service‑level objective” (plain unchanged)**.
**Relation:** `renames("SLO" → "service‑level objective")`.
**Why:** F.5 morphology & expansion; SenseCell unchanged (same clause semantics).
**Effect:** Old guidance remains readable; new writing spells out the term.

#### F.13:9.2 - Alias for a common legacy synonym (Sys‑CAL)

*Context:* **state‑space control (design)**.
Preferred: **“actuation”**. Legacy: **“control output”**.
**Relation:** `aliases("control output" ↔ "actuation")`.
**Why:** Same SenseCell; legacy term appears in older textbooks.
**Effect:** Readers resolve to the SenseCell; new texts use “actuation”.

#### F.13:9.3 - Split of a muddled local sense (Enactment)

*Context:* **BPMN 2.0**.
Legacy label **“process”** was used to mean both **“collaboration”** and **“executable process”** in a team’s prose.
**Relation:** `splits("process" ⇒ {"collaboration","executable‑process"})`.
**Effect:** The single Concept‑Set row becomes two; old label is deprecated with a disambiguation note.

#### F.13:9.4 - Merge after clustering raised confidence (Kind-CAL row)

Two Concept‑Set rows **{“DBaaS”, “Database‑Service”}** converge after F.3 within the same context profile and F.9 raised CL.
**Relation:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")`.
**Effect:** “DBaaS” becomes a legacy alias with an epoch note.

#### F.13:9.5 - Not a rename: Cross‑context temptation (forbidden)

*Contexts:* **BPMN (design graph)** vs **PROV‑O (run activity)**.
Temptation: “Let’s rename *process* to *activity*.”
**Diagnosis:** Cross‑context; **different SenseCells**.
**Action:** **No continuity relation.** Keep labels; if needed, declare a **Bridge** (F.9) explaining design→run mapping with CL/Loss.

### F.13:10 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in texts                                                      | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                         |
| ------- | -------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Cross‑context rename**      | “Let’s rename *process (BPMN)* to *activity (PROV)*.”                 | Erases Context boundaries; hides loss; violates locality.         | **Do not rename across Contexts.** Keep both labels; if you must relate them, declare a **Bridge** (F.9) with CL/loss.              |
| **A2**  | **Retroactive rewrite**    | Old passages silently updated to new names.                           | Breaks provenance; misleads readers about what was meant then. | **Non‑retroactivity.** Past texts stand; add **read‑paths** via `renames/aliases`; attach **epoch notes** when helpful.          |
| **A3**  | **Alias flood**            | Long lists of synonyms for comfort.                                   | Raises ambiguity; dilutes teaching signals.                    | **Alias parsimony.** Keep ≤ 1 legacy alias per register (Tech/Plain) **inside the same Context or row**.                            |
| **A4**  | **Paint‑over rename**      | Rename used where sense actually changed.                             | Confuses continuity with revision; hides splits.               | Use **`splits`** (or **`merges`**), not `renames`. If Contexts diverge, adjust **rows** (F.7) and **Bridges** (F.9).                |
| **A5**  | **Global alias**           | One catchy word reused as alias in several Contexts.                     | Creates a pseudo‑global dictionary; invites category errors.   | **Local aliases only.** If a word appears in many Contexts, treat it as **homonymous**; keep Context‑prefixed speech.                  |
| **A6**  | **Euphemism treadmill**    | Frequent cosmetic renames (“modernising” labels) with no gain.        | Cognitive noise; readers lose confidence in names.             | Apply the **Same‑sense test**. If gain is marginal, **do nothing**; if clarity improves materially, one **`renames`** is enough. |
| **A7**  | **Grandfather everything** | Never deprecate confusing legacy labels.                              | Drags ambiguity forward; blocks sharper distinctions.          | When a label truly misleads and has no single successor, **`retires`** with a short **pointer note** to Contexts/rows.              |
| **A8**  | **Row drift via rename**   | Concept‑Set row is relabeled while its membership silently changes.   | Hides that the set changed; breaks Cross‑context alignment.       | First **split/merge rows** (F.7) as needed; only then `renames` the row **if** its intension stayed.                             |
| **A9**  | **Bridge‑by‑alias**        | Using an alias to hint two Contexts are “the same.”                      | Smuggles translation without CL/loss.                          | **No Cross‑context aliasing.** If similarity matters, **Bridge** explicitly (F.9) and keep labels separate.                         |
| **A10** | **Acronym absolutism**     | Treating acronyms as preferred labels everywhere (“SLO” in any Context). | Obscures Context‑specific senses; hurts didactics.                | Prefer **expanded** labels as preferred (F.5); keep acronym as context‑local **alias** only where historically dominant.            |
| **A11** | **Temporal fudge**         | Rename used to imply design↔run shift (“execution ≈ process”).        | Conflates time stances; erases important dualities.            | Keep **design/run** explicit on labels or glosses; if mapping is needed, do so in **F.9**.                                       |
| **A12** | **Over‑canonicalisation**  | Forcing a single “perfect” label across all rows/Contexts.               | Centralises language; breaks heterogeneity guard.              | Let each Context/row keep its **own preferred label**; put unification pressure only into **rows** and **Bridges**.                 |


### F.13:11 - Extended examples

#### F.13:11.1 - KD‑CAL × Services — *metric target* labels over time

* **Contexts:** *ITIL 4 (services, design)*; *SOSA/SSN (sensing, run)*.
* **Before:** Role Description used **“SLO”** (plain “target”) and readers often saw **“service target”**.
* **Move:** `renames("SLO" → "service‑level objective")` (Context: ITIL). Keep `aliases("service target" ↔ "service‑level objective")`.
* **Why:** Same local sense; clearer morphology for F.5; SOSA/SSN labels untouched.
* **Pay‑off:** Runtime **Observations** (SOSA) are later compared to **service‑level objective** clauses (ITIL) without Cross‑context aliasing.

#### F.13:11.2 - Sys‑CAL × LCA‑CAL — separating *execution* vs *actuation*

* **Contexts:** *IEC 61131‑3 (run)*; *state‑space control texts (design)*.
* **Temptation:** Rename **“task execution”** to **“actuation”** “to sound control‑ish”.
* **Diagnosis:** Different Contexts; different SenseCells (program run vs control output).
* **Move:** **No rename.** Keep labels; later add **Bridge** “`execution (IEC)` *produces* signals that realise `actuation (control)`” with CL stating partial coverage.
* **Pay‑off:** Plant narratives stop calling programs “actuators”; runtime vs control semantics stay crisp.

#### F.13:11.3 - Kind-CAL × Method‑CAL — false merge avoided

* **Contexts:** *OWL 2 (types, design)*; *SPEM 2.0 (methods, design)*.
* **Issue:** A row labeled **“Class”** tried to absorb **“WorkProductKind”** by a `renames`.
* **Diagnosis:** Not same sense; different calculi (type vs artefact category).
* **Move:** **Split the row**: `splits("class" ⇒ {"type‑class","work‑product‑category"})`.
* **Pay‑off:** Downstream Role Descriptions can point to the correct **SenseCell** without redefining ontological commitments.

#### F.13:11.4 - Enactment × KD‑CAL — retiring a misleading metaphor

* **Context:** *BPMN 2.0 (design)*.
* **Legacy:** Team jargon **“heartbeat”** used for a **timer event**. Newcomers confuse it with **sensor heartbeats** (KD‑CAL).
* **Move:** `retires("heartbeat")` in BPMN Context with note “use **timer event**; ‘heartbeat’ refers to sensor liveness in KD‑CAL”.
* **Pay‑off:** Two different ecosystems stop colliding on the same catchy word.

#### F.13:11.5 - Concept‑Set row refactor after rising CL

* **Rows:** `{“DBaaS”, “Database‑Service”}` representing service notions across several Contexts.
* **F.3 + F.9 outcome:** High CL; evidence of same Cross‑context alignment.
* **Move:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")` at **row level**. Both legacy labels become row‑local aliases with epoch notes.
* **Pay‑off:** One clearer row label; old articles still understandable.


### F.13:12 - Reasoning primitives (judgement schemas, notation‑free)

> Each judgement is a **pure thought**: premises ⇒ safe conclusion. No storage, no workflow, no roles.

Let **`ContextOf(ℓ)`** be the Context of label **ℓ** (when ℓ names a SenseCell); **`rowOf(ℓ)`** the Concept‑Set row (when ℓ names a row); **`senseOf(ℓ)`** the SenseCell it denotes (if local); **`pref(thing)`** the current preferred label of a SenseCell / row / Role Description.

#### F.13:12.1 - Same‑sense & same‑place

`ContextOf(ℓ₁)=ContextOf(ℓ₂) ∧ senseOf(ℓ₁)=senseOf(ℓ₂) ⊢ mayRename(ℓ₁→ℓ₂)`
*Reading:* If two labels denote **the same SenseCell in the same Context**, a rename is legitimate.

#### F.13:12.2 -Local alias

`ContextOf(ℓ₁)=ContextOf(ℓ₂) ∧ senseOf(ℓ₁)=senseOf(ℓ₂) ⊢ aliases(ℓ₁↔ℓ₂)`
*Reading:* Legacy synonym can be kept **as a read‑path**; writing uses `pref`.

#### F.13:12.3 - Split detection

`coversMultipleLocalSenses(ℓ) ⊢ splits(ℓ ⇒ {ℓA,ℓB,… })`
*Reading:* If one label straddles several local senses, declare a split and prefer the new precise labels.

#### F.13:12.4 - Merge admission

`ContextOf(ℓA)=ContextOf(ℓB) ∧ senseOf(ℓA)=senseOf(ℓB) ⊢ merges({ℓA,ℓB} ⇒ ℓN)`
*Reading:* Once F.3 shows identity of sense **within** a Context, merging labels into one preferred label is safe.

#### F.13:12.5 - Retirement

`misleading(ℓ) ∧ ¬∃ℓ' sameSense(ℓ,ℓ') ⊢ retires(ℓ)`
*Reading:* If a label misleads and has **no single** successor, retire it and point readers to relevant Contexts/rows.

#### F.13:12.6 - Cross‑context guard

`ContextOf(ℓ₁) ≠ ContextOf(ℓ₂) ⊢ ¬mayRename(ℓ₁→ℓ₂)`
*Reading:* Different Contexts forbid rename/alias; any relation goes to **Bridge** (F.9).

#### F.13:12.7 - Writing discipline

`thing t ⊢ writeWithPreferred(t) = pref(t)`
*Reading:* Normative prose uses the **current** preferred label; aliases are for reading.

#### F.13:12.8 - Reading resolution

`legacyLabel ℓ ⊢ readResolve(ℓ) = ⟨thing, pref(thing), epoch?⟩`
*Reading:* A reader can mentally resolve a legacy label to the **thing** and its present name, with epoch hint if needed.

#### F.13:12.9 - Alias budget

`aliasesFor(thing, register=r) = A ⊢ |A| ≤ 1`
*Reading:* Keep at most one legacy alias per register (Tech/Plain) for any one thing.

#### F.13:12.10 - Row‑level continuity

`rowOf(ℓA)=rowOf(ℓB)=R ∧ intension(R) stable ⊢ mayRenameRow(R,ℓB)`
*Reading:* A row label can change if the **row’s membership/intension** did not change; otherwise refactor rows first (F.7).


### F.13:13 - Relations

**Builds on:**
F.1 **context of meaning** (keeps locality), F.2 **Harvesting** (provides attested strings), F.3 **Clustering** (establishes SenseCells), F.5 **Naming Discipline** (supplies preferred labels), F.7 **Concept‑Set rows**, F.8 **Mint‑or‑Reuse**, F.9 **Bridges**, F.10 **Status windows**, F.11 **Method harmonisation**, F.12 **Service acceptance**.

**Constrains:**

* **F.5 (Naming):** may select preferred labels **only** after applying these continuity relations.
* **F.7 (Rows):** row relabels require row **intension** stability; otherwise use **split/merge rows**.
* **F.9 (Bridges):** Cross‑context changes must **not** be expressed as renames/aliases.

**Used by.**
All Part C patterns when editions shift; all examples and tutorials when teaching with legacy terminology.


### F.13:14 - Migration notes (conceptual playbook)

1. **Ask the same‑sense question first.** If the underlying **SenseCell/row** is unchanged, prefer `renames`; else reach for `splits/merges`.
2. **Keep it inside the Context.** If your explanation crosses Contexts, stop—this is **Bridge** territory (F.9), not a rename.
3. **Prefer clarity over fashion.** Rename only when the new label **removes a real ambiguity** (F.5 criteria), not to chase style.
4. **Limit nostalgia.** Admit **one** legacy alias in each register that readers will most likely meet; leave the rest to footnotes in examples.
5. **Deprecate with kindness.** When retiring a label, add a one‑line **pointer note** (e.g., “see `timer event` in BPMN; ‘heartbeat’ in KD‑CAL means sensor liveness”).
6. **Rows before names.** If a rename request coincides with a shift in what the row covers, **refactor rows** (F.7) first, then choose labels.
7. **Edition bumps.** When a canon updates, check labels used in that Context: if definitions shift, it’s a **split/merge**; if not, you may `renames` for style/uniformity.
8. **Teach the delta.** In primers, show a **mini table** with legacy → preferred pairs only where readers will encounter both.


### F.13:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.13:15.1 - Static conformance (SCR)

* **SCR-F13-S01 (context-local continuity).** Every `renames/aliases` relates labels **within the same context** or the **same row/Role Description**; none cross Contexts.
* **SCR‑F13‑S02 (Truthfulness).** For each `renames`, there exists an unchanged **SenseCell/row**; otherwise the move is rejected.
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of legacy aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR‑F13‑S05 (Row integrity).** A row rename occurs only when the row’s **intension** is stable; if membership changed, a **row split/merge** is documented (F.7).
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation is deferred to **F.9**.

#### F.13:15.2 - Regression (RSCR)

* **RSCR‑F13‑E01 (Edition drift audit).** When a canon edition changes, all labels from that Context are checked against definitions; moves are `renames` if senses stable, else `splits/merges`.
* **RSCR‑F13‑E02 (Alias creep check).** Periodically ensure alias budgets remain within **≤ 1 per register**; surplus aliases are pruned.
* **RSCR‑F13‑E03 (Bridge leak check).** Scan continuity notes for Cross‑context hints; any such case is converted into a **Bridge** or deleted.
* **RSCR‑F13‑E04 (Didactic continuity).** Sampling of examples shows that readers can **resolve** legacy labels to current ones without confusion (via the continuity notes).


### F.13:16 - Didactic distillation (60‑second script)

> **Names are lenses.** The *thing* that persists is the **sense** (a SenseCell in a Context, a Concept‑Set row, a Role Description). When you improve a lens, use **`renames`** or **`aliases`** **inside that same place**. When the *thing* changes, say so with **`splits/merges`**—and adjust rows/Bridges accordingly. **Never rename across Contexts.** Keep at most **one** legacy alias per register. Do **not** rewrite history; give readers **read‑paths** and brief epoch notes. With this discipline, you can clarify language without erasing meaning, and your models keep both **continuity** and **truth**.

### F.13:End

## F.14 - Anti‑Explosion Control (Roles & Statuses)

**“Name less, express more.”**

**Status.** Architectural pattern.
**Depends on.** F.1 **context of meaning**; F.2 **Harvesting**; F.3 **Local Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.8 **Mint‑or‑Reuse**.
**Coordinates with.** F.10 **Status Windows & Mapping**; F.11 **Method Quartet Harmonisation**; F.12 **Service Acceptance Binding**; F.13 **Lexical Continuity**.
**Aliases (informative).** *Role/Status economy*; *Explosion guard*.


### F.14:1 - Intent & applicability

**Intent.** Prevent the uncontrolled growth of **Roles** and **Statuses** by privileging **reuse**, **bundling**, **explicit separation‑of‑duties (SoD)**, and **applicability windows** over minting new names. Keep the vocabulary **small, crisp, and composable** while remaining faithful to local meanings fixed by Contexts (F.1) and SenseCells (F.3).

**Applicability.** Whenever a new Role/Status is proposed, a team merges two lines of work, or a domain shifts its jargon. Use this pattern before adding rows to the Concept‑Set Table (F.7) or new Role Descriptions (F.4).

**Non‑goals.** No org charts, no RBAC policies, no process roles. This pattern describes **mental moves** for architectural naming, not governance machinery.


### F.14:2 - Problem frame

Left unchecked, Role/Status vocabularies tend to **diverge**:

1. **Synonym stacks.** *Reviewer*, *Approver*, *Validator*, *Verifier* minted separately despite overlapping responsibilities.
2. **Modifier creep.** *Night‑Operator*, *Shift‑Operator*, *Remote‑Operator* proliferate where one Role plus a window would suffice.
3. **SoD leakage.** New names invented to **evade** an intended separation (*Requestor‑Approver* as one Role).
4. **Status paintjobs.** *Compliant*, *At‑Risk*, *Grace*, *Waived*, *Temporarily‑Breached*—labels multiply where a **single Status × window** model would be clearer.
5. **Context blending.** A control‑Context *Actuator* gets treated as an Enactment *Execution* Role; a deontic *Duty* becomes a runtime *Status*.

Explosion harms didactics and increases alignment cost (F.9).


### F.14:3 - Forces

| Force                           | Tension to resolve                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Expressiveness vs parsimony** | We must name real distinctions, but each new name increases cognitive load.                            |
| **Locality vs uniformity**      | Roles/Statuses are **context‑local**; yet we need a stable Cross‑context story through Concept‑Set rows.     |
| **Safety vs convenience**       | SoD constraints protect systems, but people seek convenience through composite roles.                  |
| **Temporal honesty**            | Many “new” Statuses are actually the **same** Status seen in different **windows** (design/run/grace). |


### F.14:4 - Minimal vocabulary (this pattern only)

* **Role Description** (F.4): a **Role** (behavioural mask) or **Status** (epistemic/deontic standing) tied to a **SenseCell**.
* **Concept‑Set row** (F.7): a Cross‑context **intent** (“what we count as one thing”) aligned by SenseCells.
* **Bundle** (this pattern): a **named composition** of Role Descriptions that are meant to be used together by design (e.g., {Requester, Approver} for change control). A Bundle is a **concept**, not a package.
* **SoD Constraint** (this pattern): a **conceptual rule** stating that two Roles **must not** be played by the same Holder in the **same window**.
* **Window** (F.10): an **claim scope** (time stance, holon level, run segment) that delimits when a Role/Status holds.


### F.14:5 - Core idea (didactic)

**Use four levers before minting a name:**

1. **Reuse the row.** If the intent matches an existing Concept‑Set row and the local SenseCell is already present, **use it**.
2. **Bundle, don’t blur.** When two Roles must travel together, **name the Bundle**, not a new hybrid Role.
3. **Declare SoD, don’t fuse.** When Roles must stay apart, **state the SoD** instead of minting a “super‑role.”
4. **Window, don’t multiply.** When a Status looks different across time/scale, keep **one Status** with **explicit windows**.


### F.14:6 - Solution — the control cabinet (conceptual, notation‑free)

#### F.14:6.1 - Reuse by row (first lever)

* **Move.** If a proposal matches the **intension** of an existing row (F.7), adopt its Role Description or add a local SenseCell **inside that row**.
* **Pay‑off.** Names don’t proliferate; Cross‑context tables stay thin.

**Example (services).** *Service‑availability‑compliance* already exists as a row. New labels *SLO‑Met* / *Uptime‑OK* **reuse** that row; SOSA/SSN Observations later feed it (F.12).


#### F.14:6.2 - Bundle instead of hybrid (second lever)

* **Move.** When practice always pairs two Roles, define a **Bundle** `{RoleA, RoleB}`.
* **Not a hybrid.** Do **not** coin *RoleAB*; you’ll erase SoD options and obscure responsibilities.

**Example (enactment).** `{Requester, Approver}` is a Bundle. *Request‑Approver* (one Role) is **not** allowed; it contradicts intended checks.


#### F.14:6.3 - Separate by SoD, don’t evade (third lever)

* **Move.** Record **SoD constraints** where separation matters (“Requester ⟂ Approver in run window”).
* **Why here.** SoD belongs to **semantics**, not org policy; it protects structure across Contexts and times.

**Example (methods).** `{Author ⟂ Reviewer}` in the **review window**. A proposal *Senior‑Reviewer* to “do both” is rejected; the **Bundle** remains `{Author, Reviewer}` with SoD.


#### F.14:6.4 - Window the Status (fourth lever)

* **Move.** Keep a single Status and attach **windows** for *grace*, *evaluation*, *active*, *archival*.
* **Avoid.** *Compliant*, *At‑Risk*, *Grace* as separate Status types.

**Example (acceptance).** **Compliance** Status has readings per window:

* *evaluation window:* “pending check”,
* *active window:* “met / breached”,
* *grace window:* “temporarily tolerated breach”.
  One Status; clear windows.


#### F.14:6.5 - Factor modifiers as facets, not names

* **Move.** Treat qualifiers (shift, locality, domain) as **facets** of the same Role/Status or as **windows**, not new types.

**Example (operations).** *Operator* with **window facet** `timeOfDay = night`—not a new Role *Night‑Operator*.


### F.14:7 - Invariants (normative)

1. **context‑locality.** Each Role Description remains tied to a **SenseCell** in a **single Context** (F.3, F.4).
2. **Row preference.** New Role Descriptions **SHOULD** map to an existing row; new rows (F.7) require F.8 justification.
3. **No hybrid Roles.** If two Roles are conceptually distinct, they **must not** be fused into one to bypass SoD. Use **Bundle + SoD**.
4. **Windowed statuses.** Status proliferation across time/scale **MUST** be expressed as **windows** of a single Status family (F.10).
5. **Bundle clarity.** A Bundle **names only composition**; it does not inherit or redefine member semantics.
6. **Minimal modifier naming.** Adding a modifier to a label **MUST** pass F.5 tests; prefer facets/windows over new Role/Status names.
7. **Concept‑first.** No invariant relies on organization charts or access policies; **semantics precede governance**.


### F.14:8 - Reasoning primitives (judgement schemas)

> Pure mental moves; no tools, no workflows.

Let **`rowOf(τ)`** be the Concept‑Set row of template **τ**, **`senseOf(τ)`** its SenseCell, **`win(τ)`** its window set.

1. **Row reuse admissibility**
   `intent(τₙ) ≡ intent(row r) ∧ ∃σ: senseOf(σ) in r ⊢ reuseRow(τₙ → r)`
   *Reading:* If the proposed template’s intent matches an existing row with a local SenseCell, reuse the row.

2. **Bundle recommendation**
   `alwaysTogether{α,β} ∧ distinct(α,β) ⊢ bundle({α,β})`
   *Reading:* If two distinct Roles occur together by design, name the Bundle.

3. **SoD necessity**
   `conflictRisk{α,β} ∧ sameHolder ∧ sameWindow ⊢ SoD(α ⟂ β)`
   *Reading:* If the same Holder in the same window would create a conflict, require SoD.

4. **Hybrid rejection**
   `SoD(α ⟂ β) ⊢ forbid(hybrid(α,β))`
   *Reading:* A SoD pair cannot be fused into one Role.

5. **Windowing over multiplication**
   `status σ showsVariantsAcross(w₁,…,wₖ) ⊢ keepOneStatus(σ) ∧ win(σ)={w₁,…,wₖ}`
   *Reading:* Variants across time/scale become windows, not new Status names.

6. **Facet over rename**
   `modifier m changes circumstance ¬ essence ⊢ preferFacet(τ,m)`
   *Reading:* If a modifier alters circumstances only, represent it as a facet/window.


### F.14:9 - Micro‑examples (engineer / manager / researcher lenses)

#### F.14:9.1 - Enactment (change control)

* **Proposal.** *Requester‑Approver* as a single Role “to move faster.”
* **Moves.** SoD(`Requester ⟂ Approver`) + **Bundle** `{Requester, Approver}`.
* **Result.** Same throughput, preserved checks, no hybrid Role.

#### F.14:9.2 - Services (SLO evaluation)

* **Proposal.** New Status *At‑Risk*.
* **Moves.** Keep **Compliance** Status; add **grace window** and a **forecast facet** (informative) if needed.
* **Result.** One Status with windows; fewer names, clearer timelines.

#### F.14:9.3 - KD‑CAL (evidence)

* **Proposal.** *Pre‑validated* between *Verified* and *Validated*.
* **Moves.** Use **Status chain** within one family: `Verified → Validated`; represent uncertainty as **confidence** (F.10), not another Status.
* **Result.** Clean ladder; no extra label.

#### F.14:9.4 - Sys‑CAL (plant ops)

* **Proposal.** *Night‑Operator*, *Remote‑Operator*.
* **Moves.** **Role:** Operator; **facets/windows:** `timeOfDay`, `presenceMode`.
* **Result.** One Role, portable qualifiers.

#### F.14:9.5 - Method quartet (reviews)

* **Proposal.** *Senior‑Reviewer* to bypass `{Author ⟂ Reviewer}`.
* **Moves.** Keep SoD; if seniority matters, introduce **Assurance Level** facet (F.10) on the **review decision**, not a new Role.
* **Result.** Separation preserved; trust expressed as a Status property, not a Role type.

### F.14:10 - Anti‑patterns & remedies

| #       | Anti‑pattern                             | Symptom in models                                                                            | Why it harms thinking                                             | Remedy (conceptual move)                                                                                                          |
| ------- | ---------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Hybrid Role minting**                  | *Request‑Approver*, *Dev‑Ops‑Engineer* as one Role.                                          | Erases intended checks; conceals distinct responsibilities.       | **Bundle** `{Requester, Approver}` + **SoD** (`Requester ⟂ Approver`). Keep Roles distinct; name the cooperation, not the fusion. |
| **A2**  | **Modifier‑as‑type**                     | *Night‑Operator*, *Remote‑Operator*, *On‑call‑Reviewer*.                                     | Name proliferation for circumstantial qualifiers.                 | Keep **Role = Operator/Reviewer**; express *night/remote/on‑call* as **facets or windows** (F.10).                                |
| **A3**  | **Window‑as‑type**                       | *Compliant*, *At‑Risk*, *Grace*, *Breached* as separate Status types.                        | Paints temporal phases as different essences; breaks comparisons. | One **Status family** (e.g., **Compliance**) with **windows**: *evaluation / active / grace / archival* (F.10).                   |
| **A4**  | **Row drift**                            | New Concept‑Set row for *Uptime‑OK* when **Service‑Availability‑Compliance** already exists. | Splits one intent across rows; Cross‑context tables get wide.        | **Reuse the row** (F.7) if intent matches; add local **SenseCell** if needed.                                                     |
| **A5**  | **SoD evasion via “trusted” super‑role** | *Senior‑Reviewer* allowed to both author and review.                                         | Conflicts of interest reintroduced under prestige.                | Keep **SoD(Author ⟂ Reviewer)**; if trust matters, attach **Assurance Level** to the *decision* (Status facet), not a new Role.   |
| **A6**  | **cross-context fusion**                    | One Role Description mixes *Execution (IEC)* with *Duty (ODRL)* semantics.                       | Violates locality; meanings leak across Contexts.                    | Keep each **Role Description** tied to a **SenseCell** (F.4). cross-context reasoning uses **Bridge** (F.9).         |
| **A7**  | **Synonym carousel**                     | *Validator* vs *Verifier* vs *Checker* minted separately in the same Context.                   | Cognitive noise; ambiguous separation.                            | Choose **one label** via F.5; keep others as **aliases** in **Lexical Continuity** (F.13), not new templates.                     |
| **A8**  | **Org-chart mirroring**                  | Roles cloned from a company chart (*Squad-Lead*, *Tribe-Lead*) as generic **Role Descriptions**. | Organisation-specific names masquerade as semantics.              | Map local titles to **Bundles** of generic Roles (e.g., `{Planner, Coordinator}`), or treat as **aliases** (F.13). |
| **A9**  | **KPI‑as‑Status inflation**              | *Latency‑Good*, *Latency‑Bad*, *Latency‑Poor* as Status types.                               | Encodes numeric thresholds as separate essences; brittle.         | One **Quality Status** with **metric threshold** in its window definition (F.10/F.12); keep adjectives out of type names.         |
| **A10** | **Traffic‑light mania**                  | *Red/Amber/Green* Status types reused across unrelated families.                             | False unification across different intents; color ≠ meaning.      | Keep canonical **Status name** (e.g., **Compliance**); use **presentation** as a separate concern; colors are not types.          |
| **A11** | **Bundle masquerading as Role**          | *Change‑Manager* invented to hide `{Requester, Approver, Implementer}`.                      | Collapses structure; SoD becomes optional.                        | Name the **Bundle** and its **SoD** explicitly; keep Roles atomic.                                                                |
| **A12** | **State‑as‑Status sprawl**           | *Pre‑validated*, *Validated*, *Re‑validated*, *De‑validated*.                                | States are temporal positions on one ladder.                      | Define one **Validation Status** with **state ladder** and **windows**; use **Assurance Level** as a facet if needed.             |
| **A13** | **Contextless Role Description**            | Role Description without a SenseCell anchor.                                                     | Floating meaning; later bridges cannot be made explicit.          | Tie every **Role Description** to a **SenseCell** (F.4). If none fits, use F.8 to decide: **new row** or **rename/reuse**.        |
| **A14** | **Profile‑driven clones**                | *API‑Approver*, *Data‑Approver*, *Model‑Approver* as different Roles.                        | Scales by surface area; loses the shared essence.                 | One **Approver** Role with a **scope facet** (`objectType=API/Data/Model`).                                                       |


### F.14:11 - Worked examples

#### F.14:11.1 - Enactment + Services + KD‑CAL — “SLO compliance without label sprawl”

**Contexts.** ITIL 4 (services), SOSA/SSN (sensing), PROV‑O (run).
**Intent.** Track SLO compliance with minimal Status vocabulary.

* **Naïve proposal.** Statuses: *Compliant*, *At‑Risk*, *Breached*, *Grace*, *Waived*.
* **Moves (F.14).** Keep **Compliance** as one **Status family**; define **windows**: *evaluation* (prediction against forecast), *active* (actuals vs target), *grace* (tolerated breach). **Waiver** becomes a **deontic Status** in ODRL Context, not part of Compliance.
* **Outcome.** One Status + windows; observations (SOSA) and provenance (PROV) feed the *active* window; service policy (ITIL/ODRL) defines *grace*.

#### F.14:11.2 - Method‑CAL + Enactment — “Reviews with SoD and Bundle”

**Contexts.** SPEM/ISO 24744 (methods), Enactment lexicon.
**Intent.** Prevent authors reviewing their own work while keeping names lean.

* **Naïve proposal.** Roles: *Author*, *Self‑Reviewer*, *Peer‑Reviewer*, *Senior‑Reviewer*.
* **Moves.** Roles **Author**, **Reviewer** only; **SoD(Author ⟂ Reviewer)** in the **review window**. If practice needs two reviewers, mint **Bundle** `{Reviewer, Reviewer₂}`; express **seniority** as a **facet** on the *decision* (Assurance Level), not a new Role.
* **Outcome.** Two Roles, one Bundle, one SoD; no hybrid Role; assurance is visible as a property of the review result.

#### F.14:11.3 - Sys‑CAL + LCA‑CAL + Services — “Operations without role fragments”

**Contexts.** IEC 61131‑3 (execution), state‑space control texts (actuation), ITIL 4 (services).
**Intent.** Staff coverage across shifts and locations without ten operator types.

* **Naïve proposal.** *Night‑Operator*, *Remote‑Operator*, *Local‑Operator*, *Shift‑Lead*, *On‑call‑Operator*.
* **Moves.** **Role** = **Operator**; add **facets/windows**: `timeOfDay`, `presenceMode`, `dutyCycle`. If coordination is distinct, mint **Coordinator** Role; when both occur together, **Bundle** `{Operator, Coordinator}`; keep **SoD** where needed (e.g., `Operator ⟂ Approver` for production change).
* **Outcome.** One Role + small facet set + Bundle; clean hooks to execution and actuation semantics.

#### F.14:11.4 - KD‑CAL + Kind-CAL — “Evidence ladder without new labels”

**Contexts.** KD‑CAL (evidence), OWL 2/FCA (types).
**Intent.** Express proof maturity without inflating Status names.

* **Naïve proposal.** *Candidate‑Evidence*, *Preliminary‑Evidence*, *Verified‑Evidence*, *Validated‑Evidence*.
* **Moves.** Keep one **Evidence Status** ladder (`Collected → Verified → Validated`); use **Assurance Level** facet (numeric or ordinal) and **windows** for in‑review vs active. Align *types* in a **row**; do not mint new Status names for granularity.
* **Outcome.** Short vocabulary, clear ladder, quantitative facet where nuance is needed.


### F.14:12 - Relations (with other patterns)

* **Builds on:** F.1 (Contexts), F.2 (Harvesting), F.3 (Local Clustering), F.4 (Role Description), F.5 (Naming).
* **Constrains:**

  * **F.7 (Concept‑Set Table):** prefer **row reuse**; new rows require F.8 justification.
  * **F.8 (Mint‑or‑Reuse):** apply **four levers** (reuse, bundle, SoD, window) before minting.
  * **F.10 (Status Windows & Mapping):** encode temporal/scale variation as **windows**, not new Status types.
  * **F.12 (Service Acceptance Binding):** bind acceptance to the **Compliance** Status family; avoid ad‑hoc status labels.
  * **F.13 (Lexical Continuity):** prior names become **aliases**; do not carry forward inflated vocabularies as new types.
* **Used by.** FPF patterns to keep Role/Status vocabularies tight.


### F.14:13 - Migration notes (conceptual playbook)

1. **Map to rows.** For each existing Role/Status, identify its **Concept‑Set row**; if two names share an intent, **collapse** to one row (keep other names as **aliases**, F.13).
2. **Extract SoD.** Replace “super‑roles” with **Bundles** plus explicit **SoD**; where conflict exists, SoD is **normative**, not cultural.
3. **Demote modifiers.** Convert adjectival Role types into **U.Facet** (per Compose‑CAL) or **windows** on the base Role.
4. **Window statuses.** Merge Status families split by time/scale into **one Status + windows**; move waived/exempt notions to the **deontic Context** if applicable.
5. **Re‑use before minting.** When encountering a gap, scan rows for a near‑match; only if intent genuinely differs, open a **new row** (F.8).
6. **Preserve continuity.** Keep historic labels as **aliases** under the consolidated template (F.13); do not rewrite past texts.
7. **Rehearse the cut.** After consolidation, you should be able to recite the entire Role/Status vocabulary **from memory**; if not, reduce again.


### F.14:14 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.14:14.1 - SCR — Static conformance

* **SCR‑F14‑S01 (Row reuse).** Every newly proposed Role Description either **references an existing row** or includes a clear **F.8 justification** for a new row.
* **SCR‑F14‑S02 (No hybrids).** No Role Description’s label or definition **conflates** two Roles that stand in a declared **SoD** relation.
* **SCR‑F14‑S03 (Windowed statuses).** Each Status family that shows temporal/scale variation is expressed as **one Status + windows** (not multiple Status types).
* **SCR‑F14‑S04 (Facet over modifier).** Role names do not encode circumstantial modifiers; such modifiers appear only as **facets/windows**.
* **SCR‑F14‑S05 (Context locality).** Every Role Description is anchored to **exactly one SenseCell**; no Cross‑context semantics inside a single template.
* **SCR‑F14‑S06 (Bundles are pure).** Every **Bundle** is a **set of templates** with **no additional semantics** beyond membership and referenced **SoD**.

#### F.14:14.2 - RSCR — Regression (evolution)

* **RSCR‑F14‑E01 (Vocabulary slope).** Over a given interval, the count of distinct Role/Status templates **does not increase** unless matched by **row justifications** (F.8).
* **RSCR‑F14‑E02 (SoD integrity).** Adding templates does not introduce a label that **circumvents** any existing **SoD** relation.
* **RSCR‑F14‑E03 (Window integrity).** When windows are refined, **Status type count** remains constant; only window definitions change.
* **RSCR‑F14‑E04 (Alias discipline).** When labels change, prior names are recorded as **aliases** (F.13); no silent type multiplication.


### F.14:15 - Didactic distillation (90‑second script)

> **Name less, express more.** Before minting a new Role or Status, try **four levers**:
> **(1) Reuse the row** — if the intent already exists, adopt it and add your local SenseCell.
> **(2) Bundle, don’t blur** — when two Roles travel together, **Bundle** them; keep **SoD** if they must stay apart.
> **(3) Declare SoD, don’t fuse** — conflicts of interest are solved with **SoD**, not with “trusted” super‑roles.
> **(4) Window, don’t multiply** — one **Status** can wear different **windows** (evaluation/active/grace); that’s not four Status types.
> Keep modifiers as **facets**, not names; keep every Role Description **context‑local** via its SenseCell. If your vocabulary no longer fits in a thoughtful mind, you have an **explosion**—return to the levers and reduce.

### F.14:End

## F.15 - SCR/RSCR Harness for Unification

**“Prove locality and parsimony first; only then prove composition.”**
**Status.** Architectural pattern.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.0.1 **Foundational Principles**; F.1–F.14.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (for CL use on Bridges).


### F.15:1 - Intent & applicability

**Intent.** Provide a **minimal, notation‑free harness of conceptual checks** that tells you whether a unification slice is **sound**: Contexts are fixed and diverse (F.1), terms are harvested and clustered **inside** Contexts (F.2–F.3), Role Descriptions **point to one SenseCell** (F.4), names obey discipline (F.5), rows are reused instead of multiplied (F.7–F.8), bridges are **explicit and penalised** (F.9), statuses vary by **windows** not type proliferation (F.10), and cross‑line bindings (F.11–F.12) respect locality.
**Applicability.** Use whenever you declare or revise any of: Context cards, Local‑Senses, SenseCells, Concept‑Set rows, Role Descriptions, Bridges, Status windows.
**Non‑goals.** No registries, workflows, or storage formats. No team roles. No metrics dashboards. This is **thinking discipline**, not governance.


### F.15:2 - Problem frame

Without a unification harness:

1. **Locality leaks.** Cross‑context equivalence creeps in “by name”.
2. **Row sprawl.** Concept‑Set tables grow laterally with near‑duplicates.
3. **Role/Status inflation.** Adjectival or temporal variants become new types.
4. **Silent rewrites.** New editions overwrite old meanings without a trace.
5. **Unstable bridges.** Cross‑context relations harden into dogma without CL or loss statements.


### F.15:3 - Forces

| Force                      | Tension to resolve                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| **Parsimony vs coverage**  | Keep vocabularies small yet expressive across multiple Contexts.         |
| **Locality vs reuse**      | Preserve context‑local meaning while enabling Cross‑context comparison.     |
| **Stability vs evolution** | Allow new editions and rows without erasing prior sense.              |
| **Clarity vs formality**   | Checks must be teachable in minutes yet strong enough to catch drift. |


### F.15:4 - Core idea (didactic)

The harness is a **two‑tier net of assertions**:

* **SCR — Static Conformance Rules.** context‑local and cross‑artefact checks that must hold **now**.
* **RSCR — Regression & Stability Rules.** Checks that must hold **across changes** (editions, rows, names).

**Registry-reference note (normative).** When an SCR/RSCR mentions `BridgeId`, policy identifiers, or edition identifiers, these are treated as **registry references**. They MUST be validated by registry presence/version checks, but MUST NOT be treated as symbols that have to appear in any `provides` list (e.g., `SignatureManifest.provides`) or be satisfied via `imports` closure, because they are not part of a signature’s exported vocabulary; they are external registry keys.

All checks are expressed as **judgement schemas** (premises ⊢ conclusion). They **never** prescribe artefact formats, roles, or workflows.


### F.15:5 - Minimal vocabulary (this pattern only)

* **Unification line (L).** The thematic cut you are pursuing (e.g., Enactment + Sensing + Execution).
* **Check.** A content‑level assertion about Contexts, senses, rows, Role Descriptions, bridges, or windows.
* **Witness.** A **thoughtful minimal example** that makes a check concrete (e.g., one seed, one bridge pair).
* **Slice.** The small set of objects under scrutiny together (Contexts in view, the row you’re adding, the Role Description that uses it, and any bridge it needs).


### F.15:6 - Objects under check

1. **Contexts** — `U.BoundedContext` cards (F.1).
2. **Local‑Sense** — clustered sense inside one context (F.3).
3. **SenseCell** — *(Context × Local‑Sense)* address (F.3/F.4).
4. **Concept‑Set row** — a cross‑projection hypothesis of “the same thing” (F.7).
5. **Role Description** — Role/Status definition pointing to **one** SenseCell (F.4).
6. **Bridge** — explicit Cross‑context relation with CL and loss notes (F.9).
7. **Windows** — temporal/scale views for a Status family (F.10).
8. **Aliases** — name continuity commitments (F.13).
9. **Bundles & SoD** — reuse levers that replace hybrid roles (F.14).


### F.15:7 - Solution overview — the harness as a lattice of checks

The harness arranges checks in three clusters:

* **S‑Local.** context‑local sanity (anchoring, clustering, two‑register labels).
* **S-Cross.** Cross-artefact coherence (row reuse, single-cell **Role Description**, bridge discipline, window honesty).
* **R‑Evo.** Evolution continuity (no silent rewrites, no vocabulary creep, bridge re‑validation).

### F.15:8 - SCR — Static conformance rules (S‑Local)

> All S‑Local rules are **Context‑internal** and derive only from F.1–F.5.

**SCR‑F15‑S1 (Anchored term).**
`Seed σ has context C ⊢ C ∈ Contexts(L)`
*Reading:* Every harvested seed lives in a Context that is **deliberately in view** for your line (F.1, F.2).

**SCR‑F15‑S2 (Edition trace).**
`Occurrence ω supports σ ⊢ ω carries edition+location`
*Reading:* A Local‑Sense can be mentally reconstructed from attestations (F.2).

**SCR‑F15‑S3 (Intra‑Context clustering).**
`Local‑Sense λ clusters {σᵢ} ⊢ ∀i: context(σᵢ)=context(λ)`
*Reading:* No Cross‑context items inside a Local‑Sense (F.3).

**SCR‑F15‑S4 (Two registers).**
`Local‑Sense λ ⊢ label(λ)=⟨tech,plain, symbol?⟩ ∧ plain≠∅ ∧ tech≠∅`
*Reading:* Both engineering and plain labels exist; symbol (if any) is purely informative (F.2/F.3/F.5).

**SCR‑F15‑S5 (Minimal gloss).**
`gloss(λ) framed at minimal necessary generality`
*Reading:* The gloss neither smuggles behaviour/deontics nor globalises the sense (F.2/F.5).

**SCR‑F15‑S6 (Context‑local normal form).**
`normalize_C(surface)=n ⊢ n used only within C`
*Reading:* No global normal form at this stage (F.2).


### F.15:9 - SCR — Static conformance rules (S‑Cross)

> S‑Cross rules tie Contexts, rows, Role Descriptions, bridges, and windows together **without** breaking locality.

**SCR-F15-S7 (Single-cell Role Description).**
`Role Description τ ⊢ anchor(τ)=one SenseCell ⟨C,λ⟩`
*Reading:* Every Role Description points to exactly **one** SenseCell; no mixed semantics (F.4).

**SCR-F15-S8 (Name discipline).**
`Role Description τ ⊢ name(τ) obeys F.5`
*Reading:* Labels follow the agreed morphology, register pairing, and minimal generality (F.5).

**SCR‑F15‑S9 (Row sufficiency).**
`Row ρ lists cells {⟨Cᵢ,λᵢ⟩} ⊢ |distinct(Cᵢ)| ≥ 2`
*Reading:* A row is meaningful only if it spans **at least two Contexts** (F.7).

**SCR‑F15‑S10 (Row purity).**
`Row ρ ⊢ no cell contains Cross‑context clustering`
*Reading:* Each cell is a **single** SenseCell, not a pre‑merged bundle (F.7).

**SCR‑F15‑S11 (Reuse before mint).**
`Proposed row ρ' overlaps intent(ρ) ⊢ prefer reuse(ρ) ∨ document F.8 decision`
*Reading:* Rows are reused by default; new rows require a mint‑or‑reuse rationale (F.7–F.8).

**SCR‑F15‑S12 (Bridge is explicit).**
`C₁≠C₂ ∧ relation asserted between λ₁,λ₂ ⊢ Bridge β: ⟨⟨C₁,λ₁⟩ ↔ ⟨C₂,λ₂⟩, kind, CL, loss⟩`
*Reading:* Cross‑context relations appear **only** as Bridges with declared kind (≡, ⊑, ⊒, ⟂), Congruence Level, and loss notes (F.9; B.3 for CL semantics).

**SCR‑F15‑S13 (Bridge locality).**
`Bridge β ⊢ cells belong to different Contexts`
*Reading:* You never bridge **within** a Context; that’s clustering (F.3/F.9).

**SCR‑F15‑S14 (Window honesty).**
`Status family Σ varies by time/scale ⊢ windows(Σ) define variation; no new Status types introduced`
*Reading:* Temporal and scale variation appears as **windows**, not as new types (F.10).

**SCR-F15-S15 (SoD preservation).**
`Bundle B = {τ₁,τ₂,…} with SoD(τᵢ ⟂ τⱼ) ⊢ no single **Role Description** fuses τᵢ,τⱼ`
*Reading:* Separation‑of‑Duties is a **normative constraint**, not a label tweak (F.14).

**SCR‑F15‑S16 (Binding coherence).**
`Service‑Acceptance binding references Status Σ and Execution E ⊢ Σ anchored; E anchored; comparison defined via Bridge(s) if Cross‑context`
*Reading:* Acceptance compares **anchored** executions and statuses, with any Cross‑context step made explicit (F.12 + F.9).

> **SCR/RSCR “Twin Harness” tests**

**SCR‑TWIN‑01 - Head term check.** Plain twin preserves/declares the head per **CC‑TWIN‑3**.  
**SCR‑TWIN‑02 - Kind check.** Plain twin maps to the same **Kind** as the Tech name (C.3).  
**SCR‑TWIN‑03 - SenseCell check.** Twin and Tech resolve to the same **SenseCell**; record counter‑example(s).  
**SCR‑TWIN‑04 - Stop‑list check.** If the base noun is in the **Ambiguity stop‑list**, require bracketed head + gloss or **fail**.  
**SCR‑TWIN‑05 - Normative surface check.** No plain twins in CC blocks, signatures, or acceptance clauses.  
**RSCR‑TWIN‑06 - Drift audit.** On Context or glossary edits, re‑run twin harness; degrade or deprecate if SenseFidelity falls.  
**RSCR‑TWIN‑07 - Bridge audit.** If a twin is copied across Contexts, ensure a **Bridge** exists; record **CL** and loss notes.

 > **Examples & Anti‑examples**

**Good (role with head):**
* Tech: `TransformerRole` → Plain: **“Transformer (role)”** — passes Head & Kind checks.
*  Tech: `IncidentCommanderRole` → Plain: **“Incident commander (role)”**.

**Good (episteme status with head):**
* Tech: `U.EvidenceRole` → Plain: **“Evidence (status)”** — first mention includes head.

**Borderline (allowed with gloss):**
* Tech: `U.Episteme` → Plain: **“Tradition (episteme)”** — **only** with first‑use gloss, e.g., _“Tradition (episteme) \[U.Episteme\] — a body of knowledge within IAU\_2006”_. (Without the head/gloss this is **forbidden** due to ambiguity.) 

**Forbidden:**
* Tech: `U.Episteme` → Plain: **“Tradition”** (bare) — fails **CC‑TWIN‑4/5**.
* Tech: `U.PromiseContent` → Plain: **“API”** — fails Kind and head checks (API is an access **method**, not the **promise**).
* Tech: `U.RoleAssignment` → Plain: **“Appointment”** — banned term; conflates governance speech‑act with the binding object.

> **Migration guidance (lightweight)**
1.  **Inventory.** List current plain twins per Context.
2.  **Score.** Assign **SenseFidelity** (0–3) and add counter‑examples; demote or deprecate any with score <2.
3.  **Head & gloss.** Add bracketed heads and first‑use glosses for all surviving twins.
4.  **Register.** Create/update entries in **E.10.P**; link a **DRR** for each change.
5.  **Lint.** Enable the **Twin Harness** in CI to block new ambiguous twins.

### F.15:10 - Judgement schemas (core moves)

> Representative mental moves; each “fires” one cluster of SCRs.

1. **Anchoring**
   `Seed σ : context C, C ∈ Contexts(L) ⊢ anchored(σ)`  *(S1)*

2. **Local clustering**
   `∀σ∈Σ: context(σ)=C ⊢ cluster_C(Σ) = Local‑Sense λ`  *(S3)*

3. **Role-Description anchoring**
   `Role Description τ names ⟨C,λ⟩ ⊢ singleCell(τ)`  *(S7)*

4. **Row reuse**
   `intent(ρ') ≈ intent(ρ) ⊢ reuse(ρ) ∨ justify_mint(ρ')`  *(S11)*

5. **Bridge assertion**
   `C₁≠C₂ ∧ compare(⟨C₁,λ₁⟩,⟨C₂,λ₂⟩) ⊢ Bridge(CL,kind,loss)`  *(S12–S13)*

6. **Windowing**
   `Status Σ exhibits temporal/scale variance ⊢ define windows(Σ); forbid Σ‑splitting`  *(S14)*

7. **SoD guard**
  `SoD(τᵢ ⟂ τⱼ) ⊢ ¬exists Role Description υ that conflates {τᵢ,τⱼ}`  *(S15)*


### F.15:11 - Micro‑witnesses (illustrative)

**11.1 Activity vs Task (PROV‑O ↔ IEC 61131‑3).**
Contexts: `PROV‑O (run)`, `IEC 61131‑3 (run)`.
Local‑Senses: *activity(prov)*, *task(iec)*.
*Fire:* S7 (**Role Description** “Execution” points to **one SenseCell**), S12 (Bridge: **overlap**, CL=2, loss: *IEC task may be cyclic; PROV activity need not be periodic*), S13 (Contexts differ), S14 (Status windows for compliance later, not new types).

**11.2 Service Acceptance (ITIL 4 ↔ SOSA/SSN).**
Contexts: `ITIL 4 (design)`, `SOSA/SSN (run)`.
Row: **Service‑Availability** with cells ⟨ITIL\:SLO availability⟩, ⟨SOSA\:observation of uptime⟩.
*Fire:* S9 (row spans ≥2 Contexts), S12 (Bridge kind: *measure-for-target*, CL=3, loss: *sampling bias*), S16 (binding coherence), **S-RoleDesc-SingleCell**.


### F.15:12 - Relations (with other patterns)

**Builds on:** E.10.D1 (Context semantics), F.1–F.14.
**Constrains:** Any addition to F.1–F.14 is **publish‑ready** only if all relevant **SCR** here evaluate **true** on its slice.
**Feed:** B.3 may use Bridge CL and loss notes to adjust assurance.

### F.15:13 - RSCR — Regression & Stability Rules (R‑Evo)

> These rules speak about **changes over time**. They are expressed as **judgement schemas** that compare two conceptual snapshots: `@t0` and `@t1`. No storage, no workflows—just content assertions.

**Notation.**
`X@t0` — object X before change • `X@t1` — after change • `Δ(X)=⟨…⟩` — described difference • `same(…) / new(…) / retired(…)` — conceptual status.


#### F.15:13.1 - Contexts & editions

**RSCR‑F15‑E1 (No silent replacement).**
`Context C@t0 : edition e0, C@t1 : edition e1, e1≠e0 ⊢ either newContext(C,e1) ∨ explicitRecency(C,e1)`
*Reading:* A new edition becomes a **new Context** if sense shifts; otherwise keep one context and mark recency. Never overwrite meaning.

**RSCR‑F15‑E2 (Trip‑wire carry‑over).**
`C@t1 derives from C@t0 ⊢ tripWires(C@t1) ⊇ review(tripWires(C@t0))`
*Reading:* Known confusions are re‑checked and re‑stated (or explicitly dropped with a sentence why).


#### F.15:13.2 - Local‑Senses & SenseCells

**RSCR‑F15‑E3 (Reconstitutable seeds).**
`Local‑Sense λ@t0, Δ(occurrences) → λ@t1 ⊢ λ@t1 still reconstructible from attestations@t1`
*Reading:* After changes in attestations, the Local‑Sense remains **auditably rebuildable**.

**RSCR‑F15‑E4 (No Cross‑context creep).**
`SenseCell ⟨C,λ⟩@t0 → @t1 ⊢ context(λ@t1)=C`
*Reading:* A SenseCell never migrates across Contexts through edits.


#### F.15:13.3 - Concept‑Set rows

**RSCR‑F15‑E5 (Row identity).**
`Row ρ@t0 with cells {⟨Cᵢ,λᵢ⟩} → ρ@t1 with {⟨Cᵢ,λᵢ'⟩} ⊢ ρ “same” iff intent(λᵢ')≈intent(λᵢ) ∀i`
*Reading:* A row is the **same** row only if each cell still means *the same thing* in its Context. Otherwise, mint a **new row** and retire the old (F.7–F.8).

**RSCR‑F15‑E6 (Row shrink‑before‑split).**
`ρ@t1 loses a cell due to edition split ⊢ prefer keep ρ@t0 + add new row ρ' rather than mutating ρ silently`
*Reading:* When a Context splits meaning, preserve history: **add** instead of rewriting.


#### F.15:13.4 - Role Descriptions (Role/Status)

**RSCR-F15-E7 (Single-cell continuity).**
`Role Description τ@t0 → τ@t1 ⊢ anchor(τ@t1)=one SenseCell ∧ (sameCell ∨ justifiedSwitch)`
*Reading:* A **Role Description** keeps pointing to **one** SenseCell; switching cells requires a **one-sentence** rationale tied to the row you reuse (F.4, F.8).

**RSCR-F15-E8 (Alias-then-rename).**
`name(τ@t0) → name(τ@t1) ⊢ create alias(name@t0→name@t1) unless semantics changed`
*Reading:* If only the **name** improves, create an **Alias** (F.13). If semantics change, **mint a new Role Description** instead.


#### F.15:13.5 - Bridges

**RSCR‑F15‑E9 (Re‑validate on movement).**
`Bridge β: ⟨⟨C₁,λ₁⟩ ↔ ⟨C₂,λ₂⟩, CL, loss⟩ @t0; any λᵢ mutates @t1 ⊢ β re‑examined; CL may drop; loss updated`
*Reading:* Any end‑cell change **forces** a fresh look; default is **more caution** (CL non‑increasing unless newly justified).

**RSCR‑F15‑E10 (No bridge drift to identity).**
`series of edits turns β(kind≠≡) → β(kind=≡) ⊢ require new witness set`
*Reading:* Equivalence (≡) is special: it needs a **fresh witness**; you cannot slide into ≡ by minor edits.


#### F.15:13.6 - Status windows & SoD

**RSCR‑F15‑E11 (Window stability).**
`Status family Σ windows@t0 → @t1 ⊢ window set changes only if variance‑of‑meaning is shown`
*Reading:* Add or remove windows **only** when meaning genuinely varies across time/scale—never for convenience (F.10).

**RSCR‑F15‑E12 (SoD invariance).**
`SoD(τᵢ ⟂ τⱼ) @t0 → @t1 ⊢ SoD preserved; no new Role Description conflates τᵢ,τⱼ`
*Reading:* Separation‑of‑Duties remains in force through changes (F.14).


### F.15:14 - Anti‑patterns the harness catches (and the fix)

| Code   | Anti‑pattern            | Symptom                                  | Why it breaks                         | Harness catch → Fix                                                                              |
| ------ | ----------------------- | ---------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **H1** | **Row‑of‑one**          | Row spans a single Context                  | No cross‑projection; fake unification | **S9** fails → either add the second cell or drop the row                                        |
| **H2** | **Bridge‑by‑name**      | “Same name” assumed across Contexts         | Imports meaning; hides loss           | **S12** missing → assert an explicit Bridge with CL+loss or withdraw the claim                   |
| **H3** | **Silent edition swap** | “BPMN” changed to 2.0 → 2.1 without note | Retcons past statements               | **E1** fails → mint a new Context or mark recency; never overwrite                                  |
| **H4** | **Locality blur**       | Local‑Sense mixes two Contexts              | Cross‑context clustering                 | **S3/S6** fail → split back by Context; keep per‑Context normal forms                                  |
| **H5** | **Window‑as‑type**      | New Status type for weekend vs weekday   | Type inflation; hides time stance     | **S14/E11** fail → represent as windows, not types                                               |
| **H6** | **SoD bypass**          | Bundle fuses mutually exclusive roles    | Hidden duty conflict                  | **S15/E12** fail → keep roles separate; use Bundle only as reuse map                             |
| **H7** | **Alias-as-merge**      | Alias used to smuggle semantic change    | Loses history; misleads readers       | **E8** fails → if semantics changed, mint new Role Description; keep old with alias note only for pure rename |
| **H8** | **CL optimism**         | Most Bridges set to high CL by default   | Over‑trust; brittle reuse             | **E9/E10** → demand witnesses; prefer conservative CL                                            |


### F.15:15 - Worked “dry‑runs” (composite slices)

> Each dry‑run shows **how the checks fire** when something evolves. These are **thinking rehearsals**, not procedures.

#### F.15:15.1 - New edition of ITIL (services) arrives

**Slice.** Contexts: ITIL 4(2020)@t0 → ITIL 4(2024)@t1; Row: *Service-Availability*; **Role Description**: `AvailabilityStatus`; Bridges: to SOSA/SSN observations.

**Fire.**
E1 (**no silent replacement**): decide **new Context** ITIL 4(2024) because SLO definitions narrowed.
E5 (**row identity**): row *Service‑Availability*@t1 **new** (cells now ⟨ITIL2024\:SLO⟩ + ⟨SOSA\:obs⟩). Retire old row with note.
E9 (**bridge re‑validate**): sampling assumptions changed → **lower CL** by one and update loss note (*new calc window*).
E7 (**single-cell Role Description**): `AvailabilityStatus` still points to exactly one cell (ITIL2024\:SLO). Name unchanged → **no alias** needed.

**Pay‑off.** History is preserved; reuse remains safe; acceptance bindings (F.12) still compare anchored things.


#### F.15:15.2 - Rename a Role Description without changing meaning

**Slice.** **Role Description** `IncidentStatus`@t0 → `ServiceIncidentStatus`@t1; same SenseCell.

**Fire.**
E8 (**alias‑then‑rename**): create **Alias** `IncidentStatus → ServiceIncidentStatus` (F.13).
S8 (**name discipline**): new name fits the suffix rules (F.5).

**Pay‑off.** Readers find both names; semantics untouched.


#### F.15:15.3 - Tighten a Bridge (weak overlap → equivalence)

**Slice.** Bridge β between ⟨OWL\:subclass⟩ and ⟨FCA\:order‑edge⟩ was *overlap, CL=2*. New formal result proves equivalence in the covered fragment.

**Fire.**
E10 (**no drift to identity**): to move from overlap→≡, present a **new witness set** (fragment constraints).
S12 (**bridge explicit**): update β(kind=≡, CL=3) with precise scope/loss (“only within acyclic concept lattices with…”)

**Pay‑off.** Equivalence is **scoped and auditable**, not hand‑waved.


#### F.15:15.4 - Window misuse detected

**Slice.** Team proposes *PeakHoursAvailabilityStatus* as a new Status type.

**Fire.**
S14/E11 (**window honesty**): reject new type; define a **window** for *peak hours* on `AvailabilityStatus`.

**Pay‑off.** No type explosion; the evaluation logic in F.12 stays uniform.


### F.15:16 - Migration cues (conceptual)

1. **When in doubt, fork—not overwrite.** New edition? **Add a Context** unless you can argue sense identity in one sentence.
2. **Name pain → aliases, not merges.** If a label confuses, **rename with an alias**; if meaning changed, **mint new**.
3. **Rows age gracefully.** Never retrofit a row; **retire and re‑row** when any cell’s sense shifts.
4. **Bridges get colder over time.** Prefer to **lower CL** when editions drift; raising CL needs fresh witnesses.
5. **Windows absorb variation.** Resist splitting Status types; **window** by time/scale/phase.
6. **Guard SoD early.** When binding composite responsibilities (F.14), check SoD before naming.
7. **Teach the delta.** When things evolve, write one‑breath deltas (“what changed, why it matters”) as part of the example narrative—no registries implied.


### F.15:17 - Acceptance summary (“Harness green”)

A unification slice is **publish‑ready** when:

1. **All SCR (S‑Local & S‑Cross) hold** for the current snapshot (Contexts, Local‑Senses, SenseCells, rows, Role Descriptions, Bridges, windows).
2. **All RSCR (R‑Evo) hold** against the previous snapshot: no silent replacements; rows either unchanged or retired+reborn; Bridges re‑validated with CL non‑inflated without witnesses; windows adjusted only for real variance; SoD intact.
3. **One micro‑witness per moving part** exists in the text (tiny example showing the check in action).
4. **Memory rule still holds**: the active Context set for the line fits in a careful mind without external aids (F.1).


### F.15:18 - Didactic distillation (90‑second teaching script)

> “Use the harness to **think like a safety net**. First, the **SCR** threads: everything is **local** to a Context; **Role Descriptions** point to **one** SenseCell; rows actually **cross** Contexts; Bridges are explicit with CL and a loss note; windows capture variation without spawning new types. Then, the **RSCR** knots: never overwrite an edition—**fork the Context** or mark recency; keep rows stable by **retiring and re-rowing**; Bridges get **re-validated** (CL goes down unless you bring proof); renames become **aliases** unless meaning changes; **windows** absorb time/scale shifts; **SoD** stays intact. If you can pass these thoughts on a small slice—and explain each pass in **one breath**—your unification is green. No tooling, no roles, no dashboards. Just clean Contexts, honest rows, cautious bridges, and names that help minds meet.”

### F.15:End

## F.16 - Worked‑Example Template (Cross‑Domain)

**“Show the thought, not the tooling.”**
**Status.** Architectural pattern.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.1–F.15.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (CL on Bridges); Part C patterns (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL).


### F.16:1 - Intent & applicability

**Intent.** Provide a **single, didactic page template** for cross‑domain worked examples that makes every claim **local to a Context** (Context), every Cross‑context step **explicit via a Bridge**, and every named role/status **traceably tied** to one **SenseCell**. The template is **notation‑free** and **tool‑agnostic**; it captures **how to think** the example so others can replay it.

**Applicability.** Use whenever you illustrate **any** FPF construct that spans more than one Context: **Role Assignment & Enactment** bindings, acceptance checks, measurement-driven claims, type alignment, control/actuation stories, etc.

**Non‑goals.** No registries, workflows, editors, or storage formats; no step‑by‑step “team procedures.” This pattern shapes **the page a reader sees**, not how it was produced.


### F.16:2 - Problem frame

Cross‑domain examples often fail in four predictable ways:

1. **Global words.** *Process*, *role*, *service*, *execution* used without the Context, inviting drift.
2. **Hidden bridges.** “It’s basically the same” across disciplines, with losses left implicit.
3. **Name without sense.** A **Role Description** name appears with no visible tie to a SenseCell.
4. **List without structure.** Facts line up but never meet in a single **Concept‑Set row**.

The template counters these by forcing **Contexts → senses → row → bridges**, in that order.


### F.16:3 - Core idea (didactic)

A robust worked example is a **compact theatre**:

* **Stage** = a declared **unification line** (which threads of Part C are in play).
* **Backdrop** = **Context set** (Contexts from F.1), each with a one‑line Card.
* **Actors** = **SenseCells** (⟨Context, Local‑Sense⟩) you will actually use.
* **Plot** = **one Concept‑Set row** where those cells stand as “the same thing” for this example.
* **Cues** = **Role Descriptions** that reference exactly one SenseCell each.
* **Cross‑talk** = **Bridges** across Contexts (with kind, CL, and loss).
* **Timing** = **Windows** (if status varies across time/scale) and **SoD** (if duties must remain separate).
* **Moral** = a handful of **harness checks** (F.15) that the reader can verify mentally.


### F.16:4 - Minimal vocabulary (this pattern only)

* **Context / Context** — always **U.BoundedContext** (E.10.D1).
* **Local‑Sense** — a sense clustered within one context (F.3).
* **SenseCell** — address `⟨Context, Local‑Sense⟩`.
* **Concept‑Set row (ρ)** — a Cross‑context alignment for “what we treat as one” in this example (F.7/F.8).
* **Role Description (τ)** — a Role or Status that **points to one SenseCell** (F.4–F.6).
* **Bridge (β)** — explicit Cross‑context relation with **kind** (≡ / overlaps / broader‑than / narrower‑than), **CL**, and **loss note** (F.9).
* **Window** — a bounded interval (time/scale/phase) tied to a Status (F.10).
* **SoD** — Separation-of-Duties constraint among **Roles** (F.14).


### F.16:5 - The one‑page **Worked‑Example Canvas**

> Each bullet is a **thought you make visible**, not a form field.

1. **Title & claim.** A short name + one‑sentence claim you will demonstrate.
   *Example:* *“Service Uptime as Evaluated by Runtime Executions”* — “We compare **Execution (IEC)** observations to **SLO (ITIL)** within a declared window.”

2. **Unification line.** Which Part C threads are active.
   *Example:* *Enactment + KD‑CAL (sensing) + Sys‑CAL (execution).*

3. **Context set (compact Cards).** 3–6 Contexts from F.1 with one‑line scope and, if inherent, **design vs run** stance.
   *Example:* *BPMN 2.0 (design: workflow graph); PROV‑O (run: Activity uses/generates); ITIL 4 (design: SLO/SLA); SOSA/SSN (run: Observation); IEC 61131‑3 (run: task executes).*

4. **SenseCells in play.** List exactly the **Local‑Senses** you will use, each prefixed by its Context.
   *Example:* ⟨**ITIL**: service‑level‑objective⟩, ⟨**SOSA**: observation⟩, ⟨**IEC**: execution‑task⟩, ⟨**PROV**: activity⟩.

5. **The Concept‑Set row (ρ).** A **single line** that places the cells you treat as “the same” for the claim, with a one‑breath justification.
   *Example row ρ:* { ⟨ITIL\:SLO⟩ ↔ ⟨SOSA\:observed‑availability⟩ } — *We treat “target availability” and “observed availability” as comparable magnitudes in a specific window.*

6. **Bridges (β).** For any Cross‑context relation **not captured by ρ** (or that requires nuance), state **kind, CL, loss**.
   *Example β₁:* ⟨**IEC\:execution‑task**⟩ **overlaps** ⟨**PROV\:activity**⟩, **CL=2**, *loss:* PROV lacks cyclic scheduling semantics.
   *Example β₂:* ⟨**SOSA\:observation**⟩ **narrower‑than** ⟨**ITIL\:measurement**⟩, **CL=2**, *loss:* ITIL omits procedure metadata.

7. **Role-Description hooks.** Name the Role/Status templates and the **one SenseCell** each references.
   *Example:* `AvailabilityStatus` → ⟨ITIL\:SLO⟩; `Execution` → ⟨IEC\:execution‑task⟩; `EvidenceObservation` → ⟨SOSA\:observation⟩.

8. **Windows & SoD (if relevant).** Spell any **status windows** and any **SoD** you rely on.
   *Example:* Window: *monthly, business‑hours*; SoD: *Operator* ⟂ *SLO‑Owner*.

9. **Micro‑narrative (5–7 lines).** Walk the reader through the claim using **Context‑prefixed words** and the row/bridges above.
   *Example (abridged):* “A **task (IEC)** runs the control program. Its **observations (SOSA)** yield availability over the *monthly* window. We compare those to the **SLO (ITIL)** in the same window. Where we refer to **activity (PROV)** we do so via **β₁** (overlap, CL=2). The row ρ is the locus of comparison; the Bridge **β₂** explains why ‘measurement’ in ITIL is broader than ‘observation’ in SOSA.”

**Harness pings (F.15).** *S-Row-Cross*, **S-RoleDesc-SingleCell**, *E-NoSilentEdition*.
    *Example:* *S‑Row‑Cross*, *S‑RoleDescription‑SingleCell*, *E‑NoSilentEdition*.

> **Memory rule.** If your Canvas cannot fit on a single page (or one slide), the example is teaching the wrong thing.


### F.16:6 - Invariants (normative)

1. **Locality of meaning.** Every term in the narrative appears **with its Context** at first mention (*process (BPMN)*, *activity (PROV)*, …).
2. **At least one row.** The example **MUST** include ≥ 1 **Concept‑Set row** spanning ≥ 2 Contexts.
3. **Single-cell Role Description.** Every **Role Description** in the example **MUST** point to **one** SenseCell.
4. **Explicit bridges.** Any Cross‑context step **not explained by the row** **MUST** appear as a **Bridge** with kind, CL, and loss.
5. **Temporal honesty.** If a Context fixes **design vs run**, the narrative respects it.
6. **Window discipline.** If comparison depends on time/scale/phase, a **window** is stated rather than minting a new Status type.
7. **SoD integrity.** If duties are involved, **SoD** is explicit and unbroken.
8. **Didactic parsimony.** One page, one claim, one row (or a tiny bundle of closely related rows).


### F.16:7 - The row panel (how to show it without notation)

Show the row as a **compact two‑to‑five‑column list**:

* **Column header** = Context.
* **Cell** = `Local‑Sense label` (tech register; optional plain label on next line).
* **Footline** (one line) = “row reason”—why these cells count as “the same thing **for this claim**.”

*Example visual (linear text):*
**ITIL 4:** *service‑level‑objective* | **SOSA/SSN:** *observed‑availability* → **Row reason:** *both quantify availability for the same window; units harmonised by KD‑CAL; procedural metadata differs (captured in loss of β₂).*


### F.16:8 - Worked micro‑example (didactic)

> **Title.** *Alarms Should Not Satisfy Uptime*
> **Claim.** An **alarm‑only Execution (IEC)** cannot satisfy the **SLO (ITIL)** because **observation (SOSA)** windows exclude time in “alarm state.”

**Contexts.** IEC 61131‑3 (run), SOSA/SSN (run), ITIL 4 (design).
**SenseCells.** ⟨IEC\:execution‑task⟩, ⟨SOSA\:observation⟩, ⟨ITIL\:SLO⟩.
**Row ρ.** { ⟨ITIL\:uptime‑SLO⟩ ↔ ⟨SOSA\:observed‑availability⟩ } — comparable magnitudes in the *calendar‑month* window.
**Bridge β.** ⟨IEC\:alarm‑state⟩ **narrower‑than** ⟨SOSA\:observation‑qualifier⟩, **CL=2**, *loss:* SOSA does not prescribe plant‑specific alarm semantics.
**Role-Description hooks.** `AvailabilityStatus` → ⟨ITIL\:SLO⟩; `EvidenceObservation` → ⟨SOSA\:observation⟩.
**Window.** *Calendar month, business‑hours*, exclusion: *alarm‑state intervals*.
**Micro‑narrative (4 lines).** A **task (IEC)** runs; when the plant is in **alarm state**, **observations (SOSA)** are flagged and **excluded** from the availability window. We then compare the remaining interval to the **SLO (ITIL)** via row ρ. The Bridge β clarifies why the flag is a **qualifier** in SOSA, not a Status type in ITIL.
**Harness pings.** *S‑Row‑Cross*, *S‑RoleDescr‑SingleCell*, *S‑Window*, *S‑TemporalHonesty*.


### F.16:9 - Relations (with other patterns)

**Builds on:**
F.1 (Contexts), F.2–F.3 (terms & senses), F.4–F.6 (roles), F.7–F.8 (rows), F.9 (bridges), F.10 (windows), F.14 (SoD), F.15 (harness).

**Constrains:**
Any example placed in Part C or Part B **must** render its claim through this canvas (or a faithful reduction), so readers can run F.15 mentally.


### F.16:10 - Didactic distillation (60‑second script)

> “A good cross‑domain example fits on **one page**. First, name the **claim**. Then show the **Contexts** you’re using. List the **SenseCells** you will actually touch. Draw **one row** that makes them the same **for this claim**. Every Cross‑context nuance you can’t justify in that row becomes a **Bridge** with a **kind**, a **CL**, and a **loss** sentence. Point each **Role Description** to **one** cell. If time/scale matters, state the **window**; if duties matter, state **SoD**. Finish with two or three **harness pings** from F.15. That’s it—no tooling, no long procedures. The reader can now replay your thought and agree (or disagree) at the right place.”

### F.16:11 - Anti‑patterns & remedies

| #         | Anti‑pattern               | Symptom in the page                                            | Why it breaks thinking                                         | Remedy (point to this template & sibling patterns)                        |
| --------- | -------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **AP‑1**  | **Row‑less tour**          | A list of facts from many Contexts with no **Concept‑Set row**.   | Reader cannot see *what is treated as the same* for the claim. | Include **≥ 1 row ρ** spanning ≥ 2 Contexts (§5‑5, §6‑2).                    |
| **AP‑2**  | **Stealth bridging**       | Phrases like “basically the same” with no Bridge.              | Imports meaning Cross‑context; hides losses.                      | State a **Bridge β** with **kind, CL, loss** (§5‑6, F.9).                 |
| **AP-3**  | **Role-Description vagueness**          | A Role/Status named without a SenseCell.                       | Why it breaks thinking                                         | Remedy (point to this template & sibling patterns)                        |
| **AP‑4**  | **Global words**           | *process, role, service* appear unprefixed.                    | Context‑less words drift mid‑example.                             | Prefix first mention with the **Context** (*process (BPMN)*) (§6‑1, E.10.D1). |
| **AP‑5**  | **Window‑free comparison** | Numbers/targets compared with no stated window.                | Apples‑to‑oranges across time/scale.                           | Declare a **Window** for the Status (§5‑8, F.10).                         |
| **AP‑6**  | **SoD leakage**            | Duties named but the same actor implicitly holds both.         | Violates Separation‑of‑Duties intent.                          | State **SoD** and keep duties disjoint (§5‑8, F.14).                      |
| **AP‑7**  | **Design/run blur**        | A design‑time notion used as if it were a run‑time occurrence. | Category error; wrong Context claims.                             | Mark Context stance and keep claims in‑stance (§5‑3, §6‑5).                  |
| **AP‑8**  | **Edition haze**           | “BPMN”, “ITIL” without edition/profile.                        | Debates about “what the book says”.                            | Put **name + edition** on each Card (§5‑3).                               |
| **AP‑9**  | **CL silence**             | Bridge kind given, no CL or loss note.                         | Reader cannot assess translation risk.                          | Add **CL** and **loss** in every Bridge (§5‑6, B.3).                      |
| **AP‑10** | **Over‑row**               | Ten cells glued into one row “for convenience”.                | Collapses distinct senses; unreadable.                         | Prefer **one tight row**; split into **two rows** if needed (§5‑5, §8).   |


### F.16:12 - Extended worked micro‑examples

> Each example fits the **one‑page canvas** (§5) and makes the **row** and **bridges** do the work.

#### F.16:12.1 - Type alignment: OWL class vs FCA concept (design‑time only)

**Title & claim.** *“Two Lenses on *Pump*: OWL class and FCA concept align for catalogue reasoning.”*
**Unification line.** Kind-CAL (design) + FCA (design).
**Contexts.** **OWL 2 (profiles)** — classes, `subClassOf` (design). **FCA corpus** — formal concepts, lattice order (design).
**SenseCells.** ⟨OWL\:class ‘Pump’⟩, ⟨FCA\:formal‑concept ‘Pump’⟩.
**Row ρ.** { ⟨OWL\:Pump⟩ ↔ ⟨FCA\:Pump⟩ } — *same practical extension in this product catalogue*.
**Bridge β.** ⟨FCA\:lattice‑order⟩ **overlaps** ⟨OWL\:subclass‑order⟩, **CL=2**, *loss:* FCA intents may include context attributes not modeled in OWL restrictions.
**Role-Description hooks.** `TypeLabel` → ⟨OWL\:class⟩ (for naming), no runtime **Role Assignment/Enactment**.
**Micro‑narrative (3 lines).** For catalogue queries, the **instances** covered by OWL class *Pump* match those of the FCA concept created from the same attributes; we treat them as one row. The **orderings** diverge in nuance (β), but not for membership in this example.
**Harness pings.** *S‑Row‑Cross*, *S‑TemporalHonesty* (design only), *S‑Bridge‑Kind‑CL*.


#### F.16:12.2 - Role vs permission: SoD in enactment vs access control

**Title & claim.** *“Behavioral role (BPMN) is disjoint from access role (RBAC); keep duties separate.”*
**Unification line.** Role Assignmnent and Enactment (design & run) + access/deontics (design).
**Contexts.** **BPMN 2.0** — participant/lanes (design). **NIST RBAC (2004)** — roles/permissions (design).
**SenseCells.** ⟨BPMN\:participant⟩, ⟨RBAC\:role⟩.
**Row ρ.** — *(intentionally none)* — we do **not** treat them as the same.
**Bridge β.** ⟨BPMN\:participant⟩ **disjoint** ⟨RBAC\:role⟩, **CL=3**, *loss:* none—*different dimensions* (behavioral mask vs permission grouping).
**Role-Description hooks.** `Operator` → ⟨BPMN\:participant⟩; `AccessRole` → ⟨RBAC\:role⟩. **SoD:** `Operator` ⟂ `AccessRole‑Admin`.
**Window.** Not applicable.
**Micro‑narrative (3 lines).** We show SoD by prohibiting the same actor from holding **Operator** and **AccessRole‑Admin**. The disjoint **β** prevents leakage between behavioral masks and permission bundles.
**Harness pings.** *S‑RoleDescr‑SingleCell*, *S‑SoD*, *S‑Bridge‑Disjoint*.


#### F.16:12.3 - Method quartet: from MethodDescription to Work with observations

**Title & claim.** *“Behavioral role (BPMN) is disjoint from access role (RBAC); keep duties separate.”*
**Unification line.** **Role Assignment & Enactment** (design & run) + access/deontics (design).
**Contexts.** **SPEM 2.0** (design: Method/MethodDescription), **PROV‑O** (run: Activity), **SOSA/SSN** (run: Observation), **ITIL 4** (design: SLO).
**SenseCells.** ⟨SPEM\:MethodDescription⟩, ⟨PROV\:activity⟩, ⟨SOSA\:observation⟩, ⟨ITIL\:SLO⟩.
**Row ρ.** { ⟨ITIL\:SLO\:build‑time⟩ ↔ ⟨SOSA\:observed‑build‑duration⟩ } — *compare promised vs observed duration on the same window*.
**Bridges.** β₁: ⟨SPEM\:MethodDescription⟩ **narrower‑than** ⟨PROV\:activity‑plan⟩, **CL=2**, *loss:* PROV lacks prescriptive structure; β₂: ⟨SOSA\:observation⟩ **narrower‑than** ⟨ITIL\:measurement⟩, **CL=2**, *loss:* ITIL abstracts from procedure.
**Role-Description hooks.** `Operator` → ⟨BPMN\:participant⟩; `AccessRole` → ⟨RBAC\:role⟩. **SoD:** `Operator` ⟂ `AccessRole-Admin`.
**Window.** *Release window: calendar week*.
**Micro‑narrative (4 lines).** The **MethodDescription (SPEM)** implies a target **build‑time**; **Work (PROV activity)** occurs; **observations (SOSA)** provide actuals; we compare against the **SLO (ITIL)** via row ρ over the *calendar week* window. Bridges β₁–β₂ explain why plan/measure semantics do not collapse.
**Harness pings.** *S‑Row‑Cross*, *S‑Window*, *S‑RoleDesc‑SingleCell*, *S‑TemporalHonesty*.


### F.16:13 - Reasoning primitives (judgement schemas)

> These are **mental checks** you can perform on any example page.

1. **Row validity**
   `cells(ρ) = {⟨Cᵢ,Sᵢ⟩} with |Contexts(ρ)| ≥ 2 ⊢ validRow(ρ)`
   *Reading:* A row is valid only if it spans at least two Contexts and all entries are legitimate **SenseCells** (from F.3).

2. **Bridge coverage**
   `coRef(Ca,Cb) ∧ ¬sameRow(Ca,Cb) ⊢ requires β(Ca↔Cb)`
   *Reading:* If two Contexts are co‑referenced in the narrative but their senses are not placed in the same row, an explicit **Bridge** is needed.

3. **Role-Description single-cell**
   `Role Description τ used ⊢ ∃!⟨C,S⟩ : ref(τ)=⟨C,S⟩`

4. **Window sufficiency**
   `compare(qᵢ@Cᵢ, qⱼ@Cⱼ) ⊢ windowDeclared`
   *Reading:* Any Cross‑context quantitative comparison calls for a stated **Window**.

5. **Temporal honesty**
   `C has stance s ∈ {design, run} ⊢ claims@C must respect s`
   *Reading:* Do not assert run‑facts in a design‑only Context, or vice versa.

6. **SoD integrity**
   `SoD(D₁ ⟂ D₂) ∧ assign(actor, D₁) ∧ assign(actor, D₂) ⊢ violation`
   *Reading:* A declared SoD cannot be violated inside the example.

7. **Bridge clarity**
   `β given ⊢ kind(β) ∧ CL(β) ∧ loss(β)`
   *Reading:* Every Bridge shows **kind**, **CL**, and a **one‑line loss**.

8. **Edition clarity**
   `card(C) ⊢ has(name, edition)`
   *Reading:* Each Context Card specifies name + edition/profile.

9. **Harness ping mapping**
   `ping ∈ {S‑*, E‑*} ⊢ ping ⇒ subset of judgements above`
   *Reading:* Each named harness check (F.15) has a clear reading in these judgements.


### F.16:14 - Acceptance tests (SCR/RSCR)

#### F.16:14.1 - Static conformance (SCR)

* **SCR‑F16‑S01 (Row present).** The page contains **≥ 1** Concept‑Set row spanning **≥ 2 Contexts**.
* **SCR‑F16‑S02 (Bridge explicit).** Every Cross‑context assertion not justified by a row is shown as a **Bridge** with **kind, CL, loss**.
* **SCR-F16-S03 (Role-Description anchoring).** Each **Role Description** appearing in the page references **exactly one SenseCell**.
* **SCR‑F16‑S04 (Context prefixes).** First mention of each ambiguous term is **Context‑prefixed**.
* **SCR‑F16‑S05 (Window discipline).** Any numeric comparison across Contexts names a **Window**.
* **SCR‑F16‑S06 (DesignRunTag).** Claims respect each Context’s **design/run** stance.
* **SCR‑F16‑S07 (SoD).** If duties are named and SoD is relevant, **SoD is stated** and unviolated.
* **SCR‑F16‑S08 (One‑page parsimony).** The example fits the **one‑page canvas**; if extended, each sub‑page still respects §6 invariants.

#### F.16:14.2 - Regression (RSCR)

* **RSCR‑F16‑E01 (Edition drift).** When a Context’s edition changes, the example either (a) is unaffected or (b) adds a note adjusting **β** or the **row**; no silent rewrites.
* **RSCR‑F16‑E02 (Bridge re‑score).** If an upstream **CL** definition changes (B.3), affected Bridges on the page show the new CL and, if needed, an updated **loss** sentence.
* **RSCR‑F16‑E03 (Row resilience).** If a SenseCell is split in F.3 (sense refinement), the example either keeps the same row using one child sense, or splits into two rows with a short justification.
* **RSCR‑F16‑E04 (Window clarity).** If organisational cadence changes (e.g., from monthly to weekly), windows on the page are updated explicitly.


### F.16:15 - Migration notes (conceptual)

1. **Refactor long tutorials.** Extract the **claim**; pick **3–6 Contexts** (Cards); list the **SenseCells** you actually use; craft **one tight row**; surface any cross‑talk as **Bridges** with loss notes; delete everything else.
2. **Split crowded rows.** If a row tries to carry more than \~4 cells, split into two rows and write a **one‑line purpose** for each.
3. **Stabilise vocabulary.** If you find yourself rewriting terms mid‑page, you likely forgot a Context; return to F.1 and add a Card.
4. **Teach the bridge itch.** Leave “*these are the same*” feelings ungratified until you can articulate **kind, CL, loss** in one sentence.
5. **DesignRunTag respect.** If a design‑only Context tempts you into runtime talk, move that part of the narrative into a **run‑Context** and Bridge as needed.
6. **Keep the page living.** When upstream rows/bridges evolve (F.7–F.9), adjust the page *minimally* and call out the change in a margin note (conceptual, not procedural).


### F.16:16 - Teaching variants (all obey §6 invariants)

* **Two‑Context equivalence.** Smallest case: 1 row, 2 Contexts, **β (≡, CL=3)** to explain why they’re truly the same *for this claim*.
* **Triangulation.** 1 row, 3 Contexts; typical for *measurement ↔ service ↔ execution*.
* **Disjointness lesson.** No row; one **β (disjoint)** plus a short SoD story.
* **Window primer.** Same sense across Contexts but different default windows; the page is about the **window choice**, not the term.


### F.16:17 - Didactic checklist (author’s quick scan)

* One sentence **claim**?
* **Contexts** (with editions) visible?
* **SenseCells** named (tech & plain labels acceptable)?
* **Exactly one** tight **row** (or two, each justified)?
* All Cross‑context steps shown as **β(kind, CL, loss)**?
* **Role Description → one SenseCell** each?
* **Window** present where numbers meet?
* **SoD** stated where duties appear?
* Page fits a **single view**?


### F.16:18 - Closing distillation (30‑second echo)

> A strong worked example is a **one‑page alignment**: claim → Contexts → cells → **one row** → explicit **bridges** → Role-Description hooks → window/SoD if needed. No tooling, no process charts—just **visible thinking** that any careful reader can replay and critique at the right place.

### F.16:End


## F.17 - Unified Term Sheet (UTS)

**“One table that a careful mind can hold.”**
**Status.** Architectural pattern.
**Builds on:** F.1–F.3 (Contexts → seeds → local senses), F.4 (Role Characterisation), F.5 (Naming), F.7 (Concept‑Set table), F.8 (Mint/Reuse decision), F.9 (Bridges), F.10–F.12 (Status & method/service bindings), F.15 (SCR/RSCR).
**Coordinates with:** A.1.1 `U.BoundedContext`, A.7 **Strict Distinction**, A.8 **Heterogeneity**, A.11 **Ontological Parsimony**, A.15 **Role–Method–Work Alignment**.
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No “data pipeline.” This pattern prescribes **what a UTS is** and **how to judge it**, not how to generate files.

### F.17:1 - Intent & Applicability

**Intent.** Provide a **single, normative table**—the **Unified Term Sheet (UTS)**—that distils the output of F.1–F.12 into **human‑readable rows**. Each row expresses **one Concept‑Set** unified into **one FPF U.Type** with its **Tech/Plain names** and **cross‑context senses**. The UTS is the *front‑door view* that authors, engineers, and managers use; it replaces scattered notes and eliminates guesswork.

**Applicability.** Produce a UTS **per FPF pattern thread** (e.g., *Role Assignment & Enactment*, *Method quartet*, *Trust & Evidence*). Use it:

* to **name** U.Types and their **Tech/Plain** labels (F.5),
* to **teach** the mapping from familiar canons to unified concepts,
* to **audit** coverage and heterogeneity (A.8), and
* to **feed** examples in Parts A/C without re‑explaining terminology.

**Why now.** Earlier F‑patterns define *how to think*. **F.17** defines *what you publish* so others can think with you.

### F.17:2 - Problem Frame

Without a single sheet:

1. **Locality is lost.** Mappings hide in prose; readers re‑globalise words.
2. **Naming drifts.** Teams adopt ad‑hoc labels that collide later.
3. **Coverage is opaque.** No quick check that coverage spans **≥ 3 domain families** across the sheet (A.8).
4. **Didactic load spikes.** Each section re‑teaches the same terms.

**UTS** fixes this by putting the **unification decision** and the **cross‑context evidence** on **one line** per concept.


### F.17:3 - Forces

| Force                             | Constraint in UTS                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Didactic primacy vs. fidelity** | UTS keeps **two names** (Tech/Plain) and **one‑line rationale**, but never misstates a source meaning.              |
| **Parsimony vs. recall**          | Each row is one concept; the UTS as a whole demonstrates heterogeneity across ≥ 3 domain families (A.8). Rows may cite fewer Contexts when the concept truly appears in fewer.                   |
| **Locality vs. comparability**    | Senses are **Context‑scoped** (E.10.D1). Cross‑context relations are shown only as **explicit bridges** (F.9) with **CL**. |
| **General usability**             | Sheet must be **legible on paper** and **memorisable** (block structure, stable row order).                         |


### F.17:4 - Core Idea

**A UTS is a Concept‑Set table with names.**
Each **row** = one **Concept‑Set** unified into one **FPF U.Type** (the “what we mean”).
Each **column family** shows **how this concept appears** in the chosen **contexts of meaning** (F.1).

Two **canonical layouts** are allowed (pick one or publish both):

* **Layout A — Kernel‑first**: rows keyed by **FPF U.Type**; **Bounded‑Context Columns (BCC)**.
* **Layout B — Base‑concept**: rows keyed by **Base concept** (EN/RU) of a discipline, then unified to **U.Type**; **Discipline Columns (DC)**.

Both layouts are normative; choose based on audience. In Layout A, comparability is by **BCC** (*Bounded‑Context Column*); in Layout B, comparability is by **DC** (*Discipline Column*); never conflate the two.

### F.17:5 - Minimal Vocabulary (for this pattern)

* **UTS (Unified Term Sheet).** The published, human‑readable table per thread.
* **Context.** Alias in Tech register for **`U.BoundedContext`** (E.10.D1). Normative unit of meaning; every SenseCell is scoped to a Context _(name + edition)._  
* **Bounded‑Context Column (BCC).** A didactic column used **only in Layout A**; one column per **Context (`U.BoundedContext`)** from the F.1 cut; **not a model element**; the **header includes the Context name + edition**.  
* **Discipline Column (DC).** A _discipline vantage_ used **only in Layout B** (e.g., _Operational Management_, _IT/Software_, _Physics_). A DC is **not** a **Bounded‑Context Column** and does not carry editions.  
* **Concept‑Set (CSR).** One unified concept with pointers to its SenseCells.  
* **SenseCell.** _(Context × Local‑Sense)_ address—how a Context “says that thing”.  
* **Bridge / CL.** Explicit cross‑context mapping (F.9) with Congruence Level and Loss note.
* **Plain Twin (LEX).** The LEX record pairing the **Unified Tech name** with its **Unified Plain name** for a U.Type; governed by **PTG** and referenced by `Twin‑Map Id (LEX)` (E.10 LEX‑BUNDLE).
* **Block Plan.** Didactic grouping of rows to keep the sheet memorizable.  
* **Unified Tech name / Unified Plain name.** Dual‑register names chosen per F.5; the **Tech name is the neutral, unified term** for the U.Type, not a borrowed Context name.

> **Discipline.** “Context” always means **`U.BoundedContext`** (E.10.D1). No global words.

### F.17:6 - Row Schema (normative)

Every UTS row **MUST** carry the following fields (verbatim headings recommended):

| Field                     | Purpose                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| **# / Block**             | Stable id and didactic block (see §7).                                                                |
| **FPF U.Type**            | Canonical kernel type (e.g., `U.Work`).                                                               |
| **Unified Tech name**     | Short technical name used in spec prose (F.5).                                                        |
| **Unified Plain name**    | Everyday name for non‑specialists (F.5).                                                              |
| **Plain‑Twin Governance (PTG) (optional)** | Stance for the Unified Plain twin: {**Strict**, **Guarded**, **Provisional**}; use when additional discipline of the Plain twin is required (E.10 LEX‑BUNDLE). |
| **Twin‑Map Id (LEX) (optional)** | Identifier of the Tech↔Plain twin record in the LEX‑BUNDLE; cite when `PTG ≠ Strict` or when multiple candidate twins exist. |
| **FPF Description**       | One‑line definitional gist (no examples).                                                             |
| **SenseCells (by context)** | Per selected Context: the local term(s) or construct that best realises the concept (one cell per Context). |
| **Bridges (CL/Loss)**     | For any cross‑context relation, record the F.9 Bridge with **CL** and a 2–6‑word loss note; if identity, mark **CL=3 (identity)**. |
| **Unification Rationale** | One sentence: why these senses are the same *conceptually*.                                           |
| **Notes (optional)**      | Brief DesignRunTag or trip‑wire hints (e.g., “design vs run”).                                     |

**Constraint.** “SenseCells (by **Context**)” **MUST** cite **at least three** distinct **Contexts** overall across the sheet for the thread (A.8). A single row may show fewer if the concept truly appears in fewer contexts; coverage is a property of the whole UTS.

**Discipline:** Every SenseCell **must** cite the **Context name + edition** (e.g., _“BPMN 2.0 (2011): Activity instance”_).

#### F.17:6.1 - NQD Fields (normative; when applicable)

If a UTS row **describes** a **Generator/Selector/Portfolio** (design‑time or run‑time artefact), it **MUST** add the following fields. These are *publication* fields, not tooling‑specific formats.

| Field | Purpose |
| --- | --- |
| **N (Novelty)** | Lawful novelty claim tied to `CharacteristicSpaceRef` + `DistanceDefRef` (declare metric/pseudometric & invariances; cite edition ids). |
| **U (Use‑Value)** | Declared acceptance/test value under the active **CG‑Frame** (units & scale typed per MM‑CHR). |
| **C (ConstraintFit)** | Feasibility against **ResourceEnvelope/RiskEnvelope** (and relevant deontic/ethics clauses); no `unknown→0` coercion. |
| **D\_P (Portfolio Diversity)** | Diversity contribution relative to the **current PortfolioPack** (`ArchiveConfig`, grid/binning, K‑capacity, dedup). |
| **E/E‑LOG policy‑id (PolicyIdRef)** | Edition id of the explore/exploit governor policy that governed generation/selection budgets. |

**Note.** These fields *extend* the Row Schema; they do not change SenseCells/Bridges/Names. Rows that are *purely definitional* (no generator/selector/portfolio semantics) do not carry §6.1.

#### F.17:6.2 - Autonomy fields (when applicable)
Add the following columns (nullable; **required** when autonomy is claimed by the row’s subject):
* `AutonomyBudgetDeclRef` (id, version)
* `Aut-Guard policy-id (PolicyIdRef)`
* `OverrideProtocolRef`
* `Scope (G)` (autonomy scope)
* `Γ_time` (admission window selector)
* *(optional)* `ScaleLensPolicyRef`
* *(optional)* `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`
**Note.** These fields are required for UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy claims; optional fields make **Bitter‑Lesson/Scale‑Lens** an explicit **opt‑in** with published criteria.

### F.17:7 - Block Plan (didactic grouping)

A UTS **MUST** declare a **Block Plan**—the sequence of blocks that group rows. Blocks are **thread‑specific**. Example **Block Plan** for *Role Assignment & Enactment* (matches your earlier tables):

* **Block A - Context & Roles** — `U.BoundedContext`, `U.Role`, `U.RoleAssignment`, `U.Capability`.
* **Block B - Method & Description** — `U.Method`, `U.MethodDescription`, Access/Acceptance descriptions (fields of `U.PromiseContent`).
* **Block C - Execution & Schedule** — `U.Work`, `U.WorkDescription`, `U.Observation`.
* **Block D - Service & Deontics** — `U.PromiseContent`, `U.SpeechAct`, `U.Commitment`, `U.PromiseContent`, `U.PromiseFulfillmentEvaluation`.
* **Block E - Carriers & Bridges** — `U.Carrier`, *Alignment (Bridge entry)*.
* **Block R - Knowledge Units & Statuses** — `U.Episteme`, `U.EvidenceRole`, `U.StandardStatus`, `U.RequirementStatus`, `U.DefinitionRole`, `U.AxiomaticCoreRole`.

> **Rule.** Block names are **didactic**, not ontological. Do **not** infer mereology or subtyping from blocks.

### F.17:8 - Column Families (two canonical layouts)

#### F.17:8.1 - Layout A — Kernel‑first (U.Type as rows)

**Columns:**

* `FPF U.Type - Unified Tech name - Unified Plain name - Plain‑Twin Governance (PTG) - Twin‑Map Id (LEX) - FPF Description` *(left rail; `PTG`/`LEX` are optional)*
* **Bounded‑Context Columns (BCC)** — one column per **Context (`U.BoundedContext`)** from the F.1 cut; each header shows _name + edition_: e.g., **OMG BPMN 2.0**, **W3C PROV‑O**, **ITIL 4**, **NIST RBAC**, **W3C SOSA/SSN**, **OMG Essence (Language)**, **DEMO/DEMO‑EO**, **PMBOK 7**, **CM/BPM (CMMN/BPMN)**, **IEC 61131‑3**, **ODRL 2.2**, **ISO 80000‑1 / Metrology** … *(your chosen 12 Contexts)*
* `Bridges (CL/Loss)`
* `Unification Rationale`
* `Notes`
  
Do not mix **Discipline Columns (DC)** in Layout A. Columns here are only **Bounded‑Context Columns (BCC)**.

#### F.17:8.2 - Layout B — Base‑concept pivot (discipline columns)

**Columns:** Base concept - Scale‑map - Unified Tech name - **Unified Plain name** - Plain‑Twin Governance (PTG) - Twin‑Map Id (LEX) - Formal U.Type - **Discipline Columns (DC)** (e.g., Operational Management / IT/Software / Physics / …) - Rationale - Notes.

* `Base concept (EN / RU)`
* `Scale‑map (Σ / Π / μ)` *(optional; see §9.4)*
* `Unified Tech name`
* `Unified Plain name`
* `Plain‑Twin Governance (PTG)` *(optional)*
* `Twin‑Map Id (LEX)` *(optional)*
* `Formal U.Type`

* **Discipline Columns (DC)** (choose 3–5): e.g., **Operational Management**, **IT/Software**, **Physics**, **Science/Theory**, **Math/Proof**, **Literature**, **Religion** *(or other discipline columns suited to the thread)*
 * `Unification Rationale`
* `Notes`
 
> **Guidance.** Publish **Layout A** for kernel users and spec authors; publish **Layout B** for cross‑disciplinary onboarding and teaching.
> **Clarification — Plain vs Base concept.** In Layout B the `Base concept (EN/RU)` is a **discipline vantage** aid and **does not substitute** for the single **Unified Plain name** in the left rail. Do not mint alternative unified‑plain synonyms inside DC cells; flag homonym risks with ⚡ in `Notes`.

### F.17:9 - Invariants (normative constraints)

1. **Locality.** Every SenseCell is **Context‑scoped** (E.10.D1). No global synonyms.
2. **Bridges only via F.9.** Cross‑context equivalence appears **only** as an explicit Bridge with **CL**. Any row citing > 1 **Context** must state at least one Bridge.
3. **Heterogeneity.** Across the UTS, coverage must involve **≥ 3 domain families** (F.1 Step 2; A.8).
4. **Scale‑map tags (optional but disciplined).** If used in Layout B:
   * **Σ (Summative):** concept’s quantitative properties aggregate across a population of executions/holders.
   * **Π (Conjunctive/Compositional):** concept composes by required conjunction (all‑of), not by averaging.
   * **μ (Micro/Atomic):** concept is inherently micro‑level (per single execution/holder).
     *(Tags aid teaching; they do not change semantics.)*
5. **Strict Distinction.** Use `U.Method` vs `U.MethodDescription`, `U.Work` vs `U.WorkDescription`, `U.Role` vs `U.RoleCharacterisation` correctly; do **not** collapse intensional objects with their descriptions.
6. **Dual register.** Every row has **Tech** and **Plain** labels per F.5.
7. **One‑breath rationale.** The `Unification Rationale` is a **single sentence** explaining the conceptual sameness despite local wording.
8. **Unified naming neutrality.** The **Unified Tech name** is the neutral FPF choice per F.5; it is **not** lifted wholesale from any single Context unless the Concept‑Set justification (F.7) shows identity.  
9. **Column discipline.** Layout A uses **Bounded‑Context Columns (BCC)** only; Layout B uses **Discipline Columns (DC)** only. Mixing is non‑conformant.
10. **Plain‑twin discipline.** The single **Unified Plain name** lives in the left rail; BCC/DC cells carry senses only. Any additional Plain aliases are managed in LEX (tv:\*) and never minted per column.

### F.17:10 - How to Compile (conceptual moves, not a workflow)

**M1 - Fix contexts (F.1).** Declare the **12 (±)** contexts for this thread.
**M2 - Harvest & cluster (F.2–F.3).** Identify candidate senses per Context; cluster *within* Contexts; mint **SenseCells**.
**M3 - Form Concept‑Sets (F.7).** For each “the‑same‑thing” across Contexts, create one **CSR**; attach SenseCells.
**M4 - Name (F.5).** Choose **Tech/Plain** labels; assert the **FPF U.Type** (or propose a new one via F.8).
**M5 - Bridge (F.9).** Where Cross‑context relations are not exact, assert Bridges with **CL** and a short **Loss** note.
**M6 - Place rows into blocks (§7).** Keep the sheet memorisable.
**M7 - Write one‑line `FPF Description` and the `Rationale`.**
**M8 - Run acceptance harness (F.15).** Apply the UTS checks in §11.

> **Note.** These are **thought moves**. No tooling is implied or required.

### F.17:11 - Acceptance Harness (SCR/RSCR) for a UTS

#### F.17:11.1 - Static Conformance Rules (SCR‑UTS)

* **SCR‑UTS‑01 (Row completeness).** Each row contains: `U.Type`, `Tech`, `Plain`, `FPF Description`, `SenseCells (≥ 1)`, `Rationale`.
* **SCR‑UTS‑02 (Dual register).** Each row has both Tech and Plain labels; Tech is used in spec prose, Plain in didactics.
* **SCR‑UTS‑03 (Locality discipline).** Every SenseCell is cited **with its Context name & edition**.
* **SCR‑UTS‑04 (Heterogeneity).** Across the sheet, the set of referenced Context spans **≥ 3 domain families**.
* **SCR‑UTS‑05 (Bridge honesty).** All cross‑context sameness claims are expressed via an F.9 **Bridge** with a **CL** score; if identity, mark **CL=3** and note “identity/no loss” rather than omitting the bridge.
* **SCR‑UTS‑06 (One‑breath rationale).** The rationale is ≤ 35 words and states the **conceptual invariant** that unifies the row.
* **SCR‑UTS‑07 (Block parsimony).** Block Plan uses **≤ 7 blocks**; each block’s rows can be recited from memory by a careful reader.
* **SCR‑UTS‑08 (Strict Distinction).** No row description conflates Method↔MethodDescription, Work↔WorkDescription, Role↔RoleCharacterisation.
* **SCR‑UTS‑09 (Unified naming).** Each row’s **Unified Tech name** complies with F.5 rules (dual register, minimal generality, morphology); it is not a mere alias of one Context unless justified by an F.9 Bridge with **CL=3**.
* **SCR‑UTS‑10 (Column discipline).** **Layout A:** all non‑left‑rail columns are **Contexts** with editions. **Layout B:** all non‑left‑rail columns are **discipline columns**. No cross‑use.
* **SCR‑UTS‑11 (Plain‑twin hygiene).** The **Unified Plain name** appears **once** in the **left rail** (**tv:primary**). Neither BCC (Layout A) nor DC (Layout B) cells may introduce alternative **unified** Plain synonyms; use the ⚡ marker in `Notes` to flag homonym risk where needed.

#### F.17:11.2 - Regression Rules (RSCR‑UTS)

* **RSCR‑UTS‑A (Edition churn).** When a Context’s edition changes, old SenseCells remain addressable; new cells are added; **no silent rewrites**.
* **RSCR‑UTS‑B (Name stability).** Tech labels change only with a documented F.5 decision; Plain labels may evolve didactically if the Tech name stays.
* **RSCR‑UTS‑C (Coverage drift).** Adding/removing rows **must not** reduce family heterogeneity below §9.3.
* **RSCR‑UTS‑D (Loss drift).** If new evidence changes a Bridge’s CL/Loss, the row updates both the CL and the 2–6 word loss note.
* **RSCR‑UTS‑E (Plain discipline).** No per‑column Plain text appears in BCC/DC columns; any additional Plain aliases are tracked in Annex with **tv:** entries and counted against the alias budget (F.13). 

### F.17:12 - Canonical Heading Templates (fill with your Contexts/Discipline columns)

**Layout A — Kernel‑first**

```
# | Block | FPF U.Type | Unified Tech name | Unified Plain name | Plain‑Twin Governance (PTG) | Twin‑Map Id (LEX) | FPF Description
  | BCC‑1 (Context name, edition) | BCC‑2 (Context name, edition) | BCC‑3 (Context name, edition) | … (more BCCs from the F.1 cut)
  | Bridges (CL/Loss) | Unification Rationale | Notes
```

**Example headers (illustrative, not canonical):**  
`OMG BPMN 2.0 (2011) | W3C PROV‑O (2013) | ITIL 4 (2020) | W3C SOSA/SSN (2017) | OMG Essence (Language, 2023)`  
_(Use the actual Contexts from your F.1 cut; always include the edition.)_

**Layout B — Base‑concept pivot**
_(Plain twin discipline identical: only one **Unified Plain name (tv:primary)** in the left rail; DCs carry senses, not Plain.)_

```
# | Block | Base concept (EN / RU) | Scale‑map (Σ/Π/μ)
  | Unified Tech name | Unified Plain name | Plain‑Twin Governance (PTG) | Twin‑Map Id (LEX) | Formal U.Type
  | DisciplineColumn‑1 (discipline) | DisciplineColumn-2 (discipline) | DisciplineColumn‑3 (discipline) | DisciplineColumn‑4 (discipline) | DisciplineColumn‑5 (discipline)
  | Unification Rationale | Notes
```

**Examples of Discipline Columns (illustrative):** Operational Management - IT/Software - Physics - Science/Theory - Mathematics - Literature - Religion.  
_(Choose 3–5 that fit the thread; do not place Contexts here.)_

### F.17:13 - Didactic Aids

* **Trip‑wire column (optional).** A ⚡ marker in `Notes` for known homonyms (e.g., *process (BPMN) ≠ process (thermo)*).
* **DesignRunTag tag (optional).** `design` / `run` hint for concepts whose senses split by time.

### F.17:14 - Micro Examples (one line each, illustrative)

*(These illustrate Layout A headings; swap Contexts to match your cut.)*

**Row: `U.Work` (Execution)**
`Tech=Execution - Plain=run` — “Dated, resource‑consuming occurrence realising a MethodDescription.”
**BPMN 2.0 (2011)**: *Activity instance* - **PROV‑O (2013)**: `prov:Activity` - **ITIL 4**: *change/incident record (run)* - **SOSA/SSN**: *(context: producer of Observation)* - **Essence (Language)**: *Activity occurrence* - **Bridges**: CL=3 (BPMN≍PROV) - **Rationale**: *All cells denote the concrete happening, not the recipe nor the capability.*

**Row: `U.MethodDescription` (Recipe)**
`Tech=MethodDescription - Plain=recipe` — “Recorded specification guiding executions.”
**BPMN 2.0 (2011)**: *Process model* - **PROV‑O (2013)**: `prov:Plan` - **ITIL 4**: *SOP / Work instruction* - **Essence (Language)**: *Activity space/Practice description* - **Bridges**: CL=2 (loss: control‑flow vs intent) - **Rationale**: *All cells denote the codified ‘how’, distinct from both the performer and the run.*

> These rows are examples only; your UTS MUST be compiled from your chosen **Contexts** (Layout A) or **Discipline Columns (DC)** (Layout B) and SenseCells.

### F.17:15 - Relations

* **Builds on:** F.1–F.3 (contexts & local senses), F.7 (Concept‑Set), F.5 (names), F.9 (Bridges).
* **Feed:** Part A and Part C definitions/examples (row ids used as cross‑refs); teaching bundles (F.16).
* **Constrained by.** A.7 **Strict Distinction**, A.11 **Parsimony**, **E.10 §6 Twin‑Register Discipline** (Tech/Plain), **E.10.P (prefix registry: tv: / ut:)**, E.10.D1 **Context discipline**.

### F.17:16 - Migration Notes

* **Re‑blocking.** If the Block Plan changes, keep row ids stable; move rows between blocks rather than renumbering.
* **Context growth.** When adding a new Context, populate SenseCells progressively; do not claim coverage until ≥ 1 row per block cites it.
* **Name evolution.** Update **Plain** labels freely for pedagogy; change **Tech** labels only via F.5 with clear S‑rules.


### F.17:17 - FAQ (authoring hygiene)

**Q1. Is the UTS a registry?**
*A.* No. It is a **didactic publication artifact**. No CRUD semantics, no workflows.

**Q2. Can we collapse two Contexts if their terms look identical?**
*A.* Only via **F.9 Bridge** with **CL=3**. Identity must be argued, not assumed by spelling.

**Q3. Where do state‑graphs (A.2.5) show up?**
*A.* In `Notes` or as a dedicated row if the stateful nature of a Role family is central to the thread.

**Q4. How do we show deontic approvals?**
*A.* The concept rows (`U.SpeechAct`, `U.Commitment`, `U.PromiseContentClause`, `U.PromiseFulfillmentEvaluation`) make the communicative/epistemic pieces visible; enactment appears in examples, not as sheet mechanics.

### F.17:18 - 90‑Second Teaching Script

> “To make our language usable, we publish a **Unified Term Sheet** for each thread. Each **row** is one **unified concept** (a Concept‑Set) named with a **Tech** and a **Plain** label and tied to concrete senses in our chosen **context of meaning**. If two contexts differ, we show an explicit **Bridge** with a **CL score** and a short **loss note**. The rows are grouped into 5–7 **didactic blocks** so the whole sheet fits in working memory. This is not a database; it’s the **one table** a careful mind can hold. From this sheet, everyone—engineers, managers, researchers—can talk precisely about **the same things** across disciplines.”

### F.17:End

## F.18 - Local‑First Unification Naming Protocol
*Status: normative (Part F, Unification Suite). Audience: engineer‑managers, lead architects, editors of FPF artefacts.* 

### F.18:1 - Context

Names must carry enough signal for everyday use, yet never smuggle in Cross‑context identities, hidden assumptions, or role/metric clutter. F.18 supplies that naming discipline and weaves it through F.1–F.17: Term Harvesting, Sense Clustering, Role Descriptions, Concept‑Sets, Bridges, Lexical Continuity, Anti‑Explosion control, and the Unified Term Sheet (UTS).

**Scope.** This protocol applies to naming of **any concepts** authored in Part F (U.Types and **local concepts** alike: kinds, roles, services, methods, works, relations, characteristics, states/statuses, etc.). The **U.Types** norms in this section are a **specialization**, not a restriction of scope.

**Purpose of this pattern.** Provide a **human‑legible, context‑anchored naming protocol** that:
* keeps *local meaning first* and prevents Cross‑context conflation;
* makes the **kind** of thing explicit (System, Episteme, Role, Service, Method, Work, Decision, Requirement, etc.);
* integrates smoothly with **Concept-Sets**, **`U.RoleDescription`**, and **Bridges** without requiring any special notation or tooling;
* supports lifecycle actions (mint, reuse, align, deprecate, split/merge) with a paper trail that managers can audit.

### F.18:2 - Problem

Without a shared naming protocol inside Part F, the same recurrent failures appear:

1. **Global‑name illusion.** A short label travels from one context to another and is *assumed* to mean the same thing; later, contradictions surface during acceptance or assurance.
2. **Context drift.** A label gradually changes inside its Context (edition, scope, envelope) without leaving a clean trace; readers argue over “what we meant.”
3. **Kind confusion.** Names hide *what sort of thing* is being named (System vs Episteme vs Role vs Service, etc.), leading to category errors and brittle integration.
4. **Threshold‑in‑the‑name.** Numeric limits, duty segregation, or state qualifiers get baked into names (“Critical‑Reviewer‑0.2 mm”), which cannot age or compose.
5. **Stealth renames.** Quiet label swaps, steered by fashion or politics, sever continuity with earlier evidence, plans, and bridges.
6. **Explosion by synonyms.** Teams mint many near‑synonyms instead of reusing a Concept‑Set row or creating an explicit Bridge with loss notes.

These failures erode trust, block reuse, and make Part F machinery (Concept-Sets, `U.RoleDescription`, Bridges) harder to apply.

### F.18:3 - Forces

| Force                                      | Tension to balance                                                                                                            |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Local truth vs Cross‑context portability**  | The name must “belong” inside one context while remaining referenceable from other contexts through explicit bridges.               |
| **Human ergonomics vs conceptual clarity** | Short, natural labels help teams move; explicit kind and Context cues keep reasoning sound.                                          |
| **Stability vs evolution**                 | Names should be durable, yet easy to deprecate or refine without breaking links to past evidence and work.                    |
| **Brevity vs auditability**                | A compact “badge” for everyday speech, plus an authoritative **Name Card** that records meaning, scope, edition, and lineage. |
| **Parsimony vs inclusivity**               | Reuse existing Concept‑Set rows where possible; mint new names only when indispensable in the local context.                     |

### F.18:4 - Solution — The Local‑First Naming Protocol

F.18 defines **eight rules** (R‑rules) and **six practices** (P‑practices). Together they produce **Name Cards** that any reader can interpret **ontologically** without guessing, and that slot cleanly into the rest of Part F.

**Path Card (subset of Name Card).** A **Name Card** whose **object‑of‑talk/entity-of-interest** is an **EvidenceGraph Path**: it cites a **PathId** (or **PathSliceId**), **Context**, **ReferencePlane**, **Γ_time**, and any **Bridge id(s) + CL/CL^plane** (with loss notes). Used by **G.6** and **G.10** to make justifications portable on UTS.

#### F.18:4.1 - The Eight R‑rules (normative)

**R1 — Speak every name *with its Context*.**
A name is **never** context‑free. When you introduce or use a name, **pair it with the Bounded Context** where it lives (the “Context of meaning”), and with the **edition** of that Context if relevant. In everyday speech: “X, *in* Y.” Cross‑context use requires a Bridge; labels alone do not travel. 

**R2 — State the ontological *Kind* on the Card.**
Every Name Card **must** state the **Kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This prevents category errors and keeps Role–Method–Work alignment clean. *Clarification:* this is a **Card requirement**, not a demand that the label string begin with the Kind.

**R3 — Declare the *Purpose / use‑domain* on the Card.**
In addition to **Kind**, the Name Card **must** state the intended **Purpose / use‑domain** that situates the concept in practice and signals **which families of contexts** are expected to use it (e.g., mathematical formalism, engineering practice, computer science, systems management). This enables reconstruction of usage from the lexicon and reduces unintended scope drift. *Clarification:* this is a **Card field**; it does **not** require the label string to carry the purpose qualifier.

**R4 — Resolve the name to a *Local‑Sense*.**
A minted name must resolve to a Local-Sense inside its Context (the result of F.2–F.3). If a name points to a Role Description, state that template and its sense basis. Avoid heavily overloaded surface terms: when needed, prefer concise two-word Tech labels that hint at the intended sense.

**R5 — Use *Twin Registers* (Unified Tech + Plain).**
Provide two human‑oriented labels on the Name Card, per **E.10** register discipline:
* a **Unified Tech** label (short, morphology‑stable, neutral in wording);
* a **Plain** label (reader‑friendly phrasing for managers and subject‑matter experts).

The **Unified Tech** label is the only one used in **Core** normative prose; **Plain** is for teaching and examples. Both remain **context‑local**; neither establishes Cross‑context identity (that is the job of the **UTS row** and **Bridges**).

**R6 — Keep thresholds and states *out of the name*.**
Do not encode numeric limits, separation‑of‑duties, or readiness states in the label. Put thresholds on **Method steps** (capability/acceptance), states in **Role State Graphs**, and SoD via **incompatibility** relations. Names carry *what this is* and *which Context claims it*—not *when and how it may act*.

**R7 — Cross‑context only by *Bridge* with loss notes.**
When another Context needs to reference a name, use an **Alignment Bridge** that states the relation (equivalent, narrower, broader, analogous) and its **Congruence Level** with explicit **loss/fit** annotations. Never equate two names by label alone.

**R8 — Make renames and merges *first‑class events*.**
When a label changes, or two labels consolidate or split, record it on the Name Card as a lifecycle action (rename, merge, split, retire) with rationale and dates. Past uses *remain valid as historical facts*; continuity comes from lineage, not silent edits.

#### F.18:4.2 - The Six P‑practices (normative process)

**P1 — Candidate set (*NQD-front* of seed-words).**
Do **not** pick a label “in one shot”. Build a **small, non-dominated candidate set** (an *NQD-front*, typically 5–10 items) by seeding and varying along:
**Traditions** — mathematics, physics, engineering, computer science, systems thinking, management, etc. with their typical contexts and situations; use maximum diversity here;
 **Novelty/Familiarity** — from careful **reuse** of established terms to sharper **neologisms** from recent SoTA traditions;  
 **Lexical form** — distinct **head terms** and morpheme families, readability/pronounceability, inflection/declension, transparency.
Use the **Novelty–Quality–Diversity** discipline from **Part G** to maintain only **non-dominated** candidates; when appropriate, you may implement this via **Γ_nqd.generate**. Record the **seeds** and the short rationale in the Card’s notes. Choose final **Unified Tech**/**Plain** labels **from this frontier**; if a strong candidate is discarded, briefly note why.

For the purposes of **Diversity_P**, group candidates into **head-term families** (same base noun/verb + minor prepositions or case endings). Variants such as *“Reference plane”*, *“Plane of reference”* and *“Referred plane”* **count as one family**, not three distinct candidates. An NQD-front with multiple near-clones from one family **does not** satisfy the diversity requirement. Aim for **≥ 3 distinct head-term families** in the CandidateSet; if the front ends up with fewer families (e.g. due to a very narrow domain or strong AliasRisk on other heads), the Name Card **MUST** record a brief rationale in the NQD-front notes.

**Lexical Q‑axes for the NQD‑front**
When P1 uses **NQD‑CAL (C.18)**, treat the **Quality vector** over candidates as part of the same archive as C.18’s **NQD‑frontier**. Recommended axes (all **ordinal; no arithmetic means**):

 * **SemanticFidelity (P — Ontological precision).**
  *Question.* Does the label verify against the **Minimal Definitional Statement (MDS)** and Concept‑Set row without adding or losing core invariants?
  *Scale (ordinal; ↑ better).* `{Misleading, Vague, Precise, Exact}` with `Exact ≻ Precise ≻ Vague ≻ Misleading`.  
  *Link to P2.* When **P2** is run, derive the SemanticFidelity rating from the per‑sense‑seed judgements: candidates with any **core** sense‑seeds classified as `wrong‑prototype` **MUST** be rated **Misleading**; candidates rated **SemanticFidelity ≥ Precise** **SHOULD** have at least a configurable fraction `θ_P` (default `θ_P = 0.7`) of sense‑seeds in `on‑target` and **NONE** in `wrong‑prototype`. Discard candidates that remain **Misleading** after revision.

* **CognitiveErgonomics (S — Sociolinguistic admissibility).**  
  *Question.* Can the target **RoleEnactors** (engineers, managers) read, pronounce, and recall the label without specialist training?  
  *Scale (ordinal; ↑ better).* `{Alienating, Jargon, Acceptable, Natural}` with `Natural ≻ Acceptable ≻ Jargon ≻ Alienating`. Prefer labels **≥ Acceptable** in the home Context.

* **OperationalAffordance (O — Morphological/action alignment).**
  *Question.* Does the morphology of the label hint at its role in **methods/morphisms** (object vs process vs result) and support the required derivational family (noun/verb/participial forms)?
  *Scale (ordinal; ↑ better).* `{Opaque, Role‑hinting, Action‑aligned}`. Action‑aligned labels make it obvious whether we are naming an **actor**, an **activity**, or an **artifact** (e.g., *Author* vs *Authoring* vs *AuthoredArtifact*).  
  *Kind‑sensitive cues.* When the **Kind** on the Card is a **Role**, prefer agentive/holder morphology (*…Role*, *…er*, *…or* or local equivalents); when the Kind is **Method/MethodDescription**, prefer verbal or gerundive forms; when the Kind is **Holon**, prefer result nouns, when **Work**, prefer verb. Misaligned morphology (e.g., a Role named with a pure process noun) should be treated as a **penalty on OperationalAffordance** and, if retained for legacy or regulatory reasons, called out explicitly in **Card notes**. See F.5/F.11/F.12 and **LEX‑BUNDLE §8**.

* **AliasRisk (A — Lexical overload).**  
  *Question.* How likely is a careful reader to import a **wrong sense** from neighbouring FPF artefacts or external canons when they see this string?  
  *Scale (ordinal; ↓ better).* `{Safe, Context‑dependent, High‑Risk, Overloaded}` with `Safe ≻ Context‑dependent ≻ High‑Risk ≻ Overloaded`. Avoid adopting **Overloaded** labels unless required by legacy and called out explicitly in notes. When C.18’s **DomainDiversitySignature** is available, AliasRisk MAY be refined into a CHR‑typed characteristic with the same polarity.

Use these axes for **Pareto comparison only** (per **C.16** ordinal discipline). Do **not** collapse them into a single scalar score; the NQD‑front is computed over the **vector of lexical Q‑components** together with **Novelty** and **Diversity_P**.

**P2 — Semantic read‑through against archetypal situations.**  
Alongside the NQD‑front of label candidates, maintain a **small set of 5–10 archetypal situations** (“**sense‑seeds**”) that instantiate the intended use (purpose) across different traditions. For **each** candidate label and each sense‑seed, perform a **read‑through test**:  
– write **1–2 short example sentences per sense‑seed** (e.g., “In case X, we perform \<Label\>”);  
– classify the outcome, for a careful reader in the home Context, as one of `{too‑narrow, on‑target, too‑wide, wrong‑prototype}`.  
Maintain, on the Name Card, a small tally per candidate of how many sense‑seeds fall into each class. Use these tallies both to **prune candidates** and to instantiate **SemanticFidelity** (P‑axis): labels with a sustained pattern of `wrong‑prototype` hits on core sense‑seeds **SHALL** be removed from the NQD‑front (or kept only as deprecated aliases with an explicit warning). Candidates rated **SemanticFidelity ≥ Precise** **SHOULD** satisfy the `θ_P` constraint from the SemanticFidelity definition (fraction of `on‑target` seeds) and have no `wrong‑prototype` counts.  
Record **rejected candidates** and their **mismatch patterns** in the Name Card’s **NQD‑front notes**.

**P3 — Mint‑or‑Reuse gate (F.8).**
Before minting, search your Context’s **Concept‑Set table**. If a row already covers your sense, reuse it and only add a **local label**. If not, propose a **new row** and capture the decision in a brief rationale.

**P4 — Concept‑Set linkage (F.7).**
Every Name Card **must** indicate its Concept‑Set row (or record “not applicable” for intentionally Context‑unique names). This is the handle for alignment and anti‑explosion control.

**P5 — UTS registration (F.17).**
Publish each Name Card to the **Unified Term Sheet** with Context, kind, twin labels, sense anchor, edition, and lifecycle status. Keep the UTS the single, human‑readable table of record.

**P6 — Lifecycle hygiene (F.13).**
Apply the same discipline to renames, splits/merges, and retirements; leave a forward/backward pointer so readers can trace continuity at a glance.

### F.18:5 - The Name Card (authoring template, representation-agnostic)

#### F.18:5.1 - Card purpose & mode guard (normative)

To prevent “post-hoc justification” of intuitively chosen labels, every **Name Card** SHALL declare its
**CardMode ∈ {MintNew, DocumentLegacy}**:

* **MintNew.** The Card is the **output of an NQD-style lexical search** over a **candidate label set** generated inside
  the home Context(s), using the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance,
  AliasRisk}` together with **Novelty (N)** and **Diversity_P** (per A.0 / C.17–C.18 / B.5.2.1).  
  – The Card SHALL record:  
    – a minimal **CandidateSet** (the labels actually evaluated), with **head-term family** tags for each candidate;  
    – the resulting **NQD-front** of **non-dominated candidates** over ⟨Q-tuple, N, Diversity_P⟩;  
    – a short **selection note** explaining why the chosen Tech/Plain pair was picked from that front
      (e.g., “better CognitiveErgonomics at equal SemanticFidelity”).  
 
  – A single-element NQD-front is permitted only if the Card records a brief rationale why **no alternative candidate
    survived** the lexical and NQD filters (e.g., legacy constraints, strong AliasRisk on all other options).

* **DocumentLegacy.** The Card documents an **externally imposed legacy label** (e.g., a regulatory or de facto Standard)
  and its mapping to FPF structures. In this mode the Card MAY omit a full NQD-front, but SHALL:  
  – state the **legacy source / provenance**;  
  – either (i) provide at least a **sketched NQD-comparison** of viable internal variants against the legacy label, or  
    (ii) record a short **out-of-scope rationale** (e.g., “name frozen by law; see cited Standard”) explaining why NQD
    search is not being used for selection.

For all **Core-surface naming of U.Types and other canonical FPF concepts**, **MintNew** is the **default** CardMode; using
DocumentLegacy for such names requires an explicit justification on the Card.

A **Name Card** is the authoritative, human‑readable record of a name inside its Context. It has these fields; teams may add local notes.

1. **Row ID** — the stable, opaque **UTS row identifier** (the identity anchor).
2. **Twin labels** — **Unified Tech** and **Plain** (per E.10).
3. **Context of meaning** — the Bounded Context and, if relevant, its edition.
4. **Kind** — what sort of thing this is (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This is an **ontological category**, not a surface‑string prefix. 
5. **Purpose / use‑domain** — the intended area(s) of use (which families of contexts are expected to use it).
6. **Minimal Definitional Statement (MDS)** — one‑paragraph intended sense in the home context (no tool/process slang).
7. **Didactic subtitle** — ≤ 12 words that signal pragmatic use.
8. **Sense reference** — a Local‑Sense reference (how F.2–F.3 clustered it).
9. **Concept‑Set linkage** — Concept‑Set reference or “not applicable” (with rationale).
10. **Alignment note** — if a Bridge exists to other Contexts, cite it and record **loss/fit** in plain words (no formulas required on the Card).
11. **Relation kind** — if the name is for a relation, declare **structural** vs **epistemic** and `validationMode ∈ {axiomatic, inferential, postulate}`. For **structural** relations, provide **Constructive** grounding (`tv:groundedBy → Γₘ.sum|set|slice`). If the name is not for a relation with arity ≥ 2, set this field to “n/a”.
12. **Manager’s clip** — one‑line “use/avoid” guidance for everyday communication.
13. **Archetypal situations (sense‑seeds)** — **5-10 short “X‑case” lines** used by **P2** for the semantic read‑through; keep them **edition‑aware** and **context‑local**.
14. **NQD‑front seeds** — brief rationale for discarded candidates (**include mismatch patterns from P2 and any lexical Q‑scores used in P1**).
15. **SemanticFidelity/CognitiveErgonomics/OperationalAffordance/AliasRisk** scores for the NQD-front labels.
16. **Version**  — current status and history of editions.
17. **Card notes** — optional free text with comments about the name (e.g., recommended translations, etymology, pronunciation). 

**Manager’s reading habit.** When two names collide in a meeting, ask for their **Context**, **Kind**, **Purpose/use‑domain**, and **Sense anchor**. If any of those differ, you are comparing different things; switch to **Bridge** talk, not label talk.

### F.18:6 - What *belongs* in the label—and what does not

**Belongs (keeps the label clean and durable):**

* The **core head word** that names the thing *(the **Kind** is recorded on the Card; the string need not encode it)* (e.g., “Pump”, “Standard”, “Requirement”, “Surgeon”, “Cooling”).
* A **purpose qualifier** if it is essential to the local sense and stable across editions (e.g., “Cooling” vs “Fuel”).
* A **scope qualifier** only if it is part of the *meaning* rather than the current plan (“Surgical Ward” rather than dates or batch numbers).

**Does not belong (move elsewhere):**

* **Numbers and thresholds** (put on steps, capabilities, acceptance clauses).
* **States** (use Role State Graphs and checklists).
* **Temporal windows** (work plans and history).
* **Organisational authorisations** (speech acts and assignments).
* **Imported acronyms** from other Contexts (use Bridges with loss notes instead).

**Quick litmus for authors.** If removing a number, date, or state *does not* change the *meaning* of the thing, it should **not** be in the label.

### F.18:7 - Worked triad (three short, context‑local examples)

*(Names below are illustrative; the same words in other Contexts may mean something else. The point is how the Name Card keeps them clear.)*

#### F.18:7.1 - Industrial operations Context: “Thermal Management - 2026”

* **Kind:** Service
* **Purpose / use‑domain:** industrial thermal utilities; line‑level planning and operations
* **Unified Tech label:** Cooling Supply
* **Plain label:** Chilled water for line B
* **Sense anchor:** supply of water at defined temperature/flow to boundary B
* **Concept‑Set:** “Utility service” row; local variant recorded
* **Alignment note:** Bridge to “Plant Utilities - 2026” notes that “Cooling Supply” there bundles filtration; *loss:* filtration is not guaranteed in this Context
* **Version:** 20 Feb 2024
* **NQD‑front (seed candidates):** *Cooling Supply*, *Chilled Water Service*, *Process Cooling*, *Cooling Utility*. **Chosen:** *Cooling Supply* (neutral, morphology‑stable).

**Why it’s good.** The label doesn’t encode temperature or flow limits (those live in acceptance). It names a Service; nobody will confuse it with a pump System or a Method.

#### F.18:7.2 - Clinical Context: “Hospital OR - 2026”

* **Kind:** Role
* **Purpose / use‑domain:** OR governance and staffing; credentialing and checklists
* **Unified Tech label:** Surgeon Role
* **Plain label:** Operating surgeon
* **Sense anchor:** person who is authorised to perform surgical steps under defined checks
* **Concept‑Set:** “Clinical roles” row
* **Alignment note:** Bridge to “Training & Credentialing - 2026” shows partial overlap; *loss:* that Context’s “Senior Surgeon” carries teaching duties that do not apply here
* **Version:** Feb 2025; renamed‑from “Lead Surgeon” (2025) with rationale: avoided “lead” vs “operating” ambiguity
* **NQD‑front (seed candidates):** *Surgeon Role*, *Operating Surgeon*, *Primary Surgeon*, *Operating Physician*. **Chosen:** *Surgeon Role* (Kind‑neutral string; Plain clarifies).
*Lexical Q snapshot (PSOA‑style, informative).*  

| Candidate | SF | CE | OA | A‑Risk | Comment |
| --- | --- | --- | --- | --- | --- |
| Surgeon Role | Precise | Acceptable | Role‑hinting | Safe | Neutral head noun; morphology matches **Role** Kind; works across departments. |
| Operating Surgeon | Precise | Natural | Role‑hinting | Context‑dependent | Reads well, but “operating” competes with “operating theatre/room”; kept as Plain label only. |
| Primary Surgeon | Vague | Natural | Role‑hinting | Context‑dependent | “Primary” ambiguous (training vs shift); rejected for governance vocabulary. |
| Operating Physician | Vague | Jargon | Role‑hinting | High‑Risk | Collides with non‑surgical physician roles; rejected despite familiarity in some hospitals. |
 
**Why it’s good.** No fatigue thresholds or readiness states in the name; those live in the Role’s state graph and checklists.

#### F.18:7.3 - Public service Context: “Civic Services - 2026”

* **Kind:** Requirement
* **Purpose / use‑domain:** service performance management; public service SLAs
* **Unified Tech label:** Passport Lead‑Time
* **Plain label:** Time to issue a passport
* **Sense anchor:** elapsed time from complete application to issuance
* **Concept‑Set:** “Service quality requirements” row
* **Alignment note:** Bridge to “Legal Framework - 2026” records that legal “deadline” has different remedies; *loss:* legal exemptions not carried into this Context
* **Version:** current
* **NQD‑front (seed candidates):** *Passport Lead‑Time*, *Issuance Time*, *Service Turnaround*, *Time to Issue Passport*. **Chosen:** *Passport Lead‑Time* (neutral; Plain remains didactic).

**Why it’s good.** Target values (e.g., ≤ 20 days) are not in the label; they live in acceptance clauses.


### F.18:8 - Conformance Checklist (editor aid) — *Part I: naming & cards* (**non‑normative**)

**CCE‑F18.1 (Context pairing).**
Every name used in normative text **must** be paired with its **Context of meaning**. If you cannot name the Context, you do not have a valid name.

**CCE‑F18.2 (Kind clarity).**
Every Name Card **must** state the **kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, …). Using labels that hide kind is non‑conformant.

**CCE‑F18.2a (Purpose declared).**
Every Name Card **must** state the **Purpose / use‑domain** (families of contexts where the concept is expected to be used). Omitting Purpose is non‑conformant.

**CCE‑F18.3 (Sense anchoring).**
A minted name **must** resolve to a **Local‑Sense** in its Context. If a sense cannot be stated, label minting is deferred.

**CCE‑F18.4 (Twin registers).**
Each Name Card carries a **Unified Tech** and a **Plain** label (E.10). Tech appears in **Core** prose; Plain in teaching/examples.

**CCE‑F18.5 (No thresholds/states in labels).**
Numeric limits, readiness states, and separation‑of‑duties **must not** appear in labels. Put them on steps, checklists, and role algebra.

**CCE‑F18.6 (Bridge‑only travel).**
Cross‑context reuse of a name **must** go through an **Alignment Bridge** with an explicit relation and **loss/fit** notes. Label matching alone is forbidden.

**CCE‑F18.7 (Lifecycle visibility).**
Renames, splits/merges, and retirements **must** be recorded on the Name Card with dates and rationale. Past occurrences remain valid as historical facts.

**CCE‑F18.8 (Mint‑or‑Reuse gate).**
Before minting, authors **must** check the Context’s Concept‑Set table; if a row exists, **reuse** it with a local label unless a documented reason compels a new row.

**CCE‑F18.9 (UTS entry).**
Names used in normative artefacts **must** appear on the **Unified Term Sheet** with the specified **Name‑Card fields**; include Notes when present).

**CCE‑F18.10 (No cross‑kind labels).**
Do not reuse the same **Unified Tech label** for different kinds inside one context (e.g., “Cooling” as a Service and as a Method). If unavoidable, add a stable qualifier to disambiguate and record the decision on both Name Cards.

**CCE‑F18.11 (Manager’s clip).**
Each Name Card **should** carry a one‑line “use/avoid” note to guide everyday speech. Where omitted, editors add it during review.

**CCE‑F18.12 (Anti‑explosion check).**
If three or more near‑synonyms for the same Local‑Sense appear in drafts, authors **must** either consolidate to one label or record an intentional synonym pair with use/avoid notes and a plan to converge.

### F.18:9 - Normative Standard (what must be true)

> This section is binding. It specifies the publication Standard for unification‑oriented names in the Unification Suite (Part F), with **local‑first authority**, **bounded context clarity**, and **one‑way unification** upwards along the ladder. It complements, and does not replace, the structural and epistemic Standards elsewhere in FPF.

**9.1 Local authority & home.**
Every unification name has a **single home**: exactly one *Bounded Context* that authors and stewards it. The home is responsible for the definition, examples, and lifecycle of the name. Cross‑context reuse happens by **bridges**, not by relocating the home.

**9.2 Minimum definitional payload.**
A published name MUST ship with a human‑readable **Minimal Definitional Statement (MDS)** that states the intended sense in the home context, and a **Didactic Subtitle** (≤ 12 words) that signals its pragmatic use. The MDS must be free of process slang and implementation jargon.

**9.3 Row ID + label surfaces.**
For each adopted name, the home supplies:
* a **Row ID** (the opaque UTS identifier — the **identity anchor**), and
* two **label surfaces**: a **Unified Tech** label (for Core prose) and a **Plain** label (for teaching).
  Both labels refer to the same underlying sense; **Plain** may simplify terms, not premises.

**9.4 One‑way dependencies.**
Each rung on the ladder depends only **downwards**: a name at rung *n* can rely on names ratified at rungs ≤ *n*, never sideways or upwards. Cycles are prohibited. If a dependency is not yet ratified at the required rung, the new name remains Draft or Pilot.

**9.5 Local‑first before reuse.**
Teams MUST first **identify and stabilize the local sense** (within their Bounded Context). **Within the home**, reuse existing **Concept‑Set rows** where they fit (§4.2 **P1**). **Across contexts**, reuse occurs via **Alignment Bridges** that map the local sense to an existing sense elsewhere—without collapsing the local home.

**9.6 Sense, not string.**
Publication concerns **sense** (intended meaning in context), not the literal string. Synonyms are allowed as **Plain** labels or **aliases** only if they point to the same **Row ID** and pass the conformance checks in §15 (“CC‑F18”). Strings must not be treated as identity.

**9.7 Relation-kind discipline (structural vs epistemic).**
If the public name surfaces a **structural relation**, its intended sense **MUST** be backed by *exactly one Constructive trace* in the structural calculus (Compose-CAL) and **SHALL** declare `validationMode=axiomatic` (see E.14). If the name surfaces an **epistemic relation**, Constructive backing is optional; **declare** `validationMode ∈ {inferential, postulate}` and use **Logical/Mapping** and/or **Empirical Validation** as appropriate. **Do not mix relation kinds** inside a single name. *(Do not use “Tier-1/2”; formality is expressed via F per C.2.3.)*

**9.8 Member vs Component.**
Names that describe collection membership MUST NOT be used to imply part‑whole structure, and vice versa. If both aspects are needed, publish two names with their own MDS and an explicit bridge.

**9.9 Lifecycle states.**
A name travels through **Idea → Draft → Pilot → Ratified → Deprecated**. Transitions require explicit human review gates. Ratified names carry a clear stewardship contact and date.

**9.10 Anti‑duplication duty.**
Before ratification, the home MUST perform a **near‑neighbor review**: identify adjacent names, record the decision to align, merge, or keep separate, and publish the rationale in the name’s record.

**9.11 Local clarity over global neatness.**
When in doubt, prefer **local intelligibility** for practitioners over global symmetry. Global neatness can be achieved later via bridges; loss of local sense is hard to repair.

**9.12 No imported tool terms in Core names.**
Names and their MDS must not carry terms whose only meaning is tied to operating tools or pipelines. If such terms are unavoidable in pedagogy, confine them to Working-Names and examples with disclaimers.

**9.13 Human‑only conformance.**
Conformance for this protocol is judged by trained human reviewers using the author/reviewer checklists in §14 and the conformance criteria in §15 (“CC‑F18”). Automated heuristics, if any exist in an organization, have no standing in the Core.

### F.18:10 - Rationale (why this exists and why these rules)

**10.1 Local‑first unlocks velocity without lexical debt.**
Centralized naming regimes seem tidy but slow learning and create brittle compromises. Local‑first minting lets teams speak clearly **now**; unification comes from disciplined bridges and one‑way dependencies, not from premature centralization.

**10.2 One home lowers ambiguity.**
Names with “many owners” drift. A **single home** concentrates accountability for sense, examples, and lifecycle, while still enabling broad reuse via alignment bridges.

**10.3 Unified Tech + Plain serve two audiences.**
Engineers need **precise** wording; managers and stakeholders need **approachable** wording. Splitting the surfaces keeps the same sense while protecting accuracy and pedagogy; both are anchored by the **Row ID**.

**10.4 One‑way ladder prevents conceptual knots.**
Acyclic dependencies cut off circular definitions and policy deadlocks. The ladder provides a simple mental model: *build on what is already firm*.

**10.5 Relation-kind discipline prevents category errors.**
Part-whole claims **(structural)** must rest on **Constructive** grounds (`tv:groundedBy → Γₘ.sum|set|slice`, `validationMode=axiomatic`). Experience-based or evaluative relations **(epistemic)** follow assurance rules (**Logical/Mapping**, and **Empirical Validation** when *postulate*), with an explicit `validationMode ∈ {inferential, postulate}`. Mixing relation kinds inside a single name confuses review and invites hidden assumptions. 

**10.6 Sense over string reduces false conflicts.**
Disputes often orbit the string (“we hate that word”). By separating **sense** (what we mean) from **string** (how we say it), the protocol enables peaceful coexistence: keep the **Row ID** constant; use one **Plain** label and, where helpful, a budgeted **alias** per register.


### F.18:11 - Application Guidance (how to apply, step by step)

**11.1 Prepare (30–60 min).**

* Clarify **your Bounded Context** and audience.
* Collect 2–3 typical user stories that require the name.
* Scan near‑neighbors in adjacent contexts (see §14.2 Reviewer checklist).

**11.2 Mint locally.**

* Write the **MDS** in plain language, one paragraph.
* Draft a **Didactic Subtitle** (≤ 12 words): “what this name buys you.”
* Decide whether the intended **relation kind** is **structural** or **epistemic** (do not mix), and declare `validationMode`.

**11.3 Choose surfaces.**

* **Unified Tech label**: concise, morphology‑stable, neutral; avoid metaphor.
* **Plain label**: approachable phrasing for non‑specialists.
* **How to choose**: pick both **from a small NQD‑frontier** (see §4.2 P1 (candidate set), P2(read-through)): diversify by tradition, novelty/familiarity, and lexical form; record discarded contenders and rationale on the Card.

**11.4 Place on the ladder.**

* Verify all dependencies are at the same rung or below.
* If a dependency is still Draft/Pilot, keep this name at most Pilot.

**11.5 Align, don’t erase.**

* Where overlap exists with another context, propose an **alignment bridge**.
* Keep your home; record the mapping and any known divergence in reading.

**11.6 Publish and steward.**

* Publish the name with MDS, subtitle, rung, home contact, examples.
* Schedule a **first refresh**: when should the home examine usage and drift?

**11.7 Deprecate gracefully.**

* If the sense is superseded, publish **Deprecation Notes**: what to use instead, and why. Keep old Working-Names visible long enough to allow safe migration.

**11.8 The “Friday test.”**

* On a busy Friday, could a competent colleague apply the name correctly using only the MDS, subtitle, and two examples? If not, refine before ratification: it too overloaded with meanings to be helpful.

### F.18:12 - Examples (worked mini‑cases for engineer‑managers)

> These examples are deliberately simple. They show how local‑first minting, one‑way unification, and tier discipline operate together.

**12.1 “Module” vs “Component” (engineering structure).**

* *Home A (Platform)* mints **Component** with MDS: “A physically or logically integrated part whose removal would alter the integrity of the whole.” **Structural**.
* *Home B (App Team)* mints **Module** with MDS: “A deployable bundle of functionality maintained as a unit.” **Epistemic** (usage practice), not a structural claim.
* **Unification:** An alignment bridge states: “In Platform, every Component may host one or more Modules; Modules are not Parts.” Dependencies are one‑way: *Module* depends on *Component*; *Component* does not depend on *Module*. No synonymy asserted. Both names remain in their homes.

**12.2 “Incident” vs “Event” (operational sense).**

* *Home C (Operations)* mints **Incident** with MDS: “An unplanned interruption or reduction in the quality of a service.” **Epistemic**.
* *Home D (Monitoring)* mints **Event** with MDS: “A recorded observation of a state change in a system.” **Epistemic**.
* **Unification:** Bridge notes: “Some Events are Incidents when they degrade service; not all Events are Incidents.” **Plain** labels (and at most one alias per register) may vary (e.g., “Outage” as an alias for **Incident**), but the **Row IDs** stay distinct. No part‑whole claims are implied.

**12.3 “Customer” vs “Account Holder” (business roles).**

* *Home E (Sales)* mints **Customer**: “A party that receives value from an offering in exchange for consideration.” **Epistemic**.
* *Home F (Finance)* mints **Account Holder**: “A party legally responsible for an account.” **Epistemic**.
* **Unification:** Bridge states overlaps and divergence: “A Customer can be an Account Holder; an Account Holder may not be a Customer (e.g., trustee).” The homes retain stewardship; a shared Working-Name “Client” may be used in executive materials with a clear note: **Working-Name only; see Concept-IDs for decisions**.

**12.4 “Batch” vs “Lot” (collection vs integration).**

* *Home G (Manufacturing)* mints **Batch**: “A collection of items produced under shared conditions.” **Epistemic membership**.
* *Home H (Quality)* mints **Lot**: “An integrated whole packaged and tracked as one item.” **Structural whole**.
* **Unification:** Bridge notes: “A **Lot** may originate from a single **Batch** or a slice of a Batch; not every Batch yields a single Lot.” Relation mapping: **MemberOf** (Batch membership) vs **ComponentOf**/**Whole** (Lot integration). *Loss note:* membership evidence does **not** imply part‑whole structure; part‑whole structure does **not** imply shared production conditions.

### F.18:13 - Anti‑Patterns & Failure Modes (what to avoid)

**13.1 “Global name first.”**
Trying to coin a single global string before local understanding is mature. **Fix:** mint locally, publish MDS, then align.

**13.2 “Synonym storm.”**
Collecting many strings without stabilizing the Concept-ID. **Fix:** one Concept-ID per sense; multiple Working-Names only if they truly help didactics.

**13.3 “Process leakage into names.”**
Burying workflow or tool steps inside the MDS. **Fix:** keep process in method descriptions; keep names about sense, not procedure.

**13.4 “Member‑implies‑part.”**
Letting collection names induce part‑whole claims. **Fix:** separate names, separate MDS; don’t smuggle structure into membership.

**13.5 “Sideways dependency.”**
Defining a name by appealing to another Draft at the same rung or higher. **Fix:** depend only downward or postpone ratification.

**13.6 “Alias/Plain drift.”**
Letting a Plain label or alias accumulate extra meanings absent in the underlying row. **Fix:** periodic label review; prune metaphors that start bending sense; respect the alias budget.

### F.18:14 - Assurance & Conformance (human‑only checks)

#### F.18:14.1 - Author checklist (before requesting review).

* [ ] I identified the **home Bounded Context** and audience.
* [ ] I wrote a clear **MDS** (≤ 1 paragraph) and a **Didactic Subtitle** (≤ 12 words).
* [ ] I declared the **relation kind** (structural vs epistemic) and the **validationMode**; no mixing.
* [ ] If **structural**, I can point to **exactly one Constructive trace** that backs the structural claim.
* [ ] I surveyed near‑neighbors and recorded my decision to align, merge, or keep separate.
* [ ] I produced both **Unified Tech** and **Plain** labels (per E.10), with the same sense and pointing to the same **Row ID**.
* [ ] Dependencies point **only downward**; no sideways or upward pulls.
* [ ] I scheduled a **refresh date** and listed 2–3 usage examples.

#### F.18:14.2 - Reviewer checklist (at the gate).**

* [ ] One home is declared; stewardship contact is clear.
* [ ] The MDS is free from process jargon and implementation slang.
* [ ] The declared **relation kind** is justified; **structural** claims are constructively grounded; **epistemic** claims declare `validationMode` and evidential posture.
* [ ] Member vs Component is respected where relevant.
* [ ] Alignment bridges are proposed where overlap exists, with explicit reading of convergence/divergence.
* [ ] The ladder discipline holds: acyclic, downward‑only dependencies.
* [ ] The **Plain** label does not smuggle extra commitments; **Unified Tech** and **Plain** remain co‑referential and point to the same **Row ID**.
* [ ] Lifecycle state is accurate (Idea/Draft/Pilot/Ratified/Deprecated) and dated.

#### F.18:14.3 - Lightweight outcomes.**

* **Ratify** (meets all checks).
* **Pilot** (publish with explicit questions and a refresh date).
* **Revise** (return to author with targeted gaps).
* **Merge** (replace with an alignment to an existing name).
* **Deprecate** (publish successor guidance and sunset plan).

### F.18:15 - Conformance Criteria (normative “CC‑F18”)

> These are **language‑level** obligations for authors and reviewers. They ensure every unified name is **local‑first**, **bridge‑aware**, and **teachable**.

**CC‑F18‑1 (Context first).** Every unified name **SHALL** be grounded in **local senses** that were harvested and clustered **inside named Contexts** (“context of meaning”) prior to unification. No name may be minted from free‑floating glosses or Cross‑context intuition. Use F.1–F.3 first.

**CC‑F18‑2 (Bridge‑only sameness).** Claims of sameness across Contexts **SHALL** be expressed only via explicit **Bridges** with a stated congruence and loss note. Mere spelling similarity never licenses a unified name. Use F.9.

**CC‑F18‑3 (Twin‑register naming).** Each unified concept **SHALL** carry **two labels**—a **Unified Tech** label (used in Core prose) and a **Plain** label (used for teaching). Labels are chosen per the naming discipline of F.5 and the register rules of **E.10**.

**CC‑F18‑4 (Neutrality of the Tech label).** The **Unified Tech** label **SHALL NOT** be borrowed wholesale from any single source Context where that borrowing would re‑import that Context’s private distinctions. Prefer a **neutral** term; **Cross‑context reuse occurs only via the UTS row and explicit Bridges**. (See F.5 “allowed/forbidden forms”.)

**CC‑F18‑5 (One concept per row, one Tech label per row).** A unified concept **SHALL** be captured as **one Concept‑Set row** in the **UTS**. Exactly **one Unified Tech label** is normative for that row; additional legacy strings are aliases in Annex (budgeted). Use F.7 with F.17.

**CC‑F18‑6 (SenseCell citations).** For each unified name, the **SenseCells** (Context × Local‑Sense) that justify it **SHALL** be cited in the UTS row with **Context name + edition**. Omit edition only if the Context has a single stable edition. See F.17 §6.

**CC‑F18‑7 (Sheet‑level coverage).** Within a thread’s UTS, the **set of rows** carrying unified names **SHALL** collectively cite **≥ 3 distinct Contexts**, ensuring breadth of evidence. Coverage is a property of the **sheet**, not of every single row. See F.17 §6 constraint.

**CC‑F18‑8 (No global words).** In Core text, **“Context” always means `U.BoundedContext`**; **discipline columns** may be used in teaching layouts but **is not** a bearer of meaning. Do not write context‑free claims of sameness. See E.10 and F.17 §5.

**CC‑F18‑9 (Didactic primacy).** A unified name **SHALL** be teachable on **one page**: its **UTS row** + a short narrative that a careful reader can replay (F.16 template). If it cannot be taught concisely, the naming attempt is premature.

**CC‑F18‑10 (No lifecycle connotations).** Names **SHALL NOT** encode imagined “maturity stages” or time‑ordering unless those are part of the concept’s intension. Stages belong in **state‑space** and dynamics narratives, not in names. (See A‑series CHR patterns.)

**CC‑F18‑11 (Strict distinction guard).** Names **SHALL** respect **A.7 Strict Distinction**: do not collapse **Role ↔ Method ↔ Work** or **Status ↔ Description** into one word. Align with F.11/F.12 where relevant.

**CC‑F18‑12 (Change control via F.13).** Renames, splits, merges, and retirements **SHALL** follow F.13’s lexical continuity rules; the UTS remains the canonical public surface for these changes.

**CC‑F18‑13 (Lexical Pareto discipline).** When a Name Card uses **NQD‑CAL (C.18)** to score label candidates, the **chosen Unified Tech label** **SHALL** lie on the **Pareto frontier** of the lexical Q‑tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` (per **C.16** ordinal discipline and P1’s NQD‑front definition), unless an explicit exception is recorded. If authors deliberately select a dominated candidate (e.g., to honour legacy regulation or user muscle memory), the Name Card’s notes **MUST** state the reason for stepping off the frontier.

**CC-F18-13 (NQD-front surfaced, with honest diversity).**  
When a Name Card is in **MintNew** mode, the **candidate label set** and the resulting **NQD-front of non-dominated label candidates** over the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` **SHALL** be explicitly recorded on the Card (at least as a small table or list), together with the NQD evidence hooks (`DescriptorMapRef`, `DistanceDefRef`, and a brief `Diversity_P` / coverage summary).  
Each candidate **SHALL** carry a **head-term family** tag; morphological or prepositional variants built on the same head (e.g. “X plane”, “plane of X”, “planar X”) **MAY NOT** be counted as distinct for Diversity_P. The Card **SHALL** indicate how many distinct head-term families are represented on the NQD-front.  
An NQD-front with fewer than **three** head-term families is permitted **only** if the Card records why no lexically more diverse alternatives survived the SemanticFidelity / AliasRisk filters (e.g., very narrow domain, frozen legacy idiom).

**CC-F18-14 (Selection from the front only).**  
The **Unified Tech** and **Plain** labels published on the UTS row for a unified concept **SHALL** be drawn from the currently recorded **NQD-front** on the Name Card. Publishing a Tech/Plain pair that is **not** on that front (or that is dominated with respect to the declared lexical Q-axes plus NQD) is **non-conformant**, except in explicit **DocumentLegacy** mode as defined in §5.1.

**CC-F18-15 (Mode declaration).**  
Every Name Card **SHALL** declare its `CardMode ∈ {MintNew, DocumentLegacy}`. For Core-surface naming of **U.Types** and other canonical FPF concepts, **MintNew** is the default; **DocumentLegacy** is permitted only when recording pre-existing external names and MUST (i) cite the legacy source, and (ii) either attach an NQD-front over viable FPF variants or record a short rationale why NQD search is out-of-scope.

### F.18:16 - Anti‑patterns & safe rewrites (normative)

> Each item names a **speaking error** and a **local‑first repair**. Use this as an author’s lint pass before proposing a unified name.

| #  | Anti‑pattern (do **not** say)                           | Why it fails                                                    | Safe rewrite (how to speak)                                                                                         |
| -- | ------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| A1 | “These terms are the same **because they look alike**.” | Cross‑context **spelling** is not evidence of conceptual identity. | “We assert sameness **via a Bridge**; the loss note explains what survives across Contexts.” (F.9)                     |
| A2 | “Use the BPMN word as our Tech label.”                  | Imports BPMN’s local commitments into the unified term.         | “Choose a **neutral** Unified Tech label; cite BPMN as a **SenseCell** in the row.” (F.5, F.17 §6)                  |
| A3 | “Merge *process* (recipe) with *process* (execution).”  | Collapses **MethodDescription** with **Work**.                  | “Split the concepts: one row for **MethodDescription**, another for **Work**; align them in examples.” (F.11/F.16)  |
| A4 | “Our name encodes the lifecycle stage.”                 | Lifecycle phrasing sneaks in time.                              | “Name the **concept**; show **state‑space** changes in examples, not in the label.” (A‑series CHR rationale)        |
| A5 | “Contextless glossary.”                                 | Violates local‑first; readers re‑globalise.                     | “Publish a **UTS** per thread; each row lists **Contexts** (Contexts+editions).” (F.17)                                |
| A6 | “We’ll fix synonyms later.”                             | Synonym sprawl grows costs.                                     | “Apply **E.10** rules now: one Tech, one Plain; retire extras via **F.13**.”                                        |
| A7 | “One mega‑row for everything service‑like.”             | Bundles distinct concepts; harms teachability.                  | “One **Concept‑Set per idea**; group with a **Block Plan** for pedagogy.” (F.17 §7)                                 |



#### F.18:16.1 - Canonical semantic unpacking for “contract” language (normative; used across FPF)

In FPF, everyday “contract” talk is treated as shorthand for a bundle of distinct roles. When precision matters (architecture, audit, compliance), authors **SHALL** avoid mapping “contract” to a single concept and instead disambiguate at least:

* **Service / promise clause (`U.PromiseContent`)** — the promised external effect + acceptance criteria (a spec/Standard), not a run (`U.Work`).
* **Utterance (`U.SpeechAct`)** — the published statement (a Description) that declares or invokes the promise content.
* **Commitment (`U.Commitment`)** — the deontic bond that binds an accountable agent/role to the promise content.
* **Work & evidence (`U.Work` + carriers)** — the actual enactment and the traces/metrics used to adjudicate fulfilment.

A “contract” bundle typically spans the whole A.6.B square; route each piece explicitly:

* `L-*`: definitions/invariants of the signature (“what it means”).
* `A-*`: admissibility/entry predicates (“when it can be applied”).
* `D-*`: duties/SLAs/penalties and who is accountable (“who is bound to what”).
* `E-*`: evidence/observability claims (“how fulfilment/violation is adjudicated”).

Example 2 (§F.18:18.2) shows one naming instantiation of this unpacking.

### F.18:17 - Migration notes (renames, splits, merges, retirements)

**M1 — Start from Contexts, not from the old global word.** When inheriting legacy names, first **re‑harvest** terms inside the chosen Contexts (F.2–F.3). Only then decide whether to **reuse** or **mint** (F.8).

**M2 — Preserve reader muscle memory without duplicating meaning.** Keep the **Plain** label close to familiar speech, but make the **Tech** label precise. If a legacy term is overloaded, publish it as a **deprecated alias** in Annexes, not as a second Tech label. (F.13; Part H “Deprecated Aliases”.)

**M3 — Prefer split‑then‑bridge over vague merges.** If one legacy word covers two distinct concepts, **split** into two rows and add a short **relation note** between them (e.g., “recipe vs run”). Do **not** hide the split under a wide new name. (F.7; F.16.)

**M4 — Keep identifiers stable; move rows between blocks.** When the **Block Plan** evolves, move rows rather than renumbering; record the move in the row’s **Notes** field. (F.17 §16.)

**M5 — Upgrade rationale quality with worked examples.** Every rename or split should be accompanied by a **one‑page example** that shows the new row in action across at least **two Contexts**. (F.16; “tell‑show‑show”.)


### F.18:18 - Worked examples (compact)

> Each example shows **how the Protocol steers naming** so engineers and managers can communicate without hidden Cross‑context leaks.  
> **Card hygiene shown explicitly:** each example **states the Kind and the Purpose/use‑domain** and **chooses Tech/Plain labels from a small NQD‑frontier** (seed set diversified by traditions, novelty/familiarity, and lexical form; see Part G patterns).
> **Head-term diversity:** each example **MUST** also state the **distinct head-term families** represented in its NQD candidate set (lexical “roots” such as *Recipe*, *Run*, *Episode*, not prepositional/morphological variants). This prevents faking Diversity_P with near-clones of one head.

#### F.18:18.1 - Example 1 — *MethodDescription* vs *Work* (recipe vs run)

* **Context harvest:**
  *BPMN 2.0 (2011):* “Process model” (recipe) and “Activity instance” (run).
  *PROV‑O (2013):* `prov:Plan` vs `prov:Activity`.
  *ITIL:* “Work instruction” vs “Change implementation record.”
* **Kind:** `U.MethodDescription` (design‑time artifact) **and** `U.Work` (run‑time occurrence).
* **Purpose / use‑domain:** planning/scheduling vocabulary across BPMN, PROV‑O, ITIL; separates *design recipe* from *execution episode* for governance and telemetry.
* **NQD‑front (seed candidates):**  
  *design‑time:* *Procedure*, *ProcessModel*, *MethodSpec*, *WorkflowDefinition*, *Recipe*, *MethodScript*  
  *run‑time:* *Run*, *Execution*, *Enactment*, *ActivityInstance*, *Job*, *Episode*
* **Head-term families used (design/run):**  
  *design-time heads:* {Procedure, ProcessModel, MethodSpec, WorkflowDefinition, Recipe, MethodScript}  
  *run-time heads:* {Run, Execution, Enactment, ActivityInstance, Job, Episode}
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.MethodDescription` / “recipe”; `U.Work` / “run”.  
  *Discarded highlights:* **Procedure** (collides with governance “procedure/policy”); **Execution** (overloaded in CS/security); 
* **Anti-pattern (for illustration only, non-conformant).**  
 > *Bad CandidateSet (lexically narrow):* {“Reference plane”, “Plane of reference”, “Planar reference”, “Ref. plane v2”}.  
 > All four are one **head-term family** (*plane*). Even if Diversity_P over raw strings looks high (four labels), **head-term diversity is 1**, so this set **fails** the F.18 diversity intent. A conformant Card would either: (a) add labels with other heads (e.g., *Layer*, *Track*, *Band*), or (b) explicitly record why other heads are rejected (AliasRisk, domain idiom) and accept low lexical Diversity_P with a rationale.
* **Enactment** (speech‑act nuance).
* **Bridges:** recipe↔run **related**, not identical; loss note “control‑flow vs. execution.”
* **Why it matters:** Managers can schedule **Work** while authors improve the **MethodDescription**—no category errors. The NQD‑front preserves tradition‑diverse, lexically stable options until a reasoned choice is made. (F.11/F.16; F.17 rows.)

#### F.18:18.2 - Example 2 — *Service* (promise) vs *SpeechAct* (utterance) vs *Commitment* (deontic)

* **Context harvest:**
  *IT service canon:* “SLA/OLA clause”, “ticket approved”.
  *Speech‑act theory:* “performative utterance”.
  *Org governance:* “approval signature”.
* **Kind:** `U.PromiseContent` (promise), `U.SpeechAct` (utterance), `U.Commitment` (deontic bond).
* **Purpose / use‑domain:** ops/governance vocabulary connecting ITSM, organizational policy, and pragmatics; separates saying, binding, and promising.
* **NQD‑front (seed candidates):**  
  *promise:* *Service*, *Offering*, *Provision*, *CapabilityOffer*  
  *utterance:* *SpeechAct*, *Performative*, *Utterance*, *Declaration*  
  *deontic bond:* *Commitment*, *Obligation*, *Binding*, *Duty*
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.PromiseContent` / “service (promise)”; `U.SpeechAct` / “utterance”; `U.Commitment` / “commitment”.  
  *Discarded highlights:* **Offering** (business‑model connotations); **Declaration** (too narrow for performatives); **Obligation** (legalese; narrower than commitment envelope).
* **Ontology note (informative):**
  `U.SpeechAct` and `U.Commitment` are defined normatively in Part A (A.2.9 and A.2.8 respectively). This F.18 card is a lexical/NQD anchor, not the ontology definition site.

* **Bridges:** utterance **institutes** commitment; commitment **binds** promise content; no synonymy claimed.
* **Why it matters:** Status tracking becomes intelligible without pretending that a “service” acts; the NQD‑front yields neutral, cross‑tradition readable labels. (F.12; F.17 blocks D/R.)

#### F.18:18.3 - Example 3 — *Characteristic* names without lifecycle bias

* **Context harvest:**
  *Quality canon:* “maturity level”; *Performance canon:* “throughput”.
 **Kind:** `U.Characteristic` (measurement names).
* **Purpose / use‑domain:** CHR‑compatible measurements for planning and performance; bridgeable across engineering and management.
* **NQD‑front (seed candidates):**  
  *readiness (ordinal):* *MaturityLevel*, *ReadinessLevel*, *PhaseReadiness*, *TRL*, *ReadinessScore*  
  *throughput (ratio):* *Throughput*, *Rate*, *ProcessingRate*, *OpsPerSecond*, *FlowRate*
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.ReadinessLevel` / “readiness level” (ordinal); `U.Throughput` / “throughput” (ratio).  
  *Discarded highlights:* **TRL** (tied to a specific scale/tradition); **Rate/OpsPerSecond** (over‑specific units baked in).
* **Narrative:** Dynamics are shown as **movement in state‑space**, not via lifecycle‑laden names such as “pre‑production process”.
* **Why it matters:** Prevents lifecycle/time from leaking into labels; the NQD‑front ensures neutrality and recognizability. (A‑series CHR rationale; F.17 §4–§6.)

### F.18:19 - FAQ (authoring hygiene)

**Q1. How many Contexts must a naming proposal cite?**
**A.** The **sheet** for a thread should cite **≥ 3** distinct Contexts overall; an individual row may cite fewer if the concept appears in fewer Contexts. The point is breadth at the **UTS** level, not token‑stuffing rows. (F.17 §6 constraint.)

**Q2. Can a Source Context’s term ever become the Tech label?**
**A.** Only if its form is **already neutral** and does **not** smuggle in that Context’s private commitments. When in doubt, pick a fresh neutral Tech label and keep the Source term in **SenseCells**. (F.5.)

**Q3. Where do we put discipline‑vantage views like “Operations” vs “Research”?**
**A.** Use the **discipline columns** in a teaching layout if helpful, but remember: **discipline columns are not Context columns** and carry no editions. (F.17 §5.)

**Q4. How do we keep names stable while the story evolves?**
**A.** Keep **row ids** stable; evolve placement via the **Block Plan** and record moves in **Notes**. Use F.13 for renames/splits/merges. (F.17 §16; F.13.)

**Q5. What if two teams insist on different Tech labels for the same concept?**
**A.** Publish **one** Tech label; treat the other as a **deprecated alias** (Annex). Bridge their local senses on the row. (F.13; Part H.)


### F.18:20 - 90‑second teaching script (for engineer‑managers)

> “**Local‑first** means we start in **context of meaning**—we harvest terms **inside** each Context and only then unify. A unified name is a **teachable promise**: one **Tech** label for precision, one **Plain** label for outreach. Its **row** in the **UTS** shows where the idea lives in real disciplines (the **SenseCells**) and how those Contexts connect (explicit **Bridges** with a brief loss note). We never equate terms by spelling; we argue sameness with a **bridge**. We also never bake stages or actors into names—those belong to **dynamics** and **roles**, not labels. When the story changes, we evolve names with **lexical continuity** rather than re‑inventing words. The result is a vocabulary managers and engineers can **hold on one page** and use the same way across projects.”

### F.18:21 - Acceptance Harness (SCR/RSCR) for F.18

**Purpose.** Provide auditable, notation‑independent checks that a proposed unified name (and its publication on a UTS line) satisfies the **local‑first** unification discipline. The harness extends the general unification checks in **F.15** with **naming‑specific** obligations.

#### F.18:21.1 - Static Conformance Rules (SCR‑UNIFY)

| ID                                                                                                                                                                                                       | Requirement (normative “SHALL/SHALL NOT”)                   | Why this exists (conceptual)                                 | Where this is reflected |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| **SCR‑U‑01 (Row‑first).** A unified Tech/Plain name **SHALL** be published **only** on a **Concept‑Set row** whose cells are SenseCells drawn from declared Contexts. No free‑floating names.               | Names are *lenses* onto a defended **row**, not vice‑versa. | **F.7** row‑as‑unit; **F.17** UTS row discipline.            | §F.7; §F.17             |
| **SCR‑U‑02 (Bridge‑only equivalence).** Cross‑context sameness **SHALL** be claimed **only** via an explicit **Bridge** with a relation kind and **CL** + loss/fit note.                                    | Prevents “string‑match identity”.                           | **F.9** Bridges; **F.0.1** principles.                       | §F.9                    |
| **SCR‑U‑03 (Neutral Tech).** The **Unified Tech** label **SHALL** be **neutral**—not lifted wholesale from any single Context **unless** the row’s Concept‑Set shows exact identity.                        | Avoids importing a local worldview as global.               | **F.5** naming neutrality; **F.17** 9.8 naming neutrality.   | §F.5; §F.17             |
| **SCR‑U‑04 (Twin registers).** Each row **SHALL** carry **Tech** and **Plain** names with the Part E register discipline; Plain is teacher‑friendly, Tech is morphology‑stable.                          | Satisfies didactic primacy without jargon creep.            | **E.10** registers; **F.5** naming rules.                    | §E.10; §F.5             |
| **SCR‑U‑05 (No window‑in‑name).** Variations by **time/phase/scale** **SHALL** be handled by **applicability windows** on **Statuses** (or examples), **NOT** by baking modifiers into the unified name. | Prevents type/status explosion by adjectives.               | **F.10/F.12** windows; **F.14** explosion guard.             | §F.10; §F.12; §F.14     |
| **SCR‑U‑06 (Heterogeneity).** A UTS block **SHALL** demonstrate **≥ 3** independent domain families across its rows, or an explicit Bias‑Annotation shall scope the claim.                               | Enforces trans‑disciplinary reach or honest scope.          | **F.17** invariants 3; **E.8** Bias‑Annotation.              | §F.17; §E.8             |
| **SCR‑U‑07 (Member≠Component sanity).** Names **SHALL NOT** imply holarchic composition when the row unifies **collections**; keep **MemberOf** distinct from **ComponentOf**.                           | Stops structural category errors.                           | Part F principles / anti‑patterns.                           | §9.8; §13               |
| **SCR‑U‑08 (One‑breath rationale).** Each row **SHALL** include a **single‑sentence** Unification Rationale that states **why** the cells denote the same thing despite wording differences.             | Keeps the argument visible and auditable.                   | **F.17** invariant 7.                                        | §F.17                   |
| **SCR‑U‑09 (Alias budget).** Per register, legacy aliases on a unified name **SHALL** be **≤ 1**; additional legacy labels go to Annex/Glossary.                                                         | Controls lexical drift while preserving continuity.         | **F.13** alias budget rule.                                  | §F.13                   |
| **SCR‑U‑10 (No Cross‑context rename).** A rename **SHALL** occur **within** the same Context or same row; Cross‑context “renames” are **prohibited**—use Bridges.                                                 | Keeps locality intact; forbids silent conflation.           | **F.13** continuity; **F.9** Bridges.                        | §F.13; §F.9             |
| **SCR‑U‑11 (Semantic read‑through).** A unified Tech/Plain name **SHALL** pass a **semantic read‑through**: the Name Card lists **5–10 diverse NQD archetypal situations** and the **NQD‑front notes** record rejected candidate and their **mismatch patterns**. | Prevents labels that mislead across the intended situations; ties lexical choice to demonstrated use. | §F.18 §4.2; §F.18 §5. | §F.18 |

#### F.18:21.2 - Regression Rules (RSCR‑UNIFY)

| ID                                                                                                                                                                       | Regression duty across editions                                        | Effect |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------ |
| **RSCR‑U‑E01 (Edition drift).** When a source Context updates, re‑validate the row: stable sense ⇒ **rename/alias**; changed sense ⇒ **split/merge** rows; never overwrite. | Preserves truthfulness without erasing history. **F.13** RSCR.         |        |
| **RSCR‑U‑E02 (CL honesty).** Bridges **SHALL NOT** increase their CL (claiming stronger sameness) without new witnesses; **SHOULD** reduce CL when editions diverge.     | Guards against optimism bias in equivalence. **F.17** migration cues.  |        |
| **RSCR‑U‑E03 (Alias creep).** Periodically prune aliases to the **≤ 1** budget per register.                                                                             | Maintains narratively crisp UTS. **F.13** RSCR‑Alias.                  |        |
| **RSCR‑U‑E04 (Name neutrality check).** If the Unified Tech label is traceable to one context’s idiom, re‑justify neutrality or retitle the row.                            | Keeps the name “ours,” not “theirs.” **F.17** 9.7–9.8.                 |        |
| **RSCR‑U‑E05 (Window misuse).** Reject newly proposed types that are really **windows** on an existing Status/Role.                                                      | Prevents explosion by adjectives. **F.14** S14/E11 patterns.           |        |

### F.18:22 - Migration & Deprecation Notes (informative, naming‑specific)

1. **Start from rows, not strings.** When consolidating legacy labels, **build or revisit the Concept‑Set row** first; only then pick the **Unified Tech/Plain** names. This keeps **meaning** primary. **(F.7, F.17)** 
2. **Prefer alias over merge.** If the *sense* is stable but the label misleads, **rename and retain one alias**; if the sense changed, **mint a new row** (no retrofits). **(F.13)**
3. **Resist modifier types.** New adjectives (e.g., *Peak*, *Remote*, *Night*) usually belong to **windows** or **examples**, not to the unified name. **(F.10/F.12/F.14)** 
4. **Keep neutrality visible.** If stakeholders push a brand‑coloured label, document why the chosen **Unified Tech** is **neutral** and include the brand as an **alias** in Glossary/Annex. **(F.5, F.17)** 
5. **Don’t globalise a Context.** Never move a Context label into the unified name as if it were universal. Use **Bridges** to relate Contexts, with an explicit **loss note**. **(F.0.1, F.9)** 

### F.18:23 - FAQ (authoring hygiene for engineer‑managers)

**Q1. Can we reuse a dominant industry term as the Unified Tech name?**
**A.** Only if the row’s Concept‑Set shows **exact identity** across Contexts; otherwise pick a **neutral** Unified Tech and list the industry label as an **alias** in the Glossary. **(F.5, F.17)** 

**Q2. Two terms look identical across Contexts—may we skip Bridges?**
**A.** No. **Sameness is argued, not spelled.** Publish a **Bridge** with relation kind and **CL** plus a short **loss/fit** note. **(F.9, F.0.1)** 

**Q3. When do we mint a new U.Type vs. add a new row vs. add an alias?**
**A.** Use **F.8 Mint‑or‑Reuse**: if the *intension* changes, **new U.Type**; if the *same thing* spans new Context, **new row**; if only the label misleads, **alias/rename**.

**Q4. Our team keeps proposing “qualified roles” (e.g., *Night‑Operator*). What do we do?**
**A.** Keep the **Role** unified and express qualifiers as **windows** on **Statuses** or as **example context**. This follows **F.14** and **F.12**.

**Q5. Can we compress two near‑equivalent rows into one to “simplify the sheet”?**
**A.** Only if the **one‑breath rationale** remains true after review and the Bridges support equivalence with the same or stronger CL; otherwise keep **two rows** with explicit differences. **(F.17, F.9)** 

### F.18:24 - Didactic distillation (90‑second script)

> **“Name on a row, never on a whim.”** In FPF we **speak on rows, not on vibes**: a **Name Card** ties each Tech/Plain pair to a concrete Context, Concept‑Set row, and SenseCells, with a small **NQD‑front** of rejected alternatives. This gives you **bridged precision** without losing **local comfort**. **Your UTS is the one page a careful mind can hold.**

### F.18:25 - SoTA‑Echoing (post‑2015 practice alignment)

* **Neural WSD & sense evaluation (2015→).** P2’s sense‑seed read‑through is a human‑scale analogue of modern **word‑sense disambiguation** evaluation, where models are scored by the fraction of examples assigned the correct sense and by error profiles across sense inventories. Post‑2015 neural WSD benchmarks (e.g., multi‑domain evaluations reported in ACL venues) motivate the explicit `{too‑narrow, on‑target, too‑wide, wrong‑prototype}` labelling and the `θ_P` threshold for **SemanticFidelity**.
* **Quality‑Diversity & multi‑objective search (MAP‑Elites, NSGA‑II families, 2015→).** P1’s NQD‑front and **CC‑F18‑13** follow the same discipline as QD/NSGA‑style archives in optimisation: maintain a **set of non‑dominated candidates** over a vector of objectives rather than a single scalar score. The lexical Q‑tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` is deliberately small so that human authors can inspect a Pareto frontier in the same way QD methods expose illumination archives.
* **Design‑space exploration & idea ranking (mechanical/industrial design, 2018→).** The PSOA‑style Name‑Card tables echo contemporary **design‑space ranking** practice, where candidate concepts are compared on diversity and quality rather than on a single “score”. Explicitly surfacing *why* one candidate dominates another improves auditability and supports teaching, mirroring recent work on ranking ideas for both diversity and quality in engineering design.
* **Semantic transparency & morphology in interfaces and code (HCI and PL practice, 2015→).** The strengthened **OperationalAffordance** guidance aligns with empirical results on **semantic transparency** of labels and identifier names: morphology that cues “actor vs activity vs artifact” improves comprehension and reduces error rates in both UIs and source code. F.18 turns these findings into a simple naming discipline (agentive forms for Roles, verbal forms for Methods, result nouns for Work/Artifacts) that can be enforced on Name Cards.

### F.18:26 - Relations

**Builds on:**
**F.0.1** Contextual Lexicon Principles (local meaning; bridge‑only Cross‑context claims). **F.1–F.3** Contexts → term harvesting → local sense clustering. **F.5** Naming discipline. **F.7** Concept‑Set construction. **F.8** Mint‑or‑Reuse decision lattice. **F.13** Lexical continuity (renames/aliases/splits/merges). **F.14** Anti‑explosion controls (bundles, SoD, windows). **F.15** SCR/RSCR harness. **F.17** UTS as the publication surface.  

**Constrains:** 
All patterns that propose or consume unified names and rows in Part F; any Part A/C pattern that cites U.Types on UTS rows inherits these naming duties (through the UTS linkage), while keeping **structural/epistemic/temporal** aspects distinct per Part E authoring rules.

**Coordinates with.**
**A.17/A.18** for measurement lexicon when rows concern measurable notions (Characteristic/Scale/Level/Coordinate vocabulary), ensuring neutral naming aligns with canonical terms and eases external alignment via Bridges.  

### F.18:End

# Part G – Discipline SoTA Patterns Kit

## G.Core - Part G Core Invariants

**Tag.** Architectural pattern (Part‑G core invariants hub; refactoring/deduplication)
**Stage.** *design‑time* (authoring discipline + ID‑stable routing; no run‑time mechanism)
**Primary hooks.** E.8 (pattern template), E.10 (lexical/ontological rules), E.19 (conformance discipline), A.6.7 (SuiteObligations + suite protocol pins), A.15.3 (planned baseline), A.19 (CN‑Spec), G.0 (CG‑Spec), A.19.CHR (CHR suite boundary), C.23 (SoS‑LOG), F.17 (UTS), F.15 (RSCR).

**Status.** Draft (Phase‑2 deliverable)  
**Placement.** Part G → immediately after `G.0` (without renumbering `G.0…G.13`)  
**Normativity.** Normative unless explicitly marked informative  

**Purpose.** Provide a *single owner* for Part‑G‑wide invariants (**delegation‑first routing**), plus a typed **RSCR trigger kind catalogue** and a **Default Ownership Index**, so Part G can be refactored without semantic drift or public‑ID breakage.

**Phase‑2 constraint.** `G.Core` is the only new Part‑G pattern introduced in Phase‑2; discipline/method/generator specifics remain in `G.x` as `Extensions`, citations to existing owner‑patterns, or Phase‑3 seeds (appendix) without new Phase‑2 norms.

**Post‑Phase‑2 evolvability policy.** The Phase‑2 restriction above is historical. From Phase‑3 onward, new Part‑G `PatternId`s are permitted when (i) they introduce a genuinely new **kit/pack class** (typically levels `G.2–G.5`), or (ii) they are required to preserve **single‑owner** discipline and wiring‑only separation. Method/discipline/generator specifics SHOULD still default to `GPatternExtension` modules under `G.x:Extensions` (scoped by `PatternScopeId = G.x:Ext.*` and `SemanticOwnerPatternId`), rather than adding new Part‑G patterns.

### G.Core:1 - Problem frame

Part G contains patterns for CG‑frame characterization and its downstream artefacts (cards, evidence graphs, bridge surfaces, refresh/shipping orchestration, parity harnesses, dashboards, interop surfaces). In the current spec, several invariants are already present as **suite obligations/protocol norms** and are **reused across Part G**.

*Part‑G‑wide* invariants reside in `G.Core` as a single-owner pattern so every `G.x` can:

* cite the core invariants rather than restating them, and
* isolate pattern-scoped specifics as `Extensions` without turning each `G.x` into a mixed bag of universal rules, kit surfaces, and method/generator descriptions.

This pattern (`G.Core`) therefore acts as the **deduplication hub** for FPF Part G.

### G.Core:2 - Problem

Without a single owner for Part‑G‑wide invariants, Part G drifts in at least six recurring ways:

1. **Shadow contract surfaces** emerge: downstream patterns restate CN‑Spec / CG‑Spec constraints, accidentally creating “local specs” that can diverge from the canonical contract surfaces.
2. **Crossing discipline becomes inconsistent**: “crossing events” and “crossing visibility” are described differently across `G.x`, causing ambiguity about what must be pinned (UTS/Path/policy‑ids/editions) and what triggers refresh/regression.
3. **Guard semantics drift**: tri‑state eligibility and “unknown handling” can be reinterpreted in local prose, producing hidden fourth statuses or implicit coercions.
4. **Hidden scalarization appears**: partial orders are silently collapsed into scalars, or totalization is introduced implicitly through “helpful” numeric summaries.
5. **Suite/kit/pack mixing blurs ownership**: downstream patterns drift into “owning” what should remain owned by the suite boundary (A.6.7/A.19.CHR), kit surfaces (each `G.x`), or shipping (G.10).
6. **Refactoring breaks public IDs**: CC items and trigger labels become hard to evolve because removing duplicates risks breaking external references.

Part G requires a single place where these invariants and refactoring disciplines live, while keeping Part G patterns modular and method/discipline specifics explicitly separated.

### G.Core:3 - Forces

* **Single source of truth vs. usability:** We must centralize universal invariants, but `G.x` must remain readable and pattern-scoped for authors.
* **Delegation-first vs. completeness:** Many norms already have canonical owners (A.6.7 / A.15.3 / A.19 / G.0 / A.19.CHR / E.*). G.Core must route to them rather than duplicating semantics.
* **Backwards compatibility:** Public CC IDs and legacy trigger tokens must remain stable; deduplication must not break citations.
* **Typed change control:** RSCR/refresh must become *id‑based* (catalogued trigger kinds) rather than prose-based “meaning”.
* **Strict distinction:** Keep contract surfaces (CN‑Spec, CG‑Spec), suites, kits/surfaces, policies, planned baselines, audits, and refresh orchestration distinct.
* **Minimal specificity naming:** New IDs must be kind‑suffixed and minimally specific, to reduce semantic lock‑in while remaining precise.
* **Phase‑2 scope discipline:** `G.Core` must not become a container for discipline/method/generator taxonomies; those remain pattern-scoped (`Extensions`), delegated to existing owner‑patterns, or marked Phase‑3 seeds (appendix) without new Phase‑2 norms.

### G.Core:4 - Solution

`G.Core` establishes Part‑G‑wide invariants as **routing rules + typed catalogs + authoring discipline**.

#### G.Core:4.1 - Delegation-first routing for Part‑G‑wide invariants

`G.Core` is a *routing hub*, not a “second spec”. For any Part‑G‑wide invariant that already has an owner, `G.Core`:

1) standardises naming via `SuiteObligations.*` (A.6.7:4.2), and  
2) records where the invariant is owned, so downstream patterns cite rather than restate.

**Routing table (normative index; no semantic duplication).**

| Obligation handle | Canonical owner(s) | Part‑G note |
| --- | --- | --- |
| `transport_declarative_only` + `cg_spec_cite_required_for_numeric_ops` | A.6.7 + A.19 (CN‑Spec) + G.0 (CG‑Spec) + A.19.CHR | CN/CG are *pins*, not copies (“contract surfaces are pins, not copies”). No embedded/shadow contract surfaces. |
| `bridge_only_crossings` | A.6.7 + E.18 | Any cross‑Context/plane/kind move is Bridge‑mediated; no implicit crossings. |
| `crossing_visibility_required` | E.18 (CrossingSurface) + A.6.7 | Crossing visibility is a published **CrossingSurface**. `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL surfaces, BridgeCards, CrossingSurface registries, and UTS rows for crossing artefacts) are treated as CrossingSurface edits. If the required CrossingSurface is missing/non‑conformant, downstream consumers MUST **abstain** from cross‑Context/plane reuse (no silent crossings). |
| `two_bridge_rule_for_described_entity_change` | A.6.7 | describedEntity retargeting requires an explicit KindBridge (`CL^k`) in addition to any Context/Plane Bridge. |
| `guard_decision_tristate(pass|degrade|abstain)` + `unknown_never_coerces_to_pass` | A.6.7 + C.23 | `GuardDecision := {pass|degrade|abstain}` only; `unknown` maps to `degrade`/`abstain` via explicit SoS‑LOG branch/policy pins. |
| `penalties_route_to_r_eff_only` | A.6.7 | Penalties affect the **R lane (R_eff)** only; **F/G invariants** must not be altered by penalties. |
| `no_silent_scalarisation_of_partial_orders` + `no_silent_totalisation` | A.6.7 | Partial orders stay set‑valued; no silent scalar ranks or “helpful” totalisation. |
| `planned_slot_filling_in_work_planning_only` + `finalize_launch_values_in_work_enactment_only` + `gate_decision_separation` | A.15.3 + A.19.CHR + A.6.7 | Planned baselines are WorkPlanning‑only; launch/finalization values are WorkEnactment‑only; planning does not own GateDecision/DecisionLog semantics. |
| `DefaultOwnershipIndex.single_owner_per_DefaultId` | this pattern | Any default has exactly one owner; `G.Core.DefaultOwnershipIndex` is an index, not a second spec. |

This pattern also owns four pieces of Part‑G‑wide infrastructure that are **not** already owned elsewhere:

* the typed **RSCRTriggerKindId catalogue** (single writer),
* the **Default Ownership Index** (single owner per DefaultId; index only), and
* the **Δ‑discipline** for ID‑stable deduplication (delegation without public‑ID breakage), and
* the **linkage compression catalogues** (`GCoreConformanceProfileId`, `GCoreTriggerSetId`, `GCorePinSetId`) used to keep `G.x` linkage sections small.

#### G.Core:4.2 - Mandatory `G.Core linkage` contract for every `G.x`

Every pattern `G.x` in Part G SHALL include a short, explicit **Core linkage** section that is notation‑independent and id‑based.

* Relations: `Builds on: G.Core`.
* Solution: include a section named `G.x:<n> - G.Core linkage (normative)` that contains a `GCoreLinkageManifest` listing, at minimum:

  * `CoreConformanceProfileIds := { GCoreConformanceProfileId… }` *(preferred)* and/or `CoreConformanceIds := { CC‑GCORE‑… }`
  * `RSCRTriggerSetIds := { GCoreTriggerSetId… }` *(preferred)* and/or `RSCRTriggerKindIds := { RSCRTriggerKindId… }`
  * `CorePinSetIds := { GCorePinSetId… }` *(preferred)* and/or `CorePinsRequired := { … }` *(pins/refs surfaced by the kit; include policy‑id pins and edition pins when applicable; list only additions/overrides if pin sets are used)*
  * `DefaultsConsumed := { DefaultId… }` *(ids only; owner is resolved via `G.Core.DefaultOwnershipIndex`; cite owner, don’t restate)*
  * `TriggerAliasMapRef?` *(present or cited) if the pattern uses local trigger tokens*

**Nil‑elision (normative size rule).** Any field whose value is `∅` MAY be omitted; omission means `∅` and does not relax any obligation.

**Expansion rule (normative).** If profile/set ids are used, the effective `CoreConformanceIds` / `RSCRTriggerKindIds` / `CorePinsRequired` are the unions of their expansions plus any explicitly listed ids (see `G.Core:4.2.2`, `G.Core:4.2.3`, and `G.Core:4.3.4.2`).

##### G.Core:4.2.1 - `GCoreLinkageManifest` (canonical shape)

`GCoreLinkageManifest` is the minimal, pattern‑local wiring manifest for citing `G.Core` without duplicating universal prose.

A `G.x` MAY render the manifest as prose, a table, or structured notation, but the ids SHALL be recoverable by authoring review:

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds?: {GCoreConformanceProfileId…},
  CoreConformanceIds?: {CC‑GCORE‑…},
  RSCRTriggerSetIds?: {GCoreTriggerSetId…},
  RSCRTriggerKindIds?: {RSCRTriggerKindId…},
  CorePinSetIds?: {GCorePinSetId…},
  CorePinsRequired?: {…pin ids…},
  DefaultsConsumed?: {DefaultId…},
  TriggerAliasMapRef?: TriggerAliasMapRef
⟩`

##### G.Core:4.2.2 - `GCoreConformanceProfileId` catalogue (compression primitive)

A `GCoreConformanceProfileId` is a stable identifier for a named set of `CC‑GCORE‑*` items. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

| GCoreConformanceProfileId | Expands to `CC‑GCORE‑*` (set) | Notes |
| --- | --- | --- |
| `GCoreConformanceProfileId.PartG.AuthoringBase` | `{CC‑GCORE‑CN‑CG‑1, CC‑GCORE‑CROSS‑1, CC‑GCORE‑PEN‑1, CC‑GCORE‑SET‑1, CC‑GCORE‑P2W‑1, CC‑GCORE‑DEF‑1, CC‑GCORE‑TRIG‑1, CC‑GCORE‑TRIG‑2, CC‑GCORE‑TRIG‑3, CC‑GCORE‑TRIG‑4, CC‑GCORE‑ID‑1, CC‑GCORE‑ID‑2, CC‑GCORE‑LINK‑1, CC‑GCORE‑LINK‑2}` | Default baseline for most Part‑G kits. |
| `GCoreConformanceProfileId.PartG.TriStateGuard` | `{CC‑GCORE‑GUARD‑1}` | Add when the kit defines/consumes eligibility/guard outcomes. |
| `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` | `{CC‑GCORE‑UTS‑1}` | Add when the kit mints/evolves public ids (UTS rows). |
| `GCoreConformanceProfileId.PartG.ShippingBoundary` | `{CC‑GCORE‑SKP‑1}` | Add when shipping boundaries are in scope for the kit. |

##### G.Core:4.2.3 - `GCorePinSetId` catalogue (compression primitive)

A `GCorePinSetId` is a stable identifier for a named set of commonly recurring **pin obligations** used in Part‑G kits. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

**Conditional pins (normative).** In pin‑set expansions below, a pin marked with `?` is **conditional**: it **MUST** be present iff the pattern actually uses the corresponding surface/artefact class; otherwise it MAY be omitted (nil‑elision permitted) and is treated as `∅`. A `G.x` MAY strengthen a conditional pin to unconditional by listing it explicitly in `CorePinsRequired`.

| GCorePinSetId | Expands to `CorePinsRequired` (set) | Notes |
| --- | --- | --- |
| `GCorePinSetId.PartG.AuthoringMinimal` | `{CG-FrameContext, describedEntity := ⟨GroundingHolon, ReferencePlane⟩, CNSpecRef.edition, CGSpecRef.edition}` | Baseline scope+contract pins for most Part‑G authoring kits (design‑time, citable, refreshable). |
| `GCorePinSetId.PartG.CrossingVisibilityPins` | `{BridgeId/BridgeCardId, BridgeMatrixId?, CL/CL^k/CL^plane, Φ/Ψ/Φ_plane policy-ids, CrossingSurfaceId?, UTSRowId[]?, PathId[]/PathSliceId[]?}` | Use when the kit asserts or consumes crossings (Bridge‑only + visible). Conditional pins cover “only if that surface is used” cases (UTS publication, path‑citable evidence, explicit CrossingSurface reference). |

#### G.Core:4.3 - RSCR Trigger Catalogue and docking discipline

`G.Core` is the **single writer** for Part‑G‑wide trigger kinds.

##### G.Core:4.3.1 - Definitions

* **RSCRTriggerKindId**
  Canonical, stable identifier for a *trigger kind* (a class of “why RSCR/refresh must fire”). Cross-pattern reason code.

* **RSCRTriggerAliasId**
  Pattern-scoped human label/token kept for ergonomics/backward compatibility (e.g., `G.11:T4`, `G.6:H3:lane-tag correction`).

* **TriggerAliasMap**
  Mapping table: `RSCRTriggerAliasId → {RSCRTriggerKindId…}` (1..n).

* **RSCRTrigger**
  Minimal conceptual form (notation-independent):

  ```
  RSCRTrigger := ⟨
    triggerKindId: RSCRTriggerKindId,
    scope: PathSliceId[] | PathId[] | PatternScopeId,
    payloadPins: { …id pins… }
  ⟩
  ```

  Where `payloadPins` contains any edition pins, policy-ids, Bridge ids, evidence pins, regression-set ids, etc., required to make the trigger actionable.

##### G.Core:4.3.2 - Owner model

* TriggerOwner := `G.Core`.
* Any new trigger kind SHALL be added to `G.Core` first.
* Other patterns MAY define aliases only (or cite shared alias maps), and MUST map aliases to canonical kinds.

##### G.Core:4.3.3 - Authoring rules

* **No implicit triggers:**
  Any RSCR/SCR/refresh artefact that *records reasons* MUST record canonical `RSCRTriggerKindId`. Aliases may be recorded as labels, but must not be the only reason code.

* **No implicit overloading:**
  A local token string (e.g., `T4`) SHALL NOT silently change meaning across patterns; namespace is part of the alias (`G.11:T4` ≠ `A.20:T4`).

* **Granularity discipline:**
  If a local cause is narrower than an existing canonical kind, map it to that kind and keep the nuance as a local scope note. If the difference matters for planning/selection, add a new canonical kind.

* **Multi-cause discipline:**
  When an event spans multiple canonical kinds, record multiple triggers (preferred) or map the alias to a set `{…}` and require emitting the full set.

##### G.Core:4.3.4 - Seed canonical catalogue (Phase‑2 minimum)

The Phase‑2 stabilized canonical catalogue (based on the Phase‑2 inventory; sufficient to dock legacy `G.6:H3` and `G.11:T0…T7` triggers and to populate `RSCRTriggerKindIds` in `G.0…G.13`):

* `RSCRTriggerKindId.LegalitySurfaceEdit`
* `RSCRTriggerKindId.PenaltyPolicyEdit`
* `RSCRTriggerKindId.CrossingSurfaceEdit`
* `RSCRTriggerKindId.ReferencePlaneEdit`
* `RSCRTriggerKindId.EditionPinChange`
* `RSCRTriggerKindId.TokenizationOrNameChange`
* `RSCRTriggerKindId.PolicyPinChange`
* `RSCRTriggerKindId.TelemetryDelta`
* `RSCRTriggerKindId.FreshnessOrDecayEvent`
* `RSCRTriggerKindId.EvidenceSurfaceEdit`
* `RSCRTriggerKindId.MaturityRungChange`
* `RSCRTriggerKindId.BaselineBindingEdit`
* `RSCRTriggerKindId.DefaultOwnerChange`

##### G.Core:4.3.4.1 - Canonical kind definitions (normative, minimal)

Each `RSCRTriggerKindId` SHALL have a short, stable definition in `G.Core` (single-writer) to prevent semantic drift.

| RSCRTriggerKindId | Minimal meaning (cause class) | Typical payload pins (non-exhaustive) |
| --- | --- | --- |
| `RSCRTriggerKindId.LegalitySurfaceEdit` | A legality surface changed (CG‑Spec: ComparatorSet/SCP/Γ_fold/MinimalEvidence, or equivalent legality inputs). | `CGSpecRef.edition`, `ComparatorSetRef.edition`, `SCPRef.edition`, `ΓFoldRef.edition` |
| `RSCRTriggerKindId.PenaltyPolicyEdit` | A penalty / Φ / Ψ / FailureBehavior / SoS‑LOG branch policy changed. | penalty policy ids, `Φ`/`Ψ` policy ids, SoS‑LOG branch id pins |
| `RSCRTriggerKindId.CrossingSurfaceEdit` | A crossing surface changed (Bridge/CL routing, crossing registry cards, crossing policy pins), including `edition_key` changes of crossing‑relevant artefacts (BridgeCards, CrossingSurface registries, UTS rows for crossing artefacts). | `BridgeId/BridgeCardId`, `BridgeMatrixId?`, `CL*` ids, crossing policy ids, `UTSRowId[]`, `PathId/PathSliceId?` |
| `RSCRTriggerKindId.ReferencePlaneEdit` | ReferencePlane or plane-routing surface changed. | `ReferencePlaneId`, plane-policy ids |
| `RSCRTriggerKindId.EditionPinChange` | Any pinned edition relevant to downstream artifacts changed (including **`CNSpecRef.edition`**, `CGSpecRef.edition`, comparator/method/descriptor/distance/etc.). Crossing‑artefact edition_key changes are additionally classified as `CrossingSurfaceEdit` per multi‑cause discipline. | changed `*.edition` pins, affected `PathSliceId`s |
| `RSCRTriggerKindId.TokenizationOrNameChange` | A published tokenization / naming / alias surface changed in a way that can affect docking, citations, or dispatch (e.g., UTS Name Cards, twin labels, alias maps). | affected `UTSRowId[]`, `NameCardId[]`, alias ids / maps |
| `RSCRTriggerKindId.PolicyPinChange` | A policy-id pin used by characterization changed (selection, insertion, emission, routing, refresh policy, etc.). | policy ids (and other non-edition configuration pins when they are explicitly pinned) |
| `RSCRTriggerKindId.TelemetryDelta` | Telemetry inputs that influence refresh/selection changed (not merely display-only). | telemetry ids/refs, `Audit`-published pins |
| `RSCRTriggerKindId.FreshnessOrDecayEvent` | Time/freshness/decay conditions affecting validity changed (window shift, decay thresholds, freshness policy edits). | freshness window refs/ids, decay/freshness policy ids |
| `RSCRTriggerKindId.EvidenceSurfaceEdit` | Evidence graph / evidence surface changed in ways that affect admissibility/acceptance/comparison. | evidence pins, `EvidenceGraph` refs, affected `PathId`s |
| `RSCRTriggerKindId.MaturityRungChange` | Maturity rung/ladder state changed for relevant artifacts or paths. | maturity rung ids, affected scopes |
| `RSCRTriggerKindId.BaselineBindingEdit` | Planned baseline bindings changed (planned slot fillings / binding refs), requiring a re-run along the P2W path. | `SlotFillingsPlanItem` refs, planned pins, variance pins |
| `RSCRTriggerKindId.DefaultOwnerChange` | The owner of a `DefaultId` (as recorded in `G.Core.DefaultOwnershipIndex`) changed, or a default row was added/deprecated. | affected `DefaultId.*`, old owner ref, new owner ref |

##### G.Core:4.3.4.2 - Canonical trigger sets (compression primitive)

`GCoreTriggerSetId` identifies a named set of `RSCRTriggerKindId` values. A `G.x` MAY cite trigger sets in `RSCRTriggerSetIds` instead of repeating long `RSCRTriggerKindIds` lists.

| GCoreTriggerSetId | RSCRTriggerKindIds (set) | Notes |
| --- | --- | --- |
| `GCoreTriggerSetId.CGSpecGate` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers CG‑Spec legality‑gate kits (e.g., `G.0`). |
| `GCoreTriggerSetId.SoTAHarvestSynthesis` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers SoTA harvesting/synthesis packs (e.g., `G.2`). |
| `GCoreTriggerSetId.EvidenceGraphKit` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers EvidenceGraph/SCR kits (e.g., `G.6`). |
| `GCoreTriggerSetId.BridgeCalibrationKit` | `{RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.BaselineBindingEdit}` | Covers bridge calibration/CL kits (e.g., `G.7`). |
| `GCoreTriggerSetId.RefreshOrchestration` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers refresh orchestration (e.g., `G.11`). |

##### G.Core:4.3.5 - Initial alias maps

These alias maps are normative docking artefacts and preserve legacy tokens while moving semantics to canonical ids.

**TriggerAliasMap.G11**
Based on the existing trigger catalogue in `G.11` (`T0…T7`).

* `G.11:T0 → { RSCRTriggerKindId.PolicyPinChange }`
* `G.11:T1 → { RSCRTriggerKindId.TelemetryDelta }`
* `G.11:T2 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T3 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T4 → { RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.11:T5 → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.11:T6 → { RSCRTriggerKindId.MaturityRungChange }`
* `G.11:T7 → { RSCRTriggerKindId.PolicyPinChange }`

**TriggerAliasMap.G0 (reserved; empty in Phase‑2).**
Map any stable legacy registry‑hook labels emitted/recorded by `G.0` to the canonical kinds above (typically `LegalitySurfaceEdit`, `PenaltyPolicyEdit`, `CrossingSurfaceEdit`, `ReferencePlaneEdit`, `TokenizationOrNameChange`), preserving the original label text as `RSCRTriggerAliasId`. If none exist, `G.0` SHOULD emit canonical `RSCRTriggerKindId` values directly.
 
**TriggerAliasMap.G6**
EvidenceGraph `H3` example causes → canonical kinds:

* `G.6:H3:freshness/decay change → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.6:H3:Bridge CL/CL^k or loss update → { RSCRTriggerKindId.CrossingSurfaceEdit }`
* `G.6:H3:Φ/Ψ policy change → { RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.6:H3:lane tag correction → { RSCRTriggerKindId.EvidenceSurfaceEdit }`
* `G.6:H3:ReferencePlane correction → { RSCRTriggerKindId.ReferencePlaneEdit }`
* `G.6:H3:QD/OEE artefact updates (U.DescriptorMapRef.edition/DistanceDef, EmitterPolicyRef, InsertionPolicyRef, archive K-capacity) → { RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange }`

#### G.Core:4.4 - Default Ownership Index

`G.Core` provides an index of Part‑G defaults with a **single owner** per `DefaultId`. The index is not a “second spec”; it is a cross-reference table that points to the *true owner* (a CC item, policy‑id, or TaskSignature rule) and states applicability conditions.

##### G.Core:4.4.1 - Definitions

* **DefaultId**
  Stable identifier of a default (a default constant or default rule).

* **DefaultOwnerRef**
  A reference to the single owner of the default (e.g., a CC item id like `CC‑G5.23`, or a policy id, or a TaskSignature rule definition).

##### G.Core:4.4.2 - Rules

* Exactly one owner per `DefaultId`.
* Any other mention in `G.x` MUST be a citation/delegation to the owner, not a competing statement.
* A default may be conditional (default-rule) with explicit applicability conditions.
* The Default Ownership Index SHALL NOT be used to “smuggle” mandatory invariants as defaults. Invariants remain invariants (typically routed via `CC‑GCORE‑…` to canonical owners).

##### G.Core:4.4.3 - Seed Default Ownership entries (Phase‑2 minimum)

| DefaultId                       | DefaultOwnerRef                                           | Notes |
| ------------------------------ | --------------------------------------------------------- | ----- |
| `DefaultId.PortfolioMode`       | `CC‑G5.23`                                                | Existing owner; other mentions delegate to it. |
| `DefaultId.DominanceRegime`     | `CC‑G5.28`                                                | Existing owner; other mentions delegate to it. |
| `DefaultId.GammaFoldForR_eff`   | `CC‑G5.4`                                                 | Default Γ‑fold for `R_eff` is weakest‑link; overrides require explicit CAL support. |

This table may grow over time; the rule is that the **owner must already exist** (or be intentionally set to `G.Core` when the default is truly Part‑G‑wide and not owned elsewhere). Any change in a row (add/remove/change owner) SHALL be treated as a refresh‑sensitive edit and recorded as `RSCRTriggerKindId.DefaultOwnerChange` (payload: affected `DefaultId.*`, old owner ref, new owner ref).

#### G.Core:4.5 - ID continuity protocol (Δ‑discipline)

When moving universal norms out of `G.x` into `G.Core`:

* existing public CC ids in `G.x` that may be referenced externally SHALL NOT be deleted or renamed;
* such CC items SHALL become **delegation** items that point to the relevant `CC‑GCORE‑…` item(s);
* each `G.x` SHALL add exactly one bridge CC item `CC‑Gx‑CoreRef` (first in its CC list) that makes linked `CC‑GCORE‑…` items mandatory for `G.x` conformance.

Legacy trigger tokens (e.g., `G.11:T*`, `G.6:H3:*`) are preserved as aliases and MUST map to canonical trigger kinds.

Non-CC public identifiers (e.g., `UTSRowId`, `RSCRTriggerAliasId`, deprecation notices, edition bumps) MUST obey the same Δ-discipline: preserve old ids; represent drift via alias/deprecation/edition evolution (see `F.17 (UTS)`); and emit canonical trigger kinds (`RSCRTriggerKindId.TokenizationOrNameChange`, `RSCRTriggerKindId.EditionPinChange`) when downstream impact is possible.

#### G.Core:4.6 - Explicit non-goals

`G.Core` does not:

* introduce CG‑frame kit entities (e.g., BridgeMatrix/ReferencePlane/Φ registries); those remain in their owning `G.x`;
* introduce method-family taxonomies, discipline packs, or generator orchestration mechanisms; those remain as `Extensions` in their owners (e.g., synthesis/shipping/refresh patterns);
* define refresh algorithms; it defines trigger kinds and docking only.

---

### G.Core:5 - Archetypal grounding

**Tell.**
In Phase‑2 refactoring, `G.Core` is the hub that allows each `G.x` to become structurally predictable: (a) a short, normative “Core linkage” slice, and (b) pattern‑scoped `Extensions`. Universal obligations are routed to canonical owners (A.6.7 / A.15.3 / A.19 / G.0 / A.19.CHR), while RSCR causes and default ownership become typed and single-owned.

**Show 1: Refresh triggers without semantic drift.**
`G.11` already uses trigger tokens `T0…T7`. `G.Core` keeps them as aliases and maps them to canonical trigger kinds (e.g., `TelemetryDelta`, `EditionPinChange`, `CrossingSurfaceEdit`). This makes RSCR reason codes consistent across patterns and avoids re-explaining trigger semantics in every pattern.

**Show 2: Resolving competing defaults.**
If multiple patterns imply a default for `PortfolioMode`, the Default Ownership Index points to a single owner (currently `CC‑G5.23`). Other patterns (e.g., bundles/log patterns) must cite that owner or delegate to it, rather than restating the default with slightly different wording. This preserves intent while preventing drift and ambiguity. 

### G.Core:6 - Bias-annotation (informative)

* **Centralization bias:** A single hub can become too “thick”. Mitigation: delegation-first routing; keep only true Part‑G invariants and typed indices here.
* **Over-typing bias:** A trigger catalogue can become overly granular. Mitigation: granularity discipline + scope notes; only add new kinds when planning/selection needs it.
* **Refactor rigidity bias:** Preserving IDs can feel cumbersome. Mitigation: delegation items preserve IDs while enabling deduplication.
* **Default absolutism bias:** Defaults may require conditional rules. Mitigation: Default Ownership Index allows conditional default rules with explicit applicability conditions.
* **Single-writer bias:** prefers single‑writer *authoring* for catalogs and explicit ownership tables.  
  *Mitigation:* delegation-first routing; keep catalogs minimal; avoid “second specs”.
* **Architectural bias:** centralizes invariants to prevent accidental coupling across `G.x`.  
  *Mitigation:* keep core thin; force `Extensions` to remain pattern‑scoped.
* **Ontological/epistemic bias:** enforces strict distinction between contract surfaces, kits, mechanisms, and orchestration.  
  *Mitigation:* allow didactic scope notes while keeping normative surface id‑based.
* **Pragmatic bias:** adds authoring overhead (linkage sections, alias maps).  
  *Mitigation:* one small mandatory bridge CC item per pattern (`CC‑Gx‑CoreRef`) and short linkage slices only.
* **Didactic bias:** risks “glossy hub prose” that hides missing CC coverage.  
  *Mitigation:* enforce CC/Solution coherence (E.19) and keep invariants checkable via `CC‑GCORE‑…`.

### G.Core:7 - Conformance checklist (normative) — **CC‑GCORE**

Conformance items are authoring obligations and are enforced transitively by `CC‑Gx‑CoreRef` in every `G.x`.

| ConformanceId        | Statement |
| -------------------- | --------- |
| **CC‑GCORE‑DEL‑1**   | A conforming `G.Core` SHALL be delegation‑first: if a norm is already owned by A.6.7 / A.15.3 / A.19 / G.0 / A.19.CHR / E.*, `G.Core` routes to it rather than duplicating semantics. |
| **CC‑GCORE‑CN‑CG‑1** | Any pattern in Part G that builds on `G.Core` SHALL cite `CN‑Spec` and `CG‑Spec` as the only contract/legality surfaces and SHALL NOT introduce shadow specs (incl. complying with `SuiteObligations.transport_declarative_only` and `SuiteObligations.cg_spec_cite_required_for_numeric_ops`). |
| **CC‑GCORE‑OBL‑1**   | A conforming `G.Core` SHALL treat the obligation vocabulary in `A.6.7:4.2` as the canonical naming surface for Part‑G‑wide obligations and SHALL NOT introduce competing obligation names for the same norms. |
| **CC‑GCORE‑CROSS‑1** | A Part‑G pattern that introduces or consumes crossings SHALL enforce `SuiteObligations.bridge_only_crossings` and `SuiteObligations.crossing_visibility_required` (CrossingSurface per E.18); SHALL prohibit implicit crossings; SHALL treat `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL/CrossingSurface registries and UTS rows for crossing artefacts) as `RSCRTriggerKindId.CrossingSurfaceEdit` (and, when an edition pin is involved, also `RSCRTriggerKindId.EditionPinChange` per multi‑cause discipline); and SHALL route `SuiteObligations.two_bridge_rule_for_described_entity_change` to its canonical owner. |
| **CC‑GCORE‑GUARD‑1** | A Part‑G pattern SHALL treat `GuardDecision := {pass|degrade|abstain}` as the only admissibility/eligibility decision domain (`SuiteObligations.guard_decision_tristate(pass|degrade|abstain)`); `unknown` SHALL NOT silently coerce to `pass` (`SuiteObligations.unknown_never_coerces_to_pass`); “sandbox/probe‑only” SHALL be expressed via SoS‑LOG branch pins (policy/FailureBehavior) (see `C.23`), not as an extra decision value. |
| **CC‑GCORE‑PEN‑1**   | A Part‑G pattern SHALL route penalties/assurance loss to the **R lane (`R_eff`) only** (`SuiteObligations.penalties_route_to_r_eff_only`) and SHALL preserve **F/G invariants** under penalties (penalties do not alter legality/invariant lanes). |
| **CC‑GCORE‑SET‑1**   | A Part‑G pattern SHALL preserve set-return semantics for partial orders and SHALL prohibit silent scalarization/totalization (`SuiteObligations.no_silent_scalarisation_of_partial_orders`, `SuiteObligations.no_silent_totalisation`); any scalar summary SHALL be report-only unless declared as a lawful comparator surface. |
| **CC‑GCORE‑SKP‑1**   | A Part‑G pattern SHALL preserve the suite/kit/pack distinction (A.19.CHR) and SHALL keep shipping concerns owned by their canonical owner patterns (e.g., G.10) rather than embedding shipping semantics into unrelated kits or core invariants. |
| **CC‑GCORE‑P2W‑1**   | A Part‑G pattern that uses planned baselines SHALL anchor them via `SlotFillingsPlanItem` in WorkPlanning (`SuiteObligations.planned_slot_filling_in_work_planning_only`) and SHALL finalize launch values only in WorkEnactment (`SuiteObligations.finalize_launch_values_in_work_enactment_only`); gate decisions remain separated per `SuiteObligations.gate_decision_separation`. |
| **CC‑GCORE‑LINK‑1**  | Every conforming `G.x` SHALL satisfy `G.Core:4.2` by providing a `G.x:<n> - G.Core linkage (normative)` section containing a `GCoreLinkageManifest` (incl. either `CoreConformanceProfileIds` or `CoreConformanceIds`, either `RSCRTriggerSetIds` or `RSCRTriggerKindIds`, and either `CorePinSetIds` or `CorePinsRequired` (or both)). Nil‑elision is permitted for `∅` fields. |
| **CC‑GCORE‑LINK‑2**  | Every conforming `G.x` SHALL include `CC‑Gx‑CoreRef` as the first checklist item; it SHALL make mandatory the effective `CoreConformanceIds` (including expansions of any `CoreConformanceProfileIds`) declared in the linkage manifest. |
| **CC‑GCORE‑UTS‑1**   | If a Part‑G pattern mints, deprecates, or evolves any public identifier, it SHALL publish/update the corresponding UTS entries and cite them via `UTSRowId` pins, delegating UTS semantics (twin labels, alias/deprecation discipline, edition pins) to its canonical owner `F.17 (UTS)`. |
| **CC‑GCORE‑ID‑1**    | When deduplicating, existing public CC ids in `G.x` SHALL NOT be deleted/renamed; they SHALL become delegation items to relevant `CC‑GCORE‑…` items. |
| **CC‑GCORE‑ID‑2**    | Public id continuity applies beyond CC item ids: `UTSRowId` rows, `RSCRTriggerAliasId` tokens (e.g., `T0…T7`), deprecation notices, and edition bumps SHALL preserve prior ids and express drift via alias/deprecation/edition evolution (never by reusing/redefining an old id). When downstream behaviour can change, the change SHALL emit a canonical `RSCRTriggerKindId` (e.g., `TokenizationOrNameChange`, `EditionPinChange`). |
| **CC‑GCORE‑TRIG‑1**  | A conforming `G.Core` SHALL define the canonical `RSCRTriggerKindId` catalogue and SHALL be its single writer. |
| **CC‑GCORE‑TRIG‑2**  | Any `G.x` that uses local trigger tokens SHALL provide (or cite) a `TriggerAliasMap` mapping each alias to canonical `RSCRTriggerKindId`. |
| **CC‑GCORE‑TRIG‑3**  | Any artefact that records RSCR/SCR/refresh reasons SHALL record canonical `RSCRTriggerKindId` (aliases may be recorded as labels only). |
| **CC‑GCORE‑TRIG‑4**  | A conforming `G.Core` SHALL keep `TriggerAliasMap.*` consistent with the owner patterns’ legacy trigger catalogues (e.g., `G.11:T*`). Any change to an alias mapping SHALL be treated as refresh‑sensitive; at minimum it SHALL be recorded/emitted as `RSCRTriggerKindId.TokenizationOrNameChange` (and, if the mapped trigger kinds change, the corresponding canonical kinds apply as well). |
| **CC‑GCORE‑DEF‑1**  | A conforming `G.Core` SHALL maintain a Default Ownership Index for Part‑G defaults, ensuring each `DefaultId.*` has exactly one owner (a CC item or a policy id). All other patterns SHALL cite the owner and SHALL NOT state competing defaults. Any owner change MUST be recorded as `RSCRTriggerKindId.DefaultOwnerChange`. |

### G.Core:8 - Common anti-patterns and how to avoid them

* **Anti-pattern:** Restating CN‑Spec/CG‑Spec rules inside a `G.x` “for convenience”.  
  **Avoid:** cite A.19 / G.0; route via `CC‑GCORE‑CN‑CG‑1`.

* **Anti-pattern:** Adding a fourth guard status (“unknown”, “maybe”, “probe-only”) as a separate decision value.  
  **Avoid:** keep guard domain tri‑state; express “probe-only” as policy/branching and record via pins/audit.

* **Anti-pattern:** Treating mandatory invariants as “defaults” to centralize them.  
  **Avoid:** keep invariants as invariants (CC‑GCORE‑* routed to canonical owners); restrict the Default Ownership Index to true defaults (constants or conditional default-rules).

* **Anti-pattern:** Turning partial orders into scalar ranks silently.  
