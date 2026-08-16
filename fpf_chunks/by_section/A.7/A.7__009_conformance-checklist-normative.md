---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__009_conformance-checklist-normative.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:7 — Conformance Checklist (normative)"
line_start: 21679
line_end: 21703
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

### A.7:7 - Conformance Checklist (normative)

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Practical test                                                                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑A7.1 (System-role-kind and behaviour split)** | A local **system-role kind** is a `U.Kind` identified by a named practice or source boundary and stable work-facing contribution distinction; an assignment is one occurrence of a directly admitted `U.SystemRoleAssignment` species. Behaviour is expressed as **Method**, with **Capability** as the exact system's ability or envelope to enact that Method under stated conditions and **Work** as the run-time occurrence. | If wording makes the kind or assignment do something, rewrite it so the holder system performs the Work by enacting a Method through a Capability. |
| **CC‑A7.2 (Transformer-system-role assignment domain)** | A suffixed source designation such as `TransformerSystemRole@ValveSelectionContext` is usable only after the suffix resolves to the named practice or source boundary in the kind's identity basis and a direct `U.SystemRoleAssignment` species admits that exact local kind in its declaration-local kind slot and systems in its holder slot. | Type-check the exact species, holder, kind domain, predicate, applicability, and occurrence identity; do not filter a permissive family value by a role label. |
| **CC‑A7.3 (Episteme non‑agency)**        | An **episteme SHALL NOT** be described as acting or as the holder in a work-facing system-role assignment. Changes to epistemes are stated through publication, carrier, Work, evidence-provenance, and source-currentness relations: Work on carriers, publication updates, evidence-provenance relations, and source-currentness records under A.10/E.17/A.15. | Text contains the acting system or holon, Work occurrence, and carrier, publication, or evidence relation when change or evidence is claimed. |
| **CC‑A7.4 (MethodDescription ≠ Method ≠ Capability ≠ Work)** | **MethodDescription** is the same independently identified C.2.1 episteme only when its exact EntityOfConcern is one admitted Method and at least one substantive way-of-doing claim obtains; **Method**, **Capability**, and **Work** retain their separate meanings. Form, label, design-time status, authoring, revision, citation, publication, approval, or use time grants no membership. | Identify the episteme triple and apply the A.3.2 threshold; then name each current Method, Capability claim and dated Work occurrence separately. |
| **CC‑A7.5 (Operator fit)**               | Use **Γ\_method** only for composing **Method**; **Γ\_time** only for **Work** histories; **Γ\_work** only for resource spend/yields; **Γ\_sys** for systemic properties of systems.                                                                                                           | No sentence should use a single generic “process operator” for all three.                                                                 |
| **CC-A7.6 (Carrier/source-currentness reference)** | Any knowledge claim that references documents or data **SHALL** cite publication carriers or A.10 carrier/source-currentness refs when evidence, source, or reliance use is current. | First mention names the carrier or source-currentness reference and the evidence/source relation made recoverable by that reference. |
| **CC‑A7.7 (Collective vs set)**          | If a grouping is expected to **act**, it **MUST** be modelled as a **collective system** (boundary + coordination Method + Work), not as a **MemberOf** set.                                                                                                                                   | Presence of boundary, Method, Work for the group.                                                                                         |
| **CC‑A7.8 (Diagram legend)**             | When domain idioms use **“process”**, diagrams or text **MUST** map them to FPF terms on first occurrence: *process (domain) ≡ Method at design time or Work at run time.*                                                                                                                           | Legend or parenthetical present at first use.                                                                                             |
| **CC‑A7.9 (System identity ⧧ system-role-kind wording)** | The safe formula is: **one System or acting holon holds an assignment; name its occurrence and declared species. Under that assignment the System has the stated Capability for a Method; its execution is Work.** | Sentences follow this order; “function” is used only as a cue to recover the behaviour claim, never as a name for the system-role kind. |
| **CC-A7.10 (Work-facing chain clarity)** | Any “triad” picture **MAY** be used only as a design-time view, never as MethodDescription-membership or execution evidence. It may show the exact assignment holder and Method directly; it may add MethodDescription only after the independently identified episteme passes A.3.2 membership; and it **MUST** show explicit Capability and Work positions elsewhere in the same section. “quartet of quartets” headings **SHALL** be avoided; use **“work-facing chain”** instead. | Diagram has visible Method, Capability and Work positions and timeline; any MethodDescription box states its episteme, exact Method EntityOfConcern and substantive claim basis. |
| **CC‑A7.11 (Terminology hygiene)**       | Avoid **“actor”** as a bare core term. Use the exact acting system or holon plus one named occurrence of its locally admitted direct assignment species when a work-facing assignment is current. | Plain text scan: no bare “actor” in normative core claims; any local shorthand is bound through A.2 and A.2.1. |
| **CC‑A7.12 (System-role domain guards)** | Work-facing assignment species declare `HolderSystemSlot` for systems or acting holons and a local system-role-kind domain for `AssignedSystemRoleKindSlot`. Epistemes may be used through reference-use, constraint-source-use, evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, or gate-use relations, but those uses create neither a system-role kind nor an assignment. | Each assignment names its occurrence and declared species. The species defines participant meanings, predicate, applicability, and occurrence identity; the occurrence supplies holder, assigned kind, case applicability, and extent. Episteme uses name the relation. |
| **CC-A7.13 (EntityOfConcern-to-Description visibility)**          | Conforming `EntityOfConcern` and Description-episteme use makes `Describe_EoC_DescEp` recoverable and does not conflate it with MVPK, transformation-flow structure, specification use or refinement, or Work steps. If a flow shows only publication faces and forms, the underlying `EntityOfConcern` and Description episteme are recoverable.       | EntityOfConcern and Description episteme are visible in text and diagrams; audit shows the describing operation and its construction/reference trace.                                                             |
| **CC-A7.14 (Describe_EoC_DescEp laws)** | Any implementation of `Describe_EoC_DescEp` MUST enforce the split DESC-1E/DESC-1N/DESC-2 law family. Episteme EoCs preserve or refine source claims under declared loss; non-episteme EoCs receive claims only through declared construction/reference/measurement/model/witness traces. Specification-use refinement is checked by the neighboring pattern governing the claim that grants the gate, not by A.7 as a third strict-distinction member. | Audit shows whether the EoC is episteme-like or non-episteme, which trace introduces claims, and which relation preserves identity, near-identity, bridge, loss, or retargeting. |
| **CC-A7.15 (Specification-use boundary)**         | If text claims that a Description episteme is a specification, formal specification, requirement, acceptance item, harnessed invariant, or measurement-criterion object, it names the exact gate: C.2.3 formality plus checkable constraint, A.21/gate or acceptance discipline, C.16 measurement-criterion discipline, A.6.2 episteme refinement, E.17 publication expression of an already admitted specification use/refinement, E.10 suffix discipline, or another neighboring pattern governing the claim. Formal notation alone is insufficient.                                     | The text shows the specification-granting gate and does not make specification a peer ontology class beside EntityOfConcern and Description.                                                     |
| **CC-A7.16 (Γ-separation)**              | describing morphisms (`Describe_EoC_DescEp`), specification-use refinements, and publication-face or publication-form projections (MVPK) carry no cost/time semantics; **Γ\_method**, Γ\_time and Γ\_work belong to **Method, Work, or System**, not to description, specification-use refinement, or publication. Any aggregate on a card cites the Γ operator and policy.   | No ledger/time fields attached to `Describe_EoC_DescEp`, specification-use refinement, or MVPK publication steps; any “publication cost” is Work in a separate publication service.             |
| **CC‑A7.17 (Publication face and form discipline)**     | Publication names use the current publication face, form, unit, carrier, and rendering vocabulary. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are faces over epistemes or views; new `...PublicationFace` or `...PublicationForm` heads are not introduced as A.7 kinds in this ontology.                                                 | Token scan shows no ad‑hoc `...PublicationFace` or `...PublicationForm` kinds.                                                       |
| **CC‑A7.18 (Bridge+CL on crossings)**    | Any cross‑Context or cross‑plane content on a face **MUST** cite **Bridge id + CL** and **Φ policy‑ids**; penalties apply to **R** only.                                                                         | Presence of Bridge ids and **Φ(CL)** and **Φ_plane** on TechCard or AssuranceLane.                        |
| **CC-A7.19 (UTS row reference)**         | Public names shown on faces **SHALL** point to **UTS rows** with twin labels (Tech/Plain), edition pins, and carrier/source-currentness refs when source or evidence use is current. | Face carries UTS row ids + edition pins plus the current source/evidence refs where needed. |
| **CC-A7.20 (Direct Method reference)** | An identifier's designation of one exact Method under an effective ReferenceScheme and a receiving claim's resolved `methodRef` remain separate from `U.MethodDescription` membership. Neither requires a description hop; `methodDescriptionRef` is optional and edition-specific only when the receiving claim uses that episteme's claims. | Resolve the identifier and receiving reference directly to the Method, then apply A.3.2 independently only for an actually cited description episteme. |

