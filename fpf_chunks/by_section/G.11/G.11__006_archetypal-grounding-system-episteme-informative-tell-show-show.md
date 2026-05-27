---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh & Decay Orchestrator"
section_id: "G.11:5"
section_title: "Archetypal Grounding — System / Episteme (informative; Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__006_archetypal-grounding-system-episteme-informative-tell-show-show.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "G.11 — Telemetry-Driven Refresh & Decay Orchestrator"
  - "G.11:5 — Archetypal Grounding — System / Episteme (informative; Tell–Show–Show)"
line_start: 77971
line_end: 77978
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.11"
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

### G.11:5 - Archetypal Grounding — System / Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump + calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). `G.11` does not “rebuild the whole maintenance doctrine”: it emits a refresh plan scoped to the affected inspection slices (paths) and publishes a refresh report with pins to the updated standard edition and the evidence paths. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by governing pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims + parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL/plane penalties. `G.11` ingests canonical trigger kinds, computes the minimal closure over affected `PathSliceId`s, schedules targeted parity reruns, then re-ships the pack through the pattern governing shipping semantics while publishing an edition bump log that makes the evolution replayable.

