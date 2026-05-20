An operations note says: “Staging is the same service as Production.” Months later, incident metrics are aggregated “because it is the same service”, and evidence across environments is mixed, producing an incorrect causal story.

**Show.**
Treat “same” as a red-flag umbrella token. Rewrite into an explicit cross-Context relation kind,
typed to the facet the draft actually uses (service delivery system sameness for actuals/evidence aggregation; not about promise contents).

**Show (candidate‑set note; endpoint facet restoration).**

```
CandidateSetNote(triggerSpan="service" in "same service", role=endpointFacet(p₁)):
- candidates: {promiseContent, serviceAccessPoint, serviceProviderPrincipal, serviceDeliverySystem}
- selected:   serviceDeliverySystem
- why:        the claim is later used to justify mixing operational actuals/evidence (metrics + incident logs);
  local cues point to delivery records/carriers (manifests/config/test runs), not clause carriers
- consequence: endpoints typecheck as `DeliverySystemRef` participants; clause/provider facets are explicitly out-of-scope

sameDeliverySystemUnder(
  leftDeliverySystemRef  = SystemRef(staging_delivery_system),
  rightDeliverySystemRef = SystemRef(prod_delivery_system),
  scope     = ClaimScope{SLO_family = X, signals = {latency, error_rate}},
  Γ_time    = interval[2025-12-01, 2026-01-31],
  viewpoint = OpsViewpoint,
  witnesses = {deploymentManifestPins, configPins, testRunPins}
)

aggregationAdmissibleIff(
  relationRef  = RelationRef(sameDeliverySystemUnder, SystemRef(staging_delivery_system), SystemRef(prod_delivery_system), ed=…),
  target       = deliveryWorkMetrics,                   // actuals
  Γ_time       = interval[2025-12-01, 2026-01-31],
  witnesses    = {metricCarrierPins, incidentLogPins}   // evidence carriers for the actuals
)
```

**Show.**
Now the relation is auditable: aggregation is admissible only if the relation kind’s admissibility
claims say it preserves the needed characteristics under the declared scope/time, and if witnesses exist.
Cross-Context reuse is explicit and cannot piggyback on label identity.


#### A.6.P:5.2 — Episteme archetype: “the models are synced”

**Tell.**
A draft says: “The simulation model is synced with the physical twin.” Reviewers ask what “synced” means. The authors respond with examples, but downstream users still cannot tell whether the claim is about parameters, structure, calibration, evidence freshness, or mapping quality.

**Show.**
Rewrite “synced” as an explicit correspondence relation kind + explicit qualifiers + witnesses:

```
entityMatchedBy(
  leftRef          = ModelRef(SimModel@ed=12),
  rightRef         = SystemRef(PhysicalTwin@ed=7),
  mappingArtifactRef = AlignmentModel_2025_11,
  scope            = ClaimScope{signals = S, metrics = M},
  Γ_time           = snapshot(t),
  referenceScheme  = RefScheme(CustomerIdRegistry#EU),
  viewpoint        = DataEngineeringViewpoint,
  witnesses        = {evalRunPins, calibrationPins, mappingArtifactPins}
)
```

**Show (change narration).**
Two weeks later, the mapping publication is replaced and the witness set is refreshed. In decision/publication lanes, represent this as a new edition and narrate the change via change classes (not via “re‑synced”):

```
withdrawRelation( relationRef = RelationRef(entityMatchedBy, leftRef, rightRef, ed=12) )

declareRelation(
  entityMatchedBy(
    leftRef           = ModelRef(SimModel@ed=12),
    rightRef          = SystemRef(PhysicalTwin@ed=7),
    mappingArtifactRef= AlignmentModel_2026_01,
    scope             = ClaimScope{signals = S, metrics = M},
    Γ_time           = snapshot(t₂),
    referenceScheme   = RefScheme(CustomerIdRegistry#EU),
    viewpoint         = DataEngineeringViewpoint,
    witnesses         = {evalRunPins_2026_01, calibrationPins_2026_01, mappingArtifactPins_2026_01}
  )
)
```

**Show.**
Different “sync meanings” become different **RelationKind tokens** (e.g., `entityMatchedBy`, `schemaAlignedUnder`), not adjectives. Subsequent changes become narratable as `retargetParticipant`, `rescope`, `retime`, or `refreshWitnesses`, rather than “we updated the sync”.

### A.6.P:6 — Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for RPR‑style precision restoration in the A.6 cluster.

* **Gov bias:** prefers explicit admissibility and evidence routing; increases auditability but raises authoring cost.
* **Arch bias:** favours reusable structural lenses (records/hyperedges) over narrative prose.
* **Onto/Epist bias:** pushes kind‑explicit relations and polarity discipline; discourages metaphor-first modeling.
* **Prag bias:** reduces rework and cross-team misinterpretation; may feel heavy in exploratory notes.
* **Did bias:** enforces teachable rewrite guides; can be perceived as prescriptive.

### A.6.P:7 — Conformance Checklist (CC‑A.6.P)

A pattern P conforms to A.6.P (i.e., is an RPR‑pattern) iff:

 > **Note.** This checklist defines conformance for **RPR specialisations** (e.g., A.6.5, A.6.6, A.6.8, A.6.9, A.6.C and future A.6.x patterns). A.6.P itself is the **suite recipe**.

1. **CC‑A.6.P‑1 — Lens is explicit.**
   P SHALL name the stable lens used to stabilise the ambiguity cluster and justify its fit.

2. **CC‑A.6.P‑2 — RelationKind is explicit and named through admissible mint-or-reuse.**
   Every in‑scope relation claim SHALL name an explicit RelationKind token, and that token SHALL resolve to a vocabulary entry whose relation specification skeleton publishes (at minimum): polarity (and explicit inverses if needed), participant SlotSpecs `⟨SlotKind, ValueKind, refMode⟩`, qualifier requirements, witness expectations for decision/publication lanes, admissible semantic change classes, and (when applicable) cross-Context or cross-plane policy (Bridge + CL + loss notes). Routed claims SHALL respect A.6.B.
   When a suitable token does not already exist, authors SHALL mint or document it through **F.18** rather than inventing a one-off label by intuition: **MintNew** is the default, the seed candidate set and NQD-front SHALL be shown, and the final token SHALL be selected from that non-dominated front unless an explicit legacy exception is recorded.
   The relation specification skeleton SHALL also declare admissible **repair paths for endpoint kind mismatches** (KindBridge / explicit narrowing / explicit retargeting) and enforce **qualifier placement discipline** (no adjective smuggling).

3. **CC‑A.6.P‑3 — Slot‑explicit instances.**
   P SHALL ensure that every in‑scope relation instance is expressible as a Qualified Relation Record filling all relation-specification-required participant slots (no hidden arity; see WF‑A6P‑QR‑1).

4. **CC‑A.6.P‑4 — Qualifiers are explicit when required.**
   If scope/time/viewpoint/reference-scheme assumptions matter (or the relation kind requires them), they SHALL be explicit; implicit “current/latest/in our context” SHALL NOT substitute.
   When witness freshness/decay matters, it SHALL be expressed explicitly (evidence-role timespans, qualification windows, explicit freshness predicates), not by treating `Γ_time` as a proxy.

5. **CC‑A.6.P‑5 — No silent polarity flips.**
   If inverse wording is used, it SHALL use explicit inverse tokens or polarity‑preserving forms; implicit role flips are forbidden.

6. **CC‑A.6.P‑6 — Change semantics use a change‑class lexicon.**
   Normative prose about relation evolution SHALL use named semantic change classes (declare/withdraw/retarget/revise/rescope/retime/refreshWitnesses/changeKind), not generic “update/modify/sync/bind/anchor”.
   Any mapping to more specific slot verbs MUST preserve the A.6.5 retarget vs by‑value edit distinction.

7. **CC‑A.6.P‑7 — “bind/binding” discipline.**
   `bind/rebind` SHALL be reserved for name binding (Identifier → SlotKind/slot‑instance) and SHALL NOT be used as a synonym for relation edits.

8. **CC‑A.6.P‑8 — Lexical firewall is normative.**
   P SHALL list red‑flag umbrella tokens for the family and provide rewrite rules; umbrella tokens SHALL NOT function as meaning‑surrogates in Tech/normative prose. If legacy/Plain umbrella wording appears, it SHALL be immediately mapped to an explicit Tech form (`relationKind(…)` or `--relationKind-->`).

9. **CC‑A.6.P‑9 — A.6.B atomicity, routing, and explicit references are respected.**
   Normative text SHALL be decomposed into atomic claims routable to exactly one quadrant (L/A/D/E). Dependencies SHALL be expressed by explicit references (IDs or canonical locations), not paraphrase. No‑upward‑dependency constraints SHALL be preserved.

10. **CC‑A.6.P‑10 — Evidence is carrier‑anchored (A.7 separation).**
    Statements about witnesses/evidence/freshness SHALL be framed as properties/expectations of carriers and work, not as properties of prose.

11. **CC‑A.6.P‑11 — A.6.S compatibility when engineered.**
    If the pattern family is presented as engineered/evolving, it SHALL be compatible with A.6.S: distinguish TargetSignature vs ConstructorSignature; map constructor verbs to A.6.5/A.6.6 canonical verbs; keep constructor ops effect‑free; and (when a ConstructorSignature is present) declare the C.2.1 slot read/write profile and whether ops are A.6.2/A.6.3/A.6.4 species.

12. **CC‑A.6.P‑12 — Cross-Context or cross-plane reuse is explicit (no “sameness by label”).**
    If a relation instance crosses Contexts/planes (or requires translation), the carrier SHALL cite Bridge ids + CL policy (and loss notes, when applicable). Label identity or “same anyway” prose SHALL NOT substitute.

13. **CC‑A.6.P‑13 — Disambiguation guide is actionable.**
    P SHALL include an explicit rewrite/selection guide that maps each red-flag umbrella cluster or generic load-bearing head phrase to candidate head kinds, candidate `RelationKind` tokens, and (when the ambiguity is endpoint-side) candidate endpoint facets/kinds, plus required qualifiers and canonical rewrite forms.
    The guide SHOULD follow the RPR‑Disambiguation format: **trigger → candidates → discriminating questions/tests → canonical rewrite → L/A/D/E L/A/D/E hooks**.

    Where endpoint referential compression is a primary risk, the guide SHOULD also include (or point to) the **Candidate‑Set Note** template (A.6.P:4.0b) so instance‑level reviews have an auditable trail: candidates → selected facet/kind → why.

14. **CC‑A.6.P‑14 — Grounding spans System and Episteme.**
    P SHALL include at least one Tell–Show–Show vignette in a **System** lane and at least one in an **Episteme** lane (per E.8), demonstrating a real ambiguity repair and a relation‑change narration using the change‑class lexicon.

15. **CC‑A.6.P‑15 — Trigger rule is explicit.**
    P SHALL include an explicit trigger rule (or selection heuristic) stating when the family applies and what counts as “in-scope” umbrella relational prose.

### A.6.P:7a - Portfolio, front, archive, and shortlist disambiguation

- Treat bare uses of `portfolio`, `front`, `archive`, `Pareto`, `shortlist`, `space`, `reachability`, and `stepping stone` as repair triggers whenever they carry live explanatory load.
- Use the helper declarations from A.0:QF.1a when repairing the sentence: do not let `SetSurfaceKind`, `SourceSurfaceKind`, `SourceSurfaceComposition`, `SubjectKind`, `DerivedViewKind`, `BasePaletteRef`, `SelectorOutcomeKind`, `HandoffKind`, `PromotionPolicy`, `RetentionIntent=steppingStone`, `EligibilitySet`, `DominanceSet`, `TieBreakerSet`, or `TelemetrySet` read as public set-outcome heads.
- The minimum repair is to state the `SubjectKind`, the declared comparison bundle, and, when selection or publication outcomes are involved, the declared `SelectorOutcomeKind`, the applicable `SetSurfaceKind` or `HandoffKind`, the declared `SourceSurfaceKind`, `SourceSurfaceComposition` when several sources are actually composed, `DerivedViewKind` or `BasePaletteRef` when a derived palette view matters, `LensId`, and which member of the shortlist family is meant.
- The declared comparison bundle is:
  - `EligibilitySet`
  - `DominanceSet`
  - `TieBreakerSet`
  - `TelemetrySet`
- If one front sentence depends on current `Q`, say whether the `DominanceSet` is the declared `Q` components or one promoted bundle under explicit policy.
- If one archive claim depends on coverage, stepping-stone retention, or reachability rather than current dominance, state that archive purpose explicitly instead of borrowing `Front` language.
- If one phrase uses `SoTA portfolio` before comparison or choice semantics exist, rewrite it as `TraditionPalette` only when the members are traditions; otherwise rewrite it as `Palette + SubjectKind`.
- If one phrase uses `Pareto archive` for the whole retained exploration outcome, rewrite it as `ExplorationArchive`.
- If one phrase uses `stepping-stone set` for the whole retained exploration outcome, rewrite it as `ExplorationArchive` and reserve `SteppingStoneSet` for one narrower retained subset when that narrower support requirement really matters.
- If one selected set is mentioned, name the shortlist-family stack explicitly:
  - `Shortlist` for the selected outcome
  - `RankedShortlist` for its ordered specialization
  - `ShortlistId` for the emitted identity or public token
  - `ChoiceSet` only when the mathematical set object itself is the point of the sentence
- If one phrase says `choice set` but the sentence is naming the public selected outcome, rewrite it as `Shortlist` and keep `choice set` only as one mathematical gloss when needed.
- If one phrase says `shortlist` and the output is explicitly ordered, rewrite it as `RankedShortlist` and keep it distinct from `Shortlist`.
- If one phrase says `shortlist` but really points at one emitted token or publication handle, rewrite it as `ShortlistId`.
- If one sentence moves between search-space and outcome-space talk, name the space whose objects are being compared before making claims about dominance, archive retention, or frontier expansion.
- If one sentence says `Pareto` but really means one post-lens selected result, rewrite it as `Shortlist` or `RankedShortlist` rather than widening `Front` until it means everything.
- Canonical rewrites for load-bearing Q-Front / NQD prose:
  - `portfolio by Q` -> `Front over the declared Q components` when the sentence is about non-domination.
  - `portfolio by NQD` -> `Front over the declared DominanceSet plus ExplorationArchive under the declared retention policy` when both current front and retained exploration outcome are meant.
  - `Pareto shortlist` -> `Shortlist from <SourceSurfaceKind> under <LensId>` when the sentence is about publication or selection.
  - `Pareto archive` -> `ExplorationArchive under <RetentionPolicy>` when the sentence is about retained exploration rather than current non-domination.
  - `space of traditions/methods/hypotheses` -> `Palette + SubjectKind` first; add `TraditionPalette` only for `SubjectKind=Tradition`.
- Discriminating tests:
  - If the sentence answers "what counts as current non-domination?", repair toward `Front` / `Q-Front` plus `DominanceSet`.
  - If the sentence answers "what remains worth retaining for reach, coverage, or later probing?", repair toward `Archive`, `ExplorationArchive`, or `RetentionIntent=steppingStone`.
  - If the sentence answers "what selected set was emitted for downstream use?", repair toward `Shortlist`, `RankedShortlist`, and optional `ShortlistId`.
  - If the sentence answers "which goal, capability, or learning frontier might widen next?", repair toward `GoalSpaceExpansionCue`, `LearningProgressSignal`, or `CompetenceModelRef`, and keep those outside default dominance unless one policy promotes them.

### A.6.P:8 — Common Anti‑Patterns and How to Avoid Them


| Anti-pattern | Why it fails | Repair |
| ---------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| “Just define the umbrella word” | Definitions do not separate arity, operation classes, or viewpoint asymmetry. | Replace umbrella use with explicit RelationKind + qualified record + change lexicon. |
| Keep the umbrella verb, add adjectives | Adjectives are not relation specifications; invariants remain unstated. | Mint/select distinct RelationKind tokens; enforce rewrite discipline. |
| Leave a load-bearing generic head uninterpreted | Readers cannot tell what kind of thing the phrase governs, so later qualifiers float without an ontology. | Restore the head kind first in source-local terms; only then repair the remaining relation/comparison load. |
| Let a qualifier smuggle the real load | A phrase like “comparative note”, “safe guidance”, or “reliable output” sounds precise while leaving the actual relation, comparison basis, or authority-reference requirement implicit. | Unpack the qualifier into explicit comparison basis, relation kind, admissibility condition, or L/A/D/E-classified claim before any claim requiring explicit relation, admissibility, or authority-reference support, or before reliance. |
| Leave pronominal/metonymic endpoints implicit | Endpoint identity/facet remains guesswork; slot typing cannot stabilise. | Reconstruct candidate referents/facets (**capture as a Candidate‑Set Note**); add explicit slots/refs; then rewrite (A.6.8 is the archetype for “service” polysemy). |
| Ontology only, no lexical guardrails | Prose re-collapses meaning. | Add red-flag tokens + prohibited umbrella use in Tech/normative prose. |
| Lexicon only, no structural lens | Becomes subjective policing. | Introduce stable lens + slot schema; then attach guardrails. |
| Solve viewpoint mismatch by renaming endpoints | Silent re-typing breaks cross-pattern reuse. | Keep roles stable; use explicit kind selection + explicit repair paths. |
| Using “bind” to mean “edit relation” | Collapses name-binding vs slot-writing classes. | Reserve `bind/rebind` for names; use change lexicon / slot verbs properly. |
| Implicit “current/latest” | Violates explicit time discipline. | Add explicit `Γ_time` where time matters. |
| Treat `Γ_time` as witness freshness | Time selection does not equal evidence freshness/decay; this conflates time discipline with evidence lanes. | Keep `Γ_time` for temporal scope; express freshness/decay via witness metadata and carrier-anchored E-claims. |
| Collapse search-space refs, support views, and publication forms into one `space` or `view` | Search-space refs, outcome-space refs, support views, and source surfaces and set surfaces become indistinguishable, so later claims lose their governed object. | Restore the declared `CharacteristicSpace`, any `SearchSpaceRef` and `OutcomeSpaceRef`, the active source surface or active set surface, the support view or atlas view if any, and any `OutcomeMapRef` or `BridgeDistortionNote` before making the claim. |
| Compare across mixed kinds | `PublicationUnit`, project record, process, authority-use claim, or source-support claim gets ranked on one comparison basis before its kind and support requirement are restored. | First restore head kind, then qualifier load, then rewrite the sentence through exact support requirement, threshold, handoff condition, or source-support claim wording so the comparison basis is homogeneous. |

**Worked repair slice — NQD/OEE space/view/publication stack.**

Draft: “The archive projects into the outcome space through the atlas view.”

Repair sequence:

* `TraditionArchive` = derived retention view over one declared palette.
* `OutcomeSpaceRef` = guarded role reference to the declared `CharacteristicSpace` used for outcome-side judgment.
* `TraditionAtlasView` = optional neighboring support view, not the default meaning of the archive.
* `OutcomeMapRef` = explicit support reference if the passage must show how the archive maps into one outcome or effect surface.

Canonical rewrite:

* Keep `TraditionArchive` as the source surface for the set publication.
* Cite `OutcomeSpaceRef` only when the claim is about outcome-side evaluation against the declared `CharacteristicSpace`.
* Cite `OutcomeMapRef` only when the source-to-outcome mapping itself matters.
* Use `TraditionAtlasView` only if several declared views or qualifiers must stay visible together; otherwise leave the passage at archive/palette-first precision.

### A.6.P:9 — Consequences


**Benefits**

* **Predictable precision upgrades.** Umbrella relational prose becomes systematically expandable into explicit structure.
* **Viewpoint conflict becomes repairable.** Differences are shown as explicit roles/kinds/qualifiers, not silent rewrites.
* **Change becomes speakable.** “What changed?” is a named semantic change class, reducing folklore.
* **Cross‑Context safety improves.** “Same/synced/linked” becomes boundary-bearing relation specification and auditable, not rhetorical.

**Trade‑offs / mitigations**

* **Higher authoring overhead.** Mitigated by progressive elaboration: expand only when invariants, reuse, or decisions require it.
* **More explicit qualifiers.** Mitigated by keeping the lens stable and reusing slot templates (A.6.5/A.6.6).
* **Perceived prescriptiveness.** Mitigated by allowing Plain-register glosses that are immediately mapped to Tech tokens (without creating new relation specifications).

### A.6.P:10 — Rationale

Upper/foundational ontologies optimise for broad applicability via sparse commitments. FPF’s recurring, high-cost failures are often elsewhere: **under‑specified relations** in prose, where ambiguity hides in arity, kind selection, viewpoint, and change semantics.

A.6.P is orthogonal to “add a global taxonomy”:

* It provides a repeatable method to **restore relational precision** without requiring any external formalism or auxiliary authoring apparatus.
* It operationalises A.6’s boundary discipline by ensuring relation talk can be cleanly separated into signature invariants, admissibility, deontics, and evidence/work (A.6.B), rather than becoming one undifferentiated boundary claim.

### A.6.P:11 — SoTA‑Echoing (informative; post‑2015 alignment)

**Evidence binding note.** If your Context maintains a SoTA Synthesis Pack for relation-specification authoring or “qualified relations”, cite it here and keep this section consistent. Otherwise, treat the table below as a seed list (informative only).

A.6.P echoes contemporary practice across independent traditions, while remaining notation‑neutral and Context-local:

| SoTA practice (post‑2015) | Primary source (post‑2015) | Echo | What A.6.P adds | Adoption stance |
| --- | --- | --- | --- | --- |
| Constraint/shape validation over graph assertions | W3C **SHACL** Recommendation (2017) | Separates “assertions” from “constraints” | Couples structural specifications with **lexical guardrails** to prevent prose regression | **Adopt/Adapt** — adopt explicit structural specifications, adapt by binding to Tech↔Plain and rewrite discipline |
| Qualified statements / reification patterns | **RDF‑star / SPARQL‑star** (2017+) practice family | Reification/qualification when hidden arity appears | Requires explicit **RelationKind** + change‑class lexicon (not just representational qualification) | **Adapt** — representation is not enough without kind selection + change semantics |
| Architecture views & correspondences | ISO/IEC/IEEE **42010:2022** | Viewpoints and correspondences as first-class concerns | Forces viewpoint discipline inside relation qualification + prohibits silent polarity flips | **Adopt/Adapt** — adopt viewpoint accountability, adapt by embedding it into relation records |
| Bidirectional transformations / optics | Pickering et al., **Profunctor Optics** (ICFP 2017) and successors | “Pairs of projections + invariants” as stable lenses | Uses optics as conceptual stabilisers for multi‑view relations while keeping Core notation‑neutral | **Adapt** — use as a stabilising lens, not as mandated notation |
| Compositional modelling (applied category theory) | Fong & Spivak, **Seven Sketches in Compositionality** (2019) | Stable abstract lenses reusable across domains | Embeds lens choice into an authoring discipline with explicit slots + guardrails | **Adapt** — keep the categorical lens didactic; operationalise via SlotSpecs + change lexicon |

These echoes justify why A.6.P is structured as: **stable lens → explicit slots → explicit change classes → lexical guardrails**, rather than “just define the verb”.

### A.6.P:12 — Relations

**Specialised by**

* **A.6.5 `U.RelationSlotDiscipline`** — slot precision restoration for n‑ary relations.
* **A.6.6 `U.BaseDeclarationDiscipline`** — base‑dependence precision restoration (SWBD + base‑change lexicon + `anchor*` red‑flags).
* **A.6.8 (RPR‑SERV)** — service polysemy unpacking as a relation/facet precision restoration discipline (serviceSituation lens + canonical rewrites + service‑specific tests and change narration).
* **A.6.9 (RPR‑XCTX)** - U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align / map” via explicit Bridges
* **A.6.H (RPR‑WHOLE)** — wholeness language unpacking (“whole/part/integrity/complete”) into boundary, typed parthood, explicit Γ selection, order/time routing, and A.15 completeness/coverage claims.

**Coordinates with**

* **A.6.S `U.SignatureEngineeringPair`** — RPR rewrite operations can be packaged as a ConstructorSignature for engineered relation families; must preserve canonical verb mapping and effect‑free constructor semantics.
* **A.19 `U.CharacteristicSpace` + `A.19.SUPPORT-VIEW`** — for declared characteristic spaces, guarded role references, and support-view and atlas-view discipline when one relation repair needs those layers explicit.
* **G.2** — for palette, front, archive, or tradition-atlas specialization when the repaired passage is SoTA-harvest or synthesis prose.
* **F.18** — when the remaining issue is naming-side choice among candidate labels rather than relation typing or publication-lane repair.
* **C.2.2a, A.16, A.16.1, A.16.2, B.4.1, and B.5.2.0 + C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** - relation publication enters only after admissible language-state chart positioning, articulation, and closure support exist; earlier cue-pack material stays on the language-state seam, prompt-shaped continuations stay with `B.5.2.0`, retreat/reopen moves remain governed by `A.16.2`, and `A.16.0` is used only when lineage, branch, loss, or handoff history must itself be published.

**Intended future A.6.x specialisations (illustrative)**

* Cross‑Context equivalence / “sameness” discipline (Bridge + loss notes families)
* Correspondence/consistency + repair discipline (sync/alignment families)
* Transfer/hand‑off discipline (multi‑party “give/assign/accountability” families)

### A.6.P:12a - Quantum-like relation/probe wording precision note

Treat quantum-like load-bearing wording such as `coupled`, `interaction`, `probe`, `measurement`, `export`, `collapse-like`, `field-like`, `state update`, or `non-copyable` as ordinary RPR triggers when they carry live explanatory load. These words are not reusable FPF relation predicates merely because they appear in a quantum-like source or example.

Action path:

1. Mark the exact trigger span in the draft.
2. Restore the head kind first: is the phrase naming a boundary interaction, bridge/export, evidence carrier, measure, work act, viability move, decision comparison, or representation shortcut?
3. Build a small candidate set for the relation kind and endpoint facets.
4. Select the relation kind or hand off to an existing governing pattern.
5. Fill slots: participants, polarity, channel/mediator, time window, witness, and change class.
6. Rewrite the sentence into explicit local prose or a relation form only after the ontology is clear.
7. Move to `C.26` only when ordinary relation repair still leaves order-sensitive, probe-frame-sensitive, incompatible-probe, no faithful-enough export, or state-representation coarsening support load.

Minimum repair for load-bearing quantum-like relation wording:

| Relation slot | Required recovery |
| --- | --- |
| Participants | Which endpoints, carriers, contexts, roles, views, or systems participate |
| Relation kind | Whether the prose means bridge/export, evidence, measurement, work enactment, boundary interaction, viability regulation, or local decision comparison |
| Direction / polarity | Whether the relation is one-way, mutual, symmetric, asymmetric, reversible, lossy, or only observer-relative |
| Channel / mediator | Message, API read, workshop, metric, dashboard, carrier, bridge, instrument, or other interaction medium |
| Time / window | `Γ_time`, persistence, decay, refresh, or reprobe condition when state reading depends on time |
| Witness | Evidence carrier or observation that makes the relation readable |
| Change class | Whether the relation is a retarget, rescope, reframe, update, export-loss, state-reading change, or ordinary relation refinement |

