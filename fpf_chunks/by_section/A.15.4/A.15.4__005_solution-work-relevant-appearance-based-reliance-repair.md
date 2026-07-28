---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:3"
section_title: "Solution - Work-Relevant Appearance-Based Reliance Repair"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__005_solution-work-relevant-appearance-based-reliance-repair.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:3 — Solution - Work-Relevant Appearance-Based Reliance Repair"
line_start: 25588
line_end: 25723
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
keywords:
  - "allowed or blocked use"
  - "appearance-based reliance"
  - "copied approval"
  - "credential"
  - "dashboard"
  - "exact attempted use"
  - "generated explanation"
  - "governing pattern and direct object"
  - "independent required-position rows"
  - "orientation and source-finding"
  - "project-side reference"
  - "publication face"
---

### A.15.4:3 - Solution - Work-Relevant Appearance-Based Reliance Repair

#### Core stress-case rule

**Ordinary local repair record.** In ordinary use, do not build a full evidence, currentness, or provenance dossier. The first useful record is:

`RelianceAppearanceRef; RelianceAppearanceKind; WorkOrRelianceUseKind; WorkOrRelianceUseRef; RequiredPositionEntries; AllowedUseNow; AppearanceOverreadBlocked; RecoveryOrStopCondition`

The reliance appearance may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source-relation chain. The pattern asks whether every direct object required by the attempted use resolves and meets its owner-defined posture and currentness conditions, not merely whether a project-side reference is named or the reliance appearance is impressive, fluent, easy to inspect, or visually salient.

**Conditional governing pattern and position field set.** Use the fuller fields below only when the attempted use is release-, safety-, compliance-, gate-, or other high-impact reliance, or when any `RequiredPositionEntries` row identifies role assignment, credential status, role state, assurance, contested/external/cross-context reliance, currentness, revocation, generated or copied source relation, or another prerequisite whose owner requires those details. Select the depth from the attempted use and typed rows, not from a parallel claim/effect field. These fields are local repair aids, not a new record kind.

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

Start with the A.15.4 first repair checks above when the reliance appearance is being used as a reason for intended work, reliance, or a work-relevant claim. If the direct question is already known, use the §3 lookup and go straight to its owner; permission or authority uses the single branch there. Use A.15.4 only when the governing pattern position and project-side reference must still be recovered before role assignment, method, plan, work, work result, result measurement, or another work or reliance claim can proceed.

**When a reliance appearance seems to authorize work or reliance.** Use A.15.4 when a publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for intended work or reliance. This is a recognition moment, not a new kind. The repair question remains: what does the user intend to do next, what claim or effect would make that intended work or reliance admissible, and which governing pattern position and project-side reference are required for it?

Here "authority-looking case" is only a recognition phrase for the encountered situation. The record, relation, slot filler, or project-side reference that authorizes, forbids, records, or carries the required relation is named by value under its FPF pattern. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to another governing pattern.

The central behaviour is: name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair; name the governing pattern position and project-side reference that carry the required claim, effect, work occurrence, or currentness value; keep the `U.Episteme` or `U.EpistemePublication` distinct from publication form, MVPK face, publication carrier, rendering, and source-finding cue; choose the minimum sufficient recovered use; and do not raise the claim beyond the recovered relation, source relation, or recovered use boundary. If a project record names a governing relation, follow its typed ref to the direct owner and test obtaining, required result posture, currentness, scope, and evidence for this attempted use; the record's statement does not make the relation obtain.

**Positive repaired disposition.** First name the attempted use and open each prerequisite through its typed ref. The appearance may guide that use beyond orientation only after every referenced relation actually obtains or result passes its owner-defined criterion, is current, covers this beneficiary/action/target/scope/window, and has the evidence or source relation required for this reliance. When a relevant permission/norm conflict exists, its separate finding row must be current and settled for this use; an `unresolved` or norm-selecting disposition blocks the use without rewriting grant currentness. Then write what may happen next. The first failed row keeps only that unsupported work or reliance use blocked.

Reliance dispositions by recovered governing pattern relation:

