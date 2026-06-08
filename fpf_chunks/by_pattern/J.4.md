---
chunk_kind: "parent"
pattern_id: "J.4"
pattern_title: "First Practical Entry Pattern-Comparison Index"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/J.4.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "J.4 — First Practical Entry Pattern-Comparison Index"
line_start: 82860
line_end: 83054
dependencies:
keywords:
---

## J.4 - First Practical Entry Pattern-Comparison Index

> **Type:** Index (J)
> **Status:** Stable
> **Normativity:** Informative navigation rule; it does not create a required sequence or replace the governing pattern body.

**At a glance.** Use `J.4` when a practitioner brings a working project into `FPF` and needs the first plausible pattern family. `J.4` starts from project problems and stabilizing results: problem shaping, responsibility alignment, choice, evidence, quality, architecture, publication, temporal and causal use, and only then wording repair when wording blocks the work. It is a compact first-entry aid, not a shadow ToC and not a mini version of the patterns it names.

**Use this when.** Use this pattern when the project-side question is real but the first `FPF` pattern is unclear, or when two or three candidate `FPF` patterns need to be distinguished before the substantive claim is handled.

**First output.** One named governing pattern to apply to the project-side problem, claim, relation, boundary, or publication-use question; or a decision that no `J.4` row is needed because the governing pattern is already recoverable.

**Primary EntityOfConcern.** One compact `FirstEntryPatternComparisonRow`: a working problem or first-entry cue, one first governing pattern reference or small candidate pattern set, and one short distinction that prevents the common wrong first choice.

**Working action path.** State the working problem and the stabilizing result being sought, inspect the nearest row, apply the named governing pattern to the substantive claim, and stop using `J.4` when the governing pattern is recoverable. Use the wording-repair row only when the wording itself hides the FPF kind named by value, relation, source-use disposition, or admissible next move. If the row needs more depth than one scan can hold, use the named pattern body or `I.2`.

**Not this pattern when.** Not this pattern when the governing pattern is already known, when the user needs the pattern body itself, or when the question is evidence, assurance, gate, decision, work, release, project certification, pattern quality, or `DRR` adequacy as a substantive claim. Those claims are governed by their own patterns.

**What this buys.** `J.4` reduces first-entry search cost for working projects without moving authority out of the named pattern. It helps choose where to begin; it does not govern the claim.

### J.4:0 - Compact Front-Door Rows

Rows are retained only when they are likely first practical entries, common wrong first guesses, or retrieval-facing cues that materially change the first pattern choice. A pattern does not need a `J.4` row merely because it exists.

The compact table has two reader families. Project and practitioner rows are the primary family: they help a user apply `FPF` to a working project, project-side claim, relation, boundary, comparison, architecture, publication, or improvement question. `FPF`-artifact rows are a small secondary family: they help a user apply `FPF` to an `FPF` artifact such as a pattern or `DRR`. Do not use an `FPF`-artifact row as project-side evidence, assurance, gate, decision, work, release, or certification.

#### Project or Practitioner First Entries

