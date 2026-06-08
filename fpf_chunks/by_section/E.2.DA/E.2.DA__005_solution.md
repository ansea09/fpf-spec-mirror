---
chunk_kind: "child"
pattern_id: "E.2.DA"
pattern_title: "FPF Pillar-Adequacy Evaluation CharacteristicSpace"
section_id: "E.2.DA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.2.DA/E.2.DA__005_solution.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "E.2.DA — FPF Pillar-Adequacy Evaluation CharacteristicSpace"
  - "E.2.DA:4 — Solution"
line_start: 56092
line_end: 56225
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.11"
  - "E.2"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.2.DA:4 - Solution

`E.2.DA` is the Pillar-adequacy specialization of `A.19.ECS`. It evaluates one FPF object under improvement against all eleven `E.2` Pillars for a declared use.

There is no smaller `E.2.DA` evaluation. If the caller only needs local pattern quality, `DRR` adequacy, or wording repair, that is a different object-under-improvement evaluation. Once `E.2.DA` is invoked, every Pillar coordinate receives a value, short rationale, evidence locus, and shared evidence basis for the FPF object being evaluated.

#### E.2.DA:4.1 - Local names and kind settlement

| Local name | Kind and role |
|---|---|
| `FPFPillarAdequacyEvaluation` | Authored evaluation record over one scoped FPF Pillar-adequacy claim. |
| `FPFObjectUnderImprovementRef` | FPF object version named by value being evaluated. |
| `FPFAdequacyUseScope` | Declared FPF-level use the object must serve. |
| `FPFAdequacyReaderScope` | Primary reader family and working situation for the adequacy claim. |
| `FPFAdequacyQualificationWindow` | Edition, source-currentness, neighbour, release, or comparison window for which the values hold. |
| `FPFPillarAdequacyCoordinateSet` | The eleven required Pillar coordinates in this pattern. |
| `FPFPillarAdequacyEvidenceBasis` | Checked loci named by value in the scoped FPF object: pattern bodies, host or monolith sections, projections, README scenarios, ToC rows, `E.11` entry-distribution loci, `I.2` expanded entry-disambiguation cases, source rows, relation rows, companion files, evaluation results, and missing or unchecked loci that affect values. |
| `FPFPillarValueRationales` | Required result rows: Pillar coordinate, value, short rationale, and evidence locus named by value. |
| `PillarAdequacyEvidenceRefs` | Loci named by value in patterns, projections, source rows, entry rows, relation rows, or findings used as value evidence. |
| `FPFKindRestorationEvidence` | Pre-repair and post-repair object-kind, relation-or-claim-kind, slot-or-use-position when live, admissible-use, and scope evidence for broad precision or wording cleanup that affects the scoped FPF object. |
| `FPFPillarAdequacyStatus` | Admissible-use result for the scoped FPF Pillar-adequacy claim. |
| `FPFPillarAdequacyFront` | Optional non-dominated set of FPF variants or edit packages under the declared coordinate set. |

These names are local to the evaluation unless `F.18` promotes a durable name. They name FPF content objects and evaluation fields, not release state, review state, or project evidence.

#### E.2.DA:4.2 - Evaluation record

```text
FPFPillarAdequacyEvaluation:
  FPFObjectUnderImprovementRef: <object and version named by value>
  FPFAdequacyUseScope: <entry | authoring | review | project use | source absorption | corpus release | other use named by value>
  FPFAdequacyReaderScope: <primary reader and working situation>
  FPFAdequacyQualificationWindow: <edition/source/neighbour/release/comparison window>
  FPFPillarAdequacyEvidenceBasis: <checked pattern, host, monolith, projection, README/ToC/E.11/I.2 entry locus, source, relation, companion, evaluation-result, and missing loci that affect values>
  FPFPillarAdequacyCoordinateTable: <all eleven coordinates, values, short rationales, evidence loci>
  FPFKindRestorationEvidence: <when broad wording/precision repair is part of the evaluated change: pre/post kind, relation or claim kind, slot or use-position when live, admissible use, scope, governing pattern when another pattern governs the kind under repair/relation/claim/position, and preserved/split/intentionally changed/blocker disposition>
  FPFPillarAdequacyStatus: <status>
  StopOrRepairCondition: <local stop, first repair, Pillar decision, or architecture decision>
```

`E.22` may frame the evaluation purpose when the caller needs floor evaluation, exceptional improvement, trade-off inspection, open-question discovery, absorption, or proposal portfolios. `E.23` governs repeated improvement after the evaluation returns findings or candidate proposals.

#### E.2.DA:4.3 - Ordinal coordinate scale

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The Pillar is not realized for the declared FPF object and use. |
| 1 | `namedOnly` | The Pillar is named but cannot guide the FPF-level use. |
| 2 | `partiallyExpressedForDeclaredUse` | The Pillar is present but incomplete, fragile, or too local. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The Pillar is realized enough for the declared use, with known limits visible. |
| 4 | `wellExpressedForDeclaredUse` | The Pillar is clear across relevant loci and protected from common loss. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The Pillar is exceptionally realized with reinforcing loci, heterogeneous cases, and no hidden FPF-level loss. |

The values are ordinal content evaluations. They are not a scalar score, maturity ladder, release gate, or proof that development ends.

#### E.2.DA:4.4 - Required Pillar coordinates

