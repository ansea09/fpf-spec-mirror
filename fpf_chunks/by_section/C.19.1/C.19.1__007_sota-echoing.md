---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:5.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__007_sota-echoing.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:5.1 — SoTA-Echoing"
line_start: 50101
line_end: 50108
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
  - "C.5"
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

### C.19.1:5.1 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Practitioner implication |
|---|---|---|---|
| Yousefi and Collins, `Learning the Bitter Lesson: Empirical Evidence from 20 Years of CVPR Proceedings`, arXiv:2410.09649, as current empirical pressure around Sutton's 2019 Bitter Lesson. | Treat general scale-amenable approaches as a live preference pressure that must be tested through declared comparison, not as folklore. | "General" or "Bitter Lesson" is proof without task-family, safety, cost, and scale-window evidence. | Use `Scale-Audit` or `BLP-waiver` before turning the slogan into selector-facing preference. |
| Kaplan et al., `Scaling Laws for Neural Language Models`, arXiv:2001.08361, and Hoffmann et al., `Training Compute-Optimal Large Language Models`, arXiv:2203.15556. | Keep compute, data, model size, budget, and scale-window relations explicit when a bearer is claimed to improve with scale. | Parameter count, compute spend, or one benchmark substitutes for the audited objective vector. | State the swept dimensions, alpha and delta tolerances, CI, and budget window before preferring the general bearer. |
| Lu et al., `The Bitter Lesson of Diffusion Language Models for Agentic Workflows: A Comprehensive Reality Check`, arXiv:2601.12979. | Treat current agentic-substrate claims as evaluation-sensitive and task-family-sensitive, especially when efficiency hype competes with reliability. | "More agentic" or "more efficient backbone" proves better workflow performance. | Keep agent-loop or substrate selection under `E.23`, `G.9`, and `C.19.1` with task-family evaluation, protected trade-offs, and stop/switch conditions. |

