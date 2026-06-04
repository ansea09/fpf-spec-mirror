---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__003_problem.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:2 — Problem"
line_start: 29026
line_end: 29036
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "C.2"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:2 - Problem

Naive aggregation of knowledge holons causes recurring failures:

1. **Trust inflation by averaging.** Averaging confidences of conflicting claims creates a falsely “reliable” whole; violates **WLNK** and **B.3** conservatism.
2. **Provenance erasure.** Merges that drop sources, methods, or links break **A.10 Evidence Graph Referring** and make results unauditable.
3. **Semantic drift.** Folding across mismatched concepts without explicit **mappings** (and their **CL**) yields incoherent composites that look formal but mean nothing.
4. **Order blindness.** Arguments with essential **dependency order** (premise ⇒ lemma ⇒ conclusion) are treated as sets; non‑commutativity is lost and results become non‑reproducible.
5. **Context chimeras.** Combining items across **bounded contexts** (different vocabularies/units/policies) without a **Context Reframe** (B.2) silently corrupts claims and inflates **R**.
6. **Category errors.** Importing **Γ\_sys** rules (e.g., “sum truth,” “avg formality”) into knowledge composition produces physically sounding but epistemically nonsensical models.

