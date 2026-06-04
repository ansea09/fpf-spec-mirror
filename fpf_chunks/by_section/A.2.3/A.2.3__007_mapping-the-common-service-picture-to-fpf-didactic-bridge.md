---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:6"
section_title: "Mapping the common “service” picture to FPF (didactic bridge)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__007_mapping-the-common-service-picture-to-fpf-didactic-bridge.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:6 — Mapping the common “service” picture to FPF (didactic bridge)"
line_start: 2789
line_end: 2805
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.3.1"
  - "A.3.2"
  - "A.6.8"
  - "A.6.C"
  - "E.10"
  - "F.12"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Scope"
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

### A.2.3:6 - Mapping the common “service” picture to FPF (didactic bridge)

The popular service diagrams (provider ↔ access ↔ use ↔ capability/activity) map to FPF as follows:

* **Agent (as Service Provider)** → `System#ServiceProviderRole:Context` (`U.RoleAssignment`).
* **Service Level Objective (SLO)** / acceptance targets → `U.PromiseContent.acceptanceSpec` (+ optional `WorkPlan` for windows).
* **Service Level Agreement (SLA)** (binding obligation) -> `U.Commitment` referencing the relevant `U.PromiseContent` (and, where needed, its acceptance/evidence specs); use **A.6.C Contract Bundle** when packaging “the SLA” as a bundle of commitments, evidence specs, and publication carriers.
* **SLA document / published terms** → `U.SpeechAct` (promise/offer act) + the clause carrier (`U.Episteme`), per A.2.9 + A.7.
* **Operating conditions / “where the promise holds”** → `claimScope : U.ClaimScope (G)` (or embedded in `acceptanceSpec`) per A.2.6.
* **Subject of service (“customer material”: asset/data/person/case whose state is changed)** → `promisedOutcomeSpecRef.resultSpec.entityOfConcernRef` (and the affected referents in delivery `U.Work.Δ`). “Ours vs theirs” (ownership/custody) is modeled as a **role/relationship inside the Context** (e.g., `OwnerRole:…`, `CustomerRole:…`, operated‑by/owned‑by), not as a Kernel‑global property.

* **Service Presence / Access** → `accessSpec : MethodDescription` (interface/eligibility); actual endpoints are **systems** playing interface roles.
* **Individual Service Use** → **consumer and provider `U.Work`** instances linked to the `U.PromiseContent` they fulfil.
* **Service‑Enabled Capability / Activity** → effects on the consumer side: either a **Capability** gained/used, or **Work** performed; do **not** reify as a new kernel type.

(Where a domain needs richer structures—catalogs, exposure layers, charging, entitlement—model them **in the domain context** and relate them to `U.PromiseContent` via `U.RoleAssignment` and alignment bridges.)

