---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:8"
section_title: "Canonical rewrites (didactic library)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__009_canonical-rewrites-didactic-library.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:8 — Canonical rewrites (didactic library)"
line_start: 19769
line_end: 19781
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

### A.7:8 - Canonical rewrites (didactic library)

| Instead of (ambiguous)                           | Write (canonical)                                                                                                                               | Why                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| “The process enforced the rule.”                 | “The acting system under `U.RoleAssignment(..., roleRef=TransformerRole@Context, ...)` executed the **Method**; the **Work** cites evidence carriers ⟨ids⟩.” | Processes don’t act; systems or acting holons do. Evidence uses Work plus A.10 carrier/source-currentness relations. |
| “The specification decided to tighten limits.”   | “The design-control system under a current role assignment updated the **carriers** of the spec, producing **Work** at ⟨time⟩ and recording the A.10/E.17 carrier and publication relations.” | Epistemes are changed via carriers by systems or acting holons. |
| “Our role is pump; the role circulates coolant.” | “`U.RoleAssignment(holderRef=<system>, roleRef=CoolingCirculatorRole@Context, boundedContextRef=<context>)` is current; under this assignment the system has **Method** and **Capability** for coolant circulation; **Work** was executed ⟨when⟩.” | Role value is not behaviour; behaviour is Method/Capability and Work. |
| “We followed the blueprint, so it’s done.”       | “We have a **MethodDescription** and a **Method**; if ability is claimed, name the system **Capability** separately; completion is evidenced by **Work** with ⟨timestamps, outcomes⟩.”                                   | Description, Method, and Capability are not the occurrence.                      |
| “Team = set of members; it performed repair.”    | “The **team** is a **collective system** (boundary + coordination **Method**); it executed **Work** ⟨…⟩.”                                       | Acting groups must be systems, not sets.                  |
| “Process cost is tracked by Γ\_method.”          | “**Work** cost is tracked by **Γ\_work**; **Γ\_method** composes the **Method** (order/branching).”                                             | Operator alignment.                                       |
| “Holon has TransformerRole.”                 | “`U.RoleAssignment(holderRef=<system-or-acting-holon>, roleRef=TransformerRole@Context, boundedContextRef=<context>)`.” | The holder, role value, and bounded context must be explicit. |
| “Publication is a special mechanism.”            | “Publication = availability of existing Description epistemes, including Description epistemes admitted for specification use, through publication units, forms, and faces (MVPK); **describing** is `Describe_EoC_DescEp`, specification use or refinement is governed by the neighboring pattern governing the claiming gate, and any execution around them is separate **Work** by a **system** on **carriers**.” | Publication is not behaviour; it is a Description-episteme-to-publication availability relation in the model. |

