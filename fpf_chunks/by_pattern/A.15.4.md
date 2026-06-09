---
chunk_kind: "parent"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Source Restoration"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.15.4.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.15.4 — Work-Relevant Source Restoration"
line_start: 21100
line_end: 21417
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
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
  - "admissible next project move"
  - "approval-looking display"
  - "blocked overread"
  - "copied statement"
  - "credential view"
  - "dashboard display"
  - "generated explanation"
  - "provenance mark"
  - "required project-side FPF kind and reference"
  - "work-relevant source restoration"
---

## A.15.4 - Work-Relevant Source Restoration

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This A.15 cluster member tells an engineer-manager which project-side FPF kind, relation, and reference must be recovered before an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain may justify a work claim or reliance claim.

**Use this when.** Use this pattern when a visible item is about to guide a work move, reliance move, or work-relevant P2W claim by appearance, and the acting user must recover the project-side FPF kind and reference named by value before proceeding.

**First output.** One compact restoration note: encountered item; live work claim, reliance claim, work-relevant P2W claim, or P2W chain position; pattern that governs the claim being made or effect; project-side FPF kind and reference named by value needed; admissible next project move now; and blocked overread.

**What goes wrong if missed.** Teams let a dashboard, credential view, copied approval, generated explanation, provenance mark, schema wording, API wording, publication, display, or cue carry a work or reliance source relation by appearance. Work then proceeds or stops while the pattern and project-side reference that actually carry the claim or effect are missing, stale, revoked, or contradicted.

**Primary EntityOfConcern in plain terms.** One source-restoration relation for one live work claim, reliance claim, work-relevant P2W claim, or P2W chain position: encountered item, claim being made or effect, pattern that governs that claim or effect, project-side FPF kind and reference named by value needed, admissible next project move now, and blocked overread. It does not introduce a new source kind, evidence path, gate record, engineering-justification record, work occurrence, or generic publication kind.

**First admissible project move in plain terms.** Recover or name the pattern that governs the claim being made or effect, project-side FPF kind and reference named by value, and live relation before allowing the encountered item to guide work or reliance. When that relation is absent or insufficient, narrow the move, reopen or refresh the source, run only a bounded reversible probe under a work plan, or block the unsupported claim or effect.

**Recognition block vs assurance block.** Read **At a glance**, **Use this when**, **First output**, **What goes wrong if missed**, **Primary EntityOfConcern**, **First admissible project move**, **Working action path**, **Not this pattern when**, and **What this buys** as the primary recognition block. Read the field tables, lookup table, lint cues, stress cases, conformance checklist, SoTA alignment, and relations below as assurance blocks and companion material that tighten the same source-restoration claim; they do not widen this pattern into an evidence, gate, engineering-justification, speech-act, commitment, boundary, or work-occurrence pattern.

**Working action path.**
1. Name the encountered source kind and publication position without treating its appearance as the source relation itself.
2. Name the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position and the claim or effect that would be carried.
3. Recover the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect.
4. Choose the lightest admissible project move now: proceed inside the recovered relation named by value, narrow the move, run a bounded reversible probe under `U.WorkPlan`, reopen or refresh the source, ask the accountable role assignment to expose or repair the missing source episteme, publication, register entry, or project record, or block only the unsupported claim or effect.
5. Return to `A.15` only when the remaining question under repair is `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.

**Not this pattern when.** Stay in A.15 when the live problem is only `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in E.17 when the live problem is only publication-face exposure or multi-view publication. Stay in A.10, B.3, A.20, A.21, A.2.8, A.2.9, A.6, or A.15.1 when evidence, currentness, engineering justification, gate validity, constraint validity, commitment, speech act, boundary claim, or work occurrence already governs the claim being made or effect directly.

**What this buys.** The acting engineer-manager can keep work moving at the lightest admissible level: proceed inside the recovered relation named by value, narrow the move, run a bounded reversible probe under a work plan, reopen the needed project-side FPF kind and reference named by value, ask the role assignment accountable for that source to expose or repair it, or block only the unsupported claim or effect while preserving narrower admissible use.

### A.15.4:1 - Problem Frame

Dashboards, credential views, generated explanations, copied approvals, provenance labels, green tiles, schema wording, API wording, and composed source chains often look ready for action before the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that make the action or reliance admissible have been recovered. The practical problem is not to classify the item in FPF; the problem is to decide what an engineer-manager may do in the project now without turning appearance into approval, gate passage, evidence, assurance, performed work, or release permission.

**Plain recognition line.** Let the visible cue point to the relation named by value, source episteme, source publication, evidence path, gate decision, role record, status record, work occurrence, or assurance claim; do not let it become the relation that permits the work or reliance move.
**Source wording discipline.** In this pattern, `source` is not a generic kind. When the word has FPF-governed use, recover the kind named by value before allowing work or reliance: source `U.Episteme`, source `U.EpistemePublication`, project-side FPF kind and reference named by value, evidence path, gate decision, speech act, commitment, credential record, status record, role assignment, work-occurrence record, register entry, source-finding cue, source relation, repair record, or request record. If that kind named by value cannot be named, keep the encountered item at cue-only orientation or source-finding use and do not use it as a work relation or reliance relation.

