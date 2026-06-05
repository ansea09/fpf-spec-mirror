---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring (C‑4)"
section_id: "A.10:4"
section_title: "Solution — The Evidence Graph Referring Standard"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__005_solution-the-evidence-graph-referring-standard.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.10 — Evidence Graph Referring (C‑4)"
  - "A.10:4 — Solution — The Evidence Graph Referring Standard"
line_start: 18255
line_end: 18483
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:4 - Solution — The Evidence Graph Referring Standard

The Standard is a small set of primitives applied uniformly, with **practitioner-first clarity** and **formal hooks** for proof obligations. Its primary EntityOfConcern is the evidence/provenance path for a claim: carriers, external transformer roles, method traces, work traces, time stance, and evidence edges. Authority-looking reliance and causal-use evidence are specialized uses of that same evidence path; they do not redefine `A.10` as a pattern about labels, dashboard wording, or source rhetoric.

#### A.10:4.1 - EPV‑DAG (Evidence–Provenance DAG).
A **typed, acyclic** graph disjoint from mereology. Node types: **SymbolCarrier** (a `s.System` in **CarrierRole**, A.15), **TransformerRole** (external Transformer, A.12), **MethodDescription** (design-time blueprint of a method, A.15), **Observation** (a dated assertion or result record), **s.Episteme** (knowledge holon). Edge vocabulary is small and normative: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore` (temporal), etc.
*Practitioner view:* it is the *“because‑graph”*: every claim answers “because of these carriers, by this Transformer, using that method, then.”

#### A.10:4.2 - Evidence relations (two relations, two flavours)

* `verifiedBy` — links a claim to **formal** evidence (proof obligations, static guarantees, model‑checking records).
* `validatedBy` — links a claim to **empirical** evidence (tests, measurements, trials, observations).
  Both evidence relations terminate in the EPV-DAG, not in the mereology graph.

#### A.10:4.3 SCR / RSCR (Symbol Carrier Registers).
Every `Γ_epist` aggregation **SHALL** emit an **SCR**: an exhaustive register of **symbol carriers** substantively used in the aggregate, with id, type, version/date, checksum, source/conditions and optional `PortionOf` (A.14) for sub‑carriers.
Every `Γ_epist^compile` **SHALL** emit an **RSCR**: SCR specialised to a **bounded context** (vocabularies, units) with publication‑grade identifiers and hashes.
*Why this matters:* it prevents “lost sources” during composition and underwrites reproducibility without mandating any specific tool.

#### A.10:4.4 Scope alignment (A.4) across Role–Method–Work (A.15).

* **Design‑time**: **MethodDescription** lives here as an episteme describing `U.Method`; evidence relations reference what *would* constitute proof or test for that method.
* **Run‑time**: **Work** (actual execution) lives here; traces reference which `U.Method` they enact and cite the `methodDescriptionRef` used to identify or constrain it and record `happenedBefore`.
  Bridging edges are explicit (“this run trace enacts that method under this method-description source”), so scopes never silently mix.

#### A.10:4.5 External TransformerRole (A.12).
The system that produces or interprets evidence is **external** to the holon under evaluation. If true reflexivity is essential, model a **meta‑holon** (A.12): the self‑updating holon becomes the *object* of a meta-holon external transformer (the “mirror”), restoring objectivity.

#### A.10:4.6 Γ-flavour hooks (how each flavour evidences).

* **Γ\_sys (formerly Γ\_core)**: physical properties are evidenced by measurement models, boundary conditions, calibration carriers, and dated observations.
* **Γ\_epist**: always outputs SCR/RSCR; every provenance/evidence node resolves to an SCR/RSCR entry.
* **Γ\_method**: order‑sensitive composition; at design‑time a **Method Instantiation Card (MIC)** states `Precedes/Choice/Join` and guards; at run‑time traces record `happenedBefore` and point to the `U.Method` they enact and the `methodDescriptionRef` they used.
* **Γ\_time**: temporal claims state interval coverage; **Monotone Coverage** (no unexplained gaps/overlaps) is required.
* **Γ\_work**: resource spending and yield are evidenced by instrumented carriers (meters, logs) and their `methodRef` plus `methodDescriptionRef`; keep **resource rosters** separate from SCR/RSCR.

> **Practitioner shortcut:** If you can answer *what carriers, which system, which method, when*, the evidence relation is likely sufficient; if any of the four is missing, it is not.

#### A.10:4.6a - Authority-reliance use of ordinary A.10 evidence paths

Use this subsection when an authority-looking case is being used as evidence for reliance. The evidence path is claim-bound: it evidences a named claim or effect for a named work move or reliance move, not "authority" in general. This subsection does not change the A.10 evidence-path EntityOfConcern; it applies the same evidence and provenance path to source-sensitive cases where displays, credentials, copied text, generated text, dashboards, provenance labels, or attestations are being overread. If the live work occurrence, gate decision, speech act, commitment, or evidence path is already clear, recover and cite that exact FPF source directly instead of analyzing nearby wording first.

A10-lite is enough for source-finding, orientation, learning, and bounded reversible probes:

| Field | Required content |
| --- | --- |
| claim or effect | The claim, effect, or source-backed reliance use the carrier is being asked to evidence for the named work move or reliance move. |
| carrier | The display, badge, credential, attestation, dashboard tile, copied text, generated text, log, trace, source file, report, or other external carrier. |
| producer, issuer, verifier, or source-maintenance role assignment | The role assignment or system that issued, performed, attested, measured, copied, generated, verified, or displayed the carrier or source-backed content. |
| method execution or work event | The work act, measurement, verification, review, build, attestation, copy, extraction, generation, dashboard query, API read, trace, log, or method instance that produced the carrier. |
| time window | Issue time, validity window, decay, supersession, revocation, policy or gate version, and reopen condition. |

Minimum path for routine reliance:

| Field | Required content |
| --- | --- |
| Evidenced claim or effect | Approval, permission, gate passage, role or status currentness, work occurrence, evidence relation, assurance input, or other exact claim or effect being attempted. |
| Carrier | The visible or recovered carrier, with enough identity to reopen it. |
| Issuer, performer, trust root, status register, or source-maintenance role assignment | The role assignment, system, or governing register accountable for producing, updating, or verifying the carrier or source-backed content in this context. |
| Affected entity and relying context | The release, service, model, person, role holder, policy subject, work item, claim, audience, tenant, environment, or other entity for which reliance is attempted. |
| Time window and freshness | Issue time, validity window, decay, supersession, revocation, policy or gate version, and reopen condition. |
| Evidence-producing work event or method trace | The production, verification, query, generation, execution, or review work that made the carrier. |
| Evidence relation and rival explanation | Which claim the carrier evidences, how it evidences it, and the principal live rival explanation such as stale display, spoofed badge, copied wording, generated paraphrase, context shift, carrier-only provenance, or local-only transform relation. |

Expanded fields are collected only insofar as they decide the live reliance question. Evidence depth follows consequence severity, reuse, contestability, cross-context movement, and the evidence relation required for the attempted claim. Do not expand a source-finding note into a full evidence dossier, and do not collect every expanded field merely because a carrier is copied, generated, credential-like, provenance-like, or cross-context.

**Adversarial misuse guard.** Do not let carrier authenticity, provenance, copied approval, generated summary, stale screenshot, credential status view, or dashboard export convert into claim truth or currentness. Treat each as a rival explanation to test against issuer or source-maintenance role assignment, method trace or work trace, time window, and relying context.

**Data-minimization and privacy boundary.** Preserve minimum sufficient evidence relation for the intended reliance use. Use redacted, hashed, scoped, or role-mediated carrier refs when raw evidence would expose personal identity, access tokens, cryptographic proof payloads, tenant identifiers, security logs, incident details, internal release metadata, audit trails, privileged reviewer names, or sensitive model/data provenance. Redaction does not create source relation; it must preserve enough recoverability for the relying context.

| Expanded field | When it is live |
| --- | --- |
| Method trace or work trace | Provenance, attestation, generated source relation, copied source relation, dashboard source relation, rollback source relation, or work occurrence is being used. |
| Carrier integrity | The carrier may be spoofed, stale, copied, transformed, rendered, redacted, or context-shifted. |
| Identity or holder binding | The claim depends on a credential holder, role holder, issuer, performer, delegate, revoker, verifier, or relying party. |
| Verifier context, relying-party context, and acceptance rule | The evidence relation is valid only for a verifier, audience, tenant, environment, release line, policy subject, operational mode, or consumer-side policy or gate rule that accepts the evidence for this use. |
| Proof, cryptographic-signature, or status verification result | Credential, provenance, attestation, authenticity, revocation, or currentness relation is claimed. |
| Policy/gate version and decision source | Permission, admissibility, gate passage, release, rollback authority, or policy authorization is attempted. |
| Source-chain transform notes | Evidence relation passed through extraction, copy, rewrite, representation shift, explanation rendering, summary, export, redaction, or another transform step before reliance. |
| Source order and supersession rule | Multiple source candidates disagree or freshness or priority may defeat the visible publication face, carrier, rendering, or cue. Include the governing register or status-source order when a register entry is the source of role assignment, status assertion, permission, duty, or gate state. |
| Minimum disclosure boundary | Raw evidence would expose secrets, personal data, tenant identifiers, privileged logs, tokens, security-sensitive traces, or unnecessary identities. |

Case repairs:

| Case | Evidence repair |
| --- | --- |
| Stale credential badge or status display | Show issuer or trust root, governing status register when one exists, holder or subject binding, verifier and relying-party context, proof result or status result, revocation and freshness, validity window, status-source entry version, and carrier integrity. Display presence is not current role assignment, status assertion, or permission. |
| Verifiable credential, credential view, or register excerpt | Treat as an A.10 carrier with issuer or trust root, governing status register when one exists, register entry or source-record id and version, holder or subject binding, verifier, proof result, status result, currentness, relying context, validity window, revocation window, and acceptance rule. When those checks pass, it may evidence credential-currentness for that holder and relying context. It evidences permission, authorization, role assignment, status assertion, or gate passage only when the register entry or another exact source such as `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` creates or states that effect for the bounded context. |
| Copied approval or review summary | Show the original `A.2.9` `SpeechActRef` / issuing act when approval or authorization is claimed, or the original reviewed source when only review-content currentness is claimed. Add copy relation, currentness, scope/window, evidence-producing work/event, and whether separate commitment/work relation is live. Copy evidence is not approval by itself. |
| Provenance, authenticity, or attestation label | Show the bounded origin, history, build, or process claim; source episteme, source episteme publication, or source carrier; method trace or work trace; source-specific proof; carrier integrity; verifier or relying policy that accepts it for this claim or effect; and rival explanation. Provenance does not show truth, safety, approval, release, gate passage, permission, or assurance unless another exact source carries that additional claim or effect. |
| Dashboard status tile | For gate-passage or release reliance, show dashboard query/source/time/window/currentness, source order, freshness policy, rival explanation, and the current `A.21` `GateDecision` / `DecisionLogRef` with gate profile/version and release/work target; the A.10 path evidences that source chain. A status display is not gate passage or work occurrence by itself. |
| Rollback command-like cue | Show command/authorization source, actor, affected work target or claim target, scope/window, and whether the cue is only an `A.6.A` action invitation. A command cue is not execution evidence. |
| Rollback execution result | Show `A.15.1` `U.Work` occurrence, method trace or work trace, logs, outcome evidence, and time window. Execution evidence is not approval, assurance, or gate passage by itself. |
| Generated explanation | Use `E.17.EFP` to classify the explanation relation and source-finding use. For reliance, show claim-bound attribution alignment: every operative claim relied on maps to a source passage, carrier, or exact `governingPatternRef` or `authoritySourceRef` that evidences that claim in the relying context. When that mapping is complete, A.10 may evidence those operative claims as source-backed evidence; the explanation itself still does not issue, approve, authorize, pass a gate, evidence execution, or raise assurance. |
| Model card or datasheet used as evidence | Show documented admissible-use statement or external intended-use field, version/window, evaluation condition, limitations, evidence carriers, and whether a `B.3` assurance claim is live. Documentation does not become readiness or assurance by presence. |
| Extracted-source chain to gate or release claim | Name the source reference, the first lossy or non-commutative transform step, the FPF relation or pattern governing that transform (`A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `E.17.ID.CR`, or `E.18` where applicable), the admissible inference move after the step, the exact `governingPatternRef` or `authoritySourceRef` that carries the live claim, the source reopen trigger, and the gate claim or release claim blocked until those source relations are recoverable. |
| Conflicting sources | When display, source carrier, decision log, recency signal, freshness signal, copied summary, generated summary, credential status, provenance label, or assurance evidence disagree, name the visible source, rival source, source order, decision source, freshness policy, and supersession rule. Do not choose by color, visual salience, confidence wording, copied wording, or apparent recency; the work claim or reliance claim is contested until the source-order question is resolved. |
| Sensitive evidence path | Use redacted, hashed, scoped, or role-mediated carrier refs when raw carriers expose secrets, personal data, security-sensitive traces/data, privileged logs, tenant identifiers, or unnecessary identities. Redaction does not create source relation; it must preserve enough recoverability for the relying context. |
| Pointer or proof-status evidence path | Use a hash, proof verification result, status verification result, source ref, scoped pointer, disclosure receipt, or role-mediated view instead of copying raw sensitive carriers or payloads when that pointer preserves enough recoverability for the relied-on claim or effect. Do not copy raw secrets, tokens, privileged logs, personal identities, or tenant details merely to make the evidence path look fuller. |

