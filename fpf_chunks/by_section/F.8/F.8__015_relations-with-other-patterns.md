---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:13"
section_title: "Relations (with other patterns)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__015_relations-with-other-patterns.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:13 — Relations (with other patterns)"
line_start: 72453
line_end: 72463
dependencies:
  - "A.11"
  - "A.7"
  - "A.8"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:13 - Relations (with other patterns)

* **Builds on:** E.10.D1 (D.CTX) **Context ≡ U.BoundedContext**; F.1 Contexts; F.2 Harvest; F.3 SenseCells.
* **Constrains:**

  * **F.4 Role Description:** **one SenseCell per Role Description**; no row anchoring.
  * **F.5 Naming:** Aliases are style‑only; no semantics movement.
  * **F.7 Concept‑Set:** rows must declare **Scope** & **Row CL(min)** and carry **loss notes**.
  * **F.9 Bridges:** any row proposal presupposes Bridges at or above τ(scope).
* **Used by.** All patterns (Part C) whenever new labels are contemplated.

