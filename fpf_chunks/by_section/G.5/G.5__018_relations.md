---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher & MethodFamily Registry"
section_id: "G.5:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__018_relations.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "G.5 — Multi‑Method Dispatcher & MethodFamily Registry"
  - "G.5:12 — Relations"
line_start: 71648
line_end: 71666
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry/eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-surface outcome"
  - "tool choices are outside the core"
---

### G.5:12 - Relations

**Builds on (normative):** `G.Core` (core invariants + linkage discipline).

**Uses (conceptual dependencies; cited via pins/ids):**

* Governing spec refs: `A.19 (CN‑Spec)`, `G.0 (CG‑Spec)`.
* Upstream object sets: `G.1 (CG‑Frame Card)`, `G.2 (SoTA Pack)`, `G.3 (CHR Pack)`, `G.4 (CAL Pack)`.
* Evidence & crossings: `G.6 (EvidenceGraph; PathId/PathSliceId)`, `G.7 (Bridge/CL calibration)`, `E.18/A.21 (CrossingBundle/GateChecks)`.
* Planning/enactment boundary: `A.15.3 (SlotFillingsPlanItem)` as the planned baseline anchor (cited, not redefined).
* Causal-use method dispatch: `C.28` when method selection involves causal effect, counterfactual comparison, causal fairness, causal policy, causal RL, or simulation-only causal-use claims.
* Optional method/generator extensions via `G.5:Ext.*`: `C.18`, `C.19`, `C.23`, plus any future extension-bearing patterns that add extra selector pins.
* Mathematical-lens adequacy: open `C.29` when a selector input depends on a load-bearing comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, QD archive descriptor, model-family label, or model-selection basis whose mathematical object, mapping mode, preserved/lost structure, or stop condition is not yet recoverable. `C.29` may return `NoMLANeeded`, `MLA.LensCandidateNote`, `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, or `NeighborGoverningLocusNote` for the stated selector use. It does not publish the selected set, selector policy, registry row, shortlist, ranked shortlist, or selector evidence pins; those stay in `G.5` and its governing refs.


**Publishes to:** `UTS` (family ids, selector policy records, and selected-set identities such as `ShortlistId` when one public result is emitted), `G.6` (audit citations), RSCR emission records (typed triggers + payload pins), and downstream packs via `G.10` shipping surfaces.

**Coordinates with:** `C.11` for local choice results, `C.19` for pool-policy records, `C.24` for enactment-facing next-move records, and the accepted Q-Front shortlist-family continuity line when the published selected-set label is one shortlist-family result.