If the path is incomplete, A.10 returns evidence-path state and source-currentness status, not work or reliance evidence relation for the attempted claim or effect. Valid dispositions include source-finding only, reopen original carrier, request issuer or status verification, refresh dashboard query or API query, mark stale or contested, narrow the live P2W class or reliance claim, proceed only with a reversible local probe under an explicit work plan when work is live, or block the unsupported work claim or reliance claim.

**Broken-source repair assignment.** If the relying actor cannot recover or verify the source path, assign the repair to the accountable project-side responsibility assignment: issuer or performer, verifier or status service, evidence-producing work role assignment or system, gate-decision source, role or status source, or boundary source. The A.10 result should name the missing source and blocked use rather than making the relying actor reconstruct a source they cannot issue or verify.

Role prompts for evidence or currentness use:

| Role in the situation | Prompt |
| --- | --- |
| Relying actor | Which exact claim or effect needs an evidence relation, and what is the minimum carrier, source, time, and relation path for that claim or effect? |
| Issuer, verifier, or status source | Which issuer, holder, verifier, proof result, status result, currentness, revocation, or acceptance-rule source must be exposed or repaired? |
| Auditor or reviewer | Which carrier, source-maintenance role assignment, method trace or work trace, time window, evidence relation, and rival explanation must be recoverable? |
| Security source or compliance source | Which source order, supersession, proof result, status result, revocation, and minimum-disclosure boundary decide this reliance question? |
| LLM/tool user | Which generated or copied operative claims map to source passages or carriers, and which claims remain only source-finding? |
| Model source or data source | Which intended-use, evaluation-condition, version, window, limitation, and evidence carriers bound the model documentation or data documentation? |

