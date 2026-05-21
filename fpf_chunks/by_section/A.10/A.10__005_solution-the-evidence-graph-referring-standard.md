---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring (C‑4)"
section_id: "A.10:4"
section_title: "Solution — The Evidence Graph Referring Standard"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__005_solution-the-evidence-graph-referring-standard.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.10 — Evidence Graph Referring (C‑4)"
  - "A.10:4 — Solution — The Evidence Graph Referring Standard"
line_start: 18473
line_end: 18649
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

The Standard is a small set of primitives applied uniformly, with **practitioner-first clarity** and **formal hooks** for proof obligations. Its governed object is the evidence/provenance path for a claim: carriers, external transformer roles, method traces, work traces, time stance, and evidence edges. Authority-looking reliance and causal-use support are specialized uses of that same evidence path; they do not redefine `A.10` as a pattern about labels, dashboard wording, or source rhetoric.

#### A.10:4.1 - EPV‑DAG (Evidence–Provenance DAG).
A **typed, acyclic** graph disjoint from mereology. Node types: **SymbolCarrier** (a `s.System` in **CarrierRole**, A.15), **TransformerRole** (external Transformer, A.12), **MethodDescription** (design-time blueprint of a method, A.15), **Observation** (a dated assertion or result record), **s.Episteme** (knowledge holon). Edge vocabulary is small and normative: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore` (temporal), etc.
*Practitioner view:* it is the *“because‑graph”*: every claim answers “because of these carriers, by this Transformer, using that method, then.”

#### A.10:4.2 - Anchors (two relations, two flavours).**

* `verifiedBy` — links a claim to **formal** evidence (proof obligations, static guarantees, model‑checking records).
* `validatedBy` — links a claim to **empirical** evidence (tests, measurements, trials, observations).
  Both anchors terminate in the EPV‑DAG, not in the mereology graph.

#### A.10:4.3 SCR / RSCR (Symbol Carrier Registers).
Every `Γ_epist` aggregation **SHALL** emit an **SCR**: an exhaustive register of **symbol carriers** substantively used in the aggregate, with id, type, version/date, checksum, source/conditions and optional `PortionOf` (A.14) for sub‑carriers.
Every `Γ_epist^compile` **SHALL** emit an **RSCR**: SCR specialised to a **bounded context** (vocabularies, units) with publication‑grade identifiers and hashes.
*Why this matters:* it prevents “lost sources” during composition and underwrites reproducibility without mandating any specific tool.

#### A.10:4.4 Scope alignment (A.4) across Role–Method–Work (A.15).

* **Design‑time**: **MethodDescription** lives here; methods are blueprints; anchors reference what *would* constitute proof or test.
* **Run‑time**: **Work** (actual execution) lives here; traces reference which MethodDescription they instantiate and record `happenedBefore`.
  Bridging edges are explicit (“this run trace instantiates that spec”), so scopes never silently mix.

#### A.10:4.5 External TransformerRole (A.12).
The system that produces or interprets evidence is **external** to the holon under evaluation. If true reflexivity is essential, model a **meta‑holon** (A.12): the self‑updating holon becomes the *object* of a meta-holon external transformer (the “mirror”), restoring objectivity.

#### A.10:4.6 Γ‑flavour hooks (how each flavour anchors).

* **Γ\_sys (formerly Γ\_core)**: physical properties are anchored by measurement models, boundary conditions, calibration carriers, and dated observations.
* **Γ\_epist**: always outputs SCR/RSCR; every provenance/evidence node resolves to an SCR/RSCR entry.
* **Γ\_method**: order‑sensitive composition; at design‑time a **Method Instantiation Card (MIC)** states `Precedes/Choice/Join` and guards; at run‑time traces record `happenedBefore` and point to the MethodDescription they instantiate.
* **Γ\_time**: temporal claims state interval coverage; **Monotone Coverage** (no unexplained gaps/overlaps) is required.
* **Γ\_work**: resource spending and yield are evidenced by instrumented carriers (meters, logs) and their MethodDescriptions; keep **resource rosters** separate from SCR/RSCR.

> **Practitioner shortcut:** If you can answer *what carriers, which system, which method, when*, the anchor is likely sufficient; if any of the four is missing, it is not.

#### A.10:4.6a - Authority-reliance use of ordinary A.10 evidence paths

Use this subsection when an authority-looking case is being used as evidence for reliance. The evidence path is claim-bound: it supports a named claim or effect for a named work move or reliance move, not "authority" in general. This subsection does not change the governed object of `A.10`; it applies the same evidence and provenance path to source-sensitive cases where displays, credentials, copied text, generated text, dashboards, provenance labels, or attestations are being overread. If the live work occurrence, gate decision, speech act, commitment, or evidence path is already clear, recover and cite that exact FPF source directly instead of analyzing nearby wording first.

A10-lite is enough for source-finding, orientation, learning, and bounded reversible probes:

| Field | Required content |
| --- | --- |
| claim or effect | The claim, effect, or source-backed posture the carrier is being asked to support for the named work move or reliance move. |
| carrier | The display, badge, credential, attestation, dashboard tile, copied text, generated text, log, trace, source file, report, or other external carrier. |
| producer, issuer, verifier, or source-maintenance role assignment | The role assignment or system that issued, performed, attested, measured, copied, generated, verified, or displayed the carrier or source-backed content. |
| method execution or work event | The work act, measurement, verification, review, build, attestation, copy, extraction, generation, dashboard query, API read, trace, log, or method instance that produced the carrier. |
| time window | Issue time, validity window, decay, supersession, revocation, policy or gate version, and reopen condition. |

Minimum path for routine reliance:

| Field | Required content |
| --- | --- |
| Supported claim or effect | Approval, permission, gate passage, role or status currentness, work occurrence, evidence support, assurance input, or other exact claim or effect being attempted. |
| Carrier | The visible or recovered carrier, with enough identity to reopen it. |
| Issuer, performer, trust anchor, status register, or source-maintenance role assignment | The role assignment, system, or governing register accountable for producing, updating, or verifying the carrier or source-backed content in this context. |
| Affected entity and relying context | The release, service, model, person, role holder, policy subject, work item, claim, audience, tenant, environment, or other entity for which reliance is attempted. |
| Time window and freshness | Issue time, validity window, decay, supersession, revocation, policy or gate version, and reopen condition. |
| Evidence-producing work event or method trace | The production, verification, query, generation, execution, or review work that made the carrier. |
| Evidence relation and rival explanation | Which claim the carrier supports, how it supports it, and the principal live rival explanation such as stale display, spoofed badge, copied wording, generated paraphrase, context shift, carrier-only provenance, or local-only transform support. |

Expanded fields are collected only insofar as they decide the live reliance question. Evidence depth follows consequence severity, reuse, contestability, cross-context movement, and the support required for the attempted claim. Do not expand a source-finding note into a full evidence dossier, and do not collect every expanded field merely because a carrier is copied, generated, credential-like, provenance-like, or cross-context.

**Adversarial misuse guard.** Do not let carrier authenticity, provenance, copied approval, generated summary, stale screenshot, credential status view, or dashboard export convert into claim truth or currentness. Treat each as a rival explanation to test against issuer or source-maintenance role assignment, method trace or work trace, time window, and relying context.

**Data-minimization and privacy posture.** Preserve minimum sufficient support for the intended reliance use. Use redacted, hashed, scoped, or role-mediated carrier refs when raw evidence would expose personal identity, access tokens, cryptographic proof payloads, tenant identifiers, security logs, incident details, internal release metadata, audit trails, privileged reviewer names, or sensitive model/data provenance. Redaction does not create source support; it must preserve enough recoverability for the relying context.


| Expanded field | When it is live |
| --- | --- |
| Method trace or work trace | Provenance, attestation, generated source support, copied source support, dashboard support, rollback support, or work occurrence is being used. |
| Carrier integrity | The carrier may be spoofed, stale, copied, transformed, rendered, redacted, or context-shifted. |
| Identity or holder binding | The claim depends on a credential holder, role holder, issuer, performer, delegate, revoker, verifier, or relying party. |
| Verifier context, relying-party context, and acceptance rule | The support is valid only for a verifier, audience, tenant, environment, release line, policy subject, operational mode, or consumer-side policy or gate rule that accepts the evidence for this use. |
| Proof, cryptographic-signature, or status verification result | Credential, provenance, attestation, authenticity, revocation, or currentness support is claimed. |
| Policy/gate version and decision source | Permission, admissibility, gate passage, release, rollback authority, or policy authorization is attempted. |
| Source-chain transform notes | Support passed through extraction, copy, rewrite, representation shift, explanation rendering, summary, export, redaction, or another transform step before reliance. |
| Source order and supersession rule | Multiple source candidates disagree or freshness or priority may defeat the visible publication face, carrier, rendering, or cue. Include the governing register or status-source order when a register entry is the source of role assignment, status assertion, permission, duty, or gate state. |
| Minimum disclosure posture | Raw evidence would expose secrets, personal data, tenant identifiers, privileged logs, tokens, security-sensitive traces, or unnecessary identities. |

Case repairs:

| Case | Evidence repair |
| --- | --- |
| Stale credential badge or status display | Show issuer or trust anchor, governing status register when one exists, holder or subject binding, verifier and relying-party context, proof result or status result, revocation and freshness, validity window, status-source entry version, and carrier integrity. Display presence is not current role assignment, status assertion, or permission. |
| Verifiable credential, credential view, or register excerpt | Treat as an A.10 carrier with issuer or trust anchor, governing status register when one exists, register entry or source-record id and version, holder or subject binding, verifier, proof result, status result, currentness, relying context, validity window, revocation window, and acceptance rule. When those checks pass, it may support credential-currentness for that holder and relying context. It supports permission, authorization, role assignment, status assertion, or gate passage only when the register entry or another exact source such as `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` creates or states that effect for the bounded context. |

| Copied approval or review summary | Show the original `A.2.9` `SpeechActRef` / issuing act when approval or authorization is claimed, or the original reviewed source when only review-content currentness is claimed. Add copy relation, currentness, scope/window, evidence-producing work/event, and whether separate commitment/work support is live. Copy evidence is not approval by itself. |
| Provenance, authenticity, or attestation label | Show the bounded origin, history, build, or process claim; source episteme, source episteme publication, or source carrier; method trace or work trace; source-specific proof; carrier integrity; verifier or relying policy that accepts it for this claim or effect; and rival explanation. Provenance does not show truth, safety, approval, release, gate passage, permission, or assurance unless another exact source carries that additional claim or effect. |
| Dashboard status tile | For gate-passage or release reliance, show dashboard query/source/time/window/currentness, source order, freshness policy, rival explanation, and the current `A.21` `GateDecision` / `DecisionLogRef` with gate profile/version and release/work target; the A.10 path evidences that source chain. A status display is not gate passage or work occurrence by itself. |

| Rollback command-like cue | Show command/authorization source, actor, affected work target or claim target, scope/window, and whether the cue is only an `A.6.A` action invitation. A command cue is not execution evidence. |
| Rollback execution result | Show `A.15.1` `U.Work` occurrence, method trace or work trace, logs, outcome evidence, and time window. Execution evidence is not approval, assurance, or gate passage by itself. |
| Generated explanation | Use `E.17.EFP` to classify the explanation relation and source-finding posture. For reliance, show claim-bound attribution alignment: every operative claim relied on maps to a source passage, carrier, or exact `governingPatternRef` or `authoritySourceRef` that supports that claim in the relying context. When that mapping is complete, A.10 may support those operative claims as source-backed evidence; the explanation itself still does not issue, approve, authorize, pass a gate, evidence execution, or raise assurance. |

| Model card or datasheet used as evidence | Show documented admissible-use statement or external intended-use field, version/window, evaluation condition, limitations, evidence carriers, and whether a `B.3` assurance claim is live. Documentation does not become readiness or assurance by presence. |
| Extracted-source chain to gate or release claim | Name the source reference, the first lossy or non-commutative transform step, the FPF relation or pattern governing that transform (`A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `E.17.ID.CR`, or `E.18` where applicable), the admissible inference move after the step, the exact `governingPatternRef` or `authoritySourceRef` that carries the live claim, the source reopen trigger, and the gate claim or release claim blocked until those supports are recoverable. |
| Conflicting sources | When display, source carrier, decision log, recency signal, freshness signal, copied summary, generated summary, credential status, provenance label, or assurance evidence disagree, name the visible source, rival source, source order, decision source, freshness policy, and supersession rule. Do not choose by color, visual salience, confidence wording, copied wording, or apparent recency; the work claim or reliance claim is contested until the source-order question is resolved. |

