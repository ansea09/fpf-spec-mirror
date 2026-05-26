---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Adequacy (MLA)"
section_id: "C.29:4"
section_title: "Solution and selected answer"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__006_solution-and-selected-answer.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.29 — Mathematical Lens Adequacy (MLA)"
  - "C.29:4 — Solution and selected answer"
line_start: 48984
line_end: 49566
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.26"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
  - "LensSupportPosture"
  - "coarse-graining"
  - "invariants"
  - "learned lens"
  - "lens mapping mode"
  - "lost structure"
  - "mathematical lens"
  - "ontology smuggling"
  - "preserved structure"
  - "rival lens"
  - "scale window"
  - "stop condition"
  - "structure-preserving representation"
  - "validation posture"
---

### C.29:4 - Solution and selected answer

#### C.29:4.1 - Selected answer in one paragraph

`C.29 — Mathematical Lens Adequacy (MLA)` is the general FPF discipline for mathematical lenses used in explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer. It handles two first-use cases, with the positive case first: an under-lensed situation where the next admissible move can benefit from a cheap first candidate lens; and an existing candidate lens ready for application, repair, bounding, replacement, or rejection. Its job is to help the reader introduce, choose, apply, limit, replace, or remove a mathematical lens so that a useful admissible next move survives. A mathematical lens is admissible for a declared use when it compresses a phenomenon by preserving declared structure, exposing useful invariants, and producing lens-supported predictions, distinctions, obstructions, or diagnostic boundaries inside a bounded context. It is inadmissible for an undeclared or unsupported use when it imports source-domain ontology, hides loss under metaphor, treats source prestige as evidence, or licenses claims outside its declared scale, context, validation, bridge, causal, or assurance boundary.


`C.29` does not mint `MathematicalLens`, `U.MathematicalLens`, `LensKind`, or any universal FPF lens object. In this pattern, “mathematical lens” names a declared use of a mathematical object, formalism, learned representation, simulation substrate, or mathematical family under declared mapping, preserved/lost structure, `LensSupportPosture`, admissible use, and stop condition; the target phenomenon and any claim outside lens adequacy keep their own FPF kinds.

Admission guard: C.29 governs mathematical-lens adequacy claims. It does not mint mathematical-lens kinds, and it does not govern or create the described entity, Bridge, evidence path, causal support, assurance score, measurement construction, dynamics semantics, decision record, work record, explanation rendering, comparative review unit, representation transition, coarsened rendering, selector, benchmark, or scale audit. Its outputs are local adequacy outputs unless a separate FPF naming and admission decision makes one durable.


#### C.29:4.2 - Mathematical Lens Adequacy Principle

> **Mathematical Lens Adequacy Principle.**
> A mathematical lens is admissible for a declared use when it compresses a phenomenon by preserving declared structure, exposing useful invariants, and producing lens-supported predictions, distinctions, obstructions, or diagnostic boundaries inside a bounded context. It is inadmissible for an undeclared or unsupported use when it imports source-domain ontology, hides loss under metaphor, treats source prestige as evidence, or licenses claims outside its declared scale, context, validation, bridge, causal, or assurance boundary.

Compact plain form:

> **A useful mathematical lens is compression with invariants and declared losses.**

Register policy: **Tech exactness below, Plain metaphor above.** Plain phrases such as “structures that survive transfer,” “what the lens makes visible,” and “where the lens stops” are admissible as recognition aids. When a sentence carries FPF-kind, relation, evidence, admissibility, causal, assurance, bridge, gate, work, decision, or pattern-application claim force, the corresponding `C.29` output recovers the exact fields and receiving patterns.

Zero/first-principles compatibility note: `E.1` and `E.2` govern the mission and pillar authority. `C.29` supports them by making mathematical first-principles support inspectable for one declared use: candidate mathematical object, preserved structure, lost structure, visible payoff, admissible move, neighboring-pattern boundary, and stop condition. It does not replace pillar authority, neighboring governing loci, ordinary FPF reasoning, or `E.9` design-rationale support for normative changes.

Mathematics is not a prerequisite for FPF use. Ordinary prose is valid when no mathematical structure changes the next admissible move. C.29 earns its place only when a mathematical object, formalism, learned representation, simulation substrate, or mathematical family changes explanation, decision, prediction, comparison, publication, bridge, assurance input, reusable transfer, or the next admissible repair.

Plain/Tech bridge:

| Plain reader question | Tech recovery |
|---|---|
| What structure helps? | `CandidateMathObject` or `CandidateLensFamily` in a `LensCandidateNote`. |
| How does it represent the phenomenon? | `LensMappingMode`. |
| What survives? | `PreservedStructure`. |
| What disappears or is deliberately ignored? | `LostStructure`. |
| Why trust this use? | `LensSupportPosture`, validation overlay when live, and neighboring evidence/assurance loci when their claims are live. |
| What can the reader now do? | `AdmissibleNextMove` or `admissibleUse`. |
| What remains blocked? | `StopCondition` and `nonAdmissibleUse`. |

State, scale, and dynamics trigger: if the lens carries state, transition, forecast, rate, temporal window, scale window, observation, measurement, comparison, or causal implication, the cheapest honest output either names the minimal relevant field or names the receiving FPF locus. State and transition semantics stay with `A.3.3`; characteristic spaces and overlays stay with `A.19`; measurement construction and direct comparability stay with `C.16`; temporal-use adequacy stays with `C.27`; scale-law and scale-preference claims stay with `C.18.1` and `C.19.1`; causal-use support stays with `C.28`.


#### C.29:4.2a - Mathematicalization Utility Principle

A mathematical lens is worth introducing only when it changes the working reader's next admissible move by making at least one first-principles modeling basis visible:

- a declared signature, structure, state variable, transition, or observation map;
- a symmetry, invariant, conservation-like constraint, equivalence, or composition rule;
- a local-global relation, boundary relation, scale variable, coarse-graining rule, scale window, or correspondence condition;
- a variational principle, action, energy, free-energy, loss, or value functional, Euler-Lagrange or stationarity condition, constrained optimization target, dual view, objective vector, or resource trade-off;
- an uncertainty, probability, information, typicality, approximation, sensitivity, or validation boundary;
- an algorithmic, constructive, resource, realizability, implementation, or adversarial limit;
- a bottleneck, obstruction, impossibility, consistency boundary, or failed transfer in the candidate-model space;
- a rival-lens distinction that changes model choice;
- a causal, intervention, or counterfactual preservation question governed by `C.28`;
- a bridge or export loss governed by `F.9`;
- a measurement or comparability condition governed by `C.16`.

If no next admissible move changes, keep the text as ordinary prose, downgrade it to a didactic metaphor, or return `NoMLANeededNote`. A lens that merely makes prose more impressive is not a successful `C.29` result.


#### C.29:4.2b - First-principles lens-family support

`C.29` supports first-principles use only when the principle family changes what the working reader can derive, inspect, compare, observe, or honestly block. The family name is never enough. Each row below is a discovery and recovery discipline: it tells the reader what must be named before the mathematical lens can carry claim force.