**Repeated missing-source indicator.** If the same visible-item family repeatedly returns stale, contested, no-source, or no-currentness A.10 results, record a source-system repair item: instrument the source, expose decision-source refs, add currentness checks and status checks, preserve claim-bound source links for generated or copied outputs, require credential views to show status windows and currentness windows, require model documentation and data documentation to expose intended-use and evaluation-condition fields, or require provenance labels and attestation labels to name their bounded claim type. Repetition is an indicator that the source path or display needs repair; it is not a reason to make each acting user rebuild the path manually.

Display guidance for evidence and currentness: an evidence or status display should show the claim or effect, carrier, source-maintenance role assignment, exact ref or link, time window, freshness, relying context, and unsupported action, claim, or effect. A display that can only show source availability should say so; it must not imply approval, permission, gate passage, work occurrence, or assurance.

Incident-learning fields for evidence and currentness overread: visible carrier or publication face, intended claim or effect, missing source-path field, exact carrier, source-maintenance role assignment, method trace, work trace, and time relation needed, rival explanation that made the overread plausible, current safe disposition, and upstream repair item for instrumentation, source refs, status, currentness, claim-bound source links, credential view, model documentation, data documentation, or provenance and attestation label.

Contestability and redress path: when an evidence path or currentness path affects person or team status, access, responsibility, a compliance relation, or a release decision, the A.10 result should name the disputed claim, carrier, source-maintenance role assignment, verifier or status source, freshness or revocation source, privacy-minimized evidence ref, safe interim disposition, and review or redress path. A disputed display remains contested until the source-order or currentness question is resolved.

