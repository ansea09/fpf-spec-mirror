---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:6"
section_title: "Archetypal Grounding (Tell-Show-Show; System and Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__008_archetypal-grounding-tell-show-show-system-and-episteme.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:6 — Archetypal Grounding (Tell-Show-Show; System and Episteme)"
line_start: 21638
line_end: 21678
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
  - "MethodDescription ≠ Method ≠ Capability ≠ Work"
  - "category error"
  - "system-role kind and assignment ≠ Work"
---

### A.7:6 - Archetypal Grounding (Tell-Show-Show; System and Episteme)

#### A.7:6.1 - System and Episteme example
**System archetype — “Digital‑twin vs asset”.**
*Claim:* *The twin (episteme) does not act; the System or acting holon that holds the assignment performs Work on the asset. Name the assignment occurrence and its declared `U.SystemRoleAssignment` species; evidence binds through A.10 carrier and source-currentness relations and evidence-provenance relations.*
*Show:* Claim-bearing episteme `MaintenanceGuide-e4` is a **MethodDescription** only because C.2.1 identifies it with exact maintenance Method `MaintenanceMethod-M1` as EntityOfConcern and its claims state substantive preconditions, actions, bounds and stops; its TechCard form and design-time authoring do not grant membership. A **Work** record (assurance face) lists Γ_time, Γ_work, PathId and **carrier** ids for telemetry. The twin’s update is **Work on the carrier**, not the asset; CL^plane penalties are disclosed when twin–asset crossings are analysed.

**Episteme archetype — “Peer‑review vs manuscript”.**
*Claim:* *A review is Work by a **system** (the reviewer) **on carriers** of an episteme (the manuscript).*
*Show:* Review episteme `PeerReviewGuide-e2` qualifies as **MethodDescription** only because its exact EntityOfConcern is admitted Method `PeerReviewMethod` and its claims state how that review is done; the SOP label alone proves nothing. The **Work** cites carrier ids (file/edition) and the selected episteme; arguments/rebuttals live on epistemes; acceptance gating lives in CAL, not in CHR cards.

#### A.7:6.2 - Didactic examples

**Example 1 — Pump in a cooling loop**

* **Substance (system):** Centrifugal pump P‑12.
* **System-role kind and assignment:** `CoolingCirculatorSystemRole@ThermalLoop-7`; `CoolingLoopCirculationAssignment-17 : CoolingLoopOperationAssignment` has pump P-12 as `HolderSystemSlot` and that kind as `AssignedSystemRoleKindSlot`.
* **MethodDescription membership:** episteme “Loop Circulation v3” has the circulation Method below as exact EntityOfConcern and claims the start → ramp → hold → stop way, conditions and bounds; its **TechCard** representation and publication timing do not establish membership. Cite A.10 carrier/source-currentness refs when evidence or source use is current.
* **Method:** ordered way-of-doing: start → ramp → hold → stop (Γ\_method).
* **Capability:** P-12 control-unit ability or envelope to enact that Method under the stated assignment, conditions, resources, and constraints.
* **Work:** run on 2025‑08‑09 10:00–10:45; energy ledger via Γ\_work; log via Γ\_time.
* **Safe phrasing:** *“Pump P-12, the holder in `CoolingLoopCirculationAssignment-17` to `CoolingCirculatorSystemRole@ThermalLoop-7`, had the **Capability** to enact the **Method** described by **MethodDescription**, and performed **Work** …”*
* **What not to write:** “The pump's function is its system role” (system-role kind and behaviour are different).

**Example 2 — Standard document cited in a design**

* **Episteme:** “Safety Standard S‑174”.
* **Carriers:** PDF and printed volume with A.10 carrier/source-currentness refs when the standard is used as source or evidence.
* **Use relation:** reference-use or constraint-source-use relation for the valve selection activity, named by its subject pattern.
* **System-role assignment for Work:** `ValveSelectionTransformerAssignment` is the declared species; it defines the holder and assigned-kind participant meanings, local kind domain, predicate, applicability, and occurrence identity. Occurrence `ValveSelectionAssignment-47` has `DesignTeamSelectionSystem` as holder and `TransformerSystemRole@ValveSelectionContext` as assigned-kind value. `ValveSelectionContext` resolves to the named ValveSelection practice boundary in that local kind's identity basis; the assertion may cite that boundary, but it is not an assignment participant.
* **MethodDescription membership:** episteme “Valve Selection SOP v5” has the valve-selection Method below as exact EntityOfConcern and claims the selection criteria, ordered checks, bounds and stop; the SOP label and citation alone establish neither episteme identity nor membership.
* **Method:** abstract valve-selection way-of-doing described by that SOP.
* **Capability:** design team's selection-service ability/envelope to enact the Method under the project conditions.
* **Work:** dated selection session that **used** the standard; the episteme did **not** act.

**Example 3 — Set vs team**

* **Set (MemberOf):** {Alice, Bob, 3.14} — a collection; **no behaviour** implied.
* **Collective system (team):** boundary, coordination **Method**, supervision **Work**; can be the holder in an obtaining occurrence such as `CoolingMaintenanceAssignment-8 : CoolingMaintenanceWorkAssignment`, whose declaration-local kind slot admits `CoolingMaintenanceSystemRole@ContextT`. Here `ContextT` denotes the named team-maintenance practice boundary used to identify that local kind; it is not an assignment participant.
* **Safe phrasing:** *“`CoolingMaintenanceAssignment-8 : CoolingMaintenanceWorkAssignment` obtains with `HolderSystemSlot = TeamT` and `AssignedSystemRoleKindSlot = CoolingMaintenanceSystemRole@ContextT`; TeamT performed Work W under that assignment.”*

