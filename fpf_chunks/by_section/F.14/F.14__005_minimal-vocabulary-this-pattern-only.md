---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti‑Explosion Control (Roles & Statuses)"
section_id: "F.14:4"
section_title: "Minimal vocabulary (this pattern only)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__005_minimal-vocabulary-this-pattern-only.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "F.14 — Anti‑Explosion Control (Roles & Statuses)"
  - "F.14:4 — Minimal vocabulary (this pattern only)"
line_start: 73773
line_end: 73780
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

### F.14:4 - Minimal vocabulary (this pattern only)

* **Role Description** (F.4): a **Role** (behavioural mask) or **Status** (epistemic/deontic standing) tied to a **SenseCell**.
* **Concept‑Set row** (F.7): a Cross‑context **intent** (“what we count as one thing”) aligned by SenseCells.
* **Bundle** (this pattern): a **named composition** of Role Descriptions that are meant to be used together by design (e.g., {Requester, Approver} for change control). A Bundle is a **concept**, not a package.
* **SoD Constraint** (this pattern): a **conceptual rule** stating that two Roles **must not** be played by the same Holder in the **same window**.
* **Window** (F.10): an **claim scope** (time stance, holon level, run segment) that delimits when a Role or Status holds.

