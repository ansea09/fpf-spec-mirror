---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Role-Projection Bridge"
section_id: "B.5.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__005_solution.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "B.5.3 — Role-Projection Bridge"
  - "B.5.3:4 — Solution"
line_start: 32671
line_end: 32698
dependencies:
  - "A.2"
  - "C.3"
keywords:
  - "concept bridge"
  - "domain-specific vocabulary"
  - "mapping"
  - "terminology"
---

### B.5.3:4 - **Solution**

FPF solves this with the **Role-Projection Pattern**, a mechanism that creates a robust, semantically rich **Concept-Bridge** between the universal kernel and domain-specific vocabularies. This pattern is built on three core components:

#### B.5.3:4.1 - The `Role` Concept

*   **Description:** FPF introduces a new universal type, `U.Role`. A `Role` is not a concrete thing but an **abstract, context-dependent role** that an entity can play. It represents the domain-specific *interpretation* of a universal concept.
*   **Example:** "Thermodynamic System" is not modeled as a new subtype of `U.System`. Instead, it is modeled as a `Role` that a `U.System` can *play* when it is being analyzed from a thermodynamic perspective.

#### B.5.3:4.2 - The `refinesType` Relation**

*   **Description:** Every `Role` **MUST** declare which universal `U.Type` it refines or specializes. This is done via the `refinesType` relation.
*   **Example:** The `ThermodynamicSystemRole` would have the relation `refinesType: U.System`. This creates a formal, unbreakable link to the kernel. It guarantees that any entity playing this role still inherits all the fundamental properties and invariants of a `U.System`. This is a many-to-one relationship: many different roles (e.g., `EconomicSystemRole`, `BiologicalSystemRole`) can all refine the same `U.System` type.

#### B.5.3:4.3 - The `plays_role_of` Relation**

*   **Description:** This relation connects a **concrete entity** in a model to a `Role`. It is the assertion that "this specific thing is currently playing that specific role."
*   **Example:** In a model of a steam engine, we would assert that our specific engine instance `plays_role_of: ThermodynamicSystemRole`. This assertion signals to all tools and reviewers that this engine should be interpreted as a `U.System` and that the rules and constraints associated with the `ThermodynamicSystemRole` now apply to it.

> **Didactic Note for Managers: From "Alias" to "Job Description"**
>
> The Role-Projection pattern is the difference between giving someone an alias and giving them a job description.
>
> *   **An Alias (the old way):** Simply says "Bob is also known as The Manager." It's just a name swap.
> *   **A Role (the FPF way):** Says "Bob `plays_role_of` Manager." This is much richer. It implies that Bob has specific responsibilities, authorities, and performance expectations that come with the "Manager" role. He might also play other roles, like "Mentor" or "Team Lead."
>
> Similarly, when we say a component `plays_role_of` "Sensor," we are not just renaming it. We are activating a rich set of expectations and rules that come with being a sensor (e.g., it must have an output port, it must have a defined accuracy, etc.). This makes our models smarter, safer, and more precise.

