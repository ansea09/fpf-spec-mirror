---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__007_archetypal-grounding.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:5 — Archetypal Grounding"
line_start: 28063
line_end: 28085
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

Start with the controller: “Thermostat_Model_T800 holds T800-home-heating-assignment as HomeHeatingController for household-temperature control.” In this constructed case, Thermostat_Model_T800 identifies one installed unit, admitted as a System, in House-H1 from 08:00 to 12:00 on Day-D. The local HomeHeatingController criterion is the ability to read the household temperature and selected set-point, command heating below the set-point and stop heating at or above it. The stipulated device behavior satisfies that criterion at the selected 21 °C set-point. The directly declared HomeHeatingAssignment species assigns a qualifying System to that kind when the household controller designation and enabled control connection obtain; both hold for T800 in that household and window.

The core result is that this System qualifies for HomeHeatingController and holds the obtaining assignment for the stated use. No Grade or autonomy measurement is needed for that result. If the household withdraws the designation while the device retains its capabilities, the assignment ceases under its rule; classification may remain true, and the precise agency claim must change. The table gives further schematic variations for individual and collective Systems, then a knowledge-artifact contrast. Its local kind names and profile/Grade assumptions are illustrative.

| Archetype | Holder (`U.System`) | Illustrative local agential system-role kind | Distinct obtaining assignment occurrence | Agency-characteristic profile sketch (illustrative assumptions) | Illustrative Agency Grade |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Simple Controller** | `Thermostat_Model_T800` | `HomeHeatingController` | `T800-home-heating-assignment` assigns `Thermostat_Model_T800` to `HomeHeatingController` for household-temperature control. | `BMC`: High (assumed).   `PH`: Zero (no prediction).   `MP`: Zero (fixed logic).   `PER`: Very High.   `OC`: Low (single set-point). | **Grade 1 (Reactive)** |
| **Advanced Controller** | `PredictiveCruiseControl_v3` | `VehicleDynamicsController` | `PCC-v3-vehicle-dynamics-assignment` assigns `PredictiveCruiseControl_v3` to `VehicleDynamicsController` for the driving situation supplied by the working case. | `BMC`: High.   `PH`: High (predicts traffic flow).   `MP`: Zero (fixed model).   `PER`: High.   `OC`: Medium (optimization). | **Grade 2 (Predictive)** |
| **Learning System** | `SelfCalibratingSensorArray` | `IndustrialProcessAdaptiveController` | `sensor-array-process-adaptation-assignment` assigns `SelfCalibratingSensorArray` to `IndustrialProcessAdaptiveController` for the calibration task family and window supplied by the working case. | `BMC`: High.   `PH`: High.   `MP`: Medium (assumed).   `PER`: High.   `OC`: Medium. | **Grade 3 (Adaptive)** |
| **Collective acting holder** | `DevOpsTeam_Phoenix` (a collective `U.System`) | `ProjectPhoenixDeliveryCoordinator` | `phoenix-team-delivery-assignment` assigns the collective System `DevOpsTeam_Phoenix` to `ProjectPhoenixDeliveryCoordinator` for the project work being claimed. | `BMC`: High (assumed).   `PH`: High (release planning).   `MP`: High (assumed).   `PER`: Medium-High.   `OC`: High (abstract business goals). | **Grade 4 (Reflective/Strategic)** |
| **Knowledge artifact** | No acting holder. `ISO_26262_Standard.pdf` is a file carrier; the selected standard edition and any exact claim episteme made available through it remain distinct. | **N/A** | **N/A**: neither the carrier nor an episteme is a `U.System`, so neither can receive an agential system-role assignment. | N/A | **N/A — no System holder or agency-characteristic profile** |

The profile values above are illustrative assumptions, not measured results. The case explanations support narrower statements:

- The thermostat “maintains temperature” in the household-control use. That does not establish the thermostat’s own structural and functional integrity under perturbation; `BMC: High` remains an assumption.
- “Learns drift” leaves the sensor’s model/parameter-update versus capability-acquisition meaning unspecified. `MP: Medium` does not supply that missing account.
- The team’s retrospectives name an activity, not a measured rate of internal-model update. `MP: High` remains an assumption; E.10.LRN keeps model change and capability acquisition separate.

**Key takeaway from grounding:**
The same ontology works for a thermostat, a predictive controller, a learning System, and a collective System: classification by a local kind and an obtaining assignment are both stated, while scope, situation, Work, evidence, profile, and grade remain separate. An exact ISO claim episteme may be cited in an A.10 evidence-provenance account or a B.3 reliance claim; any direct relation relied on by that account or claim must actually obtain under its own defining rule. Its file carrier merely bears a publication form.

