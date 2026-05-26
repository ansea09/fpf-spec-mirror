---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern Quality Characteristic Space"
section_id: "E.21:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__006_archetypal-grounding.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "E.21 — FPF Pattern Quality Characteristic Space"
  - "E.21:5 — Archetypal Grounding"
line_start: 64641
line_end: 64682
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

### E.21:5 - Archetypal Grounding

**Tell.** A good FPF pattern is not merely complete, attractive, or formally strict. It is an action-guiding method description whose quality is a scoped bundle: it helps the right reader recognise the right situation, make the next admissible move, avoid the wrong neighbour, and trust the result for the declared use.

**Recognition matrix.**

| Working situation | First honest `E.21` move | Likely wrong substitute | Coordinate tested |
|---|---|---|---|
| A system-architecture pattern has precise vocabulary and strong sources, but the opening never says what an engineer-manager does first. | Check activated `firstMoveRecoverability`; if it passes, read `WorkingSituationAndUseBoundaryRecognizability` and `ActionPathGuidance` from the opening and `Solution`. | Treat SoTA strength as enough for admission. | `firstMoveRecoverability`, `WorkingSituationAndUseBoundaryRecognizability`, `ActionPathGuidance`, `SoTABindingAndCurrentness`. |
| A publication or evidence pattern reads beautifully, but `PatternQualityStatus = admissibleForDeclaredUse` is being cited as product assurance. | Keep the quality result as pattern-quality evidence and cite `A.10`/`B.3` only when the project-side claim is live. If a card, summary, or status line is visible, check whether the projection stays a scoped echo. | Treat review approval as project certification. | `NeighborAuthorityAndBoundedUseFit`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, `ExternalEntryAndProjectionIntegrity`. |
| A mathematical-lens pattern has the right formula vocabulary, but no preserved/lost structure or non-use boundary. | Require the formal/lens proof sketch: preserved structure, rejected structure, payoff, admissible use, non-admissible use, and stop condition. | Count formal notation as sufficient lens fit. | `FormalClaimLegalityAndLensFit`. |
| A naming-heavy pattern has better prose after editing, but the kind and relation load are still ambiguous. | Fill local name-precision cards or use the full `F.18 -> A.6.P -> E.10` chain. | Treat lexical polish as ontology repair. | `SemanticKindAndNameRecoverability`. |
| Two variants both pass eligibility: one is shorter; the other has stronger examples and relation closure. | Compare through `DominanceSet`, then use `TieBreakerSet` only if neither dominates. | Average scores or choose the version that feels cleaner. | `UseAffordabilityAndApparatusProportionality`, `CaseCountercaseAndTransferCoverage`, `EvolutionFrontAndRefreshDiscipline`. |
| A pattern-quality read raises every visible coordinate to `4` or `5`, but the pattern becomes longer, harder to enter, and more expensive to maintain. | Activate `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `ProxyForValueSubstitutionResistance`; ask what became worse before accepting the stop condition. | Treat "all coordinates are high" as enough by itself. | `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, `ProxyForValueSubstitutionResistance`. |

**Show - System pattern.** A system-architecture pattern has precise structure vocabulary and a strong SoTA row, but its opening never says what an engineer-manager should do first. Activated `firstMoveRecoverability` fails for ordinary use. The admissible result is not "quality 78/100"; it is `repairBeforeUse` for admission, or `admissibleWithNarrowerUse` if it is kept as expert-only support.

**Show - First-pass target read.** An author opens a candidate FPF pattern and writes: `PatternVersionRef = C.xx@draft-3; WorkingReaderScope = engineer-manager using the pattern for first ordinary application; IntendedUse = continue drafting or repair before use; QualificationWindow = current FPF edition`.

The author reads only `Problem frame` and `Solution`. If the pattern says which object it governs but gives no first admissible action-guiding move, the first-pass read closes: activated `firstMoveRecoverability` fails and `PatternQualityStatus = repairBeforeUse` for ordinary use. No `PatternQualityFront`, `TelemetrySet`, or full coordinate table is needed.

If the first move exists but the continuation path or apparatus required to apply it is heavier than the ordinary case can justify, activate `ActionPathGuidance` and `UseAffordabilityAndApparatusProportionality`. The repair is to keep the ordinary first move light and move heavier support to a named neighbouring pattern or high-assurance support card.

**Show - Episteme pattern.** A publication or evidence pattern reads beautifully and has many examples, but it treats an `E.19` pattern-quality result as project assurance. `NeighborAuthorityAndBoundedUseFit` and `ClaimSupportTraceabilityCurrentnessAndReplayability` fail because assurance belongs in `B.3` and evidence/currentness belongs in `A.10`. If a dashboard tile or generated summary repeats the result without scope and status payload, `ExternalEntryAndProjectionIntegrity` also fails. The repair is to keep the pattern-quality result as pattern-quality evidence and open the exact project-side receiving relation only when needed.

**Show - Mathematical lens pattern.** A pattern says that it uses a characteristic space, but then compares variants by "overall quality". `FormalClaimLegalityAndLensFit` fails because the ordinal coordinates are being collapsed and the preserved and rejected structures are not named. The repair is to state the finite ordinal coordinate set, eligibility predicate, dominance relation, tie-breaker boundary, and non-admissible scalar uses.

**Show - New pattern candidate.** Two drafts of the same pattern both pass eligibility. Draft A is shorter and easier to read; Draft B has better SoTA, case/countercase breadth, and neighbour closure but adds a heavier bundle card. Neither dominates if Draft B's extra apparatus is live only for high-assurance reuse. The correct output may be one ordinary draft plus a support card for high-assurance use, not one averaged winner.

**Show - Goodhart trade-off.** An author raises visible E.21 coordinates to high values by adding proof sketches, support cards, and SoTA rows. The pattern now reads better on the visible table, but a cold author needs more time to find the first move and a maintainer must update more named sections or support records after each small repair. The quality read cannot stop until `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `ProxyForValueSubstitutionResistance` are read by content evidence. If those coordinates fall, the candidate is not an improvement for the declared ordinary-use scope; it may become a high-assurance variant instead.

**Show - Self-application support card.**

```text
CoordinateEvidenceRef:
  Coordinate: ActionPathGuidance
  EvidenceKind: recognitionTextEvidence + workedCaseEvidence
  HostSectionRef: E.21:1, E.21:4.9, E.21:5
  Claim: The reader has a first move, a continuation loop, and heterogeneous examples that show when the loop changes the quality result.
  Limitation: This is pattern-quality guidance, not project-side work authorization.
```