| Work or reliance disposition | Use when | Minimum useful record |
| --- | --- | --- |
| Orientation or source-finding note | The reliance appearance is only a publication face, publication carrier, rendering, cue, retrieval cue, learning aid, or reversible local probe trigger. | Name the appearance and exact attempted use, then add one `RequiredPositionEntries` row for the first missing direct object. Keep `AllowedUseNow`, the blocked overread, and the recovery or stop condition explicit. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated role-assignment claim, role-state claim, credential-status claim, contested source relation, or cross-context reuse. | Name the work or reliance use and only the `RequiredPositionEntries` rows it actually depends on, plus acting holder, work-performing system, or agent when current; `RoleAssignmentRef` when role-conditioned authority or work attribution is current; affected target, context, effective window; `AllowedUseNow`; and reopen trigger. |
| High-impact reliance disposition | The attempted use is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, role-state-claim-bearing, credential-status-claim-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context; or one typed prerequisite row has that owner's high-impact conditions. | Use the governing fields required by the attempted use and those exact `RequiredPositionEntries` rows. When permission or authority is current, choose exactly one row in the §3 branch rather than copying its owner catalogue here. |

A small A.15.4 local repair record is enough for the first disposition:

| Field | Value |
| --- | --- |
| `RelianceAppearanceRef` | Name the appearance being relied on by value, such as the dashboard tile, credential view, copied text, generated explanation, publication face, publication carrier, rendering, or source-finding cue. |
| `RelianceAppearanceKind` | Name the kind without granting authority by appearance: actual `U.Episteme`, actual `U.EpistemePublication`, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. |
| `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` | Name the use being justified by value: intended work, reliance on a claim, reliance on a dated `U.Work` occurrence, method-family selection, selected method, method of work, work plan, planned work, work result, result measurement, release reliance decision, non-work reliance claim, work-relevant P2W claim, or P2W chain position. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record; performed work becomes `U.Work` only after it occurs and is recorded under `A.15.1`; work-result measurement belongs with the evidence relation or result-measurement record that carries it. |
| `RequiredPositionEntries` | This is the sole prerequisite set. Add one row per independent direct object, whether it is a claim, instituted effect, relation occurrence, owner-defined result, gate decision, assignment, evidence/currentness relation, plan, or other prerequisite. Each row names its `DirectOwnerPatternRef`, exact `DirectObjectKind`, native typed `ProjectSideObjectRef`, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. Never store several patterns, kinds, or refs as comma-separated prose, and never coerce the refs into one generic `U.EntityRef` list. |
| `AllowedUseNow` | State the safe current use. `proceed-inside-recovered-relation` is allowed only after every required entry passes its `RequiredPostureOrCurrentness` and exact-use match; otherwise retain orientation, source-finding, bounded probe, repair request, narrowed reliance, or blocked unsupported use. |
| `AppearanceOverreadBlocked` | State the overread being blocked, such as treating display color as gate passage, copied approval as a current speech act, a credential screenshot as permission, or a generated explanation as evidence. |
| `RecoveryOrStopCondition` | Write the first row that fails and the observation that would make it pass. Reopen only after following every typed ref and verifying that its relation obtains or its result passes the owner-defined criterion, is current, covers the attempted use, and has the evidence/source support required for this reliance. Include separately required current conflict-finding, gate, and work-entry-readiness rows; an unresolved conflict row blocks the affected use without changing grant currentness. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `A.16.0` distinction rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`; `U.EpistemePublication` is used only when that episteme is available as a published episteme with MVPK-face references. Publication forms, MVPK faces, publication carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or relation positions in the case. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record such as `SlotFillingsPlanItem`; launch values and finalization values remain their own project records, decision logs remain gate or decision records, performed-work evidence remains evidence, and dated work occurrences remain `A.15.1` or `U.Work` matters.

When the governing pattern position is incomplete, choose one relation-governed `A.15.4` disposition after naming the work or reliance use and the exact direct objects it requires in `RequiredPositionEntries`; pick the lightest disposition that preserves practical work and recoverability:

1. Use the reliance appearance only for orientation or source-finding.
2. Reopen the source `U.Episteme` for the current claim, the `U.EpistemePublication` that exposes the claim-bound source relation, register entry, governing record, or governing relation, or refresh source-currentness, credential-status, role-state, context-state, or another currentness relation.
3. Narrow the acting holder, work-performing system, agent, `RoleAssignmentRef` when current, requested operation or work class, affected work target, affected resource, affected claim, context, and effective window until the recovered record or relation really covers the recovered use.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Ask the holder, work-performing system, maintainer, verifier, issuer, or project role holder identified by the relevant `RoleAssignmentRef` or governing relation to expose or repair the missing direct object named in that `RequiredPositionEntries` row. Keep any additional missing gate, evidence, assignment, state, currentness, or boundary object in its own row.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source-relation link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks the required relation.

#### Repair assignment rule

**Missing record or relation repair assignment.** If the required governing record or relation is unavailable to the acting user, assign only prospective repair work, request work, decision work, work-plan work, or source-relation gap work to the holder, work-performing system, maintainer, verifier, or project role holder identified by the relevant `RoleAssignmentRef` or governing pattern relation for the missing relation. The acting user records the blocked work claim or reliance claim, the missing relation, and the safe narrowed use now.

**Reliance-appearance kind check.** First name the actual kind of the reliance appearance: episteme, episteme publication, publication form, carrier, rendering, dashboard tile, credential view, generated/copied wording, or source-finding cue. If it exposes a typed ref, follow that ref to the direct owner and test the owner's obtaining or result criterion. If it exposes only a face, carrier, wording, or record entry, use it for orientation/source-finding until the direct object and evidence/currentness relation are recovered.

**Source-relation guard.** Release urgency, delegated-claim urgency, compliance concern, color, salience, copied wording, or generated wording does not replace the source relation named by value. A dashboard tile may guide release only as a current view of the relevant `GateDecision` plus evidence relation, currentness relation, scope, and window.

#### Governing-position lookup table

Governing patterns by required direct-object kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.
**Permission and authority branch — use only when that is the live claim.** Do not route from *approved*, *authorized*, *allowed*, *may*, or the look of a permit. Ask what is true now and choose one row.

| Plain question | Direct owner and object | What closes or blocks this branch |
| --- | --- | --- |
| Did an admitted system actually perform an approval, authorization, delegation, grant, or revocation communication under its covering assignment? | `A.2.9`; one actual `SA : U.SpeechAct` occurrence. | Recover the occurrence, performer system, obtaining assignment, context, time, act type, and evidence needed for reliance. A `SpeechActRecord`, message, or carrier is not the act, and the act alone does not make an institutional effect obtain. |
| Does a policy-valid strong grant currently obtain for this beneficiary and action? | `A.2.8.PER`; one `GrantedPermissionRelation@Context` occurrence. | Match beneficiary, action specification, policy/context, scope/window, and instituting `SpeechActRef`. A valid revocation, supersession, or policy failure may prevent or end the grant. An unresolved same-case conflict can block this attempted use without making the grant cease to obtain; keep those results separate. This is the permission-side instituted effect. |
| Before action, did a current frame complete enough for this use contain no applicable prohibition? | `A.2.8.PER`; one `NonProhibitionFinding@Context`. | Name the frame, use, beneficiary/action, scope/window, and evaluation. A stale or incomplete frame returns `unresolved`, not permission. |
| Did dated Work actually exercise one obtaining grant? | `A.2.8.PER`; one `PermissionExerciseRelation@Context` occurrence. | The Work must match the grant's action and the actual performer must satisfy its beneficiary branch. No dated Work means no exercise; non-exercise is not violation. |
| After Work, did a current sufficiently complete frame find no applicable violation? | `A.2.8.PER`; one `NonViolationFinding@Context`. | Name the actual Work, evaluation Work, frame, scope/window, and result. Exercise or non-exercise alone settles nothing; a stale or incomplete frame returns `unresolved`. |
| Do an obtaining grant and a current norm reach incompatible conclusions for the same beneficiary/action and overlapping scope/window? | `A.2.8.PER`; one `PermissionNormConflictFinding@Context`. | Cite the applicable precedence rule or an authorized dated decision Work and current resolution result. Otherwise keep the conflict `unresolved` and block the affected use. |
| Is an accountable subject obliged, prohibited, or given a recommendation-as-duty? | `A.2.8`; one `U.Commitment`. | Name the accountable subject, modality, referents, scope/window, and instituting act when provenance matters. The utterance, record, and carrier are not the commitment. |

A gate or readiness result remains an additional `A.21` or `A.15.5` prerequisite; it creates none of these objects. If the issue is only wording, classify it through `A.6` or the single permission-word branch in `A.6.B`. If only a permit, badge, message, record, or tile is visible, stay at orientation/source-finding until one row above can be supported.
- role-assignment, role-state, credential-status, or context-state reliance: cite `A.2.1`, `U.RoleAssignment`, a state-changing `U.SpeechAct`, a governing context-state record, a credential proof or credential-status result under `A.10`, or an `A.21` `GateDecision` when the state is gate-governed.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`. When its live job is permission or authority, return to the branch above; the displayed word does not choose the object.
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins.
- Flow constraint-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim.
- release, deployment, repair, inspection, or rollback work occurrence: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence or provenance relation when reliance on occurrence is needed.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: apply `A.10` and name the claim-bound evidence relation, currentness relation, and relation-governed or blocked use.
- assurance, safety, compliance, trust, release confidence, or `R`, `F`, `G`, or `CL` increase: apply `B.3` and name the typed assurance claim plus its limitations and reopen condition. If the word `ready` names full-kit or work-entry readiness, use `A.15.5`; if it names a gate decision, use `A.21`.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source relation for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: use the permission and authority branch above and choose by the plain question it answers now, never by the displayed word.

