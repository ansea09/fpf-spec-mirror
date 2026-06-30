---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Source Restoration"
section_id: "A.15.4:3"
section_title: "Solution - Work-Relevant Source Restoration"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__005_solution-work-relevant-source-restoration.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.15.4 — Work-Relevant Source Restoration"
  - "A.15.4:3 — Solution - Work-Relevant Source Restoration"
line_start: 22823
line_end: 22948
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.2.1"
  - "E.17"
  - "E.17.EFP"
  - "U.Work"
keywords:
  - "P2W load and position"
  - "approval-looking display"
  - "blocked overread"
  - "copied statement"
  - "credential view"
  - "dashboard display"
  - "generated explanation"
  - "provenance mark"
  - "relation-governed current use"
  - "required project-side FPF kind and reference"
  - "work-relevant source restoration"
---

### A.15.4:3 - Solution - Work-Relevant Source Restoration

#### Core stress-case rule

**Ordinary source-restoration note.** In ordinary use, do not build a source dossier. The first useful note is:

`encounteredSourceCandidate; work or reliance claim under repair; claim or effect needed; governing source needed; current relation-governed use; blocked overread; stop or reopen condition`

The encountered source candidate may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source chain. The pattern asks whether the requested claim is currently carried by a project-side source named by value, not whether the source candidate is impressive, fluent, easy to inspect, or visually salient.

**Conditional source-relation field set.** Use the fuller fields below only when release, safety, compliance, role assignment, credential-status, role-state, gate, assurance, contested source, external reliance, cross-context reuse, currentness, revocation, generated source relation, or copied source relation is being relied on for the claim under repair. These fields are local restoration aids, not a new record kind.

| Field | Working question |
| --- | --- |
| subject or actor | Who or what would perform the work, rely on the source candidate, hold the credential-status or role-state, or be affected by the claim? |
| role-assignment claim | Which `U.RoleAssignment` or role-context claim is being made? |
| guided work use or work target | Which selected method, method of work, `U.WorkPlan`, planned work, dated `U.Work`, work result, release reliance, reliance use, source-currentness, credential-status, or effect is being guided? |
| affected resource or claim | Which resource, claim, gate, credential, credential-status, role-state, evidence, approval, or source finding with authority-reference relation is supposedly affected? |
| context | Which bounded context, environment, project slice, API setting, connector setting, protocol setting, or relying situation makes the claim applicable? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition is supposed to govern the claim? |
| time window | During which window is the claim, effect, source relation, or recovered-use boundary claimed to hold? |
| currentness or revocation field | Is the source relation current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or source | Which issuer, governing source, register source, source-currentness or credential-status record, speech act, gate decision, evidence relation, or work-occurrence record carries the claim, effect, source relation, or recovered-use boundary? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation relation | Which `A.10` evidence, provenance, or attestation relation, if any, justifies the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceRelationClass | Which `E.17:5.1b` source-relation class or claim-use class applies to the encountered source candidate and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, or downstream effect remains unsupported and needs narrowing, repair, reopening, probing, or blocking? |

Start with the A.15.4 first restoration checks above when the encountered source candidate is about to guide a work use, reliance use, or work-relevant claim. If the issue under repair is only evidence, currentness, gate-passage claim, `ConstraintValidity` status, engineering justification, commitment, speech act, boundary wording, use-boundary wording, credential proof, source-currentness proof, credential-status proof, explanation, comparison, or publication-carrier or front-end behavior, use the pattern governing that issue directly. Use A.15.4 only when source restoration is needed before role assignment, method, plan, work, work result, result measurement, or another work use or reliance use can proceed.

**Authority-looking source-backed work or reliance case.** Use A.15.4 when an approval-, permission-, gate-, command-, credential-, delegation-, revocation-, role-state-, credential-status-, provenance-, dashboard-, copied-review-, generated-explanation-, schema-, API-, or composed-chain case is about to be used as a work cue, reliance claim source, release-reliance claim source, performed-work evidence source, approval-claim source, approval-effect source, role-assignment-claim source, role-state-claim source, credential-status-claim source, or work-relevant source cue. The recognition moment is that an encountered publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for starting work. The repair question remains: which work or reliance claim is being made, and which source is required for it?