### A.15.4:2 - Cluster Boundary

A.15 remains the kernel for separating `U.Role`, holder and context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and actual `U.Work`. A.15.4 starts only when an encountered item begins to justify a work claim or reliance claim and the team must recover the project-side FPF kind and reference named by value that carries that claim, effect, or relation. If the pattern and project-side reference that govern the claim being made or effect are already known, use them directly and keep A.15.4 as the bounded restoration step.

### A.15.4:3 - Work-Relevant Source Restoration

##### Core stress-case rule
**Ordinary source-restoration note.** In ordinary use, do not build a source dossier. The first useful note is:

`encountered item; live work claim or reliance claim; pattern that governs the claim being made or effect; project-side FPF kind and reference named by value needed; admissible next project move now; blocked overread`

The encountered item may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source chain. The pattern asks whether the work claim or reliance claim named by value is currently carried by a project-side FPF kind and reference named by value, not whether the item is impressive, fluent, or easy to inspect.

**Conditional source-relation field set.** Use the fuller fields below only when release, safety, compliance, role, status, gate, assurance, contested source, external reliance, cross-context reuse, currentness, revocation, generated source relation, or copied source relation is live. These fields are local restoration aids, not a new record kind.

| Field | Working question |
| --- | --- |
| subject or actor | Who or what would perform the work, rely on the item, hold the status, or be affected by the claim? |
| role | Which `U.RoleAssignment` or role-context claim is live? |
| guided action or work item | Which selected method, method of work, `U.WorkPlan`, planned work, actual `U.Work`, work result, release move, reliance move, status, or effect is being guided? |
| affected resource or claim | Which resource, claim, gate, credential, status, evidence, approval, or source finding with authority-reference relation is supposedly affected? |
| context | Which bounded context, environment, project slice, interface setting, protocol setting, or relying situation makes the claim live? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition is supposed to govern the claim? |
| time window | During which window is the claim, effect, source relation, or admissible-use boundary claimed to hold? |
| currentness or revocation field | Is the source relation current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or source | Which issuer, project-side FPF kind and reference named by value, register source, status source, speech act, gate decision, evidence path, or work-occurrence record carries the claim, effect, source relation, or admissible-use boundary? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation path | Which `A.10` evidence, provenance, or attestation path, if any, justifies the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceRelationClass | Which `E.17:5.1b` source-relation class or claim-admissibility class applies to the encountered item and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, or downstream effect remains unsupported and must be narrowed, repaired, reopened, probed, or blocked? |

Start with the A.15.4 working action path above when the encountered item is about to guide a work move, reliance move, or work-relevant claim. If the issue under repair is only evidence, currentness, gate validity, constraint validity, engineering justification, commitment, speech act, boundary wording, admissibility wording, credential proof, status proof, explanation, comparison, or carrier and front-end behavior, apply the pattern that governs that issue under repair and project-side FPF kind and reference named by value directly; use A.15.4 only when that source must be restored before role, method, plan, work, work result, result measurement, or another work move or reliance move can proceed.

**Authority-looking source-backed work or reliance case.** Use A.15.4 when an approval-, permission-, gate-, command-, credential-, delegation-, revocation-, status-, provenance-, dashboard-, copied-review-, generated-explanation-, schema-, API-, or composed-chain case is about to be used as a work cue, reliance claim source, release-reliance claim source, execution-evidence source, approval-claim source, approval-effect source, role-claim source, status-claim source, or next work-relevant move. The recognition moment is that an encountered publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for starting work; the question under repair is still the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position plus the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect being inferred from, or through, the wording, display, publication face, carrier, or source-finding cue. It is not the wording alone. A.15.4 does not change the primary `EntityOfConcern` of `A.15`; it guides only the source-restoration step before the encountered case can guide work or reliance.

Here "authority-looking case" is only a recognition phrase for the encountered situation; it is not a `U.*` kind, not an assurance tuple, not a measured value, and not a new source kind or project record. The source-backed project-side kind or record that permits, forbids, records, or carries the work-relevant claim may instead be a `GateDecision`, `SpeechAct`, `U.Commitment`, `RoleAssignment`, credential record, status record, `A.6.B`-claim being made, `A.10` evidence path, or `B.3` assurance claim. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, work claim, reliance claim, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair may belong to another pattern that governs the claim being made or effect with its project-side FPF kind and reference named by value.

The central behaviour is: name the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position; name the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect; keep the `U.Episteme` or `U.EpistemePublication` distinct from publication form, MVPK face, carrier, rendering, and source-finding cue; choose the minimum sufficient next move; recover only the project-side FPF kind and reference named by value needed for that move; and do not raise the claim beyond that recovered relation, source, or admissible-use boundary. If the named project record states the governing FPF relation, use that recorded relation directly rather than inferring it from wording.

**Positive repaired path.** An encountered `U.Episteme` publication, publication form, MVPK face, carrier, rendering, or source-finding cue may guide work or reliance only to the claim or effect carried by the recovered project-side FPF kind and reference named by value, actor or role, live work claim, reliance claim, work-relevant P2W claim, or P2W chain position, affected work item, context, window, and source-recoverable claim or effect. The repaired outcome is the smallest admissible work or reliance statement plus the unsupported work claim or reliance claim still blocked.

