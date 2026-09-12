---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:4"
section_title: "Solution — recover exact objects before drawing the path"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__005_solution-recover-exact-objects-before-drawing-the-path.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:4 — Solution — recover exact objects before drawing the path"
line_start: 22866
line_end: 23112
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.19"
  - "A.2-family"
  - "A.2.4"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.10.ROLE"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "G.11"
  - "G.4"
keywords:
  - "RelianceDisposition"
  - "actual-use relation"
  - "bounded use"
  - "carrier"
  - "claim/result episteme"
  - "currentness"
  - "dated work"
  - "direct relation"
  - "evidence-provenance path"
  - "relied-on claim"
  - "rival explanation"
  - "source publication"
  - "unsupported overread"
---

### A.10:4 - Solution — recover exact objects before drawing the path

#### A.10:4.1 - Start with the relied-on claim

Name the C.2.1 episteme and select the claim or proposition being relied on from its ClaimGraph. Recover that claim's subject, interpretation basis, polarity or status when current, and uncertainty or qualification when relevant. If the claim is used as evidence for another target claim, name that target separately under A.2.4. When the selected claim states a local result, use the pattern that defines or tests that result: C.16 for measurement, C.28 for causal support, A.19 for comparison or selection, G.4 for an acceptance-clause application, A.21 for a gate decision, C.11 for an option-set choice, and the applicable formal, diagnostic, conformance, identity, permission, or commitment pattern. When *role* appears in a technical result, use E.10.ROLE to select the exact local system-role-kind classification, `U.SystemRoleAssignment` occurrence or state, relation among system-role kinds, declaration, participation, interface, or representation claim before citing its governor.

A source episteme may contain several claims. Keep an ordinary source citation ordinary; use C.2.1:4.2.5 `ClaimAddress` only when an exact intrinsic claim reference is needed and resolves uniquely. If that needed address does not resolve uniquely, follow C.2.1's whole-episteme or separately identified claim-episteme alternative.

A carrier, citation, provenance entry, or A.10 classification does not constitute the result episteme or the domain result. When their identity is live, use C.2.1 for the result episteme and the direct subject pattern for the domain result; use A.15.PROD when inception through Work is claimed.

#### A.10:4.2 - Ground source, carrier, publication, and representation

Recover the selected source episteme and its edition and claim content. When availability, form, or carrier matters, separately recover the `EpistemePublicationRelation` occurrence, publication form, carrier, or face involved, together with any copy, extraction, or transformation between source and use. Use E.24.PUB for publication, form, and carrier relations, E.17 for multi-view publication, and C.29 for mathematical representation correspondences. The descriptive graph points outward to those independently established objects and relations.

Carrier authenticity, integrity, or provenance may support only its named origin, history, build, or transformation claim. It does not imply truth, safety, approval, release, permission, assurance, or work occurrence.

#### A.10:4.3 - Separate method, work, participants, and local result

Under A.3.2, an already identified episteme is a `U.MethodDescription` when its `EntityOfConcern` is one admitted `U.Method` and it makes at least one substantive claim about that Method as a way of doing. Generic participants, parameters, effects—including intended effects—and operating conditions can supply such claims; a name, date, or approval alone cannot. A particular work-plan intention, actual-participant binding, or proof/test occurrence remains a separate claim. The description has no actual-participant slots, and its generic method claims do not establish that Work occurred.

Source production, measurement, verification, interpretation, transformation, query, review, publication, or later reliance may be described ordinarily. When the current claim says that one of these is a dated `U.Work` occurrence, first recover each actual performer's A.13 core and independently admit the occurrence through A.15.1 from its performance history, enacted Method, extent, and containing-System relation. Add F.6 afterward only when the evidence account also needs precise assignment-bound attribution. The A.13 core always includes the obtaining assignment. A short account may omit an assignment identifier unused by the receiving claim only when the complete core and all consumed relations remain recoverable; a precise attribution claim additionally requires the F.6 facts. Affected or evaluated referents, resources, and actual participants enter only through direct subject relations or A.6.1 operation-application bindings. Capability, authority, and responsibility remain separate predicates. A compatible signature, plan, description, log schema, or graph node establishes none of those bindings.

For every cited result, name the pattern that defines or tests it and its C.2.1 result episteme separately. The provenance path may represent exact Work, participants, entities, domain results, result epistemes, and outcomes only after their direct relations are established. Relate Work to a returned or produced value only through an exact A.6.1 application binding, one exact local A.15.PROD claim, or a direct subject predicate under its own pattern; otherwise show the two facts separately and return the reason-specific non-assertability result if that connection is needed.

#### A.10:4.4 - Build a descriptive evidence-provenance path

The minimum A.10 path records only what the bounded use needs:

| Field | Required content |
| --- | --- |
| Relied-on claim | The selected claim or proposition in one identified C.2.1 episteme; a separate target claim when the evidence use distinguishes it |
| Bounded use | The ordinary orientation, learning, action, or reliance use being judged, and its premise, reference, decision-use, operation-argument, or other direct use relation. Add an exact later `U.Work` occurrence only when it is independently current. |
| Sources and carriers | Selected source epistemes and editions; publication occurrences, forms, carriers, and faces when material; transformations; and direct provenance/citation relations |
| Work and bindings | Only independently current dated `U.Work`, its complete basis, and the performers, Methods, resources, direct relations, and A.6.1 bindings used by the claim. A claimed Work-to-value link also needs an A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate defined by its own pattern. |
| Result rule | For each asserted local result, the pattern that defines or tests it and its distinct result episteme |
| Time/currentness | Source and result windows plus G.11 currentness when currentness affects use |
| Challenge | A live rival explanation when it needs discrimination; a locally grounded, plausible unsupported use when excluding it changes reliance; an available contest/redress path when a party is affected; and the stop or reopen condition applicable to this use |

