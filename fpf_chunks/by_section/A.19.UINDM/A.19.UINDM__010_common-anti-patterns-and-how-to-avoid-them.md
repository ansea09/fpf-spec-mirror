---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Unified Indicatorization Mechanism (UINDM)"
section_id: "A.19.UINDM:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.19.UINDM — Unified Indicatorization Mechanism (UINDM)"
  - "A.19.UINDM:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 31407
line_end: 31420
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:8 - Common Anti‑Patterns and How to Avoid Them

* **“NCV ⇒ indicator.”** Treating all measurable characteristics as indicators. Violates “No implicit NCV⇒indicator.”

* **Indicatorization hidden in scoring.** A scoring method silently ignores some characteristics or introduces an implicit “feature selection” without an explicit indicator set.

* **Silent emptying.** When evidence is insufficient, returning an empty indicator set (or treating missing evidence as “pass”) without a tri‑state guard decision.

* **Cross‑context reuse without Transport.** Reusing an indicator set across contexts without naming Bridge/CL/ReferencePlane, thereby hiding penalties and violating crossing visibility.

* **Smuggling plan‑binding into the mechanism.** Binding concrete edition pins / planned slot fillings (“launch values”) inside the UINDM description instead of using the P2W seam (WorkPlanning) and recording only effective refs/pins in `Audit`.

* **GateDecision leakage.** Emitting or implying GateDecision/GateLog as part of the `indicatorize` step (gate decisions are separated from suite steps; keep UINDM at guard+audit level).