Useful outputs:

- an ordinary `F.9`, `A.6.8`, `A.6.9`, `C.16`, `A.15`, or `C.25` receiving pattern when the repaired slots reduce to one existing support load;
- a local explanatory phrase when no reusable relation token is justified;
- an `A.6.P` repair plus `F.18` naming pass when a reusable relation token is actually needed;
- a `C.26` handoff only for the remaining state, probe, export, frame, or coarsening support load.
### A.6.P:12b - C.29 MLA relation

> **MLA relation.** `A.6.P` may select a stable mathematical substrate for relation precision restoration: arity, polarity, endpoint discipline, slot structure, and relation-kind repair. This does not by itself apply `C.29`. `C.29 Mathematical Lens Adequacy` applies only when that substrate is used as a load-bearing mathematical representation of a target phenomenon beyond relation repair. `A.6.P` does not by itself license source-domain ontology transfer.

### A.6.P:End
## A.6.Q - `U.QualityTermPrecisionRestoration` — Quality Term Precision Restoration (Q-TERM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Quality-term precision restoration.

**Intent.**
Provide a reusable discipline for repairing overloaded uses of the word **quality** in FPF texts.
This pattern is an **A.6.P RPR specialisation**: it rewrites bare evaluative prose as either an explicit endpoint-pattern-governed evaluative form or, when endpoint selection is still being stabilized, one explicit, slot-explicit **quality ascription** transitional relation family with a declared **sense family**, admissible **normal form** (`SignalPack | Characteristic | Bundle | Objective`), explicit **change semantics**, explicit **reference-plane accountability**, and lexical guardrails.
It allows philosophical, neuro-symbolic, control-theoretic, engineering, and open-ended-search uses to coexist **without false identity by label**.

**Placement.**
Part A > cluster **A.6 Signature Stack & Boundary Discipline** > specialisation of **A.6.P** for overloaded broad evaluative terms centered on *quality*.

**Builds on.**
A.6, A.6.B, A.6.P, A.6.S, A.6.0, A.6.5, A.7, A.2.6, A.17, A.18, C.2.1, C.16, C.25, C.17–C.19, E.8, E.10, F.9, F.18.

**Coordinates with.**
**A.6.A** for action-invitation exits; **C.2.2a**, **A.16**, **A.16.1**, **A.16.2**, and **B.4.1** for language-state chart positions, admissible moves, early cue handling, responsibility handoff, and admissible retreat when an evaluative publication must be reopened; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account; **B.5.2.0** when the admissible continuation is still an open explanatory probe rather than a stable endpoint ascription; **C.2.LS**, **C.2.4**, **C.2.5**, **C.2.6**, and **C.2.7** for articulation, closure, anchoring, and representation-factor facets referenced but not governed here; **E.17.0**, **E.17**, and **E.18** for viewpoint publication; **A.10** and **B.3** for evidence and assurance; **A.19.CN** for comparability governance; **F.9.1** for bridge-stance annotations; **C.3.3** for explicit kind-bridge repair when endpoint kind mismatches appear.

**Non-goal.**
This pattern does **not** assert that phenomenal character / qualia, phenomenological preconceptual fit, Pirsig-style dynamic/static quality, latent fit in learned representations, explanatory merit, engineering `-ilities`, QD/NQD selector value, and control adequacy are one concept.
Its job is to publish a disciplined **bridge reading** across those traditions while preventing false identity by shared label.
It also does **not** assert that every trigger use of “quality” is admissibly repaired by `evaluativeAscription(...)`: where the repaired statement is primarily about an **action invitation** under `A.6.A` rather than an evaluative ascription, or is primarily about a **requirement or commitment over explicit heads** (for example, *quality requirements* over named Characteristics, Q-Bundle heads, or objective heads), the admissible move may be `changeRelationKind(...)` into a different relation family.

### A.6.Q:1 - Problem frame

FPF repeatedly encounters a predictable precision failure mode around the token **quality**:

authors say:

* “this design has quality”
* “the model quality improved”
* “quality matters before formalisation”
* “quality characteristics”
* “quality in QD / NQD”
* “the world model is higher quality”
* “the explanation is high-quality”

…but the intended meaning is actually one of several different **evaluative families**, for example:

1. **Phenomenal character / qualia** when the experienced quality itself is the topic of description rather than an externally measured characteristic.
2. **Preconceptual fit / felt rightness** before stable object-characterisation.
3. **Latent / distributed fit signals** in learned representations, world models, or active inference loops.
4. **Explanatory merit** of a theory, problem frame, or conjecture.
5. **Architectural-description fitness / compression merit** of an architecture description or architecture model under a declared viewpoint.
6. **Engineering quality families** such as reliability, maintainability, security, evolvability.
7. **Usefulness / selection value** in open-ended search, novelty–quality–diversity, or portfolio selection.
8. **Control adequacy** of a policy/model/controller in a closed loop.

The failure modes are recurrent:

* **Sense elision.** One broad evaluative noun hides several non-equivalent evaluative kinds.
* **Carrier confusion.** The bearer of the evaluation is unclear: record/carrier, episode, model, policy, explanation, candidate, architecture, relation, or action loop.
* **Form confusion.** A non-metric signal is rewritten as a metric; a bundle is treated as one scalar; an objective is mistaken for a characteristic.
* **Substrate confusion.** Embodied/preconceptual, latent/distributed, and symbolic/local representations are silently collapsed.
* **Plane confusion.** Quality of the described entity, quality of the description, quality of the carrier, and quality of the publication face are silently collapsed across `ReferencePlane` / A.7 lanes.
* **Bridge illusion.** Similar wording across traditions is mistaken for sameness.
* **Illegal scalarisation.** Composite engineering families or explanatory merit are compressed into one number without an admissible scoring method.
* **Viewpoint conflict.** One stakeholder means architectural attributes, another means usefulness, another means preconceptual fit.

### A.6.Q:2 - Problem

How can FPF let authors use the communicative convenience of the word **quality** while preventing category errors when the term crosses:

* phenomenological / epistemological discourse,
* architecture-description fitness discourse and viewpoint-fit discourse,
* representation-learning / neuro-symbolic discourse,
* Popper/Deutsch-style explanation-and-criticism discourse,
* engineering architecture and quality-characteristic discourse,
* open-ended evolution / NQD / selection discourse,
* control / world-model / active-inference discourse,
* ecological affordance discourse, including cases that must exit this relation family altogether?

### A.6.Q:3 - Forces

* **Breadth vs precision.** “Quality” is attractive because it is broad; that same breadth makes it unsafe at boundaries.
* **Preconceptuality vs auditability.** Some uses refer to something real but not yet stably characterised.
* **Distributed substrate vs local publication.** Some evaluative signals arise in distributed or embodied substrates but must later be published in explicit local forms.
* **Comparability vs non-reduction.** Engineering and selection settings need comparability, but not every evaluative signal is an admissible metric.
* **Cross-tradition dialogue vs false unification.** The framework should support parallels without asserting identity.
* **Progressive articulation.** A term may begin as a felt signal and later become a bundle, proxy set, or objective.

### A.6.Q:4 - Solution

**Stable lens > Sense Family > Slots > Normal Form > Change Lexicon > Guardrails**

#### A.6.Q:4.0 - Trigger rule

A use of **quality** is in scope for A.6.Q when any of the following holds:

* the token **quality** or **high-quality / low-quality** appears in Tech or normative prose;
* a boundary statement relies on “quality” for admission, selection, explanation, comparison, assurance, or requirement-setting;
* different traditions are compared using the same word *quality*;
* a draft introduces *quality metric*, *quality score*, *quality characteristic*, *quality requirement*, *model quality*, *architecture quality*, *solution quality*, or *quality in QD* without a declared sense;
* the author intends the word to carry more than one of: evaluative fit, measurable characteristic, bundle, utility, or optimization objective.

#### A.6.Q:4.0a - Operational repair sequence

When the trigger fires, authors SHOULD follow the A.6.P operational repair path:

1. **Capture the trigger span.**
   Copy the exact trigger phrase using *quality* (or a red-flag derivative such as *high-quality*, *quality metric*, *quality characteristic*, *model quality*).

2. **Reconstruct the candidate set.**
   Enumerate plausible candidate senses and, when relevant, candidate endpoint governing FPF patterns or `authoritySourceRef` targets plus bearer lanes/facets (A.7: `Object | Description | Carrier`).
   If the occurrence is decision-bearing or publication-bearing, record this as a short **Candidate-Set Note** before selecting a repair.

   **Collision note.**
   This **Candidate-Set Note** is a local RPR disambiguation record for `quality` repairs; it is **not** the F.18 naming-process candidate set.

2a. **Check for an out-of-family affordance reading.**
   If the occurrence is primarily about an **action invitation** rather than an evaluative ascription, do **not** force a `QualitySense`.
   Classify it with `changeRelationKind(...)` into the appropriate relation family and treat the quality token as token-under-discussion only.

3. **Select one explicit quality sense.**
   Pick one `QualitySense` token and state why rival senses were rejected in this local context.

4. **Emit an endpoint-explicit or transitional rewrite.**
   Rewrite the sentence either into one explicit endpoint-pattern-governed evaluative form (`Characteristic | Q-Bundle | Objective | ExplanatoryMeritBundle | selector-value endpoint`) or, when endpoint choice is still being stabilized, into one explicit `evaluativeAscription(...)` transitional record with bearer, frame, evaluator/viewpoint, normal form, and explicit qualifiers.
5. **Classify boundary-bearing consequences.**
   If the repaired statement is used for admissibility, commitments, publication, or evidence-bearing decisions, classify the resulting `L/A/D/E` hooks with A.6.B instead of letting “quality” carry the required support by itself.

#### A.6.Q:4.1 - Transitional lens: evaluative classification anchored by `evaluativeAscription(...)`

A.6.Q stabilises the ambiguity cluster by treating every in-scope quality statement as **explicit evaluative content that must name the endpoint governing pattern or publication with named authority-reference relation that carries it**, not as a bare adjective.
`evaluativeAscription(...)` remains the canonical **transitional/metalinguistic repair record** when the endpoint choice is not yet fixed, but it is not the universal resting place.
Entry into A.6.Q therefore presupposes enough local `AE` to name the bearer, the frame, and at least one candidate evaluative family explicitly. `CD` may remain low while `evaluativeAscription(...)` is still serving as a transitional record, but if the content is still only a cue pack, a routed cue, or an open explanatory probe, it SHOULD remain in `A.16.1` / `B.4.1` / `B.5.2.0` rather than being published here prematurely. If a previously published evaluative record later loses the support needed to keep even that transitional status live, retreat via `A.16.2`.
In A.6.P terms, this pattern fixes one classification discipline plus one canonical transitional relation family:

* **`evaluativeAscription`** — the explicit transitional relation kind for “X has quality / quality improved / high-quality / quality in QD / quality characteristic / model quality” rewrites while preparing handoff to a more specific endpoint governing pattern or publication with named authority-reference relation.
#### A.6.Q:4.1a - RelationKind specification skeleton for `evaluativeAscription`

The family-specific `RelationKind` token is **`evaluativeAscription`**.
Its relation specification publication SHALL declare, at minimum:

* **(L)** applicability of the token in the local Context or plane set;
* **(L)** bearer-centred polarity (the bearer is the evaluated participant; inverse prose SHALL NOT silently swap bearer and evaluator);
* **(L)** participant SlotSpecs for bearer, sense, evaluation-frame, evaluator, and normal-form positions;
* **(A)** repair paths for bearer-kind mismatches: explicit narrowing, `KindBridge`, and/or explicit `retargetBearer(...)`;
* **(L)** qualifier expectations for `scope`, `Γ_time`, `viewpoint`, `view`, `referencePlane`, `refScheme`, `reprScheme`, `representationSubstrate`, and `bridgeRef`;
* **(D)** qualifier-placement discipline: frame/scope/time MUST NOT be smuggled into adjectives such as *high-quality*;
* **(A/E)** witness discipline for decision/publication lanes;
* **(L/A)** admissible semantic change classes and their edition-fence expectations;
* **(A/E)** cross-context and cross-plane policy when actual reuse is claimed (Bridge id + CL/loss-note policy).

Each in-scope occurrence SHALL be representable as a pattern-specific **QualifiedRelationRecord**:

```text
evaluativeAscriptionRecord :=
⟨
  relationKind            : evaluativeAscription,
  bearerTuple             : …,
  qualitySense            : QualitySense,
  evaluationFrame         : …,
  evaluator?              : …,
  viewpoint?              : U.Viewpoint,
  view?                   : U.View,
  referencePlane?         : ReferencePlane,
  refScheme?              : U.ReferenceScheme,
  reprScheme?             : U.RepresentationScheme,
  normalForm              : SignalPack | Characteristic | Bundle | Objective,
  scope?                  : U.Scope,
  Γ_time?                 : U.GammaTimePolicy,
  representationSubstrate?: embodied-kinesthetic | latent-distributed | symbolic-local | hybrid,
  bridgeRef?              : BridgeId,
  witnesses?              : EvidenceRefSet
⟩
```

So the sentence “X has quality” is never accepted as a terminal form.
It must be rewritten either into an explicit endpoint-pattern-governed evaluative form or into an explicit `evaluativeAscription(...)` transitional record with a declared endpoint governing pattern or publication with named authority-reference relation.

**Discipline note.**
`QualitySense` is a **slot value inside** the transitional relation family; it is not a replacement for the endpoint governing FPF pattern or `authoritySourceRef` target.
The stable intermediate lens is the ascription relation; the sense token refines **what kind of evaluative ascription** is being made while the endpoint target remains explicit.

**Separation note.**
`evaluator` and `viewpoint` are not synonyms.
When both matter, they SHALL be published separately: the evaluator is the observing / criticising / selecting party or policy, while the viewpoint is the declared `U.Viewpoint` under which the ascription is presented.
#### A.6.Q:4.1b - Polarity discipline (bearer-centred; no silent inverse)

`evaluativeAscription` is bearer-centred.
Tech / normative prose SHALL keep the evaluated participant in the bearer position and SHALL publish evaluator/viewpoint separately.

* “Architects rate the system highly” rewrites to `evaluativeAscription(bearer=System, evaluator=ArchitectureReviewBoard, …)`.
* “The benchmark says model quality is high” rewrites to `evaluativeAscription(bearer=Model, evaluator=BenchmarkPolicy, …)`.

There is no inverse token that silently makes the evaluator the bearer.
If inverse wording is used in Plain prose, authors SHALL rewrite it into the bearer-centred form (or mint an explicit inverse RelationKind token and publish its polarity specification).

#### A.6.Q:4.1c - Endpoint-first discipline

When the admissible endpoint governing FPF pattern or `authoritySourceRef` target is already known, authors SHOULD publish the endpoint-pattern-governed evaluative form directly and use `evaluativeAscription(...)` only when preserving the transitional ambiguity is itself informative. `evaluativeAscription(...)` is therefore a classification record, not a shadow endpoint source.

Typical direct endpoints are:

* engineering `-ility` heads published as one `Characteristic` or one `Q-Bundle`,
* selector-context uses published as an `Objective` headed by `QS.UseValue` unless overridden explicitly,
* architecture-description uses published under the description-side evaluative head already selected by the viewpoint bundle,
* explanatory-merit uses published under the explicit merit bundle when that bundle head is already known.

#### A.6.Q:4.2 - Core construct: `QualitySense`

Every in-scope use SHALL resolve to an explicit **`QualitySense` token**.

A `QualitySense` token publishes at least:

```text
QualitySense :=
  ⟨
    senseId,
    bearerArity,
    articulationMode,
    representationSubstrate,
    defaultNormalForm,
    admissibleNormalForms,
    evaluationFrameKind,
    admissibleEvidenceModes,
    admissibleChangeClasses,
    bridgePolicy
  ⟩
```

Where:

* **`articulationMode`** ∈
  `{ preconceptual, exemplar-grounded, proxy-grounded, characteristic-bound, bundle-bound, objective-bound }`
* **`representationSubstrate`** ∈
  `{ embodied-kinesthetic, latent-distributed, symbolic-local, hybrid }`
* **`defaultNormalForm`** ∈
  `{ SignalPack, Characteristic, Bundle, Objective }`
* **`admissibleNormalForms`** is the explicitly declared set of admissible publication forms for the sense.
  `defaultNormalForm` names the primary publication form; any additional forms MUST be declared here rather than inferred ad hoc.

#### A.6.Q:4.3 - Normative starter set of sense families

A Context MAY add local senses, but the following starter set is normative as the initial disambiguation menu:

| `QualitySense` token               | Use when “quality” means…                                                                                      | Default normal form | Typical substrate                | Must **not** be silently collapsed into                                    |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------: | -------------------------------- | -------------------------------------------------------------------------- |
| `QS.PreconceptualFit`              | preconceptual fit, felt rightness, “quality before definition”, kinesthetic/embodied salience                |         `SignalPack` | `embodied-kinesthetic` or `hybrid` | Characteristic, utility, fitness score                                     |
| `QS.PhenomenalCharacter`           | phenomenal character / qualia / felt characteristic when the experienced quality itself is described          |         `SignalPack` | `embodied-kinesthetic` or `hybrid` | `QS.PreconceptualFit`, engineering quality, utility                        |
| `QS.LatentFit`                     | distributed fit/tension in learned representations, world models, probes, prediction structures              |         `SignalPack` | `latent-distributed` or `hybrid` | `QS.PreconceptualFit`, engineering quality, explanatory merit              |
| `QS.ExplanatoryMerit`              | epistemic merit of an explanation, conjecture, problem frame, or theory                                      |             `Bundle` | `symbolic-local` or `hybrid`     | engineering `-ilities`, use-value                                          |
| `QS.ArchitecturalDescriptionFitness` | task-fit / compression merit of an architecture description, architecture model, or viewpoint bundle as a description of structure for downstream reasoning |             `Bundle` | `symbolic-local` or `hybrid`     | `QS.EngineeringQualityFamily`, `QS.ExplanatoryMerit`, publication polish   |
| `QS.EngineeringQualityFamily`      | reliability/availability/security/maintainability/evolvability/usability/etc.                                |             `Bundle` | `symbolic-local` or `hybrid`     | function/capability statements, preconceptual fit                          |
| `QS.UseValue`                      | usefulness of a candidate under a declared goal/CG-frame; the “Q” head in NQD/QD by default                  |          `Objective` | `symbolic-local` or `hybrid`     | engineering quality family, explanatory merit                              |
| `QS.ControlAdequacy`               | adequacy of a policy/model/controller in a closed action loop                                                |             `Bundle` | `hybrid`                         | bare model “quality”, felt fit                                             |

**Default-form note.**
`QS.EngineeringQualityFamily` and `QS.ControlAdequacy` default to `Bundle`.
A local Context MAY operationalize one explicit head as a `Characteristic`, but that is a declared operationalization, not a second default normal form.

**Normative rewrite note.**

* In **NQD / QD / selector** contexts, bare *quality* SHALL rewrite to **`QS.UseValue`** unless a different `QualitySense` is explicitly declared.
* In **engineering** contexts, bare *quality* SHALL rewrite either to:

  * one explicit **`U.Characteristic` + CSLC Scale**, or
  * one explicit **`Bundle`**, preferably authored as a **`Q-Bundle`** when composite.
* In **phenomenological** contexts, bare *quality* SHALL rewrite to **`QS.PhenomenalCharacter`** when the experienced quality itself is the topic of description, and to **`QS.PreconceptualFit`** when the talk is about preconceptual fit / felt rightness before stable characterisation.
* In **representation-learning / world-model** contexts, bare *model quality* SHALL rewrite to **`QS.LatentFit`** and/or **`QS.ControlAdequacy`**, with the distinction made explicit.
* In **epistemic evaluation** contexts, “good explanation” SHALL rewrite to **`QS.ExplanatoryMerit`**.
* In **architecture-description fitness or viewpoint** contexts, bare *architecture quality* or *architectural quality* SHALL first disambiguate the bearer lane: if the bearer is the described system, use **`QS.EngineeringQualityFamily`**; if the bearer is the description or episteme, use **`QS.ArchitecturalDescriptionFitness`**.

#### A.6.Q:4.4 - Required slots for a conforming `evaluativeAscription`

A conforming `evaluativeAscription` SHALL make explicit:

1. **Bearer tuple.**
   What is being evaluated, with arity explicit.

2. **`QualitySense`.**
   Which evaluative family is intended.

3. **Evaluation frame.**
   The criterion-basis under which the ascription is made.
   Examples: exemplar pack, probe pack, criticism/test pack, Q-bundle definition, CG-frame, acceptance spec, control horizon.

4. **Evaluator or viewpoint.**
   State the evaluator (observer, critic, selector policy, stakeholder family, or review body) and, when relevant, the `U.Viewpoint`, separately.
   The two SHALL NOT be silently collapsed when they differ.

5. **Normal form.**
   Whether the ascription is published as `SignalPack`, `Characteristic`, `Bundle`, or `Objective`.

6. **Scope and time when relevant.**
   The relevant USM scope (`U.ClaimScope`, `U.WorkScope`, `U.PublicationScope`, or generic `U.Scope`) and `Γ_time` SHALL be explicit when omission changes meaning.
   Freshness windows, qualification windows, or evidence decay windows SHALL be declared in the appropriate evidence or capability lane rather than smuggled into “quality” as an adjective.

7. **Reference plane when relevant.**
   Especially when the same trigger phrase can refer to the described entity, its description, its carrier, or a publication face under a different `ReferencePlane`.

8. **Reference / representation scheme when relevant.**
   Especially when the ascription depends on a declared reference scheme, representation scheme, or viewpoint-specific decoding convention.

9. **Representation substrate when relevant.**
   Especially when discussing parallels between preconceptual, latent-distributed, and symbolic-local treatments.

10. **Witness / evidence mode.**
   Exemplars, probes, measurements, bundle members, tests, traces, or closed-loop performance carriers.

#### A.6.Q:4.5 - Normal-form discipline

A `QualitySense` SHALL declare one admissible **default** normal form and MAY declare additional admissible normal forms explicitly.

**QNF-1 — `SignalPack`.**
Use for `QS.PhenomenalCharacter`, `QS.PreconceptualFit`, and many cases of `QS.LatentFit`.

A conforming `SignalPack` publishes:

* exemplar/contrast set or probe set,
* articulation notes,
* source episode, carrier, and observer,
* optional ordinal or thresholded summaries,
* explicit warning that the signal is **not** yet a `Characteristic` unless an admissible proxy is later declared.

**QNF-2 — `Characteristic`.**
Use only when the sense is truly one measurable characteristic on one declared scale.
This routes through **A.17/A.18/C.16** and inherits full scale legality.

**QNF-3 — `Bundle`.**
Use when the sense is composite.
Typical for `QS.ExplanatoryMerit`, many engineering quality families, and `QS.ControlAdequacy`.

A conforming bundle publishes:

* member heads,
* whether each head is Characteristic / status / mechanism / scope / test,
* aggregation policy if any,
* prohibition on hidden scalarisation.

**Engineering note.**
For engineering `-ility` families, the preferred bundle form is **`Q-Bundle`** (C.25), because it keeps **Measures[CHR]** distinct from **ClaimScope/WorkScope** and from **Mechanisms/Status**.
`Q-Bundle` is a **C.25 authoring profile of `Bundle`**, not a fifth normal form beside `SignalPack | Characteristic | Bundle | Objective`.
Do not publish a free-floating bundle with hidden metric semantics.

**QNF-4 — `Objective`.**
Use for `QS.UseValue` in selection/generation/search contexts.

A conforming objective publishes:

* CG-frame / objective `authoritySourceRef` target,
* admissible comparators,
* acceptance / selector policy,
* reference plane and window,
* relation to novelty/diversity/constraints.

#### A.6.Q:4.6 - Functional vs quality-family discipline

A.6.Q SHALL prevent the collapse of **function/capability** claims into **quality-family** claims.

* A statement about **what a system does** belongs to functional/procedural description.
* A statement about **how well / how safely / how robustly / how maintainably** it does so belongs to `QS.EngineeringQualityFamily`.
* “Quality characteristic” and “functional characteristic” SHALL NOT be used as interchangeable labels.
* In engineering contexts, `-ility` names are **quality-family labels**, not automatically Characteristics.
  They become admissible only as one explicit `U.Characteristic` or one explicit `Bundle` (preferably authored as `Q-Bundle` when composite).
* Cross-references are allowed; category collapse is not.

#### A.6.Q:4.7 - Bridge discipline across traditions

Whenever two different traditions are compared using the word *quality*, the author SHALL publish an explicit **bridge stance** and loss note.

Allowed bridge stances:

* **`localRename`** — near-synonymous within one Context.
* **`operationalizes`** — one sense is turned into a proxy or measurable form.
* **`partialAnalogy`** — structurally similar but not identical.
* **`projection`** — one richer sense is projected into a narrower evaluative frame.
* **`nonEquivalent`** — same word, no admissible bridge asserted.

Examples:

* `QS.PreconceptualFit` - `QS.LatentFit` is usually `partialAnalogy`, not identity.
* `QS.PreconceptualFit` - `QS.PhenomenalCharacter` is usually a progression-by-articulation relation, not identity.
* `QS.PreconceptualFit` > engineering measures is usually `operationalizes` or `projection`, with loss notes.
* `QS.EngineeringQualityFamily` > `QS.UseValue` is usually `projection` under a CG-frame.
* `QS.ExplanatoryMerit` - `QS.UseValue` is **not** identity unless a Context explicitly defines such a projection.
* Pirsig-style **dynamic quality** usually applies `QS.PreconceptualFit` (sometimes `QS.LatentFit`) only as `localRename` / `partialAnalogy` under a declared `U.BoundedContext`; it is not identity by label.
* Pirsig-style **static quality** usually applies `Characteristic` or `Bundle` publication under some other declared sense; it is not identity with dynamic quality.
* `QS.ArchitecturalDescriptionFitness` - `QS.EngineeringQualityFamily` is usually `projection` or `nonEquivalent` unless the Context explicitly states which heads of description-fitness are intended to proxy which system-side characteristics.

#### A.6.Q:4.8 - Change lexicon

A conforming pattern SHALL narrate changes with a stable change lexicon aligned to A.6.P:

