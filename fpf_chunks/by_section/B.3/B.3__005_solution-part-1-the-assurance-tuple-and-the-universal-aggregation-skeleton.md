---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:4"
section_title: "Solution — Part 1: The assurance tuple and the universal aggregation skeleton"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__005_solution-part-1-the-assurance-tuple-and-the-universal-aggregation-skeleton.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:4 — Solution — Part 1: The assurance tuple and the universal aggregation skeleton"
line_start: 38751
line_end: 39106
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.4"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "C.29"
  - "D.4"
  - "E.14"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

### B.3:4 - Solution — **Part 1: The assurance tuple and the universal aggregation skeleton**

B.3 defines **what** the assurance components are, **where** they are assigned on nodes and edges of the dependency graph, and the **shape** of the aggregation that any Γ-flavour must honor when producing an *assurance result*.

#### B.3:4.1 - The F-G-R assurance components (typed; `F` and `R` as CHR, `G` as USM)

We standardize **two claim-facing characteristics**, **one claim-scope value**, and **one integration-relation characteristic**. Every value still names its exact bearer, scheme, scope, window, and basis under B.3:4.2-4.3:

1. **Formality (F)** — *how constrained the reasoning is by explicit, proof-grade structure.*

   * **Scale kind:** **ordinal** (its scale values do not admit arithmetic).
   * **Canonical scale values (example):**
     `F0 Informal prose` - `F1 Structured narrative` - `F2 Formalizable schema` - `F3 Proof-grade formalism`.
   * **Monotone direction:** higher is better (never lowers assurance when all else fixed).

2. **ClaimScope (G)** — *the declared set of `U.ContextSlice` values where the result applies.*

   * **Type:** **set-valued USM scope value** (A.2.6), **not** a CHR characteristic.
   * **Well-typed operations:** **membership** and **set algebra** (`∈`, `⊆`, `∩`, `⋃`, `SpanUnion`, plus declared Bridge translation, widening, narrowing, or refit operation).
   * **Scalar proxy (report-only):** if a G scope report needs a number, it may publish an explicitly declared **CoverageMetric(G)**; such a proxy must not replace G in norms, gates, bridge semantics, or CL-bearing relation decisions.

3. **Reliability (R)** — *how likely the claim or behavior holds under stated conditions.*

   * **Scale kind:** **ratio** in `[0,1]` (or a conservative ordinal proxy when numeric modeling is unavailable).
   * **Monotone direction:** higher is better.

4. **Congruence Level (CL)** — *characteristic of one exact integration, mapping, calibration, interface, or other admitted relation occurrence: how well its participants fit for the named assurance use.*

   * **Scale kind:** **ordinal** with a **monotone penalty function** `Φ(CL)` where `Φ` decreases as CL increases.
   * **Canonical scale values (example):**
     `CL0 tentative guess` - `CL1 plausible mapping` - `CL2 validated mapping` - `CL3 verified equivalence`.
   * **Interpretation:** low CL reduces the credibility of the *integration itself* (not the parts), and therefore **penalizes** the aggregate **R**.

> **EntityOfConcern and description strict distinction (A.7).**
>
> * Assurance components are recorded as **value and scope claim components**: `F` and `R` as characteristics, `G` as a scope value, while the governing composition, order, temporal, and work patterns keep **structure, order, and time** distinct.
> * Do not smuggle assurance components into structural edges; keep `F`, `R`, and `CL` explicit as CHR metadata and `G` explicit as a USM scope value.

> **Assurance shoulders (Working-Model split).**
> **Mapping** raises **TA** (typing, fit, and CL). **Logical** and **Constructive** contribute to **VA** (intended relation semantics; constructive-composition identity when its governor admits it). **Empirical Validation** contributes to **LA** through exact input-result and evidence-use relations under the named ReferenceScheme, ClaimScope, conditions, and window. These inputs may be cited from an E.14 Working-Model assertion layer, but B.3 does not make the layer, face, or record an assurance result.

#### B.3:4.2 - Assurance as a typed result claim

Begin with one exact C.2.1 target-claim episteme `E_C`: its ClaimGraph states the claim being assured, its EntityOfConcern identifies what that claim concerns, and its effective ReferenceScheme interprets the claim. Any measurement, causal, conformance, status, capability, safety, or other subject result asserted by that ClaimGraph remains with its direct governor. B.3 neither makes that result obtain nor changes claim truth.

For one named assurance use `U_A`, B.3 may constitute a separate assurance-result episteme whose ClaimGraph contains:

```text
AssuranceResult(E_C, U_A | RS_A, G_A, T_A)
  = <F_eff, G_eff, R_eff, CL_basis, disposition, limitations>
```

