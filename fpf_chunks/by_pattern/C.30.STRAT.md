---
chunk_kind: "parent"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/C.30.STRAT.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
line_start: 52433
line_end: 52664
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "J.4"
keywords:
---

## C.30.STRAT - Stratification Wording Precision Restoration

> **Type:** Architectural precision-restoration subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Stratification and architecture-operation source-label repair.

**Intent.** Recover source wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, and `gate` by completing the `E.10.ARCH` recovery row for that wording use: `semanticAreaBaseConcept`, `semanticAreaSenseFamily`, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, encountered FPF kind or reference, relation to the primary `EntityOfConcern`, recovered kind, relation, or claim-use, source-use disposition, exact receiving pattern, admissible use, non-admissible use, and remaining reader move. No conforming `C.30.STRAT` use mints `U.Layer`, `U.Level`, `U.Tier`, `U.Stack`, `U.Ladder`, `U.Rung`, `U.Block`, `U.Expert`, `U.Cache`, or one universal `U.Stratification`.

**Builds on.** `E.10`, `E.10.ARCH`, `E.8`, `F.18`, `C.30.P`, `A.22`, and `C.30`.

**Coordinates with.** `C.30.ASV`, `C.30.LCA`, `C.30.TGA-FLOW-REL`, `C.30.ILC`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.16`, `A.19.SPR`, `C.2.P`, `E.17`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11`.

**E.10.ARCH receiver relation.** When `E.10` encounters a stratification or architecture-operation source label whose `ontologicalNeighborhood`, primary `EntityOfConcern` kind, recovered kind, relation, claim-use, source-use disposition, or exact receiving pattern is hidden, `E.10.ARCH` sends the case to `C.30.STRAT` only until those row fields are recovered or the wording is lowered to ordinary source label, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. `C.30.STRAT` then exits to the exact receiving pattern; it does not own the recovered architecture, module, flow, scale, publication, state, evidence, assurance, gate, work, decision, causal-use, or mathematical-lens claim.

### C.30.STRAT:0 - Use this when

Use this pattern when stratification or architecture-operation wording is doing FPF-governed work but the selected `ontologicalNeighborhood` and exact receiving pattern for the source-label use are not yet recoverable by value.

Typical source labels:

- `layer`, `level`, `tier`, `stack`, `ladder`, `rung`;
- `block`, `expert`, `cache`, `router`, `gate` when architecture-operation prose uses them as recognition labels before the FPF kind is known.

**What goes wrong if missed.** A source label starts acting as ontology. `Layer` may be taken as a holon level, control layer, publication layer, scale window, or module boundary without saying which neighborhood is live. `Stack` may become architecture by label. `Block` may become a module. `Expert` may become a role. `Cache` may become a memory relation or state. `Router` may become a decision policy. `Gate` may become a gate decision. None of those interpretations is admissible by word shape alone.

**What this buys.** The practitioner can keep useful source language while recovering the selected `ontologicalNeighborhood` and sending the case to the exact receiving pattern, instead of replacing the source label with another umbrella word.

**First useful move.** Treat the word as a `sourceLabel` and complete the recovery row: source label, bounded text, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, relation to that `EntityOfConcern`, recovered kind, relation, or claim-use, exact receiving pattern, admissible use, non-admissible use, and remaining reader move.

**Not this pattern when.** If the exact receiving pattern is already recoverable by value, use it directly. Do not open `C.30.STRAT` merely because a familiar word appears. If the wording is only ordinary source prose with no FPF-governed use, keep ordinary prose or quote-only wording and stop.

### C.30.STRAT:1 - Problem frame

Architecture and engineering sources use compact labels because they work in local practice. Neural-network architecture prose says `block`, `expert`, `cache`, or `router`. Control architecture says `layer`. Organizations say `level` or `tier`. Documentation says `section`, `stack`, or `view`. Mathematical and scale prose says `level`, `resolution`, or `coarse-graining step`.

Those labels are useful recognition cues, but FPF cannot rely on them as kinds. A label is not enough to know whether the next admissible move is module-relation repair, structure selection, functional-structure record, control-structure view, scale-window naming, source-publication return, or evidence, assurance, gate, decision, work, or causal-use assignment.

