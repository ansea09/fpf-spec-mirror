---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__006_solution.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:4 — Solution"
line_start: 58597
line_end: 58721
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
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "I.2"
keywords:
---

### C.30.STRAT:4 - Solution

Write the direct local repair first. For example: `Here “gate” names the neural-network path selector, not a project gate decision; use E.18 to describe the selected path.` That sentence can be the complete result.

When the repair must be compared, handed on, or revisited, retain a compact note:

```text
StratificationSourceLabelRepairNote:
  sourceLabel:
  boundedTextSpan:
  recoveredObjectRelationOrClaim:
  actualParticipantsOrBearer?:
  sourceUseDisposition:
  patternRef?:
  repairedWordingOrDemotion:
  admissibleUse:
  blockedOverread:
  remainingReaderUse:
  disposition: direct-pattern-use | local-rewrite | ordinary-source-label |
    quote-only | reduced-use-cue | blocked-use | incomplete-rewrite
```

The note is neither the selected structure nor the relation, claim, publication, or pattern result it points to. Omit it when the direct sentence is enough.

#### C.30.STRAT:4.1 - Recovery sequence

1. **Copy the sentence and label.** Keep enough source context to tell what the sentence is doing.
2. **Try the cheap exits.** If the word carries no FPF claim, keep ordinary prose or quote it and stop. If the source already gives the technical term one clear local meaning, keep that term and use its rule directly. If one local rewrite makes the meaning clear, write it and stop. A controlled vocabulary or preferred-word list is not by itself a reason to replace useful domain language.
3. **Recover plausible meanings.** Treat the label as a designation, not as the object, relation, or claim. If it belongs to a named model, viewpoint, standard, or local vocabulary, recover that source-local convention first. Then ask which object, relation, participants or bearer, claim, scope, time, and source use the sentence could be compressing. Include literal and metonymic readings when both are plausible.
4. **Choose by the recovered meaning.** Use the first matching row in C.30.STRAT:4.2; never choose from the label alone. A standard or model may settle the label inside its declared use, but neither its status nor its popularity extends that meaning to another subject or source.
5. **Open only the needed rule.** Name the actual participants, relation, structure, characteristic, state, publication, evidence, work, decision, or other object that makes the claim true or false. Do not copy every possible field into the result.
6. **Return to ordinary wording.** Write the shortest sentence that preserves the recovered claim and names the next pattern only when its contribution matters.
7. **State the stop.** Give the allowed use, the tempting stronger reading that remains blocked, and the next action. If no useful action survives, use quote-only, reduced-use, blocked, or incomplete-rewrite disposition.

#### C.30.STRAT:4.2 - Recovered meanings and patterns to use

