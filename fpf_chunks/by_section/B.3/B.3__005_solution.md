---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__005_solution.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:4 — Solution"
line_start: 39311
line_end: 39433
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

### B.3:4 - Solution

#### B.3:4.1 - Start from one assurance question

State these three things before choosing measures or a record:

1. the exact target claim;
2. the named assurance use;
3. the conclusion that must be supported, narrowed, or refused for that use.

Keep the following objects separate whenever they are current:

1. world-side facts and direct domain results;
2. the target-claim episteme;
3. evidence-use relations and source-provenance paths;
4. any assessment Work and the System that performed it;
5. formal, empirical, causal, measurement, conformance, or comparison input results;
6. the assurance-result episteme;
7. calculation traces, witnesses, and an optional note or publication that cites the result;
8. later reliance, status use, gate, permission, release, or action.

Evidence can support or challenge a claim. It does not make the target fact true. A favorable assurance result does not pass a gate, grant permission, or prove that later work relied on it.

#### B.3:4.2 - Use the smallest sufficient result

The compact result contains only facts every B.3 use needs:

```text
AssuranceResult:
  targetClaimRef:
  assuranceUse:
  basisRefs:
  disposition: supported-for-use | narrowed | abstain | evidence-needed | reopen | blocked
  limitationsAndNotCarried:
  reopenCondition:
```

`targetClaimRef` identifies the exact C.2.1 episteme or one exact C.2.1 `ClaimAddress` when the use concerns one addressed claim inside a larger episteme. `basisRefs` cite the direct results, evidence-use relations, provenance paths, argument claims, or domain rules actually used. A compact result is complete when these fields decide the named use and another person can see why the stronger use is not carried.

Add a claim scope, condition set, interpretation scheme, audience, or time window only when changing it could change the conclusion. Keep design and run conclusions separate whenever their inputs or conditions differ.

Add assessment Work, performer, Method, application bindings, witnesses, or a reusable record only when the receiving use depends on competence, conflict of interest, timing, reproducibility, contest, redress, or later replay. These identities are never mandatory merely because B.3 is used.

An optional assurance note may cite the result and its basis. B.3 does not define a reusable `RelianceSafetyCase`, a safety authority, or a general contest-and-redress profile. If such a reusable object is needed, it requires its own problem, ontology, sources, minimum output, and direct domain boundaries.

#### B.3:4.3 - Name each characteristic by its bearer and scale

Include a characteristic result only when the assurance argument consumes it. State:

```text
AssuranceCharacteristicResult:
  bearerRef:
  characteristic:
  scaleAndUnit:
  valueOrInterval:
  interpretationForThisUse:
  basisRef:
```

One characteristic name must not silently change meaning between subjects. System reliability, replication quality, evidential support, proof inspectability, and relation congruence are different characteristics even when a local source labels several of them `R` or `CL`.

The legacy letters `F`, `G`, `R`, and `CL` may appear inside a declared local scheme, but B.3 assigns them no universal cross-domain meaning:

- **Formality or inspectability.** Formal structure can make assumptions and inference steps easier to check. It raises assurance only when the named argument explains which uncertainty or verification need it closes. Making a wrong model proof-grade does not improve truth or empirical adequacy.
- **Claim scope.** `U.ClaimScope` stays an A.2.6 value. It is not a quality coordinate. Widening or narrowing scope changes the claim and its applicable use under the declared scope rules.
- **Reliability-like characteristics.** Use the exact domain definition, bearer, population or trials, conditions, scale, unit, and qualification window. A system reliability measure and an evidence-quality judgment are not interchangeable.
- **Relation congruence.** Characterize one exact mapping, calibration, interface, or other relation occurrence only under a declared scale and interpretation. The value neither changes the participants nor supplies a universal penalty.

Never average ordinal values. Do not subtract an ordinal value from a ratio quantity. Thresholds and order comparisons are valid only under the scale that defines them.

#### B.3:4.4 - Aggregate only under an applicable model

B.3 supplies no default fold. When the assurance argument combines quantitative or ordered inputs, cite:

