---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__011_rationale.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:10 — Rationale"
line_start: 45117
line_end: 45336
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

### C.3.A:10 - Rationale

One final allow/refuse bit is operationally convenient but ontologically poor. Keeping declarations, candidate judgments, Scope, bridges, evidence, and disposition separate lets a reviewer see which repair is needed and prevents a guard from becoming a hidden relation, assertion, or evidence-to-truth converter.

#### C.3.A:Annex A - Regulatory and compliance alignment [A/I]

##### C.3.A:A.1 Purpose and fit

Regulations name categories such as Adult person, Class II medical device, Personal data, and Lease. A local context needs both a faithful category correspondence and explicit jurisdiction/version/time applicability. The kind channel answers “about what”; USM Scope answers “where and when”; neither answers whether one exact local candidate satisfies the target criterion.

##### C.3.A:A.2 Normative obligations

**C-REG-1 (Regulatory declarations).** Each used regulatory category SHALL be an exact authority-context local kind with a separately identified `KindSignature` declaration episteme edition. Any F value characterizes that episteme, not the kind.

**C-REG-2 (Kind correspondence).** Cross-context category use SHALL recover an obtaining KindBridge relation between exact authority and local kinds plus a separate bridge assertion with mapping, pinned editions, preservation/loss, `CL^k`, evidence, definedness, and admitted use.

**C-REG-3 (Scope).** Jurisdiction, effective dates, grace periods, and other genuinely contextual applicability conditions SHALL be Claim scope over exact context slices with explicit `Gamma_time`. A product-family or platform distinction belongs in Scope only when it is genuinely a context-slice dimension of the claim; when it classifies the target entity, recover it as an exact kind and, for candidate-bearing use, an exact candidate judgment. A direct candidate feature remains with its own governor and SHALL NOT be smuggled into Scope.

**C-REG-4 (No synonym shortcut).** A legal label, translation row, or policy card SHALL NOT substitute for the KindBridge relation, its assertion, or the target declaration.

**C-REG-5 (Exact candidate use).** Whenever a policy is applied to candidate `candidate`, the guard SHALL evaluate `J(candidate, localKind, localSignatureEdition, localSlice)` and retain `true`, `false`, or `unknown`. Declaration compatibility alone is insufficient.

**C-REG-6 (Consequences).** Justified kind- and scope-bridge consequences SHALL affect R only. They SHALL NOT alter F, G, or the candidate judgment.

**C-REG-7 (Editioning).** A change in law that changes the criterion creates another signature episteme edition; a change in applicability changes Scope. C.3.1 decides kind continuity. Guards SHALL pin editions and time and SHALL NOT rely on “latest”.

**C-REG-8 (Local adaptation).** A local nuance MAY use a RoleMask declaration. If it becomes a stable conceptual distinction, the context SHALL separately identify any new local kind and establish its obtaining subkind relation; mask reuse does not perform that change.

##### C.3.A:A.3 Regulatory guards

**Guard_RegAdopt(P, candidate, authorityKind, authoritySignatureEdition, localKind, localSignatureEdition, S_local).**

1. Check P's governed scope and explicit time against `S_local`.
2. Recover the exact authority/local declarations, KindBridge relation, and bridge assertion.
3. Check bridge applicability and route its consequence to R.
4. Evaluate `J(candidate, localKind, localSignatureEdition, S_local)`.
5. Continue only on `true`; retain known `false` or `unknown` before refusing.
6. Check freshness of relied-on regulatory and candidate support separately.

**Guard_RegChange(change, impactedDeclarations, impactedScopes).**

1. Decide whether the change alters criterion, reference scheme, applicability, or more than one.
2. Author the required signature episteme edition and let C.3.1 settle kind continuity.
3. Update Scope independently when jurisdiction/version/time coverage changes.
4. Reassess the bridge assertion's mapping, loss, `CL^k`, evidence, and admitted use.
5. Evaluate affected exact candidates for the new receiving use under the new declaration edition while preserving every prior judgment indexed to its prior edition and slice; do not edit a set representation or rewrite historical judgments as a substitute.

**Guard_RegXContextUse(P, candidate, sourceKind, targetKind, targetSignatureEdition, S_target).** Apply `Guard_XContext_Typed` and then the exact target candidate judgment. A missing target dependency yields `unknown`; it is not cured by a high bridge assessment.

##### C.3.A:A.4 Worked examples [I]

**Adult dosage across jurisdictions.** Authority kind `AdultPerson@RegY` uses threshold 18; hospital kind `AdultPatient` uses 21. The obtaining KindBridge and its assertion state the boundary loss and `CL^k=1`. For patient P-44, the hospital evaluates its target signature edition in the dated formulary slice. Missing DOB support gives `unknown`; the guard refuses without asserting that P-44 is a non-adult.

