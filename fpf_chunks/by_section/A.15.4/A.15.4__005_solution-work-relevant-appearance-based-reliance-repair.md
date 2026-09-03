---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:3"
section_title: "Solution - Work-Relevant Appearance-Based Reliance Repair"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__005_solution-work-relevant-appearance-based-reliance-repair.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:3 — Solution - Work-Relevant Appearance-Based Reliance Repair"
line_start: 26272
line_end: 26408
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
  - "A.2.5"
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
  - "F.6"
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

**Ordinary local note.** Use the opening sentence or six-line note and stop after the first missing prerequisite. Do not build a full evidence, currentness, or provenance dossier for that case.

For several prerequisites, a high-impact use, audit, handoff, or later reliance, expand that note with `RequiredPositionEntries`, `AllowedUseNow`, `AppearanceOverreadBlocked`, and `RecoveryOrStopCondition`.

The reliance appearance may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source-relation chain. The A.15.4 check asks whether every direct object required by the attempted use resolves and meets the posture and currentness predicates defined for that object, not merely whether a project-side reference is named or the reliance appearance is impressive, fluent, easy to inspect, or visually salient.

**Conditional structured field set.** Use the fuller fields below only for several independent prerequisites, later handoff or audit, or release-, safety-, compliance-, gate-, or other high-impact reliance. Also use them when an exact prerequisite's own rule requires assignment identity, assignment state, credential status, assurance, currentness, revocation, or cross-context detail. Select the depth from the attempted use and those direct prerequisites. The fields are worksheet aids or C.2.1 ClaimGraph content when persisted, not a record kind.

| Field | Working question |
| --- | --- |
| acting or affected system | Which admitted System would perform the Work, rely on the appearance, or be affected by the claim? A system-role kind, system-role assignment, credential status, and assignment-state relation are not the acting system. |
| system-role-assignment claim | Which assignment occurrence is being claimed, and which `U.SystemRoleAssignment` species declares it? A context field ending in `...SystemRoleAssignmentRef` is typed by `U.RelationRef constrained to U.SystemRoleAssignment` and resolves the occurrence. Keep capability, authority, responsibility, and Work attribution in their own rows. |
| intended work or work target | Is the user planning intended work, relying on a dated `U.Work` occurrence or result, or making another reliance claim? Name that branch and its required relation or result before the reliance appearance guides it. |
| affected resource or claim | Which resource, claim, gate, credential, credential-status, system-role-assignment-state relation or assertion, evidence, approval, or source-finding pointer with an authority relation is supposedly affected? |
| context | Which bounded context, environment, project slice, API setting, connector setting, protocol setting, or relying situation makes the claim applicable? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition applies to the claim? |
| time window | During which window is the claim, effect, source relation, or recovered-use boundary claimed to hold? |
| currentness or revocation field | Is the source relation current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or required reference | Which issuer, project reference, register entry, source-currentness or credential-status record, speech act, gate decision, evidence relation, or work-occurrence record is required for the current use, and where is its criterion defined? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation relation | Which `A.10` evidence, provenance, or attestation relation, if any, justifies the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceRelationClass | Which `E.17:5.1b` source-relation class or claim-use class applies to the reliance appearance and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, required value, or downstream effect remains unsupported and needs narrowing, repair, reopening, probing, or blocking? |

Start with the A.15.4 first repair checks above when the reliance appearance is being used as a reason for intended work, reliance, or a work-relevant claim. If the direct question is already known, use the §3 lookup and test its exact predicate and subject assertion; permission or authority uses the single branch there. Use A.15.4 only when `SubjectPatternLocator` and the project-side reference must still be recovered before a system-role-assignment, method, plan, Work, work result, result measurement, or another work or reliance claim can proceed.

**When a reliance appearance seems to authorize work or reliance.** Use A.15.4 when a publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for intended work or reliance. This is a recognition moment, not a new kind. The repair question remains: what does the user intend to do next, what relation or result would make that use admissible, and which project-side reference and test are required?

Here "authority-looking case" is only a recognition phrase for the encountered situation. The record, relation, slot filler, or project-side reference that authorizes, forbids, records, or supports the required relation is named by value under its FPF pattern. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to another FPF rule or result.

The central behaviour is: name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair; name each required relation or result and its project-side reference; keep the selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence when availability is material, publication form, MVPK face, publication carrier, rendering, and source-finding cue distinct; choose the minimum sufficient recovered use; and do not raise the claim beyond the recovered relation, source relation, or recovered use boundary. If a project record names a required relation or result, follow its typed ref and apply the criterion defined for it, including obtaining, result posture, currentness, scope, and evidence for this attempted use. Cite the exact defining or constraining `ClaimGraph` only when rule identity or edition changes the use or reliance; the record's statement does not make the relation obtain.

