---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:3"
section_title: "Problem & Context (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__004_problem-context-informative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:3 — Problem & Context (Informative)"
line_start: 40852
line_end: 40863
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

### C.16:3 - Problem & Context (Informative)

#### C.16:3.1 - The problem C.16 solves

Across FPF patterns, people say “score”, “metric”, “rating”, “property”. Without a shared substrate, numbers drift: *42 of what? on which scale? comparable to whom?* C.16 eliminates drift by requiring every metric notion to **bind** to **one** Characteristic and **one** Scale, and by **separating** Characteristic/template bindings from descriptions and ScoringMethods. The result is **portable meaning**: a measure is always readable as a **Coordinate on a declared Scale of a named Characteristic**, with a principled path to evidence.

#### C.16:3.2 - Context and prior art

* **Kernel canon.** A.17 makes **Characteristic** the sole canonical head for measurability; A.18 fixes **CSLC** as the minimal sufficiency for interpretability. C.16 relies on both.
* **Cross‑domain alignment.** The MM‑CHR family already maps FPF U.Types to **ISO 80000‑1 (Quantity)**, **ISO/IEC 25024 (Data‑quality Characteristic)**, **QUDT (QuantityKind and QuantityValue)**, **W3C SOSA/SSN (Observable, Observed, and Result)**, and domain “feature/metric” usage (Verspoor, TF Metrics). C.16 uses these rows **as Bridges** (Part F), preserving local senses and documenting losses.
* **Open‑ended evolution.** FPF replaces “lifecycle” with **Role‑State Graph (RSG)** style state checklists (A.2.5): movement is along **certified states** with checklists; re-entry is valid when distinctions change. C.16 uses this device only to frame **readiness** and **revision** of metric notions conceptually (no processes implied).