**Positive repaired path.** When the source path is complete, return the smallest source-backed evidence-use statement: named claim or effect, carrier and source-maintenance role assignment, method trace or work trace, time window, currentness, evidence relation, and the exact action or reliance for which it is admissible. The downstream use is admissible only inside that scope, without treating evidence relation as approval, permission, gate passage, work occurrence, or assurance.

What this does not authorize: `A.10` does not approve, authorize action, pass a gate, release, create permission, create a commitment, assign a role, record a work occurrence, or raise assurance. It supplies the evidence path and evidence-use classification that `A.15`, `A.6`, `B.3`, `A.21` gate-decision sources, `A.20` constraint-validity sources, `A.2.9` speech-act sources, `A.2.8` commitment sources, `A.15.1` work-occurrence sources, or another exact `governingPatternRef` or `authoritySourceRef` may consume.

#### A.10:4.6b - Local evidence-use classifier and `RelianceDisposition` for source-looking evidence uses

Use this subsection when a visible source is being treated as evidence for a claim, act, work move, gate, release, review claim, assurance use, or problem-side P2W use. The first A.10 move is to recover the evidence kind and the bounded use it can actually make admissible. Broad source words such as `source`, `metric`, `confidence`, `conformant`, `safe`, `ready`, `certified`, `approval`, or `permission` are only recovery prompts; they do not name the evidence relation by themselves.

