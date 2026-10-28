---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__013_sota-echoing.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:8 — SoTA-Echoing"
line_start: 30703
line_end: 30717
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
| Dynamic authorization or policy-response displays need the requested operation and the policy conditions relevant to this use. | NIST SP 800-207 recommends resource access per session under dynamic policy. Cedar 4.5 evaluates a principal–action–resource–context request against policies and entity data. OpenFGA checks a user's modeled relation to an object using an authorization model and relationship tuples, with conditions and request context where applicable. | [NIST SP 800-207 Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf); [Cedar Policy Language Reference Guide v4.5](https://github.com/cedar-policy/cedar-docs/blob/ad5f61e979dbdb124c664ac9890da246a10aa0cf/docs/collections/_auth/authorization.md); [OpenFGA authorization concepts](https://openfga.dev/docs/concepts). | Name the attempted work or reliance use and the policy inputs it consumes, including the affected resource or work target, situation, policy edition and qualification window when material. Recover the direct permission or authority result required by that use. | Apply the actual policy, currentness and bounded-use conditions; reject treating policy-looking output as permission or authority by display alone. |
| Register-backed credential status or system-role-assignment state needs source and effect separation. | Verifiable Credentials Data Model 2.0 distinguishes issuer claims, holder presentations, credential verification and purpose-specific validation. Its `credentialStatus` property provides information for checking status under a selected scheme. Bitstring Status List v1.0 specifies how to retrieve and verify the referenced status-list credential and read the relevant status entry. | [W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/); [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) as one status scheme. | Treat the entry as authoritative source only under the named rule for its exact effect; test the direct relation or finding and the evidence and currentness claims separately. | Use the register under its named authority and status rule; verify issuer/holder binding, current status and the particular claim the intended use consumes. |
| Provenance and attestation marks need a checked link to the underlying assertions and a defined scope for using those assertions as evidence. | C2PA 2.4 binds provenance assertions to assets through signed claims and defines validation of their bindings and signatures. SLSA v1.2 build provenance describes a build's inputs, builder and execution; verification checks the artifact and provenance against trusted identities and expected values. in-toto Statement v1 binds a typed predicate to artifact subjects identified by digest. | [C2PA Specifications 2.4](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html); [SLSA v1.2 build provenance](https://slsa.dev/spec/v1.2/build-provenance) and [artifact verification](https://slsa.dev/spec/v1.2/verifying-artifacts); [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md). | Follow the mark to the independently established provenance or process-trace relation. Use A.10 for bounded reliance on it and the direct subject pattern for any further truth, release, permission, gate or Work claim. | Use validated provenance as evidence within its supported scope; reject inferring truth, release authorization, deontic permission, gate passage, assurance or work occurrence from a mark alone. |
| Change, gate, release, and approval displays need decision, schedule, and performed-work separation. | ISO/IEC/IEEE 15288:2023 describes system life-cycle processes; the historical ISO/IEC/IEEE 12207:2017 describes software life-cycle processes, activities and tasks. ITIL 4 Change Enablement addresses change-risk assessment, authorization and scheduling. ITIL 4 Release Management addresses making new or changed services available under organizational policies and agreements with service consumers. | [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) and the historical [ISO/IEC/IEEE 12207:2017](https://www.iso.org/standard/63712.html) life-cycle process frameworks; the latter was superseded by [12207:2026](https://www.iso.org/standard/90219.html). [ITIL 4 Change Enablement](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-practitioner-change-enablement-3794) and [Release Management](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-practitioner-release-management-3798). | An approval-looking display supports reliance only when it exposes the exact §3 branch object, `GateDecisionResult`, `U.WorkPlan`, or dated `A.15.1` Work occurrence required by the attempted use, plus the evidence/currentness relation needed for reliance. | Adopt decision, permission/authority, schedule, and performed-work separation; reject a green tile, copied approval, or generated explanation as any of those by appearance. |

**Source scope and FPF application.** The FPF applications and rejected shortcuts above are this pattern's adaptation of the cited contributions. Use §3 to identify the relation or result required for the intended reliance, then inspect the relevant content and case facts under its authority, evidence and currentness conditions. Verified provenance may support a Work claim within its recorded scope; a visible mark alone is insufficient.



