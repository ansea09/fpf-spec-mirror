---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
section_id: "A.6.P:0"
section_title: "TERM/LEX token guards (local-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__002_term-lex-token-guards-local-first.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.P — U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
  - "A.6.P:0 — TERM/LEX token guards (local-first)"
line_start: 12049
line_end: 12069
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.2.6"
  - "A.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.8"
  - "A.6.9"
  - "A.6.A"
  - "A.6.B"
  - "A.6.H"
  - "A.6.Q"
  - "A.6.S"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "C.26"
  - "C.3.3"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "QualifiedRelationRecord"
  - "RelationKind"
  - "coupling"
  - "endpoint referential compression"
  - "export"
  - "language-state seam"
  - "lexical guardrails"
  - "measurement"
  - "probe"
  - "relation precision restoration"
  - "under-specified relational language"
---

### A.6.P:0 — TERM/LEX token guards (local-first)

This pattern reserves the following tokens in Tech/normative prose:

* **RPR** — *Relational Precision Restoration* (the suite recipe; not a new `U.Type`).
* **RelationKind** — a Context-local vocabulary token (signature-level) that fixes polarity and SlotSpecs for participant/qualifier positions. It is a *registry entry/token*, not a relation instance.
* **QualifiedRelationRecord** — the slot-explicit relation instance record kind (Context-local episteme/record kind); instances carry a `relationKind` token reference plus explicit participant/qualifier slots.

**Mint-or-reuse note (recipe-level).** This pattern mints the suite label **RPR**, the role name **RelationKind**, and the generic shape name **QualifiedRelationRecord** as local-first terms for this family. It reuses existing FPF terms (`U.Signature`, SlotKind/ValueKind/RefKind, Bridges/CL, `U.Scope`, `Γ_time`, `U.View`/`U.Viewpoint`, evidence pins/carriers) without changing their meanings.

**Definitions (recipe-level; non-deontic).**

* **RelationKind token** — a declared vocabulary element (signature-level) whose public definition fixes polarity and SlotSpecs for participant/qualifier positions, and that is referenced by L/A/D/E-classified claims that govern admissibility, duties/commitments, and evidence/work.
* **QualifiedRelationRecord** — a Context-local episteme/record kind whose `relationKind` field points (by id/ref) to a RelationKind token and whose instance records make all relation-specification-required participant/qualifier slots explicit.

Rename-guards (common collisions):

* **agreement-like boundary wording** — Plain shorthand for a published boundary-interface description; a conforming text MUST NOT treat such wording as itself establishing a promise/obligation. Promises, duties, and gates are classified under `A.6.B`.
* **bind/binding** — reserved for **name binding** (Identifier → SlotKind/slot-instance) and MUST NOT be used as a synonym for relation instance edits.
* **same/synced/linked/connected/anchored/grounded** — treated as umbrella tokens; allowed as Plain gloss only when immediately mapped to an explicit RelationKind token (Tech) via rewrite rules.

