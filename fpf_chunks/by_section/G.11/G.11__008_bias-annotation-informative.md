---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:6"
section_title: "Bias-Annotation (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__008_bias-annotation-informative.md"
commit_sha: "2154d21570c891bd5ed30fd6e6136f17f1942cae"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:6 — Bias-Annotation (informative)"
line_start: 107187
line_end: 107196
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
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:6 - Bias-Annotation (informative)

Bias lenses: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions and policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: create queue, plan and report content only for the corresponding need; retain applicable support without an omission certificate, while preserving warnings a later receiver needs.
* **Onto and Epist bias (toward one governing definition semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System and Episteme grounding and keep SoTA-echoing explicit.