| Working problem or first-entry cue | Apply first | If the question is actually... |
|---|---|---|
| "We have a messy situation, concern, complaint, or opportunity, and do not yet know what problem-side material is accepted before work starts." | `C.22.2` | Use `E.18.1` only after accepted problem-side material needs first-principles-to-work carry-through. Use `A.15`, `A.15.2`, or `A.15.3` when the issue is responsibility, method, plan, or performed work rather than problem-side material. |
| "A serious cue or emerging idea is too important to ignore but too early to publish as a settled claim, requirement, or work record." | `C.2.2a` | Use `C.2.P` when the cue's wording must be restored before stronger use, and use the endpoint pattern only when the cue has matured into that endpoint's governed claim. |
| "A first-principles distinction should change what work, method, or modeling move is tried next." | `E.18.1` | Use `C.29` when the live move is mathematical-lens use, `A.6.0` when a `U.Signature(profile=FormalSubstrate)` declaration must be written, and `A.6.1` when mechanism realization or import is being claimed. |
| "Responsibilities, roles, methods, plans, performed work, and source use are being mixed in the project conversation." | `A.15` | Use `A.1.1` for bounded responsibility context, `A.15.2` or `A.15.3` for plan and work separation, `A.15.4` for work-relevant source use, and `B.5.1` when the alignment frame itself is being made. |
| "We need to compare alternatives, keep a shortlist honest, decide locally, or publish a selected set without hiding the comparison logic." | `A.19` and `C.19` | Use `C.11` for a local choice, `C.18` for portfolio or archive context, and `G.5` when a selector or set-return claim is being made. |
| "The first deliverable is a reusable search, generator, SoTA harvest, novelty-diversity archive, or exploration portfolio rather than one recommendation." | `G.0` | Use `G.1`, `G.2`, and `G.5` for generator and set-return claims; use `C.18` and `C.19` when the archive or selected-set publication is central; use `A.19` when the characteristic space already governs comparison. |
| "We need to say what better means before evaluating, comparing, or improving an object." | `A.19.ECS` | Use `C.16` for measurement construction, `C.25` for an existing Q-Bundle, `E.22` when a suitable evaluation exists but the evaluation question needs framing, and `E.23` when repeated improvement is needed. |
| "Evidence, test gaps, assurance, gate validity, or decision permission must be made explicit before commitment." | `A.10` and `B.3` | Use `A.20` for internal constraint validity, `A.21` for gate decisions, `C.11` for local choice, and `A.15` when the claim being made is performed work or planned work. |
| "We need to describe or change the architecture of some holon, selected structure, or architecture-relevant characteristic." | `C.30` | Use `A.22` or `C.30.ASV` for selected-structure and structural-view questions, `C.30.AD` when the object under repair is an architecture description, and `C.30.STRAT`, `C.30.LCA`, or `C.30.ILC` when stratification, control, or interlevel residuals are live. |
| "Function, module, interface, port, platform, reusable structure, or scale preference is central to the project move." | `A.6.F` and `A.6.M` | Use `C.31` for modularity or reusable-structure characteristics, `C.31.RSA` for reusable-structure accounting, `C.31.ASAP` for scale-amenability preference, and `C.30.TGA-FLOW-REL` when a TGA flow relation changes an architecture claim. |
| "Different audiences need aligned descriptions, explanations, screens, summaries, or renderings without changing the underlying EntityOfConcern." | `E.17` | Use `E.17.0` for description discipline, `E.17.AUD` for same-publication-unit use, `E.17.EFP` for explanation-facing rendering, `E.17.ID.CR` for bounded comparative interpretation, and `A.6.3.*` for same-EntityOfConcern episteme morphisms. |
| "Timing, freshness, delay, cadence, throughput, rate, recovery, effort, or resistance changes what can be claimed or done." | `C.27` | Use `C.16` for characteristic or measurement admission, and the work, comparison, quality, mechanism, evidence, or decision pattern when the temporal cue only modifies that claim. |
| "A correlation, explanation, scenario, model output, or comparison is being used as if it justified intervention, responsibility, or counterfactual choice." | `C.28` | Use `A.10` for evidence-path use, `B.3` for assurance, `C.16` for measurement, `C.27` for temporal adequacy, and `A.15` for performed work when those claims are live. |
| "Agreement, API, boundary, protocol, compliance, SLA, acceptance, or permission wording mixes rules, gates, duties, evidence, quality, or action." | `A.6` | Use `A.6.B` for boundary claims, `A.6.C` for claim routing, `A.10` for evidence, `B.3` for assurance, `A.20` for internal constraint validity, `A.21` for gate decisions, and `A.15` for work. |
| "Vocabulary is breaking down: a word or phrase hides the FPF kind, relation, source-use disposition, value meaning, or admissible move." | `E.10` and `E.10.ARCH` | Use the repair pattern after the kind is recovered: `F.19` for phrase apparatus, `F.18` for naming, `A.19.SPR` for state-family wording, `C.16.P` or `C.16.Q` for characteristic, scale, or quality wording, `E.10.D2` for EntityOfConcern, description, or specification-use wording, `A.6.P`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `A.6.F`, `A.6.M`, or another governing pattern. |

#### FPF-Artifact Author First Entries

| Working problem or first-entry cue | Apply first | If the question is actually... |
|---|---|---|
| "We need to evaluate or improve an FPF artifact without reducing quality to one score." | `E.22` | Use `E.21` for one pattern version, `E.9.DA` for one `DRR`, `E.2.DA` for FPF-level quality, and `E.23` when repeated improvement is being made. Use `A.19.ECS` first only when the needed evaluation characteristic space does not yet exist or is inadequate. |
| "We need to publish an accepted evaluation CharacteristicSpace as an FPF pattern." | `E.8.ECSPF` | Use `A.19.ECS` while constructing or repairing the evaluation characteristic space itself. Use `E.21`, `E.9.DA`, or `E.2.DA` when applying an existing evaluation to a pattern, `DRR`, or FPF-level object. |

### J.4:0.1 - First-Use Slice

