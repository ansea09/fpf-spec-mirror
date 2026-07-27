---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__003_problem.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:2 — Problem"
line_start: 22627
line_end: 22638
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "evidence for permission result versus commitment or issuing act"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:2 - Problem

Without a uniform evidence-provenance path, models drift into five failure modes:

1. **Weightless claims.** Metrics or arguments appear in the model with no link to their **symbol carriers** (files, datasets, lab notebooks, figures).
2. **Collapsed scopes.** Design-time method specs are silently mixed with run-time traces; results cannot be reproduced because "what was planned" and "what work occurred" are conflated.
3. **Self-justifying loops.** A claim is used as evidence for itself, or the same work occurrence both produces the target claim and supplies its evidence without a separated evidence-producing or interpreting work occurrence, provenance relation, source-maintenance role assignment, or relying context.
4. **Source loss during aggregation.** As `Γ` combines parts, some sources fall out; subsequent audit cannot reconstruct why a compound claim was accepted.
5. **Temporal ambiguity.** Time-series are aggregated without interval coverage or dating source; gaps and overlaps invalidate comparisons and trend claims.

The business effect is predictable: confidence badges cannot be defended, cross‑scale consistency (A.9) is broken, and iteration slows because every review re‑litigates “where did this come from?”.