| Sensitive evidence path | Use redacted, hashed, scoped, or role-mediated carrier refs when raw carriers expose secrets, personal data, security-sensitive traces/data, privileged logs, tenant identifiers, or unnecessary identities. Redaction does not create source support; it must preserve enough recoverability for the relying context. |
| Pointer or proof-status evidence path | Use a hash, proof verification result, status verification result, source ref, scoped pointer, disclosure receipt, or role-mediated view instead of copying raw sensitive carriers or payloads when that pointer preserves enough recoverability for the relied-on claim or effect. Do not copy raw secrets, tokens, privileged logs, personal identities, or tenant details merely to make the evidence path look fuller. |


If the path is incomplete, A.10 returns evidence-path posture and source-currentness posture, not work or reliance support for the attempted claim or effect. Valid dispositions include source-finding only, reopen original carrier, request issuer or status verification, refresh dashboard query or API query, mark stale or contested, narrow the live P2W class or reliance claim, proceed only with a reversible local probe under an explicit work plan when work is live, or block the unsupported work claim or reliance claim.


**Broken-source repair assignment.** If the relying actor cannot recover or verify the source path, assign the repair to the accountable project-side responsibility assignment: issuer or performer, verifier or status service, evidence-producing work role assignment or system, gate-decision source, role or status source, or boundary source. The A.10 result should name the missing source and blocked use rather than making the relying actor reconstruct a source they cannot issue or verify.