* `E_C` is the exact target-claim episteme, not a carrier, status tile, evidence item, result record, or bare holon label.
* `U_A` is the exact readiness, compliance, safety, release-confidence, model-credibility, trust, or other receiving assurance use; it is not proof that later work actually relied on the result.
* `RS_A` is the effective ReferenceScheme interpreting the assurance-result ClaimGraph. The target claim retains its own effective ReferenceScheme.
* `G_A` is the A.2.6-governed claim scope for this assurance result. Assumptions, environment, audience, operating conditions, and local sense constraints are stated by value rather than hidden in a generic context field.
* `T_A` is the declared design/run stance and exact applicability, evidence, or reliance window. Design and run results remain separate.

Keep the following objects distinct whenever they are current:

1. the world-side subject facts and domain-local result under their direct governors;
2. target-claim episteme `E_C` under C.2.1;
3. each exact A.2.4 evidence-use relation classifying an episteme for a target claim, scope, polarity, window, and intended assurance use;
4. the A.10/G.6 source-provenance path and local `RelianceDisposition` for the bounded evidence use;
5. dated assurance-assessment `U.Work`, its performer assignment, enacted method, and exact direct or A.6.1 application bindings;
6. formal, empirical, causal, measurement, conformance, comparison, or other input results and the C.2.1 epistemes that state them;
7. the B.3 assurance-result claim and its distinct C.2.1 episteme;
8. witnesses, calculation traces, an optional assurance record episteme, publication occurrence, form, rendering, and carrier; and
9. any later premise/use relation, reliance decision, F.10 status use, A.21 gate decision, permission, release decision, or performed action.

None of objects 3-9 makes the target fact true. An evidence change may change input availability, warrant, `F/G/R/CL`, the assurance disposition, or admissible reliance without changing the world-side result or `E_C`. Absence of evidence is therefore not a negative target result. A status value, successful check, record field, publication, or favorable assurance result likewise does not create the target, approve a release, grant permission, or establish actual use.

A minimally replayable assurance-result ClaimGraph designates:

```text
AssuranceResultClaim:
  TargetClaimEpistemeRef: E_C
  AssuranceUse: U_A
  EffectiveReferenceScheme: RS_A
  ClaimScope: G_A
  TimeStanceAndWindow: T_A
  AssumptionAndConditionRefs:
  F_eff:
  G_eff:
  R_eff:
  CongruenceOccurrenceRefs:
  AggregationRuleRef:
  InputResultClaimRefs:
  EvidenceUseRelationRefs:
  A10OrG6PathRefs:
  AssessmentWorkRef:
  AssessmentMethodAndApplicationRefs:
  WitnessOrCalculationTraceRefs:
  Disposition: pass | bounded | degrade | abstain | evidence-needed | reopen | blocked
  LimitationsAndNotCarried:
  DecayAndReopenCondition:
```

The ClaimGraph is claim content, not a work log or record schema that performs the assessment. `AssessmentWorkRef` and application refs must resolve outward to independently governed occurrences. Witnesses support replay; they are not result claims. An optional assurance record cites the result and its basis; it does not become the result or perform the work.

**Validation modes (preserved input distinction).** When a target claim is published through an E.14 Working-Model assertion, its declared `validationMode ∈ {postulate, inferential, axiomatic}` is one input to assurance reasoning. `postulate` calls for the declared empirical audit basis; `inferential` calls for the exact reasoning basis; `axiomatic` calls for the exact constructive identity and grounding basis under its direct governors. The declaration, `tv:groundedBy` pointer, assessment work, result claim, evidence use, and publication remain different objects.

**Design versus run (no chimeras).** Produce separate assurance-result claims when the target use, assumption set, scope, evidence window, or design/run stance differs. Compare them explicitly; do not compose blueprint formality and runtime evidence into one score.

#### B.3:4.2a - Authority-looking labels and dashboard tiles

A badge, label, score, dashboard tile, credential display, provenance mark, compliance-looking mark, model card, datasheet, data card, assurance document, attestation label, assurance-looking note, or generated confidence phrase does not enter assurance calculus or improve `F`, `G`, `R`, `CL`, readiness, safety, compliance, trust, release confidence, or assurance by display alone.

**Adversarial misuse guard.** Do not let dashboards with favorable labels, compliance-looking badges, old model cards, provenance labels, assurance-looking documents, or generated confidence phrases supply missing evidence, limitations, scope, decay, or argument for an assurance claim.

B.3 dispositions for such a source or publication face are:

| Disposition | Use when | Output |
| --- | --- | --- |
| No assurance use | The encountered source or publication face is only a cue, source pointer, evidence question, currentness question, gate decision, role assertion, status-value assertion, commitment, boundary wording, or work occurrence. | Use `A.15`, `A.10`, `A.6`, `A.21`, `A.20`, `A.2.1`, `A.2.8`, `A.2.9`, or `A.15.1`; no tuple is needed. |
| Compact bounded assurance-result claim | The target use is local, reversible, non-release, non-compliance, non-safety, not reused as assurance input, and does not affect a people or team status value. | Name `E_C`, `U_A`, the exact evidence-use/provenance refs, limit, disposition, and stop or reopen condition; do not turn the work record into the result. |
| Full assurance-result claim | The receiving use raises readiness, compliance, safety, release confidence, trust, explicit `F/G/R/CL`, or reused assurance input. | One typed `AssuranceResult(E_C, U_A &#124; RS_A, G_A, T_A)` claim with assessment basis, argument, evidence-use/provenance refs, limitations, disposition, and decay condition. |
| Rejected or narrowed assurance claim | Evidence, scope, argument, currentness, or limitations do not carry the attempted assurance claim. | State the assurance claim, work claim, or reliance claim that the current assurance tuple does not carry, then name the next legitimate formalization, evidence repair, scope narrowing, or claim narrowing move. |