**Positive repaired disposition.** First name the attempted use and open each prerequisite through its typed ref. The appearance may guide that use beyond orientation only after every referenced relation actually obtains or result passes its defined criterion, is current, covers this beneficiary/action/target/scope/window, and has the evidence or source relation required for this reliance. When a relevant permission/norm conflict exists, its separate finding row must be current and settled for this use; an `unresolved` or norm-selecting disposition blocks the use without rewriting grant currentness. Then write what may happen next. The first failed row keeps only that unsupported work or reliance use blocked.

Reliance dispositions after prerequisite recovery:

| Work or reliance disposition | Use when | Minimum useful result |
| --- | --- | --- |
| Orientation or source-finding note | The reliance appearance is only a publication face, publication carrier, rendering, cue, retrieval cue, learning aid, or reversible local probe trigger. | Use the opening ordinary sentence or six-line note. Name the first missing direct object in plain language; add no `RequiredPositionEntries` row unless a structured-use condition applies. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated system-role-assignment claim, assignment-state claim, credential-status claim, contested source relation, or cross-context reuse. | For one prerequisite, use the opening ordinary result. If several prerequisites are independently required, add one typed row for each. Name the acting or affected System, target, situation, window, assignment occurrence, capability, authority, or responsibility only when this attempted use relies on that value; each stronger relation must obtain independently or return its exact missing governor. |
| High-impact reliance disposition | The attempted use is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, system-role-assignment-state-claim-bearing, credential-status-claim-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context; or one typed prerequisite row triggers high-impact conditions defined for that prerequisite. | Use the additional fields required by the attempted use and those exact `RequiredPositionEntries` rows. When permission or authority is current, choose exactly one row in the §3 branch rather than copying the whole catalogue here. |

For a structured use, add only the rows and fields that the attempted use actually needs:

