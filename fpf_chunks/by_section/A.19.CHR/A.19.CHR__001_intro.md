---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite: Shared Rules for Characterization and Selection"
section_id: "A.19.CHR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__001_intro.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.CHR — CHRMechanismSuite: Shared Rules for Characterization and Selection"
  - "A.19.CHR:intro — Intro"
line_start: 34060
line_end: 34072
dependencies:
  - "A.15.2"
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "A.6.7"
  - "A.6.RCD"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.19"
  - "G.0"
  - "G.10"
  - "G.5"
keywords:
  - "Bridge-only transport"
  - "CG-Spec"
  - "CHR suite"
  - "CN-Spec"
  - "P2W seam"
  - "SlotFillingsPlanItem"
  - "admissibility gate"
  - "characterization core"
  - "crossing visibility"
  - "no hidden scalarization"
  - "no hidden thresholds"
  - "penalties→R_eff"
  - "planned baseline"
  - "set-return selection"
  - "suite obligations"
  - "tri-state guard decision"
---

## A.19.CHR - CHRMechanismSuite: Shared Rules for Characterization and Selection

> **Type:** Architectural (A)
> **Status:** Stable

**Use this when.** A characterization or selection task combines normalization, indicator choice, scoring and comparison, and the stages must agree on admissibility, uncertainty and the meaning of their results. A locally reasonable calculation can still be unusable downstream if it changes a scale, hides a default or discards a distinction needed for comparison.

**Start here.** Select the exact declaration edition for each of the six CHR roles in §4.2. For the intended protocol, resolve each stage to its operation and governing specifications before choosing input values. The first useful result is a chain whose arguments, results and stop conditions agree. §4.8.1 works this through from a baseline to a concrete selected set.

**Ordinary boundary.** For one operation, use its A.19 member pattern directly. For a different set of jointly used contracts, use A.6.7. For an edition/reference plan without shared CHR conditions, use A.15.2. A CHR suite describes the shared contract; actual applications, gate decisions and publication retain their own rules.

`CHRMechanismSuiteDescription` is the canonical `MechSuiteDescription` instance for the six CHR roles. Its selected edition can be cited through `MechSuiteDescriptionRef`. An ordinary A.15.2 WorkPlan records the chosen baseline; `CHRMechanismSuiteSlotFillingsPlanItem` is used only when A.15.3 typed filling is needed for an independently declared position.

