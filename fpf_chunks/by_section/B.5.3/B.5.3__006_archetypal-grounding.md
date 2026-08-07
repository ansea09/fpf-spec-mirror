---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Domain-Concept Bridge"
section_id: "B.5.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__006_archetypal-grounding.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "B.5.3 — Domain-Concept Bridge"
  - "B.5.3:5 — Archetypal Grounding"
line_start: 40954
line_end: 40991
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.7"
  - "B.3.3"
  - "C.2.1"
  - "C.3"
  - "E.17"
  - "E.24.UK"
  - "F.1"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "bounded context"
  - "bridge scope"
  - "concept bridge"
  - "domain vocabulary"
  - "local sense"
  - "role assignment boundary"
---

### B.5.3:5 - **Archetypal Grounding**

A thermodynamics team models a heat engine.

* "Thermodynamic system" names the engine as the entity under thermodynamic concern in the current bounded context. The bridge points to the same system or holon already used elsewhere, plus the thermodynamic boundary and state variables that matter here. It is not automatically a role.
* "Macrostate" names a state description or characteristic bundle over pressure, volume, temperature, and particle amount. The bridge records the reference scheme and units.
* "Control volume" may name a boundary or region relation. The bridge must say which entity is bounded and which exchanges cross the boundary.
* "Free-energy objective" may name an objective claim, characteristic, or selection criterion. The bridge must say which FPF value the decision uses.
* If the engine control system is assigned the role of heat-source controller in a work context, that is a separate `U.RoleAssignment(holderRef, roleRef, boundedContextRef)` claim.

Current physical-system claims in this example use `A.1` for system identity, `A.14` and `A.22` for composition and boundary relations, `A.3.4` for state and dynamics, `B.1.6` for work-resource aggregation, and `C.16` for measured characteristics. Planned `C.1` (Sys-CAL) may later consolidate that guidance; it is not a current governor.


What this achieves:

* Domain constraints become reviewable without turning every domain word into a root kind.
* Verification can use the governing pattern for the recovered value: boundary discipline for a control volume, characteristic-space discipline for state variables, role-assignment discipline for controller work, and publication-use or evidence-use discipline for reports and dashboards.
* The heat engine remains the same system or holon when a power-plant architecture, finance model, safety case, and thermodynamics model all discuss it. Bridges record which local meanings travel across those contexts and which losses block substitution.

The same local word can be reused in an architecture view, a requirements document, and a simulation model only after the bridge states whether those uses point to the same entity, the same characteristic, the same role assignment, or merely related descriptions.

**Conformance Checklist**

* **CC-B5.3.1 (Recover the FPF value used by the claim):** A bridge row names the current FPF value or slot relation before naming the preferred wording.
* **CC-B5.3.2 (No kindhood by spelling):** A local term, dotted name, table row, or diagram label does not become a U-kind unless admission under `E.24.UK` and `C.3` supplies the ontic and the needed slot relation.
* **CC-B5.3.3 (Role boundary):** Role language is used for system or holon role assignments in bounded work and method contexts; other uses are expressed through their own FPF values or relations.
* **CC-B5.3.4 (Scope and loss):** A bridge records context, scope, loss, and return conditions; it does not claim lossless sameness by name alone.
* **CC-B5.3.5 (Description boundary):** If the local word appears in a requirement, diagram, dashboard, report, or publication, the bridge keeps the described entity distinct from the description and publication form.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | What it looks like | Better FPF move |
| :--- | :--- | :--- |
| **Subtype explosion** | Every domain term becomes a new root kind. | Keep the local term in its context unless admission under `E.24.UK` and `C.3` proves durable kindhood. |
| **Magic synonym** | A table says "sensor = component" with no scope or loss. | Write a bridge row naming the FPF value used by the claim, context, admissible use, and return trigger. |
| **Role-for-everything** | Evidence, status, domain interpretation, and document use are all called roles. | Use role assignment only for systems or holons in work-facing contexts; use episteme, publication, evidence-use, status-use, characteristic, method, or work vocabulary for the value being claimed. |
| **Description collapse** | A diagram label is treated as the entity, interface, or method itself. | Keep entity, description episteme, representation scheme, and publication form distinct. |