Recovered governing pattern outputs for A.15.4 closure:
| Governing pattern or relation used | Recovered output for this A.15.4 repair | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the pattern that governs the current boundary claim or the current effect-bearing claim. | Use for wording, boundary, API, schema, or use-boundary recovery before intended work or reliance. |
| `A.10` | Claim-bound evidence relation, freshness field, currentness field, and relation-governed or blocked use for the attempted claim. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the work or reliance claim under repair relies on a typed assurance claim. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidity` status, witness, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim. | Use for flow constraint-validity reliance. |
| Permission or authority is current | Use the single branch above and carry the selected owner's native object with its own closing conditions. | Do not mint or cite a generic permission-result object. |
| `A.15.1` | Dated `U.Work` occurrence plus `A.10` evidence or provenance relation when relied on. | Use for reliance on performed work. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the source `U.Episteme` or the `U.EpistemePublication` exposing that source relation. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

High-impact work or reliance - especially external-impact, irreversible, release-bearing, role-assignment-bearing, role-state-claim-bearing, credential-status-claim-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - may guide work only for the acting holder, work-performing system, or agent, the `RoleAssignmentRef` when role-conditioned capacity or attribution is current, the work or reliance claim under repair, work-relevant P2W claim under repair, P2W chain position under repair, affected work target or claim, audience, scope, environment, version, policy context, operational mode, and time window for which the required FPF-governed project-side source relation, evidence relation, gate decision, or assurance claim is recoverable. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full evidence, currentness, or provenance dossier.
Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Release dashboard tile exposing a source relation | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release scope or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence relation, it may carry gate-passage reliance for that release and environment. |
| Release dashboard tile without current gate or evidence relation | Use the tile only for display or source-finding until the current `A.21` `GateDecision` or `DecisionLogRef`, release scope or work target, environment or scope, time window, gate profile, gate version, and `A.10` evidence relation are recoverable. Open `B.3` only when an assurance claim is being made. |
| Copied review summary or copied approval | Treat it as copied wording and a currentness cue. If the intended use relies on permission or authority, use the single branch above and follow only its selected direct owner. Gate passage still needs the `A.21` decision, performed work still needs the dated `A.15.1` occurrence, and reliance needs the applicable `A.10` evidence/currentness relation. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work target, affected resource, affected claim, scope, window, the delegation record or relation permitting delegation, subdelegation allowance if any, revocation relation, currentness relation, and evidence relation. A forwarded approval is not delegated authority by copy alone. |
| Role-assignment, revocation, role-state, or credential-status display | Resolve to role assignment, state-changing speech act, context-state record, credential proof or credential-status result, or gate decision with freshness field, revocation relation, or revocation record; visual display cannot defeat a higher-priority revocation or supersession relation. |
| Conflicting source relations | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source-relation order, governing decision record, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed credential-status view | Treat the display as a publication of a register-entry episteme. Before relying, recover separately: the exact entry and its publication relation; the constitutive policy/rule; the admitted system and covering assignment for any authorized entry-producing speech act, the actual matching Work for an exercise claim, or the evaluation Work required for a finding; the actual direct relation/finding selected by its owner; and the evidence/currentness/revocation relation. The entry is authoritative source only under the named rule for the exact claim or effect that rule governs. An institutional effect still needs the authorized Work that the rule makes constitutive; a finding still needs its owner-defined evaluation. Inscription alone performs no Work, institutes no effect, and creates neither exercise nor non-violation. |
| Rollback command-like cue | Treat as cue or `A.6.A`-governed invitation unless command record, authorization, work occurrence, performed-work result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Use the explanation only to find source publications, claim-bound source relations, or governing positions. If permission or authority is the live claim, route through the single branch above. The explanation itself supplies none of that branch's objects and proves neither gate passage nor performed work. |
| Extracted source publication, rewrite, representation shift, explanation, then gate or release claim | Return to the source `U.EpistemePublication`, source-bearing relation, transform record, evidence relation, explanation relation, or governing pattern position at the first lossy or non-commutative transformation operation; the gate claim or release claim waits for the required transform record, evidence relation, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-relation repair work: expose decision refs, fix dashboard semantics, add claim-bound source relations and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