| Recovered meaning | Common source labels | What must become clear | Pattern to use |
| --- | --- | --- | --- |
| Control structure | `layer`, `level`, `tier`, sometimes `gate` | The obtaining control relation, what its participants do, any rate band or locality boundary, and a B.2.5 supervisor-subholon relation only when it obtains. | `C.30.LCA`; use B.2.5, dynamics, temporal, evidence, assurance, or gate patterns only for their separate claims. |
| Selected structure or structural view | `layer`, `level`, `stack`, `block`, `view` | The selected, hidden, lost, or preserved structure; view selection; correspondence; source return; an `ArchitectureClaim` when claim content is needed; and a separate `ArchitectureRelation` only when that direct relation obtains. | `A.22`, `C.30`, `C.30.ASV`, or the applicable C.30 subpattern. |
| Module, interface, or substitution | `block`, `cache`, `router`, `expert`, sometimes `layer` or `stack` | Module boundary, interface specification, substitutability relation, variation point, conformance relation, or reliance boundary. | `A.6.M`; stop using C.30.STRAT once that relation is clear. |
| Function or transformation flow | `block`, `expert`, `cache`, `router`, `gate`, sometimes `layer` | Transformation or effect, path selection, graph node, path or crossing, architecture-to-flow relation, or E.18 flow valuation. | `A.6.F`, `E.18`, or `C.30.TFS-REL`. |
| Characteristic, scale, or mathematical lens | `level`, `tier`, `ladder`, `rung`, `layer`, `stack`, `block` | Characteristic and bearer, coordinate or value, scoring method, comparison criterion, scale window, resolution, coarse-graining, preserved or lost structure, lens-use result, and stop condition only where the claim needs them. State separately how the subject is mapped to a scale value; a scale or band does not by itself establish levels in the subject. | `C.16.P`, the applicable characterization pattern, or `C.29`. |
| Episteme, publication, view, or source use | `stack`, `layer`, `section`, `view`, `cache`, `gate` | Description episteme, publication unit, face, form, carrier, source-currentness or source-use relation, source-return condition, or ordinary publication label. | `C.2.P`, `E.17`, or the pattern for the publication or source-use claim. |
| State, currentness, time, or dynamics | `cache`, `stable`, `level`, `readiness`, sometimes `gate` | Bearer, state frame and values, validity window, currentness relation, dynamics, temporal aspect or rate band, authored temporal-claim adequacy, and reopen condition. | `A.19.SPR`, `A.3.3`, `C.27.TA`, `C.27`, or the applicable state or temporal pattern. |
| Evidence, assurance, gate, work, decision, or causal use | `gate`, `proof`, `safety`, `decision`, `work`, `effect`, or any label used as authority | Evidence path, assurance argument, constraint-validity record, gate decision, Work occurrence, decision record, causal-use record, and the stronger readings that remain blocked. | `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or the applicable neighboring pattern. |
| Ordinary source-label non-use | any source label | No FPF claim remains after the sentence is read in context. | No precision-restoration pattern; keep ordinary wording, quote it, reduce its use, or block reliance. |

**When a level claim matters.** When a later decision or design relies on a sentence such as “X is at level L” or “A is above B,” name the subject at stake (the `EntityOfConcern`), what is being ordered, compared, grouped, or mapped, the relation or scale mapping that gives the claim its meaning, when it applies, and whether the sentence asserts, proposes, assumes, or merely illustrates the claim. Apply the same test when `layer`, `tier`, `band`, `scale`, or `stage` carries the stronger claim. A named model or standard may provide this mapping within its declared use; its status does not extend the claim beyond that use. The source word may remain, but these facts—not the label—carry the claim. A list, diagram row, first-then order, carrier section, curriculum, scale label, stage sequence, or coarse-grained description does not establish a subject level by form. If the facts are missing, keep the wording local or illustrative and block reliance on the stronger level claim.

#### C.30.STRAT:4.2a - Same-sentence claim boundary

One sentence may use a source label while making several claims. Split them instead of adding a local catalogue of everything the label does not prove. C.30.STRAT repairs the label; the applicable pattern defines, constrains, or tests each separate claim. The table above lists common destinations, not a mandatory reading list.

#### C.30.STRAT:4.3 - Source-label cue table

| Source label family | Recovery discipline |
| --- | --- |
| `layer` | Do not choose by the word. Test control structure; selected structure or structural view; module or interface; scale or mathematical lens; and publication or source-use meanings. |
| `level` | Before relying on “X is at or above level L,” name the subject, what is being ordered, compared, grouped, or mapped, the relation or scale mapping that gives the claim its meaning, when it applies, and whether the claim is asserted, proposed, assumed, or only illustrated. List order, a diagram row, first-then sequence, carrier section, curriculum, scale label, stage sequence, or coarse-grained view supplies none of these. Then test holon or aggregation use only when a named relation or structure pattern defines it; otherwise test characteristic or scale, ordinal classification, organization scope, Work scope, evidence scope, publication grouping, or ordinary source-label non-use. |
| `tier` | Test deployment, service, organization, classification, aggregation, and publication meanings. When one of those claims is current, use the pattern that defines or tests it; `tier` itself is not the ontology. |
| `stack` | Test signature or slot construction, relation set or relation chain, architecture or control arrangement, aggregation arrangement, virtualization arrangement, deployment arrangement, publication-section ordering, or ordinary source-label non-use. A stack is not architecture by itself. |
| `ladder` and `rung` | Test ordinal or classification scale, declared maturity or readiness progression, C.28 causal-use ladder or rung, publication taxonomy, or ordinary source-label non-use. Do not use ladder wording for an undeclared progression scale. |
| `block` | Test module or interface, selected structure or structural view, function or transformation flow, mathematical lens or coarse-graining, evidence, causal use, gate, and decision meanings. |
| `expert` | In MoE-like prose, first test submodel, subholon, specialized transformation, path-selection relation, candidate-selection relation, ordinary wording, or source-label non-use. If claim-bearing wording still means only “role,” use `E.10.ROLE`; then recover independently any local system-role kind, separate System-classification judgment, obtaining assignment, performer System and complete Work-attribution basis, responsibility or authority relation, or another direct subject relation. Infer none from `expert`. |
| `cache` | Test module-interface, flow buffer or path, state or currentness, capacity characteristic, latency characteristic, memory characteristic, reuse characteristic, source-currentness, publication cache, temporal-aspect or rate-band claim, authored temporal-claim adequacy, or ordinary source-label non-use. |
| `router` | Test path selection, flow relation, transformation function or selection function, module-interface relation, candidate selection, decision, ordinary label, local system-role kind, separate System-classification judgment, obtaining assignment, or actual Work only when that exact claim is being made. |
| `gate` | Test constraint-validity record or gate-decision record, gating function, path selection, flow relation, publication label, or ordinary source-label non-use. A source label `gate` is not gate passage. |

#### C.30.STRAT:4.4 - Author-facing placement note

This subsection maintains the E.10.ARCH applicability row; it is not part of the ordinary project result.

- `semanticAreaBaseConcept` is stratification wording and architecture-operation source labels.
- `semanticArea` is the Part-F row-set for `layer`, `level`, `tier`, `stack`, `ladder`, and `rung`, plus `block`, `expert`, `cache`, `router`, and `gate` when they appear before their technical meaning is known.
- `semanticAreaSenseFamily` is source-label wording for stratification, ordering, aggregation, and architecture-operation recognition. It is not a topic, workstream, or pattern grouping.
- `ontologicalNeighborhood` is the author-facing applicability family selected from C.30.STRAT:4.2. It is neither a second ontology nor a field that an engineer adds to the project object.

The pattern is placed under `C.30.*` because architecture and structure prose is the recurring entry. Placement does not decide the recovered meaning. After recovery, use the rule that defines, constrains, or tests the actual object or claim.

#### C.30.STRAT:4.5 - Worked cases

| Wording | Repair |
| --- | --- |
| `The module layer is stable.` | Keep `layer` as a source label until the sentence reveals a module or interface relation, scale or comparison, publication or view, state, dynamics, or temporal claim. Use only the matching pattern: for example `A.6.M`, `C.16.P`, `C.29`, `C.2.P`, `A.19.SPR`, `A.3.3`, `C.27.TA`, or `C.27`. |
| `The expert routes the token.` | In mixture-of-experts prose, first test submodel or subholon, specialized transformation, path selection, architecture-to-flow relation, candidate selection, ordinary wording, or non-use. Only an unresolved claim-bearing use of *role* opens `E.10.ROLE`; any system-role kind, classification, assignment, performer, Work, responsibility, or authority claim must then obtain independently. |
| `The cache proves the architecture scales.` | Split three questions: what `cache` names, whether an evidence or assurance relation exists, and what measurable scale or lens-use claim is being made. Use `A.6.M`, `A.6.F`, E.18, state or temporal patterns, `C.16.P`, C.29, A.10, B.3, or G.6 only for the branch that is actually present. |
| `The LCA upper layer guarantees safety.` | First decide whether `layer` names a control relation. If so, C.30.LCA records the relation, participant meanings, rate band, and relevant locality or model-use boundary. Safety, evidence, assurance, dynamics, temporal, and gate claims remain separate. |
| `The architecture description places service logic in the application layer.` | Recover the description's declared viewpoint or model-kind convention and what `application layer` means there. It may be a useful grouping in the description. State separately any claim that the described system itself has an obtaining layer, dependency, module, control, or flow relation; neither the diagram position nor architecture-description conformance establishes that world-side claim. |
| `Our operating model has strategic, coordination, and execution levels.` | If these are only headings or work areas, keep them as local labels. Before claiming levels in an organization or practice, say what the three areas are, how they are ordered or mapped, when that ordering applies, and whether it is asserted, proposed, assumed, or only illustrated. Slide order, a curriculum, or a first-then flow establishes none of this. |
| `This gate selects the winning architecture.` | A neural-network gate or router uses `A.6.F` or E.18; a project gate decision uses A.20 or A.21; candidate selection uses G.5 or C.11. The label alone decides none of these. |

#### C.30.STRAT:4.5a - Filled repair note

For `The cache proves the architecture scales`, do not hide the split inside one formal record. Read it as three candidate claims:

1. `cache` may name a state-bearing module, interface arrangement, flow buffer, or ordinary source label; the sentence does not yet decide which;
2. `proves` requires an actual evidence relation or assurance argument; otherwise lower that wording;
3. `scales` requires a characteristic and bearer, comparison or scale construction, architecture scale-preference claim, or mathematical-lens use.

A retained note can remain compact:

```text
StratificationSourceLabelRepairNote:
  sourceLabel: cache
  boundedTextSpan: “The cache proves the architecture scales.”
  recoveredObjectRelationOrClaim: cache meaning unresolved; proof and scale are separate claims
  sourceUseDisposition: keep cache as a source label until its relation or bearer is known
  patternRef?: A.6.M, A.6.F, E.18, A.19.SPR, or A.3.3 for the cache;
    C.16.P, C.29, or C.31.ASAP for scale; A.10, B.3, or G.6 for proof or assurance
  repairedWordingOrDemotion: “The response cache is a candidate state-bearing part of the architecture; no proof or scaling claim has yet been established.”
  admissibleUse: start the three-way investigation
  blockedOverread: cache does not prove scaling, substitutability, or architecture quality
  remainingReaderUse: state the smallest result for each recovered claim, or keep ordinary source wording
  disposition: local-rewrite; direct-pattern-use only for branches that become current
```

The note preserves every live branch without requiring a project engineer to reproduce E.10.ARCH authoring coordinates.

#### C.30.STRAT:4.6 - Lowering and reopen conditions

A repair remains usable only while its source span, recovered meaning, applicable rule, allowed use, and next action remain clear. Reopen or narrow it when the label begins carrying another relation or claim, the actual object becomes clear and makes this detour unnecessary, the interpretation was chosen from word similarity rather than evidence, or the repair is precise but leaves no useful reader action.

Also reopen the affected authoring row when E.10.ARCH changes its internal coordinates, C.30.P changes architecture-wording repair, F.19 changes the plain-language boundary, or another realization pattern now handles this wording family. Lower the result to ordinary wording, quotation, reduced-use cue, blocked use, or incomplete rewrite when the object, applicable rule, allowed use, blocked overread, or next action cannot be stated.