This subsection uses a local reliance-use classifier, not a Core evidence-kind ontology. Its practical gain is a smaller next move: recover the evidence relation, name the admissible and non-admissible use, then stop or exit to the exact receiving pattern. It is not a required project review step and does not ask the practitioner to inspect every source-looking item.

Section role: the first table is an A.10 recognition aid, the `RelianceDisposition` table is a minimum local record aid, and the worked source-overread slices are regression/review slices. They are not project checklists, a required sequence, a new evidence ontology, or a general source classifier. Use only the row that answers the live attempted evidence use, then stop when the bounded evidence relation, admissible use, non-admissible use, and reopen condition are clear. This local section returns the attempted use to A.10 evidence relation; it does not create an extra SEMIO authority or cross-pattern relation vocabulary.

Affordability card: orientation or source-finding remains a cue and stops here; bounded reliance states one admissible use, non-admissible use, window, and reopen condition; threshold reliance exits to the minimum receiving pattern only when the B.3 material-reliance threshold is live: behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation would materially change. Plain wording remains ordinary unless it changes admissible use, source relation, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

Cheap stop: if a bounded claim, current carrier, evidence path, window, admissible use, non-admissible use, and reopen trigger are present, and no assurance, gate, work, control-bearing relation, release relation, or B.3 material-reliance threshold is live, stay in `A.10`. Do not open `B.3`, `A.21`, `B.2.5`, or a broad evidence pack merely because the source looks official, quantitative, generated, credentialed, or safety-related.

Common wrong first reading: a visible source is approval, permission, safety, or readiness. First honest entry: recover the A.10 evidence path for one bounded claim or use; approval, permission, safety, readiness, gate passage, and work authority stay with their receiving patterns when live.

Plain move palette: `RelianceDisposition=pass` means proceed only inside the bounded use; `RelianceDisposition=degrade` means use only a narrower or reversible version; `RelianceDisposition=abstain` means do not decide yet; `RelianceDisposition=reopen` means changed or contested evidence relation defeated the previous reading; `RelianceDisposition=evidence-needed` means ask for the named missing evidence at the named decision point; `RelianceDisposition=safety-case-required` means return to `B.3` because the B.3 material-reliance threshold is live; `RelianceDisposition=no-admissible-current-use` means block the current attempted use until a receiving source changes.

