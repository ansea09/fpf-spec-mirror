---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__013_sota-echoing.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:8 — SoTA-Echoing"
line_start: 30560
line_end: 30574
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

### A.15.4:8 - SoTA-Echoing



| Claim need | Source contribution | Named source | FPF application | Shortcut rejected |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need requested operation named by value, affected resource or work target, situation, and window. | Dynamic authorization practice separates subject, requested operation, affected resource or work target, situation, and window before a relying use is allowed. | NIST SP 800-207 Zero Trust Architecture; Cedar Policy Language Reference Guide v4.5; OpenFGA authorization-modeling docs. | The local note names the attempted work or reliance use, affected resource or work target, policy version, situation, and time window before treating a visible allow or deny response as a source for work or reliance. | Adopt bounded currentness, source-relation, and bounded-use invariants; adapt them through FPF project records named by value; reject treating policy-looking output as permission or work-relevant source relation by display. |
| Register-backed credential status or system-role-assignment state needs source and effect separation. | Credential and status practice distinguishes issuer/holder claims, presentation and status checks; a register-backed use additionally needs the rule establishing that register's authority. FPF adds the separate Work and relation analysis when those claims are consumed. | W3C Verifiable Credentials Data Model v2.0 Recommendation and register-backed status practice. | Treat the entry as authoritative source only under the named rule for its exact effect; test the direct relation or finding and the evidence and currentness claims separately. | Adopt register authority and currentness checks; reject entry or display presence as the status, assignment-state relation, Work, exercise, non-violation, gate passage, permission, or authority itself. |
| Provenance and attestation marks need source relation and process-trace relation without becoming truth, release, or work evidence. | Provenance and attestation practice separates origin relation, process traceability relation, build claim, supply-chain claim, and verification metadata from truth of downstream claims, release authorization, or deontic permission. | C2PA Specifications 2.4 content provenance and attestations; SLSA v1.2 provenance; in-toto Statement v1 attestations. | Follow the mark to the independently established provenance or process-trace relation. Use A.10 for bounded reliance on it and the direct subject pattern for any further truth, release, permission, gate or Work claim. | Adopt source traceability and process traceability; reject provenance-mark-as-truth, release authorization, deontic permission, gate passage, assurance, or work occurrence. |
| Change, gate, release, and approval displays need decision, schedule, and performed-work separation. | Release and change practice separates approval/authorization acts, permission and authority objects, gate decisions, planned schedules, and performed work. | ISO/IEC/IEEE 15288:2023 and ISO/IEC/IEEE 12207:2017 life-cycle process separation; ITIL 4 Change Enablement and release/change practice. | An approval-looking display supports reliance only when it exposes the exact §3 branch object, `GateDecisionResult`, `U.WorkPlan`, or dated `A.15.1` Work occurrence required by the attempted use, plus the evidence/currentness relation needed for reliance. | Adopt decision, permission/authority, schedule, and performed-work separation; reject a green tile, copied approval, or generated explanation as any of those by appearance. |

**Digital-identity and provenance boundary.** The cited identity, provenance, policy, and change sources supply currentness, credential-status, system-role-assignment-state, provenance, and change-practice checks. They do not turn a credential, provenance label, attestation, policy response, register excerpt, or dashboard display into Work, gate passage, permission, authority, assurance, release, or another project relation. Use §3 to recover the exact relation or result and its applicable test before relying.



