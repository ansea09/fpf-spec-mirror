---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__002_problem-frame.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:1 — Problem frame"
line_start: 74980
line_end: 75005
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.3.2"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "E.10"
  - "E.10.D1"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:1 - Problem frame

Use this pattern when one passage names an exact entity and also speaks of a description, specification, view, diagram, publication, file, dashboard, model, evidence item, assurance result, gate result, or decision around it. The recognizable failure is that the wording makes one of those neighboring objects stand in for the entity, the episteme, or the authority for the next action.

Begin with the receiving use:

1. What exact work, decision, comparison, inquiry, preservation, teaching, publication, or other use needs the description?
2. What is the next unresolved question or choice for that use? Do not invent one for a use that has none.
3. What exact claim content is being used?
4. What exact `U.Entity` is the `EntityOfConcern` of that claim-bearing whole?
5. Which effective `U.ReferenceScheme` supplies the designation and interpretation rules that make those claims readable about that entity?

The last three answers recover the C.2.1 `EpistemeConstitutionRelation`. If identity is all the receiving use needs, stop there. Otherwise open only the neighboring object or relation needed for the next visible sentence or action.

Not this pattern when the live question is already an exact evidence path, assurance claim, work occurrence, gate decision, commitment, Bridge, publication occurrence, representation correspondence, or state fact. Use its direct governor. Return here only if the wording also obscures which entity is being described or which episteme carries the claims.

The working distinctions are:

* the **EntityOfConcern** is the independently identified entity about which the selected claim-bearing whole makes its claims;
* a **description episteme** is an ordinary `U.Episteme` used to carry descriptive claims about that EntityOfConcern;
* a **describing use** names the receiving use and may select one exact viewpoint when that selection changes what is read or checked; selection changes neither episteme identity nor conformance;
* **specification use** is a checkable use of a description episteme, not a third peer ontology class;
* viewpoint, view, claim scope, model-use structure, grounding, evidence, edition, publication, carrier, and representation remain neighboring objects and relations.

This buys a small practical result: the reader can say what is described, which claim-bearing episteme is being used, what the receiving use needs next, and where any additional claim is governed. A formal-looking file, card, suffix, approval, or diagram gains no ontological or practical authority by appearance.

