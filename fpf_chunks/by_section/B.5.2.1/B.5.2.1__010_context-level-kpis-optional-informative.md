---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:9"
section_title: "Context‑Level KPIs (optional, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__010_context-level-kpis-optional-informative.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:9 — Context‑Level KPIs (optional, informative)"
line_start: 50258
line_end: 50267
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

### B.5.2.1:9 - Context‑Level KPIs (optional, informative)

Practitioners may monitor these indicators to improve practice; they do not serve as admission conditions:

1. **Profile-specific assurance progression (optional).** When a receiving domain uses an assurance-level profile, report the fraction of cycles whose candidate meets a named level under that profile within the policy window. Name the claim, use and satisfying evidence; omit this KPI when no such profile is used.
2. **Frontier‑Hit Rate (FHR).** % of cycles where the chosen candidate lies on the **Pareto front** over the declared `DominanceSet` at selection time; track novelty/diversity contribution separately as archive, tie-break, or policy-promoted evidence.
3. Coverage Gain (ΔI, report). Change in the *illumination summary* (coverage map/%filled cells) per cycle (how much of the descriptor space is now “lit”).
4. **Exploration Cost Ratio (ECR).** Under one resource metric, divide generation cost by positive downstream analysis or evidence-acquisition cost savings relative to a stated comparison baseline. State whether the savings are measured or estimated and identify the comparison or estimation Method. If positive savings are not established, report the costs and the supported saving result or unresolved saving claim separately.
5. **Refutation Learning Yield (RLY).** Among *refuted* candidates, report the percentage that added new coverage or contributed a specified increase in Surprise. For the Surprise branch, identify the constituted result and its baseline or reference set, and use a declared comparison rule on a compatible basis to determine whether the candidate counts.