Graph nodes retain their admitted kinds. Each edge cites one independently established direct relation; no generic `evidences`, `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or criterion-participant relation is minted as a fallback. A project may label display edges for navigation, but the label has no ontic force.

#### A.10:4.5 - Classify bounded reliance

The canonical local `RelianceDisposition` member set is exactly: `pass`, `degrade`, `abstain`, `reopen`, `evidence-needed`, `assurance-needed`, and `blocked-current-use`. `pass` supports only the exact bounded use; `degrade` supports only the named narrower or reversible use. `assurance-needed` says that A.10 alone cannot support the attempted use because a direct domain rule or receiving decision requires a separately stated assurance claim. It creates no assurance claim and does not open B.3 until that claim is current. No disposition is claim truth, `CV.Status`, gate decision, selector outcome, approval, permission, release, assurance, or Work authorization.

When an actual named assurance claim is current, use B.3 for that assurance question. A.10 continues to supply the exact source and provenance paths but does not issue the assurance result. Consequential evidence use without such a claim stays with the direct safety, access, status, gate, permission, release, responsibility, or controlled-action pattern.

A reliance limitation qualifies the attempted use. When advice must also say what to do next, use `C.11.DUA` to compose a feasible continuation from that limitation. Further inquiry is one possible continuation. Retain the unsupported claim boundary when choosing a narrower use, another action or a stop. Use an already adequate `C.11` choice directly.

#### A.10:4.5a - Route unlike exploratory inputs without changing their kind

When an observation, objective, former cue, novelty characterization, or similarly interesting item is proposed as a premise for an exploratory or creative move, recover the item under its direct owner before applying this bounded reliance classification. Do not rename every item `signal` or `cue`, and do not create a second premise-disposition vocabulary.

| Incoming item | Source/result recovery | A.10 use | Receiving choice |
| --- | --- | --- | --- |
| Evidence-bearing measurement, assessment, experiment, inference, or capability result | The selected claim in an identified C.2.1 episteme and the measurement, capability, experiment, inference, or other pattern that defines or tests its result. | State the relied-on claim, evidence-provenance path, bounded premise use, and existing `RelianceDisposition`; exclude a locally plausible unsupported use when that distinction changes reliance. | When an option or probe comparison is current, `C.11` compares the available alternatives and emits its `ChoiceResult`. |
| Objective, reward, utility term, loss, preference, or heuristic that is not evidence | The exact objective, evaluation, preference, Method, or source-local construction. | Apply A.10 only to a separate evidence or source-reliance claim about that construction or its bounded transfer; the numeric objective is not self-authenticating evidence. | Enter the term as the declared `EvaluativeMeasure`, `PreferenceOrder`, or `ChoiceRule` input that it actually supplies, with assumptions and limits visible. |
| A former pre-articulation cue that has now been articulated | `A.16.1` no longer owns the articulated result. Use `B.4.1`, `B.5.2`, or the direct endpoint claim owner selected by the articulation. | Qualify reliance only when that articulated claim is actually used as a premise. | `C.11` owns any current option/probe comparison; the earlier cue pack neither selects nor evidences the move. |
| A non-evidential `C.17` novelty, surprise, use, or creativity characterization | `C.17` owns the characteristic claim, its scale/basis, and its limitations. | Apply A.10 only when evidence or source reliance for that characteristic claim is current; characterization is not evidence merely by being decision-relevant. | `C.11` may consume the bounded characteristic together with other premises and still choose, reject, probe, or reroute. |

The composition retains the direct source result and an existing `RelianceDisposition` when bounded reliance is current. A later `ChoiceResult` is required only for an actual option/probe comparison under `C.11`. If the source claim is already qualified and the current `C.11` record can use it directly, stop; no intermediate premise record is required.

#### A.10:4.6 - Currentness, actual use, and graph limits

Source availability and source currentness are distinct. Record issue/effective windows, supersession, revocation, source-order rules, and the G.11 currentness result when a use depends on them.

Actual reliance requires one exact premise, reference, decision-use, operation-argument, or other direct relation to the result episteme. When that reliance is also claimed as dated `U.Work`, recover the Work independently. Storage, indexing, citation, graph membership, visibility, or co-location establishes neither reliance nor performed Work.

Part-whole, temporal, production, publication, representation, provenance, participation, and reliance relations must each be established separately. The A.10 graph may cite them together for replay but never substitutes one for another.

#### A.10:4.6a - Authority-reliance use of ordinary A.10 evidence-provenance paths

Use this subsection when an authority-looking carrier is being relied on. The A.10 path represents one named claim, its exact sources and direct relations, and one bounded use; it is not an authority relation. If the Work occurrence, gate decision, speech act, commitment, permission, exact system-role assignment, assignment-state assertion, or other required relation already exists in a project-side source, recover that object by value and let the graph cite it.

Start with A10-lite for source-finding, orientation, learning, and bounded reversible probes. It is sufficient only when these fields supply the evidence required by the claim and its direct rule; reversibility alone does not establish sufficiency:

| Field | Required content |
| --- | --- |
| claim or effect | The claim, effect, or source-backed reliance use the evidence carrier is being asked to evidence for the named work occurrence or reliance use. |
| evidence carrier | The display, badge, credential, attestation, dashboard tile, copied text, generated text, log, trace, source file, report, or other `SymbolCarrier`/publication carrier. |
| producer, issuer, verifier, or source contact | Name the admitted System that issued, attested, copied, generated, verified, displayed, or maintains the source-backed content, and the direct issuer, verification, publication, register, or source-maintenance relation used by this claim. If dated Work is asserted, first recover each precise performer's A.13 core and independently admit the Work under A.15.1. The core includes the obtaining assignment; add an F.6 link through that same assignment only when this evidence path consumes precise assignment-bound attribution. |
| method use or Work occurrence | Name the ordinary source-finding or method use. Add admitted measurement, verification, review, build, attestation, copy, extraction, generation, query, trace, or log `U.Work` only when independently current. If that Work is said to have returned, produced, or first constituted the carrier or result, cite an exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate under its own pattern; otherwise keep the facts separate. |
| time window | Issue time, effective window, decay, supersession, revocation, policy or gate version, and reopen condition, each when the selected source or bounded use depends on it. Name a missing required value rather than inventing one. |

Minimum evidence-provenance path for routine reliance:

| Field | Required content |
| --- | --- |
| evidenced claim or effect | Approval, permission, gate passage, local system-role-kind classification, system-role-assignment occurrence or state, relation among system-role kinds, status currentness, work occurrence, evidence relation, assurance input, or other claim named by value or effect being attempted. Route any other technical *role* use through E.10.ROLE. |
| evidence carrier | The visible or recovered carrier, with enough identity to reopen it. |
| issuer, performer, trust root, status register, and source-side predicates | Name every object this path actually uses: the admitted System performing source-side Work; the trust-root or status-register episteme, register, or service; and the issuer, publication, registration, status-source, source-maintenance, trust, acceptance, or currentness predicate by which that object bears on the relied-on claim. For admitted Work, first recover every precise performer's A.13 core and independently admit the Work under A.15.1. The core includes the obtaining assignment; add an F.6 link through that same assignment only when this path consumes precise assignment-bound attribution. If no current pattern defines or tests the needed predicate, return the A.6.RCD `missing-governor` result. Authority and source-maintenance responsibility remain separate relations. |
| affected entity and relying context | The release, service, model, person, admitted System and any separately obtaining assignment, policy subject, work target, claim, audience, tenant, environment, or other entity for which reliance is attempted. |
| time window and freshness | Retain each issue/effective, decay, supersession, revocation, policy/gate-version, or reopen value that the selected source or bounded use consumes; report a missing required value. |
| relevant Work occurrence or method trace | Any independently current production, verification, query, generation, review, or other `U.Work`, plus the method trace when the method matters. Connect that Work to the carrier or result only through an exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate under its own pattern; otherwise record them separately. |
| evidence relation and rival explanation | Which claim the carrier evidences, how it evidences it, and any live rival explanation that must be distinguished—for example, that the display is stale, the badge spoofed, copied or generated wording changes the claim, or a context shift or limited source relation defeats the use. |

Expanded fields are collected only insofar as they decide the current reliance question. Evidence depth follows consequence severity, reuse, contestability, cross-context movement, and the evidence relation required for the attempted claim. Do not expand a source-finding note into a full evidence dossier, and do not collect every expanded field merely because a carrier is copied, generated, credential-like, provenance-like, or cross-context.

**Adversarial misuse guard.** When a carrier appears to support a claim, name what it appears to establish and any live competing explanation. An apparently current credential may have an authentic carrier but a stale displayed status; a copied approval may be genuine but concern a different scope or window. Test the source, issuer, or currentness predicate and relying context that distinguish that explanation; include source-side Work and precise attribution only when the claim uses them. Authenticity and provenance can contribute to their named claims, but appearance or provenance alone does not establish additional truth, currentness, or authority. If the required predicate has no governor, return that A.6.RCD gap.

**Data-minimization and privacy boundary.** Preserve the minimum source, provenance, and direct-relation account sufficient for the intended use. Use redacted, hashed, scoped, or access-controlled carrier refs when raw material would expose personal identity, access tokens, cryptographic proof payloads, tenant identifiers, security logs, incident details, internal release metadata, audit trails, privileged reviewer identities, sensitive model provenance, or sensitive data provenance. Redaction creates no source relation; it must preserve enough recoverability for the relying context.

| Expanded field | When it is needed |
| --- | --- |
| method trace or work trace | The selected provenance, attestation, generated/copy/dashboard/rollback source relation, or Work claim depends on how the method was applied or the Work occurred. A source relation alone need not assert Work. |
| evidence-carrier integrity | A plausible spoof, stale source, copy, transformation, rendering, redaction, or context shift could change the relied-on claim or its use. Check the integrity property that discriminates that risk. |
| identity or holder binding | The claim depends on a credential holder, admitted System, separately obtaining assignment holder, acting holon, issuer, performer, delegate, revoker, verifier, or relying party. |
| verifier context, relying-party context, and acceptance rule | The evidence relation is accepted only for a verifier, audience, tenant, environment, release line, policy subject, operational mode, or consumer-side policy or gate rule that accepts the evidence for this use. |
| proof, cryptographic-signature, or status verification result | The selected credential, provenance, attestation, authenticity, revocation, or currentness claim requires that verification result under its source specification or verification/use policy. Retain every check required by that regime. |
| policy version, gate version, and decision source | The attempted permission, release, rollback-authority, policy-authorization, or other use depends on that policy or decision. Gate version and gate-decision source are required for a gate-dependent use. |
| source-chain transform notes | Evidence relation passed through extraction, copy, rewrite, representation shift, explanation rendering, summary, export, redaction, or another transform step before reliance. |
| source order and supersession rule | Multiple source candidates disagree or freshness or priority may defeat the visible publication face, publication carrier, rendering, or cue. Include the direct register or status-source-order relation when a register entry is the source for an exact system-role-assignment occurrence, status assertion, permission, commitment, or gate state. |
| minimum disclosure boundary | Raw evidence would expose secrets, personal data, tenant identifiers, privileged logs, tokens, security-sensitive traces, or unnecessary identities. |

Case repairs:

| Case | Evidence repair |
| --- | --- |
| Stale credential badge or status display | Name the exact issuer or trust-root object and its direct issuer or trust relation; name the exact status register, entry, and direct registration or status-source relation when one exists; then show the verifier and relying-party context and the proof, status, freshness, window, entry-version, and integrity facts needed to resolve the stale-source claim. Include holder or subject binding when the claim or regime requires it, validity limits when present or required, and revocation/status checks when the mechanism is present or the selected verification/use policy requires them. Display presence is not an obtaining system-role-assignment occurrence, status assertion, or permission. |
| Verifiable credential, credential view, or register excerpt | Treat it as an `A.10` carrier. Name the exact issuer or trust-root object and relation; the exact status register, entry, and registration or status-source relation when present; the selected source `U.Episteme` and edition and, when availability matters, its exact `EpistemePublicationRelation`; verifier, relying context, acceptance rule, and the proof/currentness facts required by that rule. Include holder or subject binding only when required by the claim or verification regime, validity limits when present or required, and status/revocation checks when that mechanism is present or the selected verification/use policy requires it. Passing the applicable checks may evidence credential currentness for that bounded use; it does not imply a holder-bound claim where none was established. A strong grant, exercise, weak non-prohibition or non-violation finding, or conflict requires `A.2.8.PER`; an actual commitment requires `A.2.8`; an issuing act requires `A.2.9`; an exact system-role assignment requires `A.2.1`; a status assertion requires its direct status pattern; an entry predicate requires its defining pattern and `A.6.B` boundary classification; and gate passage requires `A.21`. Display presence creates none of them. |
| Copied approval or review summary | Show the original `A.2.9 SpeechActRef` or issuing act when approval or authorization is claimed, or the original reviewed source when only review-content currentness is claimed. Add the copy relation, currentness, scope, and window. Add a separately identified dated `U.Work` only when it is current, and connect it to the copy or result only through an A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate defined by its own pattern. State separately whether the claim concerns an `A.2.8.PER` grant, finding, exercise, or conflict result; an `A.2.8` duty, recommendation, or prohibition commitment; or another Work relation. Copy evidence is not approval by itself. |
| Provenance, authenticity, or attestation label | Show the bounded origin, history, build, or process claim; selected source `U.Episteme`, the exact `EpistemePublicationRelation` occurrence when availability is material, or evidence carrier; the method/Work trace, source-specific proof, and carrier-integrity facts that this claim and its verification regime require; the verifier or relying policy that accepts them; and any live rival that changes reliance. Provenance does not show truth, safety, approval, release, gate passage, permission, or assurance unless another FPF relation named by value carries that additional claim or effect. |
| Dashboard status tile | Recover the dashboard query and the source relation or source-bearing record it uses, with the time, window, currentness, source order, freshness policy, and live rival relevant to the claim. For a gate-dependent use, cite the current `A.21` `GateDecisionResult`, directly or through its `DecisionLogRef`, with gate profile, gate version, release target, and work target. For a release claim not dependent on a gate, cite that claim's own rule and decision source; do not invent a gate result. A.10 records this source-to-use account. A status display is not gate passage or Work occurrence by itself. |
| Rollback command-like cue | Show command record or issuing speech act, authorization relation, actor, affected work target or claim target, scope, window, and whether the cue is only an `A.6.A` action invitation. A command cue is not performed-work evidence. |
| Rollback performed-work result | Show `A.15.1` `U.Work` occurrence, method trace or work trace, logs, outcome evidence, and time window. Performed-work evidence is not approval, assurance, or gate passage by itself. |
| Generated explanation | Use `E.17.EFP` to classify the explanation relation and source-finding use. For reliance, show claim-bound attribution alignment: every operative claim relied on maps to a source passage, carrier, or `relationFunctionClaimRef` or `authoritySourceRef` named by value that evidences that claim in the relying context. When that mapping is complete, A.10 may support bounded reliance on those source-backed operative claims; explanation wording alone still does not issue, approve, authorize, pass a gate, evidence performed work, or raise assurance. |
| Model card or datasheet used as evidence | Show documented bounded-use statement or external intended-use field, version, window, evaluation condition, limitations, evidence carriers, and whether a `B.3` assurance claim is being made. Documentation does not become readiness or assurance by presence. |
| Extracted source-to-use path to gate or release claim | Name the selected source `U.Episteme` ref and, when availability is material, the exact `EpistemePublicationRelation` occurrence ref; the source-bearing relation or pattern reference that identifies the rule carrying the claim; the actual transformation chain and any loss or non-commutativity, identifying its first step when present; the FPF relation or pattern that defines or constrains each relevant transform (`A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `E.17.ID.CR`, or `E.18` where applicable); and the bounded inference relation after the transform. A lossless chain retains those actual relations without a fictional lossy step. Also name the `relationFunctionClaimRef` or `authoritySourceRef` named by value that carries the claim being made; the reopen trigger naming the selected source episteme, publication occurrence when relevant, source-bearing relation, transform record, evidence relation, or pattern passage that must be rechecked; and the gate claim or release claim blocked until those source-to-use and cited-claim relations are recoverable. |
| Conflicting source relations | When display, source publication carrier, decision log, recency signal, freshness signal, copied summary, generated summary, credential status, provenance label, or assurance evidence disagree, name the visible source relation, rival source relation, source-order rule, decision-source relation, freshness policy, and supersession rule. Do not choose by color, visual salience, confidence wording, copied wording, or apparent recency; the work claim or reliance claim is contested until the source-order question is resolved. |
| Sensitive evidence-provenance path | Use redacted, hashed, scoped, or access-controlled carrier refs when raw carriers expose secrets, personal data, security-sensitive traces or data, privileged logs, tenant identifiers, or unnecessary identities. Redaction does not create a source relation; it must preserve enough recoverability for the relying context. |
| Pointer or proof-status evidence-provenance path | Use a hash, proof or status verification result, selected source `U.Episteme`, exact `EpistemePublicationRelation` occurrence when availability matters, source or source-currentness relation, scoped pointer, disclosure receipt, or access-controlled view instead of copying raw sensitive carriers or payloads when that pointer preserves enough recoverability for the relied-on claim or effect. Do not copy raw secrets, tokens, privileged logs, personal identities, or tenant details merely to make the path look fuller. |

