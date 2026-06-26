---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__006_archetypal-grounding.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:5 — Archetypal Grounding"
line_start: 22288
line_end: 22325
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.7"
  - "B.3"
  - "C.27.TA"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.20"
  - "E.24"
  - "G.11"
  - "G.6"
  - "U.RelationSlotDiscipline"
  - "U.Work"
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

### A.15.3:5 - Archetypal Grounding

#### A.15.3:5.1 - CHR suite planned baseline

**Tell.** A team plans characterization work over a CG-frame using a CHR mechanism suite. The suite description declares SlotKinds for normalization method, indicator policy, comparator spec, and selector policy.

**Show without A.15.3.** The plan says "use the latest CG-Spec and current best comparator." Later the comparator set changes. Later audit readers cannot tell whether the work used the intended comparator or a later one.

**Show with A.15.3.** The `SlotFillingsPlanItem` targets the CHR suite description edition, names the bounded context and time selector, and writes rows:

```text
planned_fillings:
  - slot_kind: NormalizationMethodSlot
    planned_filler: ByRef(UNMDescriptionRef:2026-06)
    edition_pin: 2026-06
  - slot_kind: ComparatorSpecSlot
    planned_filler: ByRef(ComparatorSpecRef:CG42-v3)
    edition_pin: v3
  - slot_kind: SelectorPolicySlot
    planned_filler: ByValue(SetReturningSelectionPolicy)
```

If the later work uses `ComparatorSpecRef:CG42-v4`, the work record states variance or crossing witness. The PlanItem remains the planned baseline.

#### A.15.3:5.2 - Archive and QD selection

**Tell.** A project plans to return an archive rather than one winner. Descriptor definitions and distance functions are edition-sensitive.

**Show without A.15.3.** The published archive card lists descriptors and distances, but the original planned descriptor edition is gone. The card becomes a mutable publication face rather than a planned-baseline relation.

**Show with A.15.3.** The PlanItem rows pin descriptor description refs, distance-definition refs, and time rule. The published card is a projection of those rows. If the archive generation later changes descriptors, performed work and result records cite the baseline and state the variance.

#### A.15.3:5.3 - Hardware acceptance fixture

**Tell.** A hardware team plans acceptance work for a fixture. The slot-bearing description is an acceptance-method description with slots for reference plane, measurement method, calibration source, and acceptance threshold.

**Show with A.15.3.** The planned baseline pins the reference-plane description, calibration source ref, and threshold edition. The performed acceptance work later records actual measurements and substitutions. The PlanItem does not become the measurement evidence.