| First-principles family | Use when the working problem asks | Required `C.29` recovery | Stop or neighboring exit |
|---|---|---|---|
| Boundary, exterior derivative, Stokes-like local-to-global relation | How local increments, flows, sources, interfaces, or balances compose into a global claim. | Name the domain, boundary, field/form/flow, derivative/divergence/curl-like operator, boundary condition, and what is conserved, sourced, or lost at the boundary. | Does not make all boundary language one mechanism; measurement, evidence, and bridge claims move to `C.16`, `A.10`, or `F.9`. |
| Cohomology, closed/exact split, topological obstruction | Why a local rule cannot be made global, or why a transfer/composition is blocked. | Name the cycle/cocycle-like object, equivalence class or obstruction, local closure condition, failed exactness/global witness, and the blocked claim. | Useful obstruction is a `LostStructure` or `StopCondition`; it is not a causal explanation without `C.28` and evidence. |
| Symmetry, invariance, equivariance, Noether-like conservation | Which transformations leave the relevant claim unchanged, or which conservation-like quantity follows from an invariance. | Name the transformation family, action on the described variables, invariant or conserved quantity, assumptions, and distinctions intentionally lost. | Does not transfer physical conservation, coordinate-free truth, or causal mechanism without domain evidence and dynamics support. |
| Variational principle, action, energy/free-energy/loss/value functional, Legendre or convex duality | Whether a behavior, representation, design, or trade-off follows from stationarity, extremum, dual variables, or potential transformation. | Name the functional, admissible variation space, constraints, boundary conditions, stationarity or extremum condition, dual transform, and what the dual view makes visible. | Does not imply the target literally optimizes that functional unless `A.3.3`, `A.10`, or `C.28` support the dynamics, evidence, or causal use. |
| RG, coarse-graining, fixed point, basin, universality | Why different microdescriptions can share one macropattern, or when a scale claim stops. | Name the scale variable, scale window, coarse-graining rule, fixed point or attractor, basin/regularity condition, invariant or exponent, and lost microstructure. | Scale-law adequacy and scale advantage move to `C.18.1` and `C.19.1`; no micro-mechanism identity is licensed. |
| Diagonal, self-reference, fixed-point theorem, no-go family | Whether a universal evaluator, complete language, self-model, closure rule, or governance rule is blocked by self-application. | Name the encoding, evaluator or self-map, diagonal/fixed-point construction, universal claim being tested, and exact impossibility or closure boundary. | Does not prove every recursive-looking case is a no-go theorem; assurance or governance claims move to `B.3`, `E.19`, or the local domain pattern. |
| Composition, category, operad, optic, semiring or limit transform | Whether composition, interface, view, transformation, or algebraic law is the useful preserved structure. | Name objects, morphisms/relations, composition law, identity or interface condition, preserved algebraic law, failed transfer, and any limit transform such as classical/tropical or Fourier-Laplace/Legendre. | Bridge semantics and substitution safety move to `F.9`; C.29 only records lens adequacy and loss. |
| Probability, information, observation, acquisition | Which uncertainty, information, typicality, readout, or next observation changes the next admissible move. | Name the random variables or distributions, utility or information criterion, observation/probe design variable, model assumptions, estimation method, validation boundary, and robustness posture. | Measurement, evidence, experiment planning, causal support, and assurance stay with `C.16`, `A.10`, `C.28`, `A.15`, and `B.3`. |

This table is normative as a recovery guide, not as a mandatory taxonomy. A local project may name a closer family, but it must recover the same kind of load-bearing structure: mathematical substrate, preserved structure, lost structure, visible payoff, support posture, and stop condition.

#### C.29:4.3 - Use boundary

This boundary prevents `C.29` from being over-applied.

**Use `C.29` when** a mathematical object, formalism, learned representation, simulation substrate, or mathematical family is used as a lens for explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer over a physical, organizational, epistemic, social, computational, scientific, or methodological phenomenon, or when a phenomenon, decision, explanation, comparison, model-selection, diagnosis, or method-choice problem is stable enough that the first useful move is to choose a cheap candidate lens that makes relevant structure visible.

**Do not use `C.29` as the governing pattern when:**