The repair question is:

> Which `ontologicalNeighborhood` does this source-label use belong to, and which exact receiving pattern now carries the recovered kind, recovered relation, recovered claim-use, source-use disposition, or non-use disposition?

### C.30.STRAT:2 - Problem

How can FPF keep common stratification and architecture-operation language without:

- minting false root kinds for `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate`;
- making `C.30` the universal receiving pattern for all structure-like wording;
- making `A.6.M` or `C.30.LCA` carry a duplicate local trigger registry;
- treating source labels as evidence, assurance, gate passage, decision, work, causal proof, modularity, architecture adequacy, or mathematical-lens success by appearance;
- removing useful source language before a remaining admissible reader move is recoverable?

### C.30.STRAT:3 - Forces

| Force | Tension |
| --- | --- |
| Source-language usability vs ontology | Practitioners need compact local words; FPF needs selected `ontologicalNeighborhood`, exact relation or claim-use, source-use disposition, and use boundary. |
| Pattern placement vs ontological neighborhood | The placement is in the `C.30` pattern nest because the recurring first confusion is architecture or structure wording, but its exits may be A.6, C.16, C.2, C.29, evidence, assurance, gate, work, decision, or ordinary non-use. |
| Thin repair vs shadow registry | Subject patterns need one pointer, not copied trigger lists. |
| Direct receiving pattern vs detour | If the relation, function-like use, control use, scale use, publication use, evidence use, or decision use is already exact, the exact receiving pattern starts directly. |
| Didactic payoff vs sterile precision | The repair is complete only when it leaves one useful move: exact receiving-pattern application, local rewrite, source return, ordinary source label, or blocked use. |

### C.30.STRAT:4 - Solution

Produce a `StratificationSourceLabelRepairNote` or an equivalent local rewrite. The note records the recovered `E.10.ARCH` row fields for this source-label use. It is not itself the selected structure, relation, claim record, source publication, gate record, work occurrence, decision, or mathematical-lens result.

```text
StratificationSourceLabelRepairNote:
  sourceLabel:
  boundedTextSpanOrPublicationUnit:
  localSentenceRole:
  encounteredSourceContext:
  semanticAreaBaseConcept:
  semanticAreaSenseFamily:
  selectedOntologicalNeighborhood:
  primaryEntityOfConcernKind:
  encounteredFPFKindOrReference:
  relationToPrimaryEntityOfConcern:
  recoveredKindRelationOrClaimUse:
  sourceUseDisposition:
  exactReceivingPattern:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderMove:
  disposition:
    exact-receiving-pattern | local-rewrite | ordinary-source-label |
    quote-only | reduced-use-cue | blocked-use | incomplete-rewrite
```

#### C.30.STRAT:4.1 - Recovery sequence

1. **Bound the text and label.** Name the sentence, table row, diagram label, publication unit, or source span; copy the source label; and state the local sentence role.
2. **Check cheap closure.** If there is no FPF-governed use, keep ordinary prose or quote-only wording and stop. If one small local rewrite restores the intended non-FPF use, close locally under `E.10`.
3. **Recover candidate ontology.** Recover candidate primary `EntityOfConcern` kinds, candidate encountered FPF kinds or references, relation candidates, claim-use candidates, source-use candidates, live scope, time, viewpoint, and context facets. Include literal and intended candidates when metonymy or compression is plausible.
4. **Select the ontological neighborhood.** Select the first applicable neighborhood by recovered relation, claim-use, source-use disposition, formal apparatus, or exact receiving-pattern field set, not by the source label.
5. **State the apparatus that makes the repair checkable.** Use relation slots, control roles and rate bands, module-interface fields, flow fields, transduction fields, characteristic and scale construction, publication relation set, source-use disposition, mathematical-lens fields, evidence path, assurance argument, gate record, work occurrence, decision record, causal-use record, or ordinary non-use disposition as live.
6. **Project back to wording.** Produce the repaired wording, compact note, direct exact receiving-pattern application, or non-use disposition. The replacement candidate is accepted only after it passes `E.10`.
7. **State use and move.** State admissible use, non-admissible wider or adjacent use, and one remaining reader move. If no move remains, the disposition is reduced-use, quote-only, blocked use, or incomplete rewrite.

