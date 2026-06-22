---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:2"
section_title: "Kind and Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__003_kind-and-boundary.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:2 — Kind and Boundary"
line_start: 2659
line_end: 2691
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:2 - Kind and Boundary

`U.Capability` is a system-side ability claim.

```text
Capability:
  CapabilityHolderRef: U.System
  WorkFamilyOrResultClassRef:
  CapabilityEnvelope:
  CapabilityMeasureSet:
  QualificationWindow:
  EvidenceOrSourceUseRefs:
  CapabilityCurrentnessPredicate:
```

**CapabilityHolderRef.** The holder is a `U.System`: a physical system, cyber system, socio-technical system, organization, team, composite cell, software service as deployed system, or other acting holon admitted as system for the claim. A role assignment, method, method description, work record, episteme, publication, standard, or dashboard is not the capability holder merely because it appears in the sentence.

**WorkFamilyOrResultClassRef.** The ability is about a class of work results or a method family the holder can enact. It may refer to a `U.Method`, `U.MethodDescription`, method family, result class, or work family, but the reference does not turn the method or description into the holder.

**CapabilityEnvelope.** The envelope states the bounded conditions under which the ability is claimed: input range, environment, resources, configuration, system version, calibration state, staffing composition, access constraints, safety limits, or other current conditions.

**CapabilityMeasureSet.** The measures state the achieved or required bounds with units, scales, tolerances, success predicates, reliability, throughput, latency, precision, defect rate, or other characteristics.

**QualificationWindow.** Capability is stable enough to plan with but not timeless. A claim may depend on software version, calibration horizon, team training state, wear, operating season, regulatory state, or other temporal currentness relation.

**EvidenceOrSourceUseRefs.** Evidence, tests, certifications, prior work summaries, simulations, audit records, standards, and model results can justify a capability claim through direct evidence or source-use relations. They do not become the capability.

**CapabilityCurrentnessPredicate.** The claim states what keeps the ability current and what lowers or reopens it.

**Neighboring-term boundary.** When a neighboring pattern uses `U.WorkScope`, recover the set-valued condition part of `CapabilityEnvelope`: the inputs, environment, resources, configuration, and assumptions against which an intended work slice is checked. When it uses `U.WorkMeasures`, recover `CapabilityMeasureSet`. `JobSlice` names the intended work slice for a work-admission check. `QualificationWindow` names the temporal currentness relation for the capability claim. These are neighboring governed terms, not substitute names for `U.Capability`.



