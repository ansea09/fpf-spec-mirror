---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:8"
section_title: "Archetypal grounding (informative; SoTA‑oriented)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__012_archetypal-grounding-informative-sota-oriented.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:8 — Archetypal grounding (informative; SoTA‑oriented)"
line_start: 92495
line_end: 92508
dependencies:
  - "A.19"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.22.1"
  - "C.23"
  - "C.27"
  - "C.28"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:8 — Archetypal grounding (informative; SoTA‑oriented)

**Show‑A — Multi‑tradition parity for decision systems (post‑2015 practice).**
ParityPlan pins a rolling evidence window and comparator refs; ParityReport publishes a selected-set outcome plus the evidence trace. Family labels such as preference-learning comparators, causal decision pipelines, offline-RL evaluation pipelines, and robust BO-style selectors remain illustrative until a `G.2` SoTA pack or named current source pins the exact family being compared; the parity report still must preserve the selected set or partial order rather than collapse everything into a single scalar.

**Show‑B — QD parity (MAP‑Elites lineage; CMA-MAE `arXiv:2205.10752`; DQD `arXiv:2106.03894`; QDax `arXiv:2308.03665`; QDHF or QDAIF refs only when a feedback-guided QD claim is live).**
ParityPlan pins descriptor/distance definitions and archive insertion policy editions. ParityReport includes archive outcomes and telemetry deltas needed for refresh, without silently converting illumination summaries into dominance.

**Show‑C — Open‑ended parity (POET `arXiv:1901.01753` as lineage; AlphaEvolve `arXiv:2506.13131` when the live generator-family claim is coding-agent discovery; other current generator-family claims require a named `G.2` SoTA pack or exact current source).**
ParityPlan pins transfer rule editions and exploration policy refs. ParityReport publishes selected-set outcomes plus transfer‑keyed traces (PathSlice), enabling refresh reruns when any pinned policy changes.

**Show-D — Causal method rung parity.**
A team compares an observational predictor, an intervention optimizer, and a counterfactual policy strategy under one "best causal method" headline. `G.9` first runs `CausalRungParityScreen`: if rungs, support bases, estimands, or outcome windows differ, the screen returns degraded parity or abstain before a full record is fabricated. When full parity remains plausible, `G.9` requires `CausalMethodRungParityRecord`: each method declares `targetCausalUseClaimKind`, target `CausalityLadderRung`, `estimandRef`, interventional-action basis, `CausalEvidenceSupportBasis`, relevant `C.28` support record and verdict when consumed, follow-up window, outcome measure, source population and target population basis, and estimation-validity basis. If those fields differ, the parity report names `declaredCausalityLadderBridgeOrLossRef`, transportability or estimation refs where available, and degraded parity or abstain result. The admissible output may be a selected set by comparable rung, not one scalar winner.

