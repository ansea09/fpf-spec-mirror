---
chunk_kind: "parent"
pattern_id: "J.4"
pattern_title: "First Practical Entry Neighborhood Index"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/J.4.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "J.4 — First Practical Entry Neighborhood Index"
line_start: 82038
line_end: 82241
dependencies:
keywords:
---

## J.4 - First Practical Entry Neighborhood Index

> **Type:** Index (J)
> **Status:** Stable
> **Normativity:** Informative navigation rule; it does not create a required sequence or replace the governing pattern body.

**At a glance.** Use `J.4` when a practitioner has a live entry question and needs the first plausible FPF patterns to inspect without turning the index into a universal lookup table or required sequence.

**Use this when.** Use this pattern when several nearby first entries are plausible, the wrong first stop is common, or a lexical cue is likely to hide a more exact governing pattern.

**First output.** One selected entry row, or a decision that no `J.4` row is needed because the governing pattern is already obvious.

**Primary EntityOfConcern.** One informative `EntryNeighborhoodRow` or the table of such rows: entry neighborhood, honest entry question, first patterns to inspect, nearby reclassifications, admissible entry stop, non-entry condition, and lexical-query help.

**Working action path.** Name the live entry question, inspect the closest row, test the non-entry condition, open the named governing pattern rather than staying in `J.4`, and lower or ignore the row when the exact governing pattern is already recoverable.

**Not this pattern when.** Not this pattern when the user already has the exact governing pattern, needs the governing pattern body itself, needs a required ordered sequence, or needs pattern-quality, DRR-adequacy, evidence, assurance, gate, decision, work, or project certification.

**What this buys.** `J.4` reduces first-entry search cost while preserving pattern authority: it points, stops, and reclassifies; it does not govern the substantive claim.

This index is informative navigation only.
It helps one practitioner compare plausible first pattern entries under one live
entry question. It is not one universal lookup table, not one required sequence, not one
learning syllabus, and not one pattern-local recognition role. It is one
compact comparison of nearby starting points.
Plain use: choose by what you are really trying to decide, not by document
order. A row names first patterns to inspect, plausible wrong first stops, and
where entry can stop without pretending there is a required ordered sequence.

Plain column key: entry neighborhood = nearby starting-point cluster; first
honest entry question = what you are really trying to decide or stabilize; first patterns
to inspect = patterns to inspect first; admissible entry stop = enough to proceed
without pretending there is a required ordered sequence.

This table helps recover the governing pattern or verify the preceding guidance. It does not replace the pattern's Solution and does not create a required sequence.

