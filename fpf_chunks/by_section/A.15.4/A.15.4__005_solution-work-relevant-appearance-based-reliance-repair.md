---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:3"
section_title: "Solution - Work-Relevant Appearance-Based Reliance Repair"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__005_solution-work-relevant-appearance-based-reliance-repair.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:3 — Solution - Work-Relevant Appearance-Based Reliance Repair"
line_start: 24882
line_end: 25013
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.EFP"
  - "U.Work"
keywords:
  - "allowed use now"
  - "appearance overread blocked"
  - "appearance-based reliance"
  - "claim/effect position"
  - "copied approval"
  - "credential view"
  - "dashboard display"
  - "exact permission-result relation or finding"
  - "generated explanation"
  - "project-side claim/effect reference"
  - "publication face"
  - "reliance appearance"
  - "required claim before use"
  - "required instituted effect before use"
  - "work or reliance use"
---

### A.15.4:3 - Solution - Work-Relevant Appearance-Based Reliance Repair

#### Core stress-case rule

**Ordinary local repair record.** In ordinary use, do not build a full evidence, currentness, or provenance dossier. The first useful record is:

`RelianceAppearanceRef; RelianceAppearanceKind; WorkOrRelianceUseKind; WorkOrRelianceUseRef; RequiredClaimBeforeUseRef; RequiredInstitutedEffectBeforeUseRef; ClaimOrEffectPatternRef; ClaimOrEffectPositionKind; ClaimOrEffectPositionRef; ProjectSideClaimOrEffectRef; AllowedUseNow; AppearanceOverreadBlocked; RecoveryOrStopCondition`

The reliance appearance may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source-relation chain. The pattern asks whether the work or reliance use is currently carried by a claim/effect position and project-side reference named by value, not whether the reliance appearance is impressive, fluent, easy to inspect, or visually salient.

**Conditional governing pattern and position field set.** Use the fuller fields below only when `RequiredClaimBeforeUseRef` or `RequiredInstitutedEffectBeforeUseRef` falls in release, safety, compliance, role-assignment relation, credential-status, role-state, gate, assurance, contested source relation, external reliance, cross-context reuse, currentness, revocation, generated source relation, or copied source relation. These fields are local repair aids, not a new record kind.

| Field | Working question |
| --- | --- |
| subject or actor | Who or what would perform the work, rely on the appearance, hold the credential-status or role-state, or be affected by the claim? |
| role-assignment claim | Which `U.RoleAssignment` or role-context claim is being made? |
| intended work or work target | Is the user planning intended work, relying on a dated `U.Work` occurrence or result, or making another reliance claim? Name that branch and the governing pattern before the reliance appearance guides it. |
| affected resource or claim | Which resource, claim, gate, credential, credential-status, role-state, evidence, approval, or source-finding pointer with authority-reference relation is supposedly affected? |
| context | Which bounded context, environment, project slice, API setting, connector setting, protocol setting, or relying situation makes the claim applicable? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition is supposed to govern the claim? |
| time window | During which window is the claim, effect, source relation, or recovered-use boundary claimed to hold? |
| currentness or revocation field | Is the source relation current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or governing reference | Which issuer, project reference, register entry, source-currentness or credential-status record, speech act, gate decision, evidence relation, or work-occurrence record is required by the governing pattern for the current use? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation relation | Which `A.10` evidence, provenance, or attestation relation, if any, justifies the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceRelationClass | Which `E.17:5.1b` source-relation class or claim-use class applies to the reliance appearance and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, governing value, or downstream effect remains unsupported and needs narrowing, repair, reopening, probing, or blocking? |

Start with the A.15.4 first repair checks above when the reliance appearance is being used as a reason for intended work, reliance, or a work-relevant claim. If the issue under repair is only evidence, currentness, gate-passage claim, `ConstraintValidity` status, engineering justification, commitment, exact permission result, speech act, boundary wording, use-boundary wording, credential proof, source-currentness proof, credential-status proof, explanation, comparison, or publication-carrier or front-end behavior, use the pattern governing that issue directly, including `A.2.8.PER` for the permission result. Use A.15.4 only when the governing pattern position and project-side reference must be recovered before role assignment, method, plan, work, work result, result measurement, or another work or reliance claim can proceed.

