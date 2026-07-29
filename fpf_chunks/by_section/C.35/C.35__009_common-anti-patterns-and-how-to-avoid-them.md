---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 66896
line_end: 66906
dependencies:
  - "A.22"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "E.18"
  - "G.5"
keywords:
  - "DSM"
  - "LLM"
  - "NAS"
  - "candidate admission"
  - "described structure"
  - "generated carrier"
  - "produced carrier"
  - "source return"
  - "structural discovery"
  - "structural synthesis"
---

### C.35:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| LLM output as architecture | A plausible diagram or prose proposal may not carry selected structures, constraints, bearer feasibility, or carrier-admission return. | Record the output as produced carrier; recover described structure; set candidate-admission condition; route decision and ADR claims to PAD and ADR governing patterns. |
| Pareto point as admission | A Pareto point shows trade-off position under chosen criteria, not architecture adequacy across selected structures and bearers. | Name search space, criteria refs, constraints, preserved and lost structure, bearer boundary, and eval return; then route candidate use to `C.32`. |
| One output as reusable-generator governance | A single generated artifact does not describe the method, mechanism suite, dataset, prompt policy, or refresh process that produced a reusable generator. | Keep the one-case output in C.35 and open `E.20`, `G.1`, `G.10`, `G.11`, or another selected governing pattern when reusable generator governance is the claim. |
| Cluster as module architecture | A DSM or MDM cluster can preserve co-change or dependency pressure while losing functional bearer semantics and interface substitutability. | Route modularity and reuse claims to `C.31`; route candidate palette use to `C.32`; keep C.35 for admission of the produced cluster carrier. |
| Transformation output as feasibility proof | A graph grammar or model transformation can preserve formal structure while dropping manufacturing, deployment, organizational, or method bearers. | Record transformation trace, selected source structures, target structures, preserved structure, lost structure, and bearer boundary; use C.34 for preservation and the direct governing pattern for feasibility. |
| Bypassing eval and measurement governance | A search score, benchmark, ablation, or validation trace can look like proof of architecture quality. | Route readings to `C.16`, Q-bundle use to `C.25`, eval programs and eval results to `C.32.ACE`, and decisions to `C.32.PAD`. |

