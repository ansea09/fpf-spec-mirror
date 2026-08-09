---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__014_sota-echoing.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:12 — SoTA-Echoing"
line_start: 2967
line_end: 2974
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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

| Practice line | Source and status | FPF mutation | Practical consequence |
| --- | --- | --- | --- |
| Current foundational-ontology work keeps role-like classification, relation-participant distinctions, relation aspects, and situations from collapsing into one taxonomy. | Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint; used as a current comparator, not as an imported category hierarchy. | Keep `U.Role`, `U.RoleAssignment`, A.6.5 participant SlotKinds, role-state relations, and episteme-use relations distinct. FPF additionally applies its own constructive holon-admission test and does not admit `U.Role` as a holon. | A practitioner can model different assignments without creating system subtypes or role parts. |
| DDD makes model applicability local and describes Context Mapping as a method applied to actual model-use boundaries. | Eric Evans, [Domain-Driven Design Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), 2015 mature reference; Evans, [Context Mapping with an AI-based Component](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/), 2026 current worked practice. | Translate the action-facing DDD object to a selected `BoundedModelUseStructure`; keep Context Mapping as `U.Method` and its intended and performed work separate; designate the structure only in the receiving assertion or use whose interpretation it changes. | A pump assignment needs taxonomy and scheme; a DDD integration use names the selected structure without extending generic assignment identity. |
| FPF relation and episteme discipline keeps description and publication epistemes distinct from evidence, reliance, source-use, and publication relations and from the systems that perform work. | Current `C.2.1`, `A.6.REL`, `A.10`, `A.15.4`, and `E.17` pattern line. | Require a system holder for enactment-facing role assignment and keep each episteme in the direct relation that makes its use relevant. | A team can use a standard as the source for constraints and a report as evidence without either becoming the doer of work. |

