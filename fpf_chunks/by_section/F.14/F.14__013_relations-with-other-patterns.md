---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti‑Explosion Control (Roles & Statuses)"
section_id: "F.14:12"
section_title: "Relations (with other patterns)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__013_relations-with-other-patterns.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.14 — Anti‑Explosion Control (Roles & Statuses)"
  - "F.14:12 — Relations (with other patterns)"
line_start: 73176
line_end: 73187
dependencies:
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.12"
  - "F.13"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:12 - Relations (with other patterns)

* **Builds on:** F.1 (Contexts), F.2 (Harvesting), F.3 (Local Clustering), F.4 (Role Description), F.5 (Naming).
* **Constrains:**

  * **F.7 (Concept‑Set Table):** prefer **row reuse**; new rows require F.8 justification.
  * **F.8 (Mint‑or‑Reuse):** apply **four levers** (reuse, bundle, SoD, window) before minting.
  * **F.10 (Status Windows & Mapping):** encode temporal/scale variation as **windows**, not new Status types.
  * **F.12 (Service Acceptance Binding):** bind acceptance to the **Compliance** Status family; avoid ad‑hoc status labels.
  * **F.13 (Lexical Continuity):** prior names become **aliases**; do not carry forward inflated vocabularies as new types.
* **Used by.** FPF patterns to keep Role and Status vocabularies tight.

