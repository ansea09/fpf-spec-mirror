---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
section_id: "G.8:6"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__007_archetypal-grounding-system-episteme.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "G.8 — Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
  - "G.8:6 — Archetypal Grounding (System / Episteme)"
line_start: 130082
line_end: 130092
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.23"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "SoS-LOG"
  - "admissibility ledger"
  - "rule ids"
  - "tri-state {pass"
---

### G.8:6 - Archetypal Grounding (System / Episteme)

**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (for example, conservative offline RL and transformer-based policy models). The bundle cites `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`) and cites `AcceptanceClauseId[]` for any floors (governed by `G.4`). The run‑time `AdmissibilityLedger` cites `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.

**Show-B — QD archive dispatch with edition-pinned descriptors.**
A method family uses a QD archive, for example one driven by CMA-ES or a differentiable QD method. The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show-C — Open-ended environment–method co-evolution.**
A generator family operates in an open‑ended setting (e.g., POET‑style and PAIRED‑style regimes). The bundle carries `TransferRulesRef.edition` and validity region pins; unknown transfer validity triggers a `degrade` branch rather than an ad‑hoc fourth status. Telemetry (coverage/regret proxies) is emitted for refresh planning, not silently turned into dominance.

