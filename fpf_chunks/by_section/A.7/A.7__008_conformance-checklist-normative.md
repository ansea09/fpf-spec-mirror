---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__008_conformance-checklist-normative.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:7 — Conformance Checklist (normative)"
line_start: 17978
line_end: 18001
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.2"
  - "A.21"
  - "A.3"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "Role ≠ Work"
  - "category error"
  - "ontology"
---

### A.7:7 - Conformance Checklist (normative)

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Practical test                                                                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑A7.1 (Role/Behaviour split)**       | A **Role** must be modelled as a contextual **mask** borne by a holon; **behaviour** must be expressed as **Method** (abstract way-of-doing), with **Capability** as the system ability/envelope to enact that Method under conditions and **Work** as the run-time occurrence.                                                                                                              | In any sentence, if “role” is used as if it *does* something, rewrite: the **system bearing TransformerRole** does it by enacting a **Method** through a **Capability** in **Work**. |
| **CC‑A7.2 (Transformer domain)**         | **TransformerRole SHALL be borne only by a system.**                                                                                                                                                                                                                                           | Type‑check: bearer ∈ `U.System`. “holon bearing TransformerRole” is invalid.                                                              |
| **CC‑A7.3 (Episteme non‑agency)**        | An **episteme SHALL NOT** be described as acting. All changes to epistemes must be routed to their **symbol carriers** (A.10) by a **system bearing TransformerRole**.                                                                                                                         | Text contains the acting system + carriers (SCR ids).                                                                                     |
| **CC‑A7.4 (MethodDescription ≠ Method ≠ Capability ≠ Work)** | **MethodDescription** (description episteme), **Method** (abstract way-of-doing), **Capability** (system ability/envelope to enact a Method under conditions), and **Work** (performed occurrence) **SHALL** be kept distinct in wording and modelling.                                                                                                                                                          | Ask: is there a MethodDescription or design-time publication, a Method, a Capability claim about a system, or a dated occurrence? Each live MethodDescription, Method, Capability claim, and dated Work occurrence must be named separately.                                         |
| **CC‑A7.5 (Operator fit)**               | Use **Γ\_method** only for composing **Method**; **Γ\_time** only for **Work** histories; **Γ\_work** only for resource spend/yields; **Γ\_sys** for systemic properties of systems.                                                                                                           | No sentence should use a single generic “process operator” for all three.                                                                 |
| **CC-A7.6 (SCR carrier reference)**      | Any knowledge claim that references documents or data **SHALL** cite **carriers** via **SCR/RSCR** on first mention in the subsection.                                                                                                                                                          | First mention expands as “Symbol-Carrier Register (SCR)”; references list carrier ids.                                                    |
| **CC‑A7.7 (Collective vs set)**          | If a grouping is expected to **act**, it **MUST** be modelled as a **collective system** (boundary + coordination Method + Work), not as a **MemberOf** set.                                                                                                                                   | Presence of boundary, Method, Work for the group.                                                                                         |
| **CC‑A7.8 (Diagram legend)**             | When domain idioms use **“process”**, diagrams or text **MUST** map them to FPF terms on first occurrence: *process (domain) ≡ Method at design time or Work at run time.*                                                                                                                           | Legend or parenthetical present at first use.                                                                                             |
| **CC‑A7.9 (Substance ⧧ Role wording)**   | The safe formula is **“System (substance) plays Role; under that Role it has Method; its execution is Work.”**                                                                                                                                                                                 | Sentences follow this order; “function” used only as synonym for **behaviour**, never for the **role**.                                   |
| **CC‑A7.10 (Quartet clarity)**           | Any “triad” picture **MAY** be used only as a **design‑time stand‑in** (Transformer + MethodDescription + Method) and **MUST** be accompanied by an explicit **Work** lane elsewhere in the same section. “quartet of quartets” headings **SHALL** be avoided; use **“Quartet backbone”** instead. | Diagram has a visible **Work** lane/timeline or separate box within the same section. |
| **CC‑A7.11 (Terminology hygiene)**       | Ban **“actor”** in core text. Use **“system bearing TransformerRole”**; bind local shorthand **“Transformer”** only per A.12 rules.                                                                                                                                                            | Plain text scan: no “actor”; shorthand is locally bound.                                                                                  |
| **CC‑A7.12 (Role domain guards)**        | Behavioural roles’ domain = **system**. Epistemes may bear **non‑behavioural** roles (e.g., ReferenceRole, ConstraintSourceRole) only.                                                                                                                                                         | Role declarations name their domain.                                                                                                      |
| **CC-A7.13 (EntityOfConcern-to-Description visibility)**          | Conforming `EntityOfConcern` and Description-episteme use makes `Describe_EoC_DescEp` recoverable and does not conflate it with MVPK, TGA, specification use or refinement, or Work steps. If a flow shows only publication faces and forms, the underlying `EntityOfConcern` and Description episteme are recoverable.       | EntityOfConcern and Description episteme are visible in text and diagrams; audit shows the describing operation and its construction/reference trace.                                                             |
| **CC-A7.14 (Describe_EoC_DescEp laws)** | Any implementation of `Describe_EoC_DescEp` MUST enforce the split DESC-1E/DESC-1N/DESC-2 law family. Episteme EoCs preserve or refine source claims under declared loss; non-episteme EoCs receive claims only through declared construction/reference/measurement/model/witness traces. Specification-use refinement is checked by the neighboring pattern governing the claim that grants the gate, not by A.7 as a third strict-distinction member. | Audit shows whether the EoC is episteme-like or non-episteme, which trace introduces claims, and which relation preserves identity, near-identity, bridge, loss, or retargeting. |
| **CC-A7.15 (Specification-use exit)**         | If text claims that a Description episteme is a specification, formal specification, requirement, acceptance item, harnessed invariant, or measurement-criterion object, it names the exact gate: C.2.3 formality plus checkable constraint, A.21/gate or acceptance discipline, C.16 measurement-criterion discipline, A.6.2 episteme refinement, E.17 publication expression of an already admitted specification use/refinement, E.10 suffix discipline, or another neighboring pattern governing the claim. Formal notation alone is insufficient.                                     | The text shows the specification-granting gate and does not make specification a peer ontology class beside EntityOfConcern and Description.                                                     |
| **CC-A7.16 (Γ-separation)**              | describing morphisms (`Describe_EoC_DescEp`), specification-use refinements, and publication-face or publication-form projections (MVPK) carry no cost/time semantics; **Γ\_method**, Γ\_time and Γ\_work belong to **Method, Work, or System**, not to description, specification-use refinement, or publication. Any aggregate on a card cites the Γ operator and policy.   | No ledger/time fields attached to `Describe_EoC_DescEp`, specification-use refinement, or MVPK publication steps; any “publication cost” is Work in a separate publication service.             |
| **CC‑A7.17 (Publication face and form discipline)**     | Publication names use the current publication face, form, unit, carrier, and rendering vocabulary. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are faces over epistemes or views; new `...PublicationFace` or `...PublicationForm` heads are not introduced as A.7 kinds in this ontology.                                                 | Token scan shows no ad‑hoc `...PublicationFace` or `...PublicationForm` kinds.                                                       |
| **CC‑A7.18 (Bridge+CL on crossings)**    | Any cross‑Context or cross‑plane content on a face **MUST** cite **Bridge id + CL** and **Φ policy‑ids**; penalties route to **R** only.                                                                         | Presence of Bridge ids and **Φ(CL)** and **Φ_plane** on TechCard or AssuranceLane.                        |
| **CC-A7.19 (UTS row reference)**         | Public names shown on faces **SHALL** point to **UTS rows** with twin labels (Tech/Plain), edition pins, and SCR carrier ids.                                                                                    | Face carries UTS row ids + edition pins.                                                          |

