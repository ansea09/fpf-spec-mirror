---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern Quality Characteristic Space"
section_id: "E.21:4"
section_title: "Solution - Pattern quality as a scoped Q-Bundle over declared characteristics"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__005_solution-pattern-quality-as-a-scoped-q-bundle-over-declared-characteristics.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "E.21 — FPF Pattern Quality Characteristic Space"
  - "E.21:4 — Solution - Pattern quality as a scoped Q-Bundle over declared characteristics"
line_start: 63993
line_end: 64640
dependencies:
  - "A.17-A.19"
  - "A.6.P"
  - "A.6.Q"
  - "C.16"
  - "C.25"
  - "E.10.SEMIO"
  - "E.11"
  - "E.17.AUD"
  - "E.19"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
  - "Goodhart/proxy substitution"
  - "Pareto/front comparison"
  - "PatternQualityCharacteristicSpace"
  - "PatternQualityQBundle"
  - "activation-normalized coordinates"
  - "and admissibility predicates are not written as duties"
  - "bounded non-use"
  - "coordinate evidence"
  - "definitions"
  - "eligibility filters"
  - "first move"
  - "invariants"
  - "pattern quality"
  - "state agent obligations only"
  - "stop condition"
  - "typing rules"
---

### E.21:4 - Solution - Pattern quality as a scoped Q-Bundle over declared characteristics

State the scoped FPF pattern-quality read as a `PatternQualityQBundle`, not as one score.

#### E.21:4.0 - Architectural position

`E.21` is a local receiving pattern for scoped FPF pattern-quality claims. It specialises existing FPF architecture; it does not create a new quality-governance subsystem.

It defines how to read whether one authored FPF pattern version is good enough for one declared reader, use, and scope, why improvement may stop, and which weaknesses remain bounded.

`E.21` owns only these questions:

1. Which exact FPF pattern version is being read?
2. For which reader, use, scope, and currentness window?
3. Which hard blockers make comparison meaningless?
4. Which ordinal pattern-quality coordinates are active?
5. Which content evidence supports the coordinate readings?
6. Which `PatternQualityStatus` follows?
7. Why may improvement stop, or why must the claim narrow, repair, hold for architecture, or refresh?

`E.21` does not own:

* authoring the pattern body (`E.8`);
* running admission or refresh review profiles (`E.19`);
* general measurement legality (`C.16`, `A.17`, `A.18`, `A.19`);
* arbitrary engineering quality-family bundling (`C.25`);
* durable naming and local-first unification (`F.18`, `E.10`, `A.6.P`);
* project evidence, assurance, gate, work, release, safety, security, or compliance claims (`A.10`, `B.3`, `A.20`, `A.21`, `A.15`, or the exact receiving pattern).

A conforming `E.21` read may cite neighbouring patterns, but it may not absorb their governed objects.

`E.21` protects these seam surfaces as part of the pattern-quality read: self-application, first-entry/discoverability, publication/projection, bounded non-use, no forced winner, falsifiability/lowering evidence, reviewer-power misuse, AI/RAG/thin-echo summaries, and corpus ecology. A read that crosses one of these surfaces must keep the pattern-quality claim scoped, replayable, falsifiable, and routed to the exact neighbouring pattern instead of becoming control apparatus.

#### E.21:4.0a - Mint/reuse and kind settlement

`E.21` mints no new Kernel kind, no project-side evidence kind, no assurance kind, no work kind, no gate kind, no release kind, and no general maturity kind.

Its durable heads are local specialisations, fields, value sets, or scoped support constructs over existing FPF kinds:

| E.21 head | Kind settlement | Existing governing pattern kept intact |
|---|---|---|
| `PatternQualityQBundle` | Local `C.25` Q-Bundle specialisation for one scoped FPF pattern-quality claim. | `C.25` remains the general Q-Bundle normal form. |
| `PatternQualityCharacteristicSpace` | Local `A.19` CharacteristicSpace specialisation for ordinal pattern-quality content readings. | `A.17`, `A.18`, `A.19`, and `C.16` keep general Characteristic/Scale/Coordinate and measurement legality. |
| `PatternQualityStatus` | Local value set inside a `PatternQualityQBundle`; an admissible-use posture for the pattern-quality claim. | Not a role state, release state, gate decision, assurance level, or project status. |
| `EligibilitySet` | Set-valued hard-filter field inside `PatternQualityQBundle`. | Not an `A.21` gate, not an `E.19` review profile, and not a soft score region. |
| `DominanceSet` | Set-valued coordinate-selection field for Pareto comparison after eligibility passes. | Not a hidden scoring method, not `G.5` selection policy, not `C.11` choice result. |
| `TieBreakerSet` | Set-valued secondary preference field among non-dominated candidates. | Not a secret dominance coordinate or hard blocker override. |
| `TelemetrySet` | Set-valued reopen/calibration signal field for the pattern-quality claim. | Not project telemetry, not certification evidence, not replacement for content evidence. |
| `CoordinateEvidenceRef` | Local evidence-reference record for one coordinate reading. | It may cite `A.10` or `B.3` only when evidence/assurance claims are actually live. |
| `CoordinateEvidenceRefs` | Set-valued field of `CoordinateEvidenceRef` records. | Not a support archive, review verdict, or proof of project-world truth. |
| `PatternQualityFront` | Scoped non-dominated set over candidate pattern versions or candidate edits under the active `E.21` relation. | Not a `C.18` NQD archive, not a `G.5` shortlist, not a project backlog. |
| `PatternImprovementArchive` | Bounded trade-off support archive for candidate pattern edits/variants. | Not process history, chat memory, permanent backlog, or mandatory appendix. |

Coordinate heads in `E.21:4.3` are local pattern-quality characteristic heads inside `PatternQualityCharacteristicSpace`. They do not become general FPF characteristics, metrics, maturity dimensions, or measurement templates unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration makes that live.

A conforming `E.21` read treats these heads as exact local constructs. When a head is reused outside `E.21`, the receiving text must either cite `E.21` by value or rerun the exact governing pattern for the new use.

#### E.21:4.0b - Layered use architecture

`E.21` has four activation layers.

Layer 0 and Layer 1 are ordinary; Layer 2 and Layer 3 are live-claim only.

**Layer 0 - first-pass slice.**
Used for one first read of one pattern version. It names `PatternVersionRef`, `WorkingReaderScope`, `IntendedUse`, `QualificationWindow`, first admissible move evidence, activated blockers, minimal active coordinates, status, and next admissible repair or bounded non-use.

**Layer 1 - content-evidence coordinate read.**
Used when the first-pass slice survives or when a substantive quality claim is being made. It checks activated `EligibilitySet` rows, active ordinal coordinates, and local `CoordinateEvidenceRefs`.

**Layer 2 - comparison and stop.**
Used when several candidate edits or variants are live, or when a stop decision is being claimed. It activates `DominanceSet`, floors, `TieBreakerSet`, `PatternQualityStatus`, and `StopCondition`.

**Layer 3 - optional refresh and trade-off support.**
Used only when live reuse, repeated findings, retrieval failure, high-use patterns, high-assurance reuse, contested neighbour authority, or variant-history retention makes support necessary. It may activate `TelemetrySet`, `PatternQualityFront`, `PatternImprovementArchive`, and full support cards.

