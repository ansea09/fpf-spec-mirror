---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
section_id: "A.6.P:0"
section_title: "TERM and LEX token guards (local-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__002_term-and-lex-token-guards-local-first.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.6.P — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
  - "A.6.P:0 — TERM and LEX token guards (local-first)"
line_start: 13928
line_end: 13948
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
  - "A.6.S"
  - "A.7"
  - "C.16.Q"
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
  - "selected support reading"
  - "support/support-headed wording"
  - "under-specified relational language"
---

### A.6.P:0 — TERM and LEX token guards (local-first)

This pattern reserves the following tokens in Tech and normative prose:

* **RPR** — *Relational Precision Restoration* (the governing repair discipline; not a durable U-kind).
* **RelationKind** — a Context-local vocabulary token (signature-level) that fixes polarity and SlotSpecs for participant and qualifier positions. It is a *registry entry token*, not a relation instance.
* **QualifiedRelationRecord** — the slot-explicit relation instance record kind (Context-local episteme or record kind); instances carry a `relationKind` token reference plus explicit participant and qualifier slots.

**Mint-or-reuse note (pattern-level).** This pattern mints the label **RPR**, the role name **RelationKind**, and the generic shape name **QualifiedRelationRecord** as local-first terms for relation precision restoration. It reuses existing FPF terms (`U.Signature`, SlotKind, ValueKind, RefKind, Bridges, CL, `U.Scope`, `Γ_time`, `U.View`, `U.Viewpoint`, evidence pins, and carriers) without changing their meanings.

**Definitions (pattern-level; non-deontic).**

* **RelationKind token** — a declared vocabulary element (signature-level) whose public definition fixes polarity and SlotSpecs for participant and qualifier positions, and that is referenced by L, A, D, and E-classified claims that govern admissibility, duties, commitments, evidence, and work.
* **QualifiedRelationRecord** — a Context-local episteme or record kind whose `relationKind` field points (by ID or reference) to a RelationKind token and whose instance records make all relation-specification-required participant and qualifier slots explicit.

Rename-guards (common collisions):

* **agreement-like boundary wording** — Plain shorthand for a published boundary-interface description; a conforming text MUST NOT treat such wording as itself establishing a promise or obligation. Promises, duties, and gates are classified under `A.6.B`.
* **bind and binding** — reserved for **name binding** (Identifier to SlotKind or slot instance) and MUST NOT be used as a synonym for relation instance edits.
* **same, synced, linked, connected, anchored, grounded, supported, and supporting** — treated as umbrella tokens; allowed as Plain gloss only when immediately mapped to an explicit RelationKind token (Tech) or to an claim kind governed by an FPF pattern named by value or admissible-use boundary via rewrite rules.