- the mathematics is ordinary local domain theory already governed by a domain pattern;
- the phrase is a purely didactic analogy that is not reused for decisions, evidence, assurance, publication, bridge, comparison, or transfer;
- the live question is causal-use support, which is governed by `C.28`;
- the live question is measurement construction, scale legality, direct comparability, or evidence-stub adequacy, which is governed by `C.16`;
- the live question is cross-context meaning or substitution safety, which is governed by `F.9`;
- the live question is dynamics semantics without a separate lens-transfer claim, which is governed by `A.3.3`;
- the live question is a `CharacteristicSpace` overlay with no domain-transfer, prediction, assurance, publication, or reusable explanation claim, which stays under `A.19`.
- the live object is a `ChoiceResult`, local choice record, selected-set publication, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, or work-relevant source restoration; those claims stay with `C.11`, `G.5`/`G.9`, `A.15`, `A.15.1`, or `A.15.4` as appropriate.
- the live object is an explanation-facing rendering, bounded comparative review unit, same-described-entity representation-scheme transition, or controlled semantic coarsening; those claims stay with `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, or `A.6.3.CSC`, with MLA fields carrying only mathematical-lens adequacy when the mathematical lens affects the stated admissible use.
- the live claim is about forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, speed, temporal window, or rate-change as sufficient for use; temporal-claim adequacy stays with `C.27`.

This boundary keeps mathematical-lens adequacy from becoming a shadow record for neighboring work.

Lexical rule: use **structure-preserving representation** rather than **structure-preserving identification** in discoverability-bearing prose, unless equivalence or identity is explicitly the declared `LensMappingMode`.

#### C.29:4.4 - Action path before the full card

Begin with action guidance, not with the full card.

First action choices: keep ordinary prose, introduce a cheap candidate lens, name a substrate that fits the stated use more directly, add visible payoff, add loss, choose the principal rival lens, add validation posture, narrow an existing claim, downgrade an overclaim, or move any evidence, causal, bridge, assurance, work, decision, publication, or admission claim to the exact neighboring FPF locus.

Memory hook: a successful C.29 application can raise or lower the mathematical claim force. It can introduce a first candidate lens, keep ordinary domain prose, remove a mathematical lens, repair relation wording through `A.6.P`, declare a `CharacteristicSpace` through `A.19`, use `C.16` for measurement and comparability, open `F.9` for bridge semantics, ask the `C.28` causal-use question, restore work or source responsibility through `A.15`, or send temporal-use adequacy to `C.27`.

No-lens cheap path: name the `ProblemStructureCue`, choose the cheapest candidate lens family that makes it visible, test whether that lens changes the next admissible move, and if no move changes, keep ordinary prose or collect more observations before using mathematical-lens wording.

First neighboring-locus map:

| Claim-bearing question | Govern there first | C.29 remainder |
|---|---|---|
| relation substrate, relation kind, or structure-preserving relation wording | `A.6.P` and local relation patterns | mathematical-lens adequacy only if a mathematical object changes the stated use |
| state variables, transition law, observation map, constraints, or calibration | `A.3.3` and `A.19` | preserved/lost structure and lens stop condition |
| measurement construction, scale, unit, polarity, or comparability | `C.16` | lens support posture for measurement-dependent use |
| scale law, universality, knee, exponent, or scale preference | `C.18.1` / `C.19.1` | scale-bounded mathematical-lens adequacy |
| cross-context meaning, substitution, or Bridge-supported use | `F.9` | mathematical structure used inside the bridge claim |
| causal, intervention, policy, or counterfactual use | `C.28` | whether the lens preserves, approximates, or blocks causal-use structure |
| evidence, provenance, source currentness, assurance, release, selector, or benchmark use | `A.10`, `B.3`, or relevant `G.*` pattern | adequacy of the mathematical lens as one input only |

Math-apparatus boundary: `C.29` coordinates the lens-adequacy part across relation substrate, state/characteristic spaces, measurement, dynamics, scale, bridge, causal, evidence, assurance, selector, and benchmark patterns. It does not replace any one of them.


1. **Find the claim-bearing phrase.** Mark the exact mathematical phrase that affects explanation, decision, prediction, comparison, publication, bridge, assurance-input, or reusable transfer.
2. **Choose the smallest output class that preserves honesty.** The output-class decision happens before any full-card fields.
3. **Name the concrete mathematical object or structure.** Family labels such as `category theory`, `field`, `graph`, `quantum`, `RG`, or `geometry` are entry prompts, not adequate substrates for the stated use by themselves.
4. **State the lens mapping mode.** Use the least committing honest `C.29`-local lens mapping mode: analogy-only prompt, representation, empirical fit, simulation, quotient, abstraction, coarse-graining, embedding, homomorphism, isomorphism, functor-like transfer, cross-context lens-transfer candidate, or accepted local theory. If cross-context meaning, substitution, CL, sense cells, or Bridge-supported use is live, `F.9` governs that claim; the MLA fields record only mathematical-lens adequacy for the declared transfer.
5. **State preserved structure and lost structure.** This is the central repair move.
6. **State what becomes visible.** Name the invariant, obstruction, fixed point, symmetry, conservation law, diagnostic boundary, lens-supported distinction, model-selection consequence, or other payoff.
7. **State the supported use and blocked use.** Say what is now admissible, what remains blocked, and which named neighboring FPF locus governs any live claim outside lens adequacy.
8. **If the claim does not pass, repair rather than merely fail.** Downgrade, narrow, switch to a principal rival lens, add `LensSupportPosture` or validation posture, split out bridge, dynamics, measurement, causal, temporal, decision, work, explanation, comparison, representation, scale, or assurance claims to the neighboring governing locus, or remove the mathematical phrase from claim-bearing use.

Application output classes:

| Output class | Output | Use condition | Required content |
|---|---|---|---|
| `NoMLANeeded` | `NoMLANeededNote` or ordinary Plain orientation | Mathematical language is local, didactic, or accepted local theory and is not used for transfer, decision, evidence, assurance, publication, bridge, comparison, or reusable explanation. | State why `C.29` is not opened; no card. |
| `LensCandidateNote` | `MLA.LensCandidateNote` | A problem whose next move can depend on a mathematical lens is stable enough for a first candidate lens, but no adequate mathematical object has been named yet. | `TargetPhenomenon`, `ProblemStructureCue`, `CandidateLensFamily`, optional `CandidateMathObject?`, `WhyThisLensCouldHelp`, `ExpectedVisiblePayoff`, `ObservableOrControllableCue?`, `AdmissibleNextMove`, `OrdinaryRivalOrFallback`, `StopCondition`, `NextMLAOutput`. |
| `OneLine` | `MLA.OneLine` | An under-specified phrase affects explanation, decision, prediction, comparison, publication, bridge, assurance input, or reusable transfer and needs repair before reuse. | `TargetPhenomenon`, `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `VisiblePayoff`, `AdmissibleNextMove`, optional `ObservationOrReadoutNeeded?`, `OrdinaryRivalOrFallback`, `StopCondition`. |
| `MiniCard` | `MLA.MiniCard` | The lens supports a reusable explanation, local decision, comparison, or method-selection claim. | `OneLine` content plus `InvariantsExposed`, `LensSupportPosture`, `admissibleUse`, `nonAdmissibleUse`, principal rival, and `RivalLensRelation?` when another mathematical lens changes the admissible move. |
| `FullCard` | `MLA.FullCard` | Publication, bridge, assurance input, benchmark, model selection, prediction, formal pattern claim, or repeated cross-case use is live. | Full `MLA.Card@Context` plus any conditional overlays. |
| `NeighborGoverningLocusNote` | `NeighborGoverningLocusNote` | The live claim is causal use, bridge or substitution, measurement construction, scale legality, direct comparability, evidence-stub adequacy, dynamics semantics, temporal adequacy, decision result, selected method, work plan, performed work, evidence trust, assurance, explanation rendering, comparative review, representation transition, coarsening, scale law, release, selector, or benchmark. | Name the governing FPF locus and apply `C.28`, `F.9`, `C.16`, `A.3.3`, `C.27`, `C.11`, `A.15`, `A.15.1`, `A.15.4`, `A.10`, `B.3`, `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, `A.6.3.CSC`, `C.18.1`, `C.19.1`, or a relevant G pattern. The C.29 application keeps only lens-adequacy support. |

Micro-template examples:

```text
MLA.LensCandidateNote example := {
  TargetPhenomenon: slow Product-X team flow,
  ProblemStructureCue: waiting and work-in-progress look more important than individual task difficulty,
  CandidateLensFamily: queue or flow lens,
  CandidateMathObject?: single-server or multi-server queue candidate,
  WhyThisLensCouldHelp: arrivals, service time, WIP, and waiting time could expose the bottleneck,
  ExpectedVisiblePayoff: decide whether delay is arrival-rate, service-rate, batching, or WIP-boundary pressure,
  ObservableOrControllableCue?: arrivals, service time, wait time, WIP limit,
  AdmissibleNextMove: observe the variables before claiming queue adequacy,
  OrdinaryRivalOrFallback: ordinary process narrative without queue assumptions,
  StopCondition: no claim about motivation, obligation, blame, or full team ontology,
  NextMLAOutput: NoMLANeededNote or MLA.OneLine after observation
}
```

```text
MLA.OneLine example := {
  TargetPhenomenon: Product-X backlog delay,
  CandidateMathObject: queue model over arrivals, service time, waiting time, and work in progress,
  LensMappingMode: representation,
  PreservedStructure: flow, bottleneck candidates, wait, WIP, service-rate pressure,
  LostStructure: motivation, priority politics, contractual duties, skill learning, quality of work,
  VisiblePayoff: identify whether delay is arrival-rate, service-rate, batching, or WIP-boundary problem,
  AdmissibleNextMove: observe arrivals, service, wait, and WIP; test one local WIP-limit or batching hypothesis,
  ObservationOrReadoutNeeded?: service-time and wait-time readings,
  OrdinaryRivalOrFallback: process narrative without queue assumptions,
  StopCondition: do not infer team obligation, motivation, blame, or organizational ontology
}
```

```text
MLA.MiniCard example := {
  TargetPhenomenon: production-line throughput and latency,
  CandidateMathObject: queueing network with stated stations and service-rate assumptions,
  LensMappingMode: representation,
  PreservedStructure: flow, bottlenecks, service rates, waiting times,
  LostStructure: human meaning, contractual obligations, rare failure modes, causal interventions not represented by the network,
  InvariantsExposed: bottleneck station and queue-length sensitivity under stated assumptions,
  LensSupportPosture: accepted local theory plus local observations,
  admissibleUse: throughput and latency reasoning inside the declared line model,
  nonAdmissibleUse: motivation, duty, causal intervention, full organization ontology, or release assurance,
  PrincipalRivalLens?: direct empirical dashboard reading,
  RivalLensRelation?: complementary,
  StopCondition: no inference about motivation, obligation, rare-event causality, or full organizational ontology
}
```

```text
MLA.OneLine := {
  TargetPhenomenon,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  VisiblePayoff,
  AdmissibleNextMove,
  ObservationOrReadoutNeeded?,
  OrdinaryRivalOrFallback,
  StopCondition
}
```

For `MLA.OneLine`, `VisiblePayoff` says what the lens makes visible, such as a bottleneck, invariant, obstruction, incompatibility, loss boundary, or diagnostic split. `AdmissibleNextMove` says the now-admissible user move, such as compute a local quantity, compare only inside a declared structure, run a validation slice, apply a neighboring pattern, keep the phrase as local metaphor, or remove the phrase from claim-affecting use. `ObservationOrReadoutNeeded?` names the missing observable, readout, assignment, outcome, validation slice, or scale point needed before the repaired line can support the stated move. `OrdinaryRivalOrFallback` says what the reader would use without this mathematical lens: ordinary prose, accepted local domain theory, direct measurement, a causal model, a queueing model instead of a quantum-like metaphor, an `A.19` space declaration instead of `C.29`, or an `F.9` bridge instead of category-like wording. If two mathematical lenses already change the next move at this cheap-output class, add one ordinary-language note about the disagreement and move to `MLA.MiniCard` or `MLA.FullCard` before claiming a reusable rival-lens relation.

```text
MLA.LensCandidateNote := {
  TargetPhenomenon,
  ProblemStructureCue,
  CandidateLensFamily,
  CandidateMathObject?,
  WhyThisLensCouldHelp,
  ExpectedVisiblePayoff,
  ObservableOrControllableCue?,
  AdmissibleNextMove,
  OrdinaryRivalOrFallback,
  StopCondition,
  NextMLAOutput
}
```

`MLA.LensCandidateNote` is not evidence, assurance, a bridge, a decision record, a selector result, a literature survey, or a full adequacy card. It is a cheap first-candidate lens selection note. Its successful next outputs are `NoMLANeededNote`, `MLA.OneLine`, or a named neighboring governing-locus note.

Name guard for this note: `ProblemStructureCue` is a recognition cue, not a FPF signature; `CandidateLensFamily` is a family prompt, not a kind; `AdmissibleNextMove` is action guidance, not a work record; `NextMLAOutput` is the next C.29 output class, not a new record family.

Do not use `MLA.OneLine` with an empty `CandidateMathObject`. If the candidate object has not yet been named, use `MLA.LensCandidateNote` first or exit to ordinary prose or a neighboring governing locus.

Cheap stop: if the mathematical phrase does not affect any claim beyond orientation, do not open the full card. If the first honest output is `NoMLANeededNote`, that is a successful `C.29` result, not an underfilled card.

#### C.29:4.4.1 - Output set and use-rights

After applying `C.29`, the output is one of these:

| Output | Meaning |
|---|---|
| `NoMLANeededNote` | Ordinary local math or didactic metaphor; no transfer, decision, evidence, assurance, publication, bridge, comparison, or reusable-explanation use. |
| `MLA.LensCandidateNote` | Cheap first-candidate note for an under-lensed problem whose next move can depend on a mathematical lens; not evidence and not a full adequacy card. |
| `MLA.OneLine` | Target, mathematical object, lens mapping mode, preserved structure, lost structure, visible payoff, admissible next move, optional observation or readout needed, ordinary rival or fallback, and stop condition. |
| `MLA.MiniCard` | One-line plus invariant or payoff, `LensSupportPosture`, admissible use, non-admissible use, and rival-lens relation when disagreement changes the next move. |
| `MLA.FullCard` | Full card for publication, bridge, assurance input, model selection, benchmark, prediction, or reusable explanation. |
| `NeighborGoverningLocusNote` | A named neighboring FPF locus governs the live causal, bridge, evidence, scale, dynamics, temporal, decision, work, explanation, comparison, representation, measurement, or assurance claim; the C.29 application records only the lens-adequacy part. |

Positive warning: a successful `C.29` output makes the mathematical lens honest for its declared use. It does not make the claim true, safe, released, benchmark-superior, decision-ready, or causally supported. Truth, safety, release, benchmark, decision, and causal-use claims need their governing neighboring FPF patterns.

`LensMappingMode`, `LensSupportPosture`, and use posture are separate readings.

| Reading | Question it answers | Where it is recorded |
|---|---|---|
| Mapping construction | How does the mathematical object represent, abstract, embed, quotient, simulate, learn, or transfer the phenomenon? | `LensMappingMode`, `PreservedStructure`, `LostStructure`, and any `ScaleWindow?` or `CoarseGrainingRule?`. |
| Support basis | What supports this declared lens use? | `LensSupportPosture`, validation overlay when live, and neighboring evidence or assurance patterns when their claims are live. |
| Use posture | What can the working reader now do, and what remains blocked? | `admissibleUse`, `nonAdmissibleUse`, `AdmissibleNextMove`, `StopCondition`, and named neighboring FPF loci. |

`LensMappingMode` names construction, not permission. Typical local values include `representation`, `abstraction`, `quotient`, `coarse-graining`, `embedding`, `homomorphism`, `isomorphism`, `functor-like transfer`, `simulation substrate`, and `learned or fitted representation`. A broad family name such as graph, field, category, geometry, quantum-like, variational, or Bayesian is only a prompt until the concrete construction and preserved/lost structure are named.

`LensSupportPosture` grants only limited use-rights:

| `LensSupportPosture` value | Allowed use | Blocked use |
|---|---|---|
| analogy-only prompt | orientation, hypothesis generation, recognition cue | decision, assurance, causal claim, or publication as established model |
| diagnosticOnly | finding a candidate obstruction, bottleneck, mismatch, missing state variable, or rival-lens split | prediction, decision, causal use, bridge substitution, assurance, or ontology without neighboring support |
| formal derivation inside accepted theory | local explanation or theorem-supported transfer when assumptions hold | empirical claim without observation or evidence |
| simulation | candidate model and scenario exploration | real-world causal or predictive reliance without validation |
| empirical fit | local prediction inside validation regime | out-of-regime generalization and causal use |
| accepted domain theory | local domain model use | cross-context ontology import |
| SoTA-echo candidate | structured exploration and lens-adequacy testing | accepted FPF law, assurance, release, or foundation claim |
| mechanized proof | formal property under assumptions | real-world adequacy unless assumptions, bridge, and evidence hold |

Use posture is not inferred from elegance, familiarity, source prestige, or mapping type. It is stated in `admissibleUse`, `nonAdmissibleUse`, and `StopCondition`. Mathematical adequacy is not empirical truth, causal support, bridge substitution, assurance, release confidence, decision sufficiency, or benchmark superiority; those claims need their governing neighboring FPF patterns.

#### C.29:4.4.2 - From lens to local action


Local action change from a mathematical lens is limited to these cases unless a neighboring pattern supports the needed non-C.29 use:

1. observe or measure a newly named variable or relation;
2. compare only under a declared structure and loss boundary;
3. diagnose a bottleneck, obstruction, mismatch, invariant, or failed transfer;
4. choose or reject a principal rival lens for the current local use;
5. narrow, downgrade, or block a tempting overread;
6. open the exact neighboring FPF locus when the live claim is causal, bridge, evidence, assurance, measurement, temporal, decision, work, scale, selector, or benchmark.

Each item closes either as a local C.29 output or as a named neighboring-pattern opening. If the needed result is a work plan, choice result, selector output, benchmark, or evidence record, publish that neighboring result in its governing pattern rather than from this list.

#### C.29:4.4.3 - No-lens entry: choosing a first candidate lens

Use this when the next admissible move can benefit from a mathematical lens but no adequate mathematical object has been named. The output is `MLA.LensCandidateNote`, not `MLA.OneLine` and not a full card. State the `ProblemStructureCue`, choose one cheap `CandidateLensFamily`, say what it could make visible, name the `ObservableOrControllableCue?` when available, state the `AdmissibleNextMove`, compare it with the `OrdinaryRivalOrFallback`, and stop if no action changes. If the cue is still pre-articulation and no stable `ProblemStructureCue` can be named, do not mathematize it; preserve cue plurality through `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state locus before returning to `C.29`.

