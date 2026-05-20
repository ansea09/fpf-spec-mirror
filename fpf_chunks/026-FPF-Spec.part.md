   Every Bridge names two SenseCells bound to declared Contexts and publishes kind, direction (if needed), `CL`, Loss Notes, and Bridge-supported use.
2. **CC-F.9-2 - Substitution discipline.**
   Any substitution or row support comes only from a Substitution Bridge on the same `senseFamily`; Role Assignment & Enactment-level substitution requires `CL >= 2`, and Type-structure substitution requires `CL = 3` plus matched invariants.
3. **CC-F.9-3 - Interpretation embargo.**
   Interpretation Bridges remain explanation-only and are not used to justify substitution or Concept-Set rows.
4. **CC-F.9-4 - CL honesty and loss visibility.**
   Bridges with `CL <= 2` publish a counter-example or explicit boundary case; Bridges with `CL = 3` publish the invariants that justify the higher-scope use; all Bridges publish Loss Notes.
5. **CC-F.9-5 - Weakest-link row discipline.**
   Cross-context rows never claim a broader scope or higher row-level `CL` than the participating Bridges support.
6. **CC-F.9-6 - Overlay non-collapse.**
   If a `F.9.1` Bridge Stance Overlay is used, it remains an annotation and does not replace bridge kind, direction, `CL`, or Loss Notes.
7. **CC-F.9-7 - Registry-reference discipline.**
   `BridgeId` and cited policy pins are treated as registry references, not as signature-exported semantic symbols.

8. **CC-F.9-8 - Coarsened cross-context note is not treated as a Bridge Card.**
   If bridge-bearing reuse begins from a lighter note, summary, or comparison aid, the source-bearing episteme or source publication needed for bridge support is reopened and a full Bridge Card is published before any equivalence, substitution, `Naming-only` row, interoperability, or other row support is claimed.

### F.9:21 - Consequences


**Benefits.**
F.9 lets FPF compare, translate, and partially reuse ideas across Contexts without collapsing them into one vocabulary. It gives downstream rows, claims, and assurance reasoning an explicit Bridge Card record instead of relying on prose intuition.

**Trade-offs / mitigations.**
The pattern adds explicit bridge declaration and may feel heavier than informal comparison. Mitigation: use Naming-only scope when explanation is enough, and reserve higher-scope uses for Bridges that carry the required `CL` and invariants.

### F.9:22 - Rationale

The core move of F.9 is simple: cross-context work is unavoidable, but silent sameness is unacceptable. A Bridge therefore does two jobs at once:

* it preserves practical reuse where bounded transport is genuinely available, and
* it keeps non-identity visible through direction, Loss Notes, `CL`, and weakest-link scope.

Without that discipline, every shared label becomes a hidden ontology merger. With it, cross-context comparison stays teachable, auditable, and compatible with the rest of FPF.

### F.9:23 - SoTA-Echoing

**SoTA note.** This section does not mint an independent second bridge rule track. It stays truthful only when Bridge kinds, `CL`, Loss Notes, weakest-link scope, the `A.6.3.CSC` neighbor boundary, and the review matrix below still tell the same story about admissible cross-context reading.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `F.9` | Adoption status |
| --- | --- | --- | --- | --- |
| Shared labels across contexts are not enough for supported cross-context reuse. | Terminology and ontology practice distinguishes objects, concepts, definitions, designations, and typed relations instead of treating the same string as identity. | ISO 704:2022; ISO 1087:2019; ISO/IEC 21838-2:2021 (BFO). | `F.9` requires typed SenseCells, bridge kind, direction where needed, `CL`, and Loss Notes rather than string-equals identity. | **Adopt/Adapt.** Adopt explicit term/concept/relation discipline; adapt it into Bridge Cards; reject lexical sameness as reuse support. |
| Viewpoint and context boundaries must stay explicit when descriptions are reused. | Architecture-description practice distinguishes an entity of interest, architecture description, viewpoint, view, model kind, concern, and correspondence. | ISO/IEC/IEEE 42010:2022. | `F.9` binds every Bridge to declared Contexts and forces downstream rows to obey weakest-link scope instead of outrunning the supporting correspondences. | **Adopt.** Adopt boundary-explicit architecture-description discipline and apply it to FPF cross-context bridge cards. |
| Data/catalog/validation practice separates metadata, validation conditions, and exchange support from substitution authority. | Web-data and semantic-web standards make metadata, provenance, structural constraints, validation, and catalog federation explicit without turning metadata into the data itself. | W3C Data on the Web Best Practices (2017); W3C SHACL (2017); W3C DCAT v3 (2024). | `F.9` separates explanatory/interpretive bridges from substitution bridges and keeps bridge publication distinct from coarsened notes or catalog-style discovery aids. | **Adapt/Reject.** Adapt explicit metadata and validation practice; reject treating discovery, gloss, or validation support as substitution support. |
| Model-based engineering uses traceable model elements and formal semantics, but tool interoperability is not itself semantic identity. | Current MBSE practice improves precision, traceability, and interoperability through explicit model elements, libraries, APIs, and formal semantics. | OMG SysML v2.0 Language Specification (2025); OMG KerML v1.0 Specification (2025). | `F.9` uses Bridge Cards as human-readable, reviewable relations whose `CL` and loss fields remain narrower than and do not replace any hidden tool or model interchange claim. | **Adapt.** Adopt traceable relation discipline; reject tool or interchange success as proof of same meaning. |

**Worked-slice docking.** The nearest practical recovery anchors here are the micro-examples in `F.9:10`, the worked examples in `F.9:12`, the revision law in `F.9:14`, and the review matrix in `F.9:26`. If the SoTA claim cannot be recovered through those explicit bridge-card anchors, do not let the alignment rationale stand in for live bridge law.

**Local stance.** Best-known current practice supports a narrow rule: cross-context reuse is admissible only when correspondence is typed, directional where needed, explicit about loss, and narrower than silent lexical identity or convenience equivalence.

### F.9:24 - Bridge Card Publication Discipline

#### F.9:24.1 - Minimal bridge-card declaration
A usable Bridge Card should make visible:

- the two typed SenseCells,
- the bridge kind,
- direction where direction matters,
- declared `senseFamily`,
- `CL`,
- explicit Loss Notes,
- and the Bridge-supported use or row consequence.

If any of these fields is absent, later readers are forced back into inference by prose similarity, which is exactly what `F.9` is supposed to block.

#### F.9:24.2 - One-pair default rule
The default declaration discipline is one primary Bridge per cell pair per relevant `senseFamily`, with richer Loss Notes rather than many near-duplicate cards. Local exceptions are admissible only when the cards genuinely differ in bridge kind, direction, or admissible use.

#### F.9:24.3 - Revision over silent drift
If later evidence changes bridge `CL`, direction, or loss, the Bridge Card should be revised explicitly. It should not be left in place while surrounding prose quietly changes the practical scope.

### F.9:25 - Bundle and Endpoint Interaction Law

#### F.9:25.1 - Viewpoint and bundle interaction
Viewpoint bundles, quality bundles, and other endpoint bundles may cite Bridges, but they do not absorb bridge semantics. `F.9` remains the pattern for cross-context alignment, while the citing bundle keeps its own ontology.

#### F.9:25.2 - Quality-family interaction
When a quality family claim crosses contexts, bridge loss and `CL` affect what may be compared or reused, but they do not retype the quality family itself. Any resulting assurance penalty feeds `R` rather than changing the ontology of `F`, `G`, or the Q-Bundle head.

#### F.9:25.3 - Overlay interaction rule
A `F.9.1` stance overlay may help readers interpret a bridge, but the bridge card remains primary. If the overlay overstates the bridge kind, direction, `CL`, or Loss Notes, the card wins and the overlay should be narrowed or removed.

### F.9:26 - Review Matrix and Migration Tests

A reader can test bridge integrity with six questions:

1. **Are the two cells and contexts explicit?**
2. **Is the bridge kind the least-committing truthful kind rather than the friendliest one?**
3. **Does `CL` match the published counter-example or invariant evidence?**
4. **Are Loss Notes specific enough that the Bridge-supported use is really bounded?**
5. **If a row or bundle cites the bridge, does it stay within the Bridge-supported use?**
6. **If a stance overlay exists, does it stay within the bridge card's kind, direction, `CL`, and Loss Notes?**

