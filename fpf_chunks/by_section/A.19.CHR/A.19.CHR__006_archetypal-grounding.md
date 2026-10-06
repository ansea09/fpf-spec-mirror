---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite: Shared Rules for Characterization and Selection"
section_id: "A.19.CHR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__006_archetypal-grounding.md"
commit_sha: "2c16067fe8c7f34ea3313d66d36738870f5c2087"
heading_path:
  - "A.19.CHR — CHRMechanismSuite: Shared Rules for Characterization and Selection"
  - "A.19.CHR:5 — Archetypal Grounding"
line_start: 34888
line_end: 34905
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

### A.19.CHR:5 - Archetypal Grounding

#### A.19.CHR:5.1 - `U.System` vignette (Tell–Show–Show)

**Tell.** A system-level decision must select a declared set of options when measurable evidence comes from multiple slices (test rigs, simulations, field trials). Measurements are multi-scale and not always comparable without explicit normalization, and some evidence is missing or stale. The team needs lawful comparison and selection without forcing a single scalar “fitness”.

**Show.** Use the filled reference selection in §4.8.1 as the baseline: exact contracts, scales, methods, time rule and policies yield a retained set of two offers. When the inputs instead come from tests or field trials, replace the stipulated case evidence with the evidence required by the actual CN-Spec/CG-Spec; incomplete evidence follows the declared failure rule. A claimed dated Work and any launch witness require their independent enactment basis. Any actual semantic/kind/plane relation or flow/gate crossing retains its own required anchors.

**Show.** If the team instead embeds normalization inside scoring (“we always normalize to [0,1]”) or collapses a partial order into a single weighted sum, the suite protocol explicitness and “no silent scalarization/totalization” obligations make the violation legible at review time, and the planned baseline cannot honestly pin the missing UNM/ULSAM steps.

#### A.19.CHR:5.2 - `U.Episteme` vignette (Tell–Show–Show)

**Tell.** A research episteme compares methodological claims across traditions where some evaluation scales are ordinal (rank-based) and others are interval or ratio. The group wants to select a method family for a task while keeping uncertainty explicit and avoiding illicit aggregation (e.g., averaging ranks).

**Show.** The episteme’s planned baseline pins `CNSpecRef` (comparability mode and indicator policy) and `CGSpecRef` (SCP, ComparatorSet, MinimalEvidence, Γ_fold). The suite runs `UINDM` to select indicators, `USCM` to compute lawful score measures under SCP, `ULSAM` only when Γ_fold is explicitly selected, and `CPM` to compare without scalarizing partial orders. The selector returns a selected set rather than forcing a single winner.

**Show.** If a draft evaluation writes “take the mean rank and pick the minimum”, replace that step with a scale-lawful comparator declared in CG-Spec. For report-only telemetry, retain the rank distribution or another summary justified by the declared ordinal scale, such as a median when applicable. An arithmetic mean requires a separately justified quantitative model; calling it telemetry does not make ordinal averaging lawful.

