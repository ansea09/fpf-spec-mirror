---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:8.3"
section_title: "Archetypal Grounding - Cross-Domain Vignettes (Informative, transdisciplinary)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__012_archetypal-grounding-cross-domain-vignettes-informative-transdisciplinary.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:8.3 — Archetypal Grounding - Cross-Domain Vignettes (Informative, transdisciplinary)"
line_start: 43436
line_end: 43455
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:8.3 - Archetypal Grounding - Cross-Domain Vignettes *(Informative, transdisciplinary)*

> *Each vignette shows an CSLC‑conformant template → measure, without duplicating the A.17 and A.18 glossaries.*

**V‑A (Architecture — relational property).**
Characteristic: **Coupling** (relational) between modules; Scale: ordinal {Low, Med, High}; Unit: level‑labels; Polarity: ↓ better.
Reading: subsystem pair ⟨M₁, M₂⟩ gets **Med**; **ScoringMethod** (optional) maps levels monotonically to a bounded Score for comparative dashboards.

**V-B (Physics — interval or ratio).**
Characteristic: **ResponseTime**; Scale: ratio with non‑negative reals; Unit: seconds; Polarity: ↓ better.
Reading: subject S has **0.237 s**; direct comparability holds with readings on the **same template**; cross‑template comparability requires an explicitly cited equivalence relation, Bridge, or transformation relation with its governing FPF pattern or specification record named.

**V‑C (Performing arts — ordinal).**
Characteristic: **EdgeControlQuality**; Scale: ordinal levels 1…5; Unit: level‑labels; Polarity: ↑ better.
Reading: performance P gets **4**; any aggregation remains order‑respecting. If a numeric dashboard score is needed, cite a scoring method **𝒢** that maps levels monotonically to a bounded Score.

**V‑D (AI ethics — ratio).**
Characteristic: **ParityGap** (difference of positive rates); Scale: interval with symmetric bounds; Unit: percentage points; Polarity: ↓ better (0 is target).
Reading: model M on cohort C shows **3.2 pp**; evidence points conceptually to the derivation rationale (inputs, reference cohorts).