Migration from legacy "same/equivalent/align/map" prose should therefore recover the Bridge Card first, then any row support, then any optional stance overlay. Doing it in the opposite order recreates silent equivalence under new vocabulary.
### F.9:14a - C.29 MLA relation

> When meaning, substitution, sense cells, direction, `CL`, or Bridge-supported use crosses context, write the `F.9` Bridge Card first. Add the applicable `C.29` output only for mathematical-lens adequacy: candidate mathematical object, lens-mapping posture, preserved and lost structure, exposed invariants or distinctions, support posture, use-rights, and stop condition. Do not duplicate Bridge semantics inside MLA. A Bridge may make a mathematical lens interpretable across contexts without making it substitution-safe.

### F.9:End
## F.9.1 - Bridge Stance Overlay

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Bridge-card stance overlay.
**One-line summary.** `BridgeStanceOverlay` governs one stance annotation over an existing `F.9` bridge card so authors can say how to read that bridge without changing its kind, direction, `CL`, or loss notes and without treating the overlay as bridge authority or as a cure for missing source-bearing return.
**Governed object in plain terms.** One overlay annotation attached to an existing `F.9` bridge card; not the bridge card itself, not a second bridge kind, and not the pattern that governs coarsened renderings.
**Use this when.** Use this overlay when an existing bridge card already exists and the real need is one compact stance label such as `localRename`, `operationalizes`, `partialAnalogy`, `projection`, or `nonEquivalent` that helps readers interpret that bridge without widening its substitution licence.
**Start here when.** Your first honest artefact is already an `F.9` bridge card, and the practical question is how to read that bridge rather than whether a bridge exists at all.
**What goes wrong if missed.** Authors fall back to vague phrases like "roughly analogous" or "just a rename", and readers either over-read the gloss as silent bridge authority or under-read it as disposable style.
**What this buys.** One compact interpretive gloss over an existing bridge card that stays reusable, keeps the bridge taxonomy stable, and still leaves source-bearing return and bridge publication duties where they belong.
**Not this pattern when.** Not this overlay when the case is the bridge card itself under `F.9`, or when a coarsened rendering still needs source-bearing return before any bridge-bearing use is admissible; use `A.6.3.CSC Controlled Semantic Coarsening` for that coarsened-rendering relation.


### F.9.1:1 - Problem frame
When positions or trajectories in language-state work are compared across schools or contexts, authors often need a disciplined interpretive gloss on top of a formal bridge card. The gloss must help reading without becoming a second bridge taxonomy.

### F.9.1:2 - Problem
Authors often express stance informally ("roughly analogous", "really a projection", "just a rename"), which makes bridge interpretation unstable. A full second taxonomy would be worse: it would compete with the core bridge kinds.

### F.9.1:3 - Forces
| Force | Tension |
|---|---|
| **Expressive stance vs bridge discipline** | Add interpretive clarity without introducing a rival bridge-kind system. |
| **Reuse vs inflation** | Make stance annotations reusable across bundles while keeping bridge cards structurally governed by `F.9`. |
| **Interpretive help vs substitution abuse** | Help readers interpret a bridge without silently licensing substitution beyond what `F.9` allows. |

### F.9.1:4 - Solution
A Bridge Stance Overlay is a local interpretive annotation attached to an existing `F.9` bridge card. It does not change the underlying bridge kind, direction, `CL`, or loss notes.

#### F.9.1:4.1 - Starter overlay vocabulary
| Stance | Intended reading | What it does **not** imply |
|---|---|---|
| `localRename` | the target term is near-renaming within the current context boundary; if a cross-context relation is live, the `F.9` bridge card must exist first | automatic cross-context identity |
| `operationalizes` | the target is a procedural or operational reading aid over the declared bridge | enactment, implementation, execution permission, gate approval, `A.15` work authority, or type-structure equivalence |
| `partialAnalogy` | some explanatory pattern is shared, but only partially | admissible substitution |
| `projection` | the target is a deliberate reduction or aspectual projection of the source bridge reading | completeness, reversibility, loss governance, recoverability governance, narrower-use permission, or source reopen |
| `nonEquivalent` | the bridge card does not license equivalence or silent substitution | `Disjoint`, `CL=0`, or a full incompatibility verdict unless the bridge card itself says so |

#### F.9.1:4.2 - Boundary rule
A stance annotation is interpretive help for authors and readers. It is not a second bridge ontology, not a bridge card, and not a permission and not a publication with named authority-reference relation.

It is also not the coarsening governing pattern. Labels such as `projection` or `nonEquivalent` may help a reader interpret an already-declared bridge, but they do not carry source tether, narrower admissible use, non-admissible downstream use, or reopen duty for a coarsened rendering. If that coarsened-rendering relation becomes primary, it belongs to `A.6.3.CSC Controlled Semantic Coarsening` rather than being absorbed into stance language. If return to the source-bearing episteme or source publication is still needed before any bridge reading is admissible, reopen that episteme or publication before adding stance.

#### F.9.1:4.3 - Relation to `CL` and loss
- `CL` still governs substitution licence.
- loss notes still govern what fails to carry.
- stance annotations merely say how the author wants the bridge to be read.

If the stance materially affects interpretation, the bridge card should publish explicit loss notes that match it.

### F.9.1:5 - Archetypal Grounding
**Tell.** A stance annotation says how to read the bridge, not what the bridge kind structurally is.

**Show (System).** An operator alarm label may `operationalizes` a broader control cue without becoming identical to it.

**Show (Episteme).** A TAE felt-sense phrase may be only a `partialAnalogy` to a later formal term.

### F.9.1:6 - Bias-Annotation
Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for stance overlays attached to existing `F.9` Bridge Cards inside FPF.
This pattern favors disciplined cross-school comparison and bridge readability over sweeping synonym claims. The main mitigation is that every stance remains subordinate to the underlying Bridge Card, its direction, `CL`, and loss notes, with explicit handoff to `A.6.3.CSC` when the live issue is source-bearing return for a coarsened rendering rather than bridge-card reading.

### F.9.1:7 - Conformance Checklist
- `CC-F.9.1-1` A stance annotation **SHALL NOT** replace the underlying `F.9` bridge kind.
- `CC-F.9.1-2` Stance annotations **SHOULD** be accompanied by explicit loss notes when they materially affect interpretation.
- `CC-F.9.1-3` `nonEquivalent` **SHALL** block silent substitution.
- `CC-F.9.1-4` A stance annotation **SHALL NOT** claim higher-CL sameness than the bridge card's `CL` and kind allow.
- `CC-F.9.1-5` A stance annotation **SHALL NOT** stand in for source-bearing return when a coarsened rendering still needs reopen before any bridge-bearing reading is admissible; that relation belongs to `A.6.3.CSC Controlled Semantic Coarsening`.

### F.9.1:8 - Common Anti-Patterns and How to Avoid Them
- **Annotation as ontology.** Do not treat stance as the bridge kind itself.
- **Friendly-vague analogy.** If the relation is high-loss, say so explicitly.
- **Stance inflation.** Do not use the annotation to smuggle in substitution rights that `F.9` withholds.
- **Stance as coarsened-rendering cure.** Do not add `projection`, `localRename`, or another overlay as if that repaired a coarsened note that still needs source-bearing return before bridge reading.

### F.9.1:9 - Consequences
The benefit is reusable interpretive clarity for bridge-heavy bundles and school comparisons. The trade-off is one more declared annotation layer on bridge cards.

### F.9.1:10 - Rationale
`U.LanguageStateSpace` and `U.LanguageStateTransductionTrajectory` create many legitimate cross-school comparisons. `F.9.1` gives those comparisons a reusable stance vocabulary without fragmenting the underlying `F.9` bridge discipline.

The practical gain is narrow but real: teams already use short stance glosses in review work, and without a governed overlay those glosses either smuggle bridge `CL` through casual wording or sprawl into a second bridge taxonomy. Keeping the overlay subordinate to the bridge card lets bundles reuse interpretive cues while the boundary rule and the worked `projection` anti-case keep source-bearing return and bridge publication duty where they belong.

### F.9.1:11 - SoTA-Echoing
**SoTA note.** This section does not mint an independent second bridge rule track. It stays truthful only when the boundary rule, conformance checklist, worked bridge-card examples, and legacy-note repair below still tell the same story about the stance staying subordinate to the bridge card.

