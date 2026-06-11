---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__005_solution.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:4 — Solution"
line_start: 1728
line_end: 1780
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:4 - Solution

We elevate **Role** to a first‑class semantic construct: a context‑bound *mask* (capability/obligation schema) worn by a holon. **Behaviour** and **resource deltas** live in **Method**/**Work**, not in the role itself.

#### A.2:4.1 - S‑level definitions (normative)

* **`U.Role`** — a **context-bound** capability/obligation schema that a holon **may bear (play)** for a time interval. A role has **no structural parts** (it does not participate in A.14 `partOf`) and **no resource deltas** of its own. Role refinement/bundling is expressed via in‑Context relations (`≤`, `⊥`, `⊗`) rather than mereology. *(A7 guard)*
* **`U.RoleAssignment`** — a first-class assignment record recording that a holon **bears (plays)** a role **in** a bounded context over an optional **Window**. Keep the signature aligned with **A.2.1 Role Assignment Standard**; governance metadata (authority/justification/provenance) is captured via `U.RoleAssigning` and the evidence graph (A.10).

```
U.RoleAssignment {
  holder        : U.Holon,
  role          : U.Role,
  context       : U.BoundedContext,
  window? : U.Window
  justification?: U.Episteme,  // why (standard, SOP, evidence)
  provenance?   : U.Method     // how assignment/verification was done (NOT the role's bound method set)
}
```

Short form (readable): `Holder#Role:Context@Window`.

> **Why a first-class assignment record?** It keeps identity (holon), function (role), context (semantics), and time (run-window) separate yet linked, preventing the substance/function conflation identified above. The early `playsRoleOf(Holon, Role, span)` relation in the draft is subsumed by `U.RoleAssignment` and extended with **Context** (and optional governance fields).

#### A.2:4.2 - Temporal & behavioural alignment

* **Method (intension) vs Work (occurrence).** A `U.Method` is a **design‑time, order‑sensitive capability**: what can be enacted, under which preconditions/invariants, with what admissibility/acceptance gates. A `U.Work` is the **dated, spatiotemporally bounded enactment** of such behaviour by a system bearing a role (A.15.1).
* **MethodDescription is representation (viewpoint), not “the method itself”.** `U.MethodDescription` is an `U.Episteme` that represents a method under an explicit **viewpoint**. Step‑graphs/scripts/workflows are one common viewpoint, but not universal. Other valid viewpoints include state‑machines, dynamical/solver/controller models, lab protocols, and quantum circuits/channels. A method itself **need not** admit a step decomposition; only a given description might.
* **Executable chain (who / what / how / when).** A **behavioural Role** is eligible/authorized for one or more Methods (design‑time, Context‑local). A Work is `isExecutionOf` a **specific MethodDescription version** (run‑time) and cites `performedBy = U.RoleAssignment`. Together, these anchors answer “what happened, by which method, under which role” without collapsing design‑time into run‑time.
* **Resource accounting lives in Work.** Only `U.Work` carries resource deltas (feeds Γ\_work); Roles/Methods/MethodDescriptions do not.

> **Lexical note (A.6.P trigger).** In the Role–Method–Work cluster, `bindsMethod` is a **technical token** meaning “Context‑local eligibility/authorization of a Role for a Method”. Do not use plain “bind/rebind” as umbrella prose for editing relationships; when describing edits, prefer explicit change classes (declare/withdraw/retarget/revise/rescope/retime/refreshWitnesses).

#### A.2:4.3 - Admissibility constraints (concept-level; non-deontic).

1. **Locality.** `role ∈ Roles(context)`. Outside its context, a role’s meaning is undefined.
2. **Structural‑mereology firewall.** No Role (nor Method or MethodDescription) may appear as a node in any A.14 `partOf` chain; holarchies are for substantial holons only. Role refinement/bundling (`≤`, `⊗`) and method relations (refinement, factorization, step/phase views) are **not** `partOf` and MUST NOT be rewritten into structural parthood.
3. **Multiplicity.** A holder may **bear** multiple roles concurrently; a role may be **borne** by many holders—subject to each context’s compatibility rules.
4. **Time anchoring.** `window` (if present) is non-empty and finite for run‑time claims; open‑ended assignments are allowed but must be traceably open‑ended from an assignment time (A.2.1). Design‑time bindings are timeless but **descriptions are versioned** via `U.MethodDescription` identity.
5. **Behavioural coherence.** For any `U.Work` window, the performer’s cited RoleAssignment and the executed MethodDescription must align in the **same Context**: `work.performedBy = RA`, `work.isExecutionOf = MD`, and `RA.role` is eligible/authorized for the Method represented by `MD`. *(No hidden role swaps; no implicit method drift.)*

#### A.2:4.4 - Taxonomic frame (within a context)

Within each `U.BoundedContext`, role names are organised as a **partial order** (refinements) plus an **incompatibility** relation (mutually exclusive roles). Typical **substrate‑neutral** anchors:

| Kernel Role       | Intent                                | System archetype              | Episteme archetype                       |   |
| ----------------- | ------------------------------------- | ----------------------------- | ---------------------------------------- | - |
| `TransformerRole` | Changes other holons via Method/Work. | Robot arm assembling casings. | Prover constructing a new lemma.         |   |
| `ObserverRole`    | Collects evidence and metrics.          | Sensor array on a test‑rig.   | Reviewer annotating an article.          |   |
| `SupervisorRole`  | Governs subordinate holons.           | PLC orchestrating a line.     | Meta‑analysis curator combining studies. |   |

> Domains refine these anchors: e.g., `CoolingCirculatorRole`, `CitationSourceRole`, `LemmaRole`.