If the evidence-provenance path is incomplete, A.10 reports the missing source, carrier, work, rule for the cited result, direct relation, or G.11 currentness fact and narrows or blocks only the attempted use. Possible continuations include source-finding only, reopen original carrier, request issuer or status verification, refresh the source query, mark stale or contested, narrow the attempted P2W class or reliance claim, proceed only with a reversible local probe under an explicit work plan, or block the unsupported use.

**Missing source-relation repair assignment.** If the relying actor cannot recover or verify the source relation, first name the missing relation or source-bearing record and the affected use. Source-finding, a request, narrowing, or a stop may be the complete continuation. If the selected continuation allocates or requests repair, recover the recipient and the independently obtaining project-side responsibility, allocation, permission, or commitment relation that the instruction consumes. An assignment to an admitted System must identify that System and its actual assignment basis. Plan or request the future repair under its applicable planning or assignment rule; this is not an assertion that repair Work has occurred. The source-side objects and relations identified above remain separate facts, not responsibility by source label or form. Return an exact A.6.RCD missing governor only when the selected assignment claim requires that missing predicate. Source exposure and the affected party's challenge remain available independently of who may later perform repair.

| Viewpoint | Prompt |
| --- | --- |
| Relying actor | Which claim named by value or effect needs an evidence relation, and what is the minimum carrier, source-bearing record or relation, time, and evidence-provenance path for that claim or effect? |
| Issuer, verifier, or status relation maintainer | Which facts in the selected source relation and verification regime must be exposed or repaired for this claim? |
| Auditor or technical reviewer | Can the carrier and selected source relation be recovered, together with the method/Work trace, time, and live rival that this reliance question needs? |
| Security reviewer or compliance reviewer | Which applicable verification, source-order, supersession, and disclosure conditions decide this reliance question? |
| LLM user or tool user | Which generated or copied operative claims map to source passages or carriers, and which claims remain only source-finding? |
| Author of model documentation or data documentation | Which intended-use, evaluation-condition, version, window, limitation, and evidence carriers bound the model documentation or data documentation? |