**Traditions covered.** This overlay binds itself to comparative-theory glossing, design-translation annotation, operator documentation, and other practices that add short interpretive stance labels on top of already governed relation cards.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `F.9.1` | Adoption status |
| --- | --- | --- | --- | --- |
| A short stance label can help reading only if the underlying concept/relation remains explicit. | Terminology practice distinguishes concepts, designations, definitions, and relations, and treats a designation as a representation of a concept rather than the concept itself. | ISO 704:2022; ISO 1087:2019. | `F.9.1` lets a stance word such as `localRename` or `projection` guide reading only after the underlying `F.9` bridge card remains primary. | **Adopt/Adapt.** Adopt designation/concept separation; adapt it into local stance overlays; reject treating the stance word as a bridge kind. |
| Viewpoint notes and model annotations help users only when they remain subordinate to the described relation. | Architecture-description and model-based engineering practice use viewpoints, views, model elements, and traceable semantics to keep explanatory descriptions tied to explicit underlying descriptions. | ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025). | `F.9.1` keeps stance overlays subordinate to bridge kind, direction, `CL`, and loss notes, with worked examples showing where the overlay helps and where it must wait. | **Adapt.** Adapt viewpoint/traceability discipline to bridge-card reading; reject a second bridge taxonomy. |
| Shared operational names and semantic attributes aid observability and documentation, but common naming does not by itself license substitution. | Contemporary observability practice standardizes common operation and data names while keeping those conventions tied to explicit resources, spans, metrics, logs, and profiles. | OpenTelemetry Semantic Conventions (2025). | `F.9.1` adopts the value of short reusable glosses, but keeps them local to the bridge card and loss notes. | **Adapt/Reject.** Adapt common-name discipline as a readability aid; reject common naming as proof of equivalence or completeness. |
| Validation and metadata practice keeps annotations inspectable instead of letting them replace the object they annotate. | Semantic-web validation and catalog practice separates shapes/metadata from the data graph or dataset being described. | W3C SHACL (2017); W3C DCAT v3 (2024). | `F.9.1` treats a stance overlay as inspectable annotation over a bridge card, not as a substitute bridge or source-return cure. | **Adapt.** Use annotation discipline to keep stance local and reviewable. |

**Worked-slice docking.** The nearest practical recovery anchors here are the `localRename`, `operationalizes`, `projection`, and `partialAnalogy` examples in `F.9.1:13.1` through `F.9.1:13.4`, plus the anti-case `F.9.1:13.5`. If the SoTA claim cannot be recovered through those worked slices and the early boundary rule, do not let the citation stand in for the live pattern law.

**Local stance.** Best-known current practice supports a narrow rule: stance labels are useful only when they stay visibly subordinate to a published bridge card, its direction, `CL`, loss notes, and reviewable source-cell and target-cell structure.

### F.9.1:12 - Relations
- Builds on: `F.9`, `C.2.2a`.
- Primary boundary: `F.9` governs Bridge Card discipline; `F.9.1` governs only stance overlays attached to existing Bridge Cards.
- Coordinates with: `A.16.0`, `E.17.1`, `A.6.P`, `A.6.A`, `A.6.Q`, `C.25`, and `B.4.1`.
- Constrains: local stance annotations on bridge cards used in comparative and tradition bundles.
### F.9.1:13 - Worked Bridge-Card Examples

#### F.9.1:13.1 - `localRename`
A bridge card may relate two near-coextensive operational labels inside one declared context fragment and mark the stance as `localRename`. The bridge card still publishes its own direction, kind, `CL`, and loss notes. The stance only warns the reader that the author's intended reading is close renaming **within that boundary**; it does not license export of the rename beyond the stated fragment.

#### F.9.1:13.2 - `operationalizes`
A broad capability cue may be bridged to a more procedural checklist or control ritual. The bridge card may carry the stance `operationalizes` to show that the target is being read as a procedural or operational gloss over the source. The relation can still be high-loss: the procedural target need not preserve the source's broader theoretical framing, and the stance does not claim type-structure sameness, implementation authority, execution permission, gate approval, or `A.15` work authority.

#### F.9.1:13.3 - `projection`
A rich construct may be mapped into a narrower reporting or measurement rendering. The bridge card may declare the stance `projection` when the target intentionally keeps only one aspect. The required loss notes should name the dropped dimensions, because the stance is informative only when the omitted structure is made explicit.

Table-level note: `projection` is only a stance over a declared bridge. It does not govern loss, recoverability, narrower admissible use, non-admissible downstream use, or source reopen for a coarsened rendering; that relation belongs to `A.6.3.CSC Controlled Semantic Coarsening`.

#### F.9.1:13.4 - `partialAnalogy` and `nonEquivalent`
A comparative bundle may need to mention an explanatory resemblance across traditions without claiming substitution. In such cases `partialAnalogy` may guide reading when the shared pattern is local and declared. If review concludes that this local resemblance still lacks reuse support, `nonEquivalent` should be preferred so that apparent similarity does not drift into silent replacement. The label blocks equivalence and silent substitution; it does not by itself assert `Disjoint` or `CL=0` unless the underlying `F.9` bridge card says so.

#### F.9.1:13.5 - `projection` is not a coarsened-note cure
A team may write a short comparison note saying that one report-only metric is `basically a projection` of a richer operations concept. That sentence does not by itself justify a `projection` overlay. First recover the underlying `F.9` bridge card, its direction, `CL`, and Loss Notes from the source-bearing episteme or source publication needed for bridge support. Only then may the overlay say how to read that bridge. If readers still need return to the source-bearing episteme or source publication before any bridge-bearing use is admissible, the overlay must wait; it cannot repair the missing bridge card.

### F.9.1:14 - Practical use guidance

- Publish a stance overlay only on top of a complete bridge card that already declares bridge kind, direction, `CL`, and explicit loss notes where needed.
- Choose the least-committing stance that truthfully describes the intended reading; do not upgrade the overlay merely because it sounds more helpful.
- If multiple interpretive notes are needed, prefer one primary stance plus explicit loss notes rather than several competing overlays.
- Use `nonEquivalent` when the main value of the annotation is to warn the reader away from substitution.
- In comparative sets or tradition-focused bundles, place the overlay near the bridge card it qualifies so readers can inspect structural bridge data before reading the interpretive gloss.

A practical check is simple: ask whether the overlay merely helps reading or is covertly claiming extra sameness, transport, or substitution rights. If it does the latter, revise the bridge card itself rather than decorating it.

### F.9.1:15 - Legacy-note repair and boundary
Legacy comparative notes often contain undeclared stance language such as "roughly the same", "really a projection", or "just an operational version". When such a note is normalized, the first repair step is to recover the underlying bridge card in `F.9`; only then may a Bridge Stance Overlay be added as an explicit local stance annotation.

The pattern intentionally does not define a second bridge taxonomy, a new substitution calculus, or a score for bridge quality. Those responsibilities remain with the bridge card, `CL`, and declared loss discipline. Tradition bundles may carry many bridge cards with stance overlays, but the overlays remain local annotations attached to those cards, not free-standing comparative objects.
### F.9.1:16 - Overlay Declaration Discipline

A stance overlay is useful only when it stays visibly subordinate to the bridge card it qualifies.

#### F.9.1:16.1 - Minimal overlay declaration
A usable stance overlay should normally publish:

- the qualified `F.9` bridge card,
- the chosen stance term,
- the local reason the stance is helpful,
- and any loss emphasis that becomes especially important under that stance.

Without this declaration set, a stance word becomes a decorative gloss detached from the bridge it is supposed to interpret.

#### F.9.1:16.2 - One primary stance per bridge card
A bridge card should normally carry one primary stance overlay. If several interpretive notes are needed, the extras should usually live in explicit loss notes or surrounding commentary rather than in several competing stance tags.

#### F.9.1:16.3 - Overlay locality
A stance overlay is local to the bridge card and context fragment that publish it. Reusing the same stance label elsewhere is admissible only when the new bridge card independently supports that reading.

### F.9.1:17 - Interaction with `CL`, Direction, and Loss

#### F.9.1:17.1 - `CL` remains prior
If the stance sounds friendlier than the declared `CL`, `CL` wins. An `operationalizes` or `localRename` overlay cannot overrule a high-loss bridge or a low-substitution `CL` declaration.

