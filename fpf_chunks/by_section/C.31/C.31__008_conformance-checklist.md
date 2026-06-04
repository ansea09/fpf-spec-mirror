---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__008_conformance-checklist.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:7 — Conformance Checklist"
line_start: 54180
line_end: 54195
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31.RSA"
  - "G.5"
keywords:
  - "ModularityVectorLite"
  - "bespoke residue"
  - "cohesion"
  - "coupling"
  - "evidence reuse"
  - "interface variation"
  - "modularity characteristics"
  - "reusable-structure characteristics"
  - "substitutability"
---

### C.31:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-C31-1` | Ordinary use starts with `ModularityVectorLite`, three live characteristics at most, observed problem, repair direction, and stop condition. |
| `CC-C31-2` | Each live head is classified as `DirectCharacteristic`, `CompositeCharacteristicDescription`, `LensBackedCharacteristic`, `TemporalOrScaleCharacteristic`, `CausalUseSensitiveCharacteristic`, or `ReportOnlyProxy`. |
| `CC-C31-3` | A decision-facing or publication-facing head has `MeasurementHeadMapping` and C.16-compatible fields before it is relied on. |
| `CC-C31-4` | Each characteristic row states at least one repair move or exact governing pattern application. |
| `CC-C31-5` | Report-only proxies state forbidden overread and do not carry comparison, selection, assurance, publication, causal, or gate use. |
| `CC-C31-6` | Proxy-risk and audit-question fields are present for decision-facing cards. |
| `CC-C31-7` | Complexity, residual, and growth heads remain claim-scoped cues or apply C.29, exact scale-preference receivers, C.27, C.28, C.16, C.25, C.30.ILC, C.31.RSA, G.5, or C.11 as live. |
| `CC-C31-8` | No C.31 text treats modularity as a single quality proof, assurance proof, gate result, causal proof, or architecture decision. |
| `CC-C31-9` | Any score discloses scoring method, codomain, polarity, characteristic basis, comparability basis, and use boundary through the exact governing pattern. |
| `CC-C31-10` | SoTA seeds for DSM, modularity-index, empirical modularity, platform, evidence-reuse, Conway and mirroring, Amdahl, queueing, coordination-overhead, information-hiding, abstraction-leakage, or Goodhart and Campbell proxy-risk sources are converted into pattern-local `G.2` rows before they carry live practitioner guidance. |
| `CC-C31-11` | Source labels such as block, layer, expert, cache, router, or gate use `C.30.STRAT` before they become C.31 characteristic subjects, scale cues, repair moves, or proxy-risk rows. |

