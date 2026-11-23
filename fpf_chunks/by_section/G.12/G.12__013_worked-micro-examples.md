---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:11"
section_title: "Worked Micro-examples"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__013_worked-micro-examples.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:11 — Worked Micro-examples"
line_start: 142238
line_end: 142243
dependencies:
  - "A.19"
  - "A.2.6"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.21"
  - "C.29"
  - "E.10"
  - "E.24.PUB"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.Core"
keywords:
  - "DHC"
  - "DHCReplayBasis"
  - "DHCSeries"
  - "coordinate results"
  - "dashboard"
  - "discipline health"
  - "optional publication"
  - "selective refresh"
  - "time series"
  - "views"
---

### G.12:11 — Worked Micro-examples

**Decision-making dashboard.** A local view shows exact `ReproducibilityRate`, `FormalRecognitionStatus`, `PracticeAdoptionRate`, `AlignmentDensity`, `TraditionShareEntropy`, and `TraditionShareConcentration` result refs. A row showing 60% adoption among respondents gives the number who replied, the number eligible and the period. The portfolio owner asks whether at least half of all eligible units adopted the practice. Show the C.21 result for that population. If every admissible count reaches the threshold, it is met. If every count falls short, it is missed. Two admissible counts on opposite sides leave the answer open. If only an outer bound crosses the threshold, report the limit of that calculation. A tighter calculation with the existing observations may settle the question. The owner decides what to do. Entropy and HHI occupy separate rows with their directions visible. A portfolio panel preserves the G.5 selected set. No audience publication is claimed.

**Evolutionary architecture dashboard.** A `DHCSeries` episteme orders exact reproducibility and DisruptionBalance results over declared windows. An optional open-ended panel shows transfer events as telemetry. A later E.24.PUB occurrence makes the selected series edition available to a named audience in dashboard form; that occurrence neither changes the series content nor turns the rendering Work into the health result.