A higher layer SHALL NOT be required merely because a lower-layer read exists.

Every activated layer must state what admissible use it buys.

If a field, card, telemetry signal, archive entry, or support record does not change first-pass usability, coordinate evidence, variant comparison, stop/reopen condition, or bounded non-use, it is apparatus bloat for the current claim.

#### E.21:4.0c - Self-application and recursion boundary

`E.21` may be applied to itself only through the same lowest sufficient activation layer used for any other FPF pattern.

The ordinary self-application read closes when the current `E.21` text exposes:

1. one first admissible action-guiding move for an author or reviewer;
2. the governed object of the quality read;
3. the no-single-score and no-administrative-proxy boundary;
4. the neighbour-authority boundary to `E.8`, `E.19`, `C.25`, `C.16`/`A.17`/`A.18`/`A.19`, `F.18`, `E.10`, `A.6.P`, `E.17`, `A.10`, `B.3`, `A.20`, `A.21`, and `A.15`;
5. one explicit stop or repair condition for the declared self-read scope.

Self-application SHALL NOT require an additional `PatternQualityQBundle` evaluating the previous `PatternQualityQBundle`. If the first self-read exposes a content defect, repair that defect in the pattern text or narrow the declared use. If the defect is architectural, use `holdForArchitectureDecision`.

#### E.21:4.1 - PatternQualityQBundle

`PatternQualityQBundle := <PatternVersionRef, ClaimScope, WorkingReaderScope, IntendedUse, QualificationWindow, EligibilitySet, DominanceSet, CoordinateEvidenceRefs?, TieBreakerSet?, TelemetrySet?, EvidenceRefs, PatternQualityStatus, StopCondition>`


`PatternQualityQBundle` is the publication unit for a scoped pattern-quality claim.

`PatternQualityQBundle` is replayable when another reader can recover the same target version, declared scope, active eligibility rows, active coordinates, coordinate evidence refs, status payload, and stop/non-stop reason without chat memory, steward memory, or administrative placement state.

Its first-pass slice may contain only the fields needed to decide whether one working reader can recover the governed object and first admissible move.

The full bundle is used when coordinate evidence, variant comparison, admission/refresh closure, high-assurance reuse, or contested neighbour authority is live.

The fields below are slots in that publication unit; they are not independent governed objects. The governed object remains the scoped pattern-quality claim for one pattern version.

| Field | Role |
|---|---|
| `PatternVersionRef` | The exact pattern version being assessed. A title alone is not enough when several extracted hosts or monolith editions exist. |
| `ClaimScope` | The declared pattern-quality claim boundary: ordinary authoring support quality read, admission-support quality read, refresh-support quality read, landing-support quality read, release-support quality read, canonization-support quality read, external-review-support quality read, high-assurance-reuse support quality read, or another named support scope. The administrative action is not the quality scope; it is the neighbouring action that this quality read may support. Do not name the administrative action itself as a coordinate-bearing quality scope. |
| `WorkingReaderScope` | The primary reader role and first-use situation the pattern must serve. |
| `IntendedUse` | What the quality result is allowed to support: continue drafting, admit for declared use, narrow use, repair before use, or refresh. |
| `QualificationWindow` | The time, edition, SoTA, neighbouring-pattern, or release window in which the quality read is current. |
| `EligibilitySet` | Hard filters that must pass before coordinate comparison is meaningful. |
| `DominanceSet` | The selected quality coordinates used for Pareto comparison of candidate versions or candidate edits. |
| `CoordinateEvidenceRefs?` | Text sections, worked cases, SoTA rows, relation checks, or findings that support coordinate values. Review, landing, release, or monolith state alone is not coordinate evidence. |
| `TieBreakerSet?` | Secondary preferences used only among non-dominated candidates. |
| `TelemetrySet?` | Observed return, retrieval, review, and drift signals used to reopen or calibrate the quality read. |
| `EvidenceRefs` | Evidence, worked cases, review findings, SoTA rows, or source references that support the read. |
| `PatternQualityStatus` | The resulting admissible-use posture. |
| `StopCondition` | The explicit condition under which improvement can stop for this scope. |

`PatternQualityStatus` has this value set:

| Value | Meaning |
|---|---|
| `admissibleForDeclaredUse` | Eligibility passes and the selected coordinates meet the declared floors for the current `ClaimScope`. |
| `admissibleWithNarrowerUse` | The pattern can be used only after the `ClaimScope`, `WorkingReaderScope`, or supported use is narrowed by value. |
| `repairBeforeUse` | One or more hard eligibility filters or live quality floors fail, and the pattern should not be relied on for the intended use. |
| `holdForArchitectureDecision` | The defect is not local prose; the governed object, neighbour authority, pattern split, or placement must be decided before quality evaluation can close. |
| `refreshNeeded` | The pattern was previously admissible, but a SoTA, neighbour, terminology, retrieval, telemetry, or use-scope change invalidates the old read. |

A `PatternQualityStatus` is an admissible-use posture for the pattern-quality claim. It is not a gate decision, release state, assurance level, compliance verdict, safety certificate, work authority, publication truth, or project-side refusal/approval.

A status without payload is not checkable. Every `PatternQualityStatus` SHALL carry the minimal status payload:

* `admissibleForDeclaredUse`: declared use, active floors, and remaining bounded non-use, if any.
* `admissibleWithNarrowerUse`: the exact narrowed `ClaimScope`, `WorkingReaderScope`, or `IntendedUse`.
* `repairBeforeUse`: the activated blocker and the first admissible repair target.
* `holdForArchitectureDecision`: the exact unresolved governed-object, neighbour-authority, split, or placement question.
* `refreshNeeded`: the exact SoTA, neighbour, terminology, retrieval, telemetry, or use-scope change that invalidated the previous read.

A bounded non-use result is a valid pattern-quality outcome.

When a pattern is not admissible for the declared ordinary use but remains useful as expert-only support, source-basis support, high-assurance support, historical rationale, narrow worked-case support, or neighbour-handoff support, the `PatternQualityStatus` SHALL be `admissibleWithNarrowerUse`, not `repairBeforeUse`.

The narrowed use must name:

* the exact narrowed reader/use/scope;
* the prohibited broader use;
* the first admissible next pattern or repair if broader use is still desired.

#### E.21:4.1a - Coordinate readings are content readings, not administrative-state readings

`PatternQualityCharacteristicSpace` coordinates measure the current pattern version and the content evidence available for that version: its recognition text, governed object, ontology, names, Solution, checklist, worked cases, SoTA rows, relations, and support boundaries. They do not measure whether the pattern has already been externally reviewed, merged into a monolith, included in a release branch, or accepted by one steward process.

Administrative state can change a `PatternQualityQBundle` only in these ways:

| Administrative-state effect | Admissible role |
|---|---|
| Review, landing, release, or monolith state | May constrain `ClaimScope`, `IntendedUse`, `QualificationWindow`, or confidence in `EvidenceRefs`. It does not raise or lower a coordinate by itself. |
| External review finding | May change a coordinate only when the finding identifies a content defect or content strength in the pattern version. The coordinate changes because of the defect or strength, not because a review event occurred. |
| Landing or publication move | May change which pattern version is referenced by `PatternVersionRef`, and may change discoverability or authority claims handled by other patterns. It does not make the same text more or less mathematically adequate, ontologically precise, or action-guiding by placement alone. |
| Missing administrative action | May block a release, review, or canonization claim. It is not evidence that `FormalClaimLegalityAndLensFit`, `CaseCountercaseAndTransferCoverage`, `ActionPathGuidance`, or another active coordinate is low. |

