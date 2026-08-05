---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__005_problem.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:2 — Problem"
line_start: 4464
line_end: 4474
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:2 - Problem

Without a direct role-state relation ontology, six recurring failures appear.

1. **Assignment becomes readiness.** Holding the role is treated as satisfying every state precondition of every method that names it.
2. **State label hides the predicate.** `Ready`, `Approved`, or `Active` travels between role taxonomies even though its truth conditions differ.
3. **Evidence becomes the state.** An evidence or display episteme is treated as the world-side role-state relation.
4. **Missing evidence becomes falsehood.** An unrecovered or stale evidence path is taken as proof that the world-side predicate does not obtain.
5. **Capability becomes admission.** A system's ability to perform an operation is overread as current admission of this concrete method or work claim.
6. **State notation becomes method order.** A transition arrow is treated as the work that changes the state, even though the method, work, transformation, and state-change claim have different ontics.

