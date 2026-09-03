---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:3.1"
section_title: "Archetypal Grounding - Worked Dashboard And Approval Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__006_archetypal-grounding-worked-dashboard-and-approval-examples.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:3.1 — Archetypal Grounding - Worked Dashboard And Approval Examples"
line_start: 26409
line_end: 26489
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

### A.15.4:3.1 - Archetypal Grounding - Worked Dashboard And Approval Examples

Worked dashboard and approval slice:

A release dashboard shows a green approval-looking tile for `Release-2026.05.08-prod`. If the tile is a current view of the relevant `GateDecisionRef` plus evidence relation and currentness relation, it may carry bounded gate-passage reliance for that release scope and window. A claim that deployment happened still requires a dated `A.15.1` work occurrence plus the evidence or provenance relation needed for the relying context. If the gate reference is missing or stale, treat the tile as orientation and source-finding until the team can name the release-work claim under repair, release-work position under repair, `SubjectPatternLocator` for the claim or effect, and the required gate-decision, evidence, and currentness fields.

| Step | Required record or relation |
| --- | --- |
| Required project claim or effect kind | Release reliance, gate passage, compliance proof, assurance increase, evidence relation, or currentness relation. |
| Gate decision record | Cite the current `A.21` `GateDecision` or `DecisionLogRef`, gate profile, gate version, release scope or work target, scope, window, and replay or freshness pins. Without that record, the tile is not release authorization or gate passage. |
| Flow constraint-validity witness | Cite `A.20` `ConstraintValidity` status or witness only when the claim is about flow constraint validity, not about the gate decision itself. |
| Evidence and currentness relation | Use `A.10` for the dashboard query, publication-carrier integrity, evidence refs, time, window, freshness field, revocation relation or revocation record, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance claim | Use `B.3` only if the tile is being used to raise readiness, compliance, trust, safety, release confidence, `R`, `F`, `G`, or `CL`; otherwise no assurance tuple is being claimed. |
| Repaired gate-use reliance | With the decision and evidence relation recovered, rely on gate passage only for the named release scope or work target, environment, gate profile, gate version, time, and window. A claim that deployment happened still needs its actual performer identified through A.13, the dated Work independently admitted through A.15.1, and the evidence or provenance relation needed for the relying context. If that claim must also identify the assignment under which deployment was performed, check the assignment separately through F.6. |
| Blocked overreads | The dashboard color does not create approval, deontic permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green-tile case:

An approval memo may carry an approval claim when it exposes the `A.2.9` `SpeechActRef`, the actual performer identified through A.13, and the A.15.1 account that independently admits the speech-act Work. If the approval use must also identify the grantor assignment, or that assignment changes policy applicability, add `actingSystemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment` and use F.6 to compare its holder with the already identified performer. Keep affected release scope or work target, judgement context, time, window, publication-carrier refs, evidence refs, and the instituted effect separate. Authority is never supplied by the assignment. The memo supports only the bounded approval use defined in `A.2.9`; release, deployment, rollback, or other performed Work needs its own A.13/A.15.1 basis and any A.10 evidence relation required for reliance.

Credential-status and system-role-assignment-state green-tile case:

A credential, credential-status, or system-role-assignment-state response is a publication of a claim-bearing register entry, not the status, `SystemRoleAssignmentStateRelation`, or assertion itself. It may serve as authoritative source only when the named register rule identifies the exact entry, issuer, holder-and-assignment binding, relying context, freshness and window, authorized entry-producing Work, and exact direct effect for which that Work is constitutive. Apply the criterion named by the selected §3 row to decide whether the relation obtains or the finding is warranted, and use `A.10` for the evidence and currentness claims. The response never supplies release, Work occurrence, gate passage, permission, authority, or evaluation result merely by being present.

Situation viewpoint prompts:

| Viewpoint or repair concern | Prompt |
| --- | --- |
| Acting practitioner | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work or reliance justification? |
| Release engineer | Which `A.21` gate decision, decision log, release scope, work target, and `A.15.1` work occurrence are separate here? |
| Source, gate, evidence, or assignment-record contact | Which source-currentness value, assignment-state relation or assertion, credential-status value, decision ref, or evidence relation needs exposure? Which direct source, publication, register, communication, access, or contact fact supports that request? Only if repair Work is being assigned: which allocation, responsibility, commitment, permission, or authority relation selects its performer? |
| Audit or peer-review viewpoint | Which prerequisite, object, and test in the §3 lookup must be recoverable? If permission or authority is current, which one row in that branch answers the live question? |
| Boundary claimant | Which words need typed claim IDs before they can guide work or reliance? |
| Manager | Is repeated ambiguity prerequisite-lookup or source-relation repair work rather than another manual check for the acting practitioner? |
| LLM user or tool user | Which required relation, result, or source relation does the explanation help find, and which operative claims still need an `A.10` claim-bound source relation? |
| Security or compliance source contact | Which revocation relation, currentness relation, proof, credential-status record, system-role-assignment-state assertion, source-relation order, or supersession relation needs exposure, and which direct source, register, communication, access, or contact fact supports asking for it? If repair Work is assigned, which independent allocation, responsibility, commitment, permission, or authority relation selects the performer, or which exact missing governor blocks only that stronger move? |
| Model or data documentation steward | Which intended use, evaluation condition, version, window, limitation, and evidence relation bound the model or data documentation? |
| Assurance viewpoint | Which named claim actually has a `B.3` assurance claim, with what assurance tuple, evidence relation, limitations, and reopen condition? |

Search cues for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are retrieval cues only; decide the required relation or result, the pattern whose content defines or tests it, and the project-side reference from the work or reliance question under repair, not from the displayed word, publication-carrier name, or source name.

Work and reliance disposition table for authority-looking cases:

| Question under repair | Start in | First useful output |
| --- | --- | --- |
| Can this episteme publication, publication face, publication carrier, rendering, or cue guide work or reliance by appearance? | `A.15.4` | Work or reliance use, required claim/effect, project-side reference, and minimum use supported by the recovered relation. |
| Is the problem boundary, policy, API, schema, or connector wording? | `A.6` or `A.6.B` | Typed `L-*`, `A-*`, `D-*`, and `E-*` claims before the work claim or reliance claim is used. |
| Is the problem evidence, currentness, provenance, credential-status, generated-source relation, copied-source relation, or source-chain recovery? | `A.10` | Claim-bound evidence relation, currentness relation, and the use allowed or blocked by the recovered relation. |
| Is the problem assurance, readiness, safety, compliance, trust, release confidence, or change in `R`, `F`, `G`, or `CL`? | `B.3` | Typed assurance claim, no-assurance-use disposition, or downgraded or rejected assurance use. |

Display guidance for bounded credential status or system-role-assignment state: a visible state label meant to guide Work should expose source type, reference or link named by value, freshness, window, scope, unsupported Work claim, unsupported reliance claim, and unsupported effect. For example, prefer `Gate check passed; GateDecisionRef; release scope; environment; window; not compliance proof, rollback success, or assurance increase` over a bare approval-looking label.

Incident-learning fields for authority-looking overread: encountered selected episteme, publication occurrence, form, or carrier; work or reliance claim under repair; required relation or result, its `SubjectPatternLocator`, and project-side reference; acting or affected System; a context field ending in `...SystemRoleAssignmentRef` only when assignment identity matters to F.6 attribution or another direct relation that independently obtains; separate capability, authority, and responsibility rows when current; affected target, context, and window; missing or stale source, publication occurrence, source-bearing relation, register entry, or project-side reference; the direct source, publication, register, communication, access, or contact fact supporting a cheap exposure request; and, only for prospective repair Work, the selecting allocation, responsibility, commitment, permission, or authority relation or exact A.6.RCD missing governor; plausible overread; safe disposition; and smallest upstream repair.

Contestability and redress relation: when an authority-looking case affects assignment state, credential status, access, assignment, responsibility, release blockage, compliance claim, or safety-impacting Work, name the available challenge, review, redress, communication, source, publication, register, access, or contact relation before the work claim or reliance claim hardens. Recover the disputed source relation or claim, affected use or harm, allowed evidence or argument, possible disposition change, outcome route, and reopen trigger. Keep cheap source exposure available even when no one yet bears responsibility for future repair. Only a claim that a System must conduct later review or repair Work needs its own allocation, responsibility, commitment, permission, or authority relation; if that relation is absent, its exact missing governor blocks that stronger duty claim, not the challenge itself.