**GDPR and CCPA.** Two source kinds relate to independently identified product-context kinds through separate bridges/assertions. Each policy has its own jurisdiction/time Scope. A data item is governed by a fresh target judgment; an alias table is support, not classification.

**Export control.** The shipping policy pins the target product signature edition, shipment candidate, destination/end-use slice, and date. Category correspondence and Scope translation have separate bridges. The exact product judgment and the shipping guard disposition remain separate; higher residual risk may require manual review.

**IFRS and US GAAP Lease.** Each authority kind and local corporate kind remains independently identified. The bridge assertion records the short-term-exception loss. Test planning targets boundary candidates under pinned target declarations rather than treating one shared label as truth.

##### C.3.A:A.5 Guidance and migration [I]

1. Inventory regulatory claims, exact category declarations, and applicability slices.
2. Recover or author target `KindSignature` declaration editions; keep F on those epistemes.
3. Establish KindBridge relations and separate assertions with loss and admitted use.
4. Rewrite candidate-bearing guards to pin candidate, local kind, signature edition, and slice.
5. Preserve `unknown` and record refusal separately.
6. Route Scope through USM and bridge consequences through R.
7. Use RoleMask declarations for local procedural tailoring; separately establish a new kind/order relation only when the distinction truly becomes conceptual and stable.

##### C.3.A:A.6 Manager's compact pattern [I]

- **Where and when?** Claim scope over exact context slices.
- **About what?** Exact local kind and signature declaration; KindBridge relation/assertion if foreign.
- **Which exact thing?** Fresh target `J(candidate, kind, signatureEdition, slice)`.
- **Can we act?** A separate guard disposition after scope, judgment, bridge, freshness, and policy checks.

#### C.3.A:Annex B - Assurance lanes and evidence design [A/I]

##### C.3.A:B.1 What typed assurance adds [I]

VA can prove a claim quantified over an exact declared kind; LA can exercise exact candidates and boundary cases under pinned editions and slices; TA can qualify the tools used to produce support. None of those lanes turns evidence existence into classification truth.

##### C.3.A:B.2 Normative obligations

**EA-1 (Declaration and candidate binding).** Every VA/LA artifact SHALL cite the governed claim, exact quantified kind and signature edition, and assumed Scope. Candidate-specific evidence SHALL additionally name each exact candidate and its four-input judgment.

**EA-2 (Subkind coverage).** A claim over kind `k` SHALL justify coverage over relevant obtaining subkind relations and paired signature editions. RoleMask rows may cover named procedural uses but SHALL NOT silently stand in for a stable subkind.

**EA-3 (Three values in evidence use).** A test, observation, or proof may support a classification assertion. An unavailable evidence dependency yields `unknown`; failed evidence retrieval MUST NOT be recorded as candidate `false`.

**EA-4 (Independent unions).** SpanUnion SHALL include a support-line independence account and preserve per-line candidate judgments and bridge consequences.

**EA-5 (Bridges).** Cross-context evidence use SHALL recover Scope Bridge separately from KindBridge relation/assertion, use the independently authored target declaration, and evaluate target candidates afresh. Consequences affect R only.

**EA-6 (Freshness).** Evidence windows and tool/declaration editions SHALL be explicit and tied to the governed slice. Expiry causes refusal or `unknown` at the predicate it disables; it does not widen Scope.

**EA-7 (TA separation).** Tool qualification SHALL remain distinct from content proof, candidate facts, classification judgment, and receiving disposition.

**EA-8 (No scope-by-wording).** More general wording, more matching candidates, or additional evidence-matrix rows SHALL NOT widen G. A `ΔG+` change requires the new support or sufficiently congruent bridge basis required by A.2.6; otherwise retain or narrow the declared Scope.

##### C.3.A:B.3 Evidence matrix [I]

| Rows | Columns | Cell content |
| --- | --- | --- |
| exact kind/subkind signature editions or RoleMask declaration editions | exact context slices with versions and `Gamma_time` | exact candidate(s) when current, judgment values, evidence units and support relations, freshness, bridge/assertion references, and receiving use |

Rows plan declared distinctions; they do not classify every candidate. A proof-only row may remain declaration-level when it genuinely proves a universal claim. A test or monitoring row becomes candidate-bearing and records exact judgments for the exercised candidates.

##### C.3.A:B.4 VA lane [A/I]

- **VA-1.** A proof carrier SHALL cite the exact claim, quantified kind, `KindSignature` edition, and assumed scope slices.
- **VA-2.** A proof of a universal claim need not invent a candidate; application to an actual candidate uses `Guard_CandidateUse` separately.
- **VA-3.** Cross-context proof reliance SHALL recover both bridge channels, the target declaration, loss, and R consequences.
- **VA-4.** Tool-kernel qualification belongs to TA and does not raise the declaration's F or candidate truth.

