---
chunk_kind: "parent"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.10.ARCH.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
line_start: 59332
line_end: 59584
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.6.3.CSC"
  - "A.6.F"
  - "A.6.P"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.25"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
---

## E.10.ARCH - Wording-Use Ontological Precision Restoration Architecture

> **Type:** Architectural (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Wording ontology repair architecture.

**Intent.**
Keep FPF wording-use precision restoration distributed without letting every receiving pattern grow its own first-stage trigger registry. `E.10` catches one overloaded wording use; `E.10.ARCH` says which applicability rows exist, how one row selects the first applicable restoration or receiving pattern, and when repeated repair-only prose should be extracted from a subject pattern.

`E.10.ARCH` is not a generic language-cleanup pattern. Its mechanism is ontological reconstruction: recover what kind of thing is being talked about, which neighboring EntityOfConcern values, relation records, claim records, and exact FPF kinds or references are admissibly involved, which relation, source-use disposition, or state-family value is live, and, when plain ontology is not enough, which mathematical lens under `C.29` or which pattern-defined formal apparatus makes the candidate structure checkable. The output returns to wording only after that kind and use structure is recoverable.

**Builds on.** `E.10`, `A.6.P`, `A.6.F`, `C.2.P`, `C.30.STRAT`, `A.19.SPR`, `A.6.3.CSC`, `F.18`, `E.8`, `E.19`, and `E.2`.

**Coordinates with.** `A.22`, `C.30`, `C.30.P`, `C.30.STRAT`, `C.30.ASV`, exact `C.30.*` structure or view patterns, `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.27`, `C.29`, `E.21`, `J.4`, and exact evidence, assurance, gate, work, decision, causal-use, release, and publication patterns when those claims are live.

### E.10.ARCH:0 - Use this when

Use this pattern when a recurring FPF-governed wording-use problem cannot be closed by one local `E.10` rewrite because the wording hides a stable primary-EntityOfConcern use field set, a stable recovery apparatus, and a useful remaining reader move.

Use it especially when a subject or adequacy pattern contains repeated first-stage repair prose such as:

- architecture-vs-diagram, model, graph, ADR, dashboard, view, layer, level, tier, stack, block, expert, cache, router, or gate triage before the architecture, structure, control, module-interface, flow, scale, publication, or gate pattern can start;
- axis, dimension, feature, property, metric, indicator, score, strong, weak, robust, level, coordinate, threshold, or scalar-quality triage before a characteristic or scale pattern can start;
- quality-term repair that decides between relation construction, quality characterization, evaluative characterization, Q-bundle use, pattern-quality coordinate use, action invitation, bridge, or exact receiving pattern;
- state-family wording such as state, status, posture, readiness, stance, or currentness before the bearer, state frame, value set, admissible use, or exact receiving pattern is recovered;
- source, publication, carrier, face, `PublicationUnit`, dashboard, documentation, or source-return wording whose project-side use is not yet recovered;
- relation-like, function-like, evidence-like, assurance-like, gate-like, work-like, decision-like, causal-use, release, or naming wording whose exact receiving pattern is already known or must be recovered before the sentence is admitted.

**What goes wrong if missed.** FPF accumulates many small local trigger lists. One pattern says "architecture is not a diagram", another says "metric is not proof", another says "quality is not one scalar", and a reviewer cannot tell which pattern carries the repair. The text looks more precise, but the reader does not get a stable first move.

**What this buys.** `E.10.ARCH` gives one architecture for distributing wording-use repair: `E.10` catches; `E.10.ARCH` selects the row and extraction criterion; a realization pattern or exact neighbor recovers the ontology; the subject pattern returns to its own primary `EntityOfConcern` and first useful move.

**First useful move.** Decide whether the wording can close locally under `E.10`, already has an exact receiving pattern, or needs one applicability row with stable `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `ontologicalNeighborhood`, recovery apparatus, and remaining reader move.

**Not this pattern when.**

- If a sentence is repaired locally under `E.10`, stop there.
- If the exact receiving pattern and primary `EntityOfConcern`, exact relation, or claim record are already recoverable by value, use that receiving pattern directly.
- If the live kind is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, grounded architecture adequacy, structural-view adequacy, characteristic-space construction, Q-bundle construction, pattern-quality evaluation, or another exact FPF kind, the exact receiving pattern governs its own invariant. `E.10.ARCH` only governs the wording-use restoration distribution.

### E.10.ARCH:1 - Primary EntityOfConcern and applicability-row scope

The primary `EntityOfConcern` for this pattern use is the local FPF architecture of `WordingUseRestorationApplicabilityRow` rows.

A `WordingUseRestorationApplicabilityRow` is a pattern-local row over one `semanticAreaBaseConcept`, one `semanticArea`, one `semanticAreaSenseFamily`, one recurring `entityOfConcernUseFields` field set, and one `ontologicalNeighborhood`. It states:

- the trigger source recognized by `E.10`;
- `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`;
- the primary `EntityOfConcern` kind and encountered FPF kind or reference;
- the relation between the encountered FPF kind or reference and the primary `EntityOfConcern`;
- the exact FPF kind or relation recovered when live;
- live-claim or admissible-use classification when live;
- source-use disposition when live;
- state-family value or exact receiving-pattern result when live;
- sentence role;
- admissible use;
- non-use boundary;
- remaining reader move;
- first applicable restoration or receiving pattern;
- recovery product;
- first return to the subject pattern.

`WordingUseRestorationApplicabilityRow` is not a `U.*` kind, not a conformance record, not a process task, not a deontic obligation, and not a durable project record by itself.

`WordingUseRestorationApplicabilityTable` is the pattern-local publication table of such rows. It is not a pattern cluster, workstream, campaign, module, semantic parent, or authority-bearing record.

`semanticAreaBaseConcept` is the Base concept, source-side phrase, or already settled row cue by which the reader first recognizes the candidate semantic unit.

`semanticArea` is the Part-F semantic unit used by one wording-use restoration row: one Concept-Set row, one UTS row, or an explicitly bounded row-set whose rows remain sense-uniform enough for one recovery apparatus.

`semanticAreaSenseFamily` is the Part-F `senseFamily` or exact FPF kind-family discriminator that prevents the row from becoming a theme, domain, workstream, or pattern-nest label.

`ontologicalNeighborhood` means the FPF applicability neighborhood around that named `semanticArea`: primary `EntityOfConcern` kind, admissible adjacent FPF kinds or references, relations, descriptions, publication forms or carriers, source-use dispositions, state-family values, use boundaries, applicable FPF patterns, remaining reader move, and the stable apparatus that makes the recovery checkable. It is not the semantic unit by itself and is not textual proximity, filename proximity, ToC proximity, alphabetic proximity, workstream grouping, topic grouping, discipline column, domain label, or pattern-nest placement.

`pattern nest` means a numbering or placement grouping such as `A.6.*`, `C.16.*`, or `C.30.*`. One applicability row may point to a realization pattern in one pattern nest, but the row and the nest are not the same concept.

### E.10.ARCH:2 - Distribution architecture

The standing construction is:

1. `E.10` catches an FPF-governed wording use and either closes it locally or selects an exact receiving pattern, controlled precision-reduction pattern, durable-name path, or fail-closed non-use disposition.
2. `E.10.ARCH` maintains the shared recovery algorithm and the `WordingUseRestorationApplicabilityTable`.
3. A realization pattern or retained exact pattern such as `A.6.P`, `A.6.F`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, or `A.19.SPR` unpacks the wording according to the shared algorithm for one named `semanticArea` and its `ontologicalNeighborhood`.
4. Additional applicability rows, and only when needed additional realization patterns, appear when repeated FPF-governed wording hides a stable primary-EntityOfConcern use field set, a stable recovery apparatus, and a useful remaining reader move that no existing exact pattern already carries.
5. `E.8` governs publication-form and placement wording such as `pattern nest`, and requires authoring prose that uses `ontologicalNeighborhood` to expose the governing `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily` rather than treating neighborhood as the semantic unit.
6. `E.19` checks that authored pattern hosts preserve this distribution and do not keep rival first-stage repair doctrine.

This architecture keeps `E.10` compact. It also keeps subject receiving patterns centered on their own primary EntityOfConcern values, decisions, characteristics, structures, mathematical lenses, consequences, and worked uses.

#### E.10.ARCH:2.1 - EntityOfConcern and recurring hidden-field distribution

For wording such as `EntityOfInterest`, `EoI`, `EoIClass`, `describedEntity`, `DescribedEntityRef`, and `primary described entity`, or for selected EntityOfConcern-family heads such as `EntityOfConcern`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernClass`, and `publicationUnitPrimaryEntityOfConcern`, the repair is distributed by the live FPF-governed use:

`EntityOfInterest`, `EoI`, `EoIClass`, `describedEntity`, `DescribedEntityRef`, and `primary described entity` are active repair triggers. FPF-governed wording must recover the exact EntityOfConcern-family use, publication-unit primary-EoC use, or local FPF kind, then rewrite to `EntityOfConcern`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the exact local FPF kind. If no exact use is recoverable, the wording remains quoted source or trigger wording and cannot be used for reliance.

- `C.2.1` carries the selected episteme slot and reference ontology: `EntityOfConcernSlot`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernChangeMode`, and `EntityOfConcernClass`.
- `C.2.P` carries episteme, publication, and source-use precision restoration when the sentence still hides source wording, claim-bearing episteme, publication or carrier construction, project-side reliance, pattern-application wording, or use or non-use disposition.
- `F.18` carries durable naming, selected head settlement, and source-string and durable-name discipline after the live kind and use are recovered.
- `E.17.AUD.OOTD` carries `publicationUnitPrimaryEntityOfConcern` for one bounded publication unit with one carried move and one outside-work boundary; it must not create a second C.2.1 slot.
- `A.6.3`, its retained `entityOfConcernRef`-preserving specializations, and `A.6.4` carry preservation or retargeting of the EntityOfConcern across episteme morphisms.
- Exact evidence, assurance, gate, work, decision, architecture, characteristic, mathematical-lens, or project-side patterns receive their own live claim or admissible-use boundary directly when it is already recoverable.

This selected-family case is the standing example for recurring hidden-field architecture. When a new hidden-field family recurs, it is not solved by adding local warning prose to every subject pattern. It either uses an existing exact receiving pattern, receives one applicability row in this table, or justifies a new realization pattern only when the hidden field set, recovery apparatus, and remaining reader move recur across FPF-governed texts.
### E.10.ARCH:2a - Rationale and source-use lines

This distribution is selected because the recurring failure is not "too few word rules". The failure is that repair-only trigger prose migrates into subject patterns and begins to compete with their primary `EntityOfConcern` and first useful moves. A common symptom is a non-semio pattern whose Solution mainly teaches that a description, view, publication, record, card, diagram, source, or file is not a permission, promise, prescription, evidence record, assurance verdict, decision, gate passage, release, work occurrence, or authority source. Those guards are often correct, but their ontology is publication pragmatics, description pragmatics, and exact neighboring-pattern assignment, not the subject matter of the architecture, method, role, evidence, or characterization pattern. A workable FPF answer therefore needs three separations at once: a cheap shared trigger scan in `E.10`, a shared recovery architecture in `E.10.ARCH`, and local realization only where a named `semanticArea` has stable row identity, a stable field set, an `ontologicalNeighborhood`, and a remaining reader move.

| Source or practice line | Source-use role | What the line changes in `E.10.ARCH` |
| --- | --- | --- |
| Current FPF distribution: `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.F`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, `A.19.SPR`, `F.18`, `E.8`, `E.19`, and `J.4`. | Current FPF-internal architecture source line for the selected distribution. | Keeps `E.10` compact, puts the shared recovery algorithm in `E.10.ARCH`, sends relation, source-use, architecture, stratification-source-label, characteristic, quality, state-family, function-like, and naming cases to exact realization or receiving patterns, and gives `E.19` a distribution-preservation check. |
| Pattern-language locality and FPF primary-EntityOfConcern discipline in `E.8` and `E.19`. | Current FPF authoring and review source line; not an external standard imported as ontology. | Forces thin receiving-pattern pointers and blocks local trigger-registry copies inside subject patterns whose real work is architecture, structure, characteristic, quality, evidence, gate, work, decision, state-family precision, or release. |
| Terminology and controlled-vocabulary practice named in `E.10:11a` only where it concerns designations, labels, discoverability, and controlled vocabulary publication. | Current-standard and reference-use source line; it does not define FPF kind ontology. | Provides explicit recovered heads and reusable-name discipline, but rejects a central word list or controlled vocabulary as the solution to every wording-use repair. |
| Current exact receiving-pattern growth in FPF. | Reopen pressure, not proof of this pattern's authority. | Requires a row to be removed, narrowed, or changed when a new exact receiving pattern can carry the live EntityOfConcern, relation, claim, or local field directly, or when realization patterns start copying the shared algorithm back into local prose. |

The selected architecture is lowered or reopened when one of those source lines changes: if `E.10` can close the issue locally, if a new exact receiving pattern removes the need for a restoration row, if a realization pattern needs a different stable field set, or if subject patterns again start carrying duplicated first-stage trigger registries.
### E.10.ARCH:3 - Shared recovery algorithm

Use this recovery order for FPF-relevant wording-use restoration cases. Each realization pattern may publish a compact local form, but the order stays shared.

1. **Trigger and bounded text.** Name the bounded text span or publication unit, exact trigger span, local sentence role, register classification, and whether the text is conformant FPF, project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims, or source text being unpacked for possible FPF use.
2. **Cheap local closure.** Check whether the wording has no FPF-governed use or only a small local head, register, or morphology repair. If yes, repair locally under `E.10`, state the remaining reader move, and stop.
3. **Head kind and candidate ontology.** Recover the head kind, register classification, EntityOfConcern and Description-episteme boundary, specification-use gate when live, candidate referents, candidate EntityOfConcern values, exact relation records, claim records, candidate relations, candidate carriers or publications, and live scope, time, viewpoint, or context facets. Include literal and intended candidates when metonymy or compression is plausible.
4. **Semantic area, ontological neighborhood, and receiving-pattern selection.** State `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`; then select the `ontologicalNeighborhood` and first applicable receiving pattern by primary `EntityOfConcern` kind and admissible adjacent FPF kinds, references, or relations: relation construction, function-like exact-kind and relation recovery, episteme, publication, source-use, selected structure or architecture description, characteristic or scale construction, quality characterization, evidence, assurance, gate, work, decision, causal-use, naming, controlled coarsening, or another exact FPF pattern.
5. **Formal apparatus or stable substrate.** State the stable apparatus that makes the repair checkable: relation slots, publication relation set, source-use disposition, selected structure, architecture question, characteristic or scale construction, quality bundle, mathematical lens, evidence path, gate record, work occurrence, decision record, assurance argument, causal-use record, or exact receiving-pattern field set.
6. **Normalized ontology and lexical projection.** Produce the repaired wording, compact repair note, record-shaped value, exact receiving-pattern application, or non-use disposition. Do not replace one umbrella word with another. The replacement candidate is itself a bounded wording use until it passes the `E.10` trigger scan or is demoted to ordinary wording, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite.
7. **Admissible use and remaining reader move.** State the admissible use, non-admissible claim escalation or adjacent use, and one useful reader move. If the wording is type-correct but inert, the repair is incomplete.

The sequence is shared; each wording-use restoration case differs by `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, primary `EntityOfConcern` use fields, `ontologicalNeighborhood`, receiving pattern, substrate, and result.

### E.10.ARCH:4 - Applicability table

| Semantic area and ontological neighborhood | First applicable pattern | Trigger family | Required recovery apparatus | Typical recovery product |
| --- | --- | --- | --- | --- |
| Relation construction; primary recoverable use is relation use or relation-bearing claim | `A.6.P` and retained exact A.6 relation specializations | Relation, endpoint, qualifier, slot, scope, time, viewpoint, evidence-role distinction where live, basedness, service, bridge wording, whole or part, mapping, comparison, dependency, or evaluative ascription when the hidden claim is relation construction. | `RelationKind`, slot discipline, `QualifiedRelationRecord`, endpoint facets, qualifiers, L, A, D, and E hooks, and exact retained relation specializations. | relation rewrite, relation record, candidate-set note, exact specialization application, or fail-closed Plain disposition. |
| Function-like wording; primary recoverable use is the exact FPF kind, relation, or claim hidden by `function`, `functional`, `functionality`, `effect`, or similar wording | `A.6.F` first when the exact FPF kind, relation, or claim is not already recovered; direct exact receiving pattern when it is recovered by value | Functional architecture, required transformation or effect, method, work occurrence or result, role expectation, mathematical function, relation, loss, objective, quality or functionality claim, module allocation, interface or signature relation, or evidence, assurance, gate, or decision overread. | `FunctionUseRepair`, exact-kind and relation recovery, false-kind list, exact governing-pattern reference, `C.30` or `C.30.ASV` functional-structure boundary, `C.29` mathematical-lens boundary, `C.16` or `C.25` quality boundary, `A.6.M` module-interface exits and A.6 signature or slot exits. | exact FPF kind or relation assignment, exact receiving-pattern application, `FunctionFlowModuleAlignmentNote`, mathematical-lens exit, quality or characteristic exit, `A.6.M` module-interface exit, ordinary-prose demotion, or stop. |
| Episteme, publication, and source-use; encountered entity or construction may be source span, carrier, face, publication, `PublicationUnit`, EntityOfConcern-like head, old EntityOfConcern-family wording, or text-work evaluation cue | `C.2.P` first; exact evaluation pattern after recovery when live | Source-expression, episteme or publication wording, FPF-governed wording, `EntityOfConcern` or `describedEntity`-family wording, and `reading`, `read`, or `quality-read` wording when the word could mean source interpretation, publication use, FPF-governed use, or evaluation hidden inside text work. | source-expression clarification, FPF-governed use, claim-bearing episteme, EntityOfConcern, publication, view, face, carrier relation when live, `PublicationUnit`, `publicationUnitPrimaryEntityOfConcern` when live, use disposition, project-side exact kind or reference, sentence role, and exact evaluation claim or bundle when live. | local rewrite, compact epistemic precision-restoration row, full check, recovered-by-value, reduced-use, blocked-use disposition, exact neighboring-pattern application, or exact evaluation-pattern exit such as `E.22`, `E.21`, or `E.9.DA`. |
| Architecture and structure; primary recoverable use is selected structure, `ArchitectureOf@Context` relation, conditional `ArchitectureDescription@Context` use, structural view, or exact C.30 subcase | `C.30.P` | Architecture-heavy or structure-heavy wording whose live EntityOfConcern, relation, or claim is not yet recoverable. | `A.22` selected structure and structural-view discipline, `C.30` `ArchitectureOf@Context`, `C.30.ASV` structural-view and structure-kind discipline, exact C.30 subpattern exits, and `C.30.AD` only when full architecture-description mechanism is live. | architecture-structure repair note, repaired wording, selected-structure naming, architecture question, source-return condition, exact receiving-pattern result, ordinary-prose demotion, or stop. |
| Stratification and source labels; primary recoverable use is hidden behind `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, or close engineering source labels | `C.30.STRAT` when the exact receiving pattern is not already recovered; direct exact receiving pattern when it is recovered by value | Engineering, mathematical, publication, project, control, module, neural-network, or architecture prose uses a source label as if it named the FPF kind directly. | Source label, literal source wording, candidate primary EntityOfConcern, recovered receiving FPF kind, recovered relation, recovered claim-use, recovered source-use disposition, receiving-pattern selection, admissible use, non-use boundary, and adjacent exits to `C.30.P`, `C.30.LCA`, `A.6.M`, `C.30.TGA-FLOW-REL`, `C.16.P`, `C.29`, `C.2.P`, gate, work, or decision patterns, or ordinary source label. | `StratificationSourceLabelRepairNote`, direct exact receiving-pattern application, ordinary-prose demotion, quote-only, reduced-use, or blocked-use disposition, or stop. |
| Characteristic and scale; primary recoverable use is characteristic, scale, coordinate, score, comparison, indicator role, or characteristic-space construction | `C.16.P` | Characteristic, scale, coordinate, value, score, indicator, threshold, comparison, metric, axis, dimension, feature, property, level, strong, weak, robust, or benchmark wording whose construction is not yet recoverable. | `A.17` Characteristic, `A.18` CSLC, `C.16` measurement, unit, evidence stub, `A.19` `CharacteristicSpace`, `C.25` Q-bundle, `C.29` mathematical-lens boundary, and `E.21` pattern-quality coordinate discipline. | characteristic-scale repair note, declared `Characteristic`, `Scale`, `Coordinate`, `Value`, and `Score` construction, non-comparability, non-measurement, blocked-gate disposition, exact receiving-pattern result, ordinary-prose demotion, or stop. |
| Quality characterization and evaluative characterization; primary recoverable use is quality characterization, Q-bundle use, or pattern-quality coordinate use | `C.16.Q` | Quality or evaluative characterization wording when the hidden claim is not relation construction. | `C.16.P` where bearer or scale construction is hidden, `C.25` Q-bundle, `E.21` pattern-quality coordinates, and exact characterization or relation exits. | quality-term repair note, quality-bundle or pattern-quality coordinate use, relation or bridge split when live, blocked scalar, gate, or release overread, exact receiving-pattern result, ordinary-prose demotion, or stop. |
| State-family hidden claim; primary recoverable use is a bearer with a state-like value, status, readiness, currentness, or local finite field whose frame is hidden | `A.19.SPR` | State, status, posture, readiness, stance, currentness, validity, stable, accepted, blocked, candidate, admissible, ready, degraded, or close state-family compounds. | bearer kind, state frame or exact receiving pattern, value set or classification source, admissible use, non-admissible overread, validity window or reopen condition, and direct receiving-pattern exit for source, evidence, assurance, gate, work, decision, temporal, lens-use, pattern-quality, or process cases. | state-family repair note, exact retained local field, direct receiving-pattern application, quote-only cue, reduced-use cue, blocked use, ordinary-prose demotion, or stop. |
| Exact neighboring claim or admissible-use boundary already recoverable | Exact evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens, naming, controlled-coarsening, action-invitation, `A.6.M` module-interface, or other governing pattern | Any trigger family whose recovered FPF kind, relation, claim-use, source-use disposition, or admissible-use boundary is already exact. | Receiving pattern's own ontology and conformance fields. | Direct receiving-pattern application; no detour through a new restoration pattern. |

### E.10.ARCH:5 - Direct known receiving-pattern rule

If the exact receiving pattern and its primary `EntityOfConcern`, exact relation, or claim record are already recoverable by value, use that receiving pattern directly. Do not send direct `C.30`, `C.16`, `C.29`, `E.21`, evidence, assurance, gate, work, decision, causal-use, release, naming, controlled-coarsening, action-invitation, `A.6.M` module-interface, or mathematical-lens cases through a restoration pattern only because a familiar trigger word appears.

Apply `A.6.P`, `A.6.F`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, or `A.19.SPR` only when wording hides the live EntityOfConcern, relation, characteristic, scale, score, quality characterization, comparison reference set, source-use disposition, state-family value, admissible use, or remaining reader move.

### E.10.ARCH:6 - Admission and extraction criterion

Add or retain a `WordingUseRestorationApplicabilityRow` when all of the following are true:

- the wording recurs across FPF-governed texts or project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims;
- the hidden primary-EntityOfConcern use field set is stable;
- the recovery apparatus or field set is stable enough to teach;
- repeated in-place repair distracts from the subject pattern's primary EntityOfConcern and first useful move;
- a useful remaining reader move survives after overread removal;
- no existing exact receiving pattern already carries the row without duplicating repair-only doctrine inside subject patterns.

Do not add a new realization pattern when an existing exact pattern such as `A.6.F`, `A.6.A`, `A.6.M`, `A.15.4`, `A.6.6`, `A.6.3.CSC`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or another exact pattern already carries the live EntityOfConcern, relation, claim, or field. Record that pattern as the `receivingPattern`.

Extract repair-only material from a subject pattern when the material is only trigger lists, false-friend rows, anti-umbrella prose, or repair fields that must run before the subject pattern can start. Leave a narrow first-use cue or exact receiving-pattern exit in the subject pattern.

Keep material in the subject pattern when it states the subject pattern's own invariant, worked case, conformance condition, characteristic construction, structural construction, mathematical lens, source-return condition, or user action.

### E.10.ARCH:7 - Receiving-pattern thin-pointer rule

Receiving patterns keep at most one local first-use cue when the live EntityOfConcern, relation, claim, or field is hidden, then send the reader to the selected precision-restoration pattern. They do not copy:

- the full `E.10` trigger registry;
- this shared algorithm;
- the `WordingUseRestorationApplicabilityTable`;
- broad false-friend lists whose only job is first-stage repair;
- old migration history as live architecture prose.

A thin pointer is acceptable when it helps the working reader choose the right first move, for example:

- use `C.30.P` when architecture or structure wording hides whether the live use is selected structure, architecture-description use, structural-view use, source, model, diagram, graph, dashboard, or ordinary prose;
- use `C.30.STRAT` when `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, or a close source label hides whether the live use is a control-layer relation, module-interface relation, functional-flow relation, scale or coarse-graining relation, publication relation set, gate relation, exact neighboring use, ordinary source label, quote-only cue, or blocked use;
- use `C.16.P` when metric, score, axis, dimension, feature, property, indicator, strong, weak, robust, level, coordinate, threshold, or comparison wording hides characteristic or scale construction;
- use `C.16.Q` when quality or evaluative characterization wording hides Q-bundle, pattern-quality coordinate, relation construction, action-invitation, bridge, or exact characterization use;
- use `A.19.SPR` when state, status, posture, readiness, stance, currentness, or a local state-like field hides bearer, state frame, value set, admissible use, or exact receiving pattern;
- use `C.2.P` when source, publication, carrier, face, `PublicationUnit`, dashboard, documentation, or text-work wording hides source-currentness relation or project-side reliance.
### E.10.ARCH:8 - Name and placement discipline

`semanticArea` is the selected Part-F Tech term for the semantic unit used by a wording-use restoration row. Plain speech may say "semantic area" or "meaning area" only as a gloss for that declared Part-F row or bounded row-set.

`meaning area`, `theme`, `pattern area`, `pattern cluster`, `workstream`, `campaign`, `module`, and `branch` are not selected as Tech architecture terms for this distribution. Tech prose must resolve those cues into `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `entityOfConcernUseFields`, `ontologicalNeighborhood`, exact `receivingPattern`, and realization pattern.

`pattern nest` is allowed for ID and placement grouping such as `A.6.*`, `C.16.*`, or `C.30.*`. It is not a semantic parent relation and not an authority relation.

`ReceivingLocusObligationClosure` may appear only as the exact current `E.9.DA` coordinate name. It is not a general obligation kind, locus kind, or restoration vocabulary.

### E.10.ARCH:9 - Examples and near misses

| Wording | Applicable result | Blocked overread |
| --- | --- | --- |
| "The architecture is the diagram." | `C.30.P` recovers whether the diagram is publication or carrier, structure view, architecture description, or ordinary source cue; then `C.30` or `C.30.ASV` receives only after the selected architecture or structural-view use is recovered. | diagram-as-architecture; diagram-as-proof; diagram-as-gate. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless selected structure, architecture-description use, structural-view use, source use, model use, diagram use, graph use, dashboard use, or ordinary prose remains hidden. | unnecessary restoration detour. |
| "The model has three layers." | `C.30.STRAT` treats `layers` as a source label until the receiving FPF kind, relation, claim-use, or source-use disposition is recovered: control-layer relation, neural-network block sequence, publication relation set, mathematical scale or coarse-graining relation, or ordinary source wording. Then the exact receiving pattern receives the recovered result. | layer-as-universal-kind; source label as proof of structure. |
| "This score proves readiness." | `C.16.P` recovers characteristic, scale, value, score, threshold, comparison reference set, and gate, evidence, and decision exits. | score-as-proof; score-as-release permission. |
| "This source supports the claim." | `C.2.P` is used if source-currentness relation or publication relation set is live; relation slice applies `A.6.P`; final use states recovered relation or non-use disposition. | source-as-proof; support-as-generic relation. |
| "Quality improved." | `C.16.Q` recovers quality characterization or evaluative characterization, or exits to `C.16.P`, `C.25`, `E.21`, `A.6.P`, or exact action, work, or bridge patterns. | quality-as-one scalar; quality-as-gate. |
| "The function improved maintainability." | `A.6.F` first recovers the exact FPF kind, relation, or claim when hidden; quality or maintainability wording then goes to `C.16.P`, `C.16.Q`, `C.25`, or exact quality pattern when live. | function-as-default-architecture; maintainability-as-unscaled verdict. |
| "Read this pattern for improvement proposals." | Recover whether the live FPF-governed use is source-publication use, bounded comparative review unit, or improvement-oriented evaluation. Use `E.22` only for improvement-oriented quality review under a declared pattern-under-improvement evaluation. | generic reading as a pattern. |
| "This summary is enough for action." | `E.10` checks whether the wording is precision restoration or controlled precision reduction. If coarsened source-to-rendering use is live, `A.6.3.CSC` names source-bearing side, loss mode, narrower admissible use, non-admissible downstream use, and reopen condition. | summary-as-full source; coarsening without declared loss. |
### E.10.ARCH:10 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-E10ARCH-1` | `E.10` remains the compact trigger-and-applicability pattern; `E.10.ARCH` carries the shared algorithm and applicability-row architecture. |
| `CC-E10ARCH-2` | Each `WordingUseRestorationApplicabilityRow` names `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, primary EntityOfConcern kind and use fields, `ontologicalNeighborhood`, first applicable restoration or receiving pattern, recovery product, non-use boundary, and remaining reader move. |
| `CC-E10ARCH-3` | Direct known receiving-pattern cases use the exact receiving pattern directly instead of opening a restoration detour. |
| `CC-E10ARCH-4` | A new realization pattern is added only when no existing exact receiving pattern carries the stable recovery apparatus without duplicating repair-only doctrine inside subject patterns. |
| `CC-E10ARCH-5` | Subject receiving patterns keep their primary `EntityOfConcern` and first useful move central and carry only thin first-use cues to precision restoration when wording is hidden. Generic guards about description and publication use are kept in a named description and publication-use boundary section or exact description-publication neighbor; they do not become the subject Solution. |
| `CC-E10ARCH-6` | `reading`, `read`, and `quality-read` wording remains trigger wording and does not mint `ReadingPrecisionRestoration`. |
| `CC-E10ARCH-6a` | EntityOfConcern-like hidden fields follow the selected distribution: `E.10` catches, `C.2.1` carries slot and reference ontology, `C.2.P` restores episteme, publication, and source-use wording, `F.18` settles durable heads and source-string decisions, `E.17.AUD.OOTD` carries publication-unit primary entity of concern, and exact receiving patterns carry their own live claim or admissible-use boundary. |
| `CC-E10ARCH-6b` | State-family wording follows the selected distribution: `E.10` catches, `A.19.SPR` realizes recurring hidden bearer, state-frame, value, and use recovery, and exact receiving patterns receive already-recovered evidence, assurance, gate, work, decision, temporal, mathematical-lens, pattern-quality, source-use, or process cases directly. |
| `CC-E10ARCH-6c` | Stratification and source-label wording follows the selected distribution: `E.10` catches, `C.30.STRAT` realizes recurring source-label repair, and exact receiving patterns receive already-recovered control, module-interface, flow, scale or coarse-graining, publication relation set, gate, work, decision, or ordinary non-use cases directly. |
| `CC-E10ARCH-7` | `function`, `functional`, `functionality`, and `effect` wording keeps `A.6.F` as first unpacker when the exact FPF kind, relation, claim record, view, or receiving-pattern application is hidden and does not default to architecture. |
| `CC-E10ARCH-8` | `semanticArea`, `ontologicalNeighborhood`, and `pattern nest` follow `E.8` placement discipline: `semanticArea` is the Part-F semantic unit, `ontologicalNeighborhood` is its applicability neighborhood, and `pattern nest` is placement. None of them becomes workstream, campaign, module, or authority-bearing record. |
| `CC-E10ARCH-9` | Repair removes overread and preserves one useful admissible reader move. Type-correct but inert wording is not recovered by value. |
| `CC-E10ARCH-10` | Validation checks cover duplicate trigger tables, stale quality-term-restoration links, broad `U.*` heads, shadow restoration apparatus, and entry or index drift. |
### E.10.ARCH:11 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Classification without repair | The text says "this belongs under `A.6.P`" or "this belongs under `C.2.P`" but leaves no recovered wording, record, source-use disposition, direct exact pattern application, or blocker. | Apply the selected pattern or fail closed. |
| Trigger registry copying | `E.19`, `C.30.P`, `C.16.P`, `C.16.Q`, or a subject pattern copies the full `E.10` trigger list. | Keep one thin cue in the receiving pattern and point to `E.10` and `E.10.ARCH`. |
| Umbrella-to-umbrella replacement | `support` becomes `basis`, `surface` becomes `view`, `reading` becomes `evaluation`, or `function` becomes `role` without recovered kind and use. | Recover kind, relation, apparatus, admissible use, and remaining reader move; otherwise demote or block. |
| Sterile precision | The wording is ontologically well-formed but no working reader can tell why the distinction matters or what move remains. | Restore the didactic or recognition function in admissible wording, or classify as reduced-use cue, quote-only, blocked use, or incomplete rewrite. |
| Shadow precision-restoration pattern | A subject pattern contains its own first-stage repair algorithm beside this distribution. | Extract repair-only material to the applicable realization pattern and leave a first-use cue. |
| Legacy placement as live prose | Old placement or alias text explains history instead of current use. | Keep only migration or entry rows where needed; write current pattern prose in the selected live placement. |

### E.10.ARCH:12 - Related patterns

- `E.10` catches and closes local wording issues or selects the applicable row.
- `A.6.P` realizes the shared algorithm for relation construction and retained relation specializations.
- `A.6.F` realizes function-like exact-kind and relation recovery.
- `C.2.P` realizes source-expression, episteme, publication, and FPF-governed-use recovery.
- `C.30.P` realizes architecture and structure wording recovery.
- `C.30.STRAT` realizes stratification and source-label wording recovery for `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, and close source labels before exact receiving-pattern return.
- `C.16.P` realizes characteristic and scale wording recovery.
- `C.16.Q` realizes quality characterization and evaluative characterization wording recovery.
- `A.19.SPR` realizes state-family wording recovery when bearer, state frame, value set, admissible use, or exact receiving pattern is hidden.
- `F.18` governs durable reusable naming after the live kind or relation is known.
- `E.8` governs pattern-form and placement wording.
- `E.19` checks distribution preservation during review and refresh.
- `J.4` helps readers enter the correct pattern from broad or old terms.
### E.10.ARCH:End
