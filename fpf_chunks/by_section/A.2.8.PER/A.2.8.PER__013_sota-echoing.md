---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__013_sota-echoing.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:11 — SoTA-Echoing"
line_start: 6774
line_end: 6784
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "F.6"
  - "U.Work"
keywords:
  - "checked non-violation"
  - "exact policy rule or decision result"
  - "matching dated-work exercise"
  - "permission or prohibition conflict"
  - "policy-valid strong grant"
  - "weak non-prohibition finding"
---

### A.2.8.PER:11 - SoTA-Echoing

| Practice question | Current practice and source | FPF alignment | Disposition |
|---|---|---|---|
| How do weak and strong permission differ? | Moltmann (2024) distinguishes modal objects, strong permission, weak non-violation, and action satisfiers. | Separate frame-relative findings, instituted grants, and actual exercise; retain direct FPF owners. | **Adapt.** Do not import modal objects, truthmakers, or possible worlds as U-kinds. |
| How should permission, duty, and prohibition remain distinct? | W3C ODRL 2.2 (2018) models permission, prohibition, duty, assignee, action, constraint, and policy separately. | Keep beneficiary, action specification, policy, scope/window, and duty/prohibition owners explicit. | **Adapt.** FPF uses direct relations and epistemic findings rather than importing the ODRL information model wholesale. |
| What makes a policy decision usable? | NIST SP 800-207 (2020) and current policy-as-code practice separate subject, requested action, resource/context, current policy, and decision evidence. | Exercise eligibility and conflict use are bounded by exact beneficiary, action, context, scope/window, and current policy. | **Adapt.** A policy response or gate display is not itself an enduring grant. |
| How should digital permit evidence be relied on? | W3C Verifiable Credentials Data Model 2.0 (2025) separates issuer, holder, verifier, status, proof, and relying context. | Permit publications enter `A.10` evidence/currentness paths and do not replace the grant relation. | **Adapt.** Credential form supplies neither permission nor exercise by itself. |

These sources change the practical record and its failure results. They do not license a generic authorization kind, beneficiary kind, permit-as-relation shortcut, or automatic precedence rule.