Here "authority-looking case" is only a recognition phrase for the encountered situation. The governing source that authorizes, forbids, records, or carries the work-relevant claim may instead be a `GateDecision`, `SpeechAct`, `U.Commitment`, `U.RoleAssignment`, credential record, role-state record, credential-status record, context-state record, `A.6.B`-claim being made, `A.10` evidence relation, or `B.3` assurance claim. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, work claim, reliance claim, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to another governing pattern.

The central behaviour is: name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair; name the source that carries the needed claim or effect; keep the `U.Episteme` or `U.EpistemePublication` distinct from publication form, MVPK face, publication carrier, rendering, and source-finding cue; choose the minimum sufficient recovered use; and do not raise the claim beyond the recovered relation, source relation, or recovered use boundary. If the named project record states the governing FPF relation, use that recorded relation directly rather than inferring it from wording.

**Positive repaired disposition.** An encountered `U.Episteme` publication, publication form, MVPK face, publication carrier, rendering, or source-finding cue may guide work or reliance only to the claim or effect carried by the recovered source, actor or role assignment, work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair, affected work target, context, window, and source-recoverable claim or effect. The repaired outcome is the smallest relation-governed work or reliance statement plus the unsupported work claim or reliance claim still blocked.

Reliance dispositions by recovered source relation:

| Work or reliance disposition | Use when | Minimum useful record |
| --- | --- | --- |
| Orientation or source-finding note | The encountered source candidate is only a publication face, publication carrier, rendering, cue, retrieval cue, learning aid, or reversible local probe trigger. | `encounteredSourceCandidate; required claim or effect not yet carried by a recovered source; source to reopen; stop condition`. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated role-assignment claim, role-state claim, credential-status claim, contested source, or cross-context reuse. | Work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair; required claim or effect; actor or role assignment; affected work target, context, effective window; source reference exposed by the encountered source candidate; and reopen condition. |
| High-impact reliance disposition | The required claim or effect is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, role-state-claim-bearing, credential-status-claim-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context. | Governing source with the `A.10`, `A.6`, `B.3`, `A.2.9`, `A.2.8`, `A.21`, `A.20`, or `A.15.1` fields needed for that claim or effect. |

A small A.15.4 restoration note is enough for the first disposition:

