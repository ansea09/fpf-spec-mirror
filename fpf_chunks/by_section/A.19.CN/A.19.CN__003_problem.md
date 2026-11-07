---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__003_problem.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:2 — Problem"
line_start: 36431
line_end: 36439
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "loss evidence"
  - "maintained editions"
  - "normalization refs"
  - "optional CL"
  - "semantic relations"
  - "separate use claims"
  - "Γ-fold governance"
---

### A.19.CN:2 - Problem

When the comparison basis is missing or changes silently, these failures can occur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization changes.** Re-parameterisation, such as normalising by batch size, can change the quantity being compared while a trend line still appears continuous.
3. **CN-frame sprawl.** Unrelated dashboard definitions can leave receivers unable to establish a shared comparison basis.
4. **Incompatible roll-ups.** Cross-team roll-ups average **incongruent** CN-frames without a justified common comparison or aggregation model. Use B.3 when the result serves a named assurance claim.