Candidate guidance rows are examples for first recognition. Use the row that fits the working cue, or state a closer local cue using the same fields.

| `ProblemStructureCue` | Cheap `CandidateLensFamily` | First admissible move and stop |
|---|---|---|
| waiting, backlog, bottleneck, or throughput | queue or flow network | Observe arrivals, work in progress, service time, wait time, and bottleneck candidate; do not infer obligation, motivation, or managerial authority from the queueing lens alone. |
| state change, trajectory, stabilization, or control pressure | state-space, dynamics, Markov, ODE, or control lens | Name state, transition law, observation map, and validity window; return dynamics semantics to `A.3.3` and temporal-use claims to `C.27` when live. |
| dependency, interface, composition, or transfer failure | graph, hypergraph, category, operad, or compositional lens | Expose edges, edge meaning, slots, interfaces, composition law, and failed transfer; use `F.9` when cross-context meaning or substitution is live. |
| local-to-global boundary relation, conservation across a boundary, or source/sink balance | Stokes-like, exterior-derivative, divergence, flux, or boundary-operator lens | Name the domain, boundary, local rule, boundary condition, and conserved or sourced quantity; do not infer mechanism, evidence, or bridge safety without the neighboring pattern. |
| local rule that cannot become a global solution, or a transfer blocked by topology | cohomology, closed/exact, obstruction, or failed-extension lens | Name the local closure condition, global witness that fails, obstruction class or equivalent diagnostic boundary, and the blocked claim. |
| comparison, similarity, distribution shift, population movement, or shape change | metric-space distance, topology, embedding, or optimal-transport lens | Declare what distance, neighborhood, order, embedding, coupling, or transport cost preserves and what it loses; use `C.16` for comparability and measurement construction when live. |
| scale transition, coarse behavior, universality, knee, fixed point, or basin-of-attraction cue | coarse-graining, RG, fixed-point, or scaling-law lens | Name scale variable, scale window, coarse-graining rule, fixed point or attractor, basin/regularity condition, and invariants; use `C.18.1` for scale-law adequacy and `C.19.1` when scale advantage or BLP preference is live. |
| invariance under transformations, coordinate changes, or conservation-like claim | symmetry, group action, Noether-like, invariant, or equivariant representation | Identify the transformations, invariant or conserved quantity, assumptions, distinctions preserved, and coordinate details lost; do not import physical conservation without evidence. |
| extremal behavior, trade-off, dual view, potential, or cost/resource relation | variational, Lagrangian/Hamiltonian, action/energy/free-energy, Legendre, convex-duality, or constrained-optimization lens | Name the functional, variation space, constraints, boundary conditions, stationarity/extremum condition, dual transform, and what the dual view makes visible. |
| self-reference, universal evaluator, complete-language claim, closure paradox, or impossible total method | diagonal, fixed-point theorem, no-go, or self-application lens | Name the encoding, evaluator/self-map, diagonal move, universal claim tested, and exact closure or impossibility boundary; do not turn every loop into a no-go theorem. |
| uncertainty, information value, missing observation, active probe, or next sample choice | probabilistic, information-theoretic, BED/OED, active-learning, or Bayesian-optimization lens | Name the variables/distribution, utility or information criterion, design variable, acquisition candidate, model assumptions, estimation method, validation boundary, and robustness posture. |
| intervention, policy effect, or counterfactual question | SCM, causal graph, or causal abstraction lens | Name the causal object, intervention or assignment, outcome readout, and whether counterfactual structure is preserved, approximated, or not claimed; keep causal-use support with `C.28`. |
| learned scientific representation, latent state, surrogate solver, or operator view | neural operator, latent representation, surrogate solver, or world-model lens | Add the observation map, data or training regime, validation slice, generalization claim, uncertainty or approximation note, and stop condition. |
| probe effects, order effects, context effects, incompatible frames, or measurement-as-intervention | quantum-like or contextual-probability lens | Use `C.26` for quantum-like adequacy when order/probe/context effects are actually live; block physical quantum ontology unless separate physics evidence is supplied. |

