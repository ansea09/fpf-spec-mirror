---
chunk_kind: "child"
pattern_id: "A.19.USCM"
pattern_title: "Scoring Mechanism"
section_id: "A.19.USCM:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.USCM/A.19.USCM__003_problem-frame.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.USCM — Scoring Mechanism"
  - "A.19.USCM:1 — Problem frame"
line_start: 39698
line_end: 39713
dependencies:
keywords:
  - "CG-Spec.MinimalEvidence"
  - "CSLC-lawful transforms"
  - "ScaleComplianceProfile (SCP)"
  - "ScoringMethodDescription"
  - "score profile"
  - "scoring"
  - "tri-state admissibility (pass\\"
---

### A.19.USCM:1 - Problem frame

FPF’s Characterization (CHR) suite treats scoring as a **mechanism boundary** (authoritative membership: `A.19.CHR:4.2`). Suite membership is a **set** (order has no semantics); any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under the suite obligations (`A.19.CHR:4.3`).

Within the canonical suite-closed protocol, USCM appears as the `score` stage (after `normalize` and `indicatorize`, before comparison and selection). USCM’s surface is admissibility-first: it produces **score measures** from admitted profiles while remaining constrained by the admissibility gate (`CG-Spec.SCP`) and by scale-lawfulness (CSLC).

USCM exists to keep a distinction between:

* **normalization** (UNM),
* **indicatorization** (UINDM),
* **scoring** (USCM),
* **aggregation/folding** (ULSAM), and
* **comparison/ordering/selection** (CPM + SelectorMechanism),

so that each commitment has a single place to live, can be audited, and can evolve without smuggling extra semantics into adjacent steps.