Role prompts for evidence or currentness use:

| Role in the situation | Prompt |
| --- | --- |
| Relying actor | Which exact claim or effect needs support, and what is the minimum carrier, source, time, and relation path for that claim or effect? |
| Issuer, verifier, or status source | Which issuer, holder, verifier, proof result, status result, currentness, revocation, or acceptance-rule source must be exposed or repaired? |
| Auditor or reviewer | Which carrier, source-maintenance role assignment, method trace or work trace, time window, evidence relation, and rival explanation must be recoverable? |
| Security source or compliance source | Which source order, supersession, proof result, status result, revocation, and minimum-disclosure posture decide this reliance question? |
| LLM/tool user | Which generated or copied operative claims map to source passages or carriers, and which claims remain only source-finding? |
| Model source or data source | Which intended-use, evaluation-condition, version, window, limitation, and evidence carriers bound the model documentation or data documentation? |

**Repeated missing-source indicator.** If the same visible-item family repeatedly returns stale, contested, no-source, or no-currentness A.10 results, record a source-system repair item: instrument the source, expose decision-source refs, add currentness checks and status checks, preserve claim-bound source links for generated or copied outputs, require credential views to show status windows and currentness windows, require model documentation and data documentation to expose intended-use and evaluation-condition fields, or require provenance labels and attestation labels to name their bounded claim type. Repetition is an indicator that the source path or display needs repair; it is not a reason to make each acting user rebuild the path manually.