If a quality read says "low because this has not been externally reviewed" or "high because this is already in the monolith", it is using administrative state as a proxy. The repair is to state the substantive coordinate evidence directly and keep administrative state in `ClaimScope`, `QualificationWindow`, or receiving release/review patterns.


#### E.21:4.2 - EligibilitySet: hard conditions before quality comparison

The `EligibilitySet` is not a low-scoring region. It is the precondition for meaningful comparison.

Eligibility rows have activation. A first-pass pattern-quality read always checks only the rows needed to decide whether one working reader can recognise the situation, recover the governed object, find the first admissible move, and avoid immediate neighbour-authority or apparatus overread.

Rows whose condition depends on a live source, live formal lens, live measurement claim, live accepted basis, live release/review state, live mission/pillar conflict, or live durable-name change activate only when that load is present in the target pattern or in the declared `ClaimScope`.

Failure of an activated eligibility row is a content blocker. A non-activated row is not a pass, not a waiver, and not a hidden todo; it is outside the current pattern-quality claim.

| Eligibility condition | Pass condition |
|---|---|
| `canonicalFrameConformance` | The pattern has the `E.8` canonical frame, header block, required sections, and footer marker, or the missing piece is explicitly treated as a mechanical repair before use. |
| `governedObjectClarity` | The early text says which object, relation, move, boundary, or support claim the pattern governs. |
| `firstMoveRecoverability` | The target pattern's `Problem frame` and `Solution` expose one first admissible action-guiding move for the declared `WorkingReaderScope`, or a named neighbouring-pattern handoff now carries the live claim. |
| `missionOrPillarConflict` | Activated when the pattern claims FPF-wide mission support, changes a pillar interpretation, imports external domain scope, or creates a possible pillar conflict. Absence of pillar recitation is not a defect. Pass condition: no live mission/pillar conflict is hidden, and any live constitutional payoff is carried by the exact coordinate or neighbouring pattern that owns it. |
| `noProcessLeakage` | Live pattern prose contains no campaign, review, history, planning, landing, or "what changed" residue. |
| `normativityAdmissibilitySplit` | RFC keywords state agent obligations only; definitions, invariants, typing rules, and admissibility predicates are not written as duties. |
| `terminologyAdmissibility` | Minted and load-bearing names pass the `F.18 -> A.6.P -> E.10` chain: kind, relation, qualification, governed object, governed move, and non-admissible neighbouring use are recoverable. |
| `solutionChecklistCoherence` | `Problem`, `Forces`, `Solution`, `Conformance Checklist`, anti-patterns, and relations test the same action guidance. |
| `neighborRelationClosure` | The pattern does not create shadow authority; relations and downstream hooks cite the exact neighbouring FPF patterns by value. |
| `SoTABindingMinimum` | SoTA rows are non-decorative: at least one `Solution`, checklist, boundary, worked case, or relation changes because of the adopted/adapted/rejected source stance. |
| `measurementAndScaleLegality` | Any value, score, coordinate, scale, threshold, comparison, or quality coordinate is typed through `C.16`, `A.17`, `A.18`, and applicable `A.19`/`C.25` discipline. |
| `coordinateAdministrativeIndependence` | Coordinate values are assigned from pattern content and content evidence, not from review completion, landing state, monolith placement, release state, or steward acceptance. |
| `noProxyForValueSubstitution` | The quality read asks what became worse when coordinates improved: first-use cost, author cost, maintenance cost, neighbour ripple, entry/projection cost, corpus cost, practical payoff, and bounded non-use are not hidden outside the active comparison. |
| `formalClaimLegalityAndLensFit` | If a measurement, score, comparison, threshold, aggregation, mathematical lens, causal lens, QL lens, simulation, representation, or learned-lens claim is load-bearing, the scale/comparability basis, preserved structure, lost structure, visible payoff, admissible use, non-admissible use, and stop condition are named. |
| `acceptedBasisCarryThrough` | Accepted intake, DRR, returned findings, or architecture-basis obligations that govern the pattern are expressed, intentionally absent, or assigned to a named receiving FPF pattern or support document. |

If an eligibility condition fails, the status is `repairBeforeUse` or `holdForArchitectureDecision`. Do not average the failure into better coordinates. A missing first move is not a weak coordinate. For an ordinary-use pattern-quality read, failed activated `firstMoveRecoverability` is a blocker unless the claim is explicitly narrowed to expert-only support, reference-only support, or architecture-decision support.

#### E.21:4.3 - PatternQualityCharacteristicSpace

`PatternQualityCharacteristicSpace` is the declared characteristic space for FPF pattern-quality reads. It uses ordinal coordinates. The default scale is a zero-based six-level scale:

A `PatternQualityCharacteristicSpace` is not a general FPF quality ontology. Its coordinate heads remain local pattern-quality characteristic heads unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration makes a broader characteristic or measurement claim live.

A coordinate value in `PatternQualityCharacteristicSpace` is an ordinal pattern-quality reading, not a `U.Measure` by default. It becomes a measurement claim only when the pattern explicitly declares a `C.16` measurement template, scale, unit, or admissible coordinate construction. Otherwise the value is an evidence-backed ordinal judgement over pattern content for the declared scope.

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The characteristic is not expressed in the pattern text for the declared scope. |
| 1 | `namedOnly` | The characteristic is named or implied, but the reader cannot use it as pattern-quality evidence. |
| 2 | `partiallyExpressedForDeclaredUse` | The characteristic is expressed in one or more local loci, but the expression is incomplete, fragile, or too narrow for the declared use. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The characteristic is expressed enough to support the declared use, with known limits kept visible. |
| 4 | `wellExpressedForDeclaredUse` | The characteristic is clearly and repeatedly expressed across the pattern body, with direct evidence and boundary protection. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The characteristic is expressed at an exceptional level for the declared use, across multiple reinforcing loci and cases, without hiding cost or neighbouring-pattern loss. |

The scale is zero-based because true absence is not a weak positive value. It uses six levels rather than ten because the read is ordinal: six levels distinguish absence, mere naming, partial expression, sufficiency, strong expression, and exceptional expression without pretending to have decimal-grade precision. The labels are intentionally domain-neutral. They describe degree of expression of whichever characteristic is being read; they do not import a substantive property such as robustness, stability, safety, maturity, completeness, usability, affordability, or evidence strength into every coordinate.

Authors may use a coordinate-specific named scale when needed, but they must keep the scale ordinal unless a stronger `C.16` measurement basis is declared. No arithmetic mean, percentage score, or hidden normalization is admissible.

The ordinal value of a coordinate is a content reading. `FormalClaimLegalityAndLensFit = 3` means the formal or lens claim is sufficiently expressed for the declared use; it does not mean "not yet reviewed". `FormalClaimLegalityAndLensFit = 5` means the same coordinate is exceptionally expressed in the current pattern text; it does not mean "already landed". The same pattern text in an extracted host and in a monolith should receive the same coordinate value unless the move changes the text, exposes a new content defect, changes the version under `PatternVersionRef`, or changes the declared use being evaluated.

