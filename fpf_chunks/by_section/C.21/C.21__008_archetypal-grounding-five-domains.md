---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:6"
section_title: "Archetypal Grounding (five domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__008_archetypal-grounding-five-domains.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:6 — Archetypal Grounding (five domains)"
line_start: 51516
line_end: 51539
dependencies:
  - "A.10"
  - "A.17"
  - "A.17-A.18"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.2.1"
  - "C.20"
  - "C.I"
  - "E.24.PUB"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "alignment"
  - "discipline"
  - "disruption"
  - "field health"
  - "reproducibility"
  - "standardisation"
---

### C.21:6 - Archetypal Grounding (five domains)

#### C.21:6.1 - Computer vision: direct comparison without a Bridge

Two `ReproducibilityRate` results concern the same benchmark population and ClaimScope. Both cite the same Characteristic and ratio Scale editions, the same `DHCMethodRef.edition`, compatible model and calibration rules, and matching 24-month population windows. The team compares the two rates directly under that basis. The source reports have different publication editions, but no distinct F.17 local senses are being related, so no F.9 relation is invented.

Formal benchmark approval and actual benchmark adoption are reported separately as `FormalRecognitionStatus` and `PracticeAdoptionRate`.

#### C.21:6.2 - Biomedicine: evidence resolution without ratio substitution

One claim reports `EvidenceUnitResolution = claim` under `ClinicalClaimSegmentation-3`. A separate result reports `SupportAnchorsPerClaim = 2.4 anchors/claim` for the declared corpus. Neither value is substituted for `ClaimsPerArtifact`. Replication is a separate `ReproducibilityRate` over independent cohorts and a 36-month window.

#### C.21:6.3 - Software performance engineering: explicit cross-local use

The compared cells are `OpenTelemetry:SLO/latency-objective@E4` and `VendorB:SLO/service-level-target@E7`. Relation `F9-SPE-SLO-12` obtains from the OpenTelemetry cell to the VendorB cell for the admitted use “compare service-latency objective coverage in the 2026 survey.” Its loss note says the target cell permits a different rolling-window convention, so only rows with the aligned 30-day window enter the comparison. That directed relation is one counted member of the declared AlignmentDensity cell set; it does not make all tracing-ecosystem readings comparable.

#### C.21:6.4 - Decision-making: entropy and concentration stay separate

`TraditionShareEntropy` uses normalized Shannon entropy with base and category set fixed. `TraditionShareConcentration` uses HHI over the same population and has the opposite dispersion direction. A view may show both. If a receiving comparison wants one orientation, it declares `1-HHI` as a transformation and still does not equate that Scale with normalized entropy.

#### C.21:6.5 - Evolutionary architecture: banded disruption

`DisruptionBalance` is computed over one declared corpus and method edition. The result is interpreted against an explicit target band and distance rule; a higher raw value is not automatically healthier. Architecture decision records and fitness tests remain inputs or neighboring objects, not evidence that the field itself is healthy.

