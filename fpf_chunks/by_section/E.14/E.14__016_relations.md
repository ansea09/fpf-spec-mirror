---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__016_relations.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:13 — Relations"
line_start: 77719
line_end: 77740
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:13 - Relations

**Builds on:**

* **E.8 Authoring Conventions & Style Guide** — section order, style principles, and mandatory safety subsections used here.
* **E.7 Archetypal Grounding** — the Tell‑Show‑Show rule applied in this pattern’s own Grounding section.
* **C.2.3 Unified Formality Characteristic (F)** — declares the **F** scale and **ΔF** moves for progressive rigor; Working-Model publications **SHALL** declare **F** and remain notation-agnostic.

**Coordinates with.**

* **CT2R-LOG — Working-Model Relations and Grounding** — supplies the optional elected profile that adds `validationMode` and, for covered structural assertions, `tv:groundedBy`; direct relations outside the profile need neither field.
* **Compose-CAL (Constructional Mereology)** — supplies the `sum`, `set`, and `slice` trace content when construction assurance is selected; the trace does not define the Working-Model relation or its identity.
* **E.10 Lexical Discipline & Stratification** — ensures naming discipline and register hygiene when the human layer is published.

**Constrains:**

* All architectural patterns that publish relations **SHALL** present the readable Working-Model claim first. A direct relation outside an elected assurance profile needs no E.14 assurance field. When `B.3.5` or another named current requirement applies, attach only its required support below the claim while preserving relation-family separation and notational independence. (Template conformance as per E.8.)

**Informs.**

* Part F unification practices (context of meaning, bridges, fit levels) by reinforcing the preference for human‑readable labels with explicit alignment notes rather than silent formal substitutions.

