---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__014_sota-echoing.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:12 — SoTA-Echoing"
line_start: 2329
line_end: 2337
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:12 - SoTA-Echoing

| Practice line | Selected source examples | What FPF adopts | User-facing implication |
| --- | --- | --- | --- |
| Conceptual modeling with UFO and OntoUML treats roles as context-dependent, anti-rigid, relation-dependent descriptors rather than structural parts. | Guizzardi et al., "UFO: Unified Foundational Ontology", Applied Ontology 2022; current OntoUML and UFO conceptual-modeling practice. | Keep roles distinct from system kinds, mereological parts, and relation argument positions. | A project can name `VerifierRole` or `CoolingCirculatorRole` without creating a new system subtype. |
| Bounded-context practice in domain modeling treats role names as local to a context and unsafe across boundaries without translation. | Domain-driven design and socio-technical architecture practice around bounded contexts and explicit translation. | Require bounded context for role use and reject global role meaning. | Two teams can reuse the same role word only after context and alignment are named. |
| Assurance and evidence practice treats documents, standards, reports, datasets, and proofs as evidence or source objects rather than agents. | Safety, assurance-case, model-card, provenance, and evidence-management practice; ISO 26262:2018 and NIST SP 800-53 Rev. 5 are ordinary engineering examples. | Keep epistemes outside work-facing role holding. | A standard, model card, theorem, report, or dashboard can be evidence or source material without becoming the doer of work. |
| Relation and signature modeling treat argument positions as relation positions, not as social or work roles. | `A.6.5` SlotSpec discipline and ontology-design-pattern practice for typed relation positions. | Keep SlotKind and role value distinct. | "Argument role", "parameter role", and "field role" are repaired through relation-slot discipline before any role claim is made. |

