---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__008_conformance-checklist.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:7 — Conformance Checklist"
line_start: 21818
line_end: 21853
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

### A.6.7:7 - Conformance Checklist

A `MechSuiteDescription` is conformant iff all applicable items hold:

**CC‑A.6.7‑1 (Correct level).** The suite’s `mechanisms` enumerate **distinct** `U.Mechanism` members. The suite is not encoded as `MechFamilyDescription`.

**CC‑A.6.7‑2 (Description token, not `U.*`).** The suite token is a Description token and MUST NOT be introduced under `U.*`. Its name ends with `…Description`.

**CC‑A.6.7‑3 (No execution semantics).** The suite MUST NOT define mechanism blocks (`OperationAlgebra`, `LawSet`, etc.) and MUST NOT be used as a mechanism node.

**CC‑A.6.7‑4 (No gate decisions).** The suite MUST NOT define `GateDecision`, MUST NOT publish `DecisionLog`, and MUST preserve gate/mechanism separation.

**CC‑A.6.7‑5 (Spec pins, not duplication).** If the suite is admissibility-gated for numeric comparison/aggregation/scoring, it MUST require `CG-Spec` citation pins (and SHOULD require `CN-Spec` pins where applicable). It MUST NOT duplicate spec content as “local CG-Spec”.

**CC‑A.6.7‑5a (CN+CG pins for admissibility-gated characterization).** If the suite is admissibility-gated for characterization, it MUST require both `CNSpecRef` and `CGSpecRef` as pins (references), consistent with A.6.7:4.3.

**CC‑A.6.7‑6 (Transport discipline preserved).** The suite MUST NOT introduce transport exceptions. An actual semantic crossing must recover its obtaining Bridge and bounded use under its direct rule, with any applicable penalties routed to `R/R_eff` only. Entity, scheme, plane or notation changes alone establish no Bridge.

**CC‑A.6.7‑7 (Tri-state guard discipline when used).** If the suite declares admissibility/eligibility semantics, it MUST use `GuardDecision := {pass|degrade|abstain}` and MUST NOT coerce unknown to pass.

**CC‑A.6.7‑8 (No thresholds in core).** The suite MUST NOT publish acceptance thresholds or “passing scores”. Thresholds must remain in acceptance clauses / task signatures / gate profiles.

**CC‑A.6.7‑9 (Crossing visibility anchors).** If suite use consumes an actual semantic crossing or an independently governed E.18 crossing/A.21 gate, require only that claim’s applicable visibility and audit anchors, including Bridge, CL, policy, UTS or Path pins when its direct rule requires them. A changed edition alone creates none of those objects; keep the exact changed edition pin without manufacturing a crossing.

**CC‑A.6.7‑10 (Suite id present).** The suite MUST declare `mech_suite_id: MechSuiteId` so that downstream planning/audit can cite it stably.

**CC‑A.6.7‑11 (Independent correspondence conditions).** A claimed kind correspondence MUST satisfy C.3.3 and retain the calibration and use conditions actually required there. When the use also relies on an F.9 semantic correspondence, establish that Bridge independently and retain both channels' applicable policies and penalties. A new EntityOfConcern of the same kind or a plane-only change creates neither correspondence by itself.

**CC‑A.6.7‑12 (Implementation export hygiene when cited).** If the suite cites realizations/implementations, the citations MUST preserve export/import discipline (LOG/CHR: no Γ export; CAL: exactly one Γ; imports acyclic).

**CC‑A.6.7‑13 (No Pack conflation).** The suite MUST NOT be introduced, named, or used as a publication/shipping `Pack`.

**CC‑A.6.7‑14 (Protocol closure & explicitness).** Each step resolves to one member declaration edition and one operation designator in that declaration (WF‑MS‑2). The operation's argument, result, law and admission meanings are recoverable. No unresolved edition choice, implicit operation or implicit crossing can supply that resolution.

**CC‑A.6.7‑15 (P2W split preserved when applicable).** If the suite requires a planned-baseline pin, that baseline MUST be a `WorkPlanning` plan item and MUST NOT contain launch values or `FinalizeLaunchValues` witnesses; such witnesses remain `U.WorkEnactment`-only.

