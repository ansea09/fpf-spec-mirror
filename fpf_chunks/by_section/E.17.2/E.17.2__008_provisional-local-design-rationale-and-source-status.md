---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
section_id: "E.17.2:7"
section_title: "Provisional local design rationale and source status"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__008_provisional-local-design-rationale-and-source-status.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "E.17.2 — TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
  - "E.17.2:7 — Provisional local design rationale and source status"
line_start: 82641
line_end: 82665
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.6"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24.PUB"
  - "U.View"
  - "U.Viewpoint"
  - "U.ViewpointRef"
keywords:
---

### E.17.2:7 - Provisional local design rationale and source status

This edition reports no N/U/C/D coordinate result, Pareto frontier, NQD harvest, or computed dominance comparison. The four TEVB positions are a provisional local authoring cut for routine holon description. They are retained because each changes a different immediate practitioner question and none is safely recoverable from another by label alone:

| Template position | Immediate question | Why the position is locally retained |
|---|---|---|
| functional | What transformations, capabilities, effects, and input/output boundaries characterize what H can or is intended to do? | Module structure does not determine function; procedure does not establish capability or effect; responsibility does not supply transformation semantics. |
| procedural | What methods, order, state, concurrency, failure, and recovery characterize how relevant behaviour unfolds? | Functional possibility does not determine order or recovery; a method mention does not make the holon-centred view a MethodDescription or performed Work. |
| module-interface | Which constituent holons, dependencies, interfaces, compatibility conditions, substitutability rules, and change boundaries characterize construction? | Similar function does not identify the same module organization, and a diagram or port label makes no module/interface relation obtain. |
| allocation-responsibility | Which exact Systems, local system-role kinds, current C.3.2 classification judgments, obtaining assignments, capabilities, transformations, and separately governed responsibility relations or structures are related to the behaviour? | Neither function nor procedure says which System counts under which kind for which signature edition and slice, is assigned, has capability, participates in the transformation, or bears responsibility. The view itself performs no Work and establishes none of those relations or judgments. |

The cut is deliberately small, not claimed complete. Serious omitted branches remain visible rather than being forced into the four:

| Omitted candidate family | Current local disposition |
|---|---|
| information/data | Orthogonal when data meaning, schema, information flow, or information lifecycle is the primary action-changing concern; author another exact local family rather than treating module-interface as data semantics. |
| safety/assurance | Orthogonal when hazard, safety, evidence, confidence, or reliance is current; use the applicable safety pattern, A.10 for evidence, and B.3 for assurance when those claims are current, and author a separate viewpoint family if recurring. Ordinary failure and recovery remain procedural without a universal assurance burden. |
| mission/context | Often ordinary target, use, or scope claims; author another family when mission or environment becomes a recurring independent comparison and selection concern. |
| deployment/operational | May use procedural, module-interface, and allocation positions together; author another family when deployment topology or operational environment changes a distinct recurring action. |
| business/usage/publication | Keep service, promise, stakeholder-use, and publication questions under their direct patterns; author another family only when their recurring concern cannot be represented without changing the TEVB positions. |

**Source status.** ISO 42010 is historical vocabulary lineage only. Function–behaviour–structure language is also lineage and a recognition aid, not evidence for this exact four-position cut. Query or projection production uses C.2.1 to identify the candidate episteme and A.6.3 to state its construction; it is not an external source for viewpoint selection. Responsibility/allocation is retained because it changes the practical question and avoids a recurrent function/actor collapse, not because an unreported engineering-practice harvest selected it. SysML v2 is deliberately not used as positive evidence or lineage for this selection: official status, search prominence, systems-oriented naming, and prospective scope do not supply a demonstrated current solution to this exact reusable-family problem. No unrelated modeling-language comparator is imported merely because it is current elsewhere.

**Reopen.** Re-run source selection and a bounded actual-use comparison when an exact current problem-solving source or exercised project result supplies a better reusable family; when routine project replay repeatedly needs one omitted branch at the same frequency and action impact as the four; when two retained positions cease to change different actions; or when the four-position template produces more selection work than it saves. Until such evidence exists, call the cut provisional local rationale and never a computed frontier.

