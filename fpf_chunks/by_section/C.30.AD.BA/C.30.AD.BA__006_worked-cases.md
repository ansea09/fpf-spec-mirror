---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:3"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__006_worked-cases.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:3 — Worked Cases"
line_start: 59963
line_end: 59984
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "G.11"
keywords:
---

### C.30.AD.BA:3 - Worked Cases

#### C.30.AD.BA:3.1 - Hospital ventilation and fire compartmentation

A hospital renovation uses an IFC publication, a fire-compartment view, a ventilation flow view, an equipment register, an energy-use view, and live air-handling telemetry. The immediate architecture concern is whether the changed ventilation arrangement preserves smoke-control functions across compartment boundaries. A second intended use is a bounded comparison of air-handling energy consumption; it does not share the smoke-control verdict.

The engineer names the hospital facility as `builtAssetRef`, recovers the actual subject relations and exact fire-compartment, ventilation-flow, equipment-module, and control structures, and cites an obtaining `ArchitectureRelation` only if its C.30 predicate holds. Required or proposed content remains in a bounded architecture claim. Each used architecture description has its exact ClaimGraph, one EntityOfConcern, and effective reference scheme; each claimed structural view additionally has an exact viewpoint and independently obtaining E.17.0 conformance relation.

The IFC publication supplies a source-to-use path for the spatial and equipment descriptions while its representation, publication occurrence, form, and carrier stay separate. The telemetry episteme has a currentness boundary and can support separately governed operating-state claims; it is not itself the control structure, an architecture relation, an actual physical transformation, or architecture evaluation.

For the energy use, one current `C.16` measurement-result episteme attributes `112 kWh ± 4 kWh` electrical-energy consumption to air-handling unit `AHU-3` over a declared 24-hour commissioning window. It names the exact measurand, Characteristic, Scale and unit, method and model, calibration basis, dated measurement Work, time stance, and uncertainty. Its source-to-use path cites the meter telemetry and source edition; its `G.11` currentness condition limits use to the named sensor, calibration, model editions, and validity window and reopens that use when one changes. If the engineer claims that the control revision will reduce the daily consumption rate, the action-guiding temporal claim enters `C.27` with the intervention, window, resistance or cost, evidence or assumption relation, supported use, unsupported use, and reopen condition. If that same statement is used to say that the control revision causes the reduction, and causal support makes publication, choice, deployment, assurance, audit, benchmark, or support treatment admissible, `C.28` additionally governs the causal-use class, support basis, supported use, unsupported use, and verdict. `C.27` temporal adequacy does not establish a causal intervention effect, and `C.28` does not replace the `C.16` measurement result, `C.27` temporal claim, or `G.11` currentness boundary. `A.10` and `B.3` still govern material reliance and assurance. Neither the energy view nor the recent reading proves sustainability, smoke-control adequacy, or architecture adequacy.

An air-handling unit has a product-aspect designation and a location-aspect designation. Each designation use names its scheme, selected structure, designated entity, qualification window, and exact direct relation when one obtains. A bounded correspondence claim or obtaining correspondence relation lets the maintenance team retrieve both descriptions without making the product structure identical to the location structure.

The next architecture move is then concrete: evaluate the proposed flow and control structures against the smoke-control concern and carry the bounded energy-use comparison through its own characteristic and temporal owners. It is not “approve the BIM model.”

#### C.30.AD.BA:3.2 - Bridge inspection twin

A bridge operator combines an as-maintained geometry model, structural-member view, inspection history, strain telemetry, and a simulation view. The bridge remains the built asset across model editions. The structural-member and sensor-placement structures are selected explicitly; each description keeps exact C.2.1 identity and each claimed view exact E.17.0 conformance. Inspection and telemetry claims retain their evidence, grounding, source-use, and currentness relations. A revised simulation model retains the same C.2.1 episteme identity when its claim content, EntityOfConcern, and effective reference scheme are unchanged. Otherwise identify another episteme; assert an `EpistemeEditionRelation` only when its historical-continuation predicate obtains. Assess any declared lineage or continuity claims separately for the intended reuse.

When the operator compares an original design description with the as-maintained geometry, inspection history, and live telemetry, `designRunSeparationUse` cites the exact design-side description and design Work, the exact run-side descriptions and inspection or maintenance Work, their source-to-use and currentness refs, and any separately governed design-to-realization correspondence. `actualTransformationRefs` remains absent unless an exact repair or other physical change satisfies A.3.4. The architecture description can therefore support a decision to inspect or redesign a connection while retaining the route back to the geometry publication, measurement descriptions, and selected structures. It cannot treat a successful data-exchange check, recent sensor sample, simulation result, polished dashboard, or local design/run classification as proof that the bridge architecture is adequate or that design and realized objects are identical.

