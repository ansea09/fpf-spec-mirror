---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:5"
section_title: "Archetypal Grounding (Tell–Show–Show; System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__006_archetypal-grounding-tell-show-show-system-episteme.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:5 — Archetypal Grounding (Tell–Show–Show; System / Episteme)"
line_start: 20942
line_end: 20973
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.TGA"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:5 - Archetypal Grounding (Tell–Show–Show; System / Episteme)

#### A.15.3:5.1 - Archetype 1: CHR suite planned baseline for lawful characterization

**Tell.** A team plans a characterization workflow over a CG-frame that uses a CHR mechanism suite. The suite requires an explicit planned baseline reference.

**Show (failure without `SlotFillingsPlanItem`).** The “plan” is implicit: it says “use the latest CG-Spec and the current best comparator; compute scores and launch” without an explicit `Γ_time`, without edition pins, and without a stable mapping from SlotKinds to chosen fillers. Subsequent review cannot distinguish: (i) what was planned, (ii) what was executed, and (iii) what changed via a crossing or edition-key shift.

**Show (repair with `SlotFillingsPlanItem`).** A conformant `SlotFillingsPlanItem`:
* targets `CHRMechanismSuiteDescriptionRef` as the slot-bearing description (and pins its edition if used as a reproducibility baseline),
* pins `CNSpecRef` and `CGSpecRef` (editions pinned where reproducibility requires),
* pins a `ScoringMethodDescriptionRef.edition` (e.g., a monotone scoring family) and, when needed, a set-valued method family (e.g., conformal-style set predictions),
* declares `Γ_time_selector = point(t0)` (no implicit “latest”),
* declares `expected_usm_guard_pins = {USM.CompareGuard, USM.LaunchGuard}`,
* includes evidence pin refs that will be populated or used in Work enactment.

The resulting Work enactment cites this PlanItem as the planned baseline; any substitution (e.g., retargeting a method description ref) appears as Work variance (and, when relevant, as a crossing witness), not as a retroactive plan rewrite.

#### A.15.3:5.2 - Archetype 2: Archive and QD selection with edition-sensitive descriptors

**Tell.** A workflow plans to return an **archive** (quality-diversity style) rather than a single winner. The selection pipeline depends on descriptor maps and distance definitions that are edition-sensitive.

**Show (failure without `SlotFillingsPlanItem`).** Descriptor-map and distance-definition drift is discovered only after the fact: an "archive" is produced, but practitioners or auditors cannot reconstruct which descriptor edition and distance definition were assumed at planning time, and the published view or card becomes the de facto mutable canonical source.

**Show (repair with `SlotFillingsPlanItem`).** A conformant `SlotFillingsPlanItem`:
* targets an archive-selection kit or suite as `target_slot_bearing_description_ref`,
* pins `DescriptorMapDescriptionRef.edition` and `DistanceDefDescriptionRef.edition` (or their kit equivalents),
* states `expected_usm_guard_pins = {USM.CompareGuard}` (if no LaunchGate is expected yet),
* records expected crossing policy pins if descriptors are reused cross-context.

This prevents “silent” descriptor drift across iterations and makes Part G’s archive-related extensions composable rather than embedded in selector prose.

