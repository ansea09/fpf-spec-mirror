---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:10"
section_title: "Reasoning Primitives (conceptual judgements; notation‑agnostic)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__011_reasoning-primitives-conceptual-judgements-notation-agnostic.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:10 — Reasoning Primitives (conceptual judgements; notation‑agnostic)"
line_start: 75261
line_end: 75282
dependencies:
  - "A.4"
  - "A.7"
  - "E.10.U1"
  - "E.10.U2"
  - "E.10.U4"
  - "E.10.U7"
  - "E.10.U9"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
keywords:
  - "U.BoundedContext"
  - "anchor"
  - "context"
  - "domain"
  - "frame"
---

### E.10.D1:10 - Reasoning Primitives (conceptual judgements; notation‑agnostic)

> Pure **thinking moves**; no APIs, no storage, no governance.

* **(J1) Context expansion.** `⊢ Context ≡ U.BoundedContext`
  *Reading:* wherever “Context” appears in formal prose, it denotes `U.BoundedContext`.

* **(J2) Anchor ban.** `uses("anchor") ⊢ violation(D‑CTX‑2)`
  *Reading:* usage of “anchor” flags a discipline violation.

* **(J3) Sense reference.** `ref(ContextId, LocalLabel) ⊢ SenseCell(ContextId, Local‑Sense)`
  *Reading:* a well‑formed reference identifies a SenseCell.

* **(J4) Narrative frame.** `header("Context") ⊢ replaceWith("Problem Frame")`
  *Reading:* headings “Context” in patterns must become “Problem Frame”.

* **(J5) Domain family.** `label ∈ {workflow,…} ⊢ DomainFamily(label)`
  *Reading:* Domain labels are families, not contexts.

* **(J6) Time tag.** `stance ∈ {design, run} ⊢ TimeScopeTag(stance)`
  *Reading:* time is a tag, not a new context.