**When a reliance appearance seems to authorize work or reliance.** Use A.15.4 when a publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for intended work or reliance. This is a recognition moment, not a new kind. The repair question remains: what does the user intend to do next, what claim or effect would make that intended work or reliance admissible, and which governing pattern position and project-side reference are required for it?

Here "authority-looking case" is only a recognition phrase for the encountered situation. The record, relation, slot filler, or project-side reference that authorizes, forbids, records, or carries the required relation is named by value under its FPF pattern. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to another governing pattern.

The central behaviour is: name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair; name the governing pattern position and project-side reference that carry the required claim, effect, work occurrence, or currentness value; keep the `U.Episteme` or `U.EpistemePublication` distinct from publication form, MVPK face, publication carrier, rendering, and source-finding cue; choose the minimum sufficient recovered use; and do not raise the claim beyond the recovered relation, source relation, or recovered use boundary. If the named project record states the governing FPF relation, use that recorded relation directly rather than inferring it from wording.

**Positive repaired disposition.** An encountered `U.Episteme` publication, publication form, MVPK face, publication carrier, rendering, or source-finding cue may guide work or reliance only to the claim or effect carried by the recovered governing pattern position, acting holder, work-performing system, agent, `RoleAssignmentRef` when role-conditioned attribution is current, work or reliance claim under repair, work-relevant P2W claim under repair, P2W chain position under repair, affected work target, context, window, and project-side reference. The repaired outcome says what may happen next and which unsupported work claim or reliance claim stays blocked.

Reliance dispositions by recovered governing pattern relation:

| Work or reliance disposition | Use when | Minimum useful record |
| --- | --- | --- |
| Orientation or source-finding note | The reliance appearance is only a publication face, publication carrier, rendering, cue, retrieval cue, learning aid, or reversible local probe trigger. | `RelianceAppearanceRef; RelianceAppearanceKind; WorkOrRelianceUseKind; WorkOrRelianceUseRef; RequiredClaimBeforeUseRef or RequiredInstitutedEffectBeforeUseRef when current; ClaimOrEffectPatternRef; ClaimOrEffectPositionKind; ClaimOrEffectPositionRef; ProjectSideClaimOrEffectRef; AllowedUseNow; AppearanceOverreadBlocked; RecoveryOrStopCondition`. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated role-assignment claim, role-state claim, credential-status claim, contested source relation, or cross-context reuse. | Work or reliance use, required claim when current, instituted effect when current, acting holder, work-performing system, or agent; `RoleAssignmentRef` when role-conditioned authority or work attribution is current; affected work target, context, effective window; governing pattern position or project-side source relation exposed by the reliance appearance; and reopen trigger. |
| High-impact reliance disposition | The required claim or instituted effect is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, role-state-claim-bearing, credential-status-claim-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context. | Governing pattern and position field set with the `A.10`, `A.6`, `B.3`, `A.2.9`, `A.2.8`, `A.2.8.PER`, `A.21`, `A.20`, or `A.15.1` fields required for that exact claim or effect. |

A small A.15.4 local repair record is enough for the first disposition:

| Field | Value |
| --- | --- |
| `RelianceAppearanceRef` | Name the appearance being relied on by value, such as the dashboard tile, credential view, copied text, generated explanation, publication face, publication carrier, rendering, or source-finding cue. |
| `RelianceAppearanceKind` | Name the kind without granting authority by appearance: actual `U.Episteme`, actual `U.EpistemePublication`, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. |
| `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` | Name the use being justified by value: intended work, reliance on a claim, reliance on a dated `U.Work` occurrence, method-family selection, selected method, method of work, work plan, planned work, work result, result measurement, release reliance decision, non-work reliance claim, work-relevant P2W claim, or P2W chain position. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record; performed work becomes `U.Work` only after it occurs and is recorded under `A.15.1`; work-result measurement belongs with the evidence relation or result-measurement record that carries it. |
| `RequiredClaimBeforeUseRef` | Fill when a claim must be carried by a governing pattern before the work or reliance use is admissible. Leave empty when the current reliance is only on an instituted effect. |
| `RequiredInstitutedEffectBeforeUseRef` | Fill when an effect must be carried by a governing pattern before the work or reliance use is admissible, such as approval act effect, gate passage, role-state change, credential-status effect, commitment, or speech-act effect. Leave empty when the current reliance is only on a claim. |
| `ClaimOrEffectPatternRef` | Name the direct FPF pattern that carries the required claim, required instituted effect, relation, slot filler, or source-currentness value. |
| `ClaimOrEffectPositionKind` and `ClaimOrEffectPositionRef` | Name the position kind explicitly, such as slot, relation record, project reference, source-currentness relation, gate decision, evidence relation, speech-act ref, commitment ref, role-assignment ref, role-state record, credential-status record, or work-occurrence ref. Then name the exact position or relation to inspect. |
| `ProjectSideClaimOrEffectRef` | Name the project-side FPF reference that must be current for the work or reliance use. |
| `AllowedUseNow` | State the safe current use: orientation, source-finding, cue-pack preservation, bounded reversible probe, narrowed reliance, governing-position repair request, proceed-inside-recovered-relation, or blocked unsupported use. |
| `AppearanceOverreadBlocked` | State the overread being blocked, such as treating display color as gate passage, copied approval as a current speech act, a credential screenshot as permission, or a generated explanation as evidence. |
| `RecoveryOrStopCondition` | State what blocks the work or reliance use and what would reopen it. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `A.16.0` distinction rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`; `U.EpistemePublication` is used only when that episteme is available as a published episteme with MVPK-face references. Publication forms, MVPK faces, publication carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or relation positions in the case. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record such as `SlotFillingsPlanItem`; launch values and finalization values remain their own project records, decision logs remain gate or decision records, performed-work evidence remains evidence, and dated work occurrences remain `A.15.1` or `U.Work` matters.

When the governing pattern position is incomplete, choose one relation-governed `A.15.4` disposition after naming the work or reliance use and the governing pattern position required for the required claim or instituted effect; pick the lightest disposition that preserves practical work and recoverability:

1. Use the reliance appearance only for orientation or source-finding.
2. Reopen the source `U.Episteme` for the current claim, the `U.EpistemePublication` that exposes the claim-bound source relation, register entry, governing record, or governing relation, or refresh source-currentness, credential-status, role-state, context-state, or another currentness relation.
3. Narrow the acting holder, work-performing system, agent, `RoleAssignmentRef` when current, requested operation or work class, affected work target, affected resource, affected claim, context, and effective window until the recovered record or relation really covers the recovered use.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Ask the holder, work-performing system, maintainer, verifier, issuer, or project role holder identified by the relevant `RoleAssignmentRef` or governing pattern relation to expose or repair the missing governing pattern position. `ClaimOrEffectPositionKind` may be a slot, record, or relation for the issuer, gate decision, evidence relation, role-assignment record, role-state record, credential-status record, context-state record, source-currentness relation, or boundary claim set.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source-relation link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks the required relation.

#### Repair assignment rule

**Missing record or relation repair assignment.** If the required governing record or relation is unavailable to the acting user, assign only prospective repair work, request work, decision work, work-plan work, or source-relation gap work to the holder, work-performing system, maintainer, verifier, or project role holder identified by the relevant `RoleAssignmentRef` or governing pattern relation for the missing relation. The acting user records the blocked work claim or reliance claim, the missing relation, and the safe narrowed use now.

**Reliance-appearance kind check.** First name the actual kind of the reliance appearance: actual `U.Episteme`, actual `U.EpistemePublication`, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. If the appearance exposes the governing record or relation, use that exposed value directly. If only the display face, publication carrier, wording, or cue is named, the A.15.4 disposition is orientation, source-finding, bounded reversible probe, repair request, or blocked unsupported reliance until the source relation named by value is recovered.

**Source-relation guard.** Release urgency, delegated-claim urgency, compliance concern, color, salience, copied wording, or generated wording does not replace the source relation named by value. A dashboard tile may guide release only as a current view of the relevant `GateDecision` plus evidence relation, currentness relation, scope, and window.

#### Governing-position lookup table

Governing patterns by required claim or effect kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.
- issuing, approval, authorization, delegation, or revocation act: cite `A.2.9` `U.SpeechAct` or `SpeechActRef`, including act type, acting holder, work-performing system, or agent, `RoleAssignmentRef` when role-conditioned authority is claimed, affected work target or claim, judgement context, window, publication-carrier reference, evidence reference when currentness matters, and instituted effects if claimed. Because `U.SpeechAct <: U.Work`, it can evidence only that communicative act.
- strong or weak permission, actual permission exercise, non-violation, or permission conflict: cite the exact `A.2.8.PER` relation occurrence or finding, including beneficiary/action content, policy/context, scope/window, currentness, and instituting `SpeechActRef` for a strong grant.
- obligation, prohibition, or recommendation-as-duty: cite `A.2.8 U.Commitment` and the instituting `SpeechActRef` when provenance matters. If the word instead names a use boundary, gate passage, authorization act, role/status effect, credential-status effect, cue, or advice, use that direct pattern.
- role-assignment, role-state, credential-status, or context-state reliance: cite `A.2.1`, `U.RoleAssignment`, a state-changing `U.SpeechAct`, a governing context-state record, a credential proof or credential-status result under `A.10`, or an `A.21` `GateDecision` when the state is gate-governed.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`; use `A.6.C`, `A.2.3`, `A.2.8`, `A.2.8.PER`, and `A.2.9` for agreement-like guarantee, SLA, promise, commitment, permission, or issuing-act wording before intended work or reliance.
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins.
- Flow constraint-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim.
- release, deployment, repair, inspection, or rollback work occurrence: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence or provenance relation when reliance on occurrence is needed.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: apply `A.10` and name the claim-bound evidence relation, currentness relation, and relation-governed or blocked use.
- assurance, safety, compliance, trust, release confidence, or `R`, `F`, `G`, or `CL` increase: apply `B.3` and name the typed assurance claim plus its limitations and reopen condition. If the word `ready` names full-kit or work-entry readiness, use `A.15.5`; if it names a gate decision, use `A.21`.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source relation for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: choose among the rows above named by value by asking what effect is claimed now: issuing speech act, `U.Commitment`, exact `A.2.8.PER` grant/finding/exercise/conflict result, claimed use boundary or entry predicate, gate passage, role-assignment effect, role-state change, credential-status change, evidence relation, assurance claim, or work occurrence.

