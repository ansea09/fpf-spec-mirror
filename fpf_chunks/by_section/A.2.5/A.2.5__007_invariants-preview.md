---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "U.RoleStateGraph: The Named State Space of a Role"
section_id: "A.2.5:6"
section_title: "Invariants (preview)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__007_invariants-preview.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.2.5 — U.RoleStateGraph: The Named State Space of a Role"
  - "A.2.5:6 — Invariants (preview)"
line_start: 3457
line_end: 3464
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

### A.2.5:6 - Invariants (preview)

1. **Locality.** `RSG(Role, Context)` is defined **only** within that `U.BoundedContext`.
2. **Finiteness.** The **State** set is finite and named.
3. **Checklist pairing.** Every State has a **Checklist** in the Role’s **RoleDescription**; every enactable State has **at least one** observable criterion.
4. **Green‑gate discipline.** A Method step requiring `Role` may proceed **only** if a contemporaneous **StateAssertion** exists for an **enactable** State.
5. **No silent Cross‑context reuse.** Cross‑Context reuse requires a **Bridge** with CL and loss notes; local `⊥/≤/⊗` always prevail.