Reliance disposition by pattern that governs the claim being made or effect and project-side FPF kind and reference named by value:

| Work or reliance disposition | Use when | Minimum useful record |
| --- | --- | --- |
| Orientation or source-finding note | The encountered item is only a publication face, carrier, rendering, cue, search handle, learning aid, or reversible local probe trigger. | `encountered item; required claim or effect not yet carried by a recovered source; source to reopen; stop condition`. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated role or status claim, contested source, or cross-context reuse. | Live work claim, reliance claim, work-relevant P2W claim, or P2W chain position; required claim or effect; actor or role; affected work item, context, and window; visible source ref; and reopen condition. |
| High-impact reliance path | The required claim or effect is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, status-claim-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context. | Exact project-side FPF kind and reference with the live `A.10`, `A.6`, `B.3`, `A.2.9`, `A.2.8`, `A.21`, `A.20`, or `A.15.1` fields needed for that claim or effect. |

A small A.15.4 restoration note is enough for the first disposition:

| Field | Value |
| --- | --- |
| live work claim, reliance claim, work-relevant P2W claim, or P2W chain position | Name the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position exactly: method-family selection, selected method, method of work, work plan, planned work, actual `U.Work`, work result, result-measurement, release reliance decision, or non-work reliance claim. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record; actual execution becomes `U.Work` only after it occurs and is recorded under `A.15.1`; work-result measurement belongs with the evidence or result-measurement source. This row is a local restoration label unless it cites an existing FPF kind or governing FPF relation. |
| pattern that governs the claim being made or effect and project-side FPF kind and reference named by value | Approval, permission, gate passage, role or status currentness, work occurrence, evidence relation, assurance claim, boundary claim, or other claim named by value or effect needed before that work claim, reliance claim, or P2W chain-position claim can be treated as carried by a recovered source. The governing relation must be carried by the named FPF pattern and recovered project-side reference, not by a new `A.15.4` kind. |
| actor or role | Who would act or rely. |
| affected work item, context, and window | Release, service, person, role holder, work item, claim, tenant, environment, physical batch, construction element, machine state, or validity window affected by that class or claim. |
| claim-bearing episteme or episteme publication | The claim-bearing FPF kind is `U.Episteme` or a species such as `U.EpistemePublication`; if the encountered item is only a publication form, MVPK face, carrier, rendering, `PublicationUnit`, dashboard tile, copied text, credential view, generated explanation, API wording, or cue, name that kind named by value separately. |
| project-side FPF kind and reference named by value needed or safe next move | Source `U.Episteme`, source `U.EpistemePublication`, register entry, or project-side FPF kind and reference named by value to reopen; status to refresh; reversible probe; role assignment accountable for exposing or repairing the missing source; or narrower admissible use. |
| stop or reopen condition | What blocks the work claim or reliance claim and what would reopen it. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `A.16.0` distinction rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`; `U.EpistemePublication` is used only when that episteme is available as a published episteme with MVPK-face references. Publication forms, MVPK faces, carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or roles in the case. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record such as `SlotFillingsPlanItem`; launch values and finalization values remain their own project records, decision logs remain gate or decision records, execution evidence remains evidence, and actual work occurrences remain `A.15.1` or `U.Work` matters.

When the required project-side FPF kind and reference named by value is incomplete, choose one admissible degraded-operation move after naming the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position and the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect; pick the lightest move that preserves practical work and source recoverability:

1. Use the encountered item only for orientation or source-finding.
2. Reopen the required source `U.Episteme`, source `U.EpistemePublication`, register entry, or project-side FPF kind and reference named by value, or refresh status or currentness.
3. Narrow actor or role, requested operation or work class, affected work item, affected resource, affected claim, context, and window until the recovered source really covers the move.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Ask the role assignment accountable for the issuer, gate decision, evidence path, role record, status record, or boundary claim set to expose or repair the missing source.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks source relation.

##### Repair assignment rule

**Broken-source repair assignment.** If the required project-side FPF kind and reference named by value is unavailable to the acting user, assign only prospective repair work, request work, decision work, work-plan work, or source-gap work to the role assignment accountable for the missing source relation. The acting user records the blocked work claim or reliance claim, the missing source relation, and the safe narrowed move now.

**Encountered-item kind check.** First name whether the encountered item is a `U.Episteme`, `U.EpistemePublication`, publication form, MVPK face, carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. If the item exposes a project-side FPF kind and reference named by value, use that exposed source directly. If only the display face, carrier, wording, or cue is named, the A.15.4 disposition is orientation, source-finding, bounded reversible probe, source-repair request, or blocked unsupported reliance until the source relation named by value is recovered.

**Pressure guard.** Release pressure, delegated pressure, compliance pressure, color, salience, copied wording, or generated wording does not replace the source relation named by value. A dashboard tile may guide release only as a current view of the relevant `GateDecision` plus evidence path, currentness path, scope, and window.

##### Exact project-side FPF kind and reference lookup table

Exact project-side FPF kinds and references by required claim or effect kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.
- issuing, approval, authorization, delegation, or revocation act: cite `A.2.9` `U.SpeechAct` or `SpeechActRef`, including act type, actor, role, affected work item or claim, judgement context, window, carrier reference, evidence reference when currentness matters, and instituted effects if claimed. Because `U.SpeechAct <: U.Work`, it can evidence only that communicative act.
- deontic permission, obligation, prohibition, or recommendation-as-duty: cite `A.2.8` `U.Commitment` and the instituting `SpeechActRef` when provenance matters. If the word instead names admissibility, gate passage, authorization act, role effect, status effect, credential status, cue, or advice, use the pattern that carries that kind named by value.
- role or status reliance: cite `A.2.1`, `U.RoleAssignment`, a status-changing `U.SpeechAct`, a governing context-state record, a credential proof or status result under `A.10`, or an `A.21` `GateDecision` when the status is gate-governed.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`; use `A.6.C`, `A.2.3`, `A.2.8`, and `A.2.9` for agreement-like guarantee, SLA, or promise wording before work use or reliance use.
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins.
- constraint or flow-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, path, window, sentinel, and pins where live.
- release, deployment, repair, inspection, or rollback work occurrence: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence carrier path when reliance on occurrence is needed.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: apply `A.10` and name the claim-bound evidence path, currentness path, and admissible or non-admissible use.
- assurance, readiness, safety, compliance, trust, release confidence, or `R`, `F`, `G`, or `CL` increase: apply `B.3` and name the typed assurance claim plus its limitations and reopen condition.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source relation for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: choose among the rows above named by value by asking what effect is claimed now: speech act, commitment, admissibility predicate, gate passage, role or status change, credential status, evidence relation, assurance claim, or work occurrence.