`MLA.LensCandidateNote` is local first-candidate guidance. It does not replace `G.2` SoTA synthesis, tradition mapping, or broad lens-family review. Use `G.2` when the live work is tradition-scale source synthesis; use `C.29` when the local need is to choose one cheap candidate lens that changes the next admissible move. The cheap observation and control check does not open `C.16` or `A.10` by default; it only asks what the user can observe, read out, assign, vary, or validate now. Measurement construction, evidence strength, intervention support, or validation still moves to the neighboring pattern when live.

#### C.29:4.4.4 - First honest C.29 entry cases

For E.11-style first-entry recognition, distinguish the working entry case before choosing an output:

| First honest entry case | What the working reader met | First `C.29` answer |
|---|---|---|
| Pre-articulation cue | Something feels structurally wrong, but it is not yet a claim and no stable `ProblemStructureCue` can be named. | Do not force a mathematical lens. Use `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state locus first; return to C.29 only when the problem structure is stable enough. |
| No lens or under-lensed problem | A problem situation is stable enough for mathematical help, but no mathematical substrate has been named. | Use `MLA.LensCandidateNote`: `ProblemStructureCue` -> `CandidateLensFamily` -> `AdmissibleNextMove`. |
| Under-specified lens | A phrase such as field-like, graph-like, or quantum-like appears, but no object, mapping, preservation, or loss is stated. | Write `MLA.OneLine` or downgrade to ordinary prose. |
| Useful lens with overread | The lens is useful, but the text turns it into ontology, evidence, causality, assurance, bridge, or release support. | Use `MLA.MiniCard` or `MLA.FullCard` and name blocked use plus neighboring governing locus. |
| Ordinary local math | A Markov kernel, ODE, graph data structure, or accepted domain theory appears inside its local domain use. | Return `NoMLANeededNote` and stay with the local pattern. |
| Wrong first pattern | The reader reaches for `C.26`, `F.9`, `C.28`, `C.16`, or `A.3.3` before knowing whether mathematical-lens adequacy is live, or reaches for `C.29` when a neighbor already governs. | Name the first governing locus and state what `C.29` contributes, if anything. |

#### C.29:4.4.5 - False-positive bank and entry stops

Do not open `C.29` for these non-use cases unless a separate lens-transfer, publication, assurance, bridge, comparison, or reusable-explanation claim becomes live:

- ordinary ODE inside accepted physics or local engineering model;
- Markov kernel inside accepted stochastic dynamics;
- graph used as a local data structure;
- metric-space distance, topology, order, product, subspace, or embedding declared inside `A.19` `CharacteristicSpace` with no domain-transfer claim;
- category-theoretic proof internal to a domain where that formalism is the local theory;
- one-off pedagogical metaphor not reused for decision, evidence, assurance, publication, bridge, comparison, or transfer.

False-negative bank: open `C.29` even when no polished mathematical buzzword appears if the working problem has a structure that changes an admissible next move and ordinary prose is currently hiding it.

| False-negative situation | Why `C.29` is live | Cheap move |
|---|---|---|
| “Something is off, but we cannot yet say whether it is flow, priority, meaning, or evidence.” | The cue is not stable enough for `ProblemStructureCue`. | Stay in language-state work first; do not make C.29 create a mathematical lens from an unstable cue. |
| “We have many tasks waiting, but cannot see where flow slows.” | Queue or flow structure can expose bottleneck and WIP boundary. | Use `MLA.LensCandidateNote` for queue/flow; estimate arrivals, service, waiting, and bottleneck. |
| “This comparison feels important, but distance is unclear.” | Metric-space distance, topology, embedding, or transport adequacy is live. | Name what comparison preserves and loses before using the comparison. |
| “We transfer a structure between contexts because it looks the same.” | Mathematical-lens adequacy and bridge loss are live. | Name preserved/lost structure and use `F.9` when cross-context meaning or substitution is live. |
| “A latent space is used as a scientific explanation.” | Learned-lens overread is live. | Name observation map, validation slice, generalization boundary, and stop causal or ontology overread. |
| “The method scales because the mathematics is elegant.” | Scale-law adequacy or BLP preference claim is live. | Name scale variable/window and use `C.18.1` or `C.19.1` when scale advantage is claimed. |

Entry guidance states when `C.29` is the first governing locus and when another pattern is first:

| Entry situation | First governing locus | Tempting wrong first locus |
|---|---|---|
| mathematical-lens adequacy inside a phrase such as "market is a field" | `C.29` | `C.26`, `F.9`, or `A.3.3` before lens adequacy is checked |
| explanation-facing rendering that uses a mathematical lens | `E.17.EFP`; `C.29` only for the mathematical-lens adequacy part when that lens affects explanation use | `C.29` as the first pattern for every explanation |
| bounded comparative review unit with a mathematical comparison basis | `E.17.ID.CR`; `C.29` only for lens adequacy or rival-lens support | `C.29` as the comparison or adjudication record |
| same-described-entity representation-scheme transition | `A.6.3.RT`; `C.29` only if the transition imports a contested or use-affecting mathematical lens | `C.29` for every table, diagram, geometry, or notation shift |
| coarsened rendering useful only under narrower admissible use and source-bearing reopen | `A.6.3.CSC`; `C.29` only if the coarsening depends on mathematical abstraction or coarse-graining | `C.29` as source-bearing return or bridge support |
| within-context representation adequacy | `C.29` | `F.9` when no cross-context meaning claim is live |
| quantum-like dashboard or probe-order claim | `C.26` plus `C.29` compatibility | physical quantum ontology |
| graph state space | `A.19` or `A.3.3` unless lens transfer is explicit | `C.29` for every graph word |
| category bridge across contexts | `F.9` plus `C.29` adequacy relation | duplicate bridge semantics inside `C.29` |
| prediction, rate, trajectory, recovery, convergence, or rhythm claim | `C.27` when temporal adequacy is live; `C.29` only for lens adequacy | treating a mathematical prediction cue as enough for temporal-use support |
| decorative scale language | no `C.18.1` or `C.19.1` unless scale behavior is live | scale-law review for every scale word |

Admissible entry stops are: no MLA needed, MLA one-line opened, or neighboring governing pattern selected.

#### C.29:4.4.6 - Governing-locus boundary table

A receiving `C.29` application uses this governing-locus discipline so mathematical-lens adequacy stays in the C.29 discipline rather than becoming a second authority over neighboring claims.

Positive governed claim:

> A C.29 application gives a pattern-local adequacy discipline for claims that use a mathematical object, formalism, learned representation, simulation substrate, or mathematical family as a mathematical lens for a stated use. The application asks for candidate mathematical object, lens mapping mode, preserved and lost structure, visible invariant or distinction, `LensSupportPosture` or validation posture, admissible use, non-admissible use, and stop condition.

Boundary transfer rule: when the live claim is a choice result, work plan, evidence path, assurance tuple, explanation rendering, comparative review unit, representation shift, temporal claim, bridge, causal-use claim, measurement claim, scale-law claim, selector, or benchmark, the `NeighborGoverningLocusNote` names the exact receiving FPF locus and exact project-side record. A C.29 application can contribute a lens-supported prediction, distinction, obstruction, diagnostic boundary, or rival-lens note that the receiving record can cite; it does not create that neighboring record.

| Live object or claim | Governing FPF locus | MLA adequacy contribution |
|---|---|---|
| mathematical-lens adequacy | `C.29` | Names the MLA discipline: candidate mathematical object, lens mapping mode, preserved/lost structure, invariant or distinction, `LensSupportPosture`, admissible use, non-admissible use, and stop condition. |
| durable reusable names beyond pattern-local fields | `F.18` | Cite when `MLA` names become durable beyond C.29-local use. |
| broad wording and semantic recovery | `E.10`, `E.10.SEMIO` | Obey head-kind, register, and semio repair discipline. |
| relation precision, arity, polarity, and slot structure | `A.6.P`, `A.6.5` | Apply only if relation substrate becomes representation affecting the stated use. |
| object, description, and carrier distinction | `A.7` | Do not identify the phenomenon directly with the mathematical object. |
| dynamics state space and transition law | `A.3.3` | Assess imported or contested lens adequacy; do not govern dynamics semantics. |
| `CharacteristicSpace`, slots, topology, order, and metric-space distance overlays | `A.19` | Apply only when an overlay becomes a domain-transferring or publication-bearing lens. |
| `ChoiceResult`, local choice record, selected-set publication, option-selection claim, or selector/benchmark result | `C.11`; `G.5`/`G.9` when selected-set or benchmark publication is live | Can contribute a lens-supported prediction, distinction, obstruction, diagnostic boundary, or rival-lens note for the decision or selector record. |
| selected method, method-family selection, `U.WorkPlan`, performed `U.Work`, work-result record, or work-relevant source restoration | `A.15`, `A.15.1`, `A.15.4` | Can contribute method-relevant lens adequacy; method, plan, performed-work, and source-restoration records stay with the A.15 family. |
| evidence path, source currentness, provenance, evidence carrier, or model card/datasheet used as evidence | `A.10` | States `LensSupportPosture` only; evidence paths and provenance remain A.10 matters. |
| assurance, readiness, reliability, release confidence, safety, trust, or engineering justification | `B.3` plus relevant G patterns when live | Treats lens adequacy as possible input only; mathematical elegance does not raise assurance. |
| measurement construction, scale/unit/comparability, or evidence-stub adequacy | `C.16` | States measurement-dependent `LensSupportPosture` only; measurement construction, scale/unit/polarity, direct comparability, and evidence-stub adequacy stay with `C.16`. |
| explanation-facing rendering or generated explanation use | `E.17.EFP` | States mathematical-lens adequacy for the mathematical explanation used inside the rendering; explanation-use discipline stays with `E.17.EFP`. |
| bounded comparative review unit | `E.17.ID.CR` | States lens adequacy for a mathematical comparison basis or rival lens when that basis affects the comparative review use. |
| same-described-entity representation-scheme transition | `A.6.3.RT` | Applies only if the representation shift imports a contested or use-affecting mathematical lens. |
| coarsened rendering with narrower admissible use and source-bearing reopen | `A.6.3.CSC` | Applies only if the coarsening depends on mathematical abstraction, quotienting, or coarse-graining. |
| cross-context meaning, bridge kind, direction, CL, loss, and substitution | `F.9` | Reference Bridge; do not duplicate Bridge Card semantics. |
| causal-use support | `C.28` | Block causal overread or cite a `C.28` application or support record. |
| forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, temporal window, or rate-change used as sufficient for a use | `C.27` | Can state that a mathematical lens supports a prediction or distinction; temporal-claim adequacy stays with `C.27`. |
| scale-law and Bitter-Lesson preference claims | `C.18.1`, `C.19.1` | Cite scale-window or BLP evidence when scale behavior or scale advantage is live. |
| quantum-like modeling | `C.26` | Treat `C.26` as MLA-compatible specialization, not as full-card inheritance for every QL-lite note. |
| selectors, benchmarks, parity, SoTA packs, and model-selection publications | `G.5`, `G.9`, `G.2`, `G.10` | Selector or benchmark records govern publication and evaluation; an MLA card can contribute lens adequacy for a selector or benchmark input only. |


#### C.29:4.5 - `MLA.Card@Context` shape

`MLA.Card@Context` is a pattern-local card in `C.29`. It is not `U.MLACard`, `U.LensAdequacyRecord`, or any universal `U.*` kind.


Namespace note: `MLA.Card@Context`, `MLAOutputRef`, `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, and `CC-MLA-*` are `C.29`-local instruments unless they cite existing FPF kinds or refs. `MLAOutputRef` references the applicable `C.29` output for the stated use; it is not a demand for `MLA.FullCard`. Do not mint generic suffixes such as `SystemMLA`, `MLAQuality`, or `MLACompliance`. Durable cross-pattern MLA names, records, or refs require explicit mint/reuse and naming/admission support through `F.8`, `F.18`, `C.3`, and `E.9`; otherwise they remain pattern-local labels.

