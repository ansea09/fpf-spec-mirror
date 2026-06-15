---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__010_bias-annotation.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:6 — Bias-Annotation"
line_start: 59742
line_end: 59753
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.9:6 - Bias-Annotation

| Lens | Bias risk in DRR use | Mitigation in this pattern |
|---|---|---|
| **Gov** | The DRR can become a bureaucratic approval ritual rather than a decision-rationale record. | Keep `CC-DRR.5` for lightweight editorial changes and require richer DRRs only when the content decision is semantically load-bearing. |
| **Arch** | A rich DRR can become a shadow specification that competes with the selected Core patterns and selected non-pattern FPF kind-reference pairs. | Treat the DRR as a temporary convergence aid; enduring content is distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs. |
| **Onto/Epist** | Authors can mix content decisions, evidence paths, source-use grounds, process state, and provenance into one ambiguous object. | Require exact decision grounds and selected-answer boundaries while excluding process-order state, baton, packet, and mutable status state from the DRR. |
| **Prag** | The method adds work before editing Core text. | Allow pointer-based DRRs and require only the selected non-pattern FPF kind-reference pairs materially needed for the selected decision. |
| **Did** | Rationale can become too internal for later authors to use. | Distill stable rationale, consequences, anti-cases, and SoTA implications into informative pattern sections when the Core text is updated. |

Scope: this bias annotation is universal for FPF semantic changes governed by `E.9`. It does not turn project-management state, helper state, or review logistics into DRR content.