Recovered governing pattern outputs for A.15.4 closure:
| Governing pattern or relation used | Recovered output for this A.15.4 repair | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the pattern that governs the current boundary claim or the current effect-bearing claim. | Use for wording, boundary, API, schema, or use-boundary recovery before intended work or reliance. |
| `A.10` | Claim-bound evidence relation, freshness field, currentness field, and relation-governed or blocked use for the attempted claim. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the work or reliance claim under repair relies on a typed assurance claim. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidity` status, witness, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim. | Use for flow constraint-validity reliance. |
| `A.2.9` | `SpeechActRef` with act type, acting holder, work-performing system, or agent, `RoleAssignmentRef` when role-conditioned authority is claimed, affected work target or claim, judgement context, window, and instituted effects if claimed. | Use for issued acts and, where needed, dated occurrence of that communicative act. |
| `A.2.8.PER` | Exact `GrantedPermissionRelation@Context`, `PermissionExerciseRelation@Context`, `NonProhibitionFinding@Context`, `NonViolationFinding@Context`, or `PermissionNormConflictFinding@Context`, with the fields required by that object. | Use for strong/weak permission, actual exercise, non-violation, or conflict. |
| `A.2.8` | `U.Commitment` deontic relation with accountable holder, work-performing system, or agent; `RoleAssignmentRef` when role-conditioned accountability is claimed; referents, modality, scope, effective window, and instituting `SpeechActRef` or source relation when needed. | Use for obligation, prohibition, or recommendation-as-duty. |
| `A.15.1` | Dated `U.Work` occurrence plus `A.10` evidence or provenance relation when relied on. | Use for reliance on performed work. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the source `U.Episteme` or the `U.EpistemePublication` exposing that source relation. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

High-impact work or reliance - especially external-impact, irreversible, release-bearing, role-assignment-bearing, role-state-claim-bearing, credential-status-claim-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - may guide work only for the acting holder, work-performing system, or agent, the `RoleAssignmentRef` when role-conditioned capacity or attribution is current, the work or reliance claim under repair, work-relevant P2W claim under repair, P2W chain position under repair, affected work target or claim, audience, scope, environment, version, policy context, operational mode, and time window for which the required FPF-governed project-side source relation, evidence relation, gate decision, or assurance claim is recoverable. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full evidence, currentness, or provenance dossier.
Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Release dashboard tile exposing a source relation | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release scope or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence relation, it may carry gate-passage reliance for that release and environment. |
| Release dashboard tile without current gate or evidence relation | Use the tile only for display or source-finding until the current `A.21` `GateDecision` or `DecisionLogRef`, release scope or work target, environment or scope, time window, gate profile, gate version, and `A.10` evidence relation are recoverable. Open `B.3` only when an assurance claim is being made. |
| Copied review summary or copied approval | Copied wording and copied-currentness cue at most; approval or authorization needs the original `A.2.9 SpeechActRef`, gate passage the `A.21` decision, strong/weak permission or exercise/conflict the exact `A.2.8.PER` result, a duty/recommendation/prohibition commitment the `A.2.8` object, and work occurrence the dated `A.15.1 U.Work`, each with the required `A.10` evidence or provenance/currentness relation. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work target, affected resource, affected claim, scope, window, the delegation record or relation permitting delegation, subdelegation allowance if any, revocation relation, currentness relation, and evidence relation. A forwarded approval is not delegated authority by copy alone. |
| Role-assignment, revocation, role-state, or credential-status display | Resolve to role assignment, state-changing speech act, context-state record, credential proof or credential-status result, or gate decision with freshness field, revocation relation, or revocation record; visual display cannot defeat a higher-priority revocation or supersession relation. |
| Conflicting source relations | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source-relation order, governing decision record, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed credential-status view | Use the display as a publication of a credential record, credential-status record, or role-state record, not the record or relation itself. Find the governing credential-status register, role-state register, or issuer, trust root, holder binding or subject binding, verifier context, relying context, proof or credential-status result, revocation, freshness, and effective window. If the governing register entry itself creates or changes role assignment or role state, cite `A.2.1`; for strong/weak permission, exercise, non-violation, or conflict cite `A.2.8.PER`; for an actual duty/recommendation/prohibition cite `A.2.8`; for the issuing act cite `A.2.9`; for an entry predicate cite `A.6.B`; and for a gate effect cite `A.21`, all named by value. Otherwise rely only on credential-currentness for that holder and context. |
| Rollback command-like cue | Treat as cue or `A.6.A`-governed invitation unless command record, authorization, work occurrence, performed-work result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Explanation may help find source `U.EpistemePublication` refs, claim-bound source relations, or governing pattern positions; it does not issue, approve, revoke, commit, authorize, pass a gate, provide evidence for performed work, or raise assurance. A citation or source mention inside the explanation guides intended work or reliance only when the cited publication carrier carries that relied-on claim named by value in the relying context under `A.10`. |
| Extracted source publication, rewrite, representation shift, explanation, then gate or release claim | Return to the source `U.EpistemePublication`, source-bearing relation, transform record, evidence relation, explanation relation, or governing pattern position at the first lossy or non-commutative transformation operation; the gate claim or release claim waits for the required transform record, evidence relation, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-relation repair work: expose decision refs, fix dashboard semantics, add claim-bound source relations and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

