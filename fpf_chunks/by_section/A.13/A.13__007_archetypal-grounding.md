---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__007_archetypal-grounding.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:5 — Archetypal Grounding"
line_start: 28224
line_end: 28268
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

#### A.13:5.1 - Construct a measured profile for a calibration use

Consider one installed `SensorArray-S7`, admitted as a System. This constructed case supplies its local `IndustrialProcessAdaptiveController` criterion and obtaining assignment: S7 detects deviation from a reference signal, selects a permitted offset update or stops calibration on an invalid input, and has the designation and enabled connection for that control. Those premises establish the agency core. The additional question is what its bench profile shows and whether calibration reaches residual error at most 0.1 °C within three minutes.

The measurement definitions and observations below are stipulated case inputs. The internal sensor model is `z = r + b`, where z is the raw indication, r the reference value and b the estimated offset. The reference relation establishes a constant raw offset `z - r = 0.6 °C` for this test. The admitted `OffsetUpdateMethod-3` reads that reference, checks the allowed update and commits the new offset once per minute:

`b_next = b + 0.5 * (z - r - b)`.

Starting at `b = 0`, the three committed offsets are 0.3, 0.45 and 0.525 °C. The measurement basis bounds the total uncertainty in interpreting residual error by ±0.02 °C. After the third update, that residual therefore lies in `[0.055, 0.095] °C`, satisfying the 0.1 °C target. The following profile keeps the other supported characteristics separately interpretable.

| Result | Basis and use boundary |
| --- | --- |
| BMC: integrity maintained in four of four specified perturbation cases | Integrity I requires an intact executable, one valid configuration and restoration of both channels within five seconds. The supplied test histories establish I after each one-second interruption of power, one channel or communication, and after an interrupted parameter write. Recovery is automatic after the interruption ends. This is coverage of those four cases. |
| PH: 30 seconds temporal depth | S7's internal forecasting function produces `z_hat(t+h) = r(t) + b(t)` for `0 <= h <= 30 s`, holding the current reference and offset over that prediction interval. The implementation supplies that model extent. Prediction accuracy is a separate question. |
| MP: 0.175 °C per minute over the three updates | The declared measure is total variation of the stored offset divided by elapsed time. All three updates have the same sign, so both total variation and net change equal 0.525 °C; divide by three minutes. Parameter readback resolution is 0.01 °C. |
| PER: 0.95 for uniform selection from the stated finite population | The population is 20 fully examined scripted bench episodes with valid inputs. Successful execution means completing the required reads, checks and commits of OffsetUpdateMethod-3. Nineteen histories meet it; one records a failed commit. Under uniform selection of one of these episodes, the probability is 19/20. A production-population estimate would need its own sampling and inference basis. |
| OC: one independently adjustable target pursued in this case | The local complexity criterion counts independently adjustable target quantities. Here the target quantity is residual temperature error; the three-minute budget and offset-update bounds are fixed conditions of this comparison. The calculation establishes pursuit of this objective in the stated regime. |

For the C.22.1 adaptation question, the first successful minute checkpoint is at 180 seconds, with a budget of three reference/update cycles and the stated initial model. This threshold result uses the residual-error bound; MP reports the parameter-change rate. For a local didactic convention, assign Grade 3 within this controller family when BMC covers the named perturbation set, temporal PH is positive and error-driven MP is distinguishable from zero at the declared resolution. Leave other profiles unclassified. S7 receives that label; PER and OC remain explicit profile results outside what this partial mapping summarizes.

**Changed receiving condition.** Tighten the residual-error target to 0.05 °C while keeping the three-update budget. The profile values and local Grade remain supported, but the calibration result fails the new target: even the lower residual bound after three updates is 0.055 °C. Under the same model, five updates would give an upper residual bound of 0.03875 °C. The practitioner can compare a larger adaptation budget with another update Method or a better measurement basis. The changed tolerance reopens the adaptation decision.