**Repeated missing-source-relation indicator.** If A.10 results for the same visible carrier family repeatedly report stale, contested, missing-source-relation, or no-currentness findings, record a source-relation repair action: instrument the source relation, expose the carrier field that carries the source-bearing relation, expose decision-log refs, add currentness checks and status checks, preserve claim-bound source relations for generated or copied outputs, require credential views to show status windows and currentness windows, require model documentation and data documentation to expose intended-use and evaluation-condition fields, or require provenance labels and attestation labels to name their bounded claim type. Repetition is an indicator that the source relation or display needs repair; it is not a reason to make each acting user rebuild the evidence-provenance path manually.

Display guidance for evidence and currentness: an evidence or status display should show the claim or effect, evidence carrier, the selected source relation and its recoverable reference, time window and freshness when they affect use, relying context, and any locally plausible unsupported Work use, reliance use, claim, or effect that the display must distinguish. A display that can only show source availability should say so; it must not imply approval, permission, gate passage, Work occurrence, or assurance.

Incident-learning fields for evidence and currentness overread: visible carrier or publication face, intended claim or effect, missing evidence-provenance field, evidence carrier named by value, exact source-side predicate actually used, ordinary method trace or admitted Work trace, and needed time relation; any live rival relevant to the incident; current safe disposition; and the smallest upstream repair to the implicated source relation, instrumentation, or publication. Identify the selected source episteme and the publication occurrence, form, carrier, or source display when that object needs repair; the field definitions above determine which facts must remain recoverable.

