---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:10"
section_title: "Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__011_anti-patterns-and-repairs.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:10 — Anti-Patterns and Repairs"
line_start: 3802
line_end: 3817
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:10 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| System-role-kind-as-capability | “The inspector role can detect this defect.” | Treat bare *role* through E.10.ROLE; retain the exact local system-role kind and any independently obtaining assignment, then state capability for the holder System only when the bounded capability instance and current support justify it. |
| Assignment-as-capability | "Assigned, therefore able." | Use A.2.1 for assignment and A.2.2 for the holder-dependent capability instance. |
| Method-description-as-capability | "The procedure has capability" or "the solver has the algorithm, therefore this file is a method description." | Keep capability with the holder system. Treat procedure or algorithm wording as a cue to one candidate episteme only when that is the actual object; admit it as `U.MethodDescription` through A.3.2 only after its exact `EntityOfConcern` is an admitted Method and a substantive claim says how that Method is done. |
| Work-as-capability | "We did it once, so we can." | Keep the work occurrence; add a separate capability instance only when envelope, measures, and currentness are justified. |
| Promise-as-capability | "The SLA is our capability." | Use promise content or commitment for what is offered; capability is the internal measured ability that makes the promise credible. |
| Episteme-as-holder | "The report has assessment capability." | Use evidence, source, status, or assessment relation for the episteme; capability holder remains a system. |
| Unbounded capability | "The tool can machine titanium." | Add material grade, tolerances, feed range, environment, version, qualification window, and measurement evidence. |
| Capability threshold in system-role-kind name | `HighPrecisionWelderSystemRole` hides a measured threshold. | Keep the system-role-kind name free of the threshold; put precision in the Method-side admission or fit condition and the holder capability instance. |
| Characteristic-as-capability | "Low latency is a capability." | Use `U.Characteristic` with declared scale for latency; add `U.Capability` only when a named holder can produce a result class within an envelope that includes the latency measure. |
| Q-Bundle-as-capability | "Resilience is our capability." | Use `C.25` for the composite quality family; cite a capability only when a currentness assessment supports reliance on a holder-dependent capability instance and a fit predicate tests the relevant bundle slot. |
| Architecture-row-as-capability | "Maintainability row gives capability." | Use `C.32.ACS` for the architecture-characteristic criteria row; it may constrain a capability-fit condition but is not `U.Capability`. |