Lintable overread cues:

| Lint signal | Required relation or result named by value |
| --- | --- |
| `approved`, `authorized`, `allowed`, `recommended`, or `guaranteed` in boundary, API, schema, or policy wording | Split through `A.6` or `A.6.B`; when permission or authority is the live claim, use the single branch above instead of routing from the word. |
| Dashboard tile, credential-status color, system-role-assignment-state color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecision` or `DecisionLogRef` plus `A.10` evidence and currentness relations. A displayed assignment-state label is neither `SystemRoleAssignmentStateRelation` nor its assertion. |
| Register screenshot, badge, or entry used as permission, authority, system-role-assignment, assignment-state, or gate evidence | Require five separate recoveries: the register-entry episteme and its publication relation; the constitutive rule; every authorized entry-producing, exercised, or evaluation Work, with its performer identified through A.13 and the dated occurrence admitted independently through A.15.1; a separate F.6 check when the result must also identify the assignment under which that Work was performed; the direct relation or finding under the selected §3 row; and `A.10` evidence and currentness. The entry may be authoritative source for the rule's exact claim or effect, but inscription creates neither actual exercise nor a non-violation finding. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation/source-finding and `A.10` for the claim-bound source relation; if permission or authority is current, choose one row in the single branch above. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Require a typed `B.3` assurance claim, intended-use match, evaluation condition, limitations, and `A.10` evidence relation. Use `A.15.5` instead when the current claim is full-kit or work-entry readiness. |
| Provenance or attestation label cited as truth, safety, release, permission, or authority | Require the bounded `A.10` provenance/process-trace claim plus the applicable pattern and test for the relied-on truth, safety, release, permission, or authority claim. For the last two, use the single branch above; the label is not its result. |
| Evidence, assurance, gate, or work-occurrence words without the relation or result that carries that claim or effect | Recover the `A.10` evidence relation, `B.3` assurance claim, `A.21` gate decision, or `A.15.1` work-occurrence record respectively before the work claim or reliance claim is used. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover `A.21` decision or decision log plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Treat the copy as a source-finding cue; use the permission/authority branch above to choose the one live question, then recover currentness and evidence for that selected object. |
| Credential badge screenshot after revocation. | Recover the register-entry episteme, its publication relation, named status rule, authorized entry-producing Work, direct status relation, and evidence/currentness/revocation relation separately. The revoked direct relation blocks reliance even when the entry remains visible. |
| Register entry says `grant exercised; no violation`, but no dated matching Work or evaluation Work is recoverable. | Keep both claims blocked. For each exercise or evaluation occurrence, use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. If the claim must also identify the assignment under which either occurrence was performed, check that relation separately through F.6. Then test the action and beneficiary or the current sufficiently complete frame. Inscription establishes neither result. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation/source-finding and `A.10` for the claim-bound source relation; if permission or authority is current, choose and verify one row in the single branch above. |
| Boundary wording says `guaranteed approved for production`. | Split the sentence through `A.6` or `A.6.B`; use `A.6.C` for agreement-like or promise-bearing content and the single permission/authority branch above only for the permission or authority claim that remains. |
| Dashboard says green while decision log says blocked. | Treat as conflicting source relations; name source-relation order, the decision or rule establishing that order, freshness policy, and supersession rule before the work claim or reliance claim is used. |
| CRISPR lab dashboard says the guide edit is ready. | Treat the dashboard as orientation or source-finding until the protocol publication or protocol record, approval record or gate record, exact direct system-role-assignment occurrence when assignment identity matters, evidence relation, current lab context record, and `U.WorkPlan` for the intended edit are recoverable. Recover capability, authority, responsibility, permission, and Work attribution separately when current. If the question is full-kit or work-entry readiness for the intended edit, use `A.15.5`; the readiness tile still does not create biological-intervention authorization, deontic permission, safety, or performed Work. |

