---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:1"
section_title: "Purpose (manager’s view)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__002_purpose-manager-s-view.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:1 — Purpose (manager’s view)"
line_start: 44843
line_end: 44853
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

### C.3.4:1 - Purpose (manager’s view)

Teams often need a **local projection** of a widely used kind:

* **Constraint:** “For our procedure, take `Vehicle` **with ABS** only.”
* **Vocabulary:** “Here, `AuthHeader` is called `X‑Auth`.”

If each team clones a fresh kind, catalogs fragment and bridges multiply. `RoleMask` is the disciplined alternative: keep the base kind identity, apply declared constraints and bindings, and publish one named, versioned declaration episteme that a guard can designate. The episteme is not a new U-kind, record ontology, or classification occurrence. When the constraint becomes a stable conceptual distinction, identify a separate local kind and establish its `U.SubkindOf` relation independently.

**Benefits:** fewer near‑duplicates, cleaner Cross‑context reuse, deterministic guards, and auditable narrowing instead of hand‑wavy “this is the version we mean.”