Example: a proof over `PassengerCarSignature@v4` assumes a dry-road slice. Reuse at Plant-B requires bridge/scope settlement. Application to VIN-17 then uses the Plant-B target signature and exact target judgment.

##### C.3.A:B.5 LA lane [A/I]

- **LA-1.** Each test or monitoring campaign SHALL state row declaration editions, slice columns, exact tested candidates, and their judgments.
- **LA-2.** Boundary probing SHALL distinguish criterion boundaries from Scope boundaries.
- **LA-3.** A KindBridge assertion that records collapsed distinctions SHALL lead to explicit coverage repair; it does not alter target truth.
- **LA-4.** Freshness and SpanUnion independence SHALL remain explicit.

Example: rows `PassengerCar` and `LightTruck` use pinned signature editions; columns cover dry/wet slices. The tested VINs are exact candidates. A missing sensor dependency for one VIN yields `unknown`, not a negative vehicle classification.

##### C.3.A:B.6 TA lane [A/I]

Qualify provers, checkers, measurement pipelines, and classifiers separately. A classifier output can support an assertion about `J`; the tool neither becomes the candidate nor makes the governed criterion hold. Version drift may make the support unavailable and hence produce `unknown` for a candidate-bearing use.

- **TA-1.** Every tool whose qualification is relied on by VA or LA SHALL identify its exact version and qualification status, and the receiving guard SHALL recover that declaration when the reliance is current.
- **TA-2.** Missing or weaker tool qualification MUST NOT be hidden by lowering the owning episteme's F or widening G. The receiving policy may require additional independent support, reduce or condition R, or refuse the use while preserving the exact unavailable-support reason.

##### C.3.A:B.7 Evidence guards

**Guard_EvidencePlan_Typed** SHALL check exact row declaration editions, exact slice columns, bridge/assertion needs, candidate-selection policy, freshness, independence, and TA declarations. Planning rows do not count as candidate judgments.

**Guard_EvidenceAttach_Typed** SHALL bind every evidence unit to its exact claim/use, row declaration, slice, exact candidate when current, judgment value, support relation, freshness, and bridge consequences. It SHALL preserve `unknown` and the separate attach/refuse disposition.

##### C.3.A:B.8 Anti-patterns and remedies

| Anti-pattern | Remedy |
| --- | --- |
| one golden case stands for a kind | state the declaration-level claim and plan explicit subkind/boundary coverage |
| a matrix row is treated as classification | name exact candidates and judgments in candidate-bearing cells |
| “latest data” | pin freshness and time policy |
| trusted tool substitutes for content support | keep TA separate and recover the governed candidate facts/support |
| bridge presence substitutes for target evaluation | use the independent target declaration and fresh target judgment |

##### C.3.A:B.9 End-to-end example [I]

A two-plant braking claim pins the `PassengerCar` declaration and Plant-A scope. VA proves the quantified claim over that declaration. LA tests exact VINs in dry/wet slices and records their judgments. TA identifies tool versions. Plant-B reuse recovers both bridges, the target declaration, loss and R consequences; each Plant-B candidate is evaluated afresh before evidence is attached.

#### C.3.A:Annex C - ESG and Method–Work guards

##### C.3.A:C.1 ESG obligations (normative)

When a state transition publishes or relies on a claim quantified over kinds, the ESG guard SHALL:

1. pin the claim, exact quantified claim kind, receiving kind, and both needed `KindSignature` editions;
2. establish the correct same-context restriction direction or the exact source-claim to target-receiving KindBridge relation and separate assertion;
3. check Claim scope and explicit `Gamma_time`;
4. when one or more actual candidates are part of the transition, evaluate each exact four-input target receiving-kind judgment and preserve all three values;
5. when a RoleMask is used, recover its declaration edition and evaluate the exact masked judgment;
6. apply justified bridge consequences to R only;
7. check formality and freshness on their actual owners; and
8. return a separate state-transition disposition.

ESG MUST NOT widen G to hide incompatibility, treat a label as a candidate judgment, or convert `unknown` to `false`.

##### C.3.A:C.2 Method–Work obligations (normative)

This Method–Work slice is conditional; it is not a definition that makes every actual change agentic, capability-held, planned, method-mediated, or Work. Open its capability/method/WorkPlan entry checks only when those objects and an A.15.1 Work use are current. A natural, spontaneous, formal, jointly caused, or non-separable `U.Transformation` remains under A.3/A.3.4 and does not acquire a fictive performer, role assignment, method, capability, plan, or Work to satisfy this guard. A broader scale-free-agency or Work decision remains with A.13, C.9, and A.15.1; this annex neither settles nor forbids it. Reflexive cases require separately grounded acting and affected positions, while joint or non-separable cases keep their direct dynamics, interaction, or causality governors rather than forcing one arbitrary actor-target split.