Read the MLA card through three aspects:

| Aspect | Fields or refs | Boundary |
|---|---|---|
| Mathematical substrate | `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `InvariantsExposed` | Names the representation; does not identify the phenomenon with the mathematical object. |
| Support and validation | `LensSupportPosture`, `ValidationUseOverlayRef?`, `LearnedLensOverlayRef?`, failure case, uncertainty or approximation note | States support for this use; does not create an evidence path, benchmark result, assurance, or release confidence. |
| FPF use and boundaries | `admissibleUse`, `nonAdmissibleUse`, `StopCondition`, `BridgeRefSet?`, `CausalUseDisposition?`, `AssuranceUseDisposition?`, `ExportPolicyRef?` | States what the reader may do and where neighboring FPF loci carry live claims. |

Validity boundary: mathematical validity of the object under its assumptions is not the same as representational adequacy to the phenomenon; representational adequacy is not empirical validation for a use; empirical validation is not causal-use support; causal-use support is not assurance, release confidence, decision sufficiency, or benchmark superiority.


```text
MLA.FullCard base fields:
MLA.Card@Context := {
  TargetPhenomenon,
  describedEntityRef?,
  BoundedContext,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  InvariantsExposed,
  LensSupportedPredictionOrDistinction?,
  LensSupportPosture,
  admissibleUse,
  nonAdmissibleUse,
  StopCondition
}
```

Conditional fields apply only when the corresponding neighboring claim, claim-bearing use, or publication use is live:

```text
MLA.FullCard conditional fields := {
  DynamicsRef?,
  TransitionLawRef?,
  ObservationMapRef?,
  ScaleWindow?,
  CoarseGrainingRule?,
  SourceReturnCondition?,
  PublicationUsePosture?,
  PrincipalRivalLens?,
  RivalLensSet?,
  RivalLensRelation?,
  ValidationUseOverlayRef?,
  LearnedLensOverlayRef?,
  BridgeRefSet?,
  CausalUseDisposition?,
  AssuranceUseDisposition?,
  ExportPolicyRef?
}
```

**Plain reading of the card.** A useful mathematical lens says: what phenomenon is being seen, through which mathematical object, by what mapping, what survives, what is lost, what becomes visible, what support posture and validation boundary support this use, the now-admissible user move, the blocked user inference, and where the lens stops.


#### C.29:4.5a - Conditional overlays

The base card stays light. These overlays are used only when their use is live. Ordinary C.29 use does not fill this block; it escalates here only when the claim is already publication-facing, assurance-input, benchmark, bridge, model-selection, prediction, scientific/model, learned-lens, or causal-use facing.


```text
MLA.ValidationUseOverlay@Context :=
⟨
  ClaimUse,
  ValidationRegime,
  EvaluationSlice,
  ApproximationOrUncertaintyNote,
  KnownFailureCaseOrCounterexample,
  SensitivityOrRobustnessNote?,
  DomainOfApplicability,
  OutputChangeCondition?
