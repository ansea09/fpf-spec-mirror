---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Recovering What “Context” Means in Use"
section_id: "E.10.D1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__006_archetypal-grounding.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "E.10.D1 — Recovering What “Context” Means in Use"
  - "E.10.D1:5 — Archetypal Grounding"
line_start: 75822
line_end: 75833
dependencies:
  - "A.1.1"
  - "A.2.6"
  - "C.30"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "F.0.1"
  - "F.17"
  - "F.19"
  - "F.9"
keywords:
  - "architecture"
  - "claim scope"
  - "context wording"
  - "environment"
  - "model use"
  - "positive wording repair"
  - "source-local meaning"
  - "viewpoint"
  - "working situation"
---

### E.10.D1:5 - Archetypal Grounding

**Tell.** Recover the distinction that changes the action; do not model *context* itself.

**Show — source-local meaning.** A draft says, “In the maintenance context, *service* includes scheduled inspection.” The author finds an existing `F.0.1` result for the current `MaintenanceGuide-2026` edition: its exact F.17 cell says that *service* includes scheduled inspection, and its `LocalSenseBasisRelation` names the supporting claim episteme. That result is adequate for this sentence, so the author reuses it and writes, “In `MaintenanceGuide-2026`, *service* includes scheduled inspection,” with a citation to the cell. If the source-local meaning were still unclear, the author would apply `F.0.1` first. `F.1`, `F.9`, and `F.0.2` remain closed unless source selection, a cross-local relation, or comparison of several source ontologies becomes a live question.

**Show — model-use decision.** A change note says, “The controller change stays inside the press-control context.” If the decision asks only whether `PressControlModel-5` applies to `Press-3` within the stated claim scope, the engineer states that `ModelApplicabilityRelation` and stops. If release review depends jointly on model applicability, actual assigned-Work use, fixed-content coherence, applied constraints, and one selection-use frame, the engineer selects their A.1.1 `BoundedModelUseStructure`. The word *context* does not decide between those branches.

**Show — claim boundary.** A review says, “The comparison is valid in this context.” The repaired claim names the compared bearers, comparison scheme, `U.ClaimScope`, member slices, qualification window, evidence basis, and intended use. If those values already make the claim interpretable, no additional formal object is introduced.

**Ordinary non-use.** A source quotation says, “Context mapping is collaborative.” If the current claim is only that the source uses this phrase, keep the quotation and cite the source. Open A.1.1, F.9, or another branch only when the receiving text relies on a model-use structure, semantic relation, or other recovered content.

