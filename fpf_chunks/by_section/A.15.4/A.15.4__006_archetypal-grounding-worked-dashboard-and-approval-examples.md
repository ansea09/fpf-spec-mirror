---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Source Restoration"
section_id: "A.15.4:3.1"
section_title: "Archetypal Grounding - Worked Dashboard And Approval Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__006_archetypal-grounding-worked-dashboard-and-approval-examples.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.15.4 — Work-Relevant Source Restoration"
  - "A.15.4:3.1 — Archetypal Grounding - Worked Dashboard And Approval Examples"
line_start: 22949
line_end: 23028
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

### A.15.4:3.1 - Archetypal Grounding - Worked Dashboard And Approval Examples

Worked dashboard and approval slice:

A release dashboard shows a green approval-looking tile for `Release-2026.05.08-prod`. If the tile is a current view of the relevant `GateDecisionRef` plus evidence relation and currentness relation, it may carry bounded gate-passage reliance for that release scope and window. A claim that deployment happened still requires an `A.15.1` work-occurrence source. If the gate source is missing or stale, treat the tile as orientation and source-finding until the team can name the release-work claim under repair, release-work position under repair, governing pattern for the claim or effect, and governing source for the gate decision, evidence relation, and currentness relation.

| Step | Required source or relation |
| --- | --- |
| Required project claim or effect kind | Release reliance, gate passage, compliance proof, assurance increase, evidence relation, or currentness relation. |
| Gate decision source | Cite the current `A.21` `GateDecision` or `DecisionLogRef`, gate profile, gate version, release scope or work target, scope, window, and replay or freshness pins. Without that source, the tile is not release authorization or gate passage. |
| Flow constraint-validity source | Cite `A.20` `ConstraintValidity` status or witness only when the claim is about flow constraint validity, not about the gate decision itself. |
| Evidence and currentness source | Use `A.10` for the dashboard query, publication-carrier integrity, evidence refs, time, window, freshness field, revocation source or revocation record, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance source | Use `B.3` only if the tile is being used to raise readiness, compliance, trust, safety, release confidence, `R`, `F`, `G`, or `CL`; otherwise no assurance tuple is being claimed. |
| Repaired gate-use reliance | With the decision and evidence relation recovered, rely on gate passage only for the named release scope or work target, environment, gate profile, gate version, time, and window; a claim that deployment happened still needs an `A.15.1` work-occurrence source. |
| Blocked overreads | The dashboard color does not create approval, deontic permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green-tile case:

An approval memo may carry an approval claim when it exposes the `A.2.9` `SpeechActRef`, actor and role assignment if claimed, affected release scope or work target, judgement context, time, window, publication-carrier refs, evidence refs, and instituted effect being claimed. That carries the bounded approval claim or effect only. It does not prove that release, deployment, rollback, or other work occurred; that performed-work claim still needs the dated `A.15.1` work-occurrence source plus any `A.10` evidence relation required for the relying context.

Credential-status and role-state green-tile case:

A credential, credential-status, or role-state response may carry holder reliance, credential-status reliance, role-state reliance, or currentness reliance only inside the issuer, governing credential-status register, governing role-state register, holder binding or subject binding, verifier context, relying context, proof result or credential-status result, revocation source or revocation record, freshness field, and effective window that it exposes. It does not by itself carry release, work occurrence, gate passage, engineering justification, evidence for underlying operational facts, contextual deontic permission, or authorization; those uses require the governing source for the claim or effect.

Situation viewpoint prompts:

| Viewpoint or source-restoration concern | Prompt |
| --- | --- |
| Acting practitioner | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work or reliance justification? |
| Release engineer | Which `A.21` gate decision, decision log, release scope, work target, and `A.15.1` work occurrence are separate here? |
| Issuer, gate, evidence, or role-assignment source | Which source, role-state, credential-status, decision ref, or evidence relation needs exposure or repair? |
| Audit or peer-review viewpoint | Which evidence relation, decision ref, speech-act ref, commitment, work occurrence, or assurance claim needs recoverability? |
| Boundary claimant | Which words need typed claim IDs before they can guide work or reliance? |
| Manager | Is repeated ambiguity source-relation repair work rather than another manual check for the acting practitioner? |
| LLM user or tool user | Which governing source does the explanation help find, and which operative claims still need an `A.10` claim-bound source relation? |
| Security or compliance source | Which revocation, currentness, proof, credential-status, role-state, source order, or supersession source needs exposure? |
| Model or data source | Which intended use, evaluation condition, version, window, limitation, and evidence relation bound the model or data documentation? |
| Assurance viewpoint | Which named claim actually has a `B.3` assurance claim, with what assurance tuple, evidence relation, limitations, and reopen condition? |

Search cues for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are retrieval cues only; decide the governing source and governing pattern or source relation from the work or reliance question under repair, not from the displayed word, publication-carrier name, or source name.

Work and reliance disposition table for authority-looking cases:

| Question under repair | Start in | First useful output |
| --- | --- | --- |
| Can this encountered episteme publication, publication face, publication carrier, rendering, or cue guide work or reliance? | `A.15.4` | Candidate `U.WorkPlan`, dated `U.Work`, or reliance-use relation; governing pattern for the claim or effect; governing source; minimum relation-governed use. |
| Is the problem boundary, policy, API, schema, or connector wording? | `A.6` or `A.6.B` | Typed `L-*`, `A-*`, `D-*`, and `E-*` claims before the work claim or reliance claim is used. |
| Is the problem evidence, currentness, provenance, credential-status, generated-source relation, copied-source relation, or source-chain recovery? | `A.10` | Claim-bound evidence relation, currentness relation, and relation-governed or blocked use. |
| Is the problem assurance, readiness, safety, compliance, trust, release confidence, or change in `R`, `F`, `G`, or `CL`? | `B.3` | Typed assurance claim, no-assurance-use disposition, or downgraded or rejected assurance use. |

Display guidance for bounded credential-status or role-state: a visible state label meant to guide work should expose source type, reference or link named by value, freshness, window, scope, unsupported work claim, unsupported reliance claim, and unsupported effect. For example, prefer `Gate check passed; GateDecisionRef; release scope; environment; window; not compliance proof, rollback success, or assurance increase` over a bare approval-looking label.

Incident-learning fields for authority-looking overread: encountered episteme or episteme publication, work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair, governing pattern and governing source for the claim or effect, actor and role assignment, affected work target or claim, context, window, missing or stale source `U.Episteme`, source `U.EpistemePublication`, register entry, or governing source; governing FPF relation or role assignment accountable for exposing or repairing that missing source, plausible overread, safe disposition used now, and upstream repair work for the source, dashboard, explanation, credential view, boundary wording, publication face, or publication carrier.

Contestability and redress relation: when an authority-looking case affects person or team role-state, credential-status, access, assignment, responsibility, release blockage, compliance claim, or safety-impacting work, name the review relation or redress relation before the work claim or reliance claim hardens. The relation should name the disputed source or claim, the role assignment accountable for refreshing or correcting that source, the evidence relation or state-currentness relation to reopen, the safe interim disposition, and the time and window for review.

Lintable overread cues:

| Lint signal | Governing relation named by value |
| --- | --- |
| `approved`, `authorized`, `allowed`, `recommended`, or `guaranteed` in boundary, API, schema, or policy wording | Split through `A.6` or `A.6.B` into `L-*`, `A-*`, `D-*`, and `E-*`; use `A.6.C`, `A.2.8`, and `A.2.9` for agreement-like wording when agreement, commitment, or speech-act claims are being made. |
| Dashboard tile, credential-status color, role-state color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecision` or `DecisionLogRef` plus `A.10` evidence relation and currentness relation. |
| Credential screenshot or badge used as deontic permission, authorization, role-assignment relation, role-state relation, or credential-status relation | Require `A.10` issuer, holder, verifier, credential-status, currentness, and relying-context fields, then the `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` source named by value for the required deontic permission, authorization, role assignment, role-state, credential-status, gate claim, or gate effect. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation relation and source-finding relation and `A.10` claim-bound source relation; issue, approval, gate, and commitment claims still need `A.2.9`, `A.21`, or `A.2.8`. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Require a typed `B.3` assurance claim, intended-use match, evaluation condition, limitations, and `A.10` evidence relation. Use `A.15.5` instead when the current claim is full-kit or work-entry readiness. |
| Provenance or attestation label cited as truth, safety, release, deontic permission, or authorization | Require `A.10` bounded provenance claim or process-trace claim plus separate evidence for truth, safety, release, deontic permission, authorization, or assurance. |
| Evidence, assurance, gate, or work-occurrence words without the governing source that carries that claim or effect | Recover the `A.10` evidence relation, `B.3` assurance claim, `A.21` gate decision, or `A.15.1` work-occurrence record respectively before the work claim or reliance claim is used. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover `A.21` decision or decision log plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Recover original `A.2.9` `SpeechActRef`, currentness, freshness, and any `A.2.8` commitment or `A.21` gate source needed for the claim. |
| Credential badge screenshot after revocation. | Treat as contested credential-currentness; use `A.10` issuer, holder, verifier, credential-status, and revocation relation and do not infer deontic permission or authorization. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation and source-finding and `A.10` claim-bound source relation; issuing, gate, and commitment claims still need their own sources. |
| Boundary wording says `guaranteed approved for production`. | Split through `A.6` or `A.6.B`; if agreement-like or promise-bearing, unpack through `A.6.C`, `A.2.8`, and `A.2.9`. |
| Dashboard says green while decision log says blocked. | Treat as conflicting sources; name source order, governing decision source, freshness policy, and supersession rule before the work claim or reliance claim is used. |
| CRISPR lab dashboard says the guide edit is ready. | Treat the dashboard as orientation or source-finding until the protocol, approval record or gate record, role-assignment source, evidence relation, current lab source, and `U.WorkPlan` for the intended edit are recoverable. If the question is full-kit or work-entry readiness for the intended edit, use `A.15.5`; the readiness tile still does not create biological-intervention authorization, deontic permission, safety, or performed work. |

