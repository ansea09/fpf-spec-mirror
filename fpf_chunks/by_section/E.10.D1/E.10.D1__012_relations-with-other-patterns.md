---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:11"
section_title: "Relations (with other patterns)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__012_relations-with-other-patterns.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:11 — Relations (with other patterns)"
line_start: 53533
line_end: 53544
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

### E.10.D1:11 - Relations (with other patterns)

**Builds on:** C‑6, C‑7, G‑1, G‑2.
**Constrains:**

* **E.10.U1** — lists only `U.BoundedContext`s; no “domain contexts”; context records never encode pattern semantics.
* **E.10.U2** — Seeds and Occurrences are **always** Context‑anchored; references use forms from Sec. 5.
* **E.10.U7** — Columns are **SenseCell**s; row notes never call them “anchors”.
* **E.10.U9** — All cross‑context relations live here; no implicit equivalences elsewhere.
* **`RoleAssigning` patterns (E.10.U4, …)** — Context points to **SenseCell** or **Concept‑Set columns**, never to “anchors”.