Build a `B.3` assurance claim only when the next work occurrence or reliance use depends on a typed assurance claim. The typed assurance claim names:

| Field | Required content |
| --- | --- |
| Target claim and assurance use | Exact target-claim episteme `E_C`, its direct subject-result governor, and named `U_A`: readiness, release, audit, compliance, safety, model credibility, or another assurance use. |
| Interpretation, scope, conditions, and time | `RS_A`, `G_A`, `T_A`, exact assumption/condition refs, and the audience or relying role when human-facing. The target holon is reached through `E_C`'s EntityOfConcern, not copied into a generic context tuple. |
| Assessment work and condition | Dated assessment work, performer assignment, enacted method, exact rule/application bindings, and the method, policy, test, audit, or measurement conditions consumed. |
| Input results, evidence use, and provenance | Name the exact domain input-result claims; A.2.4 evidence-use relation refs with target, polarity, scope, window, and intended use; and the minimum A.10/G.6 provenance path. A proof or status result remains a separate domain result; its appearance in an assurance record neither makes it evidence nor raises assurance. Cite the exact defining or testing content only when the assurance argument depends on that interpretation. |
| Argument and assurance rationale | The exact aggregation/argument rule and why the cited input-result and evidence-use relations warrant the assurance-result claim for `E_C` and `U_A` under `RS_A`, `G_A`, and `T_A`, including assumptions, defeaters, and challenges. |
| Limitations and rival explanations | Scope limits, claims or uses not carried by the assurance tuple, stale display, spoofing, copied text, generated text, proxy-for-value substitution, provenance-only source relation, context shift, and known failure conditions. |
| Decay and reopen condition | Valid-until, revocation, policy version, gate version, model version drift, monitoring change, incident signal, evidence refresh, and contest or redress relation. |

For a full threshold-bearing assurance result, retain the dated assessment `U.Work`, capable performer and assignment, enacted Method, and application bindings when their identity bears on replay, competence, conflict, timing, reproducibility, contest, or redress. If evidence was produced by a material analysis or test, keep that evidence-production Work and its result distinct from the assurance-assessment Work and assurance result. A method description, record, witness, publication, or favorable result performs neither work and establishes no later reliance.

**Assurance evidence minimization.** Cite only the A.2.4 evidence-use relations and minimum A.10/G.6 paths needed for `E_C` and `U_A`. Use redacted, hashed, scoped, or role-mediated refs when raw material exposes personal data, secrets, privileged logs, tenant identifiers, security-sensitive traces, incident details, or unnecessary identities; a compact pointer must still preserve enough recoverability to replay the warrant.

Viewpoint prompts for assurance use:

| Role in the situation | Prompt |
| --- | --- |
| Assurance steward | Which exact `E_C`, named `U_A`, and `AssuranceResult(E_C, U_A &#124; RS_A, G_A, T_A)` claim are being assessed or revised? |
| Audit role | Which assessment-work/application refs, input-result claims, evidence-use/provenance refs, witnesses, argument, limitations, decay condition, and reopen condition must be recoverable? |
| Manager or release role | Which desired decision or work or reliance use is outside B.3 and must instead use `A.15`, `A.21`, `A.10`, or another named source? |
| Model or data steward | Which documented bounded-use statement or external intended-use field, evaluation condition, version, window, limitation, drift, and incident condition bound the model or data documentation? |
| Evidence source-maintenance role assignment | What evidence ref or scoped pointer must be exposed without turning documentation presence into an assurance claim? |

Display guidance for assurance labels: a readiness, safety, compliance, trust, release-confidence, or assurance display should expose `E_C`, `U_A`, assessment/result ref, evidence-use/provenance refs, scope, window, limitation, disposition, decay and reopen conditions, and the status, work, gate, permission, decision, or reliance claims not carried. Display is a representation/publication of the result, not the result, assessment, or later use.

Incident-learning fields for assurance overread: visible label, documentation record, attempted assurance claim, missing tuple or evidence-provenance field, assurance claim, work claim, or reliance claim not carried by the assurance tuple, limitation or decay condition that defeated the claim, next legitimate formalization, evidence repair, scope narrowing, or claim narrowing move, and upstream repair record for documentation, evidence refs, assurance label wording, monitoring, or reopen trigger.