⟩
```

Use the validation overlay when the lens supports prediction, publication, assurance input, benchmark use, model selection, or scientific/model claim. `LensSupportPosture` alone is then insufficient. Keep the neighboring notions separate: verification is proof or formal checking under stated assumptions; validation is fit for a declared use and regime; calibration aligns model parameters or readouts with observations; explanation states why the lens makes a distinction intelligible. The C.29 output does not let any one of these four labels silently stand in for the others.

```text
MLA.LearnedLensOverlay@Context :=
⟨
  DataOrTrainingRegime,
  ObservationMapRef,
  GeneralizationClaim,
  DiscretizationOrResolutionPolicy?,
  ValidationRegime,
  ApproximationOrUncertaintyNote,
  StopCondition
⟩
```

Use the learned-lens overlay when the mathematical object is fitted, learned, latent, simulation-trained, data-derived, a neural operator, a surrogate solver, an embedding, or a world-model representation.

Learned-lens stop variants are named explicitly when they are tempting:

| Tempting overread | Stop condition form |
|---|---|
| out-of-distribution generalization | no generalization outside the declared validation regime |
| causal mechanism | no causal mechanism claim without `C.28` and evidence support |
| latent dimension ontology | latent coordinate or factor is not an entity kind without separate ontology and evidence |
| unobserved-variable recovery | no recovery of hidden variables beyond the declared observation map and validation slice |
| benchmark superiority | no benchmark or selector superiority outside the declared evaluation slice and relevant `G.*` record |
| assurance or release use | no assurance, release, or reliability use without `A.10`, `B.3`, and relevant G-pattern support |


```text
MLA.CausalAbstractionCheck@Context :=
⟨
  LensMappingMode,
  InterventionStructureStatus ∈ {preserved, approximated, notClaimed},
  CounterfactualUseStatus ∈ {preserved, approximated, notClaimed},
  C28ApplicationRef?
⟩
```

This is not a first-class causal abstraction card. It is a lightweight check: when `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation, and `admissibleUse` would include intervention, policy, counterfactual, or causal explanation, apply `C.28` for causal-use support.

#### C.29:4.5b - Repair decision table

