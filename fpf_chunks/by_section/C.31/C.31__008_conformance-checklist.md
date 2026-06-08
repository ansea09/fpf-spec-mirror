---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__008_conformance-checklist.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:7 — Conformance Checklist"
line_start: 54925
line_end: 54941
dependencies:
keywords:
---

### C.31:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-C31-1` | Ordinary use starts with `ModularityVectorLite`, three characteristics under evaluation at most, observed problem, repair direction, and stop condition. |
| `CC-C31-2` | Each characteristic head under evaluation is classified as `DirectCharacteristic`, `CompositeCharacteristicDescription`, `LensBackedCharacteristic`, `TemporalOrScaleCharacteristic`, `CausalUseSensitiveCharacteristic`, or `ReportOnlyProxy`. |
| `CC-C31-3` | A decision-facing or publication-facing head has `MeasurementHeadMapping`, C.16-compatible fields, and a required evidence path, source relation, or explicit evidence-claim-absent reason before it is relied on. |
| `CC-C31-4` | Each characteristic row states at least one repair move or claim named by value-governance assignment. |
| `CC-C31-5` | Report-only proxies state forbidden overread and do not establish beyond-local-repair use. |
| `CC-C31-6` | Proxy-risk and audit-question fields are present for decision-facing cards. |
| `CC-C31-7` | Complexity, residual, and growth heads remain claim-scoped cues; apply C.29, C.31.ASAP when an architecture scale-preference claim is being made, C.27, C.28, C.16, C.25, C.30.ILC, C.31.RSA, G.5, or C.11 when the corresponding claim kind is being made. |
| `CC-C31-8` | No C.31 text treats modularity as a single quality proof, assurance proof, gate result, causal proof, or architecture decision. |
| `CC-C31-9` | Any score discloses scoring method, codomain, polarity, characteristic basis, comparability basis, and use boundary through the governing pattern. |
| `CC-C31-10` | SoTA seeds for DSM, modularity-index, empirical modularity, platform, evidence-reuse, Conway and mirroring, Amdahl, queueing, coordination-overhead, information-hiding, abstraction-leakage, or Goodhart and Campbell proxy-risk sources are converted into pattern-local `G.2` rows before C.31 uses them for practitioner guidance being relied on. |
| `CC-C31-11` | Source labels such as block, layer, expert, cache, router, or gate use `C.30.STRAT` before they become C.31 characteristic subjects, scale cues, repair moves, or proxy-risk rows. |
| `CC-C31-12` | A vector, card, or report-only proxy states a lowering or reopen condition when proxy audit worsens, measurement or comparability basis changes, evidence path or source relation becomes stale, characteristic head changes, or a related governing pattern changes. |