Coordinate names in this section are local characteristic heads inside `PatternQualityCharacteristicSpace`. They are not `U.Measure`s and not general-purpose CHR patterns by name alone.

A coordinate value is an ordinal content reading over the target pattern text for the declared `ClaimScope`. It becomes a measurement claim only when a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration explicitly supplies the measurement basis, scale, unit, comparability mode, and evidence support.

Coordinate values in `PatternQualityCharacteristicSpace` are ordinal content readings unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration makes a measurement claim live. `DominanceSet` compares these readings without scalarizing them.

#### E.21:4.3a - Coordinate value evidence test

A coordinate value is justified by content evidence, not by the label alone. The ordinary `4 wellExpressedForDeclaredUse` test is:

1. the coordinate names the exact property being read;
2. the pattern text contains direct evidence for that property;
3. at least one positive case and one boundary or anti-case exercise the property;
4. neighbouring-pattern relations or non-use boundaries protect the property from overread;
5. SoTA or internal FPF architecture changes at least one `Solution`, checklist, relation, or worked-case line when the coordinate depends on a source or modeling lens;
6. the coordinate evidence does not depend on review completion, landing state, monolith placement, release state, or steward acceptance.

A `5 exceptionallyExpressedForDeclaredUse` value requires the `4` test plus stronger content evidence: multiple reinforcing loci, heterogeneous cases or anti-cases where the characteristic changes the result, explicit non-use boundary, and no hidden affordability, maintenance, neighbour-ripple, corpus, entry/projection, or proxy-for-value loss.

`3 sufficientlyExpressedForDeclaredUse` means the coordinate is usable for the declared scope but lacks one or more supports required for `4` or `5`. Coordinate value and evidence support remain distinct: a value says how strongly the characteristic is expressed; `CoordinateEvidenceRefs` say why that reading is justified.

The coordinates below are not one flat always-on audit grid. `PatternQualityCharacteristicSpace` is an activation-normalized characteristic menu for scoped FPF pattern-quality reads.

A coordinate is admissible only when it reads a content property of the target pattern version under the declared `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`.

Hard blockers stay in `EligibilitySet`. Evidence kinds justify coordinate readings but are not coordinates by themselves. Telemetry reopens or calibrates a read but does not replace content evidence. Fronts and archives preserve candidate trade-offs but do not add ordinary drafting obligations. `PatternQualityStatus` and `StopCondition` are results of the read, not coordinates. Project-side evidence, assurance, gate, release, work, safety, security, or compliance claims route to exact neighbouring patterns.

Each coordinate has an activation class:

- `first-pass core`: ordinarily active for the first ordinary read of one pattern version;
- `ordinary stop core`: active when the read claims admission, stop, repair-before-use, or narrowed-use closure;
- `claim-support`: active when evidence, currentness, SoTA, case breadth, measurement, formal lens, replay, or high-value claim support is live;
- `corpus/publication`: active when the edit changes entry cues, ToC/J.4/Preface, summaries, cards, dashboards, retrieval, durable names, relations, projections, or neighbouring authority;
- `front/refresh`: active when variants, non-dominated fronts, archives, refresh, repeated findings, or no-forced-winner cases are live.

Inactive coordinates are not passes, waivers, or hidden failures. They are outside the current pattern-quality claim.

| Characteristic | Activation class | What it reads | Good state |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | first-pass core | Whether the working reader recognises the situation, ordinary use, non-use, harm if missed, and first boundary early. | The reader can say "this is / is not my situation" without reading support apparatus. |
| `ActionPathGuidance` | first-pass core | Whether, after the first admissible move is recoverable, the reader can continue the admissible action path. | The `Solution` carries the action path; the checklist tests it rather than replacing it. |
| `ClosureAndBoundedNonUseRecoverability` | ordinary stop core | Whether stop, repair, narrower use, and neighbour handoff are recoverable. | The reader can tell when the governed move is enough, when to narrow, and where remaining live claims go. |
| `GovernedObjectAndClaimScopeStability` | first-pass core | Whether the governed object and quality-claim scope stay stable across title, problem frame, solution, checklist, cases, relations, and status. | The pattern does not drift between pattern, record, bundle, suite, profile, review-profile result, method, work, support document, or broader/narrower use claim. |
| `SemanticKindAndNameRecoverability` | ordinary stop core; first-pass when names are load-bearing | Whether heads, kinds, relations, qualifiers, support roles, evidence roles, and Tech/Plain names recover the same FPF reading. | Names are usable because they preserve kind, relation, and load, not because prose is polished. |
| `NeighborAuthorityAndBoundedUseFit` | first-pass core | Whether neighbouring claims stay with exact receiving patterns and residual weakness is bounded. | Evidence, assurance, measurement, naming, work, gate, decision, publication, causal, release, bridge, and refresh claims do not become `E.21` authority. |
| `PracticalUseDeltaAndHarmPrevention` | first-pass core | Whether the pattern changes a real reader move, prevents a named misuse, reduces named cost or ambiguity, or preserves a named boundary. | The reader can state what action, decision, repair, non-use, or handoff becomes better because the pattern exists. |
| `UseAffordabilityAndApparatusProportionality` | first-pass core | Whether first use is affordable and the apparatus is proportionate to the live claim. Subreadings: first-use cost and apparatus proportionality. | Ordinary use stays light; heavier fields, cards, telemetry, front/archive, support, or evidence apparatus appear only when their live claim buys admissible use. A weak live subreading limits the coordinate value; do not average the subreadings. |
| `RepairLocalityAndChangeImpactPredictability` | ordinary stop core | Whether repairs stay local and downstream impact is predictable. | The repair has the smallest live locus, known impact radius, and no unnecessary changes to names, relations, supports, evidence refs, or entry surfaces. |
| `ProxyForValueSubstitutionResistance` | ordinary stop core | Whether the quality read prevents Goodhart substitution of rubric satisfaction for pattern-use value. | The read asks what got worse and treats usability, affordability, maintainability, neighbour costs, and bounded non-use as quality evidence rather than afterthoughts. |
| `ClaimSupportTraceabilityCurrentnessAndReplayability` | claim-support | Whether another reader can replay the claim from pinned text, scope, evidence refs, currentness basis, limitations, status, and stop reason. | The claim is traceable and replayable without chat memory, steward memory, or administrative placement state; project assurance is routed out. |
| `CaseCountercaseAndTransferCoverage` | claim-support | Whether positive cases, near-misses, anti-cases, and transfer cases match claimed breadth. | Cases test the main misuse paths and boundary transfers; broad claims have heterogeneous support or explicit narrowing. |
| `SoTABindingAndCurrentness` | claim-support | Whether SoTA, lineage, rejected practice, and refresh triggers are separated and load-bearing. | Adopt/adapt/reject stances mutate `Solution`, checklist, boundary, relation, worked case, stop, or reopen condition. |
| `FormalClaimLegalityAndLensFit` | claim-support | Whether measurement, score, comparison, scale, threshold, formal model, or lens claim is legal and bounded. | Scale/comparability basis and preserved/lost structure are visible; non-admissible formal use is named. |
| `FalsifiabilityAndLoweringCondition` | claim-support | Whether high values, status claims, and stop claims say what would lower or reopen the read. | Values `4`/`5`, `admissibleForDeclaredUse`, and stop decisions carry concrete lowering conditions unless the declared use is only first-pass repair triage. |
| `ExternalEntryAndProjectionIntegrity` | corpus/publication | Whether ToC/J.4/Preface cues, cards, summaries, dashboards, generated explanations, retrieval snippets, or thin echoes preserve the governed read. | External projections guide entry by value and scope; they do not become approval badges, authority faces, project evidence, or second semantic tracks. |
| `PatternLanguageEcologyFit` | corpus/publication | Whether the pattern preserves FPF corpus health: relation fanout, name collision risk, entry-map clarity, support-role parity, stale echoes, and neighbouring-authority distribution. | Local improvement does not create corpus-level confusion, relation explosion, entry pollution, stale echoes, or shadow authority. |
| `EvolutionFrontAndRefreshDiscipline` | front/refresh | Whether variants, fronts, archives, refresh windows, no-forced-winner cases, and smallest-live-reopen rules preserve open-ended evolution without endless polishing. | Non-dominated candidates can remain visible until a declared receiving action requires one selected candidate; refresh reopens the smallest live locus. |

