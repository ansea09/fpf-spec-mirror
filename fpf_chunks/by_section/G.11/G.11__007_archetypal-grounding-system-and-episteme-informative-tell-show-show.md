---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:5"
section_title: "Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__007_archetypal-grounding-system-and-episteme-informative-tell-show-show.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:5 — Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)"
line_start: 106259
line_end: 106266
dependencies:
  - "A.6.RCD"
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

### G.11:5 - Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump and calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). `G.11` does not “rebuild the whole maintenance doctrine”: it emits a refresh plan scoped to the affected inspection slices and publishes a refresh report with pins to the updated standard edition and the evidence or source relations. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by subject pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims and parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL or plane penalties. `G.11` ingests canonical trigger kinds, computes the minimal closure over affected `PathSliceId`s, schedules targeted parity reruns, then re-ships the pack through the pattern governing shipping semantics while publishing an edition bump log that makes the evolution replayable.

