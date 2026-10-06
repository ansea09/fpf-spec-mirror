---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:7"
section_title: "Cognitive Load & Kernel Growth Budget"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__008_cognitive-load-kernel-growth-budget.md"
commit_sha: "2c16067fe8c7f34ea3313d66d36738870f5c2087"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:7 — Cognitive Load & Kernel Growth Budget"
line_start: 47592
line_end: 47603
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
---

### B.5.2.1:7 - Cognitive Load & Kernel Growth Budget

**For engineers/managers (user cognitive load).**

* *Added steps:* selecting descriptor **Characteristics** and granularity; reading the returned front. Start with front membership; consult dominated entries when their exclusion or retained archive role matters.
* *Mitigations:* a compact comparison note or table can suffice. Keep the required coordinate meanings and provenance available, and reuse applicable Context grids and metrics.
* *Reader quickstart (engineer‑manager):* (1) Pick 2–3 **Q** characteristics aligned to the anomaly + a simple **CharacteristicSpace** (2–4 dimensions). (2) Accept defaults for `NoveltyMetric`, grid granularity, and `K=1`. (3) Run **NQD‑Generate** to a fixed budget; inspect the front under its declared Q coordinates. (4) Apply Step 3 filters; log decisions in the DRR.

**For the framework (kernel growth).**

* *Zero* new primitives; only a CHR import and a **Method**. Passes **A.11** minimal‑sufficiency.