**Activated overlays.** These overlays are not ordinary coordinates. They become active only when the target pattern or declared `ClaimScope` makes the issue live.

| Overlay | Activation | Good state |
|---|---|---|
| `ConstraintAndHarmBoundaryFit` | Active when the target pattern contains safety, security, ethics, compliance, deontic, harm-prevention, prohibited-use, non-negotiable constraint, or project-risk claims. | Constraint and harm boundaries are visible, exact receiving patterns are named, and no pattern-quality result is overread as safety, security, compliance, ethics, or project approval. |
| `SelfApplicationAndRecursionBoundary` | Active for meta-patterns that govern pattern authoring, review, quality, naming, publication, SoTA, semantic repair, or characteristic spaces. | The pattern can be applied to itself at the lowest sufficient layer without recursive bundles, infinite review, or self-certifying authority. |

#### E.21:4.4 - DominanceSet, TieBreakerSet, TelemetrySet

`DominanceSet` names the subset of activated characteristics selected for the current `ClaimScope`. The coordinate menu in `E.21:4.3` is not one always-on grid.

For one first ordinary read of one target pattern version, the minimal active coordinates are:

- `WorkingSituationAndUseBoundaryRecognizability`;
- `ActionPathGuidance`;
- `GovernedObjectAndClaimScopeStability`;
- `NeighborAuthorityAndBoundedUseFit`;
- `PracticalUseDeltaAndHarmPrevention`;
- `UseAffordabilityAndApparatusProportionality`.

For admission, stop, repair-before-use, or narrowed-use closure, add the ordinary stop core coordinates:

- `ClosureAndBoundedNonUseRecoverability`;
- `SemanticKindAndNameRecoverability` when names/kinds are load-bearing beyond eligibility minimum;
- `RepairLocalityAndChangeImpactPredictability` when an edit or repair is being judged;
- `ProxyForValueSubstitutionResistance` before any stop or comparison claim.

Activate claim-support, corpus/publication, front/refresh coordinates, and activated overlays only when the target pattern, candidate edit, or declared `ClaimScope` makes their load live.

Inactive coordinates are outside the current pattern-quality claim. They are not passes, waivers, or hidden failures.

A candidate pattern version `A` dominates candidate `B` only when:

1. both pass the active `EligibilitySet`;
2. `A` is no worse than `B` on every active dominance coordinate;
3. `A` is better on at least one active dominance coordinate; and
4. `A` does not create a new hard blocker, an unacceptable drop in `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, or `ProxyForValueSubstitutionResistance`, or an unacceptable unscored increase in reader, author, maintainer, migration, evidence, entry/projection, corpus, or neighbour-integration cost.

`TieBreakerSet` is used only among non-dominated candidates. Default tie-breakers are:

| Tie-breaker | Preference |
|---|---|
| `ExistingPatternReuse` | Reuse existing FPF patterns and fields when precision is equal. |
| `MintedNameParsimony` | Mint fewer durable names when semantic fidelity is equal. |
| `ReaderCost` | Lower first-use cost when action guidance and ontology precision are equal. |
| `AuthorCost` | Fewer required declarations when safety and reviewability are equal. |
| `MaintainerCost` | Lower refresh and relation-maintenance cost when quality is equal. |
| `EntryDiscoverability` | Better practical first-entry cues when local precision is equal. |

Cost tie-breakers are not a hiding place for live quality loss. If reader, author, reviewer, maintainer, migration, evidence, entry/projection, corpus, or neighbour-integration cost can change admissible use, represent it through `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, `ProxyForValueSubstitutionResistance`, or another active coordinate before using tie-breakers.

**Support material retention test.** A support card, telemetry fixture, archive row, worked slice, proof sketch, or companion note remains attached to the pattern-quality read only when the read states what real quality breakage would return if it were absent.

If no breakage is named, fold the useful content into the pattern body, keep it as accepted basis only, or remove it from the active quality read.

**High-assurance separation rule.** When high-assurance reuse needs stronger evidence, proof sketches, telemetry, or support cards, preserve the ordinary pattern body's first admissible move unless the ordinary use itself changes.

High-assurance material should normally live in a named support card, worked slice, or neighbouring evidence/assurance pattern. It should not be inserted into the ordinary `Solution` if doing so makes first use harder for the declared ordinary reader.

`TelemetrySet` is optional for early drafts and useful for mature or high-use patterns. Telemetry is an activation signal for reopening or calibration, not a standing requirement for every pattern-quality read. Typical telemetry includes:

| Telemetry | Reopen signal |
|---|---|
| `reviewReturnDensity` | P1/P2/P3 findings per pattern or per 1k lines are not falling. |
| `repeatFindingRate` | The same defect class returns after repair. |
| `coldReaderMisentryRate` | Readers choose the wrong first pattern or wrong neighbouring exit. |
| `retrievalHitQuality` | Search or RAG finds the wrong pattern, wrong section, or unsupported summary. |
| `neighborBreakageCount` | A pattern change repeatedly forces downstream repairs. |
| `patternUseAvoidanceSignal` | Readers avoid the pattern, copy only fragments, or return to informal shortcuts because the quality apparatus is too costly. |
| `maintenanceRippleSignal` | Small pattern repairs repeatedly force unrelated name, relation, evidence, or support edits. |
| `proxyOptimizationSignal` | Edits improve checklist or coordinate wording while first-use failures, return findings, or practical-payoff complaints persist. |
| `workedCaseCoverageDelta` | Edits polish wording without adding or preserving live case coverage. |
| `terminologyCollisionCount` | New names collide with existing FPF heads or kinds. |
| `SoTAStalenessSignals` | Current-practice claims now depend on stale or superseded anchors. |

Refresh opens the smallest live locus: the affected source stance, neighbour relation, coordinate reading, worked case, name, eligibility row, or status payload. It reopens the whole pattern-quality read only when that local change can change `PatternQualityStatus` or `StopCondition`.

#### E.21:4.5 - StopCondition

Improvement can stop for the declared scope only when the `PatternQualityQBundle` satisfies:

```text
StopCondition :=
  EligibilitySet passes
  AND the target text is an action-guiding FPF pattern under E.8 for the declared use
  AND the first move is recoverable from Problem frame and Solution, or the claim is narrowed to support-only use
  AND no open P1/P2 pattern-quality findings for the declared ClaimScope
  AND all active DominanceSet coordinates meet the declared floor
  AND no active coordinate is 0 or 1 for a use the pattern claims to support
  AND the current candidate is non-dominated on the active DominanceSet
  AND the next proposed edits are TieBreaker-only or cosmetic for this scope
  AND no active improvement creates unmeasured usability, affordability, repair-impact, entry/projection, corpus-ecology, or neighbour-ripple loss outside the DominanceSet
  AND remaining weaknesses are expressed as bounded non-use or a named receiving pattern
  AND TelemetrySet, when active, shows no recurring blocker class
```

No stop condition may close while a visible coordinate improvement creates unmeasured loss in first-use cost, reader comprehension, maintainer locality, neighbour stability, bounded non-use clarity, or practical payoff.

The ordinary floor for an admission-ready pattern is `3 sufficientlyExpressedForDeclaredUse` on every active coordinate. A lower coordinate may remain only by narrowing `ClaimScope`, `WorkingReaderScope`, or `IntendedUse`; it is not hidden in an average.

#### E.21:4.6 - PatternQualityFront and PatternImprovementArchive

A `PatternQualityFront` is live only when at least two candidate versions or candidate edits are being compared.

A `PatternImprovementArchive` is live only when preserving rejected or near-miss variants changes future repair, refresh, or selection.

Do not create either construct for a single ordinary repair unless a candidate comparison or contested stop decision is already live.

When these constructs are live, keep:

| Construct | Meaning |
|---|---|
| `PatternQualityFront` | The current non-dominated set of pattern candidates under the active `EligibilitySet`, `DominanceSet`, and cost coordinates. |
| `PatternImprovementArchive` | A bounded archive of candidate edits, rejected variants, near-miss versions, and trade-off notes that explain why one candidate was not selected. |

This is the pattern-quality analogue of NQD/front discipline. It prevents "one winner" thinking while still allowing one candidate to be selected for the current `ClaimScope`.

The archive is not required for every small edit. It becomes useful when several plausible versions trade off `SemanticKindAndNameRecoverability`, reader cost, `SoTABindingAndCurrentness`, `CaseCountercaseAndTransferCoverage`, `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, or `ProxyForValueSubstitutionResistance`.

`PatternImprovementArchive` records candidate-edit trade-off evidence only. It is not chat memory, process chronology, review history, backlog, or permanent appendix.

#### E.21:4.6a - No forced winner

When several candidates are non-dominated under the active `EligibilitySet`, `DominanceSet`, and cost coordinates, `E.21` SHALL NOT force one winner unless the declared `IntendedUse` requires one selected candidate.

If ordinary drafting, exploration, or architecture discussion remains live, the admissible output may be a scoped `PatternQualityFront` with each candidate's bounded use and known trade-off. A single selected version is required only when admission, landing-support, release-support, high-assurance reuse, or another receiving action requires one candidate by value.

Choosing one candidate from a non-dominated front requires either:

* a declared `TieBreakerSet` that does not override hard blockers or live quality loss;
* a narrowed `ClaimScope` or `WorkingReaderScope`;
* a named neighbouring decision pattern when the choice is no longer a pattern-quality read.

#### E.21:4.7 - Relationship to E.19

`E.21` supplies the characteristic space and stop condition for pattern-quality claims. `E.19` supplies the review profile, findings-first run record, and admission/refresh outcome.

Use them together this way:

1. Use `E.8` to author the pattern.
2. Use `E.21` to state the quality bundle and non-scalar stop condition.
3. Use `E.19` to run the selected review profiles and record findings.
4. If an `E.19` finding changes the quality read, update the `PatternQualityQBundle`; do not turn the `E.19` verdict into a scalar score.

An `E.19` pass, return, or absence is not itself a coordinate value. It may supply evidence about the pattern text, expose a content defect, support a confidence judgement, or constrain the admissible `ClaimScope`; it does not make the same `FormalClaimLegalityAndLensFit`, `SemanticKindAndNameRecoverability`, `ActionPathGuidance`, or `ClosureAndBoundedNonUseRecoverability` stronger or weaker by administrative state alone.

Do not call an `E.21` `EligibilitySet`, `PatternQualityStatus`, `StopCondition`, or coordinate floor a gate. `E.21` states a scoped pattern-quality read. `E.19` runs pattern-quality review profiles. `A.21` governs operational gate decisions. These three uses do not collapse by metaphor.


An `E.21` result is still a pattern-quality result. It is not project evidence, safety certification, gate passage, assurance acceptance, work authority, release approval, or publication truth unless the exact receiving pattern opens that project-side relation.

#### E.21:4.8 - Minimal PatternQualityQBundle card
**Ordinary first-pass slice.** This is not a new kind. It is the smallest admissible slice of `PatternQualityQBundle` for one first read of one target pattern version.

```text
PatternQualityQBundle / first-pass slice:
  PatternVersionRef:
  WorkingReaderScope:
  IntendedUse:
  QualificationWindow:
  FirstMoveEvidenceRef: <Problem frame / Solution / named neighbouring handoff>
  EntryBlockers: <none | first move absent | governed object drift | checklist-as-solution | apparatus overreach | neighbour overread | other activated blocker>
  MinimalDominanceSet: <default six coordinates, plus activated coordinates if live>
  PatternQualityStatus:
  Next admissible repair or bounded non-use:
```

The full one-screen card is used when the first-pass slice survives or when the declared use requires coordinate evidence, variant comparison, admission, refresh, high-assurance reuse, or contested stop.

The fuller card remains one screen when Layer 1, comparison, admission, refresh, high-assurance reuse, or contested stop makes it live:

```text
PatternQualityQBundle:
  PatternVersionRef: <pattern id + edition or host path>
  ClaimScope: <ordinary authoring support quality read | admission-support quality read | refresh-support quality read | landing-support quality read | external-review-support quality read | high-assurance-reuse support quality read | ...>
  WorkingReaderScope: <primary reader + first-use situation>
  IntendedUse: <what this quality read may support>
  QualificationWindow: <edition / SoTA / neighbour / release window>
  EligibilitySet: <pass/fail rows with blockers>
  DominanceSet: <selected coordinates + floor>
  CoordinateEvidenceRefs: <text sections, worked cases, SoTA rows, relation checks, or findings that support coordinate values; not placement/review state alone>
  PatternQualityStatus: <value set from E.21:4.1>
  StopCondition: <satisfied | not satisfied, with exact reason>
  EvidenceRefs: <worked cases, SoTA rows, review refs, source refs>