1. the exact result claims being combined;
2. the dependency or alternative-path structure;
3. the domain aggregation rule or model;
4. independence, dependence, calibration, and unit assumptions;
5. the calculation or ordered comparison;
6. the rival rule that would matter if an assumption fails.

Use `min` only when the cited domain rule makes the weakest input a lower bound or bottleneck for the exact quantity. It is not universally conservative. If no applicable aggregation rule is available, report the inputs separately and return a bounded, non-positive, or unresolved disposition. Do not manufacture one score to make the result look complete.

Several independent evidence lines may strengthen an argument only through the rule that states how their dependence and coverage are handled. Claim-scope intersection or union follows A.2.6 and the relevant evidence model; it is not an assurance arithmetic shortcut.

#### B.3:4.5 - Choose one of three proof paths

**Compact path.** Use the six-field result in 4.2. Stop when it decides the named use.

**Calculated or model-bearing path.** Add the characteristic results, dependency structure, assumptions, aggregation rule, rival, calculation trace, and sensitivity or failure condition actually used.

**Replay path.** Add Work, performer, Method, application bindings, witnesses, and a reusable note only when those identities change the named assurance use. For any assessment Work, use A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently. Add F.6 only if the replay must also say exactly under which assignment the Work was performed. The Work, performer, Method, optional assignment check, result, witness, note, and publication remain separate.

Do not select the replay path merely because the use is important. Importance may make more basis necessary, but every added field must change inspectability, contestability, or the decision.

#### B.3:4.6 - Keep visible authority outside the result

A badge, score, dashboard tile, credential display, provenance mark, model card, datasheet, data card, assurance document, attestation, generated confidence phrase, or publication form can be a cue, source, evidence item, or representation. It contributes to assurance only through an exact claim and basis relation used by the argument.

If the visible item only reports a status, gate decision, permission, warning, or source location, use its direct pattern and produce no B.3 result. If an assurance claim is current, cite the item only for the property it actually establishes. A valid signature or provenance chain can establish origin and integrity without establishing safety, truth, compliance, or readiness.

#### B.3:4.7 - Leave domain obligations with their direct patterns

B.3 evaluates an assurance claim. It does not define safety duties, access rules, responsibility, affected-party disclosure, contest, redress, people or team status, resource allocation, release authority, or controlled action. Cite each applicable direct rule as a premise or limitation.

When a direct domain rule says a consequential use requires an assurance claim, state that claim and then apply B.3. When the direct rule requires a decision, permission, review, contest route, or redress relation instead, use that result directly. A display that affects behavior does not by itself open B.3.

#### B.3:4.8 - Preserve time, currentness, and design/run distinctions

State the exact window only when time changes the assurance conclusion. Monitoring, drift, incidents, evidence refresh, version change, policy change, gate change, or a newly discovered defeater can narrow, reopen, or withdraw a result while the target fact and target-claim identity remain unchanged.

Design evidence and run evidence may support different claims. Produce separate results when target use, conditions, scope, or evidence window differs; compare them instead of merging them into one score.

#### B.3:4.9 - Keep causal-use and method-structure branches direct

When an assurance argument depends on a causal-use claim, consume the exact `C.28` result and its stated supported and unsupported uses. B.3 does not re-run causal identification. An unsupported causal-use result narrows, blocks, or leaves the assurance claim unresolved; it does not become a low universal reliability coordinate.

When composition, fallback, selection, or family organization among Methods matters to the assurance argument, use `A.22` to select the exact structure for that question and use the local designator `MethodRelationStructure` only for that selected structure. Do not introduce a universal method-relation kind or infer structure from a list of Methods.

#### B.3:4.10 - Use Working-Model declarations only for what they state

An E.14 Working-Model assertion may contribute its declared validation posture and grounding links. A postulate still needs the empirical basis required by the current assurance use; an inferential claim needs its reasoning basis; an axiomatic or constructive claim needs the exact construction and identity basis it relies on. The declaration, grounding link, assessment Work, assurance result, and publication remain different objects.

