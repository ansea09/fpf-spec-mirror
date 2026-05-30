---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:11"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__012_relations.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:11 — Relations"
line_start: 30096
line_end: 30115
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:11 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: an authored temporal claim that turns a temporal slice, phase name, aggregate membership, or temporal ordering into a rate-change adequacy claim.
- This pattern keeps: contextual and temporal aggregation, declared temporal slices, and phase composition.
- Non-admissible use: temporal slices, phase names, aggregate membership, or temporal ordering do not infer acceleration or create a dynamics law.
- Exit: if only slice composition is live, stay in B.1.4; if rate-change adequacy changes admissible use, use C.27 for that claim and cite the governing FPF pattern for any law, work, causal, or benchmark question.

* **Builds on:** B.1 (Universal Γ), B.1.1 (Dependency Graph & Proofs), A.12 (Transformer), A.14 (Mereology Extension), A.15 (Strict Distinction).
* **Specialises into:** **B.1.5 Γ\_method** (adds duration, capability typing, join soundness rules).
* **Works alongside:** **B.1.6 Γ\_work** (resource accounting per step/phase).
* **Triggers:** **B.2 Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes** when re‑ordering or re‑phasing produces genuinely new properties.
* **Feeds:** **B.4 Canonical Evolution Loop** (time‑aware cycles that carry explicit costs and order).

> **One‑page takeaway.**
> If **order changes meaning**, use **Γ\_ctx** with an explicit **OrderSpec** and independence/joins.
> If you are **composing the same carrier across time**, use **Γ\_time** with a **TimeWindow**, coverage, and identity.
> Keep structure, mapping, and cost in their places, and the invariants will do the rest.