| Pillar coordinate | Evaluation question | Good state |
|---|---|---|
| `P1CognitiveEleganceAdequacy` | Does the object expose decisive structure without ornamental formalism? | The reader sees the smallest structure that changes the move. |
| `P2DidacticPrimacyAdequacy` | Does human comprehension stay ahead of formal, tooling, or review purity? | Working situation, recognition reason, first move, and payoff stay visible. |
| `P3ScalableFormalityAdequacy` | Can informality mature toward formal assurance without forks or rewrites? | Plain, Tech, Formal, and mathematical strengthening remain staged. |
| `P4OpenEndedKernelAdequacy` | Do kernel concepts stay meta-level while domain knowledge stays in patterns? | New content extends FPF without smuggling domain doctrine into the kernel. |
| `P5FPFLayeringAdequacy` | Do modular pattern layering and neighbour authority stay intact? | Patterns can be added, replaced, or removed without shadow authority. |
| `P6LexicalStratificationAdequacy` | Are Plain, Tech, Formal, and mathematical registers recoverable when live? | Load-bearing wording maps to fields named by value, kinds, lenses, or neighbours. |
| `P7PragmaticUtilityAdequacy` | Do proofs, measures, models, and reviews change real admissible action? | The object changes prediction, decision, diagnosis, design, repair, stop, or assignment. |
| `P8CrossScaleConsistencyAdequacy` | Do composition, aggregation, boundary, emergence, and method structure stay consistent across scales? | Cross-scale claims name preserved structure, lost structure, algebra, and boundary. |
| `P9StateExplicitnessAdequacy` | Are states, transitions, currentness, editions, and qualification windows explicit when live? | Readers can tell what version/state is being used and what changes it. |
| `P10OpenEndedEvolutionAdequacy` | Can improvement continue cheaply and safely without pretending development ends forever? | Local stop conditions coexist with reopen paths for new use, source, comparison, or failure evidence. |
| `P11SoTAAlignmentAdequacy` | Does current knowledge discipline the object without citation theatre? | Current sources change moves, boundaries, examples, checks, or stop rules. |

#### E.2.DA:4.5 - Evidence and coordinate separation

One evidence locus may support several coordinates, but the rationale must say what property it supports in each coordinate. The following distinctions carry most repairs:

| Distinction | Use |
|---|---|
| `P1` vs `P2` | smallest decisive structure vs reader comprehension and first move. |
| `P2` vs `P6` | usable recognition text vs recoverable register mapping. |
| `P5` vs `P7` | right governing pattern vs useful change in action. |
| `P7` vs `P11` | practical payoff vs current source contribution. |
| `P8` vs `P9` | cross-scale invariant vs state, transition, edition, and currentness. |
| `P10` vs `E.23` | evolvability of the FPF object vs repeated improvement method. |

If a distinction cannot be recovered from the FPF object, lower the affected coordinate and state the first repair. Do not add a new local doctrine table to explain around the missing content.

`E.21` and `E.9.DA` results are evidence loci for `E.2.DA`, not inputs to be averaged. A pattern-quality value can support a Pillar only by pointing to the FPF-level effect it creates or damages.

#### E.2.DA:4.5a - Result-row discipline and calibration

An `E.2.DA` result uses this table shape:

| Pillar coordinate | Value | ShortRationale | EvidenceLocus |
|---|---:|---|---|
| `<E.2.DA coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the FPF evidence; why the higher adjacent value would overstate it, or for 5 what would lower/reopen>` | `<pattern section, monolith section, host, README scenario, ToC row, E.11 entry-distribution locus, I.2 expanded case, projection, source row, relation row, companion file, evaluation result, or missing locus named by value>` |

A Pillar essay, local-quality average, two-column table, or result whose value depends on unchecked corpus/projection/source evidence is not an `E.2.DA` result. It is only draft evaluation material. Missing or unchecked evidence lowers the Pillar coordinate that needs it; it does not make the coordinate optional.

Common calibration points:

| Pillar family | `3` | `4` | `5` |
|---|---|---|---|
| Entry, usability, and projection Pillars | The object can be used with visible limits, but projection or first-use evidence is partial. | Relevant governing loci and projections are coherent enough for declared use. | The use is replayable across governing text, projection, cold-reader or retrieval evidence, and non-use boundary. |
| Layering and semantic authority Pillars | Neighbours are plausible, but some authority or shadow-spec risk remains. | Governing patterns named by value and thin projections are distinguishable. | Authority is robust across pattern bodies, relations, projection rows, and anti-fragmentation cases. |
| Source and evolution Pillars | Source or reopen language exists, but currentness, contribution, or smallest-reopen basis is compact. | Source contribution, currentness window, and reopen condition are explicit for declared use. | Source-front movement and future reopen are replayable without freezing development after a local stop. |

#### E.2.DA:4.6 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredFPFUse` | All eleven coordinates meet the declared floor for the scoped use. |
| `repairBeforeFPFUse` | One or more coordinate floors fail for the declared use. |
| `holdForPillarDecision` | The defect requires an `E.2` Pillar amendment or precedence decision. |
| `holdForArchitectureDecision` | The defect requires pattern split, object-under-improvement, source-use, projection-role, or naming architecture decision. |
| `refreshNeeded` | A source, pattern, entry role, projection, relation, or vocabulary change invalidates a previous evaluation. |

The stop condition states the declared floor, values, bounded non-use, smallest reopen locus, and first repair if the declared use is not yet admissible.

#### E.2.DA:4.7 - Compact result form

```text
E.2.DA result:
  FPF object under improvement: <FPFObjectUnderImprovementRef>
  Declared use and reader: <scope>
  Qualification window: <window>
  Evidence basis checked: <FPFPillarAdequacyEvidenceBasis>
  Status: <FPFPillarAdequacyStatus>
  Coordinate table: <Pillar coordinate | Value | ShortRationale | EvidenceLocus for all eleven Pillars>
  First repair or stop: <repair | hold | local stop>
  Reopen if: <smallest changed locus or condition>
```

For a small release decision, the coordinate table may be compact. It is still complete. Status is not assigned from prose, a checklist count, a local-pattern average, a two-column table, or a result missing evidence loci needed by its values.