Display guidance for evidence and currentness: an evidence or status display should show the claim or effect, carrier, source-maintenance role assignment, exact ref or link, time window, freshness, relying context, and unsupported action, claim, or effect. A display that can only show source availability should say so; it must not imply approval, permission, gate passage, work occurrence, or assurance.

Incident-learning fields for evidence and currentness overread: visible carrier or publication face, intended claim or effect, missing source-path field, exact carrier, source-maintenance role assignment, method trace, work trace, and time relation needed, rival explanation that made the overread plausible, current safe disposition, and upstream repair item for instrumentation, source refs, status, currentness, claim-bound source links, credential view, model documentation, data documentation, or provenance and attestation label.

Contestability and redress path: when an evidence path or currentness path affects person or team status, access, responsibility, compliance posture, or release decision, the A.10 result should name the disputed claim, carrier, source-maintenance role assignment, verifier or status source, freshness or revocation source, privacy-minimized evidence ref, safe interim disposition, and review or redress path. A disputed display remains contested until the source-order or currentness question is resolved.


**Positive repaired path.** When the source path is complete, return the smallest source-backed support statement: named claim or effect, carrier and source-maintenance role assignment, method trace or work trace, time window, currentness, evidence relation, and the exact action or reliance it supports. This lets the relying pattern proceed inside that scope without treating evidence support as approval, permission, gate passage, work occurrence, or assurance.


