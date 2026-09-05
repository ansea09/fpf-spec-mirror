---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Domain-Concept Bridge"
section_id: "B.5.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__006_archetypal-grounding.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "B.5.3 — Domain-Concept Bridge"
  - "B.5.3:5 — Archetypal Grounding"
line_start: 41707
line_end: 41746
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.6.5"
  - "A.7"
  - "B.3.3"
  - "C.2.1"
  - "C.3"
  - "E.10.ROLE"
  - "E.17"
  - "E.24.UK"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "F.17 cell"
  - "basis relation"
  - "bounded use and loss"
  - "direct relation"
  - "domain vocabulary"
  - "source-local meaning"
---

### B.5.3:5 - **Archetypal Grounding**

A thermodynamics team models a heat engine.

* In the cited thermodynamics source, "thermodynamic system" names the engine under concern together with the boundary and state variables relevant to that local claim. Recover the same System already used elsewhere; the expression does not automatically name a kind or assignment.
* "Macrostate" makes a source-local claim about a state description or characteristic bundle over, for example, pressure, volume, temperature, and particle amount. State the effective scheme and units directly; recover an F.17 cell and its basis relation when the receiving claim needs them, and add a durable term row only when reuse needs one.
* "Control volume" may name a boundary or region relation. The claim must say which entity is bounded and which exchanges cross the boundary.
* "Free-energy objective" may name an objective claim, characteristic, or selection criterion. The claim must say which FPF value the decision uses.
* If the engine control System is assigned a locally defined heat-source-controller system-role kind, establish a separate obtaining occurrence of the declared `U.SystemRoleAssignment` species. The source-local meaning, classification, assignment, Work, claim scope, and time window remain separate.

Current physical-system claims in this example use `A.1` for system identity. `A.14` distinguishes the part and whole relations actually claimed; `A.22` defines how to identify a selected organization of already established constituents and direct relations. `A.3.4` identifies an actual bounded change when one is claimed. Use `B.1.6` for any work-resource aggregation needed here and `C.16` for measured characteristics.

The control-volume boundary and exchange claims require the applicable thermodynamic rule. If that rule is unavailable, retain the local description and name the missing rule rather than asserting the relation. Planned `C.1` (Sys-CAL) may later consolidate that guidance; it is not a current governor.


What this achieves:

* Domain constraints become reviewable without turning every domain word into a root kind.
* Verification can use the direct pattern for the recovered value: boundary discipline for a control volume, characteristic-space discipline for state variables, system-role-assignment discipline when an assignment is claimed, and publication-use or evidence-use discipline for reports and dashboards.
* The heat engine remains the same System when a power-plant architecture, finance model, safety case, and thermodynamics model all discuss it. Any actual F.9 relation states how two distinct local meanings correspond; the named receiving-use claim states which losses block that use.

The same expression can be reused in an architecture view, a requirements document, and a simulation model only after each local claim identifies its actual value. If the claims use distinct local meanings, test any required F.9 relation and its receiving use separately.

**Conformance Checklist**

* **CC-B5.3.1 (Recover the FPF value used by the claim):** The result names the exact FPF value or relation used by the current claim before treating a preferred expression as reusable.
* **CC-B5.3.2 (No kindhood by spelling):** A local expression, dotted name, table row, or diagram label does not become a U-kind. A needed durable kind requires its own E.24/E.24.UK and C.3 settlement from independent ontic and membership evidence.
* **CC-B5.3.3 (Role boundary):** When *role* wording changes the claim, E.10.ROLE first recovers whether it means a local system-role kind, classification, assignment, participation, responsibility, or ordinary language. Each resulting claim then uses its own FPF pattern.
* **CC-B5.3.4 (Relation and use boundary):** Claim an F.9 Bridge only when its exact endpoint cells and predicate make it obtain. State the receiving use, direction, applicable scope, tolerated loss, evidence or reliance basis, and return condition separately; shared spelling proves none of them.
* **CC-B5.3.5 (Description boundary):** If the local expression appears in a requirement, diagram, dashboard, report, or publication, use the direct description and publication patterns to keep the described entity, description episteme, publication form, and carrier distinct.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | What it looks like | Better FPF move |
| :--- | :--- | :--- |
| **Subtype explosion** | Every domain expression becomes a new root kind. | Keep the source-local claim as wording unless E.24.UK and C.3 establish a needed kind from independent ontic evidence. |
| **Magic synonym** | A table says "sensor = component" and is treated as identity or permission. | Recover each exact local claim and the FPF value used. If two distinct cells must be related, test the actual F.9 relation and judge the named use separately. |
| **Role-for-everything** | Evidence, status, local meaning, responsibility, and document use are all called roles. | Apply E.10.ROLE, then name the actual value or relation and use its direct pattern. A local system-role kind or assignment is only one possible result. |
| **Description collapse** | A diagram label is treated as the entity, interface, or method itself. | Keep entity, description episteme, representation scheme, and publication form distinct. |

