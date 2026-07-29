---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:3.2"
section_title: "Context and prior art"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__006_context-and-prior-art.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:3.2 — Context and prior art"
line_start: 46877
line_end: 46882
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

### C.16:3.2 - Context and prior art

* **Kernel canon.** A.17 makes **Characteristic** the sole canonical head for measurability; A.18 fixes **CSLC** as the minimal sufficiency for interpretability. C.16 relies on both.
* **Cross‑domain alignment.** The MM‑CHR family maps admitted FPF measurement values and C.3-governed kind values to **ISO 80000‑1 (Quantity)**, **ISO/IEC 25024 (Data‑quality Characteristic)**, **QUDT (QuantityKind and QuantityValue)**, **W3C SOSA/SSN (Observable, Observed, and Result)**, and domain “feature/metric” usage (Verspoor, TF Metrics). C.16 uses these rows **as Bridges** (Part F), preserving local senses and documenting losses.
* **Open‑ended evolution.** FPF replaces “lifecycle” with `RoleStateRelation@BoundedContext` state checklists (A.2.5): movement is admitted through **certified states** with checklists; re-entry is valid when distinctions change. C.16 uses this device only to frame **readiness** and **revision** of metric notions conceptually (no processes implied).

