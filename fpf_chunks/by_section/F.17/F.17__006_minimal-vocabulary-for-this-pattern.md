---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet (UTS)"
section_id: "F.17:5"
section_title: "Minimal Vocabulary (for this pattern)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__006_minimal-vocabulary-for-this-pattern.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "F.17 — Unified Term Sheet (UTS)"
  - "F.17:5 — Minimal Vocabulary (for this pattern)"
line_start: 74246
line_end: 74260
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.15"
  - "A.7"
  - "A.8"
  - "E.10"
  - "E.10.D1"
  - "E.10.P"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:5 - Minimal Vocabulary (for this pattern)

* **UTS (Unified Term Sheet).** The published, human‑readable table per thread.
* **Context.** Alias in Tech register for **`U.BoundedContext`** (E.10.D1). Normative unit of meaning; every SenseCell is scoped to a Context _(name + edition)._
* **Bounded‑Context Column (BCC).** A didactic column used **only in Layout A**; one column per **Context (`U.BoundedContext`)** from the F.1 cut; **not a model element**; the **header includes the Context name + edition**.
* **Discipline Column (DC).** A _discipline vantage_ used **only in Layout B** (e.g., _Operational Management_, _IT/Software_, _Physics_). A DC is **not** a **Bounded‑Context Column** and does not carry editions.
* **Concept‑Set (CSR).** One unified concept with pointers to its SenseCells.
* **SenseCell.** _(Context × Local‑Sense)_ address—how a Context “says that thing”.
* **Bridge / CL.** Explicit cross‑context mapping (F.9) with Congruence Level and Loss note.
* **Plain Twin (LEX).** The LEX record pairing the **Unified Tech name** with its **Unified Plain name** for a U.Type; governed by **PTG** and referenced by `Twin‑Map Id (LEX)` (E.10 LEX‑BUNDLE).
* **Block Plan.** Didactic grouping of rows to keep the sheet memorizable.
* **Unified Tech name / Unified Plain name.** Dual‑register names chosen per F.5; the **Tech name is the neutral, unified term** for the U.Type, not a borrowed Context name.

> **Discipline.** “Context” always means **`U.BoundedContext`** (E.10.D1). No global words.

