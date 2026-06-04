---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holonic Foundation: Entity → Holon"
section_id: "A.1:4"
section_title: "Solution - A three-part root (Entity -> Holon -> {System, Episteme})"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__005_solution-a-three-part-root-entity-holon-system-episteme.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "A.1 — Holonic Foundation: Entity → Holon"
  - "A.1:4 — Solution - A three-part root (Entity -> Holon -> {System, Episteme})"
line_start: 1161
line_end: 1216
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.14"
  - "A.2"
  - "B.1"
  - "U.Boundary"
  - "U.Episteme"
  - "U.Holon"
  - "U.System"
keywords:
  - "U.Episteme"
  - "U.System"
  - "entity"
  - "holon"
  - "part-whole composition"
  - "system boundary"
---

### A.1:4 - Solution - A three-part root (Entity -> Holon -> {System, Episteme})

FPF adopts a **three-part root ontology** refining Koestler’s “holon,” with crisp boundaries and safe composition.

#### A.1:4.1 - `U.Entity` — Primitive of Distinction
Anything that can be individuated and referenced. **No structural assumptions.** Use when you need to name “a something” without committing to having parts.

> **Naming note (mint vs reuse).** `U.Entity` and `U.Holon` are minted kernel terms: they reuse familiar words but intentionally diverge from domain‑specific ontologies and DDD “Entity”, so we can reason cross‑domain without importing hidden assumptions.

#### A.1:4.2 - `U.Holon` — Unit of Composition
A `U.Entity` that is *simultaneously* **(a)** a whole composed of parts and **(b)** a part within a larger whole. Formally, `U.Holon ⊑ U.Entity`.
Well‑formedness constraints:

* **WF‑A1‑1 (Single boundary).** A holon has **exactly one** `U.Boundary` that separates it from its environment.
* **WF‑A1‑2 (Γ domain).** The universal aggregation operator **Γ** is defined **only** on sets of `U.Holon` (never on bare `U.Entity`).
* **WF‑A1‑3 (Γ scope).** A Γ‑application is scoped to a declared context and a single declared temporal scope (design **or** run); order/time are routed to Γ\_ctx / Γ\_time (B.1.4).

These constraints make composition rules uniform across domains and prevent Γ from being misapplied.

#### A.1:4.3 - Interface primitives: `U.Boundary` & `U.Interaction`
Every holon is defined by **how** it is separated and **what** crosses the separation.

* **`U.Boundary`** — physical or conceptual surface delimiting the holon’s scope.
* **`U.Interaction`** — any flow of matter, energy, or information that crosses a boundary.
  **Canonical boundary kinds (with twin archetypes):**

| Kind          | Permitted exchanges             | `U.System` archetype               | `U.Episteme` archetype                                        |
| ------------- | ------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| **Open**      | Matter, energy, information     | Microservice exposing a public API | Public wiki editable by anyone                                |
| **Closed**    | Energy, information (no matter) | Sealed cooling loop in a server    | Version‑locked theory accepting new evidence but fixed axioms |
| **Permeable** | User‑filtered subset            | Cell membrane regulating ions      | Legal code allowing specific amendment classes only           |

This pair (`Boundary`, `Interaction`) makes interfaces explicit, reviewable, and testable across domains.

#### A.1:4.4 - Inside/Outside decision test
To decide whether an entity **E** is *inside* a holon **H**, apply:

1. **Dependency test:** removing **E** breaks a core invariant of **H**.
2. **Interaction test:** **E** participates in causal loops wholly within **H**’s boundary.
3. **Emergence test:** **E** contributes to a novel collective property warranting **H** as a single unit.
   Fail all three → **E** is *outside*. This practical triage prevents “scope creep” and forces explicit modeling of environment vs interior.

> **Collections vs collectives.** A set/collection of holons is not itself an acting unit. If a grouping is expected to act, model it as a `U.System` holon with its own boundary and attach roles/methods/work to that system (see CC‑A1.6; details in A.2 and A.15).

#### A.1:4.5 - Archetypal sub‑holons
FPF fixes two **archetypal** specializations to ground cross‑domain universality:

| Subtype                    | Essence                                                | Governing pattern |
| -------------------------- | ------------------------------------------------------ | ---------------- |
| **`U.System ⊑ U.Holon`**   | Physical, operational holon obeying conservation laws. | **Sys‑CAL**      |
| **`U.Episteme ⊑ U.Holon`** | Knowledge holon (axioms, evidence, argument graph).    | **KD‑CAL**       |

> **Agency rule.** Behavioural roles and executed methods/work attach to `U.System` holons only; `U.Episteme` is non-agentive claim-bearing holon. Any change to an episteme is performed by an external system acting across a boundary (cf. CC‑A1.5 and A.2/A.15).

*Naming guideline:* keep “**System**” and “**Episteme**” for practitioner comfort; reserve **Holon** for meta‑level discourse and formal signatures.

