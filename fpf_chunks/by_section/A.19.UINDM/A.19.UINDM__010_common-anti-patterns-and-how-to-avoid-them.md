---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 35323
line_end: 35338
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

* **Characteristic reference substituted for a position.** Temperature occurs at Celsius and kelvin positions, but the returned set contains only TemperatureRef. Resolve the policy to the requested position or its explicitly selected all-matches set before returning S.

* **Silent emptying.** When evidence is insufficient, returning an empty indicator set (or treating missing evidence as “pass”) without a tri‑state guard decision.

* **Reusing an indicator set after its basis or use changed.** Reusing it for another bearer, scope and window, evidence basis, reference plane, or intended use without a new eligibility decision; or naming Bridge or plane-relation pins without an actual obtaining relation.

* **Smuggling plan‑binding into the mechanism.** Binding concrete edition pins / planned slot fillings (“launch values”) inside the UINDM description instead of using the P2W seam (WorkPlanning) and recording only effective refs/pins in `Audit`.

* **GateDecision leakage.** Emitting or implying GateDecision/GateLog as part of the `indicatorize` step (gate decisions are separated from suite steps; keep UINDM at guard+audit level).