Return products
 for loop closure:

| Governing source relation used | Return product for this A.15.4 restoration | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect. | Use for wording, boundary, API, schema, or admissibility recovery before work or reliance use. |
| `A.10` | Claim-bound evidence path, freshness field, currentness field, and admissible or non-admissible use for the attempted claim. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the live project move relies on a typed assurance claim. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidity` status, witness, path, window, sentinel, and pins where live. | Use for constraint-validity or flow-validity reliance. |
| `A.2.9` | `SpeechActRef` with act type, actor, role, affected work item or claim, judgement context, window, and instituted effects if claimed. | Use for issued acts and, where needed, dated occurrence of that communicative act. |
| `A.2.8` | `U.Commitment` deontic relation with accountable role, agent, referents, modality, scope, validity window, and instituting source when needed. | Use for deontic permission, obligation, prohibition, or recommendation-as-duty. |
| `A.15.1` | Dated `U.Work` occurrence plus evidence carrier path when relied on. | Use for reliance on performed work. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the source `U.Episteme` or source `U.EpistemePublication`. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

High-impact
 work or reliance - especially external-impact, irreversible, release-bearing, role-bearing, status-claim-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - is admissible only for the actor, role, live work claim, reliance claim, work-relevant P2W claim, P2W chain position, affected work item or claim, audience, scope, environment, version, policy context, operational mode, and time window for which the required FPF-governed project source, relation, evidence path, gate decision, or assurance claim is recoverable. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full source dossier.

Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Source-backed release dashboard tile | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release scope or work item, environment, scope, window, gate profile, gate version, and `A.10` evidence path, it may carry gate-passage reliance for that release and environment. |
| Unsourced or stale release dashboard tile | Display or source-finding only until the current `GateDecision` or `DecisionLogRef`, release scope or work item, scope, window, gate profile, gate version, and `A.10` evidence path are recoverable; use `B.3` only if an assurance claim is live. |
| Copied review summary or copied approval | Copied wording and copied-currentness cue at most; approval, authorization, permission, commitment, or work occurrence needs the original `A.2.9` `SpeechActRef`, `A.21` decision, `A.2.8` commitment, or `A.15.1` work source plus `A.10` evidence. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work item, affected resource, affected claim, scope, window, source permitting delegation, subdelegation allowance if any, revocation source, currentness source or currentness path, and evidence path. A forwarded approval is not delegated authority by copy alone. |
| Role, revocation, or status display | Resolve to role assignment, status-changing speech act, context-state record, credential proof or status result, or gate decision with freshness field, revocation source, or revocation record; visual status cannot defeat a higher-priority revocation or supersession source. |
| Conflicting sources | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source order, governing decision source, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed status view | Use the display as a publication of a credential source or status source, not the source itself. Find the governing status register or issuer, trust anchor, holder binding or subject binding, verifier context, relying context, proof or status result, revocation, freshness, and validity window. If the governing register entry itself creates or changes role, status, permission, duty, or gate effect in the bounded context, cite that register or status-source entry named by value and the `A.2.1`, `A.2.8`, `A.2.9`, `A.6.B`, or `A.21` source it depends on. Otherwise rely only on credential-currentness for that holder and context. |
| Rollback command-like cue | Treat as cue or `A.6.A`-governed invitation unless exact command, authorization, work occurrence, execution result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Explanation may help find sources; it does not issue, approve, revoke, commit, authorize, pass a gate, evidence execution, or raise assurance. A citation or source mention inside the explanation guides work use or reliance use only when the cited carrier carries that relied-on claim named by value in the relying context under `A.10`. |
| Extracted source, rewrite, representation shift, explanation, then gate or release claim | Reopen the most directly claim-bearing project-side FPF kind and reference named by value at the first lossy or non-commutative transform step; the gate claim or release claim waits for the required transform record, evidence path, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-system repair work: expose decision refs, fix dashboard semantics, add source links and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

##### Worked dashboard and approval examples

Worked dashboard and approval slice:

A release dashboard shows a green approval-looking tile for `Release-2026.05.08-prod`. If the tile is a current view of the relevant `GateDecisionRef` plus evidence path and currentness path, it may carry bounded gate-passage reliance for that release scope and window. Execution or deployment still requires an `A.15.1` work-occurrence source if the claim is that deployment happened. If the gate source is missing or stale, treat the tile as orientation and source-finding until the team can name the live release-work claim, live release-work position, pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect, and project-side FPF kind and reference named by value that carries the gate decision, evidence path, and currentness path.

| Step | Required move |
| --- | --- |
| Required project claim or effect kind | Release reliance, gate passage, compliance proof, assurance increase, evidence relation, or currentness relation. |
| Gate decision source | Cite the current `A.21` `GateDecision` or `DecisionLogRef`, gate profile, gate version, release scope or work item, scope, window, and replay or freshness pins. Without that source, the tile is not release permission or gate passage. |
| Constraint or flow-validity source | Cite `A.20` `ConstraintValidity` status or witness only when the claim is about constraint or flow validity, not about the gate decision itself. |
| Evidence and currentness source | Use `A.10` for the dashboard query, carrier integrity, evidence refs, time, window, freshness field, revocation source or revocation record, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance source | Use `B.3` only if the tile is being used to raise readiness, compliance, trust, safety, release confidence, `R`, `F`, `G`, or `CL`; otherwise no assurance tuple is live. |
| Admissible repaired use | With the decision and evidence path recovered, rely on gate passage only for the named release scope or work item, environment, gate profile, gate version, time, and window; a claim that deployment happened still needs an `A.15.1` work-occurrence source. |
| Blocked overreads | The dashboard color does not create approval, permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green path:

An approval memo may carry an approval claim when it exposes the `A.2.9` `SpeechActRef`, actor, role, affected release scope or work item, judgement context, time, window, carrier refs, evidence refs, and instituted effect being claimed. That carries the bounded approval claim or effect only. It does not prove that release, deployment, rollback, or other work occurred; that execution claim still needs the dated `A.15.1` work-occurrence source plus any `A.10` evidence path required for the relying context.

Credential and status green path:

A credential or status response may carry holder reliance, status reliance, or currentness reliance only inside the issuer or governing status register, holder binding or subject binding, verifier context, relying context, proof result or status result, revocation source or revocation record, freshness field, and validity window that it exposes. It does not by itself carry release, work occurrence, gate passage, engineering justification, evidence for underlying operational facts, or contextual permission; those uses require the project-side FPF kind and reference named by value that governs that claim or effect.

Role prompts:

| Role in the situation | Prompt |
| --- | --- |
| Acting user | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work or reliance justification? |
| Release engineer | Which `A.21` gate decision, decision log, release scope, work item, and `A.15.1` work occurrence are separate here? |
| Issuer, gate, evidence, or role source | What source, status, decision ref, or evidence path must be exposed or repaired? |
| Auditor or reviewer | Which evidence path, decision ref, speech-act ref, commitment, work occurrence, or assurance claim must be recoverable? |
| Boundary claimant | Which words need typed claim IDs before they can guide work or reliance? |
| Manager | Is repeated ambiguity a source-system repair item rather than another manual check for the acting user? |
| LLM user or tool user | Which project-side FPF kind and reference named by value does the explanation help find, and which operative claims still need an `A.10` claim-bound source relation? |
| Security or compliance source | Which revocation, currentness, proof, status, source order, or supersession source must be exposed? |
| Model or data source | Which intended use, evaluation condition, version, window, limitation, and evidence path bound the model or data documentation? |
| Assurance reviewer | Which named claim actually has a `B.3` assurance claim, with what assurance tuple, evidence path, limitations, and reopen condition? |
Search aliases for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are search handles only; decide the carrying project-side FPF kind and reference named by value and pattern or source relation that governs the claim being made or effect from the live work question or reliance question, not from the displayed word or carrier name or source name.

Work and reliance disposition table for authority-looking cases:

| Live question | Start in | First useful output |
| --- | --- | --- |
| Can this encountered episteme publication, publication face, carrier, rendering, or cue guide work or reliance? | `A.15.4` | Candidate next `U.WorkPlanning`, `U.Work`, or reliance move, pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect, minimum admissible next move, and project-side FPF kind and reference named by value needed. |
| Is the problem boundary, policy, API, schema, or connector wording? | `A.6` or `A.6.B` | Typed `L-*`, `A-*`, `D-*`, and `E-*` claims before the work claim or reliance claim is used. |
| Is the problem evidence, currentness, provenance, credential status, generated-source relation, copied-source relation, or source-chain recovery? | `A.10` | Claim-bound evidence path, currentness path, and admissible or non-admissible use. |
| Is the problem assurance, readiness, safety, compliance, trust, release confidence, or change in `R`, `F`, `G`, or `CL`? | `B.3` | Typed assurance claim, no-assurance-use disposition, or downgraded or rejected assurance use. |

Display guidance for bounded status: a visible status meant to guide work should expose source type, reference or link named by value, freshness, window, scope, unsupported work claim, unsupported reliance claim, and unsupported effect. For example, prefer `Gate check passed; GateDecisionRef; release scope; environment; window; not compliance proof, rollback success, or assurance increase` over a bare approval-looking label.

Incident-learning fields for authority-looking overread: encountered episteme or episteme publication, live work claim, reliance claim, work-relevant P2W claim, or P2W chain position, pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry that claim or effect, actor, role, affected work item or claim, context, window, missing or stale source `U.Episteme`, source `U.EpistemePublication`, register entry, or project-side FPF kind and reference named by value; governing FPF relation or role assignment accountable for exposing or repairing that missing source, plausible overread, safe disposition used now, and upstream repair item for the source, dashboard, explanation, credential view, boundary wording, publication face, or carrier.

Contestability and redress path: when an authority-looking case affects person or team status, access, assignment, responsibility, release blockage, compliance claim, or safety-impacting work, name the review path or redress path before the work claim or reliance claim hardens. The path should name the disputed source or claim, the role assignment accountable for refreshing or correcting that source, the evidence path or status path to reopen, the safe interim disposition, and the time and window for review.

Lintable overread cues:

| Lint signal | Governing relation named by value |

| --- | --- |
| `approved`, `authorized`, `allowed`, `recommended`, or `guaranteed` in boundary, API, schema, or policy wording | Split through `A.6` or `A.6.B` into `L-*`, `A-*`, `D-*`, and `E-*`; use `A.6.C`, `A.2.8`, and `A.2.9` for agreement-like wording where live. |
| Dashboard tile, status color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecision` or `DecisionLogRef` plus `A.10` evidence path and currentness path. |
| Credential screenshot or badge used as permission, authorization, role relation, or status relation | Require `A.10` issuer, holder, verifier, status, currentness, and relying-context fields, then exact `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` source for the required permission, authorization, role, status, gate claim, or gate effect. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation relation and source-finding relation and `A.10` claim-bound source relation; issue, approval, gate, and commitment claims still need `A.2.9`, `A.21`, or `A.2.8`. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Require a typed `B.3` assurance claim, intended-use match, evaluation condition, limitations, and `A.10` evidence path. |
| Provenance or attestation label cited as truth, safety, release, or permission | Require `A.10` bounded provenance claim or process claim plus separate evidence for truth, safety, release, permission, or assurance. |
| Evidence, assurance, gate, or work-occurrence words without the project-side FPF kind and reference named by value that carries that claim or effect | Recover the `A.10` evidence relation, `B.3` assurance claim, `A.21` gate decision, or `A.15.1` work-occurrence record respectively before the work claim or reliance claim is used. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover `A.21` decision or decision log plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Recover original `A.2.9` `SpeechActRef`, currentness, freshness, and any live `A.2.8` commitment or `A.21` gate source. |
| Credential badge screenshot after revocation. | Treat as contested credential-currentness; use `A.10` issuer, holder, verifier, status, and revocation path and do not infer permission. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation and source-finding and `A.10` claim-bound source relation; issuing, gate, and commitment claims still need their own sources. |
| Boundary wording says `guaranteed approved for production`. | Split through `A.6` or `A.6.B`; if agreement-like or promise-bearing, unpack through `A.6.C`, `A.2.8`, and `A.2.9`. |
| Dashboard says green while decision log says blocked. | Treat as conflicting sources; name source order, governing decision source, freshness policy, and supersession rule before the work claim or reliance claim is used. |

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose and Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (Work-relevant source restoration)** | Before an authority-looking case guides work or reliance, a conforming `A.15.4` use SHALL produce the ordinary source-restoration note: encountered item, live work claim, reliance claim, work-relevant P2W claim, or P2W chain position, pattern that governs the claim being made or effect, project-side FPF kind and reference named by value needed, admissible next project move now, and blocked overread. It SHALL name the pattern and project-side reference that carry the requested claim or effect; if that source is absent or stale, it SHALL lower only the unsupported reliance to orientation, source-finding, contested use, source repair, bounded reversible probe, or blocked unsupported claim. | Prevents appearance-based reliance while keeping ordinary use cheap. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that exposes a P2W chain may guide only the exact `A.15` work or planning kind named by the project use: method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, or result measurement. Claims outside that named use require their own project-side FPF kinds and references named by value. | Keeps P2W publication use tied to the live work move instead of turning publication form into project authority. |
| **CC-A15.4-3 (Lowering and refresh)** | When the pattern that governs the claim being made or effect, project-side FPF kind and reference named by value, source-currentness relation, revocation relation, affected work item, relying context, or time window cannot be recovered, the work or reliance claim SHALL be lowered to orientation, source-finding, contested use, bounded reversible probe, source-repair request, or blocked unsupported claim. Refresh is required when source currentness, revocation, governing decision, evidence path, status register, copied-source relation, generated-source relation, or publication relation changes. | Keeps A.15.4 useful without admitting a new source kind. |