When the Method–Work use is current, it has two different boundaries.

**Prospective entry.** Before execution, a guard may decide that a holder capability, method, intended `U.WorkPlan`, JobSlice, and candidate inputs are sufficient to start. That decision SHALL NOT claim that Work already occurred. The capability instance, capability statements or currentness assessments, fit predicates, WorkPlan, JobSlice, and entry record remain distinct.

**Actual result or acceptance.** When performed Work is current, the guard SHALL identify exact `W : U.Work` as an independently grounded, world-side, dated 4D Work occurrence under A.15.1. `W` is not the `U.Work` kind, JobSlice, capability, plan item, log, card, row, or assertion. Any plan, log, result record, or assurance record about W is a separate episteme that designates W.

A conforming Method–Work check SHALL:

1. require the capability's governed Work scope to cover exact JobSlice with explicit time;
2. check capability measures, qualification/currentness, and fit as separately governed predicates;
3. pin every expected input/output local kind and signature edition;
4. for every actual input candidate, evaluate `J(inputCandidate, expectedInputKind, inputSignatureEdition, JobSlice)` and preserve all three values;
5. use exact RoleMask declarations and masked judgments when procedural tailoring is current;
6. establish exact target bridges/declarations and fresh target judgments for cross-context candidates;
7. before execution, return only an entry disposition and keep W absent;
8. after execution, identify W independently and, for every actual output candidate relied on, evaluate the exact output judgment;
9. keep W, inputs, outputs, JobSlice, capability, plan, logs, and assertions distinct; and
10. refuse fail-closed on `false` or `unknown` without rewriting either value.

##### C.3.A:C.3 Ready-to-use skeletons

**ESG_TypedGate(Claim, claimKind, claimSignatureEdition, receiveKind, receiveSignatureEdition, TargetSlice, candidates?).** Apply `Guard_TypedClaim` to the exact claim and receiving kinds; for each actual candidate apply `Guard_CandidateUse` with both declaration editions; apply bridge, freshness, and policy predicates; return the separate transition disposition.

**MethodWork_EntryGate(Capability, WorkPlanRef, JobSlice, inputCandidates, inputDeclarations).** Check Work scope, capability/qualification/fit predicates, exact input judgments, masks, bridges, and freshness. Return “entry allowed/refused”. Do not create or identify W.

**MethodWork_ResultGate(W, JobSlice, actualInputs, actualOutputs, declarations, ResultRecordRef?).** First recover the independently grounded dated W under A.15.1. Then evaluate exact input/output candidate judgments, check scope and any acceptance predicates, and keep any ResultRecordRef as a separate episteme designating W.

##### C.3.A:C.4 Worked examples [I]

**ESG braking policy.** The claim pins `VehicleSignature@v4` and the dry/wet TargetSlice. The consumer is restricted to `PassengerCar`, and `SubkindOfObtains(PassengerCar, Vehicle; plantVehicleScheme)` holds under the paired exact declaration editions. For VIN-17, evaluate `J(VIN-17, PassengerCar, passengerCarEdition, TargetSlice)=true`; C.3.1 monotonicity then supplies the Vehicle-side classification needed by the universal claim. An unavailable brake-configuration dependency would yield `unknown`, and the transition would refuse separately.

**Risk-score Work entry and occurrence.** `ComputeRiskScore` capability is considered for request `req-884` in JobSlice `api-v2.3/eu-west/t-204`. The entry guard evaluates the request under the pinned `AuthenticatedRequest` signature. If true, it may admit execution; no Work occurrence yet follows. After execution, actual `W = RiskScoreRun-2026-07-22T10:03Z-884 : U.Work` is independently grounded as the dated world-side occurrence. `RiskScoreRunLog-884` is a separate episteme designating W. The output score value is a separate candidate evaluated under its declared output kind and signature edition.

**Cross-context plant use.** The source claim and source kind cross via separate Scope and KindBridge channels. Plant-B recovers its own target declaration and evaluates exact TransportUnit candidate TU-9. Bridge assertions affect R; they do not classify TU-9 or create the later Work occurrence.

##### C.3.A:C.5 Anti-patterns and remedies

| Anti-pattern | Remedy |
| --- | --- |
| widening Work scope to hide an input mismatch | repair declaration compatibility, adapter, mask, or bridge; otherwise refuse |
| calling JobSlice or WorkPlan the work | before execution keep W absent; after execution identify the independently grounded dated W |
| treating a log or result row as W | keep it as a separate episteme that designates W |
| omitting the exact candidate or signature edition | pin all four judgment inputs |
| converting unavailable support to `false` | retain `unknown` and refuse separately |
| treating bridge or adapter records as target truth | recover target declarations and evaluate candidates afresh |

