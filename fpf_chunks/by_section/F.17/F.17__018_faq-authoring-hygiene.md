---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet (UTS)"
section_id: "F.17:17"
section_title: "FAQ (authoring hygiene)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__018_faq-authoring-hygiene.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.17 — Unified Term Sheet (UTS)"
  - "F.17:17 — FAQ (authoring hygiene)"
line_start: 74155
line_end: 74168
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

### F.17:17 - FAQ (authoring hygiene)

**Q1. Is the UTS a registry?**
*A.* No. It is a **didactic publication**. No CRUD semantics, no workflows.

**Q2. Can we collapse two Contexts if their terms look identical?**
*A.* Only via **F.9 Bridge** with **CL=3**. Identity must be argued, not assumed by spelling.

**Q3. Where do state‑graphs (A.2.5) show up?**
*A.* In `Notes` or as a dedicated row if the stateful nature of a Role family is central to the thread.

**Q4. How do we show deontic approvals?**
*A.* The concept rows (`U.SpeechAct`, `U.Commitment`, `U.PromiseContentClause`, `U.PromiseFulfillmentEvaluation`) make the communicative/epistemic pieces visible; enactment appears in examples, not as sheet mechanics.

