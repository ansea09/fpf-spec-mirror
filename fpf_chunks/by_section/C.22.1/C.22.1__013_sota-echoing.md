---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__013_sota-echoing.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:12 — SoTA-Echoing"
line_start: 49971
line_end: 49991
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
  - "E.19"
  - "E.22"
  - "E.23"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "adaptation signature"
  - "budget-to-threshold"
  - "corridor entry"
  - "downside field"
  - "prior exposure"
  - "retention"
  - "stepping stone"
  - "task-family specialization"
  - "time-to-threshold"
  - "transfer"
---

### C.22.1:12 - SoTA-Echoing

**Claim 1.** Current frontier adaptation work judges usable specialization by threshold-crossing under bounded resources, not by terminal score alone.

**Practice source, local alignment, and adoption decision.** Current QD and agentic-adaptation sources such as `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026), FactorMiner `arXiv:2602.14670v1` (2026-02-16), and SkillOpt `arXiv:2605.23904v2` (2026-05-25) repeatedly separate threshold target, budget burn, transfer evidence, reuse evidence, and changed object/version from one final benchmark score. This pattern **adopts** that practical field set, **adapts** it through one `TaskFamilyRef` or `TaskSignature`-bound adaptation signature, and **rejects** generic `got better` narratives that leave threshold and budget semantics implicit.

**Claim 2.** Current open-ended exploration work treats corridor entry and stepping stones as evidence-bearing novelty signals rather than decorative commentary.

**Practice source, local alignment, and adoption decision.** Current `QD`/`OEE` source-use relation/currentness plus current FPF `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` neighbours distinguish real corridor entry from one exotic sample by asking for explicit baseline, stable descriptor shift, reproducible solution class, or an explicit stepping-stone trace. This pattern **adopts** explicit corridor baseline/evidence discipline, **adapts** it as declared adaptation-signature fields, and **rejects** novelty talk that names no baseline, evidence source, or evidence locus.

**Claim 3.** Current selector and parity practice needs one stable shared field set for specialization claims.

**Practice source, local alignment, and adoption decision.** Current FPF selector and parity neighbours keep compared candidates reviewable only when candidates reuse the same published field set for threshold, prior exposure, transfer, retention, downside, and corridor-entry field. This pattern **adopts** that reuse discipline, **adapts** it by publishing one stable adaptation-signature field set here, and **rejects** silent downstream field redefinition in `G.5` or `G.9`.

**Evidence-source note.** Peer-reviewed or archived frontier anchors carry the most direct evidence for threshold, budget, and parity claims. Fast-moving frontier lines remain explicit evidence for corridor-entry and open-ended exploration pressure only when the row names their local contribution; they are not a flattened single evidence status.

| Source-bound anchor family | Source-use relation/currentness | What it disciplines in this pattern |
| --- | --- | --- |
| `QD` / `OEE` corridor-entry work | Current QD overview plus current FPF OEE/NQD neighbours. | Corridor baseline, descriptor shift, stepping-stone evidence, and whether novelty is reproducible rather than one exotic sample. |
| Agentic adaptation benchmarks | Current narrow source lines such as FactorMiner and SkillOpt when the task family is comparable. | Threshold target, time-to-threshold, budget-to-threshold, prior exposure, and post-threshold efficiency under a declared task-family anchor. |
| Transfer / retention evaluation | Source-use relation/currentness supplied by the applying benchmark or neighbour pattern. | Transfer target, retention window, downside, and reuse evidence so specialization speed is not confused with one isolated threshold crossing. |