### A.15.4:5 - Common Anti-Patterns and How to Avoid Them

- **Appearance as source relation.** A dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source chain is used as if presentation itself carried the work-relevant source relation. First name the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position, then recover the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value that carry the requested claim or effect. If that source is missing, lower only the unsupported reliance.

### A.15.4:5a - Consequences

| Consequence | Trade-off and cost | Mitigation |
| --- | --- | --- |
| Work can continue at the lightest admissible level instead of stopping on every suspicious display. | The practitioner must name the claim being made and project-side FPF reference before relying on the source. | Use the ordinary six-field source-restoration note first; open fuller fields only for high-impact or contested reliance. |
| Appearance-based approval, evidence, assurance, gate, and work-occurrence overreads are blocked. | Some convenient dashboard or copied-text shortcuts become unusable until source currentness is recovered. | Keep orientation, source-finding, and bounded reversible probes available when no external-impact reliance is being made. |
| Repeated ambiguity becomes source-system repair work rather than repeated manual heroics. | The repair may reveal missing register entries, stale source publications, or underspecified gate and evidence paths. | Assign only prospective repair work or source-gap work; do not backdate evidence, gate passage, work occurrence, or assurance. |

### A.15.4:5b - Rationale

A.15.4 exists because work often meets sources through displays, publication faces, generated explanations, copied statements, credential views, dashboard tiles, schema wording, API wording, or composed source chains before the project-side FPF kind and reference that actually carries the claim is visible. The pattern protects work momentum and source recoverability together: it lets the practitioner use the encountered item for orientation or bounded source-finding, while preventing the item from becoming approval, evidence, assurance, gate passage, performed work, release permission, role currentness, or status currentness by appearance.

