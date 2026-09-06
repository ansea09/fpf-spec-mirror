---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__007_bias-annotation.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:6 — Bias-Annotation"
line_start: 67467
line_end: 67477
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

### C.35:6 - Bias-Annotation

| Bias | How C.35 counters it |
| --- | --- |
| Output authority bias | Require only the readable minimum before another architecture claim relies on the result: exact result, actual or proposed organization, next-use condition, and forbidden overread or return. Add representation, publication, branch, or other detail only when the use depends on it. |
| Pareto-point admission bias | Treat a Pareto point, benchmark score, archive member, or search trace as a candidate input cue until its branch-specific basis and the concrete candidate-use rule are named. |
| Reusable-generator collapse | Keep one-case output admission in C.35; handle reusable-generator, mechanism-suite, model-family, or production-pipeline claims with `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains those claims. |
| Bearer-free synthesis bias | Require bearer or realization boundary before treating a discovered function, relation, or candidate form as architecturally feasible. |
| Eval substitution bias | Handle eval programs and eval results under `C.32.ACE`; handle measurement under `C.16`; do not let good eval numbers act as candidate admission or decision authority. |
| Currentness freeze | Reopen when result identity or claim content, represented object or correspondence, source publication edition or source-use record, search space, query rule, validation trace, bearer constraints, realized structure, or eval return changes. A carrier-only change reopens C.35 only when availability or form changes the intended use. |