Contestability and redress relation: when the B.3 material-reliance threshold is met, the B.3 result should name the claim being contested, evidence-provenance path, limitation or decay condition, contest forum or decision forum, safe interim disposition, and what evidence or scope change would reopen the assurance claim.

If those fields are missing, the encountered publication face, rendering, or cue remains an orientation label, source pointer, evidence pointer, documentation record, or unsubstantiated confidence cue. Use `A.15` when the question is whether that lane may guide work or reliance, `A.10` when the question is evidence, currentness, or provenance, and `A.6` when the question is mixed policy, API, or schema wording.

**Positive repaired assurance statement.** When the named use and required fields are present, state the smallest `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim that can guide the use, with assessment ref, exact input-result and evidence-use/provenance refs, argument, limitations, disposition, decay, and reopen condition. It warrants only `U_A`; any gate, status, permission, performed work, decision, or later reliance remains separately governed.
Constructive assurance moves:

- narrow `G` to the evidenced or rule-bounded scope;
- raise `F` by formalizing argument structure, method-description fields, or `MethodRelationStructure@BoundedContext` when method composition, fallback, selection, or method-family relation is current;
- raise `R` by adding validation, replication, more probative, repeated, current, or more relevant evidence;
- improve `CL` by repairing mappings, units, interfaces, or integration edges;
- separate design assurance from run assurance;
- add limitations, assumptions, defeaters, monitoring, drift, and reopen triggers;
- reject or downgrade the assurance use when those moves are not available.

Negative controls:

| Visible source or publication face | Bounded source or assurance use | Unsupported use without a typed assurance claim |
| --- | --- | --- |
| Source-backed release dashboard tile | If the tile is a current view of `A.21` `GateDecision` or `DecisionLogRef` plus an `A.10` evidence-provenance path, it may carry gate-passage reliance outside B.3 for the named release and environment. B.3 is used only when the tile is also asked to raise readiness, safety, compliance, trust, or release-confidence assurance. | Release approval by display, compliance proof, rollback success, work occurrence, or assurance increase without a typed assurance claim. |
| Credential, compliance, or provenance label | Bounded source, holder, status value, history, or documentation source relation when evidenced. | Safety, truth, permission, gate passage, readiness, or assurance claim by label presence. |
| Model card, datasheet, data card, assurance document, or assurance-looking note | Scoped documentation for a named claim, documented bounded-use statement or external intended-use field, evaluated condition, limitation, version, and window. | Higher `R`, broader `G`, higher `F`, better `CL`, readiness, compliance, safety, or release confidence by document presence. |
| Generated confidence phrase | Source-finding or explanation relation when grounded. | Assurance increase, authority, approval, or evidence by wording alone. |

Model cards, datasheets, data cards, assurance documents, and assurance-looking notes are external documentation records or source records unless they are mapped into existing `FPF` claims and publication faces. They do not add MVPK face kinds and do not bypass `B.3` when the use under repair is an assurance claim.

**Lint trigger.** A model card, datasheet, or data card cited as readiness, safety, compliance, release confidence, or assurance proof requires an exact target-claim episteme, intended-use match, assessment condition, limitations, A.2.4 evidence-use refs, an A.10/G.6 path, and one typed `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim. Otherwise return `no assurance use`, a rejected result, or a narrower bounded result.

Positive repaired example: a model card may expose an exact model-claim episteme, intended-use statement, evaluated condition, version, window, limitations, evidence-use refs, A.10/G.6 path, and a separately constituted `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)`. That result may warrant only the named evaluated model use; the card still does not create another deployment claim, gate passage, release work, status, or compliance result.

#### B.3:4.2b - Minimum reliance safety assurance record

Use this B.3 section when the B.3 material-reliance threshold is met: reliance on a visible carrier, source reference, publication face, or display may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people or team status value, operational action, or controlled-entity regulation. The first B.3 move is to decide whether an assurance claim is being made; if it is, write the minimum reliance safety assurance record for the named reliance use. Mere attention shift, learning, orientation, source-finding, or source-wording correction is not enough.

`RelianceSafetyCase` is the local Tech label for this B.3 assurance-record form. The plain phrase is **minimum reliance safety assurance record**. The label is not a new FPF pattern, Core kind, safety authority, gate, policy source, approval, certificate, compliance method, or general safety-case ontology.

Assurance-record use: the trigger/non-trigger table is a recognition aid, the minimum-record table is a local form aid, and the worked slices are examples. They are not a universal checklist, sign-off sequence, status vocabulary, assessment work, or replacement for `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)`. The record cites the assurance-result claim and its independently governed basis; filling it makes no relation obtain.

Affordability card: orientation or source-finding stays outside B.3; bounded local reliance stays with the local evidence, explanation, CV, gate, or pattern-quality relation unless an assurance claim is being made; threshold reliance uses the minimum reliance safety assurance record only when the B.3 material-reliance threshold is met. Plain wording remains ordinary unless it changes a bounded use, source relation, evidence use, gate, assurance claim, work, or decision. Stop after naming the concrete use or relation that changed; no selected pattern locator is required.

