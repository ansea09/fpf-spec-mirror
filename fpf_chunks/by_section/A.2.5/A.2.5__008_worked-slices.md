---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__008_worked-slices.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:5 — Worked Slices"
line_start: 4033
line_end: 4077
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:5 - Worked Slices

#### A.2.5:5.1 - Incident Commander

Context: `SRE_Prod_Cluster_EU_2026`.

Role: `IncidentCommanderRole`.

States:

- `OffDuty` - not in the on-call assignment window;
- `OnCall` - assignment window and contact source are current;
- `Authorized` - escalation decision source is current;
- `Ready` - on call, authorized, not conflicted, attention-pressure indicator below threshold;
- `RunningIncident` - currently performing incident-command work;
- `Blocked` - conflicting assignment or missing source.

`Ready` and `RunningIncident` are enactable states for incident-command work in this context. A work record for "Declare severity level" may cite `performedBy = Dana#IncidentCommanderRole:SRE_Prod_Cluster_EU_2026`, but the work claim is admitted only when a `StateAssertion` puts that assignment in `Ready` or `RunningIncident` for the declaration window.

#### A.2.5:5.2 - Thermometer Observer

Context: `Metrology_Thermo_2026`.

Role: `ThermometerObserverRole`.

States:

- `Unqualified` - no traceable calibration source;
- `Calibrated` - calibration source current;
- `Synchronized` - time relation within threshold;
- `InRange` - drift and environment predicates hold;
- `Measuring` - observation procedure is active;
- `Stale` - calibration or synchronization window expired;
- `Quarantined` - suspected contamination or bias.

`Measuring` is the only enactable state for the "record temperature" work claim. `Calibrated` and `Synchronized` are useful role states, but they do not by themselves admit observation work.

#### A.2.5:5.3 - Standard or Dataset With "Status Role" Source Wording

A source may say that a standard has an "approved role" or a dataset has an "evidence role." Do not make a `RoleStateRelation@BoundedContext` for the episteme unless a direct work-facing role is actually current. Usually the repair is:

- standard or requirement source: requirement-use, status-use, source-use, or publication-use relation;
- dataset or report: evidence-use, source-use, measurement, benchmark, freshness, or provenance relation;
- claim about the worker who approved, measured, verified, or published it: `U.Work` performed by a holder under `U.RoleAssignment`, with A.2.5 used only for that holder's role state.