Contestability and redress relation: when an evidence-provenance path or source-currentness relation affects person or team status, access, responsibility, a compliance relation, or a release decision, the A.10 result names the disputed claim, evidence carrier, affected use or harm, available challenge, review, redress, communication, source, publication, register, access, or contact relation, allowed evidence or argument, possible disposition change, outcome route, reopen trigger, and safe interim disposition. Source exposure remains independent of who may later perform review or repair Work. Name a responsibility, allocation, commitment, permission, or authority relation—or its exact missing governor—only when assigning that future Work; its absence does not close the challenge.

**Positive repaired evidence-use statement.** When the source account is complete, write the smallest bounded statement: named relied-on claim; carrier and source; direct provenance and citation relations; ordinary bounded use; and `RelianceDisposition`. Include currentness, a locally plausible unsupported use, and a stop or reopen condition when each changes that reliance decision. Add producing or interpreting `U.Work`, each actual performer's A.13 core, independent A.15.1 admission, Method, actual bindings, and later Work only when those facts are current. Add F.6 afterward only when the receiving account needs precise assignment-bound attribution. A claimed Work-to-value link needs an exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate under its own pattern. Add authority or responsibility only when an exact relation is independently required by the use. A short Work statement may omit an unused assignment identifier only when the complete A.13 core, including its obtaining assignment, and every consumed relation remain recoverable; an assignment is never the authority or responsibility result.