| Field | Value |
| --- | --- |
| `RelianceAppearanceRef` | Name the appearance being relied on by value, such as the dashboard tile, credential view, copied text, generated explanation, publication face, publication carrier, rendering, or source-finding cue. |
| `RelianceAppearanceKind` | Name the encountered object or relation kind without granting authority by appearance: selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence or reference, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. |
| `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` | Name the use being justified by value: intended work, reliance on a claim, reliance on a dated `U.Work` occurrence, method-family selection, selected method, method of work, work plan, planned work, work result, result measurement, release reliance decision, non-work reliance claim, work-relevant P2W claim, or P2W chain position. A planned baseline remains claim content in one exact `U.WorkPlan`; performed work becomes `U.Work` only after its exact actual performer is recovered through A.13 and the dated occurrence is independently admitted through `A.15.1`; work-result measurement belongs with the evidence relation or result-measurement record that carries it. |
| `RequiredPositionEntries` | This is the sole prerequisite set. Add one row per independent direct object, whether it is a claim, instituted effect, relation occurrence, result with a pattern-defined criterion, gate decision, assignment, evidence/currentness relation, plan, or other prerequisite. Each row names its `SubjectPatternLocator`, exact `DirectObjectKind`, native typed `ProjectSideObjectRef`, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. The locator must identify the pattern whose content defines, constrains, or tests that direct object; never store several patterns, kinds, or refs as comma-separated prose, and never coerce the refs into one generic `U.EntityRef` list. |
| `AllowedUseNow` | State the safe current use. `proceed-inside-recovered-relation` is allowed only after every required entry passes its `RequiredPostureOrCurrentness` and exact-use match; otherwise retain orientation, source-finding, bounded probe, repair request, narrowed reliance, or blocked unsupported use. |
| `AppearanceOverreadBlocked` | State the overread being blocked, such as treating display color as gate passage, copied approval as a current speech act, a credential screenshot as permission, or a generated explanation as evidence. |
| `RecoveryOrStopCondition` | Write the first row that fails and the observation that would make it pass. Reopen only after following every typed ref and verifying that its relation obtains or its result passes the criterion defined for it, is current, covers the attempted use, and has any evidence-use, source-currentness, or other source relation required by this reliance. Include separately required current conflict-finding, gate, and work-entry-readiness rows; an unresolved conflict row blocks the affected use without changing grant currentness. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `E.24.PUB` distinctions rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`. When availability of its selected edition matters, name the exact `EpistemePublicationRelation` occurrence or reference. Publication forms, MVPK faces, publication carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or relation positions in the case; no publication-kind shortcut replaces them. A planned baseline remains one exact `U.WorkPlan` episteme; any A.15.3 planned-filling rows remain declaration-local ClaimGraph content inside it. Launch values and finalization values remain their own project records, decision logs remain gate or decision records, performed-work evidence remains evidence, and dated Work occurrences remain `A.15.1` matters.

When a required relation or result, its project-side reference, or its test is incomplete, choose one `A.15.4` disposition after naming the work or reliance use and the exact direct objects it requires in `RequiredPositionEntries`; pick the lightest disposition that preserves practical work and recoverability:

1. Use the reliance appearance only for orientation or source-finding.
2. Reopen the selected source `U.Episteme` for the current claim, the exact `EpistemePublicationRelation` occurrence when availability is the issue, the source-bearing relation, register entry, direct record, or direct relation; or refresh source-currentness, credential-status, system-role-assignment-state, context-state, or another currentness relation.
3. Narrow the acting or affected System, an exact context field ending in `...SystemRoleAssignmentRef` when assignment identity is current, requested operation or work class, affected work target, affected resource, affected claim, context, and effective window until the recovered record or relation really covers the recovered use. Check capability through A.2.2, Work attribution through F.6, and authority or responsibility through its separately admitted direct predicate or exact missing governor.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Separate finding or exposing the missing source from assigning its repair. For source finding, ask an identified issuer, maintainer, verifier, holder, publisher, source contact, or acting user to expose the source or record on the strength of the direct source, publication, register, communication, access, or contact fact already available; this request neither assigns Work nor implies responsibility. Assign prospective repair Work, or say who must repair, only when an applicable allocation, responsibility, commitment, permission, or authority relation selects the System. Without that stronger relation, return the exact A.6.RCD missing governor for the repair assignment while keeping the cheap information request available. Keep every additional missing gate, evidence, assignment, state, currentness, or boundary object in its own row.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source-relation link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks the required relation.

#### Repair assignment rule

**Missing source exposure versus repair assignment.** If a required source or record is unavailable, first make the light request: ask an identified issuer, maintainer, verifier, holder, publisher, source contact, or acting user to expose or locate it using the available direct source, publication, register, communication, access, or contact fact. This request is source finding, not prospective Work allocation, and creates no duty, authority, or responsibility. If the current move instead assigns repair Work, decision Work, planning Work, or source-relation-gap Work, select the admitted System through an independently obtaining allocation, responsibility, commitment, permission, or authority relation. An exact system-role kind or assignment may be an applicability ground but supplies none of those stronger relations. Without one, record the exact A.6.RCD missing governor for the repair assignment while retaining the safe source-finding request and narrowed use.

**Reliance-appearance kind check.** First name the actual kind of the reliance appearance: episteme, publication occurrence, publication form, carrier, rendering, dashboard tile, credential view, generated/copied wording, or source-finding cue. If it exposes a typed ref, follow that ref to the required relation or result and apply the criterion defined in its `SubjectPatternLocator`. Resolve an exact defining or constraining `ClaimGraph` only when the rule identity or edition changes this use. If the appearance exposes only a face, carrier, wording, or record entry, use it for orientation/source-finding until the direct object and evidence/currentness relation are recovered.

**Source-relation guard.** Release urgency, delegated-claim urgency, compliance concern, color, salience, copied wording, or generated wording does not replace the source relation named by value. A dashboard tile may guide release only as a current view of the relevant `GateDecision` plus evidence relation, currentness relation, scope, and window.

#### Prerequisite lookup table

Patterns and checks by required direct-object kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.

**Permission and authority branch — use only when that is the live claim.** Do not route from *approved*, *authorized*, *allowed*, *may*, or the look of a permit. Ask what is true now and choose one row.

| Plain question | Pattern and required object | What closes or blocks this branch |
| --- | --- | --- |
| Did an admitted system perform an approval, authorization, delegation, grant, or revocation communication? | `A.2.9`; one `SA : U.SpeechAct` occurrence. | Use A.13 to identify the System that actually performed the communication, then let A.15.1 admit the speech-act Work independently. If the reliance claim must also identify the assignment that covered the communication, or the policy makes that assignment material, name the assignment already used in the A.13 account and use F.6 to compare its holder with the performer. Add the context, time, act type, and evidence needed for reliance. The assignment supplies neither performerhood nor authority. A `SpeechActRecord`, message, or carrier is not the act, and the act alone does not make an institutional effect obtain. |
| Does a policy-valid strong grant currently obtain for this beneficiary and action? | `A.2.8.PER`; one `GrantedPermissionRelation@Context` occurrence. | Match beneficiary, action specification, policy/context, scope/window, and instituting `SpeechActRef`. A valid revocation, supersession, or policy failure may prevent or end the grant. An unresolved same-case conflict can block this attempted use without making the grant cease to obtain; keep those results separate. This is the permission-side instituted effect. |
| Before action, did a current frame complete enough for this use contain no applicable prohibition? | `A.2.8.PER`; one `NonProhibitionFinding@Context`. | Name the frame, use, beneficiary/action, scope/window, and evaluation. A stale or incomplete frame returns `unresolved`, not permission. |
| Did dated Work actually exercise one obtaining grant? | `A.2.8.PER`; one `PermissionExerciseRelation@Context` occurrence. | Use A.13 to identify who actually performed the Work and A.15.1 to admit that dated occurrence before matching its action and performer to the grant's beneficiary branch. If the exercise result must also identify the assignment under which the Work was performed, check that separately through F.6 against the assignment used by A.13. No dated Work means no exercise; non-exercise is not violation. |
| After Work, did a current sufficiently complete frame find no applicable violation? | `A.2.8.PER`; one `NonViolationFinding@Context`. | For both the acted-on Work and the evaluation Work, use A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently. If the finding must also identify an assignment for either occurrence, check that assignment separately through F.6. Then name the frame, scope/window, and result. Exercise or non-exercise alone settles nothing; a stale or incomplete frame returns `unresolved`. |
| Do an obtaining grant and a current norm reach incompatible conclusions for the same beneficiary/action and overlapping scope/window? | `A.2.8.PER`; one `PermissionNormConflictFinding@Context`. | Cite the applicable precedence rule or an authorized decision. If the decision is asserted as dated Work, use A.13 to identify its actual performer and A.15.1 to admit it independently. Add F.6 only if the conflict record must also identify the assignment under which that decision Work was performed. Otherwise keep the conflict `unresolved` and block the affected use. |
| Is an actual system or separately governed party obliged, prohibited, or given a recommendation-as-duty? | `A.2.8`; one `U.Commitment`. | Name the actual duty bearer, direct predicate, modality, exact referents, scope and window, applicable constitutive policy and rule, and actual instituting basis. A system-role kind or assignment may satisfy a rule antecedent but is not the duty bearer or commitment. The utterance, record, and carrier are not the commitment. |

A gate or readiness result remains an additional `A.21` or `A.15.5` prerequisite; it creates none of these objects. If the issue is only wording, classify it through `A.6` or the single permission-word branch in `A.6.B`. If only a permit, badge, message, record, or tile is visible, stay at orientation or source finding until one row above passes its stated test.
- system-role-assignment reliance: use `A.2.1` and name the assignment occurrence and its declared species. Assignment-state reliance instead uses the A.2.5 `SystemRoleAssignmentStateRelation`; credential-status reliance uses the exact proof or status result under `A.10`; context-state reliance uses its applicable direct state pattern and record; and a state established by a gate decision keeps its separate A.21 `GateDecision`. Keep every required object in its own row.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`. When its live job is permission or authority, return to the branch above; the displayed word does not choose the object.
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins.
- Flow constraint-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim.
- release, deployment, repair, inspection, or rollback work occurrence: cite the actual performer's A.13 basis, one dated `U.Work` occurrence independently admitted under `A.15.1`, and the `A.10` evidence or provenance relation when reliance on the occurrence is needed. If the reliance claim must also identify the assignment under which the Work was performed, check that relation separately through F.6.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: apply `A.10` and name the claim-bound evidence relation, currentness relation, and the use allowed or blocked by that relation.
- assurance, safety, compliance, trust, release confidence, or `R`, `F`, `G`, or `CL` increase: apply `B.3` and name the typed assurance claim plus its limitations and reopen condition. If the word `ready` names full-kit or work-entry readiness, use `A.15.5`; if it names a gate decision, use `A.21`.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source relation for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: use the permission and authority branch above and choose by the plain question it answers now, never by the displayed word.

