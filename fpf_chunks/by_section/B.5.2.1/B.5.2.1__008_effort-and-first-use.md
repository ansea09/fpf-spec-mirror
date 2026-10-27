---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:7"
section_title: "Effort and first use"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__008_effort-and-first-use.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:7 — Effort and first use"
line_start: 49767
line_end: 49774
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

### B.5.2.1:7 - Effort and first use

**For engineers/managers (user cognitive load).**

* *Added steps:* selecting descriptor **Characteristics** and granularity; reading the returned front. Start with front membership; consult dominated entries when their exclusion or retained archive role matters.
* *Mitigations:* a compact comparison note or table can suffice. Keep the required coordinate meanings and provenance available, and reuse applicable Context grids and metrics.
* *Reader quickstart (engineer‑manager):* (1) Pick 2–3 **Q** characteristics aligned to the anomaly + a simple **CharacteristicSpace** (2–4 dimensions). (2) Accept defaults for `NoveltyMetric`, grid granularity, and `K=1`. (3) Run **NQD‑Generate** to a fixed budget; inspect the front under its declared Q coordinates. (4) Apply Step 3 filters; log decisions in the DRR.

