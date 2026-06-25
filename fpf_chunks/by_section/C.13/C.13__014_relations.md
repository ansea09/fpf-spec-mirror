---
chunk_kind: "child"
pattern_id: "C.13"
pattern_title: "Constructional Mereology (Compose‑CAL)"
section_id: "C.13:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.13/C.13__014_relations.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "C.13 — Constructional Mereology (Compose‑CAL)"
  - "C.13:10 — Relations"
line_start: 42755
line_end: 42779
dependencies:
  - "A.14"
  - "B.3.5"
keywords:
  - "composition"
  - "extensional identity"
  - "mereology"
  - "part-whole"
  - "set"
  - "slice"
  - "sum"
---

### C.13:10 - Relations

**Builds on**

* **A.14 Advanced Mereology.** Uses its structural catalogue (Component/Portion/Aspect vs Member) as the *target* of constructive narratives; never collapses Member into Part.
* **E.5 Guard‑Rails (Notational Independence).** Meanings are given in prose; diagrams are illustrative only.
* **E.5 Guard‑Rails (Unidirectional Dependency).** Compose‑CAL depends **downward** only; it never imports alias layers or higher planes.
* **E.8 Authoring Conventions.** Conforms to the canonical pattern template (Grounding section for architectural patterns; CC placement).

**Coordinates with**
* **B.3.5 CT2R-LOG.** `tv:groundedBy` refers (conceptually) to Compose-CAL traces when `validationMode = axiomatic`; **Working-Model** relations remain the public relation layer.
* **B.1 flavours.** Keeps order (`Γ_method`) and time (`Γ_time`) outside structure; may co‑appear in narratives when relevant but never as constructors.
* **Kind-CAL / Lang‑CHR.** Provide the Mapping shoulder of assurance (labels, type alignment) that complements constructive narratives in this pattern.
* **KD‑CAL.** Provides the Logical shoulder when authors justify relations inferentially instead of constructively.
* **C.16 (Measurement substrate).** Supplies quantitative hooks when a constructive narrative benefits from explicit counts/ratios (e.g., cardinalities, coverage), while keeping metrics distinct from mereology.

**Constrains**
* Any pattern that **creates** or **reasons about** structural wholes SHOULD narrate them using only `sum | set | slice`.
* Structural publication MUST NOT encode order/time; such claims belong to their dedicated flavours.
* Introducing new structural constructors requires a separate parsimony argument and is discouraged unless the triad cannot narrate the case without ambiguity.

**Provides**
* A minimal generative calculus (`Γ_m.sum | Γ_m.set | Γ_m.slice`) and the corresponding reading discipline for constructive narratives.
* A stable CT2R-LOG relation for `tv:groundedBy` links under `validationMode = axiomatic`.