What this does not authorize: A.10 does not approve, authorize, pass a gate, release, create permission or commitment, establish a local system-role-kind classification, establish a `U.SystemRoleAssignment` occurrence or state, establish a relation among system-role kinds, establish performed Work, establish a domain result, assert a representation correspondence, or raise assurance. It supplies source recovery, provenance, and bounded reliance for the exact neighboring objects named by value.

#### A.10:4.6b - Local evidence-use classifier and `RelianceDisposition` for source-bearing carrier or display reliance

Use this subsection when a visible carrier, publication face, selected source `U.Episteme` ref, exact `EpistemePublicationRelation` occurrence ref when availability is material, source relation ref, or display is being relied on for a named claim or act. First recover the claim kind, the pattern or source rule that defines or tests the claim, the source/provenance path, and the bounded use. Broad words such as `source`, `metric`, `confidence`, `conformant`, `safe`, `ready`, `certified`, `approval`, or `permission` are recovery prompts, not relation names.

This is a local reliance-use classifier, not a Core evidence-kind ontology. Use only the row that decides the attempted use. The path represents exact direct relations and the `RelianceDisposition` records one bounded A.10 judgment; neither becomes a general evidence or authority relation.
Affordability: ordinary orientation or source-finding can stop here; bounded reliance states one evidence use and the currentness window, unsupported-use boundary, and stop or reopen condition that apply to it. If a direct domain rule requires assurance, state the exact assurance claim and then use B.3. Plain wording remains ordinary unless it changes one of the named source, evidence, gate, assurance, Work, decision, or control claims.

Cheap stop: if the bounded claim, carrier, evidence-provenance path, and bounded evidence use are recoverable, with the currentness, unsupported-use boundary, and stop or reopen condition applicable to that use, and there is no actual assurance claim, gate relation, Work relation, control-bearing relation, or release relation, stay in `A.10`. Do not open B.3, A.21, B.2.5, or a broad evidence pack merely because the carrier or display looks official, quantitative, generated, credentialed, or safety-related.

Common wrong first classification: a visible carrier, selected source `U.Episteme` ref, publication-form or carrier ref, exact `EpistemePublicationRelation` occurrence ref, source relation ref, or display is approval, permission, safety, or readiness. First honest entry: recover the A.10 evidence-provenance path for one bounded claim or use; approval, permission, safety, readiness, gate passage, and work authority must be established separately under the pattern that defines or tests each claim.

Plain disposition palette: `RelianceDisposition=pass` means proceed only inside the bounded evidence use; `degrade` means use only a narrower or reversible version; `abstain` means do not decide yet; `reopen` means a changed or contested evidence relation defeated the previous classification; `evidence-needed` names missing evidence at the decision point; `assurance-needed` says a separately stated assurance claim is required before this attempted use can proceed; `blocked-current-use` blocks the attempt until its evidence-provenance path or source relation changes.

| Source-looking evidence use or attempted use | First A.10 action | Escalation trigger | Forbidden overread |
| --- | --- | --- | --- |
| Ordinary source-backed report, record, citation, observation, model card, datasheet, data card, or publication excerpt | Name the claim, carrier, producer or Method trace when relied on, evidence-provenance path, and bounded evidence use. Add currentness, a locally plausible unsupported use, and a stop or reopen condition when they change reliance. | Open B.3 only when an actual named assurance claim is current; open A.21 for a relied-on gate decision, A.15 or A.15.1 for Work, or another pattern only when that relation is actually claimed. | Evidence presence as approval, gate passage, assurance, release permission, Work authority, control authority, or safety acceptance. |
| Confidence, calibration, prediction interval, abstention reason, or selective-action cue | Name the act and the assumptions of the selected inference or calibration method. Retain its calibration population and exchangeability when that method requires them, and the window, shift, applicability, and stop condition that bound this evidence use. Use `pass` or `degrade` only for that use; exclude a locally plausible unsupported wider use when the distinction matters. | Open C.27 or G.11 when timing, expiry, refresh, distribution shift, monitoring, or applicability changes the act; open B.3 only for an actual named assurance claim. | Confidence as global permission, trust, readiness, safety, release reliance, or engineering justification. |
| Generated explanation, generated summary, or didactic reconstruction | Keep the rendering in `E.17.EFP` as explanation or source-finding unless each relied-on operative claim has an `A.10` evidence-provenance path or another source relation that carries or exposes the source basis for the operative claim. | Apply `A.10`, `B.3`, `A.21`, `A.15`, or the pattern that defines or tests the operative claim being relied on. | Explanation wording as evidence, assurance, approval, gate passage, work occurrence, or permission. |
| Conformance label, `CV.Status`, benchmark result, score, semantic-fidelity marker, or CV-looking publication near release | Recover the declared relation: measurement or marker relation, `A.20` step-local CV status, `A.21` gate check, `E.19` admission/refresh review result, `E.21` pattern-quality evaluation result, `C.16` characterization, or external-rule source named by value. A score label alone selects neither E.19 nor E.21. | Open `A.21` only when a named gate applies its profile rule to the effective check-application results and returns a `GateDecisionResult`; open `B.3` only when an assurance claim is being made. | Conformance or score as value, adequacy, release confidence, work occurrence, safety, trust, or gate passage outside the declared relation. |
| Provenance, authenticity, C2PA-like credential, SLSA-like attestation, build record, or status-register display | State the bounded origin, history, build, or currentness claim being evidenced and the source relation carrying it. Retain the method/production trace, holder, status, verifier rule, and relying-context facts required by that claim or verification regime. | Open the record or relation that carries truth, permission, safety, release, gate passage, work occurrence, or assurance only when that relation is being claimed by value. | Provenance, authenticity, or status-currentness as truth, safety, approval, permission, release, gate passage, or assurance. |
| Contest, redress request, challenge, appeal, or conflicting source relation | Name the contested claim, evidence carrier, source-order or currentness issue, affected use or harm, available challenge or redress relation, allowed evidence, possible disposition change, outcome route, and reopen trigger. Add a review-responsibility relation or missing governor only when the claim assigns future review Work. | Open neighboring system-role, assignment-state, commitment, gate, control, assurance, Work, or representation patterns only when those effects are claimed by value. | Appeal-channel presence, challenge form, or redress workflow presence as truth, compliance proof, social-effect acceptance, completed redress, gate passage, or work authorization. |