Common wrong first classification: a safety-looking note, safety case, compliance-looking label, or dashboard warning is a certificate, approval, or gate. First honest entry: state one typed B.3 assurance claim with A.10 evidence-provenance path, assumptions, limitations, defeaters, residual uncertainty, monitoring or stop condition, contest and redress relation, bounded assurance use, and unsupported attempted use.

First B.3 move: name the reliance use, the assurance claim, the affected context or audience, the trigger that meets the B.3 material-reliance threshold, the A.10 evidence-provenance path, the argument, limitations, defeaters, contest and redress relation, stop or monitoring condition, bounded assurance use, and unsupported attempted use. If those pieces are absent, use `A.10`, `E.17.EFP`, `A.20`, `A.21`, `E.19`, or the local relation that actually governs the source use rather than inventing assurance by label.

Trigger and non-trigger cases:

| Encountered source use | B.3 disposition | Minimum response |
| --- | --- | --- |
| Ordinary source-backed report, citation, model card, datasheet, data card, or documentation record with no assurance use and no met B.3 material-reliance threshold | No B.3 assurance use. | Stay in `A.10` with claim, source record or publication face, evidence-provenance path, window, bounded evidence use, unsupported attempted use, and reopen trigger. |
| Generated explanation, generated summary, or didactic reconstruction used only for source-finding or learning | No B.3 assurance use. | Stay in `E.17.EFP` unless operative claims are relied on through `A.10` evidence-provenance paths or another source relation that carries or exposes the source basis for the operative claim. |
| Local conformance label, `CV.Status`, benchmark result, or score near a release conversation but not used to raise assurance | No B.3 assurance use. | Keep `CV.Status` in `A.20`, gate-decision publication in `A.21`, pattern-quality result in `E.19`, measurement or marker relation in `C.16` or `A.10`, and no assurance tuple unless an assurance claim is being made. |
| Confidence, calibration, prediction interval, or abstention reason tied to one reversible local act | Compact bounded assurance claim only when the act depends on assurance; otherwise no B.3 use. | State act, context, window, calibration condition, stop condition, bounded evidence use, and unsupported attempted use; use `C.27` or `G.11` when time, expiry, refresh, or monitoring changes the action. |
| Safety-looking note, compliance-looking label, public warning, dashboard value, generated operational explanation, or status-value display is intended or reasonably foreseeable to meet the B.3 material-reliance threshold: reliance materially changes behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people or team status value, operational action, or controlled-entity regulation. | Minimum reliance safety assurance record is required. | Build the B.3 assurance record with A.10 evidence-provenance path and any relevant `A.20`, `A.21`, `E.19`, `C.27`, `G.11`, `B.2.5`, or representation and retargeting dependency. |

Minimum assurance record:

| Field | Required content |
| --- | --- |
| Reliance use and assurance claim | The behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people or team status value, operational action, or controlled-entity regulation that would materially change, and the assurance claim being made about that change. |
| Scope, conditions, audience, and affected systems | Exact ReferenceScheme and ClaimScope, environment and condition refs, time window, user group or public audience, relying and affected Systems, any exact local system-role kinds and separately obtaining assignments required by the use, tenant, release line, service, and receiving Work or use relation. Assignment does not establish authority or responsibility. |
| Source relation or carrier record and evidence kind | The visible carrier, source reference, publication face, record, cue, marker, conformance label, dashboard, explanation rendering, score, warning, or status-value display, plus the evidence kind being used. |
| A.10 evidence-provenance path | Claim, source record or source relation, producer or Method trace, currentness and window, and admitted source-maintenance System. When maintenance is admitted Work, A.15.1 identifies it and F.6 identifies the assignment under which each performer acted; include an assignment identifier only when the assurance claim uses it. Also state the direct source-maintenance responsibility relation or exact missing governor, evidence relation, rival explanation, bounded evidence use, unsupported attempted use, and reopen trigger. |
| Argument and assurance relation | Why this evidence-provenance path carries the assurance claim under the context; include assumptions, limitations, defeaters, residual uncertainty, and unacceptable-harm or risk-tolerance condition when relevant. |
| Dependencies | Any relevant `A.20` CV status, `A.21` gate decision, `E.19` pattern-quality result, `C.27` temporal claim, `G.11` refresh and decay relation, `B.2.5` control relation, or representation and retargeting relation. |
| Monitoring, rollback, or stop condition | What observation, incident, drift, contest, expiry, changed C.28 identification or realizability profile, changed A.21 gate profile, changed evaluation condition, changed source record, or failed check stops, narrows, reopens, or withdraws the reliance. |
| Contest and redress | The disputed claim or disposition, affected use or harm, admitted review System, any exact review-system-role kind or assignment needed by the work context, direct review-responsibility relation or exact missing governor, challenge evidence admitted by the contest relation, possible disposition change, outcome record, and reopen trigger. |
| Public and protected evidence boundary | Public summary, protected evidence reserved for the admitted review System under its access relation, affected-party contestable minimum, and any scoped, redacted, hashed, or mediated evidence ref needed to preserve recoverability without overexposure. A system-role kind or assignment does not supply access or authority. |