Recovered prerequisites for A.15.4 closure:
| Pattern or relation used | Recovered output for this A.15.4 repair | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the pattern that defines or constrains the current boundary claim or the current effect-bearing claim. | Use for wording, boundary, API, schema, or use-boundary recovery before intended work or reliance. |
| `A.10` | Claim-bound evidence relation, freshness field, currentness field, and the use allowed or blocked by that relation for the attempted claim. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the work or reliance claim under repair relies on a typed assurance claim. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidity` status, witness, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim. | Use for flow constraint-validity reliance. |
| Permission or authority is current | Use the single branch above and carry the native object named by the selected row with its own closing conditions. | Do not mint or cite a generic permission-result object. |
| `A.13` and `A.15.1`; F.6 when the assignment matters | A.13 identifies the actual performer, and A.15.1 independently admits the dated `U.Work` occurrence. If this reliance must also state under which assignment the Work was performed, F.6 checks that separate relation. Add the `A.10` evidence or provenance relation when the reliance uses it. | Use for reliance on performed Work without turning the assignment check into a Work premise. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the selected source `U.Episteme`, with the exact `EpistemePublicationRelation` occurrence named separately when availability is material. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

High-impact work or reliance - especially external-impact, irreversible, release-bearing, system-role-assignment-bearing, assignment-state-claim-bearing, credential-status-claim-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - may guide work only for the acting or affected System, any exact `...SystemRoleAssignmentRef` whose assignment identity is current, the work or reliance claim under repair, work-relevant P2W claim under repair, P2W chain position under repair, affected work target or claim, audience, scope, environment, version, policy context, operational mode, and time window for which the required project-side source relation, evidence relation, gate decision, or assurance claim is recoverable. Capability, authority, responsibility, assignment, Work attribution, and permission remain separate prerequisite rows. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full evidence, currentness, or provenance dossier.
Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Release dashboard tile exposing a source relation | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release scope or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence relation, it may carry gate-passage reliance for that release and environment. |
| Release dashboard tile without current gate or evidence relation | Use the tile only for display or source-finding until the current `A.21` `GateDecision` or `DecisionLogRef`, release scope or work target, environment or scope, time window, gate profile, gate version, and `A.10` evidence relation are recoverable. Open `B.3` only when an assurance claim is being made. |
| Copied review summary or copied approval | Treat it as copied wording and a currentness cue. If the intended use relies on permission or authority, use the single branch above and follow only the selected row. Gate passage still needs the `A.21` decision. Performed Work still needs its actual performer identified through A.13 and the dated occurrence independently admitted through `A.15.1`; if the relied-on account must also identify the assignment, check it separately through F.6. Reliance still needs the applicable `A.10` evidence/currentness relation. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work target, affected resource, affected claim, scope, window, the delegation record or relation permitting delegation, subdelegation allowance if any, revocation relation, currentness relation, and evidence relation. A forwarded approval is not delegated authority by copy alone. |
| System-role-assignment, revocation, assignment-state, or credential-status display | Resolve an assignment claim to both its occurrence and declared `U.SystemRoleAssignment` species. Resolve the other claims to the assignment-state relation, state-changing speech act, context-state record, credential proof or credential-status result, or gate decision with freshness field, revocation relation, or revocation record; visual display cannot defeat a higher-priority revocation or supersession relation. |
| Conflicting source relations | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source-relation order, the decision or rule establishing that order, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed credential-status view | Treat the display as a publication of a register-entry episteme. Before relying, recover separately: the register entry and its publication relation; the constitutive policy or rule; the admitted System and any assignment needed by the authorization claim; each matching exercise or evaluation Work, with its performer identified through A.13 and the dated occurrence admitted independently through A.15.1; a separate F.6 check if the result must also identify the assignment under which that Work was performed; the relation or finding required by the selected §3 row; and the evidence, currentness, and revocation relations. Assignment does not supply performerhood, authority, or responsibility. The entry is authoritative source only under the named rule for the claim or effect covered by that rule. Inscription alone performs no Work, institutes no effect, and creates neither exercise nor non-violation. |
| Rollback command-like cue | Treat it as a cue, or use `A.6.A` when it is an action invitation, unless the command record, authorization, work occurrence, performed-work result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Use the explanation only to find source publications, claim-bound source relations, or required relations and results. If permission or authority is the live claim, route through the single branch above. The explanation itself supplies none of that branch's objects and proves neither gate passage nor performed work. |
| Extracted source publication, rewrite, representation shift, explanation, then gate or release claim | Return to the selected source `U.Episteme` and, where the break concerns availability, its exact `EpistemePublicationRelation` occurrence, form, or carrier; otherwise return to the source-bearing relation, transform record, evidence relation, explanation relation, or required relation or result at the first lossy or non-commutative transformation operation. The gate claim or release claim waits for the required transform record, evidence relation, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-relation repair work: expose decision refs, fix dashboard semantics, add claim-bound source relations and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

