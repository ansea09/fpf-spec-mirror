---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:6"
section_title: "Archetypal Grounding (Tell-Show-Show; System and Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__007_archetypal-grounding-tell-show-show-system-and-episteme.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:6 — Archetypal Grounding (Tell-Show-Show; System and Episteme)"
line_start: 19191
line_end: 19231
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "Role ≠ Work"
  - "category error"
  - "ontology"
---

### A.7:6 - Archetypal Grounding (Tell-Show-Show; System and Episteme)

#### A.7:6.1 - System and Episteme example
**System archetype — “Digital‑twin vs asset”.**
*Claim:* *The twin (episteme) does not “act”; the system or acting holon under a current `U.RoleAssignment` enacts Work on the asset; evidence binds through A.10 carrier/source-currentness and evidence-provenance relations.*
*Show:* A maintenance **MethodDescription** (tech card) lives at design‑time; a **Work** record (assurance face) lists Γ_time, Γ_work, PathId and **carrier** ids for telemetry. The twin’s update is **Work on the carrier**, not the asset; CL^plane penalties are disclosed when twin–asset crossings are analysed.

**Episteme archetype — “Peer‑review vs manuscript”.**
*Claim:* *A review is Work by a **system** (the reviewer) **on carriers** of an episteme (the manuscript).*
*Show:* The **MethodDescription** is the review SOP; the **Work** cites carrier ids (file/edition) and the selected episteme; arguments/rebuttals live on epistemes; acceptance gating lives in CAL, not in CHR cards.

#### A.7:6.2 - Didactic examples

**Example 1 — Pump in a cooling loop**

* **Substance (system):** Centrifugal pump P‑12.
* **Role:** **Cooling‑CirculatorRole**.
* **MethodDescription:** “Loop Circulation v3” (**TechCard**, cited through A.10 carrier/source-currentness refs when evidence or source use is current).
* **Method:** ordered way-of-doing: start → ramp → hold → stop (Γ\_method).
* **Capability:** P-12 control-unit ability/envelope to enact that Method under stated roles, conditions, resources, and constraints.
* **Work:** run on 2025‑08‑09 10:00–10:45; energy ledger via Γ\_work; log via Γ\_time.
* **Safe phrasing:** *“The **system** playing **Cooling‑CirculatorRole** (via the P‑12 control unit as **Transformer**) had the **Capability** to enact the **Method** described by **MethodDescription**, and executed **Work** …”*
* **What not to write:** “The pump’s function is the role” (role ≠ behaviour).

**Example 2 — Standard document cited in a design**

* **Episteme:** “Safety Standard S‑174”.
* **Carriers:** PDF and printed volume with A.10 carrier/source-currentness refs when the standard is used as source or evidence.
* **Use relation:** reference-use or constraint-source-use relation for the valve selection activity, named by its direct governing pattern.
* **Role assignment for work:** `U.RoleAssignment(holderRef=DesignTeamSelectionSystem, roleRef=TransformerRole@ValveSelectionContext, boundedContextRef=ValveSelectionContext)` when the selection work needs a work-facing transformer role value.
* **MethodDescription:** “Valve Selection SOP v5”.
* **Method:** abstract valve-selection way-of-doing described by that SOP.
* **Capability:** design team's selection-service ability/envelope to enact the Method under the project conditions.
* **Work:** dated selection session that **used** the standard; the episteme did **not** act.

**Example 3 — Set vs team**

* **Set (MemberOf):** {Alice, Bob, 3.14} — a collection; **no behaviour** implied.
* **Collective system (team):** boundary, coordination **Method**, supervision **Work**; can hold a current `U.RoleAssignment` for a work-facing role value such as `CoolingMaintenanceRole@Context`.
* **Safe phrasing:** *“`U.RoleAssignment(holderRef=TeamT, roleRef=CoolingMaintenanceRole@Context, boundedContextRef=ContextT)` is current for Work W…”*