Positive repaired assurance result: when the threshold is met and the record is sufficient, constitute the smallest assurance-result claim for `E_C` and `U_A`, with exact scope/conditions/window, assessment-work ref, input-result and evidence-use/provenance refs, argument, limitations, dependencies, monitoring or stop condition, contest/redress relation, disposition, and unsupported use. The record then cites that result. If insufficient, narrow, degrade, abstain, request evidence, reopen, or block; polished documentation is not safety acceptance.

A safety case is accepted only as a bounded assurance argument for the named reliance use. It remains contestable by defeaters, changed evidence, changed context, monitoring failure, residual-uncertainty breach, or affected-party challenge admitted by the contest relation. Stop when the named reliance use, unsupported attempted use, limitations, defeaters, contest and redress relation, monitoring or rollback condition, and reopen condition are sufficient for this threshold trigger; do not expand the record into a general safety dossier.

A review label, system-role kind, or assignment is insufficient by itself. Review responsibility counts here only through an admitted direct domain predicate whose actual System and applicability are explicit; if none is current, record the exact missing governor. The contest relation must still be able to change the disposition, record the outcome, and leave the bounded assurance use, unsupported attempted use, and reopen condition inspectable.

Misuse guard: an incoming or attempted-reliance `RelianceDisposition=safety-case-required` must name the trigger that meets the B.3 material-reliance threshold. A source producer, dashboard-value publisher or maintainer, model producer, documentation producer, or status-value label issuer cannot self-clear a threshold-bearing reliance by attaching the label. Where the threshold is met, the assurance record must expose an admitted review System, a separately obtaining assignment only when the work context needs it, a direct review-responsibility relation or exact missing governor, and a contest relation capable of changing the disposition.

Affected-party contestable minimum: public and protected evidence separation is sufficient only if the affected party can see enough of the claim, source class, disposition, affected use, admitted review System, direct review-responsibility relation, and challenge evidence admitted by the contest relation to challenge the result. Protected evidence may stay protected under a separate access relation, but protection cannot make redress non-contestable while the assurance use still claims contest or assurance. A blocked, abstained, degraded, or evidence-needed assurance use is not final if admitted challenge evidence, missing affected-party evidence, changed source, changed context, monitoring failure, or redress can materially change the disposition.

Worked reliance-threshold slices:

| Slice | B.3 move | Boundary |
| --- | --- | --- |
| A public-service or access status-value display changes who receives access, assistance, or review. | Use the minimum reliance safety assurance record for the named status-value-changing reliance, with contest and redress and unsupported attempted use. | The display is not approval, safety, fairness, compliance, or resource authority by itself. |
| An SRE dashboard changes incident behavior or resource allocation. | Use B.3 only when the dashboard is asked to raise assurance or safety-bearing reliance; keep ordinary evidence and currentness in A.10. | Use B.2.5 only for a control relation being claimed and A.21 only for a gate decision being claimed. |
| A public warning or synthetic-content label changes perceived meaning but there is no evidence that it changed the behavior claimed to change, release risk, safety claim, or control relation. | Keep the label as A.10 evidence or source-finding and orientation cue; require audience-effect or behavior-effect evidence before B.3 reliance. | Do not infer safety, compliance, behavior change, or control effect from label presence alone. |
| A manufacturing conformance label appears near release. | Keep local CV or conformance evidence in `A.20`, `A.21`, `C.16`, or `A.10`; use B.3 only when assurance, safety, compliance, or release-confidence reliance is being claimed. | Conformance presence is not safety acceptance or release permission. |
| A software supply-chain attestation is cited as runtime safety. | Use `A.10` for origin, build, and process claims and B.3 only for the named assurance claim with argument, limitations, defeaters, and stop condition. | Build provenance is not runtime safety or operational permission. |
| A people or team status-value badge changes permissions, resources, or review priority. | Require an assurance record that names affected and relying Systems, any exact system-role kind or assignment needed by the context, the evidence-provenance path, direct review-responsibility relation or exact missing governor, contest relation, and disposition-change condition. | The badge issuer cannot self-clear the status-value-changing reliance by issuing the badge, and assignment does not establish authority or responsibility. |
| A standards-document clause is reused as approval. | Use `A.10` for evidence of the clause; use the named approval, commitment, gate, or assurance relation only when that relation is being claimed by value. | A cited clause is not project approval, gate passage, or assurance by quotation. |

Do not treat the assurance record as a graded scale, standalone status value, universal assurance checklist, release certificate, or new safety-case disposition family. B.3 consumes the assurance record only as typed assurance input for the named claim and reliance use.