#### C.30.STRAT:4.2 - Ontological-neighborhood exits

| Ontological neighborhood selected by recovery | Common source labels | Required recovery apparatus | First receiving pattern |
| --- | --- | --- | --- |
| Control-structure neighborhood | `layer`, `level`, `tier`, sometimes `gate` | Control role, control relation, rate band, bounded context, and, when live, B.2.5 supervisor-subholon relation. | `C.30.LCA` for control-structure view; `B.2.5`, dynamics, temporal, evidence, assurance, or gate patterns only when those claims are separately live. |
| Selected-structure or structural-view neighborhood | `layer`, `level`, `stack`, `block`, `view` | Selected structure, hidden structure, lost structure, preserved structure, structural-view selection, correspondence or source-return boundary, and `ArchitectureOf@Context` relation when live. | `A.22`, `C.30`, `C.30.ASV`, or exact C.30 subpattern. |
| Module-interface and substitution neighborhood | `block`, `cache`, `router`, `expert`, sometimes `layer` or `stack` | Module boundary, interface specification, substitutability relation, variation point, conformance relation, or module-interface reliance boundary. | `A.6.M`; not `C.30.STRAT` once the module-interface relation is recovered. |
| Function-like, flow, or transduction neighborhood | `block`, `expert`, `cache`, `router`, `gate`, sometimes `layer` | Transformation or effect claim, path-selection relation, graph node, graph path, graph crossing, transduction-flow relation, or flow valuation under E.18. | `A.6.F`, `E.18`, or `C.30.TGA-FLOW-REL`. |
| Characteristic, scale, or mathematical-lens neighborhood | `level`, `tier`, `ladder`, `rung`, `layer`, `stack`, `block` | Characteristic, scale, coordinate, value plus declared scoring method, comparison criterion or declared comparability relation, scale window, resolution, coarse-graining, preserved structure, lost structure, C.29 mathematical-lens result, and stop condition when live. | `C.16.P`, exact characterization pattern, or `C.29`. |
| Episteme, publication, view, or source-use neighborhood | `stack`, `layer`, `section`, `view`, `cache`, `gate` | Description episteme, publication unit, publication face, publication form, carrier, source-currentness relation, source-use disposition, source-return condition, or publication label. | `C.2.P`, `E.17`, or the exact publication or source-use pattern. |
| State, currentness, temporal, or dynamics neighborhood | `cache`, `stable`, `level`, `readiness`, sometimes `gate` | Bearer kind, state frame, value set, validity window, currentness relation, dynamics claim, temporal claim, or reopen condition. | `A.19.SPR`, `A.3.3`, `C.27`, or exact state pattern or temporal pattern. |
| Evidence, assurance, gate, work, decision, or causal-use neighborhood | `gate`, `proof`, `safety`, `decision`, `work`, `effect`, sometimes any source label used as authority | Evidence path, assurance argument, constraint-validity record, gate decision, work occurrence, decision record, causal-use record, and non-admissible overread. | `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or exact neighboring pattern. |
| Ordinary source-label non-use | any source label | No FPF-governed claim after context check; optional quote-only or reduced-use cue. | No precision-restoration receiving pattern opens; stop with ordinary wording, quote-only wording, or blocked use. |

#### C.30.STRAT:4.3 - Source-label cue table

| Source label family | Recovery discipline |
| --- | --- |
| `layer` | Do not choose by the word. Test control-structure, selected-structure or structural-view, module-interface, scale or mathematical-lens, and publication or source-use neighborhoods. |
| `level` | Test holon-level or aggregation use only when declared by an exact pattern; otherwise test characteristic or scale, ordinal classification, organization scope, work scope, evidence scope, publication grouping, or ordinary source-label non-use. |
| `tier` | Test deployment, service, organization, classification, aggregation, and publication neighborhoods. Exact deployment or service claims use their receiving patterns rather than `tier` as ontology. |
| `stack` | Test signature or slot construction, relation set or relation chain, architecture or control arrangement, aggregation arrangement, virtualization arrangement, deployment arrangement, publication-section ordering, or ordinary source-label non-use. A stack is not architecture by itself. |
| `ladder` and `rung` | Test ordinal or classification scale, declared maturity or readiness progression, C.28 causal-use ladder or rung, publication taxonomy, or ordinary source-label non-use. Do not use ladder wording for an undeclared progression scale. |
| `block` | Test module-interface or substitution, selected-structure or structural-view, function-like or flow, mathematical-lens or coarse-graining, evidence, causal-use, gate, and decision neighborhoods. |
| `expert` | In MoE-like prose, test submodel, subholon, specialized transformation, path-selection relation, candidate-selection relation, or actual role or enactment only when an `A.2` or `A.15` role or work claim is live. |
| `cache` | Test module-interface, flow buffer or path, state or currentness, capacity characteristic, latency characteristic, memory characteristic, reuse characteristic, source-currentness, publication cache, temporal claim, or ordinary source-label non-use. |
| `router` | Test path selection, flow relation, transformation function or selection function, module-interface relation, candidate selection, decision, or actual role or work only when that claim is live. |
| `gate` | Test constraint-validity record or gate-decision record, gating function, path selection, flow relation, publication label, or ordinary source-label non-use. A source label `gate` is not gate passage. |

#### C.30.STRAT:4.4 - Placement discipline

`semanticAreaBaseConcept`: stratification wording and architecture-operation source labels.

`semanticArea`: the Part-F semantic row-set used for `layer`, `level`, `tier`, `stack`, `ladder`, and `rung` plus architecture-operation labels such as `block`, `expert`, `cache`, `router`, and `gate` when they are used as source labels before exact FPF recovery.

`semanticAreaSenseFamily`: source-label wording for stratification, ordering, aggregation, and architecture-operation recognition; not a topic label, pattern-placement claim, or pattern-nest grouping.

`ontologicalNeighborhood`: the applicability neighborhood selected by the recovery row, not a second ontology. The admissible neighborhoods are the rows in `C.30.STRAT:4.2`: control structure; selected structure or structural view; module-interface and substitution; function-like, flow, or transduction; characteristic, scale, or mathematical-lens use; episteme, publication, view, or source-use; state, currentness, temporal, or dynamics; evidence, assurance, gate, work, decision, or causal-use; and ordinary source-label non-use.

The pattern nest is `C.30.*` because the recurring first failure is architecture or structure wording in architecture-operation prose. That placement does not make `C.30` the receiving pattern for relation structure, interface structure, function-like structure, characteristic and scale construction, source use, publication use, evidence, assurance, gate, work, decision, or mathematical-lens claims. The selected `ontologicalNeighborhood` and exact receiving-pattern row decide where the case goes.

#### C.30.STRAT:4.5 - Worked cases

| Wording | Repair |
| --- | --- |
| `The module layer is stable.` | Copy `layer` as source label. Test whether the selected neighborhood is module-interface, scale or comparison, publication or view, or state or temporal. Use `A.6.M`, `C.16.P` or `C.29`, `C.2.P`, `A.19.SPR`, `A.3.3`, or `C.27` only after the neighborhood and apparatus are recovered. |
| `The expert routes the token.` | In MoE prose, `expert` is not a human role by default. Test submodel or subholon, specialized transformation, path-selection relation, transduction-flow relation, candidate selection, or actual role or enactment. Use `A.6.F`, `E.18`, `C.30.TGA-FLOW-REL`, `G.5`, `C.11`, `A.2`, or `A.15` only for the recovered neighborhood. |
| `The cache proves the architecture scales.` | `cache` may belong to module-interface, flow buffer or path, state or currentness, characteristic, source-currentness, or temporal neighborhoods. `Proves` and `scales` are separate evidence, assurance, and scale or mathematical-lens claims. Use exact receiving patterns for each recovered claim-use; do not let `cache` carry proof. |
| `The LCA upper layer guarantees safety.` | Use `C.30.STRAT` only to recover whether `layer` belongs to the control-structure neighborhood. Then `C.30.LCA` records control roles, relations, rate band, and bounded context. Safety proof or assurance exits to `B.3`, `A.10` or `G.6`, dynamics, temporal, and gate patterns. |
| `This gate selects the winning architecture.` | If `gate` is a neural-network gating function or router, use `A.6.F` or `E.18`; if it is a project gate decision, use `A.20` or `A.21`; if it is candidate selection, use `G.5` or `C.11`. The label alone decides none of these. |

#### C.30.STRAT:4.6 - Lowering and reopen conditions

A `StratificationSourceLabelRepairNote` remains admissible only while its source span, selected `ontologicalNeighborhood`, exact receiving pattern, and remaining reader move stay recoverable. Reopen or lower the repair when:

- the source label starts carrying a new relation, characteristic, publication, evidence, assurance, gate, work, decision, causal-use, or mathematical-lens claim;
- a direct exact receiving pattern becomes recoverable and the detour through `C.30.STRAT` no longer buys action guidance;
- the selected neighborhood was chosen by label similarity rather than by recovered apparatus;
- the repair preserves kind recovery but leaves no useful admissible reader move.

Lower the result to quote-only, reduced-use cue, blocked use, or incomplete rewrite when the exact receiving pattern, admissible use, non-admissible use, or remaining move cannot be stated.
### C.30.STRAT:5 - Archetypal Grounding

| Template element | `U.System` illustration | `U.Episteme` illustration |
| --- | --- | --- |
| Source-label cue | A neural-network architecture source says that an `expert block` sits above a `router layer`. | A source-publication note says that a `cache layer` keeps a diagram or view current. |
| Recovery result | `Expert`, `block`, `router`, and `layer` stay source labels until the repair recovers module-interface, function-like, path-selection, flow, or selected-structure apparatus. | `Cache` and `layer` stay source labels until the repair recovers publication source-currentness, view, state or currentness, or ordinary non-use apparatus. |
| Admissible move | Open `A.6.M`, `A.6.F`, `E.18`, `C.30.TGA-FLOW-REL`, `G.5`, or `C.11` only after the exact neighborhood is recovered. | Open `C.2.P`, `E.17`, `A.19.SPR`, `A.3.3`, or `C.27` only after the exact publication, episteme, state, or temporal claim is recovered. |

### C.30.STRAT:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto and Epist**, **Prag**, **Did**, and **Gov**. Scope: architecture and engineering source-label precision restoration, with exits to non-architecture receiving patterns when recovery selects them.

This pattern intentionally biases away from lexical replacement and toward ontology-first recovery. The mitigation is the cheap-closure rule: ordinary source prose stays ordinary, quote-only wording stays quote-only, and direct exact cases skip `C.30.STRAT`.

### C.30.STRAT:7 - Conformance checklist

| ID | Check |
| --- | --- |
| `CC-C30STRAT-1` | The source label is copied as a source label before any FPF kind is assigned. |
| `CC-C30STRAT-2` | The repair names the source label, bounded text, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, encountered FPF kind or reference, relation to the primary `EntityOfConcern`, recovered kind, relation, or claim-use, source-use disposition, exact receiving pattern, admissible use, non-admissible use, and remaining reader move. |
| `CC-C30STRAT-3` | No root kind or universal kind is minted for layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or stratification. |
| `CC-C30STRAT-4` | The selected `ontologicalNeighborhood` and exact receiving-pattern row select the receiving pattern; the source label does not select the pattern nest by itself. |
| `CC-C30STRAT-5` | Direct exact cases use the exact receiving pattern directly instead of detouring through this pattern. |
| `CC-C30STRAT-6` | The repair distinguishes the neighborhoods in `C.30.STRAT:4.2` when any of them are live, and it does not compress several live neighborhoods into one word. |
| `CC-C30STRAT-7` | Subject patterns use at most a thin pointer to this pattern and do not copy this trigger table. |
| `CC-C30STRAT-8` | The result preserves one useful admissible reader move; if no move remains, the disposition is quote-only, reduced-use cue, blocked use, or incomplete rewrite rather than recovered by value. |

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by label. | Complete the `StratificationSourceLabelRepairNote` and select the exact receiving pattern from the recovered neighborhood. |
| C.30 takeover | Any structure-like word is sent to C.30 because it sounds architectural. | Choose by selected `ontologicalNeighborhood`; relation, function-like, scale, publication, evidence, assurance, gate, work, decision, and lens claims exit when those neighborhoods are selected. |
| Local trigger fanout | `A.6.M`, `C.30.LCA`, `C.31`, or another subject pattern copies a growing label table. | Keep one thin pointer to `C.30.STRAT` and keep the subject pattern to its own invariant. |
| Expert-as-role false positive | `expert` in MoE prose becomes an `A.2` role-enactor claim by word alone. | Treat as source label for submodel, transformation, path selection, or candidate selection unless an `A.2` or `A.15` role or work claim is actually live. |
| Gate-as-gate-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use `A.20` or `A.21` only for actual constraint-validity or gate-decision claims; otherwise use the exact function, flow, publication, or ordinary-label disposition. |

### C.30.STRAT:9 - Consequences

| Benefit | Trade-off or mitigation |
| --- | --- |
| Source labels remain usable recognition cues without becoming root kinds. | The reader pays one recovery-row cost only when FPF-governed use is live; ordinary prose closes cheaply. |
| Subject patterns avoid copied trigger registries. | Subject patterns need accurate thin pointers to `C.30.STRAT` and still keep their own invariants precise. |
| Architecture wording no longer captures relation, evidence, assurance, gate, work, decision, publication, state, or mathematical-lens claims by sound. | The repair may open several exact receiving patterns when one sentence compresses several claims; the benefit is that each claim remains governed by its exact pattern. |

### C.30.STRAT:10 - Rationale

Stratification words are common because they compress local practice. That compression is useful at entry time and unsafe as ontology. FPF therefore keeps the word as a source label, recovers the `ontologicalNeighborhood`, and then uses the exact receiving pattern for the recovered claim.

The pattern is placed under `C.30` because architecture and structure prose is the recurring entry point. The placement does not make `C.30` the receiving pattern for every recovered case. If the recovery result is a relation, module-interface relation, characteristic or scale claim, source-publication claim, state or currentness claim, evidence path, assurance argument, gate decision, work occurrence, decision record, causal-use claim, or mathematical-lens result, the receiving pattern outside `C.30.STRAT` carries the live content.

### C.30.STRAT:11 - SoTA-Echoing

Reduced SoTA is sufficient for this precision-restoration pattern. The source practice being adopted is not a new external ontology; it is the observed architecture and engineering habit of using compact labels such as `layer`, `level`, `tier`, `stack`, `block`, `expert`, `cache`, `router`, and `gate` as local recognition language. FPF adapts that practice by keeping labels as source labels and requiring ontology-first recovery before they carry FPF-governed use.

Internal FPF current practice is the governing source here: `E.10` supplies trigger handling, `E.10.ARCH` supplies the recovery architecture, `C.30.P` supplies architecture and structure wording repair, and exact receiving patterns carry recovered cases. The `Solution`, checklist, worked cases, and relations in this pattern change because that source-use disposition rejects lexical replacement and trigger-table fanout.

### C.30.STRAT:12 - Relations

- `E.10` catches the trigger and selects this pattern only when stratification or architecture-operation source-label recovery is needed.
- `E.10.ARCH` supplies the recovery architecture, placement rule, and anti-fanout discipline.
- `C.30.P` remains the broader architecture and structure wording repair. `C.30.STRAT` is the narrower stratification source-label realization when those labels recur with stable recovery apparatus.
- `A.6.M` receives only recovered module-interface relation and interface-specification cases.
- `C.30.LCA` receives only recovered control-structure view cases with control roles, relations, rate bands, control-layer labels, and bounded context.
- `C.31` and `C.31.RSA` receive only recovered characteristic, reusable-locus, bespoke-residue, `accountingBasisRef`, or report-only share cases.
- `C.2.P`, `E.17`, `A.6.F`, `E.18`, `C.30.TGA-FLOW-REL`, `C.16.P`, `A.19.SPR`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11` carry their exact cases when recovered.

Does not replace: `A.22`, `C.30`, `C.30.P`, `C.30.ASV`, `C.30.LCA`, `A.6.M`, `A.6.F`, `E.18`, `C.16`, `C.29`, `C.2.P`, evidence, assurance, gate, work, decision, causal-use, state-family, source-publication, or naming patterns.

### C.30.STRAT:End