* **`declareevaluativeAscription(...)`** — create a new explicit quality ascription record.
* **`withdrawevaluativeAscription(...)`** — retire a prior record.
* **`retargetBearer(...)`** — change the evaluated bearer tuple while keeping the same relation family.
* **`reviseSense(...)`** — change the value in the `qualitySense` slot.
* **`reArticulate(...)`** — change `articulationMode` while preserving sense family.
* **`reProxy(...)`** — change proxy/probe/operationalisation details.
* **`reBundle(...)`** — change bundle members or aggregation policy.
* **`reScale(...)`** — change characteristic scale or scale type.
* **`reFrame(...)`** — change evaluation frame.
* **`reView(...)`** — change evaluator/viewpoint.
* **`rescope(...)`** — change `U.Scope`.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnesses(...)`** — refresh evidence or witness bindings.
* **`changeRelationKind(...)`** — semantic move to a different relation family; never edit in place silently.

A silent **sense rewrite** is a breaking semantic change.
If the ascription ceases to mean “quality ascription” at all, use `changeRelationKind(...)` rather than pretending the same record survived unchanged.

**A.6.P rewrite note.**
`retargetBearer(...)` is the family-specific form of `retargetParticipant(BearerSlot, …)`.
`reviseSense(...)`, `reArticulate(...)`, `reProxy(...)`, `reBundle(...)`, `reScale(...)`, `reFrame(...)`, and `reView(...)` are family-specific refinements of `reviseByValue(...)` and SHALL preserve the A.6.5 distinction between ref retargeting and by-value edits.

#### A.6.Q:4.8a - A.6.B classification template for `evaluativeAscription`

When a repaired quality statement becomes boundary-bearing, classify it explicitly:

* **L** — `evaluativeAscription` relation specification skeleton, `QualitySense` semantics, normal-form admissibility, and declared bridge stances;
* **A** — admissibility conditions for using the ascription in selector, gating, and publication lanes (required qualifiers, witnesses, thresholds, qualification windows);
* **D** — author and publisher obligations (lexical firewall, mandatory rewrites, publication duties);
* **E** — carrier-anchored evidence/work effects (measurements, traces, critique sheets, probe packs, selector logs).

Where this family is published as a reusable boundary publication, authors SHOULD publish stable `L-Q*` / `A-Q*` / `D-Q*` / `E-Q*` claim ids (or explicitly cite the reused L/A/D/E-classified claim set by location) and SHALL avoid paraphrase drift across quadrants.
Do not let the bare word *quality* carry L/A/D/E force by itself.

#### A.6.Q:4.9 - Lexical guardrails

In **Tech / normative prose**:

* bare **quality** MUST NOT appear without immediate resolution to a `QualitySense`;
* **high-quality / low-quality / quality metric / quality score / quality requirement / model quality / architecture quality / solution quality** are red-flag tokens;
* **quality characteristic** MAY appear only as:

  * a bridge label to an external standard/tradition, or
  * a family label immediately rewritten into one explicit `U.Characteristic` or `Q-Bundle`;
* **quality requirement / quality requirements** MUST NOT remain bare noun phrases; authors SHALL rewrite them into explicit `RequirementRole` / `U.Commitment` / `U.PromiseContent.acceptanceSpec` structures over one named `U.Characteristic`, one `Q-Bundle` head, or one explicit objective head;
* **architecture quality / architectural quality** MUST NOT appear without an explicit bearer lane (`Object | Description | Carrier`) and, when omission changes meaning, an explicit `referencePlane`;
* in QD/NQD contexts, bare **quality** MUST default to **`QS.UseValue`**;
* preconceptual uses MUST NOT be presented as if they were already Characteristics;
* latent/distributed fit MUST NOT be presented as if it were automatically explanatory merit;
* if the occurrence is primarily **action-invitation** talk, authors MUST NOT force a `QualitySense`; they SHALL exit to the appropriate relation family;
* scope words (*applicability*, *envelope*, *generality*, *validity*) MUST NOT be used as hidden substitutes for `U.Scope`, `U.ClaimScope (G)`, or `U.WorkScope`;
* quoted metalinguistic uses of the token *quality* are allowed, but SHALL be marked as **token-under-discussion**, not as a boundary-bearing term.

#### A.6.Q:4.10 - Progressive elaboration

A.6.Q supports monotone elaboration:

1. Start by selecting a **`QualitySense`** and capturing rival candidates when ambiguity is live.
2. Declare bearer, frame, viewpoint, and substrate.
3. Choose an admissible **normal form**.
4. Add exemplars / probes / characteristic heads / bundle members / objective pins.
5. Add bridges and loss notes if comparing traditions.
6. If the repaired sentence is boundary-bearing, emit `L/A/D/E` L/A/D/E hooks rather than letting “quality” carry them implicitly.
7. Never move between sense families silently.

### A.6.Q:5 - Archetypal Grounding

#### A.6.Q:5.1 - Tell

If a draft says *quality*, the author has not yet named the evaluative family.
A conforming rewrite publishes either one explicit endpoint-pattern-governed evaluative form or one explicit `evaluativeAscription(...)` transitional record with one `QualitySense`, one bearer tuple, one evaluation frame, one evaluator/viewpoint, one admissible normal form, explicit scope/time/bridge qualifiers when they matter, and declared target endpoint governing pattern or publication with named authority-reference relation.
#### A.6.Q:5.2 - Show (System lane)

**Draft:** “The model quality improved.”

**Repair A — latent representation line**
`evaluativeAscription(
  bearer = Model_v5,
  qualitySense = QS.LatentFit,
  evaluationFrame = ProbePack_PP2,
  evaluator = RepLearningReviewBoard,
  normalForm = SignalPack,
  Γ_time = Window_W5,
  witnesses = {ProbeSeparationRun_22, AliasRiskCard_9}
)`

**Repair B — closed-loop control line**
`evaluativeAscription(
  bearer = PolicyModelPair_PM5,
  qualitySense = QS.ControlAdequacy,
  evaluationFrame = Horizon_H × EnvClass_E,
  evaluator = ControlReviewBoard,
  viewpoint = ControlView_VP,
  normalForm = Bundle,
  scope = U.WorkScope(ControlDeploymentScope_7),
  Γ_time = RunWindow_RW,
  witnesses = {ClosedLoopTraceSet_41}
)`

#### A.6.Q:5.3 - Show (Episteme lane)

**Draft:** “Quality matters before definition.”

**Repair A — preconceptual / phenomenological line**
`evaluativeAscription(
  bearer = ProblemFramingEpisode_PF3,
  qualitySense = QS.PreconceptualFit,
  evaluationFrame = ExemplarPack_EP3,
  evaluator = ReviewerGroup_A,
  normalForm = SignalPack,
  representationSubstrate = embodied-kinesthetic,
  witnesses = {EpisodeNotes_3}
)`

**Repair B — explanatory line**
`evaluativeAscription(
  bearer = Explanation_N5,
  qualitySense = QS.ExplanatoryMerit,
  evaluationFrame = CriticismBundle_CB4,
  evaluator = TheoryReviewPanel,
  referencePlane = epistemic,
  normalForm = Bundle,
  witnesses = {CritiqueSheet_14, CounterexampleSet_2}
)`

#### A.6.Q:5.3a - Show (Architecture description lane)

**Draft:** “The architecture quality improved.”

**Repair A — quality of the described system**
`evaluativeAscription(
  bearer = PaymentPlatform_v4,
  qualitySense = QS.EngineeringQualityFamily,
  evaluationFrame = Q_Bundle_AvailabilitySecurityEvolvability_3,
  evaluator = ArchitectureReviewBoard,
  viewpoint = TEVB_ArchitectureViewpointSet,
  referencePlane = world/external,
  normalForm = Bundle,
  witnesses = {AvailabilityReport_8, CouplingCheck_3, EvolvabilityNote_2}
)`

**Repair B — quality of the architecture description**
`evaluativeAscription(
  bearer = ArchitectureDescription_AD12,
  qualitySense = QS.ArchitecturalDescriptionFitness,
  evaluationFrame = ViewpointBundle_TEVB × DecisionQuestionSet_DQ7,
  evaluator = ArchitectureReviewBoard,
  viewpoint = TEVB_ArchitectureViewpointSet,
  referencePlane = epistemic,
  normalForm = Bundle,
  witnesses = {CoverageMatrix_4, CorrespondenceCheck_7, ViewConsistencyNote_2}
)`

#### A.6.Q:5.4 - Show (QD / selector lane)

**Draft:** “Quality in our QD loop.”

**Repair**
`evaluativeAscription(
  bearer = Candidate_7,
  qualitySense = QS.UseValue,
  evaluationFrame = CG_Frame_9,
  evaluator = SelectorPolicy_P4,
  normalForm = Objective,
  Γ_time = SelectionWindow_SW,
  witnesses = {ObjectiveCard_9, AcceptanceSpec_4}
)`

### A.6.Q:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for overloaded evaluative uses of *quality* in FPF prose.

* **Gov bias:** this pattern favors explicit evaluative publication and explicit L/A/D/E hooks, which improves auditability but adds authoring overhead.
* **Arch bias:** this pattern prefers one stable ascription relation over free-form philosophical prose, which improves reuse but can feel rigid in exploratory notes.
* **Onto/Epist bias:** this pattern refuses to collapse preconceptual, latent, explanatory, engineering, and selector senses into one concept; that increases honesty at the cost of extra lexical work.
* **Prag bias:** this pattern defaults QD/NQD uses toward `UseValue`, which improves selector clarity but can feel narrower than colloquial “quality”.
* **Did bias:** this pattern is intentionally teachable through repeated rewrites; the risk is over-formalizing early exploratory language.

### A.6.Q:7 - Conformance Checklist (CC-A.6.Q)

A text or pattern conforms to A.6.Q iff:

1. **CC-A.6.Q-1 - Explicit endpoint classification and explicit sense.**
   Every in-scope use of *quality* resolves either to one declared endpoint-pattern-governed evaluative form or to one declared `evaluativeAscription(...)` transitional record with one declared `QualitySense` and explicit endpoint classification.
2. **CC-A.6.Q-2 - Explicit bearer and arity.**
   The evaluated bearer tuple is explicit.

3. **CC-A.6.Q-3 - Explicit frame.**
   Evaluation frame is explicit and reviewable.

4. **CC-A.6.Q-4 - Evaluator/viewpoint is explicit.**
   The ascription states who evaluates, from which viewpoint, or under which selector/observer policy.

5. **CC-A.6.Q-5 - Substrate and referencePlane are declared when relevant.**
   Cross-talk between preconceptual, latent-distributed, symbolic-local, and world/concept/epistemic uses is not allowed without an explicit substrate and/or `referencePlane` declaration when those distinctions are live.

6. **CC-A.6.Q-6 - Scope and `Γ_time` are explicit when omission changes meaning.**
   If scope or time selection affects interpretation, the ascription declares `U.Scope` and/or `Γ_time` explicitly.

7. **CC-A.6.Q-7 - Lawful normal form.**
   The ascription is published as `SignalPack`, `Characteristic`, `Bundle`, or `Objective`, with the corresponding discipline observed.

8. **CC-A.6.Q-8 - No illegal scalarisation.**
   Composite senses are not collapsed into one score without an explicit scoring method.

9. **CC-A.6.Q-9 - No silent sense rewrite.**
   Any semantic change in the ascription uses the declared change lexicon; changing sense silently is forbidden.

10. **CC-A.6.Q-10 - QD default.**
   In search/selection/NQD contexts, *quality* resolves to `QS.UseValue` unless overridden explicitly.

11. **CC-A.6.Q-11 - Engineering family discipline.**
   Engineering `-ility` uses resolve to one explicit `U.Characteristic` or one explicit `Bundle` (preferably authored as `Q-Bundle` when composite); they are not left as free-floating adjectives.

12. **CC-A.6.Q-12 - Functional separation.**
    Function/capability claims remain distinct from quality-family claims.

13. **CC-A.6.Q-13 - Bridge accountability.**
    Cross-tradition parallels publish bridge stance and loss notes; cross-context or cross-plane reuse cites explicit Bridge ids and CL policy where applicable.

14. **CC-A.6.Q-14 - Boundary-claim hook when needed.**
    If a repaired quality ascription is used for admissibility, commitments, publication, or adjudication, the downstream `L/A/D/E` hooks are explicit rather than carried implicitly by the word *quality*.

15. **CC-A.6.Q-15 - Lexical firewall.**
    Bare *quality* is absent from Tech/normative prose except as quoted metalinguistic discussion.

16. **CC-A.6.Q-16 - `evaluativeAscription` relation specification skeleton is published.**
    The family-specific `RelationKind` token `evaluativeAscription` resolves to a relation specification skeleton that publishes polarity, participant SlotSpecs, qualifier expectations, repair paths for bearer-kind mismatches, witness discipline, admissible change classes, and cross-context or cross-plane policy.

17. **CC-A.6.Q-17 - Candidate-Set Note is used when ambiguity is live.**
    If sense selection, bearer facet, or A.7 lane (`Object | Description | Carrier`) is non-obvious, the text records a short Candidate-Set Note before the rewrite is treated as decision-bearing or publication-bearing.

18. **CC-A.6.Q-18 - Evaluator and viewpoint are not silently collapsed.**
    When both an evaluator and a `U.Viewpoint` matter, they are represented as separate slots or fields.

19. **CC-A.6.Q-19 - Family-specific change verbs dock cleanly with A.6.P / A.6.5.**
    `retargetBearer(...)` is used only for ref retargeting; sense/frame/bundle/scale/view edits are narrated as explicit by-value revisions; silent retyping is forbidden.

### A.6.Q:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| --- | --- | --- | --- |
| **Magic scalar quality** | one number silently stands for several evaluative families | collapses senses, carriers, and scoring legality | publish one explicit `QualitySense` and an admissible normal form |
| **Preconceptual-as-metric** | felt fit is presented as if it were already a measured characteristic | erases articulation stage and overstates evidence | keep it as `SignalPack` until an admissible proxy is declared |
| **Engineering adjective drift** | *reliable / maintainable / high-quality* appear with no explicit Characteristic or Q-Bundle | hides measurement shape and scope | rewrite to one `U.Characteristic` or one `Q-Bundle` |
| **Selector ambiguity** | *quality in QD/NQD* is left undefined | breaks comparability and selection semantics | default to `QS.UseValue` unless another objective head is declared explicitly |
| **Model-quality collapse** | latent fit, explanatory merit, and control adequacy are merged under one phrase | destroys carrier and frame distinctions | split into separate `evaluativeAscription(...)` records |
| **Architecture-vs-description collapse** | *architecture quality* is used with no explicit bearer lane | collapses the described system into its description, carrier, or publication face | publish the bearer lane explicitly and select `QS.EngineeringQualityFamily` or `QS.ArchitecturalDescriptionFitness` |
| **Action-invitation-as-quality** | action invitations are narrated as if they were evaluations | wrong relation family; the rewrite hides action semantics instead of clarifying them | stop the Q-rewrite and `changeRelationKind(...)` into the appropriate action-invitation family |
| **Bridge-by-label** | two traditions both use *quality*, so the draft implies they are the same | creates false identity and silent loss | publish one bridge stance with loss notes |

### A.6.Q:9 - Consequences

**Benefits.**
This pattern makes evaluative language auditable across phenomenology, engineering, and search/selection contexts.
It also makes later lexical migration easier because the repair is carried by one explicit relation family rather than by ad hoc prose rules.

**Trade-offs / mitigations.**
The pattern adds authoring overhead and can feel heavy in exploratory notes.
Mitigation: allow bare *quality* in Plain commentary during exploration, but require repair before the term enters Tech/normative, boundary, selector, or assurance use.

### A.6.Q:10 - Rationale

A.6.Q makes one strategic move:

> **The word “quality” is not treated as one concept. It is treated as a family of evaluative ascriptions whose members differ by substrate, articulation mode, bearer, frame, and admissible publication form.**

This lets FPF discuss:

* Pirsig-like preconceptual fit,
* representation-learning and neuro-symbolic latent fit,
* explanation quality in criticism-driven inquiry,
* architecture-description fitness under a viewpoint,
* engineering quality families,
* use-value in open-ended evolution,
* control adequacy in action loops,

without forcing them into one false universal scalar.

It also makes the distributed-vs-local issue explicit:

* some senses originate in **embodied** or **latent-distributed** substrates,
* some are only publishable as **symbolic-local** CHR/bundle/objective forms,
* and some require an explicit **projection** from the first into the second.

It also makes the bearer/plane issue explicit:

* some uses evaluate the **described entity**,
* some evaluate its **description** under a viewpoint,
* some evaluate a **carrier** or **publication face**,
* and those readings must not be collapsed without an explicit bearer lane and, when needed, a declared `referencePlane`.

That is exactly where semantic drift usually starts; A.6.Q turns that drift into an auditable design choice.

### A.6.Q:11 - SoTA-Echoing

**Evidence binding note.** If your Context maintains a **SoTA Synthesis Pack** for evaluative language, architecture-quality vocabularies, selector/objective semantics, world-model evaluation, or embodied/preconceptual articulation, this section **SHALL cite** its ClaimSheet IDs / CorpusLedger entries / BridgeMatrix rows and keep the adoption stances below consistent with those IDs. Otherwise, treat the table below as the seed source set for this pattern revision.

This section follows the required craft: **claim > practice > source > alignment > adoption status**. A.6.Q aligns with contemporary practice across architecture-description standards, software-quality standards, evolutionary architecture, QD search, active inference/world-model research, phenomenology/TAE, affordance theory, and philosophy of explanation—while making one explicit FPF move that those traditions usually leave implicit: the overloaded token *quality* is repaired into explicit evaluative endpoint forms, with `evaluativeAscription(...)` available as a declared transitional record carrying `QualitySense`, bearer, frame, admissible normal form, and bridge stance while routing remains open.

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

### A.6.Q:12 - Relations

* **Specialises:** **A.6.P** as an RPR pattern for overloaded evaluative language centered on *quality*.
* **Builds on:** **A.2.6** for explicit scope and `Γ_time`, **A.17/A.18/C.16** for admissible measurable characteristics, **C.25** for engineering `Q-Bundle` authoring.
* **Coordinates with:** **A.6.A** for relation-family exits into action-invitation repair; **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, admissible moves, early cue routing, responsibility handoff, and admissible retreat/reopen; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account; **B.5.2.0** for prompt-shaped continuations that are not yet stable endpoint publication; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for language-state facet governance; **C.17, C.18, and C.19** for `QS.UseValue`, novelty/diversity discipline, and selector policy; **E.17.0** and **E.17.2** for architecture-description and viewpoint bundles; **F.9** and **F.9.1** for Bridges, CL, and bridge-stance annotations; **A.6.B** when repaired ascriptions become boundary-bearing.
* **Recommends publication via:** **E.10, F.17, and F.18** when the `evaluativeAscription` relation specification skeleton, the `QualitySense` starter set, and the red-flag rewrites become stable shared vocabulary.

#### A.6.Q:12.1 - Language-space refactor note
This pattern uses **endpoint-first routing** rather than universal governance of all quality language. `evaluativeAscription(...)` remains useful as a transitional repair record, but it is not the required resting place for every repaired use of `quality`.

#### A.6.Q:12.2 - Explicit endpoint selection
Lawful endpoints after repair include:
- a single `Characteristic`,
- a `Q-Bundle`,
- an `Objective`,
- an explanatory-merit bundle,
- a selector-value endpoint.

Bare `quality` in Tech prose should therefore be banned or rewritten immediately under an explicit endpoint-governing FPF pattern or `authoritySourceRef` target. If that endpoint source is already known, `evaluativeAscription(...)` need not remain in the published normal form.

#### A.6.Q:12.3 - Ownership boundary
This pattern does not govern articulation-state characteristics, bridge stances, or representation factors. Those remain governed by `A.16`, `C.2.LS`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, and `F.9.1`.
### A.6.Q:End

## A.6.A - `U.ActionInvitationPrecisionRestoration` - Affordance / Action-Invitation Precision Restoration (ACT-INV)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Affordance / action-invitation precision restoration.

**Intent.**
Provide a reusable discipline for repairing overloaded **affordance / action-first** language in FPF texts.

This pattern is an **A.6.P RPR specialisation** for **post-threshold** action-oriented content: it turns bare action-oriented prose into one explicit, slot-explicit **action invitation** relation family with a declared **sense family**, admissible **normal forms** (`CuePack | ActionOption | OptionSet | PolicyHook`), explicit **change semantics**, and lexical guardrails.
Pre-threshold action-guiding cue content remains with `A.16.1` / `B.4.1` until the cue is articulated enough for `actionInvitation(...)` publication.
It does **not** mint a parallel execution ontology: whenever an invitation is articulated far enough to reference executable method descriptions, work plans, or work occurrences, publication SHALL dock to the exact **A.15** lane (`U.Method`, `U.MethodDescription`, `U.WorkPlan`, or actual `U.Work` once execution has occurred) rather than inventing new action kinds by prose.

It allows ecological-psychology, phenomenological, active-inference, control-theoretic, interface, engineering-operations, and robotics uses to coexist **without false identity by label**.

**Placement.**
Part A > cluster **A.6 Signature Stack & Boundary Discipline** > specialisation of **A.6.P** for under-specified affordance / action-first language.

**Builds on.**
A.3, A.6, A.6.B, A.6.P, A.6.S, A.6.0, A.6.5, A.2.6, A.7, A.15, E.8, E.10, F.9, F.18.

**Coordinates with.**
**A.6.Q** for evaluative-language repair; **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, articulation/closure coordination, admissible moves, early cue routing, responsibility handoff, and admissible retreat when a published invitation must be reopened; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account; **B.5.2.0** when the admissible continuation is still an open probe question rather than an invitation; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for articulation, closure, anchoring, and representation-factor facets referenced but not governed here; **A.10/B.3** for evidence and assurance; **B.4/B.5** for anomaly-driven cycles; **E.17/E.18** for viewpoint publication; **F.9.1** for bridge-stance annotations; **C.3.3** for kind-bridge repair when endpoint kind mismatches appear.

**Non-goal.**
This pattern does **not** assert that physical affordances, interface affordances, social affordances, epistemic probe moves, articulation-closure moves, latent policy cues, and control opportunities are one concept.

Its job is to publish a disciplined **bridge reading** across those traditions while preventing false identity by shared language.

It also does **not** assert that every trigger use of action-first language is admissibly repaired by `actionInvitation(...)`:

* where the repaired statement is primarily **evaluative**, use **A.6.Q**;
* where it is primarily about **general capability**, use functional / method description;
* where it is primarily **deontic**, apply **A.6.B**;
* where it is primarily about **scheduled or executed enactment**, dock to **A.15** (`U.Method` / `U.MethodDescription` / `U.WorkPlan`, or actual `U.Work` once execution has occurred) rather than letting `actionInvitation(...)` become a shadow execution model.

### A.6.A:1 - Problem frame

FPF repeatedly encounters a predictable precision failure mode around **affordance / action-first** language.

Authors say:

* “this handle affords pulling”
* “the interface invites confirmation”
* “the alarm calls for rollback”
* “this discrepancy suggests probing deeper”
* “the draft is ready for formalization”
* “the model wants to brake”
* “the situation is actionable”

…but the intended meaning is actually one of several different **action-oriented families**, for example:

1. **Physical affordance** — a physical/environmental configuration offers a bodily action to an embodied agent.
2. **Interface affordance** — an interface face, operator panel, alarm, or publication face presents an operator move.
3. **Social affordance** — another agent or interactional setting invites a response or coordination move.
4. **Epistemic probe move** — a problem situation invites asking, comparing, measuring, testing, or instrumenting.
5. **Closure-advance move** — a situation invites naming, rescoping, proxy declaration, or formalization.
6. **Latent policy cue** — a learned/distributed state carries an action-oriented tendency not yet locally articulated.
7. **Control opportunity** — a closed-loop state invites braking, rollback, replan, isolate, escalate, or override.

The recurrent failure modes are:

* **Site confusion.** The invitation-bearing site is unclear: object, scene, interface object, description, carrier, policy state, or problem episode.
* **Enactor confusion.** It is unclear **which system / collective system / role-holder** is invited to act: human operator, robot controller, research team, review service, or some unnamed “system”.
* **Action confusion.** The candidate action is hidden behind vague language like *actionable*, *calls for*, *ready for*, *natural next step*.
* **Invitation vs obligation collapse.** A situation that merely invites an action is rewritten as if it already created a duty.
* **Invitation vs capability collapse.** A local, situated action opportunity is rewritten as if it were a general capability claim.
* **Invitation vs work collapse.** Offered action is narrated as if it had already been executed.
* **Substrate confusion.** Ecological, embodied, latent-distributed, and symbolic-local action cues are silently collapsed.
* **Bridge illusion.** Similar language across traditions is mistaken for sameness.
* **Premature closure.** An early cue is published as if it were already a committed method, gate, or policy.

### A.6.A:2 - Problem

How can FPF let authors use the communicative convenience of **affordance / action-first** language while preventing category errors when the language crosses:

* ecological / phenomenological discourse,
* interface and operator-facing discourse,
* active-inference / world-model discourse,
* control / monitoring / incident-response discourse,
* robotics / embodied-AI discourse,
* epistemic exploration and problem-framing discourse?

### A.6.A:3 - Forces

* **Action speed vs auditability.** Action-first language is attractive because it is fast; that same speed makes it unsafe at boundaries.
* **Situated coupling vs explicit publication.** Affordances arise in agent–environment or policy–world coupling, but boundary use requires explicit local publication.
* **Preconceptual cue vs later articulation.** Some invitations are real before they are stably worded.
* **Enactor specificity vs shared discourse.** A cue may be visible to one detector yet relevant to another would-be enactor.
* **Opportunity vs obligation.** Not every invitation is a gate or commitment.
* **Option plurality vs premature scalarisation.** Several candidate actions may co-exist without an admissible total ordering.
* **Cross-tradition dialogue vs false unification.** The framework should support parallels without asserting identity.
* **Progressive closure.** An action cue may later become an option, then a policy hook, and only later a formal gate or work plan.

### A.6.A:4 - Solution - Stable lens -> Sense Family -> Slots -> Normal Form -> Change Lexicon -> Guardrails

#### A.6.A:4.0 - Trigger rule

A use of affordance / action-first language is in scope for A.6.A when any of the following holds:

* the prose uses tokens such as **affords**, **invites**, **calls for**, **actionable**, **ready for**, **ripe for**, **natural next step**, **the model wants**, **the interface tells**, **this problem asks for**;
* a boundary, gate, incident note, design note, or review note uses such language for admission, selection, triage, or action guidance;
* different traditions are compared using the same action-first wording;
* a draft introduces *model affordance*, *interface affordance*, *actionable insight*, *policy invitation*, or *ready for formalization* without declared sense;
* the author intends the phrase to carry more than one of: situational action opportunity, latent cue, operator move, probe move, closure move, or control move.

#### A.6.A:4.0a - Operational repair sequence

When the trigger fires, authors SHOULD follow the A.6.P repair path:

1. **Capture the trigger span.**
   Copy the exact trigger phrase.

2. **Reconstruct the candidate set.**
   Enumerate plausible candidate interpretations, including:

   * candidate **relation families** (`actionInvitation` vs `evaluativeAscription` vs capability claim vs commitment vs work occurrence),
   * candidate **site lane maps** over A.7 (`Object | Description | Carrier`),
   * candidate **would-be enactor lanes**,
   * candidate **action tuples**.

   If the occurrence is decision-bearing or publication-bearing, record a short **Candidate-Set Note** before selecting a repair.

3. **Select one explicit action-invitation sense.**
   Pick one `ActionInvitationSense` token and state why rivals were rejected in this local context.

4. **Emit a slot-explicit rewrite.**
   Rewrite the sentence into one explicit `actionInvitation(...)` record with site, would-be enactor, candidate action, coupling frame, detector/viewpoint, normal form, and qualifiers.

5. **Route boundary-bearing consequences.**
   If the repaired statement is used for admissibility, commitments, publication, automation, or evidence-bearing decisions, route the downstream hooks through **A.6.B** and, where enactment is implied, through **A.15**, instead of letting the vague action-first phrase carry the required support by itself.

#### A.6.A:4.1 - Post-threshold lens: action-invitation classification anchored by `actionInvitation(...)`

A.6.A stabilises the ambiguity cluster by treating in-scope post-threshold affordance/action-first statements as **qualified action-oriented content that must publish an explicit action-invitation normal form and declared downstream classification**, not as bare adjectives or rhetorical verbs.
Early action-guiding cue content may remain in `A.16.1` / `B.4.1` as cue-pack content, a `RoutedCueSet`, or another typed route-bounded upstream publication before this pattern is entered.
`A.6.A` is therefore entered only once local `AE` is high enough to name site / enactor / action structure explicitly and local `CD` is high enough that one invitation reading is worth publishing as a relation record rather than remaining cue-pack or route-candidate content. If the admissible publication is still a cue pack, routed cue, or open abductive prompt, stay in `A.16.1` / `B.4.1` / `B.5.2.0`.
If a published `actionInvitation(...)` later loses that minimal articulation/closure support, retreat via `A.16.2` rather than leaving a stale invitation record in force.

In A.6.P terms, this pattern fixes one post-threshold relation family and one downstream classification discipline:
* **`actionInvitation`** — the explicit post-threshold relation kind for affordance, invitation, control-opportunity, probe-move, and closure-advance rewrites once the cue/content is articulated enough to publish a relation record.

#### A.6.A:4.1a - RelationKind specification skeleton for `actionInvitation`


The family-specific `RelationKind` token is **`actionInvitation`**.
Its relation specification publication SHALL declare, at minimum:

* **(L)** applicability in the local Context or plane set;
* **(L)** site-centred polarity: the relation is about a **site/situation** inviting a candidate action **for** an enactor; it SHALL NOT be silently rewritten as a monadic property of an object alone;
* **(L)** participant SlotSpecs for site, invited enactor, candidate action, sense, coupling frame, and normal-form positions;
* **(A)** repair paths for site-kind and enactor-kind mismatches: explicit narrowing, `KindBridge`, and/or `retargetSite(...)` / `retargetInvitedEnactor(...)`;
* **(L)** qualifier expectations for `scope`, `Γ_time`, `viewpoint`, `view`, `representationSubstrate`, `bridgeRef`, and (when relevant) `articulationHint`;
* **(D)** detector/enactor separation discipline: the perceiver or detector SHALL NOT be silently collapsed into the invited enactor when they differ;
* **(D)** obligation barrier: invitation language SHALL NOT be silently rewritten as duty language;
* **(A/E)** witness discipline for decision/publication/automation lanes;
* **(L/A)** admissible semantic change classes and edition-fence expectations;
* **(A/E)** cross-context and cross-plane policy when reuse is claimed.

Each in-scope occurrence SHALL be representable as a pattern-specific **QualifiedRelationRecord**:

`ActionInvitationRecord :=`
`⟨`
`  relationKind             : actionInvitation,`
`  siteTuple                : …,`
`  siteFacetMap?            : tuple-member ↦ (Object | Description | Carrier),`
`  invitedEnactorTuple      : …,`
`  candidateActionTuple     : …,`
`  actionInvitationSense    : ActionInvitationSense,`
`  couplingFrame            : …,`
`  detector?                : …,`
`  viewpoint?               : U.Viewpoint,`
`  view?                    : U.View,`
`  normalForm               : CuePack | ActionOption | OptionSet | PolicyHook,`
`  articulationHint?        : open-cue | sketched | option-explicit | hook-explicit,`
`  scope?                   : U.Scope,`
`  Γ_time?                  : U.GammaTimePolicy,`
`  representationSubstrate? : ecological-world-coupled | embodied-kinesthetic | latent-distributed | symbolic-local | hybrid,`
`  bridgeRef?               : BridgeId,`
`  witnesses?               : EvidenceRefSet`
`⟩`

So the sentence “X affords Y” is never accepted as a terminal form.
Within the scope of A.6.A it must be rewritten into an explicit `actionInvitation(...)` instance with declared downstream governing pattern or publication; earlier pre-threshold cue content may instead remain as cue-pack content, a `RoutedCueSet`, or another typed route-bounded upstream publication before A.6.A entry.

**Discipline note.**
`ActionInvitationSense` is a **slot value inside** the relation family; it is not a replacement for the relation family itself.
The stable intermediate lens is the `actionInvitation(...)` relation; the sense token refines **what kind of invitation** is being published.

**P2W docking note.**
`candidateActionTuple` names the invited move as relation content. It is not an actual `U.Work` occurrence, not a `U.WorkPlan`, not a `U.MethodDescription`, and not a selected method. When the publication needs intended work, planned work, actual work, method selection, work result, or result measurement, it docks to `A.15` / `A.15.1` / `A.15.2` instead of stretching `actionInvitation(...)`.

**A.7 lane note.**
`siteFacetMap` uses only the A.7 lane distinction `Object | Description | Carrier`.
If a `PublicationSurface` / `InteropSurface` participates, declare it separately under **A.7 / L-SURF** rather than widening the lane set with a generic `Surface` token.

**Separation note.**
`detector` and `invitedEnactor` are not synonyms.
When both matter, they SHALL be published separately.

**Enactor note.**
When `invitedEnactorTuple` is published as an actual would-be enactor, it SHALL resolve to a `U.System` or to a role assignment whose holder is a `U.System`. An episteme, description, publication face, or carrier may participate in the **site**, but not as the acting bearer.

**Episteme non-agency note.**
If the site is a Description/Episteme, any later enactment still occurs on carriers and/or target systems; the description itself never acts.

#### A.6.A:4.2 - Core construct: `ActionInvitationSense`

Every in-scope use SHALL resolve to an explicit **`ActionInvitationSense`** token.

An `ActionInvitationSense` token publishes at least:

`ActionInvitationSense :=`
`⟨`
`  senseId,`
`  siteArity,`
`  enactorArity,`
`  candidateActionArity,`
`  defaultArticulationHint,`
`  admissibleArticulationHints,`
`  defaultRepresentationSubstrate,`
`  admissibleRepresentationSubstrates,`
`  defaultNormalForm,`
`  admissibleNormalForms,`
`  couplingFrameKind,`
`  admissibleEvidenceModes,`
`  admissibleChangeClasses,`
`  bridgePolicy`
`⟩`

Where:

* **`defaultArticulationHint`** and **`admissibleArticulationHints`** use the current local alias set
  `{ open-cue, sketched, option-explicit, hook-explicit }`
* **`defaultRepresentationSubstrate`** ∈
  `{ ecological-world-coupled, embodied-kinesthetic, latent-distributed, symbolic-local, hybrid }`
* **`admissibleRepresentationSubstrates`** explicitly declares the admissible publication substrates for the sense;
* **`defaultNormalForm`** ∈
  `{ CuePack, ActionOption, OptionSet, PolicyHook }`

#### A.6.A:4.2a - A.16 alias-docking note

A.6.A carries `articulationHint` only as a **local alias field**.

This field is deliberately **not** a new formality progression, **not** a maturity scale, and **not** a surrogate for **F**. Its only job is to preserve local articulation / closure cues until they are docked to `A.16` move logic and the explicit `C.2.4` / `C.2.5` governing facets.

Local `articulationHint` tokens SHALL dock to `A.16` move logic and to the explicit `C.2.4` / `C.2.5` governing facets one-for-one, and A.6.A SHALL treat them as aliases or publication conveniences only.
Until then, local hints SHALL NOT be thresholded, aggregated, or compared across Contexts.

#### A.6.A:4.3 - Normative starter set of sense families
A Context MAY add local senses, but the following starter set is normative as the initial disambiguation menu:

| `ActionInvitationSense` token | Use when the action-first phrase means…                                                     |            Default normal form | Typical substrate                                    | Must **not** be silently collapsed into                  |
| ----------------------------- | ------------------------------------------------------------------------------------------- | -----------------------------: | ---------------------------------------------------- | -------------------------------------------------------- |
| `AIS.PhysicalAffordance`      | a physical/environmental configuration offers a bodily action to an embodied agent          |    `CuePack` or `ActionOption` | `ecological-world-coupled` or `embodied-kinesthetic` | object property alone, generic capability, executed work |
| `AIS.InterfaceAffordance`     | an interface face, operator panel, alarm, or publication face presents an operator move | `ActionOption` or `PolicyHook` | `symbolic-local` or `hybrid`                         | duty/commitment, execution log                           |
| `AIS.SocialAffordance`        | another agent or social situation invites a response or coordination move                   |    `CuePack` or `ActionOption` | `embodied-kinesthetic` or `hybrid`                   | role assignment itself, deontic commitment               |
| `AIS.EpistemicProbe`          | a problem situation invites asking, contrasting, measuring, testing, or instrumenting       |  `ActionOption` or `OptionSet` | `hybrid`                                             | explanatory merit, evidence claim, finished method       |
| `AIS.ClosureAdvance`          | a situation invites naming, rescoping, proxy declaration, or formalization toward closure   |                 `ActionOption` | `symbolic-local` or `hybrid`                         | Formality **F**, acceptance status, quality ascription   |
| `AIS.LatentPolicyCue`         | a learned/distributed state carries an action-oriented tendency not yet locally articulated |       `CuePack` or `OptionSet` | `latent-distributed` or `hybrid`                     | explicit rationale, control adequacy, quality score      |
| `AIS.ControlOpportunity`      | a closed-loop state invites brake / rollback / replan / isolate / escalate / override       |    `OptionSet` or `PolicyHook` | `hybrid`                                             | bare “model wants”, obligation, work occurrence          |

**Normative rewrite note.**

* In **ecological / embodied** contexts, bare *affords* SHALL rewrite to **`AIS.PhysicalAffordance`** unless another sense is explicitly declared.
* In **interface / alarm / operator-panel** contexts, bare action-first phrasing SHALL rewrite to **`AIS.InterfaceAffordance`** and/or **`AIS.ControlOpportunity`**.
* In **epistemic exploration** contexts, “this suggests probing / formalizing / reframing” SHALL rewrite to **`AIS.EpistemicProbe`** and/or **`AIS.ClosureAdvance`**.
* In **learned world-model / active-inference / policy** contexts, bare “the model wants / the state suggests” SHALL rewrite to **`AIS.LatentPolicyCue`** and/or **`AIS.ControlOpportunity`**, with the distinction made explicit.
* If the sentence is chiefly about **better / worse / fit / merit**, use **A.6.Q** instead of A.6.A.

#### A.6.A:4.4 - Required slots for a conforming `actionInvitation`

A conforming `actionInvitation` SHALL make explicit:

1. **Site tuple and site-facet docking.**
   Site tuple members: entity, scene, interface element or front-end element, description episteme, carrier, episode, or control state - with per-member A.7 lane annotations when the tuple is mixed.

2. **Invited enactor tuple.**
   Which system / collective system / role-holder is invited to act.

3. **Candidate action tuple.**
   What action is being invited.

4. **`ActionInvitationSense`.**
   Which action-oriented family is intended.

5. **Coupling frame.**
   The relation-basis under which the invitation is published.
   Examples: reach envelope, interface state, incident horizon, control horizon, probe pack, open issue set.

6. **Detector and/or viewpoint.**
   Who or what detected the cue, and under which viewpoint it is published.

7. **Normal form and `articulationHint`.**
   How the invitation is published and how far it has been articulated.

8. **Scope and time when relevant.**
   `U.Scope` and `Γ_time` SHALL be explicit when omission changes meaning.

9. **Representation substrate when relevant.**
   Especially when comparing ecological, embodied, latent-distributed, and symbolic-local treatments.

10. **Witness / evidence mode.**
    Exemplars, sensory traces, probe notes, kinematic data, interface events, controller traces, run logs, or review notes.

#### A.6.A:4.5 - Normal-form discipline

An `ActionInvitationSense` SHALL declare one admissible default normal form and MAY declare additional admissible normal forms explicitly.

**Docking note.**
Where a published invitation already points to executable method descriptions, work plans, work occurrences, or their identifiers, the record SHOULD reuse existing `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` identifiers or refs. `PolicyHook` SHALL always be a hook over pre-existing gate, method, or protocol publications; it does not mint a new execution, admissibility, or deontic ontology.

**ANF-1 — `CuePack`.**
Use for early or low-articulation action invitations, especially `AIS.PhysicalAffordance`, `AIS.SocialAffordance`, and many cases of `AIS.LatentPolicyCue`.

A conforming `CuePack` publishes:

* exemplar or contrast episodes, sensory traces, or probe cues,
* site conditions,
* enactor profile or enactor constraints,
* a small gloss set of candidate actions,
* optional ordinal urgency or salience summaries,
* explicit warning that the cue is **not yet** a commitment, a selected method, a gate, or work,
* explicit note that witness-bearing does **not** by itself make the hinted action correct, required, or selected.

**ANF-2 — `ActionOption`.**
Use when one candidate action tuple is explicit.

A conforming `ActionOption` publishes:

* one candidate action tuple,
* invited enactor / role,
* local guard sketch,
* expected near-field effect,
* optional `U.Method` / `U.MethodDescription` / `U.WorkPlan` refs when those already exist in-context,
* explicit note that the option is **not yet selected**, **not yet obligatory**, and **not yet executed**.

**ANF-3 — `OptionSet`.**
Use when several candidate actions coexist.

A conforming `OptionSet` publishes:

* explicit action members,
* any local comparator, triage rule, or partial order,
* admissible incomparability if no total order is admissible,
* prohibition on hidden scalarisation.

**ANF-4 — `PolicyHook`.**
Use when the invitation is explicitly bound to an existing controller, gate, playbook, method, or override protocol.

A conforming `PolicyHook` publishes:

* referenced policy, method, gate, and protocol ids (pre-existing governing FPF patterns or `authoritySourceRef` targets only),
* applicable guard or trigger conditions,
* accountable role or `authoritySourceRef` target,
* escalation or override references when relevant,
* explicit note that the hook is a **binding publication** over existing semantics, not itself a commitment, an admissibility rule, or a work occurrence.

#### A.6.A:4.6 - Separation from quality, capability, commitment, and work

A.6.A SHALL prevent the collapse of action invitation language into neighbouring families.

* A statement about **better / worse / fit / merit** belongs to **A.6.Q**.
* A statement about **what a system can do in general** belongs to capability / method description.
* A statement about **what must be done** belongs to **A.6.B** (`A-*` / `D-*`).
* A statement about **what was actually done** belongs to **A.15 / U.Work**.
* If an invitation targets a description/episteme, any later enactment still occurs on symbol carriers and/or target systems; the description itself never acts.
* Mixed sentences that carry both evaluative and invitational content SHALL be split into `evaluativeAscription(...)` and `actionInvitation(...)` records, with explicit cross-references when the co-occurrence matters.

Mixed sentences SHALL be split.

Examples:

* “This scene is good for grasping” may require **both** `evaluativeAscription(...)` and `actionInvitation(...)`.
* “This alarm requires rollback” is **not** an admissible final affordance record; it needs explicit gate or duty classification.
* “The robot can grasp this handle” is a capability claim unless the situated site/actor/frame and invitation are made explicit.
* “The operator clicked rollback” is work, not invitation.

#### A.6.A:4.7 - Bridge discipline across traditions

Whenever two traditions are compared using action-first language, the author SHALL publish an explicit **bridge stance** and loss note.

Allowed bridge stances:

* **`localRename`**
* **`operationalizes`**
* **`partialAnalogy`**
* **`projection`**
* **`nonEquivalent`**

Examples:

* `AIS.PhysicalAffordance` - `AIS.InterfaceAffordance` is usually `partialAnalogy`, not identity.
* `AIS.EpistemicProbe` - `AIS.ClosureAdvance` is usually a progression-by-closure relation, not identity.
* `AIS.LatentPolicyCue` > `AIS.ControlOpportunity` is often `operationalizes` or `projection`.
* `AIS.PhysicalAffordance` > `PolicyHook` in robotics is usually `projection` under a controller frame.
* Action invitation and quality ascription may co-occur, but co-occurrence is **not** identity.

#### A.6.A:4.8 - Change lexicon

A conforming pattern SHALL narrate changes with a stable change lexicon aligned to A.6.P:

* **`declareActionInvitation(...)`** — create a new explicit action invitation record.
* **`withdrawActionInvitation(...)`** — retire a prior record.
* **`retargetSite(...)`** — change the site tuple while keeping the same relation family.
* **`retargetInvitedEnactor(...)`** — change the invited enactor tuple when that slot is ref-backed.
* **`reviseAction(...)`** — change the candidate action tuple by value (or split into the corresponding `retargetParticipant(...)` form if the local relation specification makes the action slot ref-backed).
* **`reviseSense(...)`** — change the value in the `actionInvitationSense` slot.
* **`reArticulate(...)`** — change the `articulationHint` while preserving sense family.
* **`reFrame(...)`** — change coupling frame.
* **`reGuard(...)`** — change guard sketch or hook condition.
* **`rePolicyHook(...)`** — change policy, gate, or method hook details.
* **`reView(...)`** — change detector publication, viewpoint publication, or view publication.
* **`rescope(...)`** — change `U.Scope`.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnesses(...)`** — refresh witness bindings.
* **`changeRelationKind(...)`** — semantic move to a different relation family; never edit in place silently.

