---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:6"
section_title: "Core Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__007_core-invariants-normative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:6 — Core Invariants (normative)"
line_start: 60496
line_end: 60506
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

### E.10.D1:6 - Core Invariants (normative)

1. **LCTX‑INV‑1 (Uni‑meaning).** The word **Context** in formal text equals **`U.BoundedContext`**.
2. **LCTX‑INV‑2 (No anchor).** The token **anchor** does **not** appear in normative prose; use **SenseCell** or **ConceptSet reference**.
3. **LCTX‑INV‑3 (No domain contexts).** “Domain context” is invalid; use **Domain family** + list of `U.BoundedContext`s.
4. **LCTX‑INV‑4 (Frames, not contexts).** Pattern headers use **Problem Frame** for narrative.
5. **LCTX‑INV‑5 (No hierarchy).** Contexts are flat; relationships are declared **only** via E.10.U9 Bridges.
6. **LCTX‑INV‑6 (Plane hygiene).** Contexts describe **context of meaning** for sources; they are not roles, statuses, executions, or types (C‑6).
7. **LCTX‑INV‑7 (Time tags).** DesignRunTag is a **tag** on carriers, source publications, or source epistemes as applicable; it does not multiply contexts.
8. **LCTX‑INV‑8 (Language/edition).** Multilingual or multi‑edition handling follows D‑CTX‑7.

