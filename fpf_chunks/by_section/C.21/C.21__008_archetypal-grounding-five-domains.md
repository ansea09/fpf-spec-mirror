---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:6"
section_title: "Archetypal Grounding (five domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__008_archetypal-grounding-five-domains.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:6 — Archetypal Grounding (five domains)"
line_start: 65639
line_end: 65666
dependencies:
  - "A.10"
  - "A.17-A.18"
  - "A.19"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.2.1"
  - "C.20"
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
  - "diversity"
  - "evidence resolution"
  - "field health"
  - "formal recognition"
  - "practice adoption"
  - "reproducibility"
  - "standardisation"
---

### C.21:6 - Archetypal Grounding (five domains)

#### C.21:6.1 - Computer vision: direct comparison without a Bridge

Two `ReproducibilityRate` results concern the same named set of tested benchmark claims in matching 24-month windows. They cite the same Characteristic and ratio Scale editions, the same `DHCMethodRef.edition`, and compatible model, calibration and independent-team conditions. The team can compare the rates for that set. If two reports tested different subsets of a common benchmark, state what was tested in each. An inference about the common benchmark population also depends on how the claims were selected. The source reports have different publication editions, but no distinct F.17 local senses are being related, so no F.9 relation is required.

Formal benchmark approval and actual benchmark adoption have separate results, `FormalRecognitionStatus` and `PracticeAdoptionRate`. Ten teams are eligible this quarter. Count a team as an adopter if it used the benchmark in a qualifying test during that quarter. The records establish use for four teams and no qualifying use for two. Either status remains possible for each of the other four, with no further joint restriction. Between four and eight of the ten could be adopters. A decision that requires at least six adopters is still open. Confirming qualifying use by two distinct teams among the four with unknown status would settle it even if the last two statuses remain unknown. The rate among the six teams with known status answers a different question.

#### C.21:6.2 - Biomedicine: evidence resolution without ratio substitution

One claim reports `EvidenceUnitResolution = claim` under `ClinicalClaimSegmentation-3`. A separate result reports `SupportAnchorsPerClaim = 2.4 anchors/claim` for the declared corpus. Neither value is substituted for `ClaimsPerArtifact`. Replication is a separate `ReproducibilityRate` over independent cohorts and a 36-month window.

#### C.21:6.3 - Software performance engineering: explicit cross-local use

The compared cells are `OpenTelemetry:SLO/latency-objective@E4` and `VendorB:SLO/service-level-target@E7`. For this example, take `F9-SPE-SLO-12` as an independently established directed F.9 Bridge from the OpenTelemetry cell to the VendorB cell under a satisfied predicate profile.

A separate C.2.1 bounded-use claim states suitability for “compare service-latency objective coverage in the 2026 survey” in that direction, using only rows with the aligned 30-day window and tolerating no rolling-window mismatch. The evidence loss note records that the target cell permits a different rolling-window convention; the comparison still requires current A.10 reliance on the bounded-use claim.

That directed relation is one counted member of the declared AlignmentDensity cell set; it does not make all tracing-ecosystem readings comparable.

#### C.21:6.4 - Decision-making: entropy and concentration stay separate

`TraditionShareEntropy` uses normalized Shannon entropy with base and category set fixed. `TraditionShareConcentration` uses HHI over the same population and has the opposite dispersion direction. A view may show both. If a receiving comparison wants one orientation, it declares `1-HHI` as a transformation and still does not equate that Scale with normalized entropy.

#### C.21:6.5 - Evolutionary architecture: banded disruption

`DisruptionBalance` is computed over one declared corpus and method edition. The result is interpreted against an explicit target band and distance rule; a higher raw value is not automatically healthier. Architecture decision records and fitness tests remain inputs or neighboring objects, not evidence that the field itself is healthy.