A silent move from invitation to commitment, capability, or work is a breaking semantic change.

**A.6.P rewrite note.**
`retargetSite(...)` and `retargetInvitedEnactor(...)` are family-specific refinements of participant retargeting and SHALL be used only when the corresponding slots are ref-backed. `reviseAction(...)`, `reviseSense(...)`, `reArticulate(...)`, `reFrame(...)`, `reGuard(...)`, and `rePolicyHook(...)` are by-value revisions unless the local relation specification explicitly declares the corresponding slot as ref-backed, in which case the text SHALL use the matching `retargetParticipant(...)` form. This preserves A.6.5’s ref-vs-value discipline.

#### A.6.A:4.8a - A.6.B classification template for `actionInvitation`

When an action invitation becomes boundary-bearing, classify it explicitly:

* **L** — `actionInvitation` relation specification skeleton, `ActionInvitationSense` semantics, normal-form admissibility, actor/site discipline, bridge stances.
* **A** — admissibility conditions for using the invitation in selector, triage, automation, or publication lanes.
* **D** — duties on authors, operators, or stewards of the named source with authority-reference relation: lexical firewall, naming the invited actor, naming the hook `authoritySourceRef` target, naming override paths where required.
* **E** — carrier-anchored witnesses: sensory traces, interface events, probe notes, controller logs, run traces, incident records.

Do not let bare action-first language carry L/A/D/E force by itself.

#### A.6.A:4.9 - Lexical guardrails

In **Tech / normative prose**:

* bare **affords / invites / calls for / actionable / ready for / ripe for / natural next step / the model wants / the interface tells** MUST NOT appear without immediate repair;
* **actionable insight** MUST be rewritten to `ActionOption` / `OptionSet` / `PolicyHook`, or to **A.6.Q** if the use is primarily evaluative;
* **affordance** MUST NOT be treated as a monadic property of an object without actor, site, and frame;
* an invitation MUST NOT be presented as if it were already a duty, gate, or work occurrence;
* a latent policy cue MUST NOT be presented as if it were already an explanation;
* `articulationHint` MUST NOT be read as **F**, as acceptance status, or as a replacement for `A.16` anchors;
* generic `Surface` facet tokens MUST NOT be introduced inside A.6.A; `PublicationSurface`/`InteropSurface` participation must be declared under **A.7 / L-SURF**, not by widening the A.7 lane set;
* hidden enactor language inside adjectives such as *graspable*, *deployable*, *actionable*, *ready* SHALL be unpacked;
* quoted metalinguistic uses are allowed, but SHALL be marked as token-under-discussion.

#### A.6.A:4.10 - Progressive elaboration

A.6.A supports monotone elaboration:

1. Start by selecting an `ActionInvitationSense` and recording rival candidates when ambiguity is live.
2. Declare site, would-be enactor, action, frame, and site-facet docking.
3. Choose an admissible normal form and a local `articulationHint` when omission would hide articulation state.
4. Add guards, method/policy hooks, and witness bindings.
5. If a `CuePack` or `ActionOption` is projected into `OptionSet` or `PolicyHook`, or docked to **A.6.Q**, **A.6.B**, or the relevant **A.15** pattern or lane, publish an explicit projection or operationalization note rather than silently upgrading the invitation.
6. Add bridges and loss notes if traditions are compared.
7. If the invitation becomes boundary-bearing, emit the relevant L, A, D, and E decomposition hooks and, where enactment is implied, apply the relevant A.15 pattern or lane.
8. Never move from invitation into capability, commitment, or work silently.

#### A.6.A:4.10a - Endpoint-first downstream discipline

If a repaired phrase already names an admissible downstream `authoritySourceRef`, `governingPatternRef`, or P2W lane such as a gate hook, method reference, `U.WorkPlan` / `U.WorkPlanning` plan record, or `U.Work` occurrence, authors SHOULD publish that downstream reference or P2W lane directly and keep `actionInvitation(...)` only as the preceding repair record when the invitation semantics themselves still matter. `actionInvitation(...)` is therefore a post-threshold invitation record, not a shadow substitute for `A.6.B`, `A.15`, or gate-governing patterns.

### A.6.A:5 - Archetypal Grounding

#### A.6.A:5.1 - Tell

If a draft says *affords*, *calls for*, *invites*, or *actionable*, the author has not yet named the action-oriented family.

A conforming post-threshold rewrite publishes one explicit `actionInvitation(...)` with one `ActionInvitationSense`, one site tuple, one invited enactor tuple, one candidate action tuple, one coupling frame, one normal form, and explicit articulation / scope / time / substrate qualifiers when they matter. Earlier action-guiding cue content may still remain outside A.6.A as cue-pack content, a `RoutedCueSet`, or another typed route-bounded upstream publication until threshold conditions are met.
#### A.6.A:5.2 - Show (System lane)

**Draft:** “The alarm calls for rollback.”

**Repair A — control / incident line**

`actionInvitation(`
`  site = AlarmBundle_AB9 × ServiceState_S7,`
`  siteFacetMap = { AlarmBundle_AB9: Carrier, ServiceState_S7: Object },`
`  invitedEnactor = OpsTeam_Phoenix,`
`  candidateAction = Enact(MethodDescriptionRef = RollbackRunbook_R41, target = Release_R41),`
`  actionInvitationSense = AIS.ControlOpportunity,`
`  couplingFrame = IncidentPolicy_IP2 × Horizon_H15m,`
`  detector = AnomalyPolicy_AP7,`
`  viewpoint = VP.OperationsControl,`
`  normalForm = PolicyHook,`
`  articulationHint = hook-explicit,`
`  scope = U.WorkScope(ProdCluster_EU_1),`
`  Γ_time = RunWindow_RW,`
`  witnesses = {AlertTrace_91, ErrorBudgetSeries_4}`
`)`

**Repair B — ecological / robot line**

**Draft:** “This handle affords pulling.”

`actionInvitation(`
`  site = DoorHandle_17 × DoorState_Closed × ReachEnvelope_RE2,`
`  siteFacetMap = { DoorHandle_17: Object, DoorState_Closed: Object, ReachEnvelope_RE2: Description },`
`  invitedEnactor = ServiceRobot_R2,`
`  candidateAction = PullAlong(Axis_A1),`
`  actionInvitationSense = AIS.PhysicalAffordance,`
`  couplingFrame = GripClass_G1 × ClearanceProfile_CP3,`
`  detector = PerceptionStack_PS4,`
`  normalForm = ActionOption,`
`  articulationHint = option-explicit,`
`  Γ_time = Window_W1,`
`  witnesses = {DepthFrame_883, ContactModelRun_17}`
`)`

#### A.6.A:5.3 - Show (Episteme lane)

**Draft:** “This problem asks for a better question.”

**Repair A — epistemic probe line**

`actionInvitation(`
`  site = ProblemFramingEpisode_PF3,`
`  siteFacetMap = { ProblemFramingEpisode_PF3: Description },`
`  invitedEnactor = ResearchTeam_A,`
`  candidateAction = Enact(MethodDescriptionRef = ContrastiveQuestioning_Q2),`
`  actionInvitationSense = AIS.EpistemicProbe,`
`  couplingFrame = ExemplarPack_EP3 × OpenIssueSet_O2,`
`  detector = Reviewer_A1,`
`  normalForm = OptionSet,`
`  articulationHint = sketched,`
`  representationSubstrate = hybrid,`
`  witnesses = {EpisodeNotes_3, CounterexampleCard_2}`
`)`

**Repair B — closure-advance line**

**Draft:** “The draft is ready for formalization.”

`actionInvitation(`
`  site = DraftHypothesis_H7,`
`  siteFacetMap = { DraftHypothesis_H7: Description },`
`  invitedEnactor = AuthorCollective_C1,`
`  candidateAction = Formalize_DS(TypedInvariantSet_V1),`
`  actionInvitationSense = AIS.ClosureAdvance,`
`  couplingFrame = AmbiguityMemo_8 × ClaimScope_G1,`
`  detector = ReviewPanel_R4,`
`  normalForm = ActionOption,`
`  articulationHint = option-explicit,`
`  representationSubstrate = symbolic-local,`
`  witnesses = {AmbiguityMemo_8, ReviewCommentSet_5}`
`)`

### A.6.A:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for overloaded affordance / action-first language in FPF prose.

* **Gov bias:** this pattern may tempt authors to smuggle decisions into invitation language.
  *Mitigation:* explicit A.6.B routing and obligation barrier.
* **Arch bias:** this pattern prefers one stable relation family over loose action talk.
  *Mitigation:* allow Plain exploratory prose before Tech / normative publication.
* **Onto/Epist bias:** this pattern insists on separating invitation from evaluation, capability, commitment, and work.
  *Mitigation:* explicit bridge stances and mixed-sentence split rules.
* **Prag bias:** it favors enactor/site/action explicitness, which raises authoring cost.
  *Mitigation:* small starter set, normal-form discipline, and copyable rewrites.
* **Did bias:** repeated rewrites make the pattern teachable, but may over-formalize early cues.
  *Mitigation:* `CuePack` and local `articulationHint` keep early stages admissible without pretending closure.

