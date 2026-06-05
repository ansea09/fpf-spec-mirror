---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__005_solution.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:4 — Solution"
line_start: 1371
line_end: 1413
dependencies:
  - "A.1"
  - "A.2.1"
  - "D.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "U.Boundary"
  - "U.BoundedContext"
  - "U.Holon"
keywords:
  - "DDD"
  - "context"
  - "domain"
  - "glossary"
  - "invariants"
  - "local meaning"
  - "semantic boundary"
---

### A.1.1:4 - Solution

FPF elevates **semantic framing** to a kernel primitive by introducing `U.BoundedContext` as a first-class holon of meaning.
Inspired by Domain-Driven Design (DDD) but generalized beyond software, a bounded context is not a mere namespace: it is **a governable model locale** with explicit vocabulary, rules, and role taxonomy.

#### A.1.1:4.1 - Term & Definition

* **Term:** `U.BoundedContext`
* **Definition:** A **`U.BoundedContext`** is a `U.Holon` that serves as an explicit **semantic frame of reference**. It declares a boundary within which a specific vocabulary, role taxonomy, and invariant set are coherent and authoritative. It is FPF’s kernel mechanism for localizing meaning and managing complexity by partitioning a larger conceptual space into smaller, coherent, independently governable **semantic locales** (Contexts).

**Mint vs reuse** (informative): The label "Bounded Context" is reused from DDD; `U.BoundedContext` is the FPF-defined kernel type (generalized beyond software). Cross-context sameness is never inferred from spelling; cross-context alignment is represented only via explicit `Bridge` records (F.9; E.10.U9; see CC-A1.1.5).

#### A.1.1:4.2 - Core components (normative shape)

A `U.BoundedContext` is a composite holon whose *parts* constitute the context’s local “constitution”:

* **`Glossary` (Local Lexicon):** A set of `U.Lexeme` entries (Lang-CHR) defining the local vocabulary and its intended senses. This is where a context can state: “Inside here, `ticket` denotes `U.WorkItem`, not `U.TravelPermit`.”
* **`Invariants` (Local Rules):** A set of `U.ConstraintRule`s (Norm-CAL) that must hold for holons and processes operating in this context. These rules define the context's local “physics”.
  * *Example (role compatibility):* “Within this context, a `holder` cannot simultaneously play `AuditorRole` and `DeveloperRole`.”
  * *Example (state transition):* “A `U.WorkItem` can transition from `InProgress` to `InReview`, never directly to `Done`.”
* **`Roles` (Local Taxonomy):** A partial order of `U.Role`s that are defined and valid only within this context. It specifies the “masks” available on this stage (A.2).
* **`Bridges` (Optional alignments):** A set of explicit cross-context relations (`U.Alignment`, formalized in F.9 / E.10.U9) describing how meaning translates when information crosses context boundaries, including loss/fit notes.
  * *Example (alignment):* “`AgileDevelopment:UserStory` is congruent (CL=1) to `FormalEngineering:Requirement` under the stated loss policy.”

#### A.1.1:4.3 - Context interactions with other kernel objects (normative)

* **As a `U.Holon`:** A `U.BoundedContext` has a defined `U.Boundary` and internal parts (`Glossary`, `Invariants`, …). However, **contexts do not form holarchies with each other**: per E.10.D1 (D.CTX), contexts have no is‑a or containment relations; cross-context relationships are expressed only via explicit `Bridges`.
* **As the semantic frame for `U.RoleAssignment`:** The `context` field of `U.RoleAssignment` identifies the unique semantic frame in which the holder-role assignment is interpreted (A.2.1).
* **As the scope carrier for rules and objectives:** `U.Objective`s and `U.ConstraintRule`s are typically authored and evaluated relative to a specific context’s invariants.
* **As a change target:** Context evolution (new invariants, revised glosses, deprecated roles) is modeled as a `U.Transformer` acting on the `U.BoundedContext` holon itself. Where time is merely stance (`design`/`run`), treat it as a TimeScope tag, not a new context (C‑7; D.CTX).

> *If meaning is local by design, then translation must be explicit by design.*

**Admissibility constraints (concept-level; non-deontic).**

* **BC‑1 (Holon nature).**  A `U.BoundedContext` is a `U.Holon` and declares a `U.Boundary`.
* **BC‑2 (Flat context map).** No `U.BoundedContext` is modeled as inheriting from, containing, or being contained by another `U.BoundedContext`; cross-context relations are represented only via explicit `Bridges` (E.10.D1 / E.10.U9).
* **BC‑3 (Role localization).** Every `U.Role` is defined in the `Roles` taxonomy of at least one `U.BoundedContext`; a "global role" is not a valid kernel object.
* **BC‑4 (Invariant scope).** Any invariant authored in a Context applies only to holons and processes operating within that Context; cross-context reuse is mediated by Bridges and re‑stated locally.
* **BC-5 (Bridge explicitness).** Any interaction or semantic alignment between two Contexts is represented by an explicit `Bridge` record.
* **BC-6 (RoleAssignment context field).** A `U.RoleAssignment` references exactly one `U.BoundedContext` in its `context` field (cardinality 1..1).
* **BC‑7 (Domain is metadata).** "Domain" denotes only an informative family label grouping multiple contexts; it is not a kernel type and does not substitute for `U.BoundedContext` (E.10.D1).