What this does not authorize: `A.10` does not approve, authorize action, pass a gate, release, create permission, create a commitment, assign a role, record a work occurrence, or raise assurance. It supplies the evidence path and support posture that `A.15`, `A.6`, `B.3`, `A.21` gate-decision sources, `A.20` constraint-validity sources, `A.2.9` speech-act sources, `A.2.8` commitment sources, `A.15.1` work-occurrence sources, or another exact `governingPatternRef` or `authoritySourceRef` may consume.

#### A.10:4.7 - Causal evidence support basis in evidence paths

Evidence graph paths that support causal-use claims must carry the `C.28`-governed `CausalEvidenceSupportBasis` without redefining causal estimands or causal support authority.

The `C.28` values that `A.10` may carry in an evidence path are:

```text
observationalAssociationSupportBasis
interventionalActionSupportBasis
realizedCounterfactualSampleSupportBasis
identifiedCounterfactualEstimateSupportBasis
simulationOnlyCounterfactualOutputBasis
```

`A.10` consumes this value set from `C.28`; it does not add `causalAssumptionOnlySupport` or `noCausalEvidenceSupport` as evidence-basis values. Assumption-only and no-support postures are represented by causal assumptions, support verdict, supported use, unsupported use, or abstain in `C.28`/`B.3`, not by a second evidence-basis vocabulary.

No unsupported `CausalityLadderRung` climb:

```text
observational-association evidence -> interventional-action claim requires CausalIdentificationProfile.
interventional-action evidence -> counterfactual-comparison claim requires CausalIdentificationProfile for
  identifiedCounterfactualEstimateSupportBasis, CounterfactualSamplingRealizabilityProfile for
  realizedCounterfactualSampleSupportBasis, or bounded-use treatment.
Simulation-only counterfactual output may support bounded model-supported use when model assumptions, validation, supported use, and unsupported use are declared. It does not become interventional evidence or realized counterfactual sample evidence by vocabulary, validation, or evidence-role relabeling alone.
```

Evidence-path micro-examples:

| `CausalEvidenceSupportBasis` | EPV-style path cue |
| --- | --- |
| `observationalAssociationSupportBasis` | observed cohort table -> `PathSlice` to measurement work -> association-use support statement; unsupported use = intervention-effect wording. |
| `interventionalActionSupportBasis` | randomized or governed action assignment record -> work trace -> declared intervention-effect support inside assignment, follow-up, and outcome window. |
| `realizedCounterfactualSampleSupportBasis` | counterfactual-comparison sampling work plan -> run trace -> evidence carrier -> samples from declared target counterfactual distribution under physical, ethical, and operational constraints. |
| `identifiedCounterfactualEstimateSupportBasis` | causal assumptions, graph proof, calculus proof, available-data regime set, and bound refs -> `CausalIdentificationProfile` -> estimated or bounded counterfactual use with supported use and unsupported use. |
| `simulationOnlyCounterfactualOutputBasis` | simulator output -> counterfactual model assumptions -> simulation validation ref -> bounded model-supported use; validation remains validation and does not convert the path into direct sample evidence or intervention-effect evidence. |

What changes in practice: an evidence path can show that a carrier supports a causal-use claim, but it must also show the causal evidence support basis and the relevant `C.28` support references when the claim climbs from observation to intervention or from intervention to counterfactual comparison.

What this does not authorize: `A.10` does not identify causal effects, create an estimand, certify target-trial emulation, or decide counterfactual sampling realizability; it stores and makes recoverable the evidence graph path and causal support-basis refs needed by `C.28` and `B.3`.


