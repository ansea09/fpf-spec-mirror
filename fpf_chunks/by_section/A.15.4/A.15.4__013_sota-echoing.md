---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Source Restoration"
section_id: "A.15.4:8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__013_sota-echoing.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.15.4 — Work-Relevant Source Restoration"
  - "A.15.4:8 — SoTA-Echoing"
line_start: 22740
line_end: 22754
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

### A.15.4:8 - SoTA-Echoing

**SoTA alignment rule.** Interpret each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and relations of this pattern.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need requested operation named by value, affected resource or work target, context, and window relation. | Dynamic authorization practice separates subject, requested operation, affected resource or work target, context, and window before a relying use is allowed. | NIST SP 800-207 Zero Trust Architecture; Cedar Policy Language Reference Guide v4.5; OpenFGA authorization-modeling docs; source maturity = current standards, specifications, and widely used technical practice. | The restoration note names the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair, the affected resource or work target, affected claim when one is being made, policy version, context, and time window before treating a visible allow response, deny response, or policy response as a relation-governed work or reliance source. | **Adopt, adapt, reject.** Adopt bounded currentness, source-relation, and relation-governed-use invariants; adapt them through FPF project records named by value; reject treating policy-looking output as permission or work-relevant source relation by display. |
| Credential or register-backed credential-status or role-state needs issuer, holder, verifier, currentness, and relying-context fields. | Credential and state practice separates issuer, holder binding or subject binding, verifier context, relying context, proof result or credential-status result, governing register entry, revocation, freshness, and effective window. | W3C Verifiable Credentials Data Model v2.0 Recommendation and current digital identity or register-backed status practice; source maturity = current specifications and technical practice. | A credential view, credential-status tile, or role-state tile can carry only the holder claim, credential-status claim, role-state claim, or currentness claim whose issuer, register, proof result or credential-status result, revocation, freshness, and relying context are recoverable. | **Adopt, adapt, reject.** Adopt credential-currentness, role-state-currentness, and source-currentness separation; reject treating a badge, screenshot, or register excerpt as role assignment, deontic permission, gate passage, or work reliance without the governing source for that claim or effect. |
| Provenance and attestation marks need source relation and process-trace relation without becoming truth, release, or work evidence. | Provenance and attestation practice separates origin relation, process traceability relation, build claim, supply-chain claim, and verification metadata from truth of downstream claims, release authorization, or deontic permission. | C2PA Specifications 2.4 content provenance and attestations; SLSA v1.2 provenance; in-toto Statement v1 attestations; source maturity = current standards, specifications, and widely used practice. | A provenance or attestation mark remains source relation or process-trace relation until `A.10`, `B.3`, `A.20`, `A.21`, `A.15.1`, or another source relation named by value carries the downstream claim. | **Adopt, adapt, reject.** Adopt source traceability and process traceability; reject provenance-mark-as-truth, release authorization, deontic permission, gate passage, assurance, or work occurrence. |
| Change, gate, release, and approval displays need decision, schedule, and performed-work separation. | Release and change practice separates approval acts, authorization acts, gate decisions, planned schedules, and performed work. | ISO/IEC/IEEE 15288:2023 and ISO/IEC/IEEE 12207:2017 life-cycle process separation; ITIL 4 Change Enablement and current release and change practice; source maturity = current life-cycle standards plus mature service-management practice. | A dashboard or approval-looking display supports reliance only when it exposes the `GateDecision`, `SpeechAct`, `Commitment`, `U.WorkPlan`, or `A.15.1` work-occurrence source that carries the claim named by value or effect. | **Adopt, adapt, reject.** Adopt decision, schedule, and performed-work separation; reject a green tile, copied approval, or generated explanation as rollout, release, or work reliance by appearance. |

**Digital-identity and provenance boundary.** The W3C Verifiable Credentials, C2PA, SLSA, in-toto, Cedar-style, Zanzibar-style, NIST, and ITIL sources are used for currentness, credential-status, role-state, provenance, authorization-source fields, and change-practice fields. They do not turn a visible credential, provenance label, attestation, policy response, register excerpt, or dashboard display into work occurrence, gate passage, deontic permission, assurance, release, or project claim relation without the governing source required by `A.15.4`, `A.15`, `A.10`, `B.3`, `A.20`, or `A.21`.

The nearest recovery references are the worked dashboard and approval examples, `CC-A15.4-1`, `CC-A15.4-2`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, and `A.15.1`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for the local `A.15.4` rule.