The pattern is deliberately a restoration relation, not a new authority source. Once the evidence, gate, assurance, speech-act, commitment, role, status, work-occurrence, publication, or boundary claim named by value is recovered, the pattern that governs that claim carries it directly.

### A.15.4:6 - SoTA Alignment

**SoTA alignment rule.** Read the row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and relations of this pattern.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need requested operation named by value, affected resource or work item, context, and window relation. | Dynamic authorization practice separates subject, requested operation, affected resource or work item, context, and window before a relying move is allowed. | NIST Zero Trust and dynamic authorization practice; Cedar policy language; Zanzibar-style relation authorization; source maturity = current standards, specifications, and widely used technical practice. | The restoration note names the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position, the affected resource or work item, affected claim when live, policy version, context, and time window before treating a visible allow response, deny response, or policy response as an admissible work or reliance source. | **Adopt, adapt, reject.** Adopt bounded currentness, source-relation, and admissible-use invariants; adapt them through FPF project records named by value; reject treating policy-looking output as permission or work-relevant source relation by display. |
| Credential or register-backed status needs issuer, holder, verifier, status, currentness, and relying-context fields. | Credential and status practice separates issuer, holder binding or subject binding, verifier context, relying context, proof result or status result, governing register entry, revocation, freshness, and validity window. | W3C Verifiable Credentials and digital identity or register-backed status practice; source maturity = current specifications and technical practice. | A credential view or status tile can carry only the holder claim, status claim, or currentness claim whose issuer, register, proof result or status result, revocation, freshness, and relying context are recoverable. | **Adopt, adapt, reject.** Adopt status-currentness separation; reject treating a badge, screenshot, or register excerpt as role, status, permission, gate passage, or work reliance without the pattern that governs the claim being made or effect and project-side FPF kind and reference named by value. |
| Provenance and attestation marks need source relation and process-trace relation without becoming truth, release, or work evidence. | Provenance and attestation practice separates origin relation, process traceability relation, build claim, supply-chain claim, and verification metadata from truth of downstream claims or release permission. | C2PA content provenance; SLSA and in-toto attestations; source maturity = current standards, specifications, and widely used practice. | A provenance or attestation mark remains source relation or process-trace relation until `A.10`, `B.3`, `A.20`, `A.21`, `A.15.1`, or another source relation named by value carries the downstream claim. | **Adopt, adapt, reject.** Adopt source traceability and process traceability; reject provenance-mark-as-truth, release permission, gate passage, assurance, or work occurrence. |
| Change, gate, release, and approval displays need decision, schedule, and executed-work separation. | Release and change practice separates approval acts, authorization acts, gate decisions, planned schedules, and executed work. | ITIL 4 Change Enablement and current release or change practice; source maturity = current practitioner guidance plus mature service practice. | A dashboard or approval-looking display must expose the `GateDecision`, `SpeechAct`, `Commitment`, `U.WorkPlan`, or `A.15.1` work-occurrence source that carries the claim named by value or effect. | **Adopt, adapt, reject.** Adopt decision, schedule, and executed-work separation; reject a green tile, copied approval, or generated explanation as rollout, release, or work reliance by appearance. |