| Failed or missing item | Required repair |
|---|---|
| no `CandidateMathObject` | If the problem still needs a mathematical lens for the next move, first name the `ProblemStructureCue` and write an `MLA.LensCandidateNote` with the cheapest candidate lens family and admissible next move; downgrade to ordinary prose or remove the mathematical claim only when no candidate lens changes action. |
| no `LensMappingMode` | Choose a lens mapping mode or downgrade to analogy-only prompt. |
| no `PreservedStructure` | Remove the claim-bearing mathematical phrase. |
| no `LostStructure` | Add a loss note, downgrade, or support an equivalence or isomorphism claim. |
| no invariant, obstruction, distinction, or payoff | Keep the phrase as didactic recognition cue or orientation-only. |
| no `LensSupportedPredictionOrDistinction` where decision, prediction, or model selection is live | Block decision or assurance use; downgrade to analogy-only if no supported consequence exists. |
| evidence is analogy-only | Block decision, publication-as-established-model, assurance, release, and causal use unless evidence, validation, causal-use support, or assurance support is supplied by its governing pattern. |
| no `LensSupportPosture` | Block decision, publication, assurance, benchmark, and release use. |
| causal, intervention, policy, or counterfactual overread | Apply `C.28` or block causal use. |
| cross-context meaning, export, or substitution overread | Apply `F.9` or block export and substitution. |
| scale, universality, knee, exponent, or scale-advantage claim | Apply `C.18.1` or `C.19.1`, or keep the lens local and bounded by stop condition. |
| assurance or release use | Apply `A.10`, `B.3`, or relevant G patterns, or block assurance use. |
| `StopCondition` is generic | Name the most tempting nearby overread the lens does not license. |

#### C.29:4.6 - Field meanings

| Field | Meaning selected for `C.29` | Boundary guard |
|---|---|---|
| `TargetPhenomenon` | Plain entry prompt naming the phenomenon or situation to be understood. | Not a `U.Kind`, not a described-entity slot, and not a publication object. |
| `describedEntityRef?` | Exact reference used when the lens appears inside a claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. | Required only when the lens appears in claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. |
| `BoundedContext` | Context in which the lens is claimed to work. | Cross-context use cites `F.9`. |
| `CandidateMathObject` | Concrete mathematical object, structure, formal role, learned representation, or local formalism. | Broad family labels are prompts until narrowed. |
| `LensMappingMode` | `C.29`-local lens mapping mode. | Does not replace `F.9` BridgeKind, `A.6.P` `RelationKind`, `C.3` kind, or domain relation kinds; cross-context transfer uses `F.9` when bridge semantics are live. |
| `PreservedStructure` | Structure the lens carries into the declared use. | No preserved structure means the mathematical phrase cannot carry the stated use. |
| `LostStructure` | Structure the lens drops, abstracts away, or cannot support. | Empty loss requires explicit equivalence or isomorphism support. |
| `InvariantsExposed` | Invariant, obstruction, fixed point, symmetry, conservation law, diagnostic boundary, or other payoff. | If no payoff is visible, downgrade to recognition cue. |
| `ObservableOrControllableCue?` | Cheap cue naming what can be observed, read out, assigned, varied, or validated before a candidate lens can change action. Examples include arrivals, work in progress, service time, wait time, edge meaning, intervention assignment, outcome readout, observation map, validation slice, scale variable, or scale point. | Not a measurement construction, evidence record, causal-support result, or validation verdict. Open `C.16`, `A.10`, `C.28`, or `A.3.3` when those claim types are live. |
| `ObservationOrReadoutNeeded?` | Optional one-line note naming the observable, readout, assignment, outcome, validation slice, or scale point still needed before the lens supports the stated admissible move. | If this missing item carries measurement, evidence, causal, dynamics, or validation force, the neighboring pattern governs that neighboring work. |
| `LensSupportedPredictionOrDistinction?` | Required when prediction, decision, method selection, model selection, or publication-as-model is live. | Not required for orientation-only use. |
| `DynamicsRef?`, `TransitionLawRef?` | References to `A.3.3`-owned dynamics when dynamics semantics are live. | `C.29` does not own dynamics. |
| `ObservationMapRef?` | Probe, readout, or observation map when observation makes the lens admissible for the declared use. | Required for learned or measurement-dependent lenses when live. |
| `ScaleWindow?`, `CoarseGrainingRule?` | Scale range and coarse-graining or compression rule when scale behavior, macro/effective description, universality, coarse behavior, latent compression, or renormalized description is live. | `C.18.1` and `C.19.1` carry scale-law and BLP evidence; the C.29 output states only how the lens remains adequate inside the declared window. |
| `SourceReturnCondition?` | Condition under which the reader must return from the compressed or coarse description to the source-side variables, observations, cases, or mechanisms. | Required only when abstraction, coarse-graining, compression, latent representation, or macro-modeling drops source-side distinctions that could matter to the stated use. |
| `PublicationUsePosture?` | Optional note for publication-facing use: `orientationOnly`, `explanationFacing`, `comparisonInput`, `decisionInputCandidate`, `benchmarkInput`, `assuranceInputCandidate`, or `reusableModelPublication`. | Does not publish, release, benchmark, assure, or decide anything by itself; the neighboring publication, benchmark, evidence, decision, and assurance loci still govern those claims. |
| `OutputChangeCondition?` | Condition under which the current C.29 output must be narrowed, demoted, replaced, retired from claim-bearing use, or supported by a neighboring FPF locus. | Not a process log or standing status record; it states a result boundary for the current lens use. |


| OrdinaryRivalOrFallback | Ordinary prose, accepted local theory, direct measurement, or simpler neighboring-pattern exit the reader would use without this lens. | Required for cheap outputs; prevents prestige bias before broad rival review. |
| `PrincipalRivalLens?` | Default ordinary or most relevant rival lens. | Preferred over a broad literature survey. |
| `RivalLensSet?` | Broader comparison set only when publication, selection, or claim-bearing comparison is live. | Not a `G.5` selector, benchmark harness, or parity result. |
| `RivalLensRelation?` | Declared relation between the current lens and the principal rival or live rival set. Allowed local relation values include `ordinaryFallback`, `complementary`, `sameUseLowerCost`, `morePreservedStructureHigherCost`, `lowerErrorOnDeclaredEvaluationCriterion`, `clearerExplanationForDeclaredReader`, `bridgeNeedsF9`, `causalUseNeedsC28`, `differentScaleWindow`, `differentLossProfile`, `incomparableForCurrentUse`, `blockedByStopCondition`, and `unresolved`. Examples: a queueing lens and a causal lens can be complementary for different moves; a latent manifold and a causal graph can conflict when latent axes are read causally; an RG-like lens and a micro-dynamics lens can have different scale windows. | Names disagreement only; a C.29 output is not a winning-lens choice, literature review, selector result, benchmark result, or parity result. Any superiority claim names the evaluation criterion, reader, cost, scale window, or receiving pattern that makes the comparison admissible. |

| `LensSupportPosture` | Local support-posture label. | Not evidence, an EvidenceGraph, a PathId, or an assurance score. |
| `BridgeRefSet?` | Reference to `F.9` Bridge material when context crossing is live. | Bridge semantics stay with `F.9`. |
| `CausalUseDisposition?` | One of `noCausalUseClaim`, `causalUseBlocked`, `C28ApplicationRef`, or `C28SupportRecordRef`. | No causal-reference shortcut; no causal verdict from `C.29`. |
| `AssuranceUseDisposition?` | One of `noAssuranceUseClaim`, `assuranceUseBlocked`, `evidenceInputOnly`, `A10Ref`, or `B3ApplicationRef`. | No assurance verdict from mathematical elegance. |
| `admissibleUse` | Admissible current use of the lens. | Matches evidence and validation posture. |
| `nonAdmissibleUse` | Tempting neighboring use that is blocked or handed to another governing locus. | Names the neighboring pattern when live. |
| `StopCondition` | Most tempting nearby claim the lens does not license. | Main anti-overread output; not boilerplate. |
| `ExportPolicyRef?` | Governed reuse or export policy when publication or downstream reuse is live. | Not required for local orientation or mini-card use. |

