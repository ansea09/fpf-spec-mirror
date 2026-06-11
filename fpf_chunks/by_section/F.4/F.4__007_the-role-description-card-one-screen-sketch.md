---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description (RCS + RoleStateGraph + Checklists)"
section_id: "F.4:6"
section_title: "The Role Description Card (one‑screen sketch)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__007_the-role-description-card-one-screen-sketch.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "F.4 — Role Description (RCS + RoleStateGraph + Checklists)"
  - "F.4:6 — The Role Description Card (one‑screen sketch)"
line_start: 71055
line_end: 71088
dependencies:
  - "A.11"
  - "A.2.1"
  - "A.7"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "E.10.D2"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.RoleAssignment"
  - "U.Types"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:6 - The Role Description Card (one‑screen sketch)

> Each bullet is a **thought‑item**, not a file field.

**Header**

* **Template kind:** **Role** | **Status**
* **Label pair:** **Tech** (idiomatic) - **Plain** (didactic)  *(naming discipline in F.5)*
* **SenseCell:** `⟨ContextId, Local‑Sense label⟩`

**Applicability**

* **Holder scope:** what can wear/bear it (e.g., *U.System*, *U.Work*, *U.MethodDescription*, *U.Episteme*).
* **Time stance:** **design** / **run** aligned to the Context (F.1).
* **Preconditions (Context‑true):** crisp conditions that must already be true in the Context’s idiom.

**Invariants (minimal)**

* **Behavioural invariants (Role)** *or* **Evaluation invariants (Status)** — 2–5 short lines stating what **must** hold after assignment/assertion, using the Context’s vocabulary and SenseCells where needed.
* **Separation guard:** a one‑line reminder of what this template **does not** imply (prevents senseFamily mixing).

**Consequences (informative)**

* **Typical interactions:** which **Method/Execution/Observation** constructs (by SenseCell) this template usually touches — *names only*.
* **Common misreads (trip‑wire):** 1–2 bullets to prevent known confusions.

> **Memory rule:** If your card can’t be read in **under two minutes**, you are writing a manual, not a template.

**Autonomy hooks (when Role may act autonomously)**
* **RCS additions (illustrative):** `AgencyLevel ∈ {None, Assisted, Delegated, Autonomous}`, `SafetyCriticality ∈ {SC0..SC3}`.
* **RSG gate:** mark which **states are enactable under autonomy** (cf. A.2.5); link to `AutonomyBudgetDeclRef`.
* **References:** If autonomy is claimed for this Role, the Role Description **MUST** reference: `AutonomyBudgetDeclRef` (id, version), `Aut-Guard policy-id (PolicyIdRef)`, `OverrideProtocolRef`.
* **Checklist:** include a **pre‑enactment** checklist item “Autonomy Green‑Gate passed” (guard verdicts present).

