---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:11"
section_title: "Relations (with other patterns)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__012_relations-with-other-patterns.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:11 — Relations (with other patterns)"
line_start: 76234
line_end: 76244
dependencies:
  - "A.2.1"
  - "A.4"
  - "A.7"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
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

* **F.1** — lists only `U.BoundedContext`s; no “domain contexts”; context records never encode pattern semantics.
* **F.2** — Seeds and Occurrences are **always** Context‑anchored; references use forms from Sec. 5.
* **F.7** — Columns are **SenseCell**s; row notes never call them “anchors”.
* **F.9** — All cross‑context semantic relations live here; no implicit equivalences elsewhere.
* **Role-description and role-assignment patterns (F.4, A.2.1, and F.6)** — Context points to **SenseCell** or **Concept‑Set columns**, never to “anchors”.

