---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__009_conformance-checklist-normative.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:7 — Conformance Checklist (normative)"
line_start: 21627
line_end: 21651
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
| **CC-A7.1 (System, system-role-kind, and behaviour split)** | A System acts because it satisfies A.1. A local system-role kind classifies it; an assignment occurrence relates it to that kind only when the direct assignment predicate obtains. Method, Capability, Work, transformation, kind, and assignment keep their separate meanings. | Accept ordinary actor wording when the System and contribution are recoverable; add classification, assignment, Capability, Method, or Work only for the stronger current claim. |
| **CC‑A7.2 (Transformer-system-role assignment domain)** | A suffixed source designation such as `TransformerSystemRole@ValveSelectionContext` is only a locator. The exact kind must first be recovered through its C.3 candidate domain, membership distinction, boundary probes, and continuity rule; the suffix identifies none of them. A direct `U.SystemRoleAssignment` species must then admit that kind in its declaration-local kind slot and systems in its holder slot. | Type-check the exact species, holder, kind domain, predicate, applicability, and occurrence identity; do not filter a permissive family value by a role label. |
| **CC-A7.3 (Episteme non-agency)** | An episteme does not act or hold a work-facing assignment. A System may author, revise, use, or publish it. | The ordinary sentence names the acting System; add exact Work, carrier, publication, evidence, source, or assignment relations only when the receiving claim uses them. |
| **CC‑A7.4 (MethodDescription ≠ Method ≠ Capability ≠ Work)** | **MethodDescription** is the same independently identified C.2.1 episteme only when its exact EntityOfConcern is one admitted Method and at least one substantive way-of-doing claim obtains; **Method**, **Capability**, and **Work** retain their separate meanings. Form, label, design-time status, authoring, revision, citation, publication, approval, or use time grants no membership. | Identify the episteme triple and apply the A.3.2 threshold; then name each current Method, Capability claim and dated Work occurrence separately. |
| **CC‑A7.5 (Operator fit)**               | Use **Γ\_method** only for composing **Method**; **Γ\_time** only for **Work** histories; **Γ\_work** only for resource spend/yields; **Γ\_sys** for systemic properties of systems.                                                                                                           | No sentence should use a single generic “process operator” for all three.                                                                 |
| **CC-A7.6 (Carrier/source-currentness reference)** | Any knowledge claim that references documents or data **SHALL** cite publication carriers or A.10 carrier/source-currentness refs when evidence, source, or reliance use is current. | First mention names the carrier or source-currentness reference and the evidence/source relation made recoverable by that reference. |
| **CC-A7.7 (Formal inclusion, collection, and collective)** | Mathematical set, tuple, coordinate, and other formal inclusion stays with `C.29`, `A.19`, or the applicable formal rule and creates no world-side relation. A world-side collection uses its own identity and belongs-to rule. A grouping claimed to act must separately pass all six `A.1` matters. | Check three separate statements. Infer neither belonging from formal inclusion nor parthood or holonhood from belonging; do not prohibit a separately grounded constructive part claim. |
| **CC‑A7.8 (Diagram legend)**             | When domain idioms use **“process”**, diagrams or text **MUST** map them to FPF terms on first occurrence: *process (domain) ≡ Method at design time or Work at run time.*                                                                                                                           | Legend or parenthetical present at first use.                                                                                             |
| **CC-A7.9 (Progressive actor wording)** | A contribution noun may stand for a recoverable System in ordinary prose. An assignment, local system-role kind, Capability, Method, or Work is added only when that exact distinction changes a receiving inference. | `The engineer designed the pump` may stand. For an attribution claim, separately identify the Work, assignment species and occurrence, and F.6 relation. |
| **CC-A7.10 (Work-facing chain clarity)** | A diagram shows only the positions used by its claim. MethodDescription membership, Capability, assignment, Work, and evidence are not inferred from a complete-looking chain. | Begin with the acting System and direct claim; expand the chain only for a named design, attribution, or reliance use. |
| **CC-A7.11 (Terminology hygiene)** | Avoid bare `actor` when the acting subject is known. Name the System directly or use a recognizable contribution noun. | Assignment identity is required only when a work-facing assignment claim is current; ordinary actor wording does not create one. |
| **CC‑A7.12 (System-role domain guards)** | Work-facing assignment species declare `HolderSystemSlot` for systems or acting holons and a local system-role-kind domain for `AssignedSystemRoleKindSlot`. Epistemes may be used through reference-use, constraint-source-use, evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, or gate-use relations, but those uses create neither a system-role kind nor an assignment. | Each assignment names its occurrence and declared species. The species defines participant meanings, predicate, applicability, and occurrence identity; the occurrence supplies holder, assigned kind, case applicability, and extent. Episteme uses name the relation. |
| **CC-A7.13 (EntityOfConcern and Description visibility)** | Each Description episteme is independently identified by complete claim content, exact EntityOfConcern, and effective ReferenceScheme. A.7 supplies no universal describing constructor. | Text or diagram keeps the EntityOfConcern and Description episteme visible and states any current authoring, measurement, observation, model, source-use, representation, or refinement relation separately. |
| **CC-A7.14 (Description-source discipline)** | A Description about an episteme does not automatically copy or preserve its claims; a Description about a non-episteme does not extract claims from the subject. | Name the exact source-use, representation, refinement, measurement, observation, model, authoring, or other relation that warrants the claim when that explanation is current. |
| **CC-A7.15 (Specification-use boundary)**         | If text claims that a Description episteme is a specification, formal specification, requirement, acceptance item, harnessed invariant, or measurement-criterion object, it names the exact gate: C.2.3 formality plus checkable constraint, A.21/gate or acceptance discipline, C.16 measurement-criterion discipline, A.6.2 episteme refinement, E.17 publication expression of an already admitted specification use/refinement, E.10 suffix discipline, or another neighboring pattern governing the claim. Formal notation alone is insufficient.                                     | The text shows the specification-granting gate and does not make specification a peer ontology class beside EntityOfConcern and Description.                                                     |
| **CC-A7.16 (Gamma separation)** | Description identity, specification use, and publication projection carry no execution cost or time actuals. | Any authoring or publication cost and time belongs to separately identified Work and its direct relations. |
| **CC‑A7.17 (Publication face and form discipline)**     | Publication names use the current publication face, form, unit, carrier, and rendering vocabulary. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are faces over epistemes or views; new `...PublicationFace` or `...PublicationForm` heads are not introduced as A.7 kinds in this ontology.                                                 | Token scan shows no ad‑hoc `...PublicationFace` or `...PublicationForm` kinds.                                                       |
| **CC‑A7.18 (Semantic and plane crossings).** | A face that relies on an obtaining semantic relation cites the two exact F.17 local senses, the F.9 Bridge, and a separate bounded-use claim; `CL` is optional. Cross-plane content cites the applicable plane relation. Context or plane difference alone creates no Bridge, `CL`, or penalty; any trust penalty cites the named current policy and its applicability to this use. | Audit resolves the exact semantic or plane relation and any current policy application without inferring one from labels, contexts, planes, cards, or `CL`. |
| **CC-A7.19 (UTS row reference)**         | Public names shown on faces **SHALL** point to **UTS rows** with twin labels (Tech/Plain), edition pins, and carrier/source-currentness refs when source or evidence use is current. | Face carries UTS row ids + edition pins plus the current source/evidence refs where needed. |
| **CC-A7.20 (Direct Method reference)** | An identifier's designation of one exact Method under an effective ReferenceScheme and a receiving claim's resolved `methodRef` remain separate from `U.MethodDescription` membership. Neither requires a description hop; `methodDescriptionRef` is optional and edition-specific only when the receiving claim uses that episteme's claims. | Resolve the identifier and receiving reference directly to the Method, then apply A.3.2 independently only for an actually cited description episteme. |