| Field | Value |
| --- | --- |
| work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair | Name the claim or P2W chain position by value: method-family selection, selected method, method of work, work plan, planned work, dated `U.Work` occurrence, work result, result-measurement, release reliance decision, or non-work reliance claim. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record; performed work becomes `U.Work` only after it occurs and is recorded under `A.15.1`; work-result measurement belongs with the evidence or result-measurement source. This row is a local restoration label unless it cites an existing FPF kind or governing FPF relation. |
| governing source needed | Approval act, deontic permission, gate passage, role-assignment relation, role-state or credential-status currentness, work occurrence, evidence relation, assurance claim, boundary claim, or other claim named by value or effect needed before that work claim, reliance claim, or P2W chain-position claim can be treated as carried by a recovered source. The governing relation is carried by the named FPF pattern and recovered project-side reference, not by a new `A.15.4` kind. |
| actor or role assignment | Who would act or rely, and which `U.RoleAssignment` matters when the acting capacity is part of the claim. |
| affected work target, context, and window | Release, service, person, role-assignment holder, work target, claim, tenant, environment, physical batch, construction element, machine state, or effective window affected by that class or claim. |
| claim-bearing episteme or episteme publication | The claim-bearing FPF kind is `U.Episteme` or a species such as `U.EpistemePublication`; if the encountered source candidate is only a publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, copied text, credential view, generated explanation, API wording, or cue, name that kind named by value separately. |
| source needed or safe current use | Source `U.Episteme`, source `U.EpistemePublication`, register entry, governing source, source-currentness value, credential-status value, role-state value, reversible probe, role assignment accountable for exposing or repairing the missing source, or narrower relation-governed use. |
| stop or reopen condition | What blocks the work claim or reliance claim and what would reopen it. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `A.16.0` distinction rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`; `U.EpistemePublication` is used only when that episteme is available as a published episteme with MVPK-face references. Publication forms, MVPK faces, publication carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or relation positions in the case. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record such as `SlotFillingsPlanItem`; launch values and finalization values remain their own project records, decision logs remain gate or decision records, performed-work evidence remains evidence, and dated work occurrences remain `A.15.1` or `U.Work` matters.

When the required source is incomplete, choose one relation-governed source-restoration disposition after naming the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair and the source required for that claim or effect; pick the lightest disposition that preserves practical work and source recoverability:

1. Use the encountered source candidate only for orientation or source-finding.
2. Reopen the required source `U.Episteme`, source `U.EpistemePublication`, register entry, or governing source, or refresh source-currentness, credential-status, role-state, context-state, or another currentness relation.
3. Narrow actor and role assignment, requested operation or work class, affected work target, affected resource, affected claim, context, and effective window until the recovered source really covers the recovered use.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Ask the role assignment accountable for the issuer, gate decision, evidence relation, role-assignment record, role-state record, credential-status record, context-state record, source-currentness relation, or boundary claim set to expose or repair the missing source.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks source relation.

#### Repair assignment rule

**Broken-source repair assignment.** If the required governing source is unavailable to the acting user, assign only prospective repair work, request work, decision work, work-plan work, or source-gap work to the role assignment accountable for the missing source relation. The acting user records the blocked work claim or reliance claim, the missing source relation, and the safe narrowed use now.

**Source-candidate kind check.** First name the kind of the encountered source candidate: actual `U.Episteme`, actual `U.EpistemePublication`, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. If the source candidate exposes the governing source, use that exposed source directly. If only the display face, publication carrier, wording, or cue is named, the A.15.4 disposition is orientation, source-finding, bounded reversible probe, source-repair request, or blocked unsupported reliance until the source relation named by value is recovered.

**Source-relation guard.** Release urgency, delegated-claim urgency, compliance concern, color, salience, copied wording, or generated wording does not replace the source relation named by value. A dashboard tile may guide release only as a current view of the relevant `GateDecision` plus evidence relation, currentness relation, scope, and window.

#### Governing-source lookup table

Governing sources by required claim or effect kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.
- issuing, approval, authorization, delegation, or revocation act: cite `A.2.9` `U.SpeechAct` or `SpeechActRef`, including act type, actor and role assignment if claimed, affected work target or claim, judgement context, window, publication-carrier reference, evidence reference when currentness matters, and instituted effects if claimed. Because `U.SpeechAct <: U.Work`, it can evidence only that communicative act.
- deontic permission, obligation, prohibition, or recommendation-as-duty: cite `A.2.8` `U.Commitment` and the instituting `SpeechActRef` when provenance matters. If the word instead names claimed use boundary, gate passage, authorization act, role-assignment effect, role-state effect, credential-status effect, cue, or advice, use the pattern that carries that kind named by value.
- role-assignment, role-state, credential-status, or context-state reliance: cite `A.2.1`, `U.RoleAssignment`, a state-changing `U.SpeechAct`, a governing context-state record, a credential proof or credential-status result under `A.10`, or an `A.21` `GateDecision` when the state is gate-governed.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`; use `A.6.C`, `A.2.3`, `A.2.8`, and `A.2.9` for agreement-like guarantee, SLA, or promise wording before work use or reliance use.
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins.
- Flow constraint-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim.
- release, deployment, repair, inspection, or rollback work occurrence: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence or provenance relation when reliance on occurrence is needed.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: apply `A.10` and name the claim-bound evidence relation, currentness relation, and relation-governed or blocked use.
- assurance, safety, compliance, trust, release confidence, or `R`, `F`, `G`, or `CL` increase: apply `B.3` and name the typed assurance claim plus its limitations and reopen condition. If the word `ready` names full-kit or work-entry readiness, use `A.15.5`; if it names a gate decision, use `A.21`.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source relation for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: choose among the rows above named by value by asking what effect is claimed now: speech act, commitment, claimed use boundary, gate passage, role-assignment effect, role-state change, credential-status change, evidence relation, assurance claim, or work occurrence.