| Source-looking evidence use or attempted use | First A.10 move | Escalation trigger | Forbidden overread |
| --- | --- | --- | --- |
| Ordinary source-backed report, record, citation, observation, model card, datasheet, data card, or publication excerpt | Name the claim, carrier, producer or method trace, evidence path, currentness window, admissible use, non-admissible use, and reopen trigger. | Open `B.3` only when assurance is live or the B.3 material-reliance threshold is live; open `A.21` for active gate decision, `A.15` or `A.15.1` for work, or another exact neighbor only when that relation is live; open `B.2.5` only when a controlled object is regulated through a feedback channel, evidence channel, cadence, window, or supervisory/control relation. | Evidence presence as approval, gate passage, assurance, release permission, work authority, control authority, or safety acceptance. |
| Confidence, calibration, prediction interval, abstention reason, or selective-action cue | Make only the named act admissible, context, window, calibration population or exchangeability/shift basis, applicability condition, and stop condition. Use `RelianceDisposition=pass` or `RelianceDisposition=degrade` only for that bounded use, and state the unsupported attempted use beside it. | Open `C.27` or `G.11` when timing, expiry, refresh, distribution shift, monitoring, or applicability change alters the admissible act; open `B.3` when assurance is live or the B.3 material-reliance threshold is live. | Confidence as global permission, trust, readiness, safety, release reliance, or engineering justification. |
| Generated explanation, generated summary, or didactic reconstruction | Keep the rendering in `E.17.EFP` as explanation or source-finding unless each relied-on operative claim has an A.10 evidence path or another exact receiving source. | Open `A.10`, `B.3`, `A.21`, `A.15`, or another exact source only for the operative claim being relied on. | Explanation wording as evidence, assurance, approval, gate passage, work occurrence, or permission. |
| Conformance label, `CV.Status`, benchmark result, score, semantic-fidelity marker, or CV-looking publication near release | Recover the declared relation: measurement or marker relation, `A.20` step-local CV status, `A.21` gate check, `E.19` pattern-quality result, `C.16` characterization, or exact external-rule locus. | Open `A.21` only when an active `OperationalGate(profile)` consumes effective gate-check refs and emits a `GateDecision`; open `B.3` only when assurance is live. | Conformance or score as value, adequacy, release confidence, work occurrence, safety, trust, or gate passage outside the declared relation. |
| Provenance, authenticity, C2PA-like credential, SLSA-like attestation, build record, or status-register display | State the bounded origin, history, build method or production trace, holder, status, verifier rule, relying context, and currentness claim it evidences. | Open the source that carries truth, permission, safety, release, gate passage, work occurrence, or assurance only when that exact relation is live. | Provenance, authenticity, or status-currentness as truth, safety, approval, permission, release, gate passage, or assurance. |
| Contest, redress request, challenge, appeal, or conflicting source | Name the contested claim, carrier, source order, freshness/currentness issue, affected use, accountable review role, allowed challenge evidence, possible disposition change, outcome record, and reopen trigger. | Open neighboring role, status, commitment, gate, control, assurance, work, or representation loci when their effects are live. | Appeal-channel presence as claim truth, safety, compliance proof, social-effect acceptance, or completed redress. |

For A.10 use, `RelianceDisposition` is a local disposition over the evidence path and the bounded reliance use. Outside a table column already headed `RelianceDisposition`, write the qualified form `RelianceDisposition=...` and bind it to the named attempted use, currentness/window when live, admissible use, non-admissible use, and reopen or stop condition; it is not `CV.Status`, `GateDecision`, selector result, or `ProblemCard@Context` state.

Observed-effect or consequence evidence may be used only for what happened or is credibly recorded. If the attempted use says the source caused, prevented, would have changed, or is responsible for that effect, leave ordinary A.10 reliance and open `C.28` plus any live evidence, work, or assurance relation.

If a proxy marker, benchmark, confidence value, dashboard metric, or score becomes the primary driver for action, release, resource allocation, people/team status, or P2W priority, check whether the live claim also raises an `E.13` proxy-to-objective question. Do not open `E.13` for every metric; open it only when the proxy is being used as the target or decision driver.