```

#### E.21:4.8a - Publication and projection boundary for quality cards

A rendered `PatternQualityQBundle`, first-pass slice, quality table, status badge, or dashboard tile is a publication or projection of the pattern-quality read. It is not the target pattern, not the authority source, not project evidence, not release approval, not gate passage, and not assurance acceptance.

When the rendered card is used as a bounded publication unit, the card SHALL keep visible:

1. the exact `PatternVersionRef`;
2. the carried move: scoped pattern-quality read, first-pass slice, variant comparison, stop/non-stop reason, or bounded non-use;
3. the outside boundary to project evidence, assurance, gate, release, work, and publication truth;
4. the exact receiving pattern when a downstream claim is live.

A ToC row, `J.4` row, README note, dashboard tile, or generated summary may echo an `E.21` result only as a thin orientation cue unless it cites the full governed quality read by value.

Generated summaries, retrieval snippets, README lines, ToC reminders, and `J.4` entries may expose an `E.21` result only as `thin echo` or controlled coarsening.

A thin echo may say:

* `<PatternVersionRef> has PatternQualityStatus = repairBeforeUse for ordinary use because first move is absent. See <quality read ref>.`

A thin echo SHALL NOT say:

* `approved pattern`;
* `safe pattern`;
* `compliant pattern`;
* `quality passed`;
* `do not use this pattern` without scope;
* `E.21 certified this pattern`.

If a generated or coarsened rendering is used for reliance beyond orientation, route to `A.6.3.CSC`, `E.17.EFP`, `E.17.AUD`, `A.10`, or `B.3` as live.

#### E.21:4.9 - Reader move loop

The fast entry loop for one target pattern version is:

1. write the target line: `<PatternVersionRef> for <WorkingReaderScope> under <IntendedUse> within <QualificationWindow>`;
2. read only the target pattern's `Problem frame` and `Solution` until one first admissible action-guiding move is recoverable;
3. if no first move is recoverable, or if the move lives only in the Conformance Checklist, assign `PatternQualityStatus = repairBeforeUse` for the declared use unless a narrower support-only use is explicitly named;
4. if the first move is recoverable, check the default six first-pass coordinates and any activated coordinates;
5. expand to the full comparison and stop loop only when a stop decision, variant comparison, admission, refresh, high-assurance reuse, or contested neighbour claim is live.

The full comparison and stop loop is:

1. name the exact `PatternVersionRef`;
2. declare `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`;
3. check activated `EligibilitySet` rows before comparing coordinates;
4. read each active coordinate from `CoordinateEvidenceRefs`, not from administrative state;
5. ask what became worse when the visible coordinates improved: first-use affordability, author/reviewer effort, repair-impact predictability, entry/projection integrity, corpus ecology, neighbour ripple, and proxy-for-value substitution;
6. compare candidates through `DominanceSet` only after eligibility passes and Goodhart-risk questions are visible;
7. use `TieBreakerSet` only among non-dominated candidates;
8. assign one `PatternQualityStatus`;
9. state whether `StopCondition` is satisfied or which bounded non-use, receiving pattern, or content repair remains.

If the reader cannot recover the fast-entry result for one pattern version, activated `firstMoveRecoverability` fails for ordinary use even when the prose is polished. If the first move is recoverable but the reader cannot continue the admissible action path, `ActionPathGuidance` is below `4 wellExpressedForDeclaredUse` for ordinary use. If the reader cannot perform the closure and bounded non-use loop when that loop is live, `ClosureAndBoundedNonUseRecoverability` cannot support stop closure for that declared scope.

#### E.21:4.10 - CoordinateEvidenceRefs support card

`CoordinateEvidenceRefs` may be inline section references, short claims, review findings, worked slices, or full support cards. Full support cards are required only when the coordinate value is contested, reused for high-assurance closure, used across several candidate variants, or cited outside the local pattern-quality read.

`CoordinateEvidenceRefs` is the local evidence list for coordinate values. It is support for coordinate readings, not a coordinate family by itself.

`CoordinateEvidenceRef := <Coordinate, EvidenceKind, HostSectionRef, Claim, Limitation, LoweringCondition?>`

`LoweringCondition?` is required only when a coordinate value is `4` or `5`, or when the coordinate supports `admissibleForDeclaredUse` or `StopCondition`.

It states one concrete content discovery, reader failure, neighbour conflict, SoTA change, worked-case counterexample, cost increase, entry/projection overread, corpus-ecology conflict, or affordability loss that would lower the coordinate or reopen the read.

A lowering condition is not a test suite and not a review plan. It is a falsifiability hook for the current pattern-quality claim.

Default evidence kinds:

| EvidenceKind | Use |
|---|---|
| `recognitionTextEvidence` | Shows why a working reader can recognise the situation, boundary, and first move. |
| `namePrecisionCardEvidence` | Shows why a minted or load-bearing token has a recoverable kind, relation load, admissible use, and non-admissible use. |
| `relationClosureEvidence` | Shows that neighbouring-pattern claims stay with their governing patterns. |
| `workedCaseEvidence` | Shows the coordinate in a positive case, near-miss, anti-case, countercase, transfer case, or heterogeneous application case. |
| `sotaImplicationEvidence` | Shows how a source changes `Solution`, checklist, relation, boundary, worked case, stop condition, or reopen condition. |
| `measurementScaleEvidence` | Shows Characteristic/Scale/Coordinate discipline and blocks illegal arithmetic. |
| `costAndUseEvidence` | Shows first-use, author, reviewer, maintainer, migration, entry/projection, corpus, or ordinary-use cost under the declared scope. |
| `maintenanceRippleEvidence` | Shows whether one pattern repair creates unnecessary cross-FPF relation, naming, support, evidence, entry, or projection churn. |
| `proxySubstitutionEvidence` | Shows whether a coordinate increase preserves the practical value the coordinate was meant to protect. |
| `supportBoundaryEvidence` | Shows the difference between pattern-quality evidence and project-side evidence, assurance, work, gate, release, or publication truth. |
| `entryProjectionEvidence` | Shows how ToC/J.4/Preface/search/RAG/summary/card/dashboard cues preserve the governed pattern-quality read without replacing it. |
| `corpusEcologyEvidence` | Shows whether the edit changes relation fanout, name collisions, support-role parity, entry-map clarity, stale echoes, or neighbouring authority. |
| `loweringConditionEvidence` | Shows what discovery, failure, countercase, conflict, stale source, or cost increase would lower a high coordinate or reopen the status/stop claim. |

`entryProjectionEvidence` and `corpusEcologyEvidence` are active only when the candidate edit changes durable names, relations, ToC/J.4/Preface entry support, retrieval-facing cues, support projections, summaries, cards, dashboards, or neighbouring-pattern authority. They are not required for local wording repair.

Example support card:

```text
CoordinateEvidenceRef:
  Coordinate: FormalClaimLegalityAndLensFit
  EvidenceKind: measurementScaleEvidence + workedCaseEvidence + sotaImplicationEvidence
  HostSectionRef: E.21:4.3, E.21:4.12, E.21:11
  Claim: Q-Bundle + ordinal characteristic space + Pareto/front lens preserve the comparisons needed for pattern improvement while rejecting scalar averages.
  Limitation: Not a statistical estimator, project assurance result, or tool mandate.
  LoweringCondition: If an E.21 edit permits arithmetic averaging of ordinal coordinate values, lower this coordinate to <=2 for ordinary use.
```

#### E.21:4.10a - Pattern-quality finding sentence grammar

A pattern-quality finding is admissible only when it has this shape:

```text
Pattern-quality finding:
  Target: <PatternVersionRef>
  ClaimScope / reader / use / window:
  Finding kind: <eligibility blocker | coordinate reading | status payload | stop-condition failure | bounded non-use | neighbour-handoff>
  Exact E.21 locus: <EligibilitySet row | coordinate | status | stop clause>
  Content evidence: <HostSectionRef / worked case / SoTA row / relation check / review finding>
  Result: <PatternQualityStatus effect or coordinate value effect>
  First admissible repair or bounded non-use:
