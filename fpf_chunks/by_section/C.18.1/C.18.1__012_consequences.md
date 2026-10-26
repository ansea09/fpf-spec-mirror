---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:11"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__012_consequences.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:11 — Consequences"
line_start: 60370
line_end: 60377
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "G.10"
  - "G.5"
  - "G.9"
keywords:
  - "DoE (design‑of‑experiments)"
  - "Scale Variables (S)"
  - "ScaleWindow"
  - "UNM/NormalizationMethod‑based mapping"
  - "compute‑elasticity"
  - "data‑elasticity"
  - "diminishing returns"
  - "elasticity class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "probe uncertainty"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

### C.18.1:11 - Consequences

**Benefits.** SLL prevents scale claims from becoming rhetoric. A comparison can show which knobs were scaled, what window is covered, how much probe evidence supports the slope class, and what parity or normalization losses are declared, with any assurance penalties affecting `R` only rather than silently changing dominance.

**Trade-offs.** A supported scale claim needs observations at at least two scale points and recoverable invariants, phase, seeds, uncertainty and any applicable policy thresholds. Reuse of an applicable account can avoid new probing. The gain is that selectors, parity harnesses, refresh telemetry, and mathematical-lens uses can cite one bounded scale claim instead of guessing whether the observed behavior transfers.

**Stop condition.** Stop at C.18.1 when the scale variable, ScaleWindow, probe basis, supported class or explicit classification limit, and parity notes suffice for the receiving question. An unresolved class can finish this inquiry while leaving a scale-dependent preference unsupported. Select further probing only when its attainable contribution to the decision warrants its burden; use C.11.DUA if that choice needs resolution. Move to `G.9`, `C.19`, `G.11`, `C.29`, or a domain annex when parity, selector policy, telemetry refresh, mathematical lens, or numeric fit becomes the live object.

