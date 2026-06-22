---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__018_relations.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:12 — Relations"
line_start: 85641
line_end: 85658
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
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:12 - Relations

**Builds on (normative):** `G.Core` (core invariants + linkage discipline).

**Uses (conceptual dependencies; cited via pins and ids):**

* Governing spec refs: `A.19 (CN‑Spec)`, `G.0 (CG‑Spec)`.
* Upstream object sets: `G.1 (CG‑Frame Card)`, `G.2 (SoTA Pack)`, `G.3 (CHR Pack)`, `G.4 (CAL Pack)`.
* Evidence and crossings: `G.6` (EvidenceGraph; `PathId` and `PathSliceId`), `G.7` (Bridge and CL calibration), `E.18` and `A.21` (CrossingBundle and GateChecks).
* Planning and enactment boundary: `A.15.3 (SlotFillingsPlanItem)` as the plannedBaselineRef (cited, not redefined).
* Causal-use method dispatch: `C.28` when method selection involves causal effect, counterfactual comparison, causal fairness, causal policy, causal RL, or simulation-only causal-use claims.
* Optional method or generator extensions through `G.5:Ext.*`: `C.18`, `C.19`, `C.23`, plus extension-bearing patterns admitted by a governing Part G relation when they add extra selector pins.
* Mathematical-lens use: apply `C.29` when a selector input depends on a claim-relevant comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, QD archive descriptor, model-family label, or model-selection basis whose mathematical object, mapping mode, preserved or lost structure, or stop condition is not yet recoverable. `C.29` may return no math-lens use, a lens-candidate note, a one-line note, a mini-card, a full card, or a note naming the direct governing pattern for the stated selector use. It does not publish the selected set, selector policy, registry row, shortlist, ranked shortlist, or selector evidence pins; those stay in `G.5` and its governing refs.

**Publishes to:** `UTS` (family ids, selector policy records, and selected-set identities such as `ShortlistId` when one public result is emitted), `G.6` (audit citations), RSCR emission records (typed triggers and payload pins), and downstream packs through `G.10` shipping publications.

**Coordinates with:** `C.11` for local choice results, `C.19` for pool-policy records, `C.24` for enactment-facing next-action records, and the accepted Q-Front shortlist-family continuity line when the published selected-set label is one shortlist-family result.