**Digital-identity and provenance boundary.** The W3C Verifiable Credentials, C2PA, SLSA, in-toto, Cedar-style, Zanzibar-style, NIST, and ITIL sources are used for currentness, status, provenance, authorization-source fields, and change-practice fields. They do not turn a visible credential, provenance label, attestation, policy response, register excerpt, or dashboard display into work occurrence, gate passage, permission, assurance, release, or project claim relation without the project-side FPF kind and reference named by value required by `A.15.4`, `A.15`, `A.10`, `B.3`, `A.20`, or `A.21`.

The nearest recovery references are the worked dashboard and approval examples, `CC-A15.4-1`, `CC-A15.4-2`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, and `A.15.1`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for the local `A.15.4` rule.

### A.15.4:7 - Relations

* **Cluster relation:** `A.15.4` is a cluster member under `A.15` for work-relevant source restoration; it does not replace the A.15 role, method, plan, and work kernel.
* **Uses:** `E.17:5.1b` and `E.17:5.1c` source-relation and admissible-use vocabulary, `E.17.EFP` for generated-explanation faithfulness and source-finding, `A.6`, `A.6.B`, and `A.6.C` for boundary, policy, API, and schema wording, `A.10` for evidence, currentness, provenance, and credential status, `B.3` for engineering justification claims, `A.20` for constraint validity, `A.21` for gate decisions, `A.2.8` for commitments, `A.2.9` for speech acts, and `A.15.1` for dated `U.Work` occurrences.
* **E.10.ARCH relation-selection rule:** When `E.10` encounters source-relation, authority, permission, approval, status, green-tile, generated-explanation, copied-review, credential, provenance, or dashboard wording that is about to guide work or reliance, `E.10.ARCH` selects `A.15.4` only after excluding or assigning direct evidence (`A.10`), assurance (`B.3`), gate (`A.21`), constraint (`A.20`), boundary or admissibility wording (`A.6` and `A.6.B`), speech act (`A.2.9`), commitment (`A.2.8`), work occurrence (`A.15.1`), and publication-face or explanation questions (`E.17` and `E.17.EFP`). `A.15.4` returns the work-relevant source-restoration relation named by value; it does not replace those governing patterns.
* **Returns to:** `A.15` when the remaining question under repair is role, method, plan, and work alignment rather than source restoration.

