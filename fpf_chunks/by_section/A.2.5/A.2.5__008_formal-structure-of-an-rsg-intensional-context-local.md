---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "U.RoleStateGraph: The Named State Space of a Role"
section_id: "A.2.5:7"
section_title: "Formal structure of an RSG (intensional, context‑local)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__008_formal-structure-of-an-rsg-intensional-context-local.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.2.5 — U.RoleStateGraph: The Named State Space of a Role"
  - "A.2.5:7 — Formal structure of an RSG (intensional, context‑local)"
line_start: 3465
line_end: 3485
dependencies:
  - "A.15"
  - "A.2.1"
  - "A.2.3"
  - "B.3"
  - "E.10.D1"
  - "F.9"
  - "U.RoleAssignment"
  - "U.RoleDescription"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:7 - Formal structure of an RSG (intensional, context‑local)

> **Definition.** For a given **`U.Role`** in a given **`U.BoundedContext`**, its **`U.RoleStateGraph`** is the tuple
> `RSG(Role, Context) = ⟨S, S_en, T, Guard, init?⟩`, where:

* **`S`** — a **finite set of named States** (`StateName ∈ Tech register`, with a Plain label). Names are **local to `(Role, Context)`**.
* **`S_en ⊆ S`** — the subset of **enactable** states (“green lights”). States in `S \ S_en` are **status‑only** (not enactable).
* **`T ⊆ S × S`** — a set of **typed transitions** `sᵢ → sⱼ`. Transitions are optional; the RSG may be acyclic or cyclic.
* **`Guard`** — for each transition (and optionally for state maintenance), a **predicate over**:

  * the role’s **RCS snapshot** at a **Window** (values on named characteristics; see A.2.3), and
  * **Context events** (e.g., presence of a `U.SpeechAct`, freshness of `U.Observation`, validity of a prior `U.Evaluation`).
* **`init? : S → {true,false}`** — optionally marks **initial** state(s). (Useful for state-sequence descriptions; not required for gating.)

**Naming discipline (RSG‑N1…N3).**

1. **RSG‑N1 (Minimal set).** `|S| ≥ 1`. At least **one** state must exist; if **no** state is enactable, the role is **status‑only** in this Context.
2. **RSG‑N2 (Disjoint labels).** State names are **unique** within `(Role, Context)`; reusing global labels (e.g., “Ready”) across contexts is allowed **only** via Bridges (F.9).
3. **RSG‑N3 (Human scale).** For didactics, **≤ 7 states** is the default target; exceeding it requires a one‑sentence rationale (“distinct gate we will actually use”).