A platform team asks, "Should we buy, fine-tune, or build an agent stack for our product?" The first `J.4` move is not to repair words. First ask what the working problem is. If the team still has only a vague situation, start with `C.22.2`. If responsibility, method, plan, and performed work are mixed, start with `A.15`. If the live work is comparing buy, fine-tune, build, and hybrid alternatives, start with `A.19`, `C.19`, `C.11`, or `G.5` depending on whether the comparison frame, selected set, local choice, or selector claim is live. If nobody can say what "better" means, start with `A.19.ECS` or `C.16`. If evidence and tests block commitment, use `A.10` or `B.3`. If several audiences need aligned outputs from the same underlying reasoning, use `E.17`. Use `E.10` only where a wording choice hides the kind or relation needed for one of those project moves.

`J.4` has done its job once the first governing pattern is recoverable. The working project then continues in that pattern, not in `J.4`.

### J.4:1 - Row Discipline

FirstEntryPatternComparisonRow := <workingProblemOrCue, firstGoverningPatternRefOrSmallSet, disambiguatingDistinction>.

A `FirstEntryPatternComparisonRow` is a `Part J` navigation-index row over published `FPF` patterns. It is not a `semanticArea`, not an `ontologicalNeighborhood`, not a `pattern nest`, not a table-of-content proximity relation, and not a structure of `FPF` itself.

A row is informative projection only. It remains valid only while the referenced pattern ids exist and the working problem or cue still changes first pattern choice. Lower, split, or remove a row when it duplicates the named pattern's recognition text, cannot stay compact, names stale ids, or no longer prevents a common wrong first choice.

Project-side rows start from the user's working problem or desired stabilizing result. Lexical cues may appear as search handles, but they must not become the table's organizing principle unless the live problem is wording-use repair. When a cue carries FPF-governed use, `E.10`, `E.10.ARCH`, and the named governing pattern recover the kind named by value, relation, source-use disposition, source-currentness claim, or value meaning.

FPF-artifact rows are secondary. They help FPF stewards evaluate, improve, or publish `FPF` artifacts; they do not define the main public reason a project comes to `FPF`.

### J.4:2 - Conformance Checklist

| ID | Check |
|---|---|
| CC-J4-1 | A row is informative first-entry projection only and does not create a required sequence, governing claim, or replacement for the named pattern body. |
| CC-J4-2 | A project-side row starts from one working problem or desired stabilizing result before lexical cues, pattern ids, or internal corpus topology. |
| CC-J4-3 | `Apply first` stays small enough for first use, and `If actually` names only the distinction needed to prevent the common wrong first choice. |
| CC-J4-4 | Lexical cues stay retrieval cues; kind named by value and relation recovery belongs to `E.10`, `E.10.ARCH`, and the named governing pattern. |
| CC-J4-5 | A row is lowered, split, or removed when it no longer changes first-pattern choice, duplicates a pattern's own recognition text, cannot stay compact, or names stale pattern ids. |
| CC-J4-6 | FPF-artifact rows remain visibly secondary to project and practitioner entry rows and cannot be used as project-side evidence, assurance, gate, decision, work, release, or certification. |

### J.4:3 - SoTA and Practice Alignment

| Practice source family | Local invariant | Shortcut rejected |
|---|---|---|
| Problem-first onboarding and practitioner front-door practice | Rows begin from recognizable working situations and stabilizing results. | Presenting the entry index as a catalog of wording repairs or internal pattern topology. |
| Information-foraging and information-scent practice | Rows keep high-recall cues, but the cue points to a working problem and first admissible pattern. | Choosing by table order, pattern id, or familiar name when the working problem requires a different governing pattern. |
| Faceted navigation and controlled-vocabulary practice | The row separates working problem or cue, first application, and near-miss distinction. | One synonym list that hides kind recovery. |
| Decision-aid triage practice | A row is useful only if it changes the first practical choice. | Keeping rows merely because a pattern exists. |
| Search and retrieval practice for technical corpora | Lexical cues help retrieval but do not become FPF kinds. | Treating a search phrase as canonical ontology. |

### J.4:4 - Relations and Refresh

`J.4` depends on the published pattern corpus, pattern ids, and the recognition text of the patterns it names. It coordinates with `Preface` for coarse orientation, `I.2` for expanded entry-disambiguation cases, `E.10` for wording-use recovery, `E.21` for pattern-quality evaluation, `E.23` for repeated improvement, and the named governing pattern for every substantive claim.

Refresh a row when a named pattern is renamed, split, merged, removed, or given a materially different recognition boundary; when a new pattern changes first-entry choice; when a lexical cue becomes misleading; when project front-door use reveals a missing problem family; or when the row grows too large to scan. Move depth to `I.2` when it no longer works as compact first-entry projection.

### J.4:End

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