#### B.3:4.3 - Where the values are assigned (and where they are not)

* **On exact assurance inputs:** every `F_i`, `G_i`, or `R_i` designates the exact target or input claim to which it applies, its bearer under the current characteristic/scope governor, effective ReferenceScheme, scope, time stance/window, and input-result or evidence-use basis. A node, row, label, source file, or evidence item does not receive a value merely by appearing in a graph.
* **On exact integration relations:** every `CL` value qualifies one independently established integration, mapping, calibration, interface, or other direct relation occurrence. A drawn edge or Bridge description does not create that occurrence.
* **On the assurance result:** the aggregation rule yields `F_eff`, `G_eff`, and `R_eff` in the B.3 assurance-result ClaimGraph for `E_C` and `U_A`. It does not overwrite the input values, the subject result, or the target claim.
* **Not inside Γ:** Γ consumes its own admitted inputs and produces its own composed result or holon under the applicable composition pattern. B.3 only evaluates assurance for the named claim about that result; it does not become the composition operator.
* **Not work, evidence, status, or a state space:** `⟨F,G,R⟩` is neither assessment work, an evidence-use relation, a provenance path, a status value, nor a `U.CharacteristicSpace`. Do not draw trajectories in it; use ESG and the assurance-trace hooks for separately identified changes in assurance-result claims.

#### B.3:4.4 - Universal aggregation skeleton (domain‑neutral)

When a B.3 assessment consumes results organized by a Γ-flavour, its assurance-result claim **must** adopt the following conservative skeleton; the Γ record itself neither emits nor performs assurance:

1. **Formality:**

   ```
   F_eff = min_i F_i
   ```

   *Rationale:* the least formal piece caps the formality of the whole (WLNK on F).
   *Monotone:* raising any `F_i` cannot reduce `F_eff`.

2. **ClaimScope (G):**

   ```
   G_eff(path)  = intersection({G_i | i is essential on the dependency path})
   G_eff(claim) = SpanUnion({G_eff(path_j)}) only across independently evidenced paths
   ```

   * Along an essential dependency path, every required evidence relation must hold on the same slice, so the effective claim scope is the intersection of the required scopes. Empty intersection means the path does not evidence the claim on any slice.
   * Across independent evidence lines for the same claim, B.3 may publish a `SpanUnion` of the path scopes, but only when the independence assumption and evidence relation are explicit.
   * **Constraint:** any region not covered by the required evidence relation for its path is dropped. A raw union of node scopes is never the default law for `G`.
   * *Monotone:* adding an independently evidenced path may widen the published claim scope; adding a new essential dependency may narrow it.

3. **Reliability (penalized by integration):**

   ```
   R_raw = min_i R_i                       # Weakest-link cap
   R_eff = max(0, R_raw − Φ(CL_min))       # Congruence penalty
   ```

   * `CL_min` is the **lowest** Congruence Level (`CL`) value on any edge in the declared proof path or critical integration subgraph for the claim `C`.
   * `Φ` is **monotone decreasing** and **bounded** (never makes negative values).
   * *Monotone:* increasing any `R_i` or any `CL` cannot lower `R_eff`.

4. **Evidence-source notes:**
   * The aggregation yields values in the assurance-result ClaimGraph. An optional assurance record separately cites all contributing input claims and exact integration relations, their F/G/R/CL values and bearers, assessment-work/application refs, evidence-use/provenance refs, and witnesses. Use A.10 and G.6 for the descriptive paths and G.11 for any currentness result.
   * The record also cites `E_C`'s ClaimGraph, EntityOfConcern, effective ReferenceScheme, and any separately obtaining empirical-grounding relation; it may present separable TA, VA, and LA input breakdowns, decay/valid-until marks, and the Epistemic-Debt tally without making those presentation fields target facts or evidence-use occurrences.
   * If order or time mattered for the claim, attach the OrderSpec or TimeWindow identifiers (B.1.4).

This skeleton is **mandatory**. Domain‑specific patterns may add **refinements** (e.g., separate epistemic “replicability” vs. “calibration”) as long as they **do not violate** WLNK or MONO and preserve scale kinds.

#### B.3:4.5 - System vs. Episteme - same shape, different interpretations

For **systems**:

  * `F` means **engineering discipline** (from ad-hoc method to verified specification).
  * `G` means **operational envelope coverage**.
  * `R` means **assured reliability** for the exact system claim under the named requirements, environment, test basis, scheme, scope, and time window.
  * `CL` covers interface verification or integration verification.

For **epistemes**:

  * `F` means **logical formality or semantic formality** (from prose to proof).
  * `G` means **domain span** (concepts, populations, conditions).
  * `R` means **evidential relation quality** (replication quality, measurement integrity).
  * `CL` covers vocabulary mapping quality and ontology mapping quality.

#### B.3:4.6 - Scale discipline (CHR guard‑rails)

To prevent silent misuse:

* **Ordinal scales (F, CL):** never average or subtract; use only `min`, `max`, thresholds, and monotone comparisons defined for ordinal scale values.
* **Coverage scales (G):** use union and intersection in a declared domain space; do not “average” sets. If a numeric proxy is used (e.g., coverage ratio), it **must** be derived from a set operation, not vice versa.
* **Ratio scales (R):** may be combined with `min`, `max`, or explicitly justified conservative functions; do not combine values across different target claims, effective ReferenceSchemes, scopes, assumption sets, or windows without an exact admitted comparison/translation rule.

#### B.3:4.7 - What improves the tuple (improvement-pattern overview)

B.3 remains neutral about *how* improvement happens, but for didactic clarity:

* **Raise F:** formalize narratives (specifications, machine‑checked models).
* **Raise G:** enlarge evidence-covered span (new test regimes, new populations) with adequate evidence.
* **Raise R:** replicate, calibrate, tighten measurement error, reduce bias.
* **Raise CL:** reconcile vocabularies, align units, formalize mappings, verify interface Standards.

Each improvement may involve an admitted System, one local system-role kind, an assignment occurrence and its declared `U.SystemRoleAssignment` species, a `U.Method` or `U.MethodDescription` change, evidence-producing `U.Work`, and an improvement move. Keep those values separate: the assignment establishes neither Work, capability, authority, nor responsibility. Their run-time counterparts are covered by temporal evidence and work-cost evidence under the relevant temporal and Work patterns.

#### B.3:4.8 - Prohibition (normative) — F–G–R is not a CharacteristicSpace

Do not treat `⟨F,G,R⟩` as a `U.CharacteristicSpace` and do not define geometric **trajectories** over it. Use **ESG** for episteme state and the **assurance‑trace** hooks for trends in assurance tuples.

#### B.3:4.9 - Assurance consequence for unsupported causal-use claims

`B.3` consumes `CausalUseSupportVerdict`, `CausalEvidenceSupportBasis`, and relevant profile refs from `C.28` and `A.10` when an assurance claim depends on a `C.28` causal-use verdict:

```text
CausalUseSupportVerdict = supported | bounded | unsupported | abstain
```

`CausalAssuranceTupleTrigger` is narrower than local causal-use repair. A local `C.28` downgrade, redirection to a relation governing the asserted use, or abstain disposition does not require a new `B.3` assurance tuple by itself. Create or update a `B.3` tuple only when the causal-use claim is assurance-bearing, publication-bearing, release-bearing, or reused as an input to assurance, trust, certification, risk acceptance, or downstream selection. Exploratory causal wording, local causal wording repair, or a `C.28` cheap stop remains outside `B.3` until it changes assurance or publication use.

An unsupported causal-use shift lowers, blocks, or abstains from `R` for the affected causal-use claim. If `CounterfactualSamplingRealizabilityProfile.verdict = nonrealizable`, `B.3` lowers or blocks `R` for claims that require direct counterfactual-comparison sampling evidence. If `CounterfactualSamplingRealizabilityProfile.verdict = unknown`, direct-realization claims are unsupported, while identified, bounded, or simulation-only bounded use may remain available when `C.28` declares the bounded use and unsupported use.

Verdict consequences:

| `CausalUseSupportVerdict` | Assurance consequence | Bounded assurance wording |
| --- | --- | --- |
| `supported` | The causal-use claim contributes to `R` only inside the named `CausalUseSupportStatement`, scope `G`, `CausalEvidenceSupportBasis`, and cited profile refs. | "Supported only for the declared causal use under the cited `CausalEvidenceSupportBasis`, profile refs, and scope." |
| `bounded` | `R` is bounded to the declared bounded-use limit; assurance prose must name the bound, the `CausalUseSupportStatement`, and the `CausalUseUnsupportedStatement`, and must not imply unqualified causal use outside them. | "Bounded causal-use claim for the declared regime, population, policy, model, or window; unsupported outside that bound." |
| `unsupported` | The causal-use claim cannot raise `R`; it becomes `CausalUseUnsupportedStatement`, is downgraded, removed, or blocks the assurance claim when the causal use is necessary. | "Causal use unsupported for this assurance claim; use association-only, metric-only, or simulation-only wording or block the causal assurance claim." |
| `abstain` | No causal-use conclusion contributes to `R`; the assurance tuple either proceeds only on named non-causal grounds or abstains from the affected causal claim. | "No causal-use conclusion is used; assurance proceeds only on named non-causal grounds or abstains from this causal claim." |

What changes in practice: assurance prose cannot say "high confidence that the policy caused improvement" when the evidence-provenance path only evidences association or simulation-only counterfactual output; the unsupported causal-use step must degrade, abstain, or block the causal-use claim.

What this does not authorize: `B.3` does not determine the `C.28` target `CausalityLadderRung`, estimand, causal identification, evidence design, or realizability profile; it applies assurance consequences to the `CausalUseSupportVerdict` supplied by `C.28` and the evidence-provenance path supplied by `A.10`.