Recovered source outputs for A.15.4 closure:
| Governing source relation used | Recovered output for this A.15.4 restoration | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the pattern that governs the claim being made or effect and the governing source for that claim or effect. | Use for wording, boundary, API, schema, or use-boundary recovery before work or reliance use. |
| `A.10` | Claim-bound evidence relation, freshness field, currentness field, and relation-governed or blocked use for the attempted claim. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the work or reliance claim under repair relies on a typed assurance claim. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidity` status, witness, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim. | Use for flow constraint-validity reliance. |
| `A.2.9` | `SpeechActRef` with act type, actor and role assignment if claimed, affected work target or claim, judgement context, window, and instituted effects if claimed. | Use for issued acts and, where needed, dated occurrence of that communicative act. |
| `A.2.8` | `U.Commitment` deontic relation with accountable role assignment, agent, referents, modality, scope, effective window, and instituting source when needed. | Use for deontic permission, obligation, prohibition, or recommendation-as-duty. |
| `A.15.1` | Dated `U.Work` occurrence plus `A.10` evidence or provenance relation when relied on. | Use for reliance on performed work. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the source `U.Episteme` or source `U.EpistemePublication`. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

High-impact work or reliance - especially external-impact, irreversible, release-bearing, role-assignment-bearing, role-state-claim-bearing, credential-status-claim-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - may guide work only for the actor and role assignment, work or reliance claim under repair, work-relevant P2W claim under repair, P2W chain position under repair, affected work target or claim, audience, scope, environment, version, policy context, operational mode, and time window for which the required FPF-governed project source, relation, evidence relation, gate decision, or assurance claim is recoverable. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full source dossier.
Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Source-backed release dashboard tile | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release scope or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence relation, it may carry gate-passage reliance for that release and environment. |
| Unsourced or stale release dashboard tile | Display or source-finding only until the current `GateDecision` or `DecisionLogRef`, release scope or work target, scope, window, gate profile, gate version, and `A.10` evidence relation are recoverable; use `B.3` only if an assurance claim is being made. |
| Copied review summary or copied approval | Copied wording and copied-currentness cue at most; approval, authorization, deontic permission, commitment, or work occurrence needs the original `A.2.9` `SpeechActRef`, `A.21` decision, `A.2.8` commitment, or `A.15.1` work source plus `A.10` evidence. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work target, affected resource, affected claim, scope, window, source permitting delegation, subdelegation allowance if any, revocation source, currentness source or currentness relation, and evidence relation. A forwarded approval is not delegated authority by copy alone. |
| Role-assignment, revocation, role-state, or credential-status display | Resolve to role assignment, state-changing speech act, context-state record, credential proof or credential-status result, or gate decision with freshness field, revocation source, or revocation record; visual display cannot defeat a higher-priority revocation or supersession source. |
| Conflicting sources | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source order, governing decision source, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed credential-status view | Use the display as a publication of a credential source, credential-status source, or role-state source, not the source itself. Find the governing credential-status register, role-state register, or issuer, trust root, holder binding or subject binding, verifier context, relying context, proof or credential-status result, revocation, freshness, and effective window. If the governing register entry itself creates or changes role assignment, role-state, deontic permission, duty, or gate effect in the bounded context, cite that register or status-source entry named by value and the `A.2.1`, `A.2.8`, `A.2.9`, `A.6.B`, or `A.21` source it depends on. Otherwise rely only on credential-currentness for that holder and context. |
| Rollback command-like cue | Treat as cue or `A.6.A`-governed invitation unless command record, authorization, work occurrence, performed-work result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Explanation may help find sources; it does not issue, approve, revoke, commit, authorize, pass a gate, provide evidence for performed work, or raise assurance. A citation or source mention inside the explanation guides work use or reliance use only when the cited publication carrier carries that relied-on claim named by value in the relying context under `A.10`. |
| Extracted source, rewrite, representation shift, explanation, then gate or release claim | Reopen the governing source at the first lossy or non-commutative transform step; the gate claim or release claim waits for the required transform record, evidence relation, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-relation repair work: expose decision refs, fix dashboard semantics, add source links and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