#### F.9.1:17.2 - Direction-sensitive reading
Some stance labels read differently depending on bridge direction. A construct may project into a report-only rendering in one direction while the reverse direction is not admissible at all. Authors should therefore avoid stance prose that sounds symmetric when the bridge card is directional.

#### F.9.1:17.3 - Loss emphasis rule
When a stance is likely to invite over-reading, the loss note should state a sharper boundary rather than soften it. The overlay is useful exactly because it helps interpretation; that is also why it can mislead if the losses are understated.

### F.9.1:18 - Bundle Use and Comparative Reading

#### F.9.1:18.1 - Bundle-level reuse
Tradition bundles and viewpoint bundles may reuse the same stance vocabulary across many bridge cards, but the interpretation remains card-local. Bundle reuse is a readability aid, not a warrant that similarly named overlays are structurally equivalent.

#### F.9.1:18.2 - Comparative stance caution
Two bridge cards may both be marked `projection` while dropping very different dimensions. Reviewers should therefore compare the loss notes and source-cell and target-cell structure, not the overlay term alone.

#### F.9.1:18.3 - Boundary to second bridge taxonomy
If authors start grouping bridges primarily by stance label and ignoring bridge kind, direction, `CL`, or loss, they have implicitly created a rival bridge taxonomy. `F.9.1` forbids that drift.

### F.9.1:19 - Review Matrix and Migration Tests

A reviewer can test stance-overlay integrity with five questions:

1. **Is the underlying bridge card complete and still primary?**
2. **Does the overlay stay within the bridge card's structural claims?**
3. **Would the same overlay still be truthful if read in the reverse direction?** If not, the locality or directionality needs to be made clearer.
4. **Do the loss notes carry the interpretive claim that the overlay might otherwise overstate?**
5. **Is the bundle using stance as a readability aid, or as a covert replacement for bridge ontology?**

Legacy prose about things being "really the same", "only a projection", or "just an operational version" should therefore be migrated by recovering bridge kind, direction, `CL`, and loss first, then adding an overlay only if it still adds disciplined interpretive value.
### F.9.1:End


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
* **DesignRunTag bleed.** Design‑time “approved method” is used as if it proved run‑time “meets SLO”.
* **False substitution.** *Observed availability 99.95%* is silently treated as *SLO satisfied* without declaring the translation.
* **Name inflation.** New U.Types minted to stabilise drifting status words instead of fixing Contexts and Bridges.


### F.10:3 - Forces

| Force                                     | Tension to resolve                                                                             |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Local fidelity vs Cross‑context reuse**    | Keep native Context meanings, yet enable explanation and (sometimes) substitution.                |
| **Didactic simplicity vs status variety** | Many status schemes exist; we need a **small spine** that admits Context synonyms.                |
| **Design vs run**                         | Standards speak design; evidence speaks run; requirements span both; do not swap them.         |
| **Safety vs utility**                     | Substitution is powerful but risky; explanation carries less substitution authority. Make the choice explicit. |


### F.10:4 - Core idea (didactic)

**Three families, two modalities, one habit.**
Treat every status word as a **SenseCell with a declared StatusModality** and **inside one Context**. When you must relate statuses across Contexts, **declare a Bridge** (F.9) that says *what kind of relation*, *which CL value applies*, *which way (if narrower/broader)*, and *what is lost*. Prefer **explanation** Bridges; permit **substitution** only when kind/CL allow it.

**Reading an Episteme.** For every `U.Episteme`, read the `DescribedEntitySlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`, `ViewpointSlot`, and carrier references under A.7 and MVPK. **Statuses classify the Episteme;** enactment remains with `U.System` and `U.Work`. (Formal identity rules: see **KD‑CAL**.)

### F.10:5 - Minimal vocabulary (this pattern only)

* **StatusFamily.** Sub‑typing inside **senseFamily=Status**: one of **EvidenceStatus**, **StandardStatus**, **RequirementStatus**.
* **StatusCell.** A **SenseCell** whose meaning is a status with a declared **StatusModality ∈ {epistemic, deontic}**
* **StatusModality.** The mode of a StatusCell: **epistemic** or **deontic**. Use this term instead of the bare word *modality* per E.10 LEX rules.
* **Polarity.** The orientation of a status relative to a claim/obligation: **Positive** (supports/satisfies), **Negative** (contradicts/violates), **Neutral/Undetermined**.
* **Window.** The **applicability span** of a status (temporal or conditional), e.g., “Q3‑2025”, “under load ≥ 70%”.
* **Status target.** The exact value the status qualifies: a **claim** (epistemic), a **method** or exact standard-governed project kind and reference (standard), or a **clause** (requirement).
* **Bridge (F.9).** The only admissible way to relate StatusCells across Contexts; declares **kind** (≈, ⊑, ⊒, ⋂, ⊥, or an Interpretation arrow), **CL**, and **Loss**; **substitution is modality‑preserving**.

> **StatusModality guard.** EvidenceStatus is **epistemic**; StandardStatus & RequirementStatus are **deontic**. **Role Description Status** templates (F.4) bind to these **StatusModalities**; **no mixing**. The bare token *modality* is against E.10/LEX); this pattern uses **StatusModality**.


### F.10:6 - The spine: three local ladders (Context‑native, small and renameable)

> The following ladders are **didactic spines**. Each Context may rename levels or insert thin sub‑levels, but Bridges must state how they align to this spine (kind & CL). Names appear in **Tech** / **Plain** register.

 -   **Episteme‑as‑actor (forbidden).** Never attribute **Work** to an Episteme; only Systems act.

-   **Requirement vs Hypothesis.** “Desired property/goal” is **not** `Requirement` status; use hypothesis/target + evaluation.

-   **Mereology ≠ Provenance.** Part‑whole edges never justify claims; use EPV‑DAG with carriers.


#### F.10:6.1 - EvidenceStatus (epistemic statusModality)

**EvidenceStatus order (lower-support to higher-support):**

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

**Citation operators (context‑scoped).** Authors MAY use the **typed edges** `supports`, `refutes`, `dependsOn`, `supersedes` **inside a single Context** when expressing how an `Evidence`/`Standard` status applies. **Formal semantics are governed by B.3.2 (Evidence & Validation Logic).** Cross‑Context use requires a declared **Bridge** (F.9) and carries CL/Loss penalties.


### F.10:7 - Solution — how meanings connect (conceptual, notation‑free)

**S‑1. Anchor status meanings per Context.**
Every status word (*validated*, *approved*, *compliant*) is treated as a **StatusCell** inside a specific Context. The **ladder position** is determined **locally** (e.g., “validated (metrology)” aligns to **Replicated** with CL stated; “validated (software)” may align to **Corroborated**).

**S‑2. Attach statuses to the right Targets.**
*EvidenceStatus → Claim or Quantity; StandardStatus → Method/Artefact; RequirementStatus → Clause.*
This prevents swapping “how we measure” with “what we promise”.

**S‑3. Translate via Bridges, not by name.**
Example: **Measured availability (SOSA)** →ᴍᴇᵃ **SLO clause (ITIL)** with **CL=2**, Loss: sampling window & clock skew. This supports **explanation**; **substitution** (“Satisfied”) requires **same StatusModality**, a stricter Bridge kind (F.9) **and** a declared evaluation rule (from the Service pattern), not from F.10.

**S‑4. Keep DesignRunTag honest.**
**StandardStatus** is design‑stance; **EvidenceStatus** is run‑signal; **RequirementStatus** spans both. Use **Interpretation Bridges** (F.9) for design↔run readings, not equivalence.

**S‑5. Prefer explanation over substitution.**
If a Bridge cannot reach **CL≥2** on the **same senseFamily**, do **not** substitute. Use **Naming‑only** rows or **explanations**; keep Role Descriptions (F.4) out of harm’s way.


### F.10:8 - Invariants (normative, lightweight)

1. **Modality purity.** A StatusCell’s **StatusModality** is explicit and **must not change** during reasoning; cross‑modality claims require an **Interpretation Bridge** (F.9).
2. **Target typing.** A status **must name its Target kind**: claim, artefact, or clause. Inferences that ignore the Target kind are invalid.
3. **Window discipline.** Every positive/negative status **names a Window**; contradictions are detected **within the same Window** only.
4. **Local monotonicity.** Within one context, a higher-support EvidenceStatus implies all lower-support positives for the same Target & Window.
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
| **AP‑4**  | **Synonym drift of status labels**           | *Verified/validated/approved* used interchangeably across Contexts.               | Homonymy across Contexts; undercuts claim support.                                               | Treat each status word as a **StatusCell** tied to its Context; relate only via **Bridge(kind, CL, Loss)**.                                                                                                                                       |
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