### A.6.A:7 - Conformance Checklist (CC-A.6.A)

A text or pattern conforms to A.6.A iff:

1. **CC-A.6.A-1 — Explicit post-threshold relation family and explicit sense.**
   Every in-scope post-threshold action-first use resolves to one declared `actionInvitation(...)` instance and one declared `ActionInvitationSense`; earlier cue-like content stays under `A.16.1` or `B.4.1` instead of being forced into A.6.A prematurely.
2. **CC-A.6.A-2 — Explicit site and site-facet docking.**
   The site tuple is explicit; when ambiguous or mixed, the A.7 lane map (`Object | Description | Carrier`) is explicit.

3. **CC-A.6.A-3 — Explicit invited enactor.**
   The invited enactor tuple is explicit.

4. **CC-A.6.A-4 — Enactor discipline.**
   When the invited enactor is meant as the actual would-be enactor, it resolves to a `U.System` or role assignment with system holder.

5. **CC-A.6.A-5 — Explicit candidate action.**
   The candidate action tuple is explicit and reviewable.

6. **CC-A.6.A-6 — Explicit coupling frame.**
   The coupling frame is explicit.

7. **CC-A.6.A-7 — Detector/viewpoint separation.**
   When both matter, `detector` and `viewpoint` are not silently collapsed.

8. **CC-A.6.A-8 — Lawful normal form.**
   The invitation is published as `CuePack`, `ActionOption`, `OptionSet`, or `PolicyHook`, with corresponding discipline observed.

9. **CC-A.6.A-9 — Articulation-hint discipline.**
   If omission changes meaning, `articulationHint` is explicit and is not treated as **F** or as an acceptance state.

10. **CC-A.6.A-10 — No invitation-as-obligation.**
    An invitation is not silently published as a duty or gate.

11. **CC-A.6.A-11 — No invitation-as-work.**
    An invitation is not silently published as a work occurrence.

12. **CC-A.6.A-12 — No capability collapse.**
    A situated invitation is not silently rewritten as a general capability claim.

13. **CC-A.6.A-13 — No object-property collapse.**
    Affordance language is not published as a monadic object property when actor/site/frame matter.

14. **CC-A.6.A-14 — No hidden scalarisation.**
    `OptionSet` publication does not introduce a hidden total score or ranking without an explicit comparator / policy.

15. **CC-A.6.A-15 — No silent sense rewrite.**
    Sense changes use the declared change lexicon.

16. **CC-A.6.A-16 — No silent relation-family switch.**
    Moving from invitation to quality ascription, capability, commitment, or work uses `changeRelationKind(...)` or an explicit split.

17. **CC-A.6.A-17 — Bridge accountability.**
    Cross-tradition parallels publish bridge stance and loss notes.

18. **CC-A.6.A-18 — Boundary-claim hook when needed.**
    If the repaired invitation is used for admissibility, commitments, publication, or automation, downstream `L/A/D/E` hooks are explicit.

19. **CC-A.6.A-19 — Lexical firewall.**
    Bare action-first trigger tokens are absent from Tech / normative prose except as quoted metalinguistic discussion.

20. **CC-A.6.A-20 — `actionInvitation` relation specification skeleton is published.**
    The family-specific `RelationKind` token resolves to a relation specification skeleton with SlotSpecs, enactor/site discipline, qualifier expectations, repair paths, witness discipline, admissible change classes, and cross-context policy.

21. **CC-A.6.A-21 — Candidate-Set Note is used when ambiguity is live.**
    If the site lane map, enactor lane, relation family, or sense selection is non-obvious, the text records a short Candidate-Set Note before decision-bearing use.

### A.6.A:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                   | Symptom                                                                                     | Why it fails                                           | How to avoid / repair                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| **Object-property affordance** | “The object is actionable” with no enactor or site frame                                    | collapses relationality into monadic property language | publish site + enactor + action + coupling frame               |
| **Invitation-as-obligation**   | “This calls for rollback” is treated as if rollback is already required                     | hides A/D routing and accountability                   | publish `actionInvitation(...)`, then route duty/gate via A.6.B |
| **Invitation-as-work**         | “The system reacted” is used where only a cue or option exists                              | confuses offer with execution                          | keep invitation separate from A.15 / `U.Work`                   |
| **Capability-as-invitation**   | “The robot can do X” stands in for a situated affordance                                    | destroys local enactor/site conditions                 | separate capability description from action invitation          |
| **Latent cue as explanation**  | a model tendency is narrated as if it were already an explicit rationale                    | overstates articulation and evidence                   | keep as `CuePack` or `OptionSet` until further articulation     |
| **Premature automation**       | an under-supported cue is wired directly into gates or controllers with no explicit hook `authoritySourceRef` target or guard | creates unsafe action pathways                         | require `PolicyHook` + A.6.B routing + witnesses                |
| **ArticulationHint as F proxy**| `hook-explicit` is read as “more formal”                                                    | recreates a forbidden second formality characteristic          | keep F in C.2.3; reserve articulation/closure semantics for `A.16` |

### A.6.A:9 - Consequences

**Benefits.**
This pattern gives FPF an admissible **post-threshold repair record family** for **action-first** discourse. It lets embodied, ecological, latent, interface, and control cues be published without pretending they are already commitments, capabilities, metrics, or work.

It also complements A.6.Q cleanly: A.6.Q repairs **evaluative** ambiguity, while A.6.A repairs **action-inviting** ambiguity.

**Trade-offs / mitigations.**
The pattern adds authoring overhead and can feel heavy in early exploration.

Mitigation: allow bare action-first language in Plain exploratory notes, but require repair before it enters Tech / normative, boundary, automation, assurance, or publication use.

### A.6.A:10 - Rationale

A.6.A makes one strategic move:

> **Affordance / action-first language is not treated as a monadic property and not treated as a hidden duty. It is treated as a family of action invitations whose members differ by site, actor, candidate action, coupling frame, substrate, and admissible publication form.**

This bridge reading is intentionally neutral: in ecological settings the site is **not** treated as a literal speaker or norm-giver. “Invitation” is the stable publishable FPF lens for situated opportunity-to-act talk, not a claim that all source traditions use that word or share one ontology.

This gives FPF an admissible path for:

* ecological and embodied affordances,
* interface and operator prompts,
* epistemic “probe this / formalize this / reframe this” moves,
* latent policy cues in learned systems,
* control opportunities in closed loops,

without forcing them into one false universal vocabulary.

It also keeps the larger architecture clean:

* **A.6.Q** governs evaluative repairs,
* **A.6.A** governs action-invitation repairs,
* **A.6.B** governs boundary routing,
* **A.15** governs enactment and work,
* **A.16** governs articulation / closure progression and admissible moves,
* **C.2.3** remains the sole governing pattern for formality characteristic **F**.

### A.6.A:11 - SoTA-Echoing

Recent philosophical and ecological work treats affordances as **action-relevant possibilities** perceived in engagement and, in some accounts, as **invitations for action**, rather than as viewpoint-free monadic object properties. A.6.A adopts that relational, action-first stance, adapts it by forcing explicit `siteTuple` / `invitedEnactorTuple` / `couplingFrame` publication, and rejects silent collapse into monadic object labels. ([Frontiers][1], [Springer][2])

Recent empirical review work on affordance perception emphasises **attunement and recalibration** in person-plus-object systems rather than fixed, context-free labels. A.6.A adopts the need for actor- and situation-specific publication, adapts it into `CuePack` / `ActionOption` / `OptionSet` normal forms, and rejects any assumption that an affordance phrase is already an admissible metric or a universally portable invariant. ([Springer][2])

Current active-inference work frames generative models as supporting **action-perception loops** and, in many cases, **action-oriented models** that are for adaptive interaction rather than only detached description. A.6.A adopts the action-oriented emphasis and the separation between model-side cueing and enacted action; it adapts this by making `detector` and `invitedEnactor` explicit and by forbidding latent policy cues from counting as work, commitment, or explicit rationale by default. ([UCL Discovery][3])

Current robotics work increasingly uses affordances as **intermediate representations** between perception-language representations and concrete action, including compact keypoint or staged affordance plans. A.6.A adopts this as evidence that affordance publication can be an admissible intermediate publication form; it adapts it into `ActionOption`, `OptionSet`, and `PolicyHook`, and rejects silent promotion of such representations into deontic obligation, proof of correctness, or objective value. ([Robotics: Science and Systems][4])

**Coverage note.**
This section already covers the load-bearing relational/action-oriented stance. Operator-facing interface practice should also be backed by explicit operator-interaction, operator-alarm, and incident-response SoTA support so that it is evidenced as directly as the current ecology, active-inference, and robotics branch.

### A.6.A:12 - Relations

* **Specialises:** **A.6.P** as an RPR pattern for overloaded affordance / action-first language.
* **Builds on:** **A.3/A.7** for enactor discipline and Object≠Description≠Carrier separation; **A.15** for keeping invitation distinct from enactment; **A.6.B** for boundary routing; **E.17/E.18** for viewpoint publication.
* **Works alongside:** **A.6.Q** for evaluative language; the two are siblings, not substitutes.
* **Coordinates with:** **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, admissible moves before post-threshold repair, and retreat when a published invitation must be reopened; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account; **B.5.2.0** for probe-question cases that are still prompt-shaped; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for language-state facet governance.
* **Must not replace:** **C.2.3** as the single governing pattern for **F**.
* **Recommends publication via:** **E.10, F.17, and F.18** when `actionInvitation` tokens, starter senses, and red-flag rewrites become shared vocabulary.


[1]: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1388852/full "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1388852/full"
[2]: https://link.springer.com/article/10.3758/s13423-023-02319-w "https://link.springer.com/article/10.3758/s13423-023-02319-w"
[3]: https://discovery.ucl.ac.uk/10191719/3/Friston_Neural%20representation%20in%20active%20inference.pdf "https://discovery.ucl.ac.uk/10191719/3/Friston_Neural%20representation%20in%20active%20inference.pdf"
[4]: https://roboticsconference.org/2024/program/papers/62/ "https://roboticsconference.org/2024/program/papers/62/"

#### A.6.A:12.1 - Language-space refactor note
This pattern is scoped to **action-invitation repair and endpoint handoff**, not to the whole early cue lane. Early action-guiding cue content may remain in `A.16.1` as cue-pack content, a `RoutedCueSet`, or another typed route-bounded upstream publication before it stabilizes into `actionInvitation(...)`.

#### A.6.A:12.2 - Canonical downstream seam
`actionInvitation(...)` should be classified through `A.6.B` and connected to `A.15` when work enactment is live toward gates, commitments, methods, or work. Operator-facing starter senses such as `AIS.AlertInterventionCue` or `AIS.OperatorInterventionCue` should not be buried under generic `AIS.InterfaceAffordance` when human factors and policy hooks substantively differ.

#### A.6.A:12.3 - Governance boundary
Bridge stances, articulation-state governing patterns, authority-reference fields, and language-state facet characteristics are **referenced** by this pattern but remain governed by `F.9.1`, `A.16`, `C.2.LS`, `C.2.4`, `C.2.5`, `C.2.6`, and `C.2.7`.
### A.6.A:End


## A.6.5 -  U.RelationSlotDiscipline - SlotKind / ValueKind / RefKind discipline for n‑ary relations (with slot‑operation lexicon)

**Plain‑name.** Relation slot discipline.

**Status.** Normative (Core).
**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; directly under A.6.0 `U.Signature` and alongside A.6.1–A.6.4.
**Depends on.**
– A.1 `U.Holon` (holonic carrier model).
– A.6.0 `U.Signature` (universal morphism/relationship signatures).
– A.7 (Strict Distinction; I/D/S vs Surface).
– E.8 (pattern authoring order & SoTA discipline).
– E.10 (LEX‑BUNDLE: Tech/Plain registers, naming guards).

**Coordinates with.**
– C.2.1 `U.EpistemeSlotGraph` (episteme slots: DescribedEntity, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme).
– C.3.* Kind‑CAL (Kinds, KindSignature, KindBridge).
– F.18 (name governance; twin‑register discipline).

### A.6.5:1 - Problem frame

FPF relies heavily on **n‑ary relations and morphisms**:

* episteme component layouts (`U.EpistemeKind` in C.2.1),
* role enactment and assignment,
* method/service signatures,
* guards and bridges in Part B/C,
* publication and view operators in Part E, and any other `U.Signature` whose **Vocabulary** row declares n‑ary relations or operators across Part A/B/C/E.

In practice, existing episteme and drafts **frequently conflate**:

1. the **place/position** in a signatured structure (relation/operator/record/port bundle; e.g. “the 2nd argument, named Subject”),
2. the **kind of value** that may fill that position (`U.Entity`, `U.Holon`, …), and
3. the **reference/identifier** we actually store there (`…Id`, `…Ref`).

This produces subtle bugs (elaborated in A.6.5:2):

* misuse of “Subject/Object” as SlotKind‑like names for very different ValueKinds (explicitly banned for episteme Tech names by E.10),
* the `…Ref` suffix attached to both conceptual values and reference fields, erasing ValueKind vs RefKind,
* mixed reasoning about “role”, “slot”, and “filler” as if they were the same layer,
* fragile substitution questions (“can I plug this module here?”) that depend on informal judgement rather than SlotSpec laws.

A second, subtler conflation appears in prose: authors mix **binding / initialization / assignment / substitution / retargeting / mutation / passing** as if they were synonyms for “put something in a slot”. This blurs the intended discipline precisely in the places where FPF must be crisp (signatures, morphisms, bridges, and viewing operators).

`U.RelationSlotDiscipline` pins a **single, reusable discipline** over `U.Signature` so that **every position in an n‑ary signature** is described with:

* a **SlotKind** — *where* in the signature,
* a **ValueKind** — *what sort of thing* may fill that place, and
* a **RefKind** — *how we point at it* in episteme (identifier / handle), if at all,

**and** it standardises the **lexicon for operations over slots** so that extension texts can describe “early vs late binding”, “retargeting”, and “by‑value edits” without collapsing layers.

This pattern makes slot discipline explicit and shareable across **epistemes, roles, methods, services, bridges, guards, and all other `U.Signature`d calculi**: any “parameter list”, “port list”, “field set”, or “coordinate tuple” for an n‑ary signature in FPF **is** a set of SlotSpecs governed by this discipline.

### A.6.5:2 - Problem (symptoms in FPF)

Typical failure modes the pattern is designed to eliminate:

1. **Slot vs value vs ref confusion.**
   Episteme fields such as `DescribedEntityRef` are sometimes treated as:

   * the **slot** (“the described entity position”),
   * the **value kind** (“the described entity type”), and
   * a **reference field** (“this is the pointer we store”).

   Reasoning about substitution (“can I swap one described entity for another?”) then mixes three levels at once.

2. **Kernel types misused as slot names.**
   Kernel concepts like `U.Entity` or `U.Holon` are used directly as slot names (“the `U.Entity` of this episteme”), hiding the difference between:

   * the abstract **Kind** (`U.Entity` as intensional universe), and
   * the **place** where one such entity is used in a particular relation.

3. **“Role” overloaded as slot.**
   In relation signatures and structural calculi, “role” has crept in as a synonym for “argument position”: “the role of the subject”, “the role of the provider”. This clashes with `U.Role` in RoleEnactment and makes it hard to distinguish:

   * **holonic role** (mask worn by a system), from
   * **slot** (position in a relation).

4. **Ref‑suffix drift.**
   In the absence of a discipline, the suffix `…Ref` is attached to:

   * entity kinds (`U.EntityRef` interpreted as “the entity itself”),
   * episteme fields (`describedEntityRef`),
   * sometimes even to slots (“DescribedEntityRefSlot”).

   That makes it impossible to read signatures and know whether we talk about:

   * a **conceptual value** (by‑value), or
   * a **reference/identifier** (by‑reference via a handle).

5. **Substitution rules not localisable.**
   When the slot/value/ref layers are not separated:

   * we cannot state “you may substitute **any instance of ValueKind V** in Slot S”, nor
   * “this Bridge only changes RefKind, not ValueKind”.

   This blocks clean use of A.6.0 `U.Signature` as a shared calculus for method/role/episteme signatures.

6. **Episteme‑specific slots not standardised.**
   For epistemes, the positions “what is this about?”, “in which holon is it grounded?”, “what ClaimGraph is inside?” re‑appear across patterns. Without a shared slot discipline, each pattern names these ad‑hoc, breaking the ability to state **universal laws** over episteme morphisms (A.6.2–A.6.4).

7. **Operation‑lexicon drift (slot filling spoken as one verb).**
   Extension prose introduces ad‑hoc words for “put something in a slot” and then imports unintended semantics. The most common mistakes are:

   * using a single word (e.g. “fill”, “set”, “occupy”, “attach”) to cover **initialization**, **assignment**, **retargeting**, and **by‑value editing**;
   * using person/role metaphors for slot content (“occupant”) that re‑introduce the “role ≈ slot” confusion;
   * describing “early vs late binding” without stating **which link** is early/late (name→slot binding vs slot→content filling vs ref→referent resolution).

The result: **local convenience, global incoherence** — exactly what A.6.0 and E.10 are supposed to prevent.

### A.6.5:3 - Forces

* **F1 - Simplicity vs expressiveness.**
  Engineers need a **small number of concepts** they can hold in mind while reading a signature; yet we must express:

  * where a parameter sits,
  * which kinds it can take,
  * whether it’s by value/by reference,
  * how substitution behaves,
  * and (in prose) what kind of slot‑operation is being described.

* **F2 - Cross‑disciplinary reuse.**
  Slot discipline must work for:

  * logical relations (KD‑CAL, LOG‑CAL),
  * episteme structures (C.2.1),
  * systems/roles/methods (A/B),
  * services and APIs (including method/service interfaces and ports),
  * cells in tables and databases,
  * guards, bridges, and flows in E.TGA,
  * and publication operations (E.17).

  A scheme that is too domain‑specific (e.g. “database attributes only”) won’t scale; the same discipline must underlie **all** `U.Signature`d argument/port lists.

* **F3 - Alignment with existing tooling.**
  Tooling stacks already operate with:

  * typed parameters and records,
  * identifiers vs values vs references,
  * and (in modern typed settings) explicit distinctions between *binding*, *store update*, and *mutation*.

  FPF must line up with this practice enough that signatures can be implemented without inventing a parallel type system.

* **F4 - I/D/S discipline.**
  Strict distinction (A.7, E.10.D2) already separates **intensional objects**, their **descriptions**, and **specifications**. The same discipline is needed inside relations:

  * slot ≠ value ≠ reference,
  * system role ≠ slot name,
  * describedEntity ≠ guard,
  * and “change the reference” ≠ “change the thing referred to”.

* **F5 - Didactic primacy and naming discipline.**
  E.8 and E.10 demand patterns that are:

  * teachable (Tell‑Show‑Show examples, explicit biases),
  * lexically guarded (Tech/Plain split, explicit head‑nouns).

  Slot discipline must integrate seamlessly with that.

* **F6 - Binding‑time talk must be unambiguous.**
  “Early binding / late binding” is meaningful only if the author states **what is being fixed when**. FPF needs a canonical way to speak about:

  * early/late **slot filling**,
  * early/late **reference resolution / dispatch**,
  * and (where a language expression is in play) early/late **name binding**.

### A.6.5:4 - Solution — SlotKind / ValueKind / RefKind triple (plus a slot‑operation lexicon)

#### A.6.5:4.1 - Three layers for every argument position

`U.RelationSlotDiscipline` extends `U.Signature` with a **three‑layer description** for every argument position (whether we call it “parameter”, “slot”, “coordinate”, or “port” in colloquial prose).
In **normative** text, the canonical word is **slot**, and the canonical carrier is a **SlotSpec** triple (A.6.0).

1. **SlotKind (place in signature).**
   *How this position is denoted in the Signature and what is fixed about it by the signature’s definition.*
   – Examples: `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ServiceEndpointSlot`, `CallerHolonSlot`, `MetricSlot`.
   – SlotKind is **structural**: it picks out **one distinguished place** in the argument/port/field list of a given relation, operator, record, or other signatured bundle; it does **not** name a “role” played by whatever fills the slot.
   – For an n‑ary relation/operator declared in a `U.Signature`, the pair *(Signature id, SlotKind)* identifies a **slot**; positional indices are merely a presentation‑level enumeration of these slots.
   – What a filler “does” in that place (its contribution to laws, constraints, effects) is governed by the **laws over the Signature** and by the corresponding ValueKind, not by SlotKind‑as‑“role”.

2. **ValueKind (kind of slot filler).**
   *Which kinds of things may fill this position in principle (at the intensional level).*
   – Examples: `U.Entity`, `U.Holon`, `U.Method`, `U.Episteme`, `U.ClaimGraph`, `U.Viewpoint`, `U.Characteristic`, `U.ReferenceScheme`.
   – ValueKind is a **Kind** (C.3.\*) or another kernel‑level type; it is **not** a slot and never carries `*Slot`/`*Ref` suffixes.

3. **RefKind (how we store / refer).**
   *What reference/identifier we actually store in episteme when we fill this slot.*
   – Examples: `U.EntityRef`, `U.HolonRef`, `U.MethodRef`, `U.EpistemeRef`, `U.ViewpointRef`, `U.SurfaceRef`, (optionally) `U.ClaimGraphRef` if a Context chooses to reference claim graphs rather than store them by value.
   – RefKind is **about references, not values**; it usually points to an editioned referent (A.7, F.15) and carries the `.edition` field when pinning a phase.

**Discipline:**

* Each declared argument position in a `U.Signature` **MUST** be described by:

  * a SlotKind (name and documentation),
  * a ValueKind (type of permissible fillers),
  * and either a RefKind or an explicit declaration “**by‑value**” (no RefKind; the value is embedded).
* SlotKind and ValueKind are **intensional**; RefKind is **representational**. This mirrors I/D/S: *slot* describes structure, *value* describes what can sit there, *ref* describes how we point to concrete instances.

#### A.6.5:4.2 - Naming discipline: `*Slot` and `*Ref`

This pattern introduces the following **lexical constraints**, aligned with E.10:

1. **`*Slot` reserved for SlotKind.**

   * Any Tech name ending with `…Slot` **MUST** denote a SlotKind: a named place in a relation/morphism signature.
   * Examples:
     – `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`.
   * `*Slot` **MUST NOT** appear in names of:
     – ValueKind (e.g. `U.Entity`, `U.Holon`, `U.Method`),
     – RefKind (e.g. `U.EntityRef`),
     – concrete episteme fields (they may be named e.g. `describedEntityRef`, but not `describedEntitySlotField`).

2. **`*Ref` reserved for RefKind and reference fields.**

   * Any Tech name ending with `…Ref` **MUST** denote either:
     – a **RefKind** (type of references/identifiers), or
     – a **field** whose type is a RefKind (`describedEntityRef : U.EntityRef`).
   * `*Ref` **MUST NOT** appear in names of:
     – ValueKinds (e.g. `U.EntityRef` **cannot** mean “an entity”; it is a reference type),
     – SlotKinds,
     – Kinds themselves (`U.Kind`, `U.Entity`, `U.Holon`).

3. **ValueKind names carry no `*Slot`/`*Ref`.**

   * ValueKinds are named using standard FPF conventions (A/E/F, E.10), without `*Slot`/`*Ref`.
   * Examples: `U.Entity`, `U.Holon`, `U.Method`, `U.ClaimGraph`, `U.ReferenceScheme`, `U.Viewpoint`, `U.View`.

4. **No “Role” as SlotKind head.**

   * In the context of relation signatures, **do not** use “Role” as the head noun for SlotKinds (to avoid conflict with `U.Role`).
   * Use “Slot” or a neutral description: e.g. `EnactorHolonSlot` (ValueKind `U.Holon`) rather than `EnactorRoleSlot`.

These rules become part of the **LEX‑BUNDLE guards** and are enforced by F.18 / name‑acceptance harnesses.

#### A.6.5:4.3 - Integration with `U.Signature` (A.6.0)

`U.Signature` already provides a generic pattern for declaring morphism/relationship signatures (SubjectKind, BaseType, Quantification, ResultKind, Vocabulary, Laws).

`U.RelationSlotDiscipline` refines this by adding a **SlotSpec** layer:

*For each parameter position `i` in a signature*:

```
SlotSpec_i = ⟨name: SlotKind, value: ValueKind, refMode: {ByValue | RefKind}⟩
```

* **SlotKind** — Tech name with `*Slot` suffix, plus documentation.
* **ValueKind** — a `U.Type` (often a `U.Kind` or kernel type) declaring the intensional universe of admissible fillers.
* **refMode**:

  * `ByValue` — the actual value of ValueKind is embedded (typical for small structured values like `U.ClaimGraph` inside an episteme card).
  * `RefKind` — a **type** of references/identifiers for that ValueKind; e.g. `U.EntityRef` for `U.Entity`, `U.HolonRef` for `U.Holon`. Substitution then operates on references, not directly on the underlying values.

In practice, a `U.Signature` that follows this pattern:

* becomes **self‑documenting**: each parameter has a clear “slot vs value vs ref” story;
* supports **typed substitution**: replacing content within the same SlotKind requires only ValueKind compatibility;
* aligns with **tool signatures** in implementation languages (row‑typed records, dependently typed parameters, effect‑typed arguments). ([13])

#### A.6.5:4.4 - Typed substitution discipline

Given a relation or morphism `R` with signature Σ and SlotSpecs `{SlotSpec_i}`:

* A **substitution** at slot `i` is a change of the **slot content** that fills SlotKind_i, within or across episteme entries.
* `U.RelationSlotDiscipline` enforces:

1. **SlotKind invariance.**
   A substitution **never** changes SlotKind — only the slot content (Value/Ref).
   – “We put a different dataset into the `DatasetSlot`.”
   – “We switch the grounding holon in `GroundingHolonSlot`.”

2. **ValueKind compatibility.**
   The new content **MUST** be of the same ValueKind (or a declared subkind) as `SlotSpec_i.value`; Kind‑CAL governs this (`⊑` in C.3.1–C.3.2). If a Context uses EoIClass species constraints (C.3.2), those act as additional guards but do **not** change the SlotKind.

3. **RefKind correctness.**
   If `refMode=RefKind`, the stored field is of that RefKind; substitutions operate on references, not on underlying values. Edition pinning is handled as usual by `.edition` fields in F‑patterns (F.15, etc.).

4. **By‑value vs by‑ref awareness.**
   Substitutions at by‑value slots (e.g. `ClaimGraphSlot`) are **content edits** to the episteme or relation instance; they may affect formality F or assurance lanes. Substitutions at ref slots are **retargetings** of describedEntity or context, and their legality is governed by A.6.2–A.6.4 and Bridge/CL rules. Tooling SHOULD surface this difference explicitly in authoring surfaces (e.g. separate “Ref” vs “embedded content” columns).

These rules give a uniform way to say:

> “You may swap component X with Y in this slot, because they share ValueKind and pass the relevant Kind/Bridge constraints.”