| Entry neighborhood | First honest entry question or case signal | First patterns to inspect | Nearby reclassification cues | First admissible entry stop | Non-entry condition and search cues |
| --- | --- | --- | --- | --- | --- |
| Project alignment | "We keep mixing responsibilities, method, plan, and performed work." | `A.1.1`; `A.15`; `A.15.2`; `A.15.3`; `B.5.1` | `F.11` for unstable method/work vocabulary; `F.9` for bridge discipline | alignment pattern opened, or one shared work/term form stable enough to proceed | not comparison, boundary-claim placement, SoTA scaffold, or generator scaffold; cues: responsibility, plan, actual work |
| Principles-to-work carry-through | "Accepted problem-side output plus principle, result, source, interface, or integration cue needs the next P2W relation." | `E.18.1`; `C.22.2`; `A.6.0`; `A.6.1`; `A.15`; `A.15.4` | `C.29` for mathematical-lens use; `A.15.1`/`A.15.2`/`A.15.3` for performed or planned work; `E.18` for graph relation | carry-through record names next kind, relation, record, application, or stop condition | not when no accepted problem-side output exists or one exact pattern already governs the claim; cues: P2W, first principles to work, result carry-through, interface split |
| Partly-said cue and language-state discovery | "Something important is present but too early for a settled claim, requirement, or work record." | `C.2.LS`; `A.16`; `A.16.1`; `A.16.2`; `B.4.1`; `B.5.2.0` | endpoint claim/action/quality patterns only after the cue matures | cue preserved, language-state cue typed, or entry plurality opened | not when the claim is already stable enough for L/A/D/E claim decomposition; cues: vague cue, not yet a claim |
| Wording-use precision restoration | "The wording hides the head kind, relation, source-use role, state-family value, architecture/structure use, characteristic, quality sense, function sense, or governing pattern." | `E.10`; `E.10.ARCH`; exact realization pattern when known | `C.2.P`, `A.6.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, `A.19.SPR`, `A.6.F`, or `F.18` by recovered kind | false positive, local repair, direct exact pattern, or restoration note names remaining move | not a toll booth when exact pattern is already recoverable; cues: source says, readiness claim, function of, layer/level/tier/stack/block/gate |
| Ontology-first plain technical rewriting | "The sentence has an FPF object, but phrase apparatus hides object, claim, relation, or action." | `F.19`; `E.8`; `E.21` when quality evaluation is live | `E.10`, `E.10.ARCH`, `F.18`, or exact pattern after apparatus is removed | phrase apparatus removed/moved, remaining content repaired, or blocker names hidden kind | not one overloaded word/head alone; cues: official-sounding sentence, mostly negative paragraph, reference boilerplate before action |
| Boundary unpacking and claim decomposition | "Agreement, API, protocol, SLA, acceptance, or compliance wording mixes law, gate, duty, evidence, quality, or action." | `A.6`; `A.6.B`; `A.6.C` | `A.6.RSIG`, `A.6.P`, `C.16.Q`, or `A.6.A` when first-contact, relation, quality, or action wording is live | boundary claim pattern opened or L/A/D/E atomic claim set ready | not partly-said cue or already decomposed claim set; cues: API, promise, commitment, duty, evidence, gate |
| Architecture, diagram, module, and model distinction | "Architecture, module diagram, ports, functional architecture, graph, control description, modularity, scale-preference, or source-label wording hides the EntityOfConcern." | `C.30.P`; `C.30.STRAT`; `C.30`; `A.6.M`; `C.31` family | `C.30.ASV`, `C.30.TGA-FLOW-REL`, `E.18`, `C.30.LCA`, `A.6.F`, `C.30.ILC`, `C.16.P`, `C.29`, or `C.2.P` by recovered relation | architecture, structure, module, modularity, reusable-structure, or scale-claim triage is selected | not universal layer/stack ontology or scale-proof shortcut; cues: architecture, ports, three layers, modularity score, LCA proves safety |
| Comparison, pool policy, selection, and selected-set publication | "We need comparison, shortlist, pool policy, call-planning distinction, or selected set without forcing one winner." | `A.19:0`; `A.17-A.19`; `A.19.CN`; `C.18`; `C.19`; `G.0`; `G.5` | `C.11` for local choice; `C.24` for `CallPlan`/`CheckpointReturn`; `A.19.CPM` or `A.19.SelectorMechanism` when structure is live | comparison relation, pool policy, local choice, call plan, or selected-set publication pattern identified | not when selector mechanism or selected-set publication is already settled; cues: shortlist, acceptable option set |
| Generator, SoTA, or portfolio scaffold | "The work is a reusable search, harvest, generator, selector, or portfolio scaffold, not one recommendation." | `A.0`; `G.0`; `G.1`; `G.2`; `G.5` | `B.5.2.1`, `C.17-C.19`, `G.10`, or `G.11` when creative search, policy, shipping, or refresh is live | generator/scaffold entry opened or portfolio/set publication pattern identified | not one local comparison or one-off recommendation; cues: scaffold, reusable search, generator |
| Same-entity rewrite, explanation, and comparative interpretation | "Restate, explain, render, repair, or compare the same claim-bearing `PublicationUnit` without changing what it is about." | `A.6.3.CR`; `A.6.3.RT`; `E.17.EFP`; `E.17.ID.CR` | `E.17.AUD.LHR` or `E.17.AUD.OOTD` when pressured-head or `PublicationUnit` stability is live | rewrite, transition, explanation-facing rendering, or bounded comparative interpretation opened | not a new episteme, new rule track, or independent `PublicationUnit`; cues: same unit, different audience |
| Temporal claim adequacy | "Speed, cadence, throughput, recovery, stabilization, rollout, or learning rate changes the next move." | `C.27`; `C.16`; `A.3.3` | `B.1.4`, `B.1.6`, `C.18.1`, `C.19`, `C.22.1`, `C.24`, `C.25`, `C.26`, `C.26.3`, or `G.9` by other live question | ordinary prose, Dyn0/Dyn1, `Dyn2TemporalClaimAdequacyCard`, profile, or exact relation | not speed metaphor, snapshot, benchmark, or QL residue alone; cues: velocity, rhythm, cadence, throughput, recovery |
| Causal-use and counterfactual claim repair | "This caused that, an intervention would work, a policy would have prevented harm, or a benchmark is counterfactual." | `C.28`; `A.10`; `B.3`; `D.5`; `G.5`; `G.9` | `C.16`, `C.27`, `C.26`, `A.15`, `A.3.2`, or `A.6` when the live claim is measurement, temporal, QL, work, or boundary split | causal-use triage card, or downgrade to association, measurement, temporal, simulation, method, work, or boundary interpretation | not observed association, work occurrence, schedule, duty, or simulation trace alone; cues: caused, effect, intervention, counterfactual |
| Quality-evaluation question framing | "Are we asking for floor blockers, exceptional improvements, trade-off check, open questions, or absorption impact?" | `E.22`; `E.21`; `E.9.DA`; `E.19` | `C.16`/`A.17-A.19` for characteristic legality; `E.10`, `A.6.P`, `C.2.P`, `F.18` for wording/names; project-side patterns for overread | `QualityEvaluationQuestionFrame` names object version, use, purpose, floor/aim, evidence basis, result form, and non-use boundary | not already-framed evaluation awaiting execution; cues: review this, raise to 5, absorption impact, Pareto trade-off |
| EntityOfConcern-under-improvement evaluation setup | "We want to improve something but cannot yet say better for whom, by which values, against which cases, or when to stop." | `A.19.ECS`; `A.19`; `E.22`; `E.23` | exact evaluations such as `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, or `C.25`; `A.17`, `A.18`, `C.16`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` when live | evaluated object kind, use, contrast cases, coordinates, value meanings, missingness, protected trade-offs, state-family value, and stop/reopen declared | not one already-framed evaluation, local work task, or project certification; cues: what is better, arbitrary rubric, when stop improving |
| Repeated quality-improvement loop | "The object has an evaluation and candidate repairs; now we need evaluate-change-reevaluate-stop without treating activity as improvement." | `E.23`; `E.22`; exact object-under-improvement evaluation | `A.19.ECS` when evaluation is inadequate; `C.19`/`G.5` for proposal selection; project-side patterns for evidence/assurance/decision/gate/work overread | loop opens with object version, evaluation, expected value movement, protected trade-offs, cost boundary, re-evaluation result form, and stop/reopen | not single evaluation, generator design, selected-set publication, project approval, or external certification; cues: another pass, closed checklist, all fives |
| Evaluation CharacteristicSpace FPF pattern publication form | "A reusable evaluation characteristic space exists or is being built, and the question is how to publish it as an FPF pattern." | `E.8.ECSPF`; `A.19.ECS`; `E.8`; `E.21` | `E.22`, `E.23`, `F.18`, `E.9.DA`, `E.2.DA`, `C.25`, or exact neighbors by live claim | publication form states evaluated kind, use, first evaluation, coordinates, result form, evidence basis, cases, non-use, reopen | not local, temporary, or one-project-only evaluation; cues: make this rubric a pattern, table right but hard to use |
| FPF-level Pillar adequacy and whole-FPF improvement | "We are improving FPF as corpus, release candidate, cluster, or language ecology." | `E.2.DA`; `E.2`; `E.23`; `E.22` | `E.21` for one pattern; `E.9.DA` for one DRR; `F.18` for lexical quality; `J.4` for discoverability | FPF object under improvement, use scope, Pillar coordinates, evidence loci, rationales, trade-offs, stop, and reopen declared | not local pattern quality, one DRR, one term, or project-side certification; cues: improve FPF, Pillars, corpus discoverability |
| Pattern-quality stop, repair, and non-scalar improvement | "A pattern draft/update may be good enough, blocked, or improvable without reducing quality to one score." | `E.21`; `E.19`; `E.8`; `C.25`; `C.16.Q` | `C.16`/`A.17-A.19`, `F.18`, `C.2.P`, `E.17.AUD`, or project-side patterns when those claims are live | `PatternQualityEvaluation` names pattern version, reader, use, window, evidence basis, coordinate rationales, status, stop, or first repair | not only E.8 body shaping, E.19 frame execution, generic measurement, or project certification; cues: quality score, Goodhart, first move missing |
| DRR decision adequacy before pattern drafting | "Can I draft from this DRR without inventing missing decisions, selected loci, source-use payload, or accepted-decision carry-through?" | `E.9.DA`; `E.9`; `E.10` when wording repair is live | `E.21` for pattern quality; `E.19` for admission/refresh review; project-side or measurement patterns when those claims are live | `DRRDecisionAdequacyEvaluation` names DRR version, use, evidence loci, coordinate rationales, selected-locus disposition, carry-through, status, and first drafting move/repair | not ordinary pattern-quality evaluation, local wording repair, or project-world certification; cues: vague DRR, selected patterns, source-use carry-through |
Rows are for likely first practical entries, common wrong first guesses, or
public-facing or retrieval-facing entry points. A pattern does not need a `J.4` row merely
because it exists. A row belongs here only when the pattern is a practical entry
point or when its first-pattern choice commonly changes. The pattern text itself
still needs a pattern-local `Problem frame` and any live wrong-pattern boundary to be clear.
A `J.4` row usually stays bounded: `3-6` first patterns to inspect, `1-3` nearby or
reclassification cues, one short not-this-entry sentence, and one short admissible
entry-stop phrase. The row remains compact enough to scan in one pass and
specific enough not to smuggle a required ordered sequence.

### J.4:1 - Row Discipline

`EntryNeighborhoodRow := <entryNeighborhood, honestEntryQuestion, firstPatternsToInspect, nearbyReclassifications, admissibleEntryStop, nonEntryCondition, lexicalQueryHelp>`.

This is an informative projection row only. The phrases in `Worked walk-through and lexical-query help` are retrieval cues, not canonical recovered kinds. When a lexical cue has FPF-governed use in FPF-governed wording, `E.10` and the referenced governing pattern decide the exact kind, relation, source-use disposition, source-currentness claim, or value meaning.

A row is current only while the referenced pattern ids exist and the row's first-entry question remains true. Lower, narrow, or remove a row when it no longer changes first-pattern choice, duplicates the referenced pattern's recognition text, cannot stay compact, or its first-entry claim is no longer true for current pattern ids. Update `J.4` when a new or changed pattern materially changes the honest first-entry choice; do not add historical status notes.

`J.4` remains the compact projection role for these rows. It does not become the applicable governing pattern body for the entry questions or relations it points to. `SoTA`-related cues only help select the first governing pattern; source currentness and `SoTA` adoption are evaluated in that governing pattern, not in `J.4`. If a referenced pattern's `Problem frame` does not expose its use situation, the pattern itself remains under-specified. If a row cannot stay compact, the depth belongs in `I.2`.

When `J.4` itself is under improvement, use `E.21` for the pattern-quality evaluation and `E.23` for repeated improvement. `J.4` only answers whether a row is a useful first-practical entry projection.

### J.4:2 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-J4-1 | A row is informative navigation only and does not create a required sequence, governing claim, or replacement for the named pattern body. |
| CC-J4-2 | A row starts from one honest entry question or case signal, not from alphabetical order, table position, campaign history, or pattern-id proximity. |
| CC-J4-3 | First patterns to inspect stay bounded enough for first use; nearby reclassifications are explicit and do not become a hidden required action chain. |
| CC-J4-4 | Lexical-query help stays a retrieval cue. If the cue carries FPF-governed use, the named governing pattern and `E.10` recover the exact kind or relation. |
| CC-J4-5 | A row is lowered, narrowed, or removed when it no longer changes first-pattern choice, duplicates a pattern's own recognition text, cannot stay compact, or points to stale pattern ids. |
| CC-J4-6 | `J.4` points to pattern-quality, DRR-adequacy, evidence, assurance, gate, decision, work, release, or project-certification patterns only as first entries; those patterns govern their own claims. |

### J.4:3 - SoTA and Practice Alignment

| Practice source family | Local invariant | Shortcut rejected |
| --- | --- | --- |
| Information-foraging and information-scent practice | Entry rows use the practitioner's live question and recognizable cues before taxonomy. | Choosing by table order, pattern id, or familiar name when the live question points elsewhere. |
| Faceted navigation and controlled-vocabulary practice | Rows combine entry neighborhood, first question, nearby reclassification, stop condition, and lexical-query help as separate facets. | One universal lookup column or one synonym list that hides kind recovery. |
| Decision-aid triage practice | `Not this entry when` and admissible entry stop are as important as first patterns to inspect. | Turning an index into a required action chain or exhaustive taxonomy. |
| Search and retrieval practice for technical corpora | Lexical cues are allowed as search handles, but recovered FPF kinds come from the governing pattern. | Treating a search phrase as the canonical kind, relation, or evidence source. |

### J.4:4 - Relations and Refresh

`J.4` depends on the current pattern corpus, current pattern ids, and the recognition text of the patterns it points to. It coordinates with `I.2` for deeper walk-throughs, `E.10` for wording-use recovery, `E.21` for pattern-quality evaluation, `E.23` for repeated improvement, and the named governing pattern for every substantive claim.

Refresh a row when a named pattern is renamed, split, merged, removed, or given a materially different recognition boundary; when a new pattern changes first-entry choice; when a lexical cue becomes misleading; or when the row grows too large to scan. Lower the row to ordinary prose or move depth to `I.2` when it no longer works as compact first-entry navigation.

### J.4:End

# **Part K - Lexical Debt**

## Mandatory replacement map for measurement terms


> **Rule:** In all **normative** content (specifications, data schemas, etc.), the deprecated terms **“axis”** and **“dimension”** (and their plural or compound forms) **MUST NOT** be used to denote a measurable aspect. Use **Characteristic** in the Tech register instead. Other colloquial terms should be mapped to canonical terms as listed below. In **Plain** narrative, deprecated aliases may appear _only on first use_ and only if paired with their canonical equivalent for clarity.

| Deprecated term (context) | **Replace with** (Tech register) | Plain register allowance | Canonical Reference |
| --- | --- | --- | --- |
| axis (of measurement); dimension (of a system or quality) | **(disallowed in Core prose)** → use **Characteristic** | No parenthetical allowance in Core; use **Characteristic**, **Measure**, or **Coordinate** only | A.17 (CHR-NORM) |
| point (on an axis); data point | **Coordinate** (on a Scale) | “point” _(in explanations only, e.g. “a point on the scale”)_ | A.18 (CSLC-KERNEL) |
| metric value; raw score | **Coordinate** (or **Value**) | “value” _(acceptable in plain usage when context is clear, but formally it’s a Coordinate tied to a Characteristic)_ | A.18, C.16 |
| score (composite or normalized) | **Score** (produced via a **ScoringMethod**) | “score” _(if needed in narrative, ensure it’s explained as a result of a defined ScoringMethod)_ | A.17/A.18 (ScoringMethod/Score) |
| unit dimension; unit axis | **Unit** (of a Scale) | “unit” _(plain usage okay)_ | A.18 (Scale/Unit) |
| metric (as a noun) | **Avoid in Tech and as primitive** → use **`U.DHCMethodRef` / `U.Measure` / Score** | “metric” _(Plain only on first use, with pointer to canonical terms)_ | C.16 § 5.1 (L5), A.18 |

## Temporal claim lexical debt from C.27

Retire untyped velocity, acceleration, cadence, agility, rhythm, inertia, and dynamics language when it is used outside a named C.27, C.16, or A.3.3 reading. Repair each occurrence to one of: ordinary prose, Dyn0 state reading or snapshot, Dyn1 measured rate or trend, Dyn2 intervention-sensitive temporal claim, C.16 measurement construction, or A.3.3 reusable transition law or model.

Russian/English Plain-Tech twins for authoring:

| Russian Plain | Safe Tech reading |
| --- | --- |
| скорость | rate, throughput, or tempo reading |
| ускорение | rate-change or intervention-sensitive temporal claim |
| усилие | planned effort, work, resource, or input basis, or intervention basis |
| инерция | resistance/inertia proxy, not a physical mass analogue by default |
| ритм | bearer/anchor/window/proxy relation |
| динамика второй производной | Dyn2 claim reading, not second-derivative ontology |

## Migration debt from A.2.6 (Scope, ClaimScope, WorkScope)

### Deprecations (normative)

The following terms **MUST NOT** name scope objects in normative text, guards, or conformance blocks:

* *applicability*, *envelope*, *generality*, *capability envelope*, *validity* (as a characteristic name).

Use instead:

* **`U.ClaimScope`** (*Claim scope*, nick **G**) for epistemes;
* **`U.WorkScope`** (*Work scope*) for capabilities;
* **`U.Scope`** only when explaining the abstract mechanism (not in guards).

### Affected locations and required edits (normative)

Editors SHALL apply the following replacements:

1. **Part C.2.2 (F–G–R).**

   * Replace any internal definition of “Generality” with a normative reference to **A.2.6 §6.3** (*Claim scope (G)*).
   * Where “abstraction level” is mentioned as G, replace with “Claim scope (where the claim holds)”; keep **AT** (AbstractionTier) only as optional didactics (non‑G).
   * Ensure composition examples use **intersection/SpanUnion** for G, not ordinal “more/less general”.

2. **Part C.2.3 (Formality F).**

   * No change to F itself.
   * Any example that implies “raising F widens G” MUST be rephrased: F changes expression form; G changes only via **ΔG**.

3. **Part A.2.2 (Capabilities).**

   * Replace “capability envelope/applicability” with **`U.WorkScope`**.
   * Method–Work gates MUST test **Work scope covers JobSlice**, with **measures** and **qualification windows** bound.

4. **Part B (Bridges & CL).**

   * Add a note: **CL penalties apply to R**, not to **F/G**; mapping MAY recommend **narrowing** the mapped scope (best practice).

5. **Part E (Lexicon).**

   * Add entries for **Claim scope (G)**, **Work scope**, **Scope** (mechanism).
   * Mark listed deprecated terms as **deprecated aliases** allowed only in explanatory notes.

6. **ESG & Method–Work templates.**

   * Replace any “applicability”/“envelope” guard phrasing with **ScopeCoverage** (see §10).
   * Require explicit **`Γ_time`** selectors in all scope‑sensitive guards.

### Migration playbook (informative)

1. **Inventory** scope‑like phrases across your Context (search: applicability, envelope, generality, capability envelope, valid\*).
2. **Classify** each occurrence as **Claim scope** (episteme) or **Work scope** (capability); replace any “scope characteristic(s)” with “scope object”, “scope type”, or “USM scope object” depending on sentence grammar.
3. **Rewrite** guards to use `Scope covers TargetSlice` + explicit **`Γ_time`**; remove “latest”.
4. **Publish** any required **Bridges** with **CL** for Cross‑context usage.
5. **Document** ΔG changes separately from evidence freshness (R).

### Alias and body-prose continuity (informative)

Existing body prose may keep older phrasing only when it is explanatory and carries no current requirement. All **guards, conformance checklists, and state assertions** MUST be rewritten to the USM terms and semantics.

### Change Log (normative migration record)

* **A.2.6 introduced.** Defines `U.ContextSlice`, `U.Scope`, `U.ClaimScope (G)`, `U.WorkScope`; sets algebra and guard patterns.
* **Deprecated labels.** “applicability / envelope / generality / capability envelope / validity” as characteristic names.
* **Edits required.** C.2.2 (G = Claim scope), A.2.2 (Work scope for capabilities), Part B (CL→R note), Part E (Lexicon updates), ESG/Method–Work guard templates (ScopeCoverage + `Γ_time`).
* **No change.** C.2.3 (F) unchanged; its examples updated only for wording consistency.
