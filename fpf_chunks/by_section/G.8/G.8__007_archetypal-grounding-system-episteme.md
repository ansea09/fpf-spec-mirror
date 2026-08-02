---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "SoS‑LOG Bundles & Maturity Ladders"
section_id: "G.8:6"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__007_archetypal-grounding-system-episteme.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "G.8 — SoS‑LOG Bundles & Maturity Ladders"
  - "G.8:6 — Archetypal Grounding (System / Episteme)"
line_start: 100587
line_end: 100599
dependencies:
  - "A.10"
  - "A.21"
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
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `RuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (governed by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.
**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (governed by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.

**Show‑B — QD archive dispatch with edition‑pinned descriptors (post‑2015 QD families).**
A method family uses a modern QD line (e.g., CMA‑ES‑driven archives, differentiable QD variants, and large‑scale JAX‑style QD toolchains). The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show‑C — Open‑ended environment–method co‑evolution (post‑2018 open‑ended families).**
A generator family operates in an open‑ended setting (e.g., POET‑style and PAIRED‑style regimes). The bundle carries `TransferRulesRef.edition` and validity region pins; unknown transfer validity triggers a `degrade` branch rather than an ad‑hoc fourth status. Telemetry (coverage/regret proxies) is emitted for refresh planning, not silently turned into dominance.

