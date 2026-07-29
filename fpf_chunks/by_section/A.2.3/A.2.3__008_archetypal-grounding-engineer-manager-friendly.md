---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:5"
section_title: "Archetypal grounding (engineer‑manager friendly)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__008_archetypal-grounding-engineer-manager-friendly.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:5 — Archetypal grounding (engineer‑manager friendly)"
line_start: 3469
line_end: 3478
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.8"
  - "A.6.C"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "F.12"
  - "F.9"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Episteme"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
---

### A.2.3:5 - Archetypal grounding (engineer‑manager friendly)

| Domain | Promise-content episteme | Provider and consumer assignments | Access specification | Delivery work | Evidence and evaluation |
| --- | --- | --- | --- | --- | --- |
| Cloud storage | Store and retrieve blobs up to 5 TB under declared criteria—for example, 99.9% availability and 11x9 durability; these values illustrate targets and are not defaults. | `CloudStoragePlatformSystem` holds `StorageProviderRole`; `BackupControllerSystem` holds `StorageConsumerRole`, each through a named A.2.1 assignment occurrence. | `S3ApiDescription-vX`, a `U.MethodDescription`; the endpoint remains a separate `U.System`. | Dated PUT, GET, replication, and integrity-check work occurrences participating in `PromiseContentUse`. | Request and integrity observations enter direct evidence relations; actual evaluation applications bind availability or durability results, and separately constituted verdict epistemes state the judgments. |
| Manufacturing utility | Deliver compressed air at 8 bar in Zone B under stated pressure, flow, and purity criteria. | `CompressedAirPlantSystem` holds `UtilityProviderRole`; `LineBSystem` holds `UtilityConsumerRole`. | `ZoneBManifoldAccessDescription`, a `U.MethodDescription`; the manifold remains a separate `U.System`. | Dated compression and delivery work occurrences. | Pressure, flow, and purity observations support delivery claims; an actual evaluation application binds the comparison result under the declared scale and window, and a verdict episteme states the judgment. |
| Public passport service | Issue an admissible passport within 20 days under declared defect and eligibility criteria—for example, a ≤ 1% defect target; this value is illustrative, not a default. | `IssuingAgencySystem` holds `PassportIssuerRole`; `ApplicantPersonSystem` holds `PassportApplicantRole`. | `PassportApplicationAccessDescription`, a `U.MethodDescription`; portal and service desk remain access-point `U.System` values. | Dated application-handling and passport-issuance work occurrences. | Submission, issuance, elapsed-time, and defect observations support claims; actual evaluation applications bind lead-time or defect results, and separately constituted verdict epistemes state the judgments. |

**Key takeaway.** The same pattern yields one promise-content episteme in each domain without treating the promise as the provider, access point, method, work occurrence, evidence, operation-result binding, or verdict episteme. Direct role-assignment, `PromiseContentUse`, evaluation-operation, evidence, acceptance, and publication relations retain their own participants and governors; evaluation remains separately performed `U.Work`.