If publication or observation of a cue changes the situation or source condition being read, recover the probe-coupled boundary before treating the cue as passive evidence. This sentence does not import quantum-like vocabulary; it only prevents passive-evidence overread for dashboards, warnings, labels, and public status displays.

| `RelianceDisposition` | A.10 reading | Minimum A.10 statement |
| --- | --- | --- |
| `RelianceDisposition=pass` | The exact evidence relation is live, the evidence kind is present, the source is current enough for the named use, and the supported use is bounded. | State the supported claim, act, work move, review claim, or P2W receiving use, the unsupported attempted use, the carrier path, and the window. |
| `RelianceDisposition=degrade` | The source relations only a narrower claim, smaller audience, reversible local act, lower assurance input, or shorter window. | State the narrowed admissible use, the attempted use still not admissible, and the stop condition. |
| `RelianceDisposition=abstain` | Evidence is insufficient, stale, out-of-context, uncalibrated, conflicted, or not tied to the live relation, while immediate rejection is not justified. | State the claim not decided and the missing evidence or relation needed before use. |
| `RelianceDisposition=reopen` | A contest, changed representation, changed selected entity, stale source, expired window, changed profile, conflicting source, retargeting, or new evidence defeats the previous evidence path. | State the source or relation to reopen and the previous use that is no longer supported. |
| `RelianceDisposition=evidence-needed` | The visible source may matter, but the required evidence kind or source-currentness path is absent. | State the missing evidence kind, receiving pattern, and decision point so delay does not become indefinite. |
| `RelianceDisposition=safety-case-required` | The B.3 material-reliance threshold is live: reliance on the visible source may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation. | State the threshold trigger and return to `B.3` for the minimum reliance safety assurance record, with A.10 evidence paths for the source claims. |
| `RelianceDisposition=no-admissible-current-use` | No current evidence path makes the attempted act admissible, work, claim, gate, release, assurance, review, control-bearing feedback, or P2W use. | State the blocked use and the neighboring pattern or project record required before a new attempt. |

Minimum real contest/redress: a contest path exists only when the affected party or accountable reviewer can identify the disputed claim or source, affected use or harm, accountable review role, evidence or argument allowed in challenge, possible disposition change, outcome record, and reopen trigger. A feedback channel, complaint form, or appeal label without those recoverable items is not enough to change the disposition.

Affected-party contestable minimum: even when raw evidence stays reviewer-only, the contesting party must be able to see enough of the claim, source class, disposition, affected use, accountable role, and allowed challenge evidence to challenge the result. Privacy, security, or privilege can narrow disclosure; they cannot erase the challengeable minimum while still claiming contest or redress.

False-negative reliance guard: a blocked, abstained, or evidence-needed use is not final if admissible challenge evidence, missing affected-party evidence, changed source, changed representation, or redress can materially change the disposition. If refusal is based on missing evidence, name the missing evidence kind and decision point rather than closing the dispute by vagueness.

Sensitive evidence boundary: use scoped, hashed, redacted, or role-mediated evidence refs when raw carriers would expose personal data, secrets, tokens, privileged logs, tenant identifiers, incident details, security-sensitive traces, or unnecessary identities. A redacted path must still preserve enough recoverability for the relied-on claim, disposition, and contest path.

Worked source-overread slices:

| Slice | A.10 usable reading | Non-admissible lift |
| --- | --- | --- |
| Software supply-chain attestation is cited near a release conversation. | The attestation may evidence bounded origin, build method or production trace, verifier-rule, holder, and currentness claims. | Runtime safety, release approval, gate passage, or assurance unless `B.3`, `A.21`, or another exact receiving relation is live. |
| A valid provenance credential, watermark, or authenticity mark appears on a publication face. | The mark may evidence where the carrier, signature, assertion, or manifest came from under the verifier regime. | Truth of the represented world-state, safety, permission, or adequacy by provenance alone. |
| A confidence interval or calibration result is used for one reversible act. | State the act, context, calibration basis, window, admissible use, non-admissible use, and stop condition. | Global readiness, trust, safety, release reliance, or engineering justification. |
| A generated explanation or summary says a result is reliable. | Treat the rendering as source-finding or explanation until the operative claim has an `A.10` evidence path or another exact receiving source. | Evidence, approval, gate passage, work occurrence, or assurance by fluent wording. |
| Contest or redress is claimed after a source is challenged. | State the disputed claim, affected use, accountable review role, allowed challenge evidence, possible disposition change, outcome record, and reopen trigger. | Claim truth, compliance proof, completed redress, or social-effect acceptance by appeal-channel presence. |
| A harmed party gives admissible challenge evidence, but the accountable party answers "evidence insufficient" without naming the missing evidence kind or decision point. | Treat the refusal as `RelianceDisposition=reopen` or invalid `RelianceDisposition=evidence-needed`; name the missing evidence kind, decision point, accountable role, and possible disposition change. | Closed refusal, completed redress, or `RelianceDisposition=no-admissible-current-use` by vague insufficiency. |

#### A.10:4.7 - Causal evidence relation basis in evidence paths

Evidence graph paths used for causal-use claims must carry the `C.28`-governed `CausalEvidenceSupportBasis` without redefining causal estimands or causal-use authority.

The `C.28` values that `A.10` may carry in an evidence path are:

```text
observationalAssociationSupportBasis
interventionalActionSupportBasis
realizedCounterfactualSampleSupportBasis
identifiedCounterfactualEstimateSupportBasis
simulationOnlyCounterfactualOutputBasis
```

`A.10` consumes this value set from `C.28`; it does not add `causalAssumptionOnlySupport` or `noCausalEvidenceSupport` as evidence-basis values. Assumption-only and no-evidence-use cases are represented by causal assumptions, support verdict, admissible use, non-admissible use, or abstain in `C.28`/`B.3`, not by a second evidence-basis vocabulary.

No non-admissible `CausalityLadderRung` climb:

```text
observational-association evidence -> interventional-action claim requires CausalIdentificationProfile.
interventional-action evidence -> counterfactual-comparison claim requires CausalIdentificationProfile for
  identifiedCounterfactualEstimateSupportBasis, CounterfactualSamplingRealizabilityProfile for
  realizedCounterfactualSampleSupportBasis, or bounded-use treatment.
Simulation-only counterfactual output may be admissible for bounded model use when model assumptions, validation, admissible use, and non-admissible use are declared. It does not become interventional evidence or realized counterfactual sample evidence by vocabulary, validation, or evidence-role relabeling alone.
```

Evidence-path micro-examples:

| `CausalEvidenceSupportBasis` | EPV-style path cue |
| --- | --- |
| `observationalAssociationSupportBasis` | observed cohort table -> `PathSlice` to measurement work -> association-use statement; unsupported use = intervention-effect wording. |
| `interventionalActionSupportBasis` | randomized or governed action assignment record -> work trace -> declared intervention-effect admissible use inside assignment, follow-up, and outcome window. |
| `realizedCounterfactualSampleSupportBasis` | counterfactual-comparison sampling work plan -> run trace -> evidence carrier -> samples from declared target counterfactual distribution under physical, ethical, and operational constraints. |
| `identifiedCounterfactualEstimateSupportBasis` | causal assumptions, graph proof, calculus proof, available-data regime set, and bound refs -> `CausalIdentificationProfile` -> estimated or bounded counterfactual use with admissible use and non-admissible use. |
| `simulationOnlyCounterfactualOutputBasis` | simulator output -> counterfactual model assumptions -> simulation validation ref -> bounded model-supported use; validation remains validation and does not convert the path into direct sample evidence or intervention-effect evidence. |

What changes in practice: an evidence path can show that a carrier evidences a causal-use claim, but it must also show the causal evidence relation basis and the relevant `C.28` support references when the claim climbs from observation to intervention or from intervention to counterfactual comparison.

What this does not authorize: `A.10` does not identify causal effects, create an estimand, certify target-trial emulation, or decide counterfactual sampling realizability; it stores and makes recoverable the evidence graph path and causal support-basis refs needed by `C.28` and `B.3`.