**Contexts.** *ML validation canon* — DesignRunTag hybrid; *Policy Context (fairness charter)* — deontics; *SOSA/metrics* — sensing.

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
   *Reading:* Higher-support status implies lower-support status within the same Window.

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
> When you must relate status meanings across Contexts, **draw a Bridge** that states the **kind** (≈, ⊑/⊒, ⋂, ⊥ or Interpretation), the **CL** value, and the **Loss** (what you ignore). Prefer **explanation**; allow **substitution** only when statusModalities match, kind permits, **CL≥θ**, and Windows align.
> Keep **design vs run** stance honest: approval is **design‑time**, evidence is **run‑time**, requirements **span both**. With this habit, “validated”, “approved” and “compliant” stop being a muddle of synonyms and become **precise, local meanings** you can compare **safely** and **audibly**.

### F.10:End

## F.11 - Method Quartet Harmonisation

**“Keep the *how* (Method), the *recipe* (MethodDescription), the *happening* (Work/Execution), and the *control push* (Actuation) in their own Contexts—then relate them explicitly.”**

**Status.** Architectural pattern.
**Builds on:** E.10.D1 **D.CTX** (Context discipline); A.3/**A.3.1**/**A.3.2** (Transformer Constitution; `U.Method`, `U.MethodDescription`); A.15/**A.15.1** (`U.Work` as record of occurrence); Sys‑CAL (control/actuation semantics); KD‑CAL (observation).
**Coordinates with.** F.1–F.3 (Contexts, Seeds → SenseCells), F.4 (Role Description), F.5 (Naming), F.6 (Role Assignment & Enactment Cycle (Six-Step)), F.7/F.9 (Bridges), F.10 (Status families & Windows).
**Aliases (informative).** *Method/Spec/Work or Actuation split*; *DesignRunTag harmonisation*.


### F.11:1 - Intent & applicability

**Intent.** Provide a **notation‑free, Context‑aware map** that keeps four notions distinct and connectable:

* **`U.Method`** — the abstract **way of doing** (design‑time concept).
* **`U.MethodDescription`** — the **recipe episteme** that describes a Method.
* **`U.Work`** (informal: *Execution*) — the **run‑time occurrence** of doing (recorded event).
* **`U.Actuation`** — the **control output** applied to a plant (domain‑specific Work in Sys‑CAL).

The pattern makes the split **usable across FPF patterns** (Role Assignment & Enactment, Sys-CAL, KD-CAL, Kind-CAL, planned LCA-CAL) and **legible across Contexts** (SPEM/BPMN for design; PROV-O/SOSA for run; IEC 61131-3/state-space for control).

**Applicability.** Any time a discussion risks **mixing designs with executions**, **recipes with runs**, or **workflow with control signals**; whenever you need to **name** or **reason** about “how we do X”, “the SOP/script/model”, “the actual run”, or “the actuator push”.

**Non‑goals.** No team workflow, no editors, no tools. No prescriptive file formats. **Only** conceptual distinctions and safe reasoning moves.


### F.11:2 - Problem frame

When Method, MethodDescription, Work, and Actuation **collapse into one another**, models drift:

1. **DesignRunTag blur.** A BPMN *process* (design graph) is cited as if it had *happened*.
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

* If the claim is about **what should be done** or **how it is described**, you are on the **design stance** (Method or MethodDescription).
* If the claim is about **what happened** or **what was emitted**, you are on the **run stance** (Work or Actuation).
* **Guard rule.** Never let a conclusion cross stances without (a) an explicit Bridge kind (*interpretation* vs *substitution*), and (b) an acceptable CL (F.7/F.9, F.10).

#### F.11:6.2 - The **recipe/idea split**

* **Method** is the **idea**; **MethodDescription** is the **recipe** describing that idea.
* Different recipes may describe the **same** method (profiles, languages, detail profiles); one recipe may encode **several** methods (composite SOP).
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

1. **DesignRunTag honesty.** Statements about **Method or MethodDescription** (design) **MUST NOT** be used as if they were statements about **Work or Actuation** (run) without an explicit Bridge and Window.
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
| **A3**  | **Execution = Actuation**      | PLC log of setpoints recorded as the whole execution history.         | Loses non‑signal aspects (delays, conditions, context); removes reasoning support.  | Model **Actuation** as **within** **Work**. Keep both SenseCells: *Task execution* (Work) and *Command/Setpoint* (Actuation).                                                                                        |
| **A4**  | **BPMN‑as‑Run**                | BPMN *Process* treated as “the thing that ran.”                       | BPMN’s meaning is context‑local and design‑time.                               | Use a **Bridge** (F.7/F.9) from *BPMN\:Process (design)* → *PROV\:Activity (run)* with kind **Interpretation**, CL/Loss declared.                                                                                    |
| **A5**  | **Spec Drift Retroactivity**   | Update to a recipe is assumed to modify past executions.              | Violates temporal honesty; breaks auditability.                             | Past **Work** remains as‑was. New **MethodDescription** versions describe future **Work** only; record variant relations if a run deviated.                                                                                 |
| **A6**  | **Homonym Collapse**           | *Task*, *activity*, *process* used interchangeably across Contexts.      | Imports meaning implicitly; masks losses.                                   | Prefix with **Context** and use **SenseCells**: e.g., *task (IEC)*, *activity (PROV)*, *process (BPMN)*. Any relation uses **Bridges** with CL/Loss.                                                                    |
| **A7**  | **Signal‑Only Compliance**     | SLO judged solely from actuator traces.                               | Ignores measured outcomes; risks false positives.                           | Tie **SLO** clauses to **Observations** (KD‑CAL) **about Work outcomes**; treat Actuation as an input, not proof.                                                                                                    |
| **A8**  | **Recipe-as-Role**             | “The Spec assigns responsibility” (mixes MethodDescription with Role constructs — `U.RoleDescription`/`U.RoleAssignment`).  | Conflates the `U.MethodDescription` episteme with behavioural masks.         | Use **F.4 Role Description**; let **MethodDescription** only **describe** a Method.                                                                            |
| **A9**  | **One‑Context Scope**        | A single Context (e.g., BPMN) used as if it covered control/measurement. | Scope mirage; silent cross‑domain generalisation.                           | Re‑cut Contexts (F.1) to include control and sensing. Re‑express statements with the quartet across those Contexts.                                                                                                        |
| **A10** | **Lossless Bridge Assumption** | Claiming “equivalent” across Contexts without Loss.                      | Hides mismatches; unsafe transfer of inferences.                            | In **F.7/F.9** declare Bridge **kind**, **CL**, and explicit **Loss** notes.                                                                                                                                         |
| **A11** | **Recipe‑as‑Type**             | Treating a MethodDescription vocabulary as a type taxonomy.                  | Category error; misuses Kind-CAL.                                           | If a stable hierarchy of **kinds** of Methods is needed, mint **U.Type** nodes in Kind-CAL; keep MethodDescription as *description* only.                                                                                   |
| **A12** | **Actuation Outside Work**     | Commands modeled without enclosing Work.                              | Severs signal from enactment context; breaks traceability.                  | Embed **Actuation** **within** **Work** intervals; relate to the enacting Role and Method or MethodDescription references.                                                                                                     |


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

* **Contexts:** *SPEM/ISO 24744* (design), *Lab assay canon* (DesignRunTag split as per discipline), *PROV‑O* (run), *SOSA/SSN* (sensing).
* **Quartet:**

  * **Method:** *ELISA*.
  * **MethodDescription:** *Kit IFU v7 (instructions for use)*.
  * **Work:** *Batch B217 performed 2025‑06‑21* (PROV Activity).
  * **Actuation:** *Pipetting robot commands* (optional detail).
* **Statuses:** *Spec Approved*; *Work Observed* (absorbance readings); *Quality gate Satisfied* within batch Window.
* **Bridge(s):** IFU (design) **interprets** Activity (run) for acceptance (CL=2, **Loss:** deviations allowed per kit tolerances).

**Pay‑off:** A clean line from recipe → run → measurement → decision, without role-assignment and status-assertion conflation.


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

12. **SLO attachment guard**
    `SLO clause about service outcome ⊢ attachesTo(Work-window), not MethodDescription`
    *Reading:* Service obligations concern **what happened** within a Window, not the existence of a plan.


### F.11:13 - Relations

**Builds on:**
E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); A.3/**A.3.1**/**A.3.2**/**A.15** (Method/Spec/Work foundations); Sys‑CAL (Actuation semantics); KD‑CAL (Observation); F.1–F.3 (Contexts → SenseCells); F.10 (Status families & Windows).

**Constrains:**

* **F.4 Role Description:** Roles or Statuses **must** point to the right box (e.g., *Approved* → MethodDescription; *Observed* → Work).
* **F.5 Naming:** Enforce distinct Tech/Plain labels for Method/Spec/Work or Actuation where homonyms threaten.
* **F.7/F.9 Bridges:** All Cross‑context assertions among quartet terms **must** go through explicit Bridges with **kind/CL/Loss**.

**Used by.**
Part C patterns (Sys‑CAL, KD‑CAL, Method‑CAL, Kind-CAL, LCA‑CAL) when describing examples, proofs, and cross‑disciplinary mappings.


### F.11:14 - Migration notes (conceptual)

1. **Split conflated “process”.** Where a single “process” node stands for both plan and run, refactor into **MethodDescription** (design) and **Work** (run); add a Bridge if the prose relied on identity.
2. **Reassign statuses.** Move any *Approval*-like statuses from Work to MethodDescription; move *Satisfied/Violated* from Spec to clauses about Work within **Windows**.
3. **Expose actuation.** If control outputs are buried in “execution logs,” mint **Actuation** SenseCells and relate them **within** Work.
4. **Version fences.** Past Works keep references to the **version** of MethodDescription they attempted to follow; don’t update those links retroactively.
5. **Name collisions.** Where *task/activity/process* appear with mixed meanings, prefix with Contexts and relabel per **F.5** (Tech/Plain).
6. **Backfill Bridges.** If earlier text implied Cross‑context equivalence, add explicit Bridges (F.7/F.9) declaring **kind/CL/Loss**.


### F.11:15 - Acceptance tests (SCR/RSCR — concept level)

#### F.11:15.1 - Static conformance checks (SCR)

* **SCR‑F11‑S01 (DesignRunTag honesty).** Every normative claim about outcomes is attached to **Work** (with Window), not to **Method or MethodDescription**.
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
**Coordinates with.** KD‑CAL (Observation/Characteristic/Scale); Sys‑CAL (Work or Actuation contexts).
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

**R1 — Attachment rule.**
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

1. **DesignRunTag split.** Clauses live on the **design stance**; judgements live on the **run stance** about **Work** (F.11).
2. **Context locality.** All terms are **context‑local**; Cross‑context meaning flows **only** across declared **Bridges**.
3. **Observation‑only evidence.** Verdicts require **Observations** that **about‑refer** to Work outcomes; **Actuation** and **Approvals** are not sufficient.
4. **Window explicitness.** Every verdict carries a **Window**; no timeless acceptance.
5. **Predicate declared.** The Clause’s **Predicate** is explicit; no hidden aggregation or default percentile.
6. **Non‑retroactivity.** Updating clauses or specs does not alter past verdicts; re‑evaluation must be explicit.
7. **One‑Work focus.** A verdict references a **specific Work** (or a defined population of Works) matched to the Clause’s scope.
8. **Loss honesty.** Each Bridge states **kind**, `CL`, and loss; wider claims require Bridges with the needed `CL` or same-Context alignment.
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
| **A1**  | **Plan‑as‑proof**               | A BPMN or runbook is cited as if it proved the SLO was met.                                  | Design artefacts are **not** occurrences.       | Apply **R1 attachment** + **R2 evidence**: attach the verdict to **ClauseCell\@Window about WorkCell** and require **Observations** of outcomes.              |
| **A2**  | **Signal‑as‑outcome**           | Control **Actuation** (setpoint writes, approvals) treated as evidence of delivered service. | Commands are intentions, not results.           | Accept only **MeasureCell** that **about‑refer** to the **same Work**; if a control signal is used as proxy, declare a **Bridge(kind=proxy, CL, Loss)**. |
| **A3**  | **Windowless verdict**          | “We met the SLA” with no stated period or scope.                                             | Unfalsifiable; mixes populations.               | Enforce **R5 Window**: every verdict names a **Window** (month, batch, incident interval).                                                               |
| **A4**  | **Global words**                | *Availability*, *latency* used without a Context.                                               | Collides senses across disciplines.             | Speak with **Context prefixes** (F.1). Cross‑context reuse demands a **Bridge** (F.9).                                                                         |
| **A5**  | **Percentile mirage**           | p95 computed on a pooled year while the clause is monthly.                                   | Predicate and Window misaligned.                | **R3 Predicate** + **R5 Window**: compute the statistic **per Clause’s Window**.                                                                         |
| **A6**  | **Proxy blindness**             | Synthetic probes stand in for user experience with no limitations stated.                    | Proxies miss geography, jitter, or pathologies. | Declare **Bridge(kind=proxy, CL, Loss)**. If proxy coverage is insufficient for the clause scope, the verdict is **Inconclusive**.                                                |
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
  **F.11**: protects **Method**, **MethodDescription**, **Work**, and **Actuation** distinctions.

* **Uses (Part C patterns).**
  **KD‑CAL** (Observation/Characteristic/Scale/Unit).
  **Sys‑CAL** (Work or Actuation Contexts).
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

Rather than maintain a tool or workflow, **think with five continuity relations**. Use the least-committing relation that tells the truth.

#### F.13:6.1 - Continuity relations (normative meanings)

1. **`renames(label_old → label_new)`** — *wording improved, sense unchanged*.
   *Use when:* Same **SenseCell** / same **Concept‑Set row** / same **Role Description**; only the lexical form changed to satisfy F.5 (morphology, disambiguation, plain/tech harmony).
   *Effect:* `label_old` becomes a **context‑local alias** of `label_new`; both resolve to the **same SenseCell, Concept-Set row, or Role Description**. Past texts remain valid.

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
| **A11** | **Temporal fudge**         | Rename used to imply design↔run shift (“execution ≈ process”).        | Conflates time stances; erases important dualities.            | Keep **DesignRunTag** explicit on labels or glosses; if mapping is needed, do so in **F.9**.                                       |
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
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of deprecated aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR‑F13‑S05 (Row integrity).** A row rename occurs only when the row’s **intension** is stable; if membership changed, a **row split/merge** is documented (F.7).
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation belongs under **F.9**.

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
**Aliases (informative).** *Role and Status economy*; *Explosion guard*.


### F.14:1 - Intent & applicability

**Intent.** Prevent the uncontrolled growth of **Roles** and **Statuses** by privileging **reuse**, **bundling**, **explicit separation‑of‑duties (SoD)**, and **applicability windows** over minting new names. Keep the vocabulary **small, crisp, and composable** while remaining faithful to local meanings fixed by Contexts (F.1) and SenseCells (F.3).

**Applicability.** Whenever a new Role or Status is proposed, a team merges two lines of work, or a domain shifts its jargon. Use this pattern before adding rows to the Concept‑Set Table (F.7) or new Role Descriptions (F.4).

**Non‑goals.** No org charts, no RBAC policies, no process roles. This pattern describes **mental moves** for architectural naming, not governance machinery.


### F.14:2 - Problem frame

Left unchecked, Role and Status vocabularies tend to **diverge**:

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
| **Locality vs uniformity**      | Roles or Statuses are **context‑local**; yet we need a stable Cross‑context story through Concept‑Set rows.     |
| **Safety vs convenience**       | SoD constraints protect systems, but people seek convenience through composite roles.                  |
| **Temporal honesty**            | Many “new” Statuses are actually the **same** Status seen in different **windows** (design, run, or grace). |


### F.14:4 - Minimal vocabulary (this pattern only)

* **Role Description** (F.4): a **Role** (behavioural mask) or **Status** (epistemic/deontic standing) tied to a **SenseCell**.
* **Concept‑Set row** (F.7): a Cross‑context **intent** (“what we count as one thing”) aligned by SenseCells.
* **Bundle** (this pattern): a **named composition** of Role Descriptions that are meant to be used together by design (e.g., {Requester, Approver} for change control). A Bundle is a **concept**, not a package.
* **SoD Constraint** (this pattern): a **conceptual rule** stating that two Roles **must not** be played by the same Holder in the **same window**.
* **Window** (F.10): an **claim scope** (time stance, holon level, run segment) that delimits when a Role or Status holds.


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

* **Move.** Treat qualifiers (shift, locality, domain) as **facets** of the same Role or Status or as **windows**, not new types.

**Example (operations).** *Operator* with **window facet** `timeOfDay = night`—not a new Role *Night‑Operator*.


### F.14:7 - Invariants (normative)

1. **context‑locality.** Each Role Description remains tied to a **SenseCell** in a **single Context** (F.3, F.4).
2. **Row preference.** New Role Descriptions **SHOULD** map to an existing row; new rows (F.7) require F.8 justification.
3. **No hybrid Roles.** If two Roles are conceptually distinct, they **must not** be fused into one to bypass SoD. Use **Bundle + SoD**.
4. **Windowed statuses.** Status proliferation across time/scale **MUST** be expressed as **windows** of a single Status family (F.10).
5. **Bundle clarity.** A Bundle **names only composition**; it does not inherit or redefine member semantics.
6. **Minimal modifier naming.** Adding a modifier to a label **MUST** pass F.5 tests; prefer facets/windows over new Role or Status names.
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


### F.14:9 - Micro‑examples (engineer, manager, and researcher lenses)

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
* **Used by.** FPF patterns to keep Role and Status vocabularies tight.


### F.14:13 - Migration notes (conceptual playbook)

1. **Map to rows.** For each existing Role or Status, identify its **Concept‑Set row**; if two names share an intent, **collapse** to one row (keep other names as **aliases**, F.13).
2. **Extract SoD.** Replace “super‑roles” with **Bundles** plus explicit **SoD**; where conflict exists, SoD is **normative**, not cultural.
3. **Demote modifiers.** Convert adjectival Role types into **U.Facet** (per Compose‑CAL) or **windows** on the base Role.
4. **Window statuses.** Merge Status families split by time/scale into **one Status + windows**; move waived/exempt notions to the **deontic Context** if applicable.
5. **Re‑use before minting.** When encountering a gap, scan rows for a near‑match; only if intent genuinely differs, open a **new row** (F.8).
6. **Preserve continuity.** Keep historic labels as **aliases** under the consolidated template (F.13); do not rewrite past texts.
7. **Rehearse the cut.** After consolidation, you should be able to recite the entire Role and Status vocabulary **from memory**; if not, reduce again.


### F.14:14 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.14:14.1 - SCR — Static conformance

* **SCR‑F14‑S01 (Row reuse).** Every newly proposed Role Description either **references an existing row** or includes a clear **F.8 justification** for a new row.
* **SCR‑F14‑S02 (No hybrids).** No Role Description’s label or definition **conflates** two Roles that stand in a declared **SoD** relation.
* **SCR‑F14‑S03 (Windowed statuses).** Each Status family that shows temporal/scale variation is expressed as **one Status + windows** (not multiple Status types).
* **SCR‑F14‑S04 (Facet over modifier).** Role names do not encode circumstantial modifiers; such modifiers appear only as **facets/windows**.
* **SCR‑F14‑S05 (Context locality).** Every Role Description is anchored to **exactly one SenseCell**; no Cross‑context semantics inside a single template.
* **SCR‑F14‑S06 (Bundles are pure).** Every **Bundle** is a **set of templates** with **no additional semantics** beyond membership and referenced **SoD**.

#### F.14:14.2 - RSCR — Regression (evolution)

* **RSCR‑F14‑E01 (Vocabulary slope).** Over a given interval, the count of distinct Role or Status templates **does not increase** unless matched by **row justifications** (F.8).
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
3. **Role or Status inflation.** Adjectival or temporal variants become new types.
4. **Silent rewrites.** New editions overwrite old meanings without a trace.
5. **Unstable bridges.** Cross‑context relations harden into dogma without CL or loss statements.


### F.15:3 - Forces

| Force                      | Tension to resolve                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| **Parsimony vs coverage**  | Keep vocabularies small yet expressive across multiple Contexts.         |
| **Locality vs reuse**      | Preserve context‑local meaning while enabling Cross‑context comparison.     |
| **Stability vs evolution** | Allow new editions and rows without erasing prior sense.              |
| **Clarity vs formality**   | Checks must be teachable in minutes yet specific enough to catch drift. |


### F.15:4 - Core idea (didactic)

The harness is a **two-part net of assertions**:

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
4. **Concept‑Set row** — a cross-context alignment hypothesis with explicit Bridge support (F.7).
5. **Role Description** — Role or Status definition pointing to **one** SenseCell (F.4).
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
*Reading:* A row is the **same** row only if each cell still means the same Local-Sense in its Context. Otherwise, mint a **new row** and retire the old (F.7–F.8).

**RSCR‑F15‑E6 (Row shrink‑before‑split).**
`ρ@t1 loses a cell due to edition split ⊢ prefer keep ρ@t0 + add new row ρ' rather than mutating ρ silently`
*Reading:* When a Context splits meaning, preserve history: **add** instead of rewriting.


#### F.15:13.4 - Role Descriptions (Role and Status)

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


#### F.15:15.3 - Tighten a Bridge (low-CL overlap → equivalence)

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

**Intent.** Provide a **single, didactic page template** for cross‑domain worked examples that makes every claim **local to a Context** (Context), every Cross‑context step **explicit via a Bridge**, and every named role template or status template **traceably tied** to one **SenseCell**. The template is **notation‑free** and **tool‑agnostic**; it captures **how to think** the example so others can replay it.

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
* **Plot** = **one Concept‑Set row** where those SenseCells are aligned for this example.
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

7. **Role-Description hooks.** Name the Role or Status templates and the **one SenseCell** each references.
   *Example:* `AvailabilityStatus` → ⟨ITIL\:SLO⟩; `Execution` → ⟨IEC\:execution‑task⟩; `EvidenceObservation` → ⟨SOSA\:observation⟩.

8. **Windows & SoD (if relevant).** Spell any **status windows** and any **SoD** you rely on.
   *Example:* Window: *monthly, business‑hours*; SoD: *Operator* ⟂ *SLO‑Owner*.

9. **Micro‑narrative (5–7 lines).** Walk the reader through the claim using **Context‑prefixed words** and the row/bridges above.
   *Example (abridged):* “A **task (IEC)** runs the control program. Its **observations (SOSA)** yield availability over the *monthly* window. We compare those to the **SLO (ITIL)** in the same window. Where we refer to **activity (PROV)** we do so via **β₁** (overlap, CL=2). The row ρ carries the comparison; the Bridge **β₂** explains why ‘measurement’ in ITIL is broader than ‘observation’ in SOSA.”

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
* **Footline** (one line) = “row reason”—why these cells belong in this row **for this claim**.

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
| **AP-3**  | **Role-Description vagueness**          | A Role or Status named without a SenseCell.                       | Why it breaks thinking                                         | Remedy (point to this template & sibling patterns)                        |
| **AP‑4**  | **Global words**           | *process, role, service* appear unprefixed.                    | Context‑less words drift mid‑example.                             | Prefix first mention with the **Context** (*process (BPMN)*) (§6‑1, E.10.D1). |
| **AP‑5**  | **Window‑free comparison** | Numbers/targets compared with no stated window.                | Apples‑to‑oranges across time/scale.                           | Declare a **Window** for the Status (§5‑8, F.10).                         |
| **AP‑6**  | **SoD leakage**            | Duties named but the same actor implicitly holds both.         | Violates Separation‑of‑Duties intent.                          | State **SoD** and keep duties disjoint (§5‑8, F.14).                      |
| **AP‑7**  | **DesignRunTag blur**        | A design‑time notion used as if it were a run‑time occurrence. | Category error; wrong Context claims.                             | Mark Context stance and keep claims in‑stance (§5‑3, §6‑5).                  |
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
**Contexts.** **SPEM 2.0** (design: Method or MethodDescription), **PROV‑O** (run: Activity), **SOSA/SSN** (run: Observation), **ITIL 4** (design: SLO).
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
* **SCR‑F16‑S06 (DesignRunTag).** Claims respect each Context’s **DesignRunTag** stance.
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

> A useful worked example is a **one‑page alignment**: claim → Contexts → cells → **one row** → explicit **bridges** → Role-Description hooks → window/SoD if needed. No tooling, no process charts—just **visible thinking** that any careful reader can replay and critique at the right place.

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

If a UTS row **describes** a generator, selector, or typed portfolio-publication surface (design‑time or run‑time artefact), it **MUST** add the following fields. These are *publication* fields, not tooling‑specific formats.

| Field | Purpose |
| --- | --- |
| **N (Novelty)** | Lawful novelty claim tied to `CharacteristicSpaceRef` + `DistanceDefRef` (declare metric/pseudometric & invariances; cite edition ids). |
| **U (Use‑Value)** | Declared acceptance/test value under the active **CG‑Frame** (units & scale typed per MM‑CHR). |
| **C (ConstraintFit)** | Feasibility against **ResourceEnvelope/RiskEnvelope** (and relevant deontic/ethics clauses); no `unknown→0` coercion. |
| **D\_P (Portfolio Diversity)** | Diversity contribution relative to the **current PortfolioPack** (`ArchiveConfig`, grid/binning, K‑capacity, dedup). |
| **E/E‑LOG policy‑id (PolicyIdRef)** | Edition id of the explore/exploit governor policy that governed generation/selection budgets. |

**Note.** These fields *extend* the Row Schema; they do not change SenseCells/Bridges/Names. Rows that are *purely definitional* (no generator/selector/typed portfolio-publication semantics) do not carry §6.1.

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
*A.* No. It is a **didactic publication**. No CRUD semantics, no workflows.

**Q2. Can we collapse two Contexts if their terms look identical?**
*A.* Only via **F.9 Bridge** with **CL=3**. Identity must be argued, not assumed by spelling.

**Q3. Where do state‑graphs (A.2.5) show up?**
*A.* In `Notes` or as a dedicated row if the stateful nature of a Role family is central to the thread.

**Q4. How do we show deontic approvals?**
*A.* The concept rows (`U.SpeechAct`, `U.Commitment`, `U.PromiseContentClause`, `U.PromiseFulfillmentEvaluation`) make the communicative/epistemic pieces visible; enactment appears in examples, not as sheet mechanics.

### F.17:18 - 90‑Second Teaching Script

> “To make our language usable, we publish a **Unified Term Sheet** for each thread. Each **row** is one **unified concept** (a Concept‑Set) named with a **Tech** and a **Plain** label and tied to concrete senses in our chosen **context of meaning**. If two contexts differ, we show an explicit **Bridge** with a **CL score** and a short **loss note**. The rows are grouped into 5–7 **didactic blocks** so the whole sheet fits in working memory. This is not a database; it’s the **one table** a careful mind can hold. From this sheet, everyone—engineers, managers, researchers—can talk precisely through **the same Concept-Set rows** across disciplines.”

### F.17:End

## F.18 - Local‑First Unification Naming Protocol
*Status: normative (Part F, Unification Suite). Audience: engineer‑managers, lead architects, editors of FPF records/publications.*

### F.18:0 - Use this when

Use `F.18` when a name must become stable and reusable across one local context, a concept set, a bridge, or a durable FPF/publication vocabulary. Use it when the issue is not merely one overloaded local phrase, but a name that must carry context, kind, local sense, use-domain, bridge posture, and lineage without smuggling global sameness.

**First useful move.** Ask whether the live work is durable naming. If yes, make the name local-first by naming its context, kind, purpose/use-domain, local sense, and bridge posture. If no, use the lighter exact pattern: local phrase repair under `E.10` or `E.10.SEMIO`, relation precision under `A.6.P`, or the domain pattern that governs the named object.

**Cheap stop.** If the wording is one-off local repair and does not create a reusable name, stop after the exact local repair. Do not open a full Name Card, mint a new head, or create lineage entries just because a phrase was clarified.


### F.18:1 - Context

Names must carry enough signal for everyday use, yet never smuggle in Cross‑context identities, hidden assumptions, or role/metric clutter. F.18 supplies that naming discipline and weaves it through F.1–F.17: Term Harvesting, Sense Clustering, Role Descriptions, Concept‑Sets, Bridges, Lexical Continuity, Anti‑Explosion control, and the Unified Term Sheet (UTS).

**Scope.** This protocol applies to naming of **any concepts** authored in Part F (U.Types and **local concepts** alike: kinds, roles, services, methods, works, relations, characteristics, states/statuses, etc.). The **U.Types** norms in this section are a **specialization**, not a restriction of scope.

**Purpose of this pattern.** Provide a **human‑legible, context‑anchored naming protocol** that:
* keeps *local meaning first* and prevents Cross‑context conflation;
* makes the **kind** of thing explicit (System, Episteme, Role, Service, Method, Work, Decision, Requirement, etc.);
* integrates smoothly with **Concept-Sets**, **`U.RoleDescription`**, and **Bridges** without requiring any special notation or tooling;
* supports lineage actions (mint, reuse, align, deprecate, split/merge) with a paper trail that managers can audit.

### F.18:2 - Problem

Without a shared naming protocol inside Part F, the same recurrent failures appear:

1. **Global‑name illusion.** A short label travels from one context to another and is *assumed* to mean the same SenseCell or Concept-Set row; later, contradictions appear during acceptance or assurance.
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

**Path Card (subset of Name Card).** A **Name Card** whose named FPF value is an **EvidenceGraph Path**: it cites a **PathId** (or **PathSliceId**), **Context**, **ReferencePlane**, **Γ_time**, and any **Bridge id(s) + CL/CL^plane** (with loss notes). Used by **G.6** and **G.10** to make justifications portable on UTS.

#### F.18:4.1 - The Eight R‑rules (normative)

**R1 — Speak every name *with its Context*.**
A name is **never** context‑free. When you introduce or use a name, **pair it with the Bounded Context** where it lives (the “Context of meaning”), and with the **edition** of that Context if relevant. In everyday speech: “X, *in* Y.” Cross‑context use requires a Bridge; labels alone do not travel.

**R2 — State the ontological *Kind* on the Card.**
Every Name Card **must** state the **Kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This prevents category errors and keeps Role–Method–Work alignment clean. *Clarification:* this is a **Card requirement**, not a demand that the label string begin with the Kind. The Kind field uses an accepted FPF kind or an explicitly marked extension candidate; the Name Card does not itself create a `U.Kind`, `RelationKind`, `GateProfile`, `EvidenceKind`, MVPK face kind, or Bridge.

**R3 — Declare the *Purpose / use‑domain* on the Card.**
In addition to **Kind**, the Name Card **must** state the intended **Purpose / use‑domain** that situates the concept in practice and signals **which families of contexts** are expected to use it (e.g., mathematical formalism, engineering practice, computer science, systems management). This enables reconstruction of usage from the lexicon and reduces unintended scope drift. *Clarification:* this is a **Card field**; it does **not** require the label string to carry the purpose qualifier.

**R4 — Resolve the name to a *Local‑Sense*.**
A minted name must resolve to a Local-Sense inside its Context (the result of F.2–F.3). If a name points to a Role Description, state that template and its sense basis. Avoid heavily overloaded label words: when needed, prefer concise two-word Tech labels that hint at the intended sense.

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
When a label changes, or two labels consolidate or split, record it on the Name Card as a lineage action (rename, merge, split, retire) with rationale and dates. Past uses *remain valid as historical facts*; continuity comes from lineage, not silent edits.

#### F.18:4.2 - The Six P‑practices (normative process)
**P1 — Candidate set (*NQD-front* of seed-words).**
Do **not** pick a label “in one shot”. Build a **small, non-dominated candidate set** (an *NQD-front*, typically 5–10 items) by seeding and varying along:
**Traditions** — mathematics, physics, engineering, computer science, systems thinking, management, etc. with their typical contexts and situations; use maximum diversity here;
 **Novelty/Familiarity** — from careful **reuse** of established terms to sharper **neologisms** from recent SoTA traditions;
 **Lexical form** — distinct **head terms** and morpheme families, readability/pronounceability, inflection/declension, transparency.
Use the **Novelty–Quality–Diversity** discipline from **Part G** to maintain only **non-dominated** candidates; when appropriate, you may implement this via **Γ_nqd.generate**. Record the **seeds** and the short rationale in the Card’s notes. Choose final **Unified Tech**/**Plain** labels **from this frontier**; if a high-quality candidate is discarded, briefly note why.

