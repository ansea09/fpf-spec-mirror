---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment: Contextual Role Assignment"
section_id: "A.2.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__002_problem-frame.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.2.1 — U.RoleAssignment: Contextual Role Assignment"
  - "A.2.1:1 — Problem frame"
line_start: 1742
line_end: 1755
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2"
  - "D.CTX"
  - "E.10.D1"
  - "E.10.D2"
  - "U.BoundedContext"
keywords:
  - "RCS/RSG"
  - "RoleEnactment"
  - "Standard"
  - "context"
  - "holder"
  - "role"
---

### A.2.1:1 - Problem frame

**Intent.** Provide one, universal, **context-local** way to say *who is being what, where (and when)* without altering what the thing **is**. The same grammar works for people, machines, software, teams, and **also** for epistemes when they hold **statuses** rather than perform actions.

**Scope.**

* Defines **`U.RoleAssignment`** (binding a **holder** holon to a **role** inside a **bounded context**, optionally within a **time window**).
* Separates that binding from **`U.RoleEnactment`** (the run‑time fact that a piece of **Work** was performed under that assignment).
* Names the **Role Characterisation Space (RCS)** and the **Role State Graph (RSG)** as **intensional** facets of a Role (recorded in its `RoleDescription`, upgraded to `RoleSpec` only after tests exist).
* Declares **eligibility** constraints so Roles apply to the right holon kinds, **without badge‑of‑badge chains** like “TransformerRole is assigned to be AgentRole”. If your Context wants taxonomic inheritance between role names, express it with in‑Context role algebra (`≤`), not via chained assignments.
* Declares **eligibility** constraints so Roles apply to the right holon kinds, **without badge‑of‑badge chains** like “TransformerRole is assigned to be AgentRole”. If a Context intends taxonomic inheritance between role names, that relation is expressed in‑Context via role algebra (`≤`), not via chained assignments.

**Non‑goals.** No storage models, no workflows, no org charts. This is a **thinking Standard**; all semantics are notation‑free.

