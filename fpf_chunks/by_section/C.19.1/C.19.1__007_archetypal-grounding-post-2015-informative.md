---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:5"
section_title: "Archetypal grounding (post-2015; informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__007_archetypal-grounding-post-2015-informative.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:5 — Archetypal grounding (post-2015; informative)"
line_start: 60926
line_end: 60946
dependencies:
  - "A.0"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.24"
  - "E.23"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP‑waiver"
  - "Scale‑Audit"
  - "alpha and delta tolerances"
  - "general-solution preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
---

### C.19.1:5 - Archetypal grounding (post-2015; informative)

These computational examples illustrate where a scale comparison may be useful; they supply no empirical conclusion for another bearer family. Each actual comparison still needs its task family, comparator, budget and safety basis, uncertainty, applicable alpha/delta tolerances and any source-currentness condition required by its receiving use.

* **LLMs:** prompt programs, **retrieval-augmented** policies, and **MoE** policies compared with narrow task-specific pipelines; set-returning selection across editions and budgets.
* **RL and planning:** model-based optimization and general agents compared with hand-coded controllers, subject to alpha and delta tolerances and safety.
* **Preference learning:** comparisons between **RLHF** and **DPO** families.
* **QD and OEE:** MAP-Elites, **CMA-ME**, **DQD**, and **QDax**; **POET** and **Enhanced-POET**; illumination remains **report-only telemetry** unless policy promotes it.

**Completed bounded comparison.** Suppose a specialist and a general search method are tested on the same fixed task set at three matched budgets on the same processor. The account includes the full computational cost, keeps the other material conditions fixed and supplies the following uncertainty bounds for the percentage of tasks solved. Both methods satisfy the same applicable safety and eligibility conditions; no separate assurance result is consumed. The budget tolerance is `alpha = 0` CPU-seconds at each matched point.

| Budget | Specialist: solved tasks | General method: solved tasks |
| --- | --- | --- |
| 100 CPU-seconds | 83–85% | 79–81% |
| 200 CPU-seconds | 85–87% | 89–91% |
| 400 CPU-seconds | 86–88% | 94–96% |

The specialist wins at the first probed budget, while the general method wins at the other two even after allowing for the supplied uncertainty. Neither response dominates across all three probed budgets. Return `no scale-based preference` for that whole comparison; the word general does not reverse it. The result supports the stated comparisons at those points, not an interpolated law between them or a claim outside the window.

If the receiving choice is confined to 100 CPU-seconds, the specialist's bounded advantage can be used under that question's comparison rule. A separately declared prefer-general policy, if applicable, still needs its own tie-break or waiver treatment. No such policy is stipulated here, so no waiver or debt entry is created merely to report these results. Changing the task family, hardware-cost account or budget window reopens the dependent comparison. This is a constructed application, not a new benchmark finding.

