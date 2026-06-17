---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open‑Ended Search Calculus (NQD‑CAL)"
section_id: "C.18:6"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__007_archetypal-grounding.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "C.18 — Open‑Ended Search Calculus (NQD‑CAL)"
  - "C.18:6 — Archetypal Grounding"
line_start: 43972
line_end: 43975
dependencies:
  - "A.1"
  - "A.15"
  - "A.17-A.19"
  - "B.5.2.1"
  - "C.16"
  - "C.17"
  - "C.19"
  - "C.2"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "CandidateSet"
  - "DescriptorMapRef"
  - "DistanceDefRef"
  - "EmitterPolicyRef"
  - "Front vs ExplorationArchive"
  - "IlluminationSummary report-only telemetry"
  - "InsertionPolicyRef"
  - "NQD-CAL"
  - "NQDArchive"
  - "provenance editions"
  - "Γ_nqd.generate"
  - "Γ_nqd.illuminate"
  - "Γ_nqd.selectFront"
  - "Γ_nqd.updateArchive"
---

### C.18:6 - Archetypal Grounding
**System.** Legged‑robot gait exploration: `Q = {forward speed, energy efficiency}`; `DescriptorMap/CharacteristicSpace = morphology/coordination descriptors (ℝ^d)`; `D = ΔDiversity_P(h | Pool)` computed over that declared descriptor space; `Archive = CVT grid`; illumination reports coverage without entering dominance.
**Episteme.** SoTA palette synthesis: `Q` is one declared objective tuple for the current synthesis task, for example external-validity gain, reuse value, or `Use-Value` only when the Context explicitly declares it inside `Q`; `DescriptorMap/CharacteristicSpace` carries method-family or claim-graph descriptors; `D = ΔDiversity_P(h | Pool)` is computed over that declared descriptor space or niche grid. Publish `DescriptorMapRef.edition` and `DistanceDefRef.edition` so the front remains reproducible.

