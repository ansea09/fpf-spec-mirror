---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:7"
section_title: "Anti‑patterns and remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__011_anti-patterns-and-remedies.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:7 — Anti‑patterns and remedies"
line_start: 105171
line_end: 105180
dependencies:
  - "A.19"
  - "A.2.6"
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
  - "U.ClaimScope"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:7 — Anti‑patterns and remedies

* **AP‑1 Hidden edition drift.** Remedy: require edition pins in `ParityPinSet`; treat changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑2 Baseline set is informal prose.** Remedy: require `BaselineBindingRef` and EvidenceTrace pins.
* **AP‑3 Comparator semantics are “whatever the code did”.** Remedy: `ComparatorSpecRef.edition` (and any normalization/comparability refs) must be cited and pinned.
* **AP‑4 Cross-sense or reference-plane reuse without its obtaining relation and visible pins.** Remedy: recover the exact F.17 cells and cite the obtaining F.9 relation when local meanings differ; cite the exact reference-plane crossing basis and visibility records when planes differ (delegated to G.Core).
* **AP‑5 Parity report becomes a hidden scoring sheet.** Remedy: preserve CSLC-admissible outcome shape and keep telemetry as telemetry unless explicitly policy‑promoted by the governing policy pattern.
* **AP‑6 “Metric” as a primitive in Tech.** Remedy: name the exact `CharacteristicRef`, `ScaleRef`, `UnitRef` when applicable, `DHCMethodRef`, `MethodRef`, and `U.Measure` or result episteme; add `DistanceDefRef` only when used. “Metric” may appear only in Plain with a pointer to those canonical objects.
* **AP‑7 Hidden DHC replay drift.** Remedy: carry every active field of the C.21 replay basis and refuse parity reuse when a required field is unresolved or differs across the compared readings. Register refresh tests only for a named receiver that consumes those changes.