For A.10 use, `RelianceDisposition` is a local disposition over the evidence-provenance path and the bounded reliance use. Outside a table column already headed `RelianceDisposition`, write the qualified form `RelianceDisposition=...` and bind it to the named bounded evidence use, with currentness and window, an unsupported-use boundary, and a reopen or stop condition when applicable; it is not `CV.Status`, `GateDecisionResult`, selector result, or `ProblemCard@Context` state.

Observed-effect or consequence evidence supports what happened or is credibly recorded. If the claim says that the source caused, prevented, would have changed, or causally contributed to the effect, use `C.28` for that causal question while retaining its A.10 evidence path and any separately required Work or assurance relation. A normative responsibility or allocation claim uses its own direct rule; the phrase 'responsible for' must be resolved from the source claim before selecting either branch.

If a proxy marker, benchmark, confidence value, dashboard metric, or score becomes the primary driver for action, release, resource allocation, people status, team status, or P2W priority, check whether the claim being made also raises an `E.13` proxy-to-objective question. Do not open `E.13` for every metric; open it only when the proxy is being used as the target or decision driver.

Use `C.26.1` when publication, observation, or another interaction changes the represented state while its output is being used as if it were a passive read, export, comparison, or decision input. First identify what the interaction changed and which use of the output must change. This is the probe-coupled question for a dashboard, warning, label, or public status display; ordinary influence without the false passive-read use does not activate it.

| `RelianceDisposition` | A.10 classification | Minimum A.10 statement |
| --- | --- | --- |
| `RelianceDisposition=pass` | The evidence relation named by value is present and current for the named use, evidence of the required kind is present, the source relation is current enough for that use, and the evidenced use is bounded. | State the evidenced claim, act, work occurrence, review claim, or P2W carry-through use and its evidence-provenance path. Add the applicable window and any locally plausible unsupported use that must be excluded. |
| `RelianceDisposition=degrade` | The source relation carries only a narrower claim, smaller audience, reversible local act, lower assurance input, or shorter window. | State the narrowed bounded evidence use, the proposed or locally plausible wider use it excludes, and the applicable stop condition. |
| `RelianceDisposition=abstain` | Evidence is insufficient, stale, out-of-context, uncalibrated, conflicted, or not tied to the claimed relation, while immediate rejection is not justified. | State the claim not decided and the missing evidence or relation needed before use. |
| `RelianceDisposition=reopen` | A contest, changed representation, changed selected entity, stale source, expired window, changed profile, conflicting source, retargeting, or new evidence defeats the previous evidence-provenance path. | State the source or relation to reopen and the previous use that is no longer evidenced. |
| `RelianceDisposition=evidence-needed` | The visible carrier, selected source `U.Episteme` ref, exact publication-occurrence ref when availability is material, source relation ref, or display may matter, but evidence of the required kind or the source-currentness relation is absent. | State the missing evidence kind, the pattern or source rule that defines or tests it, and the decision point so delay does not become indefinite. |
| `RelianceDisposition=assurance-needed` | A direct domain rule or receiving decision requires a separately stated assurance claim before the attempted use may proceed, and the current A.10 basis alone cannot supply it. | State the required assurance claim and its direct domain basis. Apply B.3 only after that claim is current; until then block or narrow the attempted use. |
| `RelianceDisposition=blocked-current-use` | No current evidence-provenance path carries the evidence relation needed for the attempted act, work, claim, gate, release, assurance, review, control-bearing feedback, or P2W use. | State the blocked use and the neighboring pattern or project record required before a new attempt. |

Minimum contest relation with possible redress: a contest relation exists when the affected party can identify the disputed claim or source, affected use or harm, an available challenge, review, redress, communication, source, publication, register, access, or contact relation, evidence or argument allowed in challenge, possible disposition change, outcome route, and reopen trigger. A system-role label, assignment, feedback channel, complaint form, or appeal label without those recoverable values is not enough to change the disposition. Responsibility for future review Work is a separate claim.

Affected-party contestable minimum: even when raw evidence stays restricted, the contesting party must be able to see enough of the claim, source class, disposition, affected use, available challenge or contact route, and allowed challenge evidence to challenge the result. Privacy, security, or privilege can narrow disclosure; they cannot erase the challengeable minimum while still claiming contest or redress.

False-negative reliance guard: a blocked, abstained, or evidence-needed use is not final if challenge evidence, missing affected-party evidence, changed source relation, changed selected source `U.Episteme` edition, changed `EpistemePublicationRelation` occurrence when availability is material, changed publication form, changed evidence carrier, changed representation, or redress can materially change the disposition. If refusal is based on missing evidence, name the missing evidence kind and decision point rather than closing the dispute by vagueness.

Sensitive evidence boundary: use scoped, hashed, redacted, or access-controlled evidence refs when raw carriers would expose personal data, secrets, tokens, privileged logs, tenant identifiers, incident details, security-sensitive traces, or unnecessary identities. A redacted path must still preserve enough recoverability for the relied-on claim, disposition, and contest relation.

Worked source-overread slices:

| Slice | A.10 usable classification | Unsupported lift |
| --- | --- | --- |
| Software supply-chain attestation is cited near a release conversation. | The attestation may evidence its named bounded origin, build-method, or production-trace claim. Recover the verifier-rule, holder, and currentness facts that this claim or its verification/use regime requires. | Runtime safety, release approval, gate passage, or assurance unless `B.3`, `A.21`, or another relation that carries the asserted use is established for that use. |
| A verified provenance credential, watermark, or authenticity mark appears on a publication face. | The mark may evidence where the carrier, signature, assertion, or manifest came from under the verifier regime. | Truth of the represented world-state, safety, permission, or adequacy by provenance alone. |
| A confidence interval or calibration result is used for one reversible act. | State the act, context, calibration condition, and bounded evidence use, with the applicable window, unsupported-use boundary, and stop condition. | Global readiness, trust, safety, release reliance, or engineering justification. |
| A generated explanation or summary says a result is reliable. | Treat the rendering as source-finding or explanation until the operative claim has an `A.10` evidence-provenance path or another source relation that carries or exposes the source basis for the operative claim. | Evidence, approval, gate passage, work occurrence, or assurance by fluent wording. |
| Contest or redress is claimed after a source relation, selected source `U.Episteme`, exact publication occurrence, publication form, or evidence carrier is challenged. | State the disputed claim, affected use or harm, available challenge or redress relation, allowed challenge evidence, possible disposition change, outcome route, and reopen trigger. Add future-review responsibility only when that stronger claim is current. | Claim truth, compliance proof, completed redress, or social-effect acceptance by appeal-channel presence. |
| A harmed party gives challenge evidence that could change the disposition, but the receiving System answers "evidence insufficient" without naming the missing evidence kind or decision point. | Treat the refusal as `RelianceDisposition=reopen` or invalid `RelianceDisposition=evidence-needed`; name the missing evidence kind, decision point, available challenge route, and possible disposition change. | Closed refusal, completed redress, or `RelianceDisposition=blocked-current-use` by vague insufficiency. |

#### A.10:4.6c - Route a Changed Claim Across Several Actual Receiving Uses

Use `A.10.1` when a later or replacement source may materially change a claim and the receiving uses must still be found across a bounded frame or closed across several actual uses. `A.10` continues to govern each exact one-use source-to-use account, direct-use relation, and `RelianceDisposition`. Applying `A.10.1` bounds the receiving-use search frame, states source-outward and receiver-oriented coverage and gaps, classifies found candidates as `depends`, `mentions only`, or `unresolved`, and prepares only action-changing `depends` branches for application of their direct subject-pattern guidance.

If one already-known bounded reliance use is the whole question, apply `A.10` and the direct subject guidance. A citation, carrier, declared edge, or graph-reachable node does not become affected merely because the source changed. The completed A.10.1 account cites each independently obtained subject result afterward; it neither replaces that result nor changes A.10's disposition set.

#### A.10:4.7 - Causal support in evidence-provenance paths

An A.10 path used for a causal claim cites the exact C.28 components it actually carries; it does not compress them into one alternative-valued “support basis” or copy C.28's field list.

```text
causalSupportComponentRefs?: CausalSupportComponentRefs
causalUseSupportResultRef?: CausalUseSupportResultRef
```

`CausalSupportComponentRefs` remains defined only by C.28. A.10's ordinary evidence-provenance path still identifies the exact source, carrier, Work or data, provenance relations, and bounded use required by this pattern. Inside the C.28 contract, cite only the components the causal claim actually relies on. When C.28 admits another specialist component, A.10 can cite it through that contract without defining a second schema.

Examples:

- an observational cohort path cites the observation and measurement Work plus `observationalOrNaturalBehaviorData`; an intervention-effect statement still needs a C.28 identification or design result;
- a randomized estimate path cites assignment and Work evidence, its identification or design result, estimate, uncertainty, and limits;
- a prospective counterfactual-sampling path may cite the realizability result, its decision Method, the sampling construction or obstruction required by its status, and any unresolved question; counterfactual-quantity bounds use a separate identification result, and the prospective path claims no performed sampling or data;
- a performed counterfactual-sampling path cites independently admitted dated sampling Work and the resulting sample or data; add precise assignment-bound attribution only when the receiving support claim uses it. Only the complete Work/data path may support `realizedCounterfactualSamplingData`;
- a simulation path cites model output, assumptions, validation, and bounded model use; it does not become realized or interventional evidence by relabeling;
- a target-trial emulation path cites its `TargetTrialMappingResult`, including the observational source, protocol-to-data mappings, gaps, residual-confounding assessment, and sensitivity mappings; reporting completeness alone establishes neither identification nor low bias;
- an off-policy or causal-RL path cites its exact `OffPolicyCausalEvaluationResult` with the question, behaviour and evaluation policies, overlap check, supported and unsupported use, and reopen condition. It also cites optional details about history or horizon, confounding, changed endpoints or transport, the estimator, and uncertainty only when they change what the path supports, where that support came from, whether it is current, its bounded use, or when it reopens;
- a causal-representation path cites its exact `CausalVariableRepresentationRecord` with the question, source representation, selection or abstraction Method, representation assumptions, intervention-validity result, supported and unsupported use, and reopen condition. It also cites optional invariance, fidelity, query-preservation, uncertainty, or shift-limit results only when they change what the path supports, where that support came from, whether it is current, its bounded use, or when it reopens;
- a transport path cites every changed endpoint, assumptions, overlap evidence, formula or comparator, uncertainty or unresolved assumptions, and bounded use carried by its transportability result; and
- an observationally identified estimate cites both the evidence path and separate identification and estimate results.

What changes in practice: the path exposes where every relied-on component came from and may cite the C.28 support-result episteme. A.10 creates none of the C.28 components, the causal verdict, or downstream authority by carrying their refs.

