---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 67504
line_end: 67514
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.6.M"
  - "A.6.RCD"
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
  - "C.36"
  - "E.18"
  - "F.6"
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
| LLM output as architecture | Plausible prose and a diagram may denote a modal architecture claim and its representation; neither supplies obtaining relation occurrences, an A.22 structure, bearer feasibility, decision, or realization. | Recover the exact architecture claim or ClaimAddress, identify the diagram as a C.29 representation only when used, state the admission condition and return, and let C.32 consume the modal proposal without actualizing it. Use `C.32.PAD` and `C.32.ADR` for decision and ADR claims. |
| Pareto point as admission | A Pareto result records trade-off position under chosen criteria; its graph, table, or file is a neighboring representation or publication item, not architecture adequacy. | Name the exact result and the current next-use condition. Add search space, criteria, constraints, bearer boundary, and eval return only when the candidate use relies on them; then handle that use under `C.32`. |
| One output as reusable-generator governance | A single generated artifact does not describe the method, mechanism suite, dataset, prompt policy, or refresh process that produced a reusable generator. | Keep the one-case output in C.35 and open `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains the reusable-generator claim. |
| Cluster as module architecture | A cluster claim can expose co-change or dependency pressure while leaving functional-bearer semantics, interface substitutability, and obtaining relation occurrences unknown; its matrix or file does not settle that gap. | Recover the exact cluster result, extraction basis, observed and inferred content, unknowns, coverage, uncertainty, validation, and any C.29 representation. Keep the inferred organization modal unless A.22 passes; handle modularity and reuse under `C.31` and candidate use under `C.32`. |
| Transformation output as feasibility proof | A graph grammar or model-transformation Method can return a useful claim and representation while proving neither an actual `U.Transformation` nor an obtaining A.22 result structure. | Record the exact result, C.29 representation only when used, Method, Work and attribution when current, transformation trace, exact source and result objects, preservation, loss, and bearer boundary. Keep a proposed result organization in its architecture claim; cite A.22 only after its four discriminators resolve, and cite A.3.4 plus the Work-to-change or A.15.PROD claim for any actual change. |
| Bypassing eval and measurement governance | A search score, benchmark, ablation, or validation trace can look like proof of architecture quality. | Handle readings under `C.16`, Q-bundle use to `C.25`, eval programs and eval results to `C.32.ACE`, and decisions to `C.32.PAD`. |

