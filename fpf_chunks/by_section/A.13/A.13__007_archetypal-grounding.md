---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__007_archetypal-grounding.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:5 — Archetypal Grounding"
line_start: 24232
line_end: 24254
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "C.16"
  - "E.16"
  - "F.6"
keywords:
  - "autonomy grading"
  - "classification"
  - "conditional characteristic profile"
  - "evidence-backed core"
  - "exact System"
  - "local agential system-role kind and criterion"
  - "obtaining assignment"
  - "scope"
  - "window"
  - "working situation"
---

### A.13:5 - Archetypal Grounding

Start with the simple controller: “Thermostat_Model_T800 holds T800-home-heating-assignment as HomeHeatingController for household-temperature control.” The holder, local kind and assignment are different objects. For this illustration, System admission, qualification under the local kind’s criterion and an obtaining assignment are premises. The working case must supply that criterion, the supporting facts and any needed scope, situation or window; the names alone supply none of them.

The table gives schematic variations for individual and collective Systems, then a knowledge-artifact contrast. Profile and Grade remain separate claims. These local kind names are examples, not a universal `AgentialRole` vocabulary.

| Archetype | Holder (`U.System`) | Illustrative local agential system-role kind | Distinct obtaining assignment occurrence | Agency-characteristic profile sketch (illustrative assumptions) | Resulting Agency Grade |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Simple Controller** | `Thermostat_Model_T800` | `HomeHeatingController` | `T800-home-heating-assignment` assigns `Thermostat_Model_T800` to `HomeHeatingController` for household-temperature control. | `BMC`: High (assumed). <br> `PH`: Zero (no prediction). <br> `MP`: Zero (fixed logic). <br> `PER`: Very High. <br> `OC`: Low (single set-point). | **Grade 1 (Reactive)** |
| **Advanced Controller** | `PredictiveCruiseControl_v3` | `VehicleDynamicsController` | `PCC-v3-vehicle-dynamics-assignment` assigns `PredictiveCruiseControl_v3` to `VehicleDynamicsController` for the driving situation supplied by the working case. | `BMC`: High. <br> `PH`: High (predicts traffic flow). <br> `MP`: Zero (fixed model). <br> `PER`: High. <br> `OC`: Medium (optimization). | **Grade 2 (Predictive)** |
| **Learning System** | `SelfCalibratingSensorArray` | `IndustrialProcessAdaptiveController` | `sensor-array-process-adaptation-assignment` assigns `SelfCalibratingSensorArray` to `IndustrialProcessAdaptiveController` for the calibration task family and window supplied by the working case. | `BMC`: High. <br> `PH`: High. <br> `MP`: Medium (assumed). <br> `PER`: High. <br> `OC`: Medium. | **Grade 3 (Adaptive)** |
| **Collective acting holder** | `DevOpsTeam_Phoenix` (a collective `U.System`) | `ProjectPhoenixDeliveryCoordinator` | `phoenix-team-delivery-assignment` assigns the collective System `DevOpsTeam_Phoenix` to `ProjectPhoenixDeliveryCoordinator` for the project work being claimed. | `BMC`: High (maintains delivery capacity). <br> `PH`: High (release planning). <br> `MP`: High (assumed). <br> `PER`: Medium-High. <br> `OC`: High (abstract business goals). | **Grade 4 (Reflective/Strategic)** |
| **Knowledge artifact** | No acting holder. `ISO_26262_Standard.pdf` is a file carrier; the selected standard edition and any exact claim episteme made available through it remain distinct. | **N/A** | **N/A**: neither the carrier nor an episteme is a `U.System`, so neither can receive an agential system-role assignment. | N/A | **Grade 0 (Non-Agential)** |

The profile values above are illustrative assumptions, not measured results. The case explanations support narrower statements:

- The thermostat “maintains temperature” in the household-control use. That does not establish the thermostat’s own structural and functional integrity under perturbation; `BMC: High` remains an assumption.
- “Learns drift” leaves the sensor’s model/parameter-update versus capability-acquisition meaning unspecified. `MP: Medium` does not supply that missing account.
- The team’s retrospectives name an activity, not a measured rate of internal-model update. `MP: High` remains an assumption; E.10.LRN keeps model change and capability acquisition separate.

**Key takeaway from grounding:**
The same ontology works for a thermostat, a predictive controller, a learning System, and a collective System: classification by a local kind and an obtaining assignment are both stated, while scope, situation, Work, evidence, profile, and grade remain separate. An exact ISO claim episteme may be cited in an A.10 evidence-provenance account or a B.3 reliance claim; any direct relation relied on by that account or claim must actually obtain under its own defining rule. Its file carrier merely bears a publication form.

