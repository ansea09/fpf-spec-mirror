---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:1"
section_title: "Purpose"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__003_purpose.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:1 — Purpose"
line_start: 45607
line_end: 45617
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
  - "base KindSignature"
  - "candidate-feature constraint"
  - "correspondence declaration"
  - "kind-use adaptation declaration"
  - "three-valued judgment"
  - "vocabulary binding"
---

### C.3.4:1 - Purpose

Teams often need a local projection of a widely used kind:

- **Constraint:** “For our procedure, take `Vehicle` with ABS only.”
- **Vocabulary:** “Here, `AuthHeader` is called `X-Auth`.”

Cloning a kind for every local use fragments catalogs and multiplies bridges. A declaration of a local use keeps the base-kind identity, makes constraints and bindings explicit, and gives a guard one named, versioned episteme to designate. The declaration is not a new U-kind, record ontology, or classification occurrence.

The practical gains are fewer near-duplicates, cleaner cross-context reuse, deterministic guards, and auditable narrowing instead of an unexplained “this is the version we mean.”