#### A.6.5:4.5 - Slot operation lexicon (binding / filling / assignment / retargeting / mutation)

This subsection standardises **how Core and extensions talk about operations over slots**, without committing FPF to any particular programming language semantics. It is a *lexical* and *didactic* guardrail that preserves the SlotKind/ValueKind/RefKind stratification in prose.

##### A.6.5:4.5.1 - Four‑way separation: Identifier vs Slot vs Slot‑content vs Referent

*Diagram is illustrative; the term distinctions are normative.*

To avoid conflating “binding / assignment / passing / mutation”, FPF authors SHALL keep the following separation in mind:

```
(1) Identifier/Name  ──binds-to──>  (2) SlotKind  ──in an instance──>  (2′) Slot‑instance  ──filled-with──>  (3) Slot‑content (Value | Ref)
                                                              └─(if Ref) resolves-to──> (4) Referent value or editioned referent
```

**Normative terms**:

* **Identifier** (Surface): a name used in a syntax, table column, record field, port label, or parameter label.
* **SlotKind** (I‑plane): the signature‑level label for a distinguished place in a relation.
* **Slot‑instance** (S‑plane / representation): the actual location/cell/position corresponding to a SlotKind inside a specific relation instance, record, port bundle, or episteme card.
* **Slot‑content** (representation): what is stored in a slot‑instance. It is either:

  * a **by‑value value** of ValueKind, or
  * a **reference handle** of RefKind.
* **Referent**: the intensional thing the RefKind points to when resolved, often an editioned referent.

This separation is the anchor for all “binding time” talk in A.6.5:4.6.

##### A.6.5:4.5.2 - Canonical verbs (Tech register) for slot operations *(normative)*

When a pattern, bridge, or operator description discusses a change or action “with respect to a slot”, it SHALL use (or explicitly map to) the following verbs. Each verb is tied to **which link/layer it affects**.

1. **bind / rebind** (Identifier → SlotKind/slot‑instance).
   *Use when the subject is an Identifier/Name and the effect is changing what that name designates.*
   – **bind**: establish a new association of an Identifier to a SlotKind/slot‑instance (or to a value in a language expression).
   – **rebind**: change an existing association of an Identifier to designate a different slot‑instance or different value.
   **Guard:** do not use “bind” to mean “write into a slot”. Binding is about *names*, not slots.

2. **fill** (Slot‑instance ← Slot‑content).
   *The generic, cross‑domain verb meaning “provide slot‑content for a slot‑instance”.*
   – Fill does **not** by itself imply first‑time vs update, nor by‑value vs by‑ref.
   – Use **fill** when discussing hardware slots, tuple coordinates, ports, record fields, or parameters uniformly.

3. **initialize** (first fill).
   *Use when the slot‑instance previously had no content.*
   – For `refMode=RefKind`: initialization sets the initial reference handle.
   – For `ByValue`: initialization sets the embedded initial value.
   **Guard:** do not call initialization “assignment” in normative text.

4. **assign / set / write / update** (subsequent fill; slot‑content replacement).
   *Use when a slot‑instance already has content and you replace it with new content.*
   – These verbs are allowed as near‑synonyms, but **SHOULD** be used consistently within one pattern family.
   **Guard:** when `refMode=RefKind`, prefer **retarget** (below) if the intent is “change what this ref points to”, not “edit content”.

5. **retarget** (Ref slot update, same SlotKind/ValueKind).
   *Use only for `refMode=RefKind` slots, when the operation replaces one reference handle with another, thereby changing the referent while preserving SlotKind and ValueKind.*
   – “Retarget `DescribedEntitySlot` from `UserService#staging` to `UserService#prod`.”
   Retargeting is the canonical FPF verb for “swap the referenced thing in this slot”.

6. **substitute** (typed replacement with explicit compatibility claim).
   *Use when the statement’s main point is the **compatibility law** (“allowed because ValueKind matches”).*
   – Substitute is a **discipline word**: it signals that SlotKind is fixed and ValueKind compatibility is being asserted/checked.

7. **resolve / dereference** (Ref → Referent).
   *Use when a reference handle is mapped to the intensional referent.*
   – This is where “late binding” often hides in runtime systems (dispatch, dynamic lookup, registry indirection).
   **Guard:** resolving a reference is distinct from retargeting the reference.

8. **mutate / modify** (Referent internal change; content unchanged).
   *Use only when the referent itself changes while the slot‑content (the reference handle) does not.*
   **FPF note:** In edition-disciplined contexts, prefer to describe intentional change as **revise**, issue a **re-edition**, and **retarget**, rather than “mutate”, because the Core treats editioned referents as stable per edition (A.7, F.15).

9. **pass** (parameter slot filling).
   *Use for method/service signatures when an argument fills a parameter slot at a call boundary.*
   – Passing is a specialised instance of **fill**, typically realised as parameter binding + slot filling in implementation languages. In FPF text, “pass into SlotKind” is acceptable if SlotKind names the parameter position.

##### A.6.5:4.5.3 - Canonical nouns *(normative)*

To prevent role metaphors from re‑entering slot talk:

