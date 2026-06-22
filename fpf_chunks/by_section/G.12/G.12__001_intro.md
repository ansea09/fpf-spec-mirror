---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__001_intro.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:intro — Intro"
line_start: 88171
line_end: 88184
dependencies:
  - "A.19"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.5.2"
  - "F.17"
  - "F.18"
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
  - "PathId/PathSliceId"
  - "RSCR/refresh wiring"
  - "UTS twins"
  - "admissible telemetry"
  - "dashboard"
  - "discipline health"
  - "edition pins"
  - "time-series"
  - "view-only slices"
---

## G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)

**Tag:** Architectural kit pattern (conceptual; notation‑independent; dashboard‑kit governing definition)

**Stage:** design‑time authoring **→** run‑time computation & publication (series and slices); **refresh/RSCR‑wired**

**Primary hooks:** **G.Core** (core invariants, linkage catalogues, RSCR trigger catalogue, Default Governing Definition Index), **C.21** (DHC slots + `DHCPack` / `DHCMethodSpec` / `DHCSeries` artefacts), **G.6** (EvidenceGraph; `PathId`/`PathSliceId` citation), **G.7** (Bridge calibration / CL & `Φ/Ψ/Φ_plane` policy surfaces; when crossings/plane routing is used), **G.11** (telemetry‑driven refresh/decay orchestration), **G.5** (selector set-result / set‑returning outputs, when dashboard consumes performance trade‑offs), **A.19** (CN‑Spec governance card), **G.0** (CG‑Spec legality gate), **F.17/F.18** (UTS + twin labels), **E.5.2** (notation independence), **E.10** (LEX discipline).
*(Optional, extension‑gated hooks:* **G.2** (SoTA palette & DHC alignment hooks), **C.18 and C.19** (QD / E‑E / OEE telemetry pins), **G.8** (SoS‑LOG bundle & maturity ladder view), **G.10** (shipping inclusion of dashboard slices).)*

**Why this exists.** **C.21** defines *what* lawful “discipline health” slots are (CHR‑typed; scale/legality aware; freshness‑windowed), but it does not, by itself, provide a **generation‑first** method for producing **edition‑pinned, evidence‑citable DHC time series** that remain refreshable under RSCR.
**G.12** is that dashboard method: it defines the **dashboard kit surfaces** (`DHCSeries@Context`, `DHCRow@Context`, `DashboardSlice@Context`, telemetry pins) and a pipeline for computing and publishing DHC readings **without shadow specs**, **without illicit arithmetic**, and **without smuggling scalar winners** out of partial orders or telemetry.

**Modularity note.** G.12 governs **dashboard publication units and wiring** only. It **does not** govern CN-Spec, CG-Spec, CHR, CAL, selection semantics, evidence semantics, shipping, or refresh heuristics. It binds to those governing definitions via refs/pins/editions/policy‑ids and keeps any method‑/generator‑specific panels strictly inside **Extensions** (`GPatternExtension` blocks).