```

Forbidden finding shapes:

* `weak pattern`;
* `not FPF enough`;
* `quality low`;
* `review failed`;
* `needs more evidence`;
* `not safe/compliant`;
* `too complex`;
* `not ready`.

These are admissible only after rewriting into the exact `E.21` locus, content evidence, status effect, and first admissible repair or bounded non-use.

#### E.21:4.11 - Local name-precision cards for E.21 heads

These cards are local name-precision evidence for `E.21`; they are not a separate glossary. Coordinate names are defined in `E.21:4.3` and are not repeated here unless the token also names a local construct.

The `E.21:4.11` local name-precision cards are the local `F.18`-compatible settlement for `E.21` heads. They do not require separate full `Name Card` artifacts for ordinary use.

A full `F.18` Name Card is required only when an `E.21` head is reused outside `E.21`, collides with an existing FPF head, enters a UTS/Concept-Set row, or becomes a durable cross-pattern naming decision rather than a local field/value-set name.

| Token | Kind named | Relation load | Admissible use | Non-admissible use |
|---|---|---|---|---|
| `PatternQualityQBundle` | Q-Bundle specialization for one pattern-quality claim. | Binds pattern version, scope, coordinates, evidence, status, and stop condition. | State a scoped non-scalar quality read. | Universal maturity score, review verdict, release approval, or project certification. |
| `PatternQualityCharacteristicSpace` | CharacteristicSpace specialization for FPF pattern-quality coordinates. | Holds ordinal pattern-quality coordinates and their scale discipline. | Compare content properties of pattern versions. | Geometric space, administrative state map, or popularity ranking. |
| `EligibilitySet` | Set-valued hard-filter field inside `PatternQualityQBundle`. | Filters candidate versions before coordinate comparison. | Block hard defects before front reasoning. | Low-score region, soft preference list, review profile, or gate profile. |
| `DominanceSet` | Set-valued coordinate-selection field inside `PatternQualityQBundle`. | Defines the active Pareto comparison relation after eligibility passes. | Compare candidates without scalarization. | Total order, average, hidden priority stack, or selector policy. |
| `CoordinateEvidenceRef` | Local evidence-reference record for one coordinate value. | Connects one coordinate value to text, cases, SoTA, relation checks, or findings. | Justify one coordinate reading by content. | Administrative placement, review state, or project evidence by itself. |
| `CoordinateEvidenceRefs` | Set-valued field of `CoordinateEvidenceRef` records. | Holds the evidence refs for active coordinate readings. | Keep coordinate values inspectable. | Support archive, review verdict, or proof package. |
| `TieBreakerSet` | Set-valued secondary-preference field inside `PatternQualityQBundle`. | Breaks ties only after dominance cannot choose. | Prefer lower reader/author/maintainer cost when quality is equal. | Secret dominance coordinate or override for hard blockers. |
| `TelemetrySet` | Set-valued reopen/calibration signal field inside `PatternQualityQBundle`. | Connects return, retrieval, drift, and repeat-finding signals to refresh. | Reopen or calibrate the pattern-quality read. | Project certificate, popularity count, or replacement for content evidence. |
| `PatternQualityStatus` | Local admissible-use value set inside `PatternQualityQBundle`. | Names admissible use, narrowed use, repair, architecture decision, or refresh for the scoped pattern-quality claim. | Express the outcome of the bundle. | Gate passage, release state, role state, assurance acceptance, or project approval. |
| `PatternQualityFront` | Non-dominated candidate set under the active quality relation. | Preserves multiple viable candidates without one scalar winner. | Select among pattern versions or candidate edits. | Permanent backlog, generic archive, or mandatory tool artifact. |
| `PatternImprovementArchive` | Bounded archive of candidate edits and rejected variants. | Keeps trade-off evidence for selected/non-selected candidates. | Explain why one candidate was selected for a scope. | Process log, chat transcript, or mandatory historical appendix. |

**Plain twins for ordinary reading.** These Plain twins are reader aids only; the Tech head remains authoritative.

| Tech head | Plain twin | Guard |
|---|---|---|
| `PatternQualityQBundle` | pattern-quality read bundle | Not a review packet, score sheet, or gate file. |
| `PatternQualityCharacteristicSpace` | pattern-quality coordinate space | Not a metric dashboard or maturity model. |
| `PatternQualityStatus` | pattern-quality use posture | Not release status, gate decision, or assurance level. |
| `EligibilitySet` | hard blockers | Not low-score items. |
| `DominanceSet` | active quality coordinates | Not weighted criteria. |
| `CoordinateEvidenceRef` | coordinate support reference | Not project evidence by itself. |
| `PatternQualityFront` | non-dominated pattern-edit set | Not backlog or shortlist by itself. |
| `PatternImprovementArchive` | bounded pattern-edit trade-off archive | Not process log or permanent appendix. |

#### E.21:4.12 - Mathematical lens adequacy proof sketch

The mathematical lens in `E.21` is a finite ordinal characteristic-space lens plus a Pareto/front comparison over candidate pattern versions.

| Lens component | Preserved structure | Lost or rejected structure | Practical payoff |
|---|---|---|---|
| Q-Bundle tuple | Keeps pattern version, scope, evidence, coordinates, status, and stop condition together. | Rejects unscoped quality adjectives. | A quality claim can be inspected without reading chat memory. |
| Ordinal characteristic coordinate | Keeps coordinate identity and ordered levels. | Rejects cardinal distance, averages, percentages, and hidden normalization. | `3` and `4` mean content states, not arithmetic quantities. |
| Eligibility predicate | Keeps hard preconditions outside optimization. | Rejects averaging hard blockers into good coordinates. | Undefined vocabulary, shadow authority, or scale illegality blocks comparison. |
| Pareto dominance relation | Keeps non-dominated alternatives visible. | Rejects one universal total order. | Shorter, more exact, and more SoTA-rich variants can coexist until a scope chooses. |
| Tie-breaker preference | Keeps secondary preferences after non-domination. | Rejects secret reweighting of the main coordinates. | Reader cost or continuity can choose only when quality comparison does not. |
| Goodhart-risk check | Keeps the relation between coordinate improvement and intended pattern-use value explicit. | Rejects "all visible coordinates improved" as sufficient when use, affordability, repair locality, entry/projection integrity, corpus ecology, or neighbour fit got worse. | A quality read must ask what became worse before it can stop. |
| Front/archive pair | Keeps selected and non-selected candidate evidence bounded. | Rejects endless polishing and permanent process history. | Improvement can stop without losing important trade-off evidence. |

The lens is admissible because pattern quality is multi-characteristic, ordinal, and scope-dependent. It is not admissible for estimating user adoption, certifying project safety, proving product compliance, or assigning a universal quality number. The stop condition closes the lens: once eligibility passes, floors are met, the candidate is non-dominated, remaining weaknesses are bounded, no active coordinate improvement hides affordability, repair-impact, entry/projection, corpus-ecology, or neighbour loss, and live telemetry shows no recurring blocker class, additional edits must show a real front movement rather than a cosmetic preference.

