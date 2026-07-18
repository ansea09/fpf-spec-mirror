---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:2"
section_title: "Problem — Why naive refresh breaks comparability and admissibility"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__004_problem-why-naive-refresh-breaks-comparability-and-admissibility.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:2 — Problem — Why naive refresh breaks comparability and admissibility"
line_start: 96270
line_end: 96279
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "decay"
  - "deprecation"
  - "edition bumps"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
---

### G.11:2 - Problem — Why naive refresh breaks comparability and admissibility

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Local trigger aliases are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS, Path, or policy pins) without a visible CrossingBundle.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance, `PortfolioMode`, or Γ-fold) or coerces partial orders into scalars “for convenience.”

