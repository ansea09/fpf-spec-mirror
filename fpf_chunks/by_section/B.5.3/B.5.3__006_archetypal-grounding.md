---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Role-Projection Bridge"
section_id: "B.5.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__006_archetypal-grounding.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "B.5.3 — Role-Projection Bridge"
  - "B.5.3:5 — Archetypal Grounding"
line_start: 34893
line_end: 34928
dependencies:
  - "A.2"
  - "C.3"
keywords:
  - "concept bridge"
  - "domain-specific vocabulary"
  - "mapping"
  - "terminology"
---

### B.5.3:5 - **Archetypal Grounding**

To illustrate the pattern in action, let's consider how we would bridge the domain of **classical thermodynamics** to the FPF kernel.

1.  **Define the Roles:** A domain expert creates a set of `Role`s, each refining a core `U.Type`:
    *   A `U.Role` named `ThermodynamicSystemRole` with `refinesType: U.System`. It might have a description: "A region of the universe under study, separated by a boundary."
    *   A `U.Role` named `MacrostateRole` with `refinesType: U.State`. Its description could specify that it is defined by variables (P, V, T, N).
    *   A `U.Role` named `ControlVolumeRole` with `refinesType: U.Boundary`.
    *   A `U.Role` named `FreeEnergyObjectiveRole` with `refinesType: U.Objective`.

2.  **Apply the Roles in a Model:** An engineer modeling a heat engine would then use these roles:
    *   They create an instance of `U.System` representing the engine and assert: `HeatEngine_Instance plays_role_of: ThermodynamicSystemRole`.
    *   They model the engine's state and assert: `EngineState_Instance plays_role_of: MacrostateRole`.
    *   They define the system's goal and assert: `EngineObjective_Instance plays_role_of: FreeEnergyObjectiveRole`.

**What this achieves:**

*   The model is now **semantically rich**. Tools can now understand that `HeatEngine_Instance` is not just any system, but one that should be analyzed using the laws of thermodynamics.
*   The model is **verifiable**. A tool could now check if an entity playing the `MacrostateRole` actually has attributes for Pressure and Temperature, enforcing domain-specific consistency.
*   The model remains **universally compatible**. Because `ThermodynamicSystemRole` refines `U.System`, the heat engine can still be reasoned about as a generic system in a wider context (e.g., in a model of the entire power plant).

**Conformance Checklist**

*   **CC-B5.3.1 (Role Grounding Mandate):** Every `U.Role` **MUST** be linked to exactly one universal `U.Type` via the `refinesType` relation. Orphaned roles are forbidden.
*   **CC-B5.3.2 (Explicit Role Assertion):** A domain-specific concept **SHALL NOT** be treated as a subtype of a `U.Type` directly. Its relationship **MUST** be expressed using the `plays_role_of` relation to a `U.Role`.
*   **CC-B5.3.3 (Multi-Role Flexibility):** A single entity **MAY** `play_role_of` multiple `Role`s simultaneously, even from different domains.
*   **CC-B5.3.4 (Semantic Integrity):** A `Role` **MAY** introduce additional constraints or required attributes that are more specific than those of the `U.Type` it refines, but it **SHALL NOT** contradict them.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Subtype Explosion"** | The list of system "types" in the project grows endlessly: `ThermodynamicSystem`, `EconomicSystem`, `SoftwareSystem`, etc. The ontology becomes bloated and unmanageable. | **CC-B5.3.2** forbids this. There is only one `U.System`. Different perspectives on it are modeled as `Role`s, which keeps the core ontology lean. |
| **The "Magic Synonym"** | A developer simply renames `U.System` to "Thermodynamic System" in their diagrams, but there are no formal rules or constraints attached. The term is just an alias. | The FPF pattern requires a formal `Role` with a `refinesType` link. This is a rich, structural connection, not just a cosmetic name change. |
| **The "One-Hat Fallacy"** | The model forces an entity to be only one thing. An asset can be a "Physical Component" or a "Financial Asset," but not both, leading to duplicated models. | **CC-B5.3.3** explicitly allows an entity to play multiple roles. A single server in your data center can simultaneously `play_role_of` "PhysicalComponent" (for Sys-CAL) and "DepreciableAsset" (for a financial mechanisms). |

