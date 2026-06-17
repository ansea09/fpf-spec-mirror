---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__008_conformance-checklist-normative.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:7 — Conformance Checklist (normative)"
line_start: 61814
line_end: 61823
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

### E.10.D1:7 - Conformance Checklist (normative)

* **CC‑LCTX‑1.** Grep‑style check: every “Context” in formal sections expands to **`U.BoundedContext`**.
* **CC‑LCTX‑2.** The token **anchor** is absent from normative text; where needed, occurrences are replaced by **SenseCell** or **ConceptSet reference**.
* **CC‑LCTX‑3.** Pattern headers use **Problem Frame**; none use “Context” for narrative.
* **CC‑LCTX‑4.** References to meaning are in one of the **reference forms** (Sec. 5).
* **CC‑LCTX‑5.** No file defines “domain context”; Domain appears only as an **informative family**.
* **CC‑LCTX‑6.** No is‑a edges between contexts; any cross‑context relation is located in **E.10.U9**.
* **CC‑LCTX‑7.** Language/edition handling matches **D‑CTX‑7** (separate Contexts when semantics can diverge).