* Use **slot‑content** (preferred) or **slot filler** for “the thing currently in the slot”.
* Avoid person/role metaphors such as **occupant** in normative writing. If a Context insists on using such a word in Plain register, it SHALL define it explicitly as a synonym for slot‑content and SHALL NOT derive role semantics from it.
* Use **target**/**referent** for what a Ref points to; use **retargeting** for changing the target by changing the Ref.
* Use **by‑value edit** (or **embedded content edit**) for changes to a `ByValue` slot such as `ClaimGraphSlot`.

##### A.6.5:4.5.4 - Operator naming guidance for slot‑writing operators *(normative, but intentionally lightweight)*

When naming an operator/morphism/bridge whose primary effect is a slot change, the Tech name SHOULD make two things legible:

1. **Which SlotKind(s) it writes**, and
2. **Which operation class it is**, using the canonical verbs above.

Recommended patterns (examples only; Contexts may adopt their own naming style via F.18):

* `Retarget<SlotQualifier>` for ref‑slot retargeting (e.g. `RetargetDescribedEntity`, `RetargetGroundingHolon`).
* `Edit<SlotQualifier>` / `Update<SlotQualifier>` for by‑value content edits (e.g. `EditClaimGraph`).
* `Substitute<SlotQualifier>` when the operator exists to enforce/declare ValueKind compatibility (e.g. `SubstituteDataset`).
* `Resolve<SlotQualifier>` when the operator is about resolving a Ref to a referent (e.g. `ResolveServiceEndpoint`).

This rule is a lexical enforcement of A.6.5:4.4 (typed substitution discipline): the name should tell the reader whether the operator is a **retargeting** (ref change) or a **content edit** (by‑value change).

#### A.6.5:4.6 - Binding time and “early vs late binding” *(normative framing, informative examples)*

In cross‑domain slot talk, “early binding / late binding” is meaningful only if the author states **which link is being fixed when**. Under A.6.5:4.5, there are three distinct “times” that writers must not conflate:

1. **SlotSpec time (signature time).**
   SlotKind / ValueKind / refMode are fixed when the `U.Signature` is declared. This is “early” by definition in FPF Core.

2. **Slot filling time (initialization / assignment / retargeting).**
   A particular relation instance / episteme card / parameter bundle acquires slot‑content for a SlotKind.
   – *Early‑filled* means: chosen at authoring/spec time (e.g. configuration pins a specific `U.HolonRef`).
   – *Late‑filled* means: chosen at runtime or late in a workflow (e.g. service endpoint selected by policy at deployment).

3. **Resolution / dispatch time (resolve RefKind; select referent).**
   Even if a ref handle is present, the referent may be resolved early or late.
   – *Eager resolution* means: resolve now, cache/commit to a referent.
   – *Lazy resolution* means: resolve on demand.
   – *Dynamic dispatch* is a special case: the “method slot” is resolved at call time based on a receiver/context, rather than being statically selected.

**Rule (lexical guard):**
Any use of “early binding” / “late binding” in Core or extensions SHALL specify which of the above it refers to, using one of:

* **early/late‑filled** (slot filling),
* **eager/lazy‑resolved** (resolution),
* **early/late name‑binding** (Identifier binding, if a language expression is being discussed).

This preserves the A.6.5 stratification and prevents importing accidental semantics from a specific programming language.

### A.6.5:5 - Archetypal Grounding (Tell‑Show‑Show)

Following E.7, we ground the pattern in a **System** example and an **Episteme** example.

#### A.6.5:5.1 - System example — authentication pipeline signature

Consider an `AuthPipelineSpecKind` (system‑level episteme describing an authentication pipeline for a microservice). Its key slots might be:

* `DescribedEntitySlot` — “which holon the pipeline is about”
  – ValueKind: `U.Holon` (EoIClass = “UserService system”).
  – RefKind: `U.HolonRef` (e.g. `UserService#prod`).

* `AuthProviderComponentSlot` — “which authentication provider component is selected”
  – ValueKind: `U.Holon` (EoIClass = “AuthProviderSystem”).
  – RefKind: `U.HolonRef` (e.g. `Auth_OIDC`, `Auth_LDAP`).

* `ClaimGraphSlot` — “what is asserted about the pipeline”
  – ValueKind: `U.ClaimGraph`.
  – refMode: `ByValue` (ClaimGraph stored inside the episteme card).

Substitutions / retargetings:

* **Retargeting** `AuthProviderComponentSlot` from `Auth_OIDC` to `Auth_LDAP`:
  – SlotKind fixed (`AuthProviderComponentSlot`).
  – ValueKind unchanged (`U.Holon`, `AuthProviderSystem ⊑ U.Holon`).
  – RefKind unchanged (`U.HolonRef`).
  – Semantically: “retarget the ref that fills the same slot”.

* **Retargeting** `DescribedEntitySlot` from `UserService#staging` to `UserService#prod`:
  – Same SlotKind and ValueKind.
  – Different `U.HolonRef` slot‑content.
  – May require different grounding and assurance episteme, but the slot discipline is identical.

#### A.6.5:5.2 - Episteme example — model evaluation result

Consider `ModelEvaluationResultKind` as an episteme kind:

* `DescribedEntitySlot` — the model being evaluated
  – ValueKind: `U.Method` (intensional ML model).
  – RefKind: `U.MethodRef` (id of `Model_v3`).

* `DatasetSlot` — the dataset on which it is evaluated
  – ValueKind: `U.Entity` (EoIClass = “Dataset”).
  – RefKind: `U.EntityRef` (e.g. `Dataset_A`, `Dataset_B`).

* `TargetCharacteristicSlot` — the characteristic being measured
  – ValueKind: `U.Characteristic` (`Accuracy`, `F1`, `AUROC`).
  – RefKind: `U.CharacteristicRef`.

* `GroundingHolonSlot` — evaluation environment
  – ValueKind: `U.Holon` (e.g. `EvalCluster#1`).
  – RefKind: `U.HolonRef`.

* `ClaimGraphSlot` — evaluation result graph
  – ValueKind: `U.ClaimGraph`.
  – refMode: `ByValue`; the numeric thresholds and results live inside `content : U.ClaimGraph`.

Typical moves:

* `DatasetSlot`: **retarget** `Dataset_A` → `Dataset_B` to test generalisation.
* `TargetCharacteristicSlot`: **retarget** `Accuracy` → `F1` to focus on class imbalance.
* `ClaimGraphSlot`: **by‑value edit** thresholds from “`P95Latency ≤ 200 ms`” to “`≤ 150 ms`” — a `ByValue` content edit, not a ref retargeting.

The SlotKind/ValueKind/RefKind discipline makes these moves **local and explicit**: the pattern describes which moves are allowed where, and A.6.2–A.6.4 then constrain how episteme morphisms may change ClaimGraphs and references.

#### A.6.5:5.3 - Didactic micro‑examples — substitution by SlotKind / ValueKind / RefKind *(informative)*

The following short examples are intended for a didactic guide or for cross‑references from A.6.0/A.6.x/C.2.1. In all of them:

* **SlotKind** names the **place/position in the structure** (slot/field/coordinate in a tuple/record/port bundle).
* **ValueKind** is the **kind of value** admissible at that place.
* **RefKind** is the **reference/identifier type** used in episteme when that slot is filled (absent when the slot is by‑value).
* `GroundingHolon` is **not** a separate kernel type: it is simply a `U.Holon` used as the ValueKind of `GroundingHolonSlot`.

Example names like `FurnitureSafetyDescriptionKind`, `AuthPipelineSpecKind`, `ModelEvaluationResultKind`, `IncidentRunbookSpecKind`, `ServiceSLARequirementKind` are **context‑local** kinds, not new kernel tokens.

##### A.6.5:5.3.1 - Mechanics — stool on a test rig

*EpistemeKind:* `FurnitureSafetyDescriptionKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — SlotKind “what this description is about”; ValueKind `U.Entity` with EoIClass ⊑ `U.Holon` (stool as a furniture holon); RefKind `U.EntityRef` (identifier of a concrete stool `S_i`).
* `GroundingHolonSlot` — SlotKind “where the test happens”; ValueKind `U.Holon` (test rig `LabRig_j`); RefKind `U.HolonRef`.
* `ClaimGraphSlot` — SlotKind for the internal content; ValueKind `U.ClaimGraph`; refMode `ByValue` (graph embedded in the episteme).

*Substitutions (all under the **same** SlotKinds):*

* Episteme `E₁`: `describedEntityRef = S_1`, `groundingHolonRef = LabRig_A`.
* Episteme `E₂`: `describedEntityRef = S_2`, `groundingHolonRef = LabRig_A` — **substitute another stool in the same `DescribedEntitySlot`** (different `U.EntityRef` slot‑content).
* Episteme `E₃`: `describedEntityRef = S_1`, `groundingHolonRef = LabRig_B` — **substitute another test rig in `GroundingHolonSlot`** while keeping the same `DescribedEntitySlot` occupant.

In all three cases the SlotKinds (and ValueKinds) are stable; only the **Refs that fill those slots** change. This matches the engineering idiom “drop another module into the same slot”.

##### A.6.5:5.3.2 - Microservices — switching the authentication provider

*EpistemeKind:* `AuthPipelineSpecKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Holon` with EoIClass = “`UserService` holon”; RefKind `U.HolonRef` (e.g. `UserService#prod`).
* `AuthProviderComponentSlot` — SlotKind “which auth provider component is used in this pipeline”; ValueKind `U.Holon` with EoIClass = “`AuthProviderSystem` holon”; RefKind `U.HolonRef` (e.g. `Auth_OIDC`, `Auth_LDAP`).
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue` (pipeline invariants and flow logic).

*Substitutions / retargetings:*

* Episteme `Spec_OIDC`: `describedEntityRef = UserService#prod`, `authProviderComponentRef = Auth_OIDC`.
* Episteme `Spec_LDAP`: same `describedEntityRef = UserService#prod`, but `authProviderComponentRef = Auth_LDAP`.

Here SlotKind is identical (`AuthProviderComponentSlot`); ValueKind is “any auth‑provider holon”; the episteme change is purely a **retargeting** of the `U.HolonRef` slot‑content.

##### A.6.5:5.3.3 - Data/ML — swapping dataset or target characteristic

*EpistemeKind:* `ModelEvaluationResultKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Method`; RefKind `U.MethodRef` (e.g. `Model_v3`).
* `DatasetSlot` — ValueKind `U.Entity` with EoIClass = “dataset”; RefKind `U.EntityRef` (`Dataset_A`, `Dataset_B`, …).
* `TargetCharacteristicSlot` — ValueKind `U.Characteristic`; RefKind `U.CharacteristicRef`.
* `GroundingHolonSlot` — ValueKind `U.Holon`; RefKind `U.HolonRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`.

*Substitutions / retargetings:*

* `Eval_1`: `describedEntityRef = Model_v3`, `datasetRef = Dataset_A`, `targetCharacteristicRef = Accuracy`, `groundingHolonRef = EvalCluster#1`.
* `Eval_2`: same model / characteristic / cluster, but `datasetRef = Dataset_B` — **substitute another dataset in `DatasetSlot`** (retarget the dataset ref).
* `Eval_3`: same model and dataset, but `targetCharacteristicRef = F1` — **substitute another characteristic in `TargetCharacteristicSlot`**.

##### A.6.5:5.3.4 - Operational practice — the same runbook in different operating centres

*EpistemeKind:* `IncidentRunbookSpecKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Method`; RefKind `U.MethodRef`.
* `GroundingHolonSlot` — ValueKind `U.Holon`; RefKind `U.HolonRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`.

*Substitutions / retargetings:*

* `Runbook_DC1`: `describedEntityRef = MajorIncidentRunbook`, `groundingHolonRef = DC1_NOC`.
* `Runbook_DC2`: same `describedEntityRef`, but `groundingHolonRef = DC2_NOC`.

This is “one and the same method is specified and validated in two different operational environments”: SlotKind and ValueKind are stable; only the `U.HolonRef` slot‑content differs.

##### A.6.5:5.3.5 - SLO/SLA requirements — changing the target characteristic vs changing the threshold

*EpistemeKind:* `ServiceSLARequirementKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Holon`; RefKind `U.HolonRef` (e.g. `CheckoutService#prod`).
* `TargetCharacteristicSlot` — ValueKind `U.Characteristic`; RefKind `U.CharacteristicRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`. Numeric thresholds live **inside the ClaimGraph as literals**, not as RefKinds.

*Moves:*

* `SLA_latency_200`: `describedEntityRef = CheckoutService#prod`, `targetCharacteristicRef = P95Latency`; ClaimGraph contains `P95Latency ≤ 200 ms`.
* `SLA_latency_150`: same refs, but ClaimGraph threshold is `P95Latency ≤ 150 ms`. This is a **by‑value edit** of `ClaimGraphSlot`.
* `SLA_availability_99_9`: same `describedEntityRef`, but `targetCharacteristicRef = Availability`; ClaimGraph states `Availability ≥ 99.9%`. This is a **retargeting** of `TargetCharacteristicSlot`.

### A.6.5:6 - Bias‑Annotation

**Lenses tested and scope.** This pattern was read through all five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`) and is intended as a **universal** discipline for n‑ary relation and morphism signatures across Parts A/B/C/E. It leans toward the `Arch` and `Onto/Epist` lenses (typed signatures, explicit kinds), but mitigates this by (a) keeping the discipline notation‑agnostic, (b) aligning with existing tooling rather than prescribing any, and (c) grounding the rules in System/Episteme examples with clear didactic intent. No domain‑specific scope limitation is claimed.

* **Typed‑language bias.**

  * The pattern leans on intuitions from typed programming languages (parameter types, records, references). This is intentional: it aligns FPF signatures with mainstream tooling and with post‑2015 typed effect/row systems. The pattern remains **notation‑agnostic** and does not commit to any specific PL or logic.

* **Slot‑first bias.**

  * We treat *slot* as the primary abstraction and discourage role‑style or object‑style naming for argument positions. This favours structural clarity over conversational metaphors (“subject/object/role”) and keeps `U.Role` free for RoleEnactment rather than param‑slots.

* **By‑value/by‑ref honesty.**
  We explicitly separate ValueKind and RefKind instead of hiding “by‑reference” behind the type system. This increases verbosity but makes reasoning about edition pinning, caching, and re‑targeting more robust, and keeps I/D/S distinctions visible inside signatures.

* **Lexicon bias (precision over metaphor).**
  We standardise the slot‑operation lexicon (bind/fill/initialize/assign/retarget/resolve/mutate) and discourage metaphors that smuggle role semantics back into SlotKinds. This increases didactic load, but directly reduces cross‑pattern ambiguity, especially in “binding time” discussions.

* **Episteme‑first describedEntity.**
  The examples and cross‑references prioritise episteme use‑cases (C.2.1, A.6.2–A.6.4) where describedEntity and retargeting are subtle. System‑only usages (e.g. method signatures) are absolutely allowed but not the driving case; they inherit the same discipline without additional obligations.

### A.6.5:7 - Conformance Checklist (normative)

**CC‑A.6.5‑1 - SlotSpec for every parameter.**
Every `U.Signature` that declares an n‑ary relation or morphism **SHALL** assign to each parameter position a SlotSpec triple: `⟨SlotKind, ValueKind, refMode⟩`.

**CC‑A.6.5‑2 - `*Slot` discipline.**
Any Tech name ending with `…Slot` **MUST** denote a SlotKind; SlotKinds **MUST NOT** be used as ValueKinds or RefKinds.

**CC‑A.6.5‑3 - `*Ref` discipline.**
Any Tech name ending with `…Ref` **MUST** denote either a RefKind or a field whose type is a RefKind. ValueKinds and SlotKinds **MUST NOT** end in `…Ref`.

**CC‑A.6.5‑4 - ValueKind purity.**
ValueKinds **MUST** be declared without `*Slot`/`*Ref` suffixes and **MUST** be FPF types (often `U.Kind` or kernel‑level types). Any existing type whose name violates this rule must be either:

* reclassified as a RefKind, or
* renamed to drop the suffix.

**CC‑A.6.5‑5 - Episteme core SlotKinds.**
For episteme kinds (`U.EpistemeKind`), the following SlotKinds **SHALL** be used (or their documented refinements) in C.2.1 / C.2.x:

* `DescribedEntitySlot` with ValueKind `U.Entity` **or a declared subkind** (e.g. `U.Method`, `U.Holon`) via Kind‑CAL (EoIClass ⊑ `U.Entity` at species level);
* `GroundingHolonSlot` with ValueKind `U.Holon`;
* `ClaimGraphSlot` with ValueKind `U.ClaimGraph` and `ByValue` mode in the minimal core;
* `ViewpointSlot` with ValueKind `U.Viewpoint`;
* `ViewSlot` with ValueKind `U.View` (`U.EpistemeView`);
* `ReferenceSchemeSlot` with ValueKind `U.ReferenceScheme` and `ByValue` mode in the minimal core.

**CC‑A.6.5‑6 - No “Role” as SlotKind head.**
SlotKinds **MUST NOT** use “Role” as their head noun; use “Slot” with a neutral qualifier instead (e.g., `EnactorHolonSlot`). `U.Role` remains reserved for RoleEnactment patterns.

**CC‑A.6.5‑7 - Substitution checks.**
Any pattern that describes substitution or replacement of arguments **MUST** phrase its rules in terms of SlotKinds and ValueKinds (and, where relevant, RefKinds), not in terms of unstructured parameter indices or ad‑hoc labels.

**CC‑A.6.5‑8 - Cross‑pattern consistency.**
When the same conceptual position is used across patterns (e.g. “describedEntity target”, “grounding holon”, “caller system”), the **same SlotKind name** and ValueKind **SHALL** be reused, unless a documented Bridge declares a different discipline or the pattern explicitly scopes itself to a distinct calculus.

**CC‑A.6.5‑9 - Migration of legacy `…Ref`/`…Slot` usage.**
Contexts adopting this pattern **MUST** maintain a migration table for legacy types/fields whose names contain `Ref` or `Slot` but do not comply with the new discipline. Each entry shall state:

* old name and role,
* new SlotKind/ValueKind/RefKind,
* whether the old name becomes an alias (deprecated) or is removed.

**CC‑A.6.5‑10 - Pattern integration.**
New or revised patterns in Part A/B/C/E that introduce n‑ary relations, morphisms, or signatures **SHALL** reference A.6.5 in their Relations section and attest that they follow SlotKind/ValueKind/RefKind discipline.

**CC‑A.6.5‑11 - Slot‑content terminology.**
Normative text that refers to “what is in a slot” **SHALL** use **slot‑content** (or **slot filler**) and **SHALL NOT** rely on role/person metaphors (e.g. “occupant”) unless explicitly defined as a strict synonym for slot‑content with no added semantics.

**CC‑A.6.5‑12 - Slot‑operation verb discipline.**
Any normative description of a change “to a slot” **MUST** specify which operation class it is (initialize vs assign/set vs retarget vs by‑value edit vs resolve vs mutate/revise), using the canonical verbs in A.6.5:4.5.2 or explicitly mapping local terms to them.

**CC‑A.6.5‑13 - Binding‑time clarity.**
Any use of “early binding / late binding” (or equivalent) **MUST** specify whether it refers to:

* Identifier binding (name‑binding),
* Slot filling (early/late‑filled),
* Reference resolution / dispatch (eager/lazy‑resolved).

### A.6.5:8 - Consequences

**Benefits**

* **Uniform language for arguments and for operations.**
  Any n‑ary relation (episteme, role, method, service, guard) can be described with the same SlotKind/ValueKind/RefKind triple **and** with a stable operation lexicon (fill/initialize/assign/retarget/resolve).

* **Safer substitutions.**
  Substitution, retargeting, and viewing laws (A.6.2–A.6.4) can be stated in terms of *which SlotKinds* they read/write and *which ValueKinds* they preserve or retarget, without accidentally collapsing into “just replace the thing”.

* **Cleaner naming and migration.**
  Misuses of `*Ref`, `*Slot`, “Role”, “Subject”, “Object” in signatures become guard‑detectable; migration strategies can be described as re‑factoring SlotKinds and ValueKinds rather than ad‑hoc renames.

* **Tool alignment.**
  Implementation languages with **row‑typed records, dependent types, and algebraic effects** map naturally to the SlotKind/ValueKind/RefKind layers, easing code generation and static analysis. ([13])

**Trade‑offs / mitigations**

* **Extra metadata in signatures.**
  Every parameter now has three pieces of information instead of one. Mitigation: template support in authoring tools; pattern‑guided macros for common shapes (episteme, role, method, service).

* **Stricter lexical rules.**
  Some legacy names will need migration (`EpistemicObject`, ad‑hoc `…Ref` types). Mitigation: migration notes in F.18 and dedicated anti‑pattern sections; transitional aliases allowed but marked deprecated.

* **Learning curve.**
  Authors must learn to think “SlotKind/ValueKind/RefKind” *and* distinguish “retarget vs edit vs resolve” before writing `id` or `subject`. Mitigation: Tell‑Show‑Show examples and a didactic micro‑guide on slot operations referenced from A.6.0/C.2.1/E.17.0.

### A.6.5:9 - Rationale

**Why a SlotKind/ValueKind/RefKind triple at all.**
In FPF this pattern makes `U.Signature` behave like a lightweight dependently‑typed record discipline: SlotKind plays the role of an index or label, ValueKind is the family of admissible fillers at that position, and RefKind captures the representation choice (by‑value or via a handle). This mirrors the way post‑2015 work on row‑polymorphic data and effect rows treats labels and field kinds as first‑class, while keeping the Core notation‑neutral.

**Why separate ValueKind from RefKind.**
In practice, “Ref” types tend to be quietly used as if they were values, eroding the I/D/S split and making edition discipline invisible. By insisting that ValueKind is always the conceptual kind (“what sort of thing is this about?”) and RefKind is always the reference/identifier kind (“how do we point at it in Episteme?”), the pattern aligns with E.10.D2’s intension/description/specification discipline and with modern resource‑aware logics that keep values and resources distinct.

**Why add a slot‑operation lexicon.**
The triple only buys safety if authors and tools can see it at a glance **and** can narrate changes without collapsing layers. A.6.5:4.5 makes the common “put something in a slot” moves explicit: initialization vs assignment vs retargeting vs by‑value editing vs resolution. This directly reduces ambiguity in episteme morphism descriptions (A.6.2–A.6.4) and prevents accidental imports from a specific PL’s terminology.

**Why standardise episteme SlotKinds.**
describedEntity and grounding recur across epistemes; standard SlotKinds (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, etc.) let A.6.2–A.6.4 and C.2.1 talk about substitutions and retargetings once, instead of re‑defining “what this is about” in every pattern.

**Why lexical rules (`*Slot`, `*Ref`, operation verbs, no “Role” heads).**
The discipline must be cheap to apply. Reserving `*Slot` for SlotKinds and `*Ref` for RefKinds/fields gives a syntax‑level guard against conflating places, kinds, and handles. Standardising operation verbs (initialize/retarget/resolve) prevents prose from re‑introducing the same conflation by different words.

### A.6.5:10 - SoTA‑Echoing (post‑2015 practice alignment)

**Purpose.** To situate SlotKind/ValueKind/RefKind discipline with respect to contemporary typed and relational approaches, without importing any external calculus into the Core. All items are used as conceptual comparators; concrete reuse in a `U.BoundedContext` would happen only via explicit Bridges (F.9) with declared CL penalties.

1. **Row‑typed, extensible data / effect rows (adopt/adapt).**
   Post‑2015 work on row polymorphism and extensible data/effect rows treats records and variants as labelled collections of fields whose presence and type can evolve independently.
   **Adopted:** the idea that **positions** (labels) are first‑class and carry their own typing discipline.
   **Adapted:** instead of row kinds, FPF uses SlotKind/ValueKind/RefKind triples for n‑ary relations and epistemic slots; the pattern is notation‑agnostic and applies equally to episteme structures, role relations, and service signatures. ([13])

2. **Dependent type systems engineered via macros (adopt/adapt).**
   Macro‑based dependent type systems such as Turnstile+ separate structural indices, value‑level types, and evidence, while allowing them to be related by construction.
   **Adopted:** the separation between **indices/labels** and **values**, and the intuition that signatures should expose both explicitly.
   **Adapted:** SlotKind corresponds to a structural index, ValueKind to the ordinary type of fillers, and RefKind to runtime‑level identifiers; the discipline is phrased at the FPF specification and kept independent of any particular PL.

3. **Relational models of types‑and‑effects (adapt).**
   Relational models for types‑and‑effects distinguish value positions from effect/resource annotations and track substitution separately across these layers.
   **Adopted:** the insistence that reasoning about **substitution and equality** must be stratified (values vs additional structure).
   **Adapted:** A.6.5 stratifies *slot / value / reference* instead of *value / effect*, and applies the discipline not only to programs but also to epistemes, roles, methods, and services. ([15])

4. **Optics / lenses as disciplined projections (echo).**
   Profunctor optics formalise get/put pairs where a fixed “focus” position within a larger structure is manipulated under composition laws.
   **Echoed:** SlotKind plays the role of the focus coordinate; ValueKind is the focus type; RefKind determines whether the focus is stored by value or via a handle. This perspective informs later use of SlotKind discipline in EpistemicViewing (A.6.3) and multi‑view publication (E.17). ([16])

**Cross‑Context reuse and Bridges.** When a `U.BoundedContext` chooses to adopt a concrete row‑typing discipline, relational logic, or optics library, it **SHALL** do so via explicit Bridges (F.9) with CL and (for plane crossings) `Φ(CL)`/`Φ_plane` policy‑ids, keeping numerical policies and notations Context‑local. A.6.5 only constrains the **slot discipline** that such Bridges must respect.

### A.6.5:11 - Relations (with other patterns)

**Specialises A.6.P `U.RelationalPrecisionRestorationSuite`.**
A.6.5 is the RPR specialisation for “n‑ary relation as slots”: it restores hidden arity by making participant positions explicit as SlotKinds, and stabilises change semantics via the slot‑operation lexicon + lexical guards.


**Builds on A.6.0 `U.Signature`.**
Refines parameter declarations with SlotSpec triples `⟨SlotKind, ValueKind, refMode⟩` while leaving the rest of the signature structure (SubjectKind, BaseType, Quantification, ResultKind, Laws) unchanged. SlotKinds become the canonical labels for argument positions.

**Constrains C.2.1 `U.EpistemeSlotGraph`.**
Fixes core episteme SlotKinds (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) and their ValueKinds/`ByValue` vs Ref discipline. C.2.1 and its extensions SHALL use these SlotKinds (or documented refinements) so that episteme morphisms can be expressed uniformly over slots.

**Supports A.6.2–A.6.4 (episteme morphisms and viewing).**
DescribedEntity‑preserving vs describedEntity‑retargeting morphisms can now be stated as constraints on which SlotKinds’ ValueKinds/RefKinds they may change. Retargeting becomes “retargeting at `DescribedEntitySlot` under a Kind‑Bridge” rather than an ad‑hoc parameter tweak. The operation lexicon in A.6.5:4.5 makes “retarget vs edit vs resolve” explicit in these morphism descriptions.

**Coordinates with B.5.* (RoleEnactment).**
Role/assignment relations may declare SlotKinds such as `HolderHolonSlot`, `RoleSlot`, `ContextSlot`, `WindowSlot` with clear ValueKinds/RefKinds, instead of overloading “role” for both holonic roles and relation positions. This keeps `U.Role` semantics (A.2, F.6) separate from slot discipline.

**Coordinates with E.17 `U.MultiViewDescribing`.**
`Viewpoint` and `View` positions are governed by SlotKind/ValueKind/RefKind; view‑changing operations can be described as substitutions at specific SlotKinds that preserve ClaimGraph content while re‑indexing viewpoints and views.

**Feeds F.18 (LEX‑BUNDLE) and E.10 (LEX).**
Provides lexical guards for `*Slot` and `*Ref`, and (via A.6.5:4.5) for operation verbs:

* `*Slot` reserved for SlotKinds only;
* `*Ref` reserved for RefKinds and reference fields;
* ValueKinds and Kind names MUST NOT carry either suffix;
* slot‑operation verbs must not collapse retargeting into “editing”.

**Used by A.19 `CharacteristicSpace` and measurement patterns.**
Characteristic‑space slots already behave as positions with attached kinds; slot discipline in A.6.5 gives a uniform story for how such slots appear inside relation signatures, episteme cards, and service definitions, and how substitution over those slots is checked.

[13] https://dl.acm.org/doi/pdf/10.1145/3290325
[14] https://www.williamjbowman.com/resources/wjb2019-depmacros.pdf
[15] https://iris-project.org/pdfs/2017-popl-effects-final.pdf
[16] https://arxiv.org/pdf/1809.00738

### A.6.5:End

## A.6.6 - U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)

**Plain-name.** Scoped witnessed base declaration discipline.

**Status.** Normative (Core).

**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; adjacent to A.6.5 `U.RelationSlotDiscipline`.

**Depends on.**
– A.6.0 `U.Signature` (universal signature carrier).
– A.6.5 `U.RelationSlotDiscipline` (SlotKind/ValueKind/RefKind stratification + slot-operation lexicon).
– A.2.6 (Scope discipline; explicit `Γ_time`; implicit “latest/current” is forbidden).
– A.2.4 `U.EvidenceRole` (timespan + evidence-role discipline for decision-relevant witness sets).
– A.7 (Strict Distinction; I/D/S vs Surface).
– E.8 (pattern authoring order & SoTA discipline).
– E.10 (LEX‑BUNDLE discipline; D.CTX lexical guardrails).

**Coordinates with.**
– A.10 Evidence–Provenance DAG discipline (`verifiedBy`, `validatedBy`).
– A.14 per-edge constructive grounding (`tv:groundedBy`) and `validationMode` discipline.
– C.2.1 `U.EpistemeSlotGraph` grounding slots (`GroundingHolonSlot`, `describedEntity`).
– A.6.3 `U.EpistemicViewing` (describedEntity-preserving view operators; base-relative “how” without retargeting).
– A.6.4 `U.EpistemicRetargeting` (base-change along `KindBridge`; retargeting lexicon and continuity rules).
– C.3.3 `U.KindBridge` & `CL^k` (explicit repair/translation when endpoint kinds or Contexts differ; no silent re-typing).
– E.18 assurance-operations on `U.Transfer` (`CalibrateTo`, `CiteEvidence`, `AttributeTo`, `ConstrainTo`, …).
– F.9 Bridges & CL (cross-context and cross-plane base declarations cite Bridge ids + CL policy).
– F.15 F‑Suite validation harness (SCR/RSCR pins and refresh governance).
– F.18 naming governance (surface rules for Tech/Plain twins).

**Aliases (informative; discouraged for normative prose).**
– “anchoring / anchor” (legacy umbrella colloquial; a red‑flag token for *under-described dependence*). **Prohibited in Tech register** as a meaning‑surrogate; treat it as a defect to be rewritten into an explicit `baseRelation(dependent, base)` form. Allowed only when referring to a **pattern-defined primitive** that already reserves the word (e.g., E.10 MG‑DA *Domain Anchoring*; evidence/pin “anchors” where the term is explicitly reserved), or inside quoted legacy text that is immediately followed by a conformant rewrite.
– “Qualified statement / attributed edge” (knowledge-graph colloquial).
– “Pinning” (when witnesses are edition pins).

**Mint‑or‑Reuse note (informative).**
This pattern **mints** the record shape name `U.ScopedWitnessedBaseDeclaration` (SWBD) and the **base‑change lexicon** operation class names (`declareBase`, `rebase`, `retime`, …) as canonical labels for semantic change classes.
It **reuses** A.6.5 SlotSpec discipline (SlotKind/ValueKind/RefMode), A.2.6 Scope discipline (`U.Scope`, explicit `Γ_time` when time matters), and A.2.4 witness semantics (`U.EvidenceRole`) as the enforcement substrate.

### A.6.6:1 - Problem frame

FPF repeatedly needs to express a family of situations of the form:

> **A dependent content is admissible, usable, or interpretable only relative to an explicit base.**

This family appears across disciplines:

* reference selection and identification (IDs, handles, pointers, registries),
* scale/datums/calibration (measurement traceability, baselines, normalisation),
* grounding of properties and abstractions to objects (attribution; “this property is about that thing”),
* admissibility/assurance (claims linked to evidence, checks, or proofs),
* publication discipline (what a statement is fit to be used for, where, and when).

In drafts, authors often reach for a single umbrella metaphor (frequently “anchor/anchoring”). That metaphor collapses **different ontological situations** and **different operation classes**, blocking precise invariants and making perspective-flips inevitable.

> **Deconfliction note (lexical).** This pattern is about *base-dependence in content* (“X is usable relative to B”). It is not about E.10’s **Domain Anchoring** (MG-DA), where “anchoring” is a *lexical* primitive for binding token morphology to the term’s described entity. When you see `anchor*` in a basedness sentence, treat it as a defect unless an explicit baseRelation token is present.
>
> **Deconfliction note (context/meaning).** This pattern is also not a license to reintroduce “anchor” as a surrogate for **Context**, **SenseCell**, or “where meaning lives”. Any such use is an *anchor‑relapse* and SHALL be rewritten into explicit Context/SenseCell/ConceptSet lane constructs (E.10 D.CTX), not into SWBD.

Like A.6.5, this family also triggers **typing conflicts across viewpoints**: an endpoint may be spoken about in its self-kind while the baseRelation declaration expects a different ValueKind (or a different `refMode`). If that mismatch is not made explicit (SlotSpec + relation-specific constraints), authors “solve” it by renaming ends or flipping direction, and the ontological obligation (bridge / narrowing / retargeting) is lost.

The structural reason for the collapse is consistent: what looks like “one anchoring” in prose is, in fact, a *based declaration* with at least five components:

1) **Dependent** — what is being made admissible/usable/meaningful,
2) **Base** — what it is relative to: reference frame, evidence carrier, standard, policy, or declared entity,
3) **BaseRelation** — the specific relation kind that states *how* dependent depends on base,
4) **Scope/Time** — where/when the declaration holds (`scope` plus explicit `Γ_time` when time matters),
5) **Witnesses / pins** — what justifies or enforces the declaration when it is used for decisions.

Until **BaseRelation** is named, umbrella words (“anchor”, “ground”, “attach”, “based on”) nearly always mean:

> “There is an under-described type of dependence here.”

This pattern introduces a single stable lens — **the based declaration** — and couples it with a strict lexical discipline and an operation lexicon, so that base-dependence can be expressed precisely across domains without collapsing back into metaphor.

### A.6.6:2 - Problem

Typical failure modes this pattern is designed to eliminate:

1. **Relation-kind elision.**
   One verb phrase is used to cover: ID-to-registry reference, claim-to-evidence admissibility, calibration-to-standard, property-to-object attribution, policy gating, etc. Rules and invariants cannot be stated because the relation family is unspecified.

2. **Perspective flip (dependent-view vs base-view).**
   The same situation is described alternately as “X is anchored/grounded” and “Y is an anchor/ground”, with incompatible naming, hidden directionality, and silent re-typing of the ends.

3. **Base–witness confusion.**
   Evidence, pins, certificates, or proofs are treated as “the base”, even when they are only witnesses for a base relation (or conversely: a true base is treated as a mere witness).

4. **Scope/time collapse.**
   Based declarations are treated as timeless truths; time dependence is smuggled in via “current/latest/recently”, violating explicit `Γ_time` discipline.

5. **`Γ_time` used as a proxy for freshness.**
   Authors treat `Γ_time` as “freshness” or “evidence decay”, collapsing TimePolicy with witness-timespan/freshness predicates.

6. **Decision use without witnesses.**
   Declarations that gate work, publication, or assurance are asserted without a witness/pin, breaking auditability and enabling folklore.

7. **Grounding conflation.**
   “Grounding” is used as if it were one relation, while FPF already distinguishes at least:
   * constructive grounding of a model-edge by a trace (`tv:groundedBy`),
   * situational/empirical grounding of an episteme via a grounding holon (C.2.1),
   * semantic meaning assignment (SenseCell/ConceptSet lane; not a base declaration).

8. **Slot/basing conflation.**
   A.6.5 disambiguates positions in n-ary relations (SlotKind) vs fillers (ValueKind) vs stored references (RefKind). Umbrella basing language reintroduces confusion at the next layer: “why this link exists” (BaseRelation) is missing, and slot-edit operations are conflated with base-declaration edits.

9. **Anchor relapse (Context/meaning surrogate).**
   “Anchor/anchoring” is used to mean “the context”, “the meaning”, “the global reference”, or “the thing that makes this true”. This collapses D.CTX + SenseCell/ConceptSet lanes into a metaphor and makes review/tooling impossible.

### A.6.6:3 - Forces

| Force | Tension |
| --- | --- |
| **Universality vs precision** | One discipline must cover calibration, evidence linking, reference selection, attribution, gating, etc., without collapsing them into one pseudo-relation. |
| **Minimal kernel vs decision auditability** | Few primitives are preferred, but decision-relevant declarations must carry witnesses/pins and explicit time selectors where needed. |
| **Two perspectives, one reality** | Dependent-view and base-view must both be expressible without renaming roles or flipping meaning. |
| **Compatibility with A.6.5** | Base declarations introduce slots and edits; they must remain SlotKind/ValueKind/RefKind disciplined and must not collapse slot edits with semantic re-declarations. |
| **Lexical guardrails** | Without strict wording rules, umbrella metaphors will return and erase the structure. |
| **Cross-context integrity** | When dependent and base cross Contexts or planes, the declaration must remain explicit and reviewable; no silent semantic drift. |

### A.6.6:4 - Solution — The `U.ScopedWitnessedBaseDeclaration` object and its lexicon

#### A.6.6:4.1 - Canonical object

**Definition.** A **`U.ScopedWitnessedBaseDeclaration`** (SWBD) is a first-class base-declaration record *shape* (a signature in the A.6.0/A.6.5 sense): it reifies “dependent is usable relative to base via baseRelation, under scope/time, witnessed by pins”.

```
U.ScopedWitnessedBaseDeclaration ::=
  〈 * DependentSlot     : SlotContent(VK_dep,  refMode_dep),
    * BaseSlot          : SlotContent(VK_base, refMode_base),
    * BaseRelationSlot  : SlotContent(U.NameToken, ByValue),     // relation-specific token; not free text; not U.Surface*
    * ScopeSlot         : SlotContent(U.Scope, ByValue),         // concretely: ClaimScope | WorkScope | PublicationScope
    * GammaTimeSlot?    : SlotContent(U.GammaTimePolicy, ByValue)?,
    * WitnessSetSlot?   : SlotContent(VK_wit,  refMode_wit)? 〉
 ```

Where:

* **`DependentSlot`** is the dependent content whose admissibility/usability/interpretation is being constrained.
* **`BaseSlot`** is the base, such as a reference frame, target, declared entity, standard, policy, or evidence carrier, that the dependent is declared relative to.
* **`BaseRelationSlot`** is a **declared relation/predicate/operator token** (a vocabulary element with a signature and relation-specific constraints) that states the precise kind of dependence. It is not a prose metaphor and is not a `U.Surface`/publication carrier.
* **`ScopeSlot`** is an explicit USM scope object (`U.Scope`): Claim scope (**G**), Work scope, or Publication scope.
* **`GammaTimeSlot`** is an explicit time selector/policy when time-dependent assumptions exist.
* **`WitnessSetSlot`** is a set of witness references/pins establishing justification or enforcement when the declaration is used for decisions.

**Notation.** `SlotContent(VK, refMode)` is a compact shorthand for “a slot whose SlotSpec declares `ValueKind=VK` and `refMode ∈ {ByValue | RefKind}` (A.6.5)”.

**SlotSpec note.** `VK_*` / `RK_*` / `refMode_*` above are **not** “anything goes”: they are fixed by the chosen `BaseRelationSlot` vocabulary entry and must be declared as SlotSpecs (A.6.5). In other words, SWBD is a reusable *shape*, but each Context’s baseRelation family makes it a concrete, typed signature.

**Instance/prose notation note (convention).** In the prose and examples below, the *occupants* are written as `dependent`, `base`, `baseRelation`, `scope`, `Γ_time`, `witnesses` (no `*Slot` suffix). The `*Slot` suffix is reserved for SlotKinds/positions only (A.6.5 / E.10).

**Well-formedness constraints.**
* **WF‑BD‑1 (No kind-elision).** A base declaration is well-formed only if `BaseRelationSlot` is present and points to a declared vocabulary element with a known signature.
* **WF‑BD‑2 (No silent re-typing).** `DependentSlot` and `BaseSlot` type-check against the `baseRelation` vocabulary entry (ValueKinds + `refMode`). If the intended endpoint kinds do not match, the repair path is explicit (Bridge / narrowing / explicit retargeting), rather than a rename.
* **WF‑BD‑3 (Time explicit when time matters).** If the declaration’s interpretation depends on time, `GammaTimeSlot` is explicit; “latest/current” is not a substitute.
* **WF‑BD‑4 (Decision use requires witnesses).** If the declaration is used for assurance, gating, or admissibility decisions, `WitnessSetSlot` is non-empty and resolvable.
* **WF‑BD‑5 (Edition fence for decision/publication).** An SWBD that is cited by PublicationScope or used for decision is immutable per edition: any permitted change class is represented as a new declaration linked via explicit continuity/withdrawal, not as an in-place rewrite.
* **WF‑BD‑6 (No silent cross-context reuse).** An SWBD that relates dependent and base across Contexts/planes (or requires scope translation) is admissible only if it cites the Bridge ids + CL policy that make the reuse admissible (F.9). No informal “it is the same entity anyway” prose is an admissible substitute.

This is the discipline-level analogue of A.6.5’s move: disambiguation is achieved by making the missing structural component explicit and non-optional in decision-relevant contexts.

#### A.6.6:4.2 - Underlying mathematical lens

SWBD reifies a **kind-labelled dependence arrow over a base**:

* a dependence edge **(dependent → base)**,
* labelled by a declared **relation token** (`baseRelation`),
* qualified by explicit **scope** and (when time matters) explicit **`Γ_time`**,
* optionally supported by a **witness set** (mandatory for decision use).

This “object over a base” lens is stable across disciplines:
calibration is “measurement over standard”, admissibility is “claim over evidence”, attribution is “property over object”, and constructive grounding is “edge over trace”.

#### A.6.6:4.3 - Slot discipline for SWBD

Any signature that introduces SWBD (or SWBD-like relations) SHALL define SlotSpecs per A.6.5: every position declares **SlotKind / ValueKind / RefKind-or-ByValue**.

Recommended canonical SlotKinds for SWBD:

* `DependentSlot`
* `BaseSlot`
* `BaseRelationSlot`
* `ScopeSlot`
* `GammaTimeSlot`
* `WitnessSetSlot`

**Slot vs filler guard.** `*Slot` names the **position** (SlotKind), not the occupant. In prose, say “fills `BaseSlot` with …” rather than calling the base itself “a BaseSlot”. (`Slot` suffix is structural; E.10.)

**Slot-level invariants (derived from WF‑BD‑1..4; testable).**
* **Invariant (SlotSpec completeness).** In any SWBD signature, the SlotSpec for `DependentSlot` and `BaseSlot` declares admissible `ValueKind` and `refMode` explicitly (A.6.5). If those types cannot be stated, the `baseRelation` vocabulary entry is not yet defined.
* **Invariant (Relation tokenness).** `BaseRelationSlot` holds a declared `U.NameToken` that resolves to a vocabulary entry with a known signature and relation-specific constraints (A.6.0 + A.6.5). It is not free text and is not typed as a publication surface (`U.Surface*`).
* **Invariant (Scope objectness).** `ScopeSlot` holds a `U.Scope` object (ClaimScope/WorkScope/PublicationScope) and is not replaced by “where it applies” prose.
* **Invariant (Time gating).** If time-dependent assumptions exist, the SWBD includes `GammaTimeSlot` carrying a `U.GammaTimePolicy` (WF‑BD‑3).
* **Invariant (Witness gating).** If the declaration participates in assurance/gating/admissibility decisions, the SWBD includes a non-empty, resolvable `WitnessSetSlot` (WF‑BD‑4).

**Field naming guard (implementation; informative).** When materialising SWBD as a record/card, implementations SHOULD avoid naming data fields with the `*Slot` suffix. Prefer `dependentRef`, `baseRef`, `baseRelationRef`, `scope`, `gammaTime`, `witnesses` (or Context‑local equivalents). `*Slot` remains reserved for SlotKinds/SlotSpecs (A.6.5).

#### A.6.6:4.4 - BaseRelation declaration

A `baseRelation` token is not “just a label”. For each baseRelation declared in a Context, its definition SHALL include:

* **Role polarity.** Which end is dependent and which end is base (or declare symmetry explicitly).
* **Typing expectations.** Admissible ValueKinds and `refMode` for `DependentSlot` and `BaseSlot`.
* **Token discipline (LEX).** The token SHALL satisfy E.10 token-class morphology for relations/verbs; it SHALL NOT use metaphor heads (`Anchor*`, `Ground*`, `Attach*`) as a meaning-surrogate. If a legacy synonym exists, record it as an alias but keep the relation-specific token specific.
* **Repair path for mismatches.** If an endpoint’s self-kind does not match the expected ValueKind, the allowed repairs are declared (KindBridge, explicit narrowing, or explicit retargeting); “renaming the endpoint” is not a repair.
* **Parameter placement.** Any additional qualifiers required by the relation kind (ranges, metrics, reference planes, policies) SHALL be represented either inside `scope` (preferred) or as explicit additional slots in an extended base-declaration signature; they MUST NOT be smuggled as adjectives on the endpoints.
* **Scope class.** Whether the declaration is claim-scoped (**G**), work-scoped, or publication-scoped.
* **Time discipline.** Whether `Γ_time` is required, optional, or forbidden for this relation kind.
* **Witness discipline.** Whether witnesses are always required vs required only for decision use, and what witness classes are admissible (`U.EvidenceRole`, edition pins, calibration cert pins, proof carriers, policy pins).
* **Admissible change classes.** Which base-change operations are permitted (below) and what continuity requirements apply.
* **Cross-context / cross-plane policy.** Whether this baseRelation family may cross Contexts/planes at all; if yes, what Bridge ids/CL thresholds must be cited and what loss notes are required (F.9 / C.3.3).

This mirrors A.6.5: a SlotKind without ValueKind/RefMode is underspecified; a baseRelation without its vocabulary entry is equally underspecified.

#### A.6.6:4.4.1 - Perspective/voice discipline (dependent-view vs base-view)

**Normative rule.** In Tech / normative prose, authors SHALL express a based declaration in one of the following explicit forms:

* `baseRelation(dependent, base)` (functional notation), or
* `dependent --baseRelation--> base` (arrow notation).

Authors SHALL NOT use passive/umbrella voice (“X is anchored/grounded/attached”) as a substitute for an explicit `baseRelation(dependent, base)` form, because it invites direction flips and silent re-typing.

**Base-view is allowed only if the polarity is preserved.** If authors use base-view wording (“B validates X”), they SHALL either (i) keep both endpoints visible using the same polarity-preserving token (e.g., `validatedBy(X,B)`), or (ii) use an explicit inverse token that is declared in the baseRelation declaration. Authors SHALL NOT flip roles implicitly in prose.

#### A.6.6:4.5 - Lexical discipline

**Normative lexical rule.** In Tech / normative prose and Tech register naming, authors MUST NOT use umbrella metaphors (“anchor/anchoring”, “attach/attachment”, “ground/grounding”) as substitutes for an explicit `baseRelation` token.

**Red-flag rule (`anchor*` as dependence metaphor).**
* In **Tech / normative** prose: authors MUST treat `anchor*` as **prohibited** as a meaning-surrogate for an unnamed dependence kind. Authors SHALL rewrite into explicit `baseRelation(dependent, base)` form (or move to the correct reserved primitive lane).
* In **Plain / legacy** commentary only: authors MAY quote `anchor*` as a legacy umbrella *only if* it is immediately paired with an explicit baseRelation token (e.g., “legacy ‘anchored’ ⇒ `validatedBy(...)`”) and does not introduce a new relation-specific token.

**Carve-outs (pattern-defined primitives).** This red-flag rule does **not** ban uses where “anchoring” is already a *pattern-defined primitive* elsewhere in the spec, such as E.10 MG-DA token-to-described-entity anchoring or A.10 evidence anchors. It still acts as a review trigger: confirm you are using the reserved sense, not smuggling a basedness meaning.

**Naming guard for baseRelation tokens.** Do not mint new baseRelation tokens whose head noun is a metaphor (`Anchor*`, `Ground*`, `Attach*`). If you are tempted to do so, you either (i) have not named the relation kind yet, or (ii) are introducing a legacy alias that must map onto an existing, more specific relation family.

Instead:
1) Name the **BaseRelation token** (declared vocabulary element), and
2) Use a **relation-specific verb phrase** that corresponds to that token.

**Lane guard for meaning.** If the intent is “attach meaning to a term”, do not introduce a baseRelation named `Anchor…` or `Ground…`. Use SenseCell/ConceptSet discipline; semantic meaning assignment is not expressed by SWBD.

**Grounding disambiguation rule.** If the prose says “grounded”, it MUST be rewritten into one of:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* meaning lane (SenseCell/ConceptSet; not SWBD).

**Bind deconfliction note.** Authors MUST NOT use the verb “bind/binding” as a synonym for declaring/refreshing/changing a base declaration. “bind/binding” is reserved for **name binding** (LEX discipline). For SWBD edits, authors SHALL use the base‑change lexicon (below) instead.

#### A.6.6:4.6 - Base-change operation lexicon

As A.6.5 distinguishes slot operations by whether they change a stored reference, resolve a reference, or replace a value, A.6.6 distinguishes **base declaration changes** by which component changes and what semantics are affected.

Operation classes (conceptual):

These names denote **semantic change classes**. In decision/publication lanes, implementations MUST represent these changes by minting a new SWBD (new id/edition) and linking it to the prior one via explicit continuity/withdrawal (WF‑BD‑5 / CC‑BD‑10), rather than mutating the old record.

1. **declareBase** — create a new base declaration with explicit `dependent`, `base`, `baseRelation`, `scope`, and, when applicable, `Γ_time`, plus witnesses when decision-relevant.
2. **withdrawBaseDecl** — retire a declaration (or render it inapplicable by scope narrowing or time restriction, depending on baseRelation declaration).
3. **rebase** — change `base` while keeping the same `dependent` and `baseRelation` (legality depends on the baseRelation declaration; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `baseRelation`.
5. **rescope** — change `scope` (widen/narrow/translate) under the baseRelation’s scope rule; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeBaseRelation** — not an edit-in-place. Changing `baseRelation` changes meaning; mint a new declaration and relate them via an explicit continuity relation (F.13 discipline), rather than silently rewriting the kind.

**Relation to A.6.5 slot operations (non-normative mapping).** These are *semantic change classes*; an implementation may realise them using A.6.5 slot operations on the SWBD record fields. Example: a **rebase** may be implemented as a `retarget` of `baseRef` on a *new* SWBD edition. The point of A.6.6 is that “we retargeted a ref” is not the semantic story; “we rebased the declaration” is.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, the allowed ops (`ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo`) can be viewed as Context-approved specialisations of `declareBase/rescope/rebase/refreshWitnesses` for specific baseRelation families, with stricter declared constraints and lintability.

#### A.6.6:4.7 - Disambiguation guide for selecting a baseRelation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it by selecting a baseRelation family:

| Colloquial intent | BaseRelation family (illustrative) | Dependent | Base | Typical witnesses |
| --- | --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification / indexing** (`identifies`, `indexedBy`, `registeredIn`) | entity-ref / slot-content | identifier / registry entry | issuance record, registry pin |
| “Make measurements comparable” | **Calibration and datum** (`calibratedTo`, `datumOf`, `normalisedTo`) | instrument, model, or output | standard or datum | calibration work plus certificate pin |
| “This claim is admissible because …” | **Evidence admissibility** (`validatedBy`, `verifiedBy`) | claim | evidence carrier or proof | SCR/RSCR pins, proof carriers |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | WM edge | constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X under a view” | **Viewing / retargeting (specialised)** (`viewedVia`, `retargetedAlong`) | episteme/view | described entity | view operator pins, Bridge ids (if retargeting) |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | work-step / publication item | policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | property/abstraction | object | observation/derivation witnesses |
| “Meaning of this term is …” | **Meaning lane** (SenseCell/ConceptSet) | term occurrence | SenseCell/Concept row | definition/usage witnesses |

This table is illustrative; the discipline requirement is that the chosen baseRelation be explicit, declared, and relation-specific. The “Meaning lane” row is included only as a **do-not-model-with-SWBD** reminder.

*Note.* The `viewedVia` / `retargetedAlong` families are defined by the A.6.3/A.6.4 viewing/retargeting operators; this table only classifies them as “relative-to-base” cases.

### A.6.6:5 - Archetypal Grounding

#### A.6.6:5.1 - System archetype: calibration to a standard

**Tell.** A lab instrument channel `TC‑17` is described as “anchored to ITS‑90”. Later, the reference standard is swapped, the phrase “still anchored” is kept, and the applicability window silently expands. Downstream work disagrees and nobody can reconstruct what changed.

**Show.** Express it as a base declaration:

```
BD#Calib_TC17_v5 :=
〈 dependent    = ThermocoupleChannelRef(TC-17),
base         = StandardRef(ITS-90 / CalStd-2025-09),
baseRelation = calibratedTo,
scope        = WorkScope{rig=R3, range=[0..200]°C},
Γ_time       = interval[2025-09-01, 2026-03-01],
witnesses    = { WorkRef(CalibrationRun#8841), CertRef(CalCert@edition=5) } 〉
```

**Show.** Disambiguate edits by operation class:

* New standard ⇒ **rebase** + **refreshWitnesses**.
* Wider applicability window ⇒ **retime** and likely **refreshWitnesses**.
* Relation-kind change (“not calibration, just normalisation”) ⇒ **changeBaseRelation** is not an edit; mint a new declaration and relate via continuity.

#### A.6.6:5.2 - Episteme archetype: claim admissibility via evidence relations

**Tell.** A report asserts: “Model M improves accuracy by 4%.” The team says the claim is “anchored in an experiment”, but dataset version, evaluation harness, and time selector are unclear, and no resolvable evidence is linked.

**Show.**

```
BD#AccGainClaim_2025Q4 :=
〈 dependent    = ClaimRef(CG:Claim#acc_gain_4pct),
base         = EvidenceCarrierRef(Work:EvalRun#2025-10-12),
baseRelation = validatedBy,
scope        = ClaimScope{dataset=BenchX@v3, metric=Top1, hardware=A100},
Γ_time       = snapshot(2025-10-12),
witnesses    = { SCRRef(EvalLog@edition=12), ComparatorSetRef@edition=7 } 〉
```

What becomes explicit is not “anchoring”, but:
* the relation kind (`validatedBy`),
* the scope slice,
* the time selector,
* the witness carriers that make the declaration admissible for decision use.

#### A.6.6:5.3 - Structural archetype: constructive grounding of a model edge

**Tell.** A structural edge is published (“A componentOf B”) without a constructor trace. It becomes treated as “obvious”, while the construction chain is not recoverable.

**Show.**

```
BD#EdgeGrounding_ComponentOf_17 :=
〈 dependent    = WMEdgeRef(Edge:componentOf#17),
base         = TraceRef(Γ_m:ComposeCAL#c17),
baseRelation = tv:groundedBy,
scope        = PublicationScope{view=WMCardLite, system=S, line=L3},
Γ_time       = snapshot(2025-11-02),
witnesses    = { WorkRef(AssemblyRun#7712), EditionPin(Γ_m:ComposeCAL@edition=4) } 〉
```

This example shows why “grounding” must be disambiguated: here it is a declared constructive relation with an explicit base (trace), not a vague claim of “stability”.

### A.6.6:6 - Bias-Annotation

| Lens | Bias introduced by this pattern |
| --- | --- |
| **Governance / assurance** | Prefers explicit witnesses and explicit time selectors for decision-relevant declarations; increases auditability but adds authoring overhead. |
| **Architecture** | Encourages reifying “relative-to” facts as first-class records rather than implicit prose. |
| **Onto-epistemic** | Treats “kind of base relation” as first-order; pushes authors to mint explicit baseRelation tokens instead of hiding semantics in adjectives. |
| **Didactic** | Introduces a new stable vocabulary (“dependent/base/baseRelation”) and requires authors to maintain it consistently across views. |

### A.6.6:7 - Conformance Checklist

A carrier (pattern, spec, schema, code carrier, or publication) conforms to A.6.6 iff:

1. **CC‑BD‑1 — Base relation kind is explicit.**
   Every base-declaration-like statement SHALL name an explicit `baseRelation` token (a declared vocabulary element). No umbrella metaphor SHALL substitute for a relation kind.

2. **CC‑BD‑2 — Dependent and base are explicit and typed.**
   Every based declaration SHALL make both `dependent` and `base` explicit, and SHALL be SlotKind/ValueKind/RefMode disciplined per A.6.5.

3. **CC‑BD‑3 — Scope is explicit.**
   Every based declaration SHALL include an explicit `scope` (Claim scope (**G**) / Work scope / Publication scope).

4. **CC‑BD‑4 — `Γ_time` is explicit when time matters.**
   If any time-dependent assumption exists, the based declaration SHALL include an explicit `Γ_time`; implicit “latest/current” SHALL NOT be used as a substitute.

5. **CC‑BD‑5 — Decision use is witnessed.**
   If a base declaration participates in assurance, gating, or admissibility decisions, it SHALL include a non-empty, resolvable `witnesses` set (pins).

6. **CC‑BD‑6 — No silent kind edits.**
   Changing `baseRelation` SHALL be treated as a semantic change: it SHALL be represented as a new declaration plus explicit continuity, not as an edit-in-place.

7. **CC‑BD‑7 — Grounding is disambiguated.**
   Any use of “grounding/grounded” SHALL be disambiguated to a specific declared relation kind or moved to the meaning lane (SenseCell/ConceptSet).

8. **CC‑BD‑8 — Cross-context use is explicit.**
   If dependent and base reside in different Contexts (or scope translation is required), the declaration’s reuse SHALL cite Bridge ids plus CL policy (no silent reuse across Contexts/planes).

9. **CC‑BD‑9 — `Γ_time` is not treated as freshness.**
   When witness freshness/decay matters, it SHALL be expressed explicitly (evidence-role timespans, qualification windows, explicit freshness predicates), not by treating `Γ_time` as a proxy.

10. **CC‑BD‑10 — Edition fence for decision/publication.**
   If a base declaration is used for decision or cited in PublicationScope, it SHALL be immutable per edition: updates SHALL mint a new declaration and connect it via explicit continuity/withdrawal.

11. **CC‑BD‑11 — Slot suffix discipline is respected.**
   The `*Slot` suffix SHALL be used only for SlotKinds/positions, never for endpoint values or references.

12. **CC‑BD‑12 — No “anchor” relapse.**
   `anchor*` / `ground*` / `attach*` SHALL NOT be used as surrogates for Context/SenseCell/ConceptSet or for an unnamed dependence kind. Authors SHALL either use the reserved primitive sense (where explicitly defined elsewhere) or rewrite into explicit `baseRelation(dependent, base)` form. Metaphor-head tokens SHALL NOT be minted as new relation-specific `baseRelation` vocabulary entries (record them only as deprecated aliases that map onto a specific, non-metaphor token).

13. **CC‑BD‑13 — BaseRelation declarations are explicit.**
    Every `baseRelation` token used in an SWBD SHALL resolve to a vocabulary entry whose vocabulary entry declares (at minimum): polarity; typing expectations (ValueKind + `refMode`) for `DependentSlot` and `BaseSlot`; admissible repair paths (KindBridge, narrowing, or explicit retargeting); scope class; time discipline (`Γ_time` required, optional, or forbidden); witness discipline; admissible change classes; and cross-context and cross-plane policy (Bridge ids + CL threshold + loss notes where applicable).

14. **CC‑BD‑14 — Authoring voice is explicit.**
    In Tech / normative prose, based declarations SHALL be written as `baseRelation(dependent, base)` or `dependent --baseRelation--> base`. Base-view prose SHALL be used only if polarity is preserved via explicit inverse-token use; implicit role flips SHALL NOT be used.

15. **CC‑BD‑15 — Meaning lane separation.**
    Semantic meaning assignment SHALL be modeled via SenseCell/ConceptSet lane constructs (E.10 D.CTX), not via SWBD. SWBD SHALL be used only for non-semantic base-dependence (admissibility, calibration, attribution, policy gating, constructive grounding, viewing/retargeting specialisations).

16. **CC‑BD‑16 — Reserved “bind” discipline.**
    `bind/binding` SHALL be reserved for **name binding** (LEX discipline) and SHALL NOT be used as a synonym for declaring/refreshing/changing a base declaration. Authors SHALL use the base‑change lexicon (`declareBase`, `rebase`, `rescope`, `retime`, `refreshWitnesses`, …) and explicit continuity/withdrawal relations instead.

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Umbrella “anchored/attached/grounded” with no baseRelation** | Hides relation kind; cannot state invariants | Introduce a declared baseRelation token and rewrite prose to use it |
| **Perspective flip without role names** | Directionality and typing become ambiguous | Use `dependent/base` roles consistently; declare polarity in baseRelation declaration |
| **Treating evidence as “the base”** | Confuses base with witnesses | Make evidence/pins witnesses unless the relation kind’s base is explicitly an evidence carrier |
| **Implicit “current/latest”** | Violates explicit time discipline | Declare `Γ_time` explicitly and use witness timespans for freshness where needed |
| **Decision gating without witnesses** | Becomes folklore; not reviewable | Add resolvable witnesses (`U.EvidenceRole`, SCR/RSCR pins, cert pins, proof carriers) |
| **Semantic meaning expressed as a base declaration** | Confuses meaning lane with admissibility lane | Use SenseCell/ConceptSet; keep SWBD for non-semantic basedness |
| **Change baseRelation in place** | Semantic shift masquerades as update | Mint a new declaration and connect via continuity |
| **Using `*Slot` to name an endpoint/value** | Confuses SlotKind with ValueKind/RefKind; breaks substitution and tooling | Keep `*Slot` for positions; use `base`/`dependent` for values and `*Ref` for stored references |
| **Typing `baseRelation` as a `U.Surface*` carrier** | Confuses a relation-specific relation token with a publication surface; invites “free text as relation kind” | Store `baseRelation` as a declared `NameToken` that resolves to a vocabulary entry with an explicit signature and relation-specific constraints |

### A.6.6:9 - Consequences

**Benefits**
* Disambiguation by construction: base-dependence becomes explicit via `baseRelation`.
* Cross-domain reuse: one stable record shape works for calibration, evidence admissibility, attribution, policy gating, and constructive grounding.
* Determinism where required: explicit scope and `Γ_time` prevent silent “latest/current” assumptions.
* Reduced “grounding” confusion: multiple grounding senses become distinguishable relation kinds.

**Trade-offs / mitigations**
* More explicit metadata and vocabulary: mitigated by defining baseRelation families once per Context and reusing them.
* Authoring overhead for witnesses in decision contexts: mitigated by pointing to already-existing `U.Work` refs and witness pins instead of creating new documents.

**Adoption test (informative).**
A team has adopted A.6.6 if, for any decision-relevant “relative-to” statement, it can produce a resolvable tuple
`〈dependent, base, baseRelation, scope, Γ_time?, witnesses?〉`
and can classify any update as one of:
`declareBase / withdrawBaseDecl / rebase / repointDependent / rescope / retime / refreshWitnesses / changeBaseRelation`.
### A.6.6:10 - Rationale

**Why focus on base declaration rather than a metaphor.**
The recurring ambiguity is not “how to attach”, but “what is the declared base, and what kind of dependence is being asserted”. Naming the baseRelation token makes the dependence explicit and reviewable.

**Why separate base from witnesses.**
Bases are semantic reference frames; witnesses are justifiers/enforcers for decision use. Conflating them makes both reasoning and audit impossible.

**Why include scope and `Γ_time`.**
A declaration is never “everywhere forever” by default in FPF. Scope makes applicability explicit; `Γ_time` prevents hidden time dependence (“recent”, “current”, “latest”).

**Why prohibit kind edits.**
Changing the relation kind changes meaning; treating it as an update erases history and breaks continuity discipline.

**Why the base-change lexicon.**
Without explicit change classes, prose collapses distinct edits (rebase vs retime vs rescope vs witness refresh) and recreates the same ambiguity A.6.5 removed at the slot layer.

### A.6.6:11 - SoTA-Echoing

1. **RDF-star and statement qualification.**
   **Adopt/Adapt.** RDF-star/SPARQL-star continues the semantic-web tradition of attaching qualifiers/provenance to statements and edges. We adopt the “qualified statement” intuition, but adapt it by requiring an explicit relation kind token and by tying time and scope discipline to FPF’s explicit `Γ_time` and USM scopes rather than leaving them implicit or purely notational.
   *Primary source:* Hartig et al., “Foundations of RDF* and SPARQL*” (2017+).

2. **Wikidata-style statements with qualifiers and references.**
   **Adopt/Adapt.** The Wikidata model popularised practical “statement + qualifiers + references” structures at scale. We adopt the separation of the core statement from its qualifiers/references, and adapt it by making decision-relevant witness requirements explicit via `U.EvidenceRole` and by requiring explicit scope/time where time-dependent assumptions exist.
   *Primary sources:* Wikidata statement model documentation and design lineage (post‑2015 practice).

3. **Metrology traceability and calibration competence.**
   **Adopt/Adapt.** Laboratory competence standards treat calibration as traceability to standards with documented evidence and bounded validity. We adopt the expectation that calibration-to-standard is not timeless, and adapt it by representing the validity window via explicit `Γ_time` plus witnesses as pinned calibration records.
   *Primary source:* ISO/IEC 17025:2017.

4. **Assurance case metamodels for claim–evidence structure.**
   **Adopt/Adapt.** SACM formalises claim/evidence structures and emphasises structured support relations. We adopt the idea that decision-relevant admissibility links should be explicit, and adapt it by using FPF’s scope/time discipline and by treating relation-kind elision as a first-order defect.
   *Primary sources:* OMG Structured Assurance Case Metamodel (SACM), 2018+.

5. **Objects over a base as a stable mathematical lens.**
   **Adopt/Adapt.** Modern category-theory texts make “objects over a base” (slice categories) a reusable pattern for “X relative to B”. We adopt that lens as the stable abstraction behind base declarations, and adapt it with explicit scope/time and witness semantics needed for engineering governance.
   *Primary source:* Riehl, *Category Theory in Context* (2016).

**SoTA binding note (informative).** This pattern’s “qualified statement + explicit relation kind + references” move aligns with RDF*/Wikidata practice (items 1–2); the explicit time-window + witness semantics in decision use align with metrology traceability and assurance-case structures (items 3–4); the “object over a base” lens is the abstraction used to keep the pattern stable across domains (item 5).