### A.15.4:7a - C.29 mathematical-lens use relation

> If a mathematical lens appears in work-relevant source restoration, use `C.29` only to state why the lens helps expose or bound an encountered item such as a visible item, generated wording, dashboard cue, copied phrase, publication form, MVPK face, carrier, rendering, `PublicationUnit`, or source-finding cue. `A.15.4` still governs the exact source item, visible item, restoration or reopen condition, reliance relation, and whether that item can be admissible for work. Method choice, plans, and performed work return to `A.15` and `A.15.1`; a `C.29` lens-use result does not turn a cue, rendering, or diagnostic phrase into source relation.

### A.15.4:7b - P2W Result-Related Source Boundary

When `E.18.1` reaches result wording, use this pattern only when a visible item, publication, dashboard, generated explanation, copied statement, provenance mark, schema wording, API wording, or composed source chain is about to justify a work-result or reliance claim by appearance. No generic `WorkResult` kind is admitted.

Recover the project-side FPF kind and reference named by value before relying on any result-related cue: result artifact, resource ledger, launch-values-bound record, substitution record, telemetry, acceptance record, quality-evaluation record, done-state update, feedback pin, result measurement, evidence path, assurance claim, parity relation, refresh relation, or role-enactability claim. If the governing pattern or relation is missing, use the encountered item only for orientation or source-finding and block only the unsupported result or reliance claim.

### A.15.4:7c - Lowering, Repair, and Refresh Conditions

Lower an `A.15.4` use when the live work claim, reliance claim, work-relevant P2W claim, P2W chain position, pattern that governs the claim being made or effect, project-side FPF kind and reference named by value, relying context, time window, source-currentness relation, revocation relation, evidence path, gate decision, assurance claim, speech-act ref, commitment, role assignment, status record, or work-occurrence source cannot be named for the intended use. The lowered use is orientation, source-finding, contested use, bounded reversible probe, source-repair request, or blocked unsupported claim.

Repair the source-restoration note when source currentness, revocation, source order, governing decision source, evidence path, copied-source relation, generated-source relation, dashboard publication, credential view, status register, boundary wording, or work-result cue changes. Repair the project-side FPF kind and reference governed by the evidence, assurance, gate, constraint, speech-act, commitment, role, status, work-occurrence, publication, or boundary-wording pattern governing the recovered claim when that recovered claim belongs outside A.15.4.

Refresh before allowing the encountered item to guide release, safety, compliance, delegated role or status, contested source, cross-context reuse, work-result reliance, external-impact reliance, or irreversible work. Stop the refresh at the smallest changed object: the encountered item, source episteme, source publication, project-side FPF kind and reference named by value, source-currentness relation, status or revocation record, gate relation, evidence relation, assurance relation, copied-source relation, generated-source relation, or work-governed relation.

### A.15.4:End