### A.6.6:12 - Relations

**Specialises A.6.P `U.RelationalPrecisionRestorationSuite`.**
A.6.6 is the RPR specialisation for “basedness / relative‑to” claims: it makes the relation kind explicit via `baseRelation`, qualifies it with scope/`Γ_time`/witnesses, and standardises evolution via a base‑change lexicon plus lexical red‑flags (`anchor*`).


**Builds on A.6.5 `U.RelationSlotDiscipline`.**
SWBD introduces a structured record with slots; those slots must be SlotKind/ValueKind/RefKind disciplined, and its change classes must not be confused with slot-edit operations (A.6.5) or name-binding terminology (E.10 / L‑BIND).

**Constrains A.10 evidence admissibility links.**
`verifiedBy` and `validatedBy` are treated as baseRelation tokens; their scope/time and witnesses become explicit when used for decisions.

**Aligns with A.2.4 `U.EvidenceRole`.**
Decision-relevant witness sets should be representable as EvidenceRoles with explicit timespans and provenance discipline, not as ad‑hoc prose references.

**Aligns with A.14 constructive grounding (`tv:groundedBy`).**
Constructive grounding is one specific baseRelation family: dependent is a model edge, base is a constructor trace; witnesses pin the trace and `U.Work` records.

**Coordinates with C.2.1 grounding holons.**
Situational/empirical grounding via `GroundingHolonSlot` is treated as a distinct baseRelation family; it must not be collapsed with `tv:groundedBy` or with semantic meaning assignment.

**Coordinates with A.6.3–A.6.4 viewing/retargeting.**
Viewing and retargeting are specialised “relative-to-base” moves (preserve describedEntity vs change it along a declared bridge). They should reuse SWBD vocabulary where an explicit base declaration is required (scope/time/witness), without collapsing into generic “anchoring” prose.

**Coordinates with A.2.6 and `Γ_time`.**
Base declarations inherit the rule that time-dependent assumptions require explicit `Γ_time`; “current/latest” is not admissible.

**Feeds E.10 / F.18 lexical governance.**
Umbrella metaphors are disallowed as substitutes for baseRelation tokens; prose must name explicit relation kinds and keep the meaning lane separate (SenseCell/ConceptSet).

### A.6.6:End

## A.6.7 - `MechSuiteDescription` — Description of a set of distinct mechanisms

> **Type:** Architectural pattern.
> **Status:** Stable.
> **Normativity:** Normative [A] (Core).

**One-line summary.** A `MechSuiteDescription` is a Kernel **Description** token that names a **set of distinct** `U.Mechanism.Intension` (different mechanisms, not realizations of one mechanism) and declares **suite-level obligations**, **required spec pins**, and **allowed usage protocols**, without conflating this with `MechFamilyDescription` or with publication `Pack`s.

**Plain-name.** mechanism suite description; mechanism suite passport.
**Placement.** Part A → cluster A.IV (A.6), immediately after A.6.5.

**Builds on.** E.8 (pattern template discipline), A.6.1 (`U.Mechanism.Intension` canonical form), A.6.5 (slot/ref discipline), E.10 (lexical + ontological rules; strict distinction; minimal specificity; kind suffixes), E.19 (conformance checks), E.18 (TGA / P2W graph discipline; crossing visibility), A.21 (OperationalGate(profile) and gate-level decisions).

**Used by.** Any framework area that needs a stable “universal kernel” shared across multiple mechanisms (notably the universalization of Part G patterns, including but not limited to G.5), and any “mechanism stack” whose correctness is defined by **shared legality + transport + audit obligations** rather than by a single shared `BaseType`.

**Mint vs reuse.**

* **Mints:** `MechSuiteDescription` (KernelToken, Description) and the record names used by its canonical form: `MechSuiteId`, `SuiteObligation`, `SuiteObligations`, `SuiteSpecPins`, `SuiteProtocol`, `ProtocolStep`, `SuiteAuditObligations`.
* **Reuses (by reference):** `U.Mechanism.Intension` (members), `MechFamilyDescription` / `MechInstanceDescription` (optional citations), existing pinned references such as `CN‑Spec` / `CG‑Spec` (as pins), and E.TGA/P2W notions (as obligations/pins), without introducing new `U.*` kernel types.

**LEX.TokenClass.**
* `LEX.TokenClass(MechSuiteDescription) = KernelToken.`
* `LEX.TokenClass(MechSuiteId) = KernelToken.`
* `LEX.TokenClass(SuiteObligations) = KernelToken.`
* `LEX.TokenClass(SuiteSpecPins) = KernelToken.`
* `LEX.TokenClass(SuiteProtocol) = KernelToken.`
* `LEX.TokenClass(SuiteAuditObligations) = KernelToken.`

**I/D/S.** Description (D); Tech name ends with `…Description`.
Lexical note: do **not** prefix this token with `U.` — `U.*` is reserved for Kernel **types**, while `MechSuiteDescription` is a Kernel **descriptor** (Description token).

### A.6.7:1 - Problem frame

In FPF, a **mechanism** is a node-level intensional object (`U.Mechanism.Intension`) with explicit SlotSpecs inside operator signatures, and a declared LawSet/guards/transport/audit (A.6.1, A.6.5). Many architectures, however, require **a stable bundle of multiple different mechanisms** that are intended to be used together under shared legality and crossing discipline (e.g., a characterization chain, a legality-gated selection pipeline, or a universal Part‑G kernel that multiple G.* patterns must reuse).

FPF already has `MechFamilyDescription`, but its meaning is: **many realizations of one and the same `U.Mechanism.Intension`**. That construct cannot correctly represent a bundle of different mechanisms (different intensions), and trying to overload it creates a level error.

Additionally, FPF reserves “Pack” for publication/shipping bundling (e.g., G.10); using “Pack” to mean “container of mechanisms” creates ontological collisions and downstream confusion.

### A.6.7:2 - Problem

We need a Kernel-level descriptor that can:

1. represent a **set of distinct mechanisms** (distinct `U.Mechanism.Intension`),
2. declare **shared obligations** that must hold across the set (e.g., crossing visibility, legality citation discipline, guard decision format, penalty routing),
3. provide **shared spec pins** (e.g., “this suite is governed by CN-Spec and CG-Spec”), without duplicating those spec contents,
4. constrain **allowed protocols** of use (allowed pipelines / permitted ordering), without turning the suite into a mechanism, and
5. preserve strict distinction among:

   * a suite of mechanisms (`MechSuiteDescription`),
   * a family of realizations of one mechanism (`MechFamilyDescription`),
   * a publication bundle (`Pack`, e.g., G.10).

### A.6.7:3 - Forces

1. **Strict distinction (level hygiene).**
   *“many mechanisms”* must not be encoded as *“many realizations of one mechanism”*.
   Violating this blurs specialization laws, SlotKind invariance expectations, and audit/crossing responsibilities.

2. **Minimal specificity + kind suffix discipline (E.10).**
   The token name should encode only what is essential: it is a description, it is about mechanisms, it is a suite.
   It must not capture a particular domain (e.g., CHR) in the Kernel name.

3. **Governing spec ref centrality (CN‑Spec and CG‑Spec).**
   Suites must cite governing spec refs as pins, not duplicate their internals, otherwise multiple competing “centers of legality” arise.

4. **Transport and crossing visibility discipline.**
   Cross-context and cross-plane steps must be visible and bridge-only; penalties must route to `R/R_eff` only; suites must not embed CL/Φ/Ψ/Φ_plane tables. Visibility is mediated via E.TGA / P2W (crossing bundles + UTS/Path pins), not by “implicit semantics”.

5. **Guard vs gate separation.**
   Mechanisms can output tri-state guard outcomes and explanations; **gate decisions** (including `block`) and `DecisionLog` remain gate-level (`OperationalGate(profile)`). A suite must not collapse these layers.

6. **FPF is conceptual.**
   The suite is a conceptual descriptor: no implementation fields, no “lint rules”, no machine governance. The suite expresses obligations as conceptual constraints and required pins/anchors.

### A.6.7:4 - Solution

Introduce a new Kernel description token:

#### A.6.7:4.1 `MechSuiteDescription` (data model)

`MechSuiteDescription` declares:

1. **Suite identifier:** a stable identifier for downstream citation.
2. **Membership:** a finite set of distinct mechanism intensions.
3. **Suite obligations:** shared invariants that every member (and any permitted composition of members) must respect.
4. **Suite spec pins:** required citations/pins to governing spec refs and other “anchor” references.
5. **Suite protocols:** allowed pipelines of use (permitted ordering and optional steps), expressed at the descriptive level.
