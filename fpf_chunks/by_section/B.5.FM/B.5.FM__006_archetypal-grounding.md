---
chunk_kind: "child"
pattern_id: "B.5.FM"
pattern_title: "Construct a First Model for the Working Question"
section_id: "B.5.FM:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.FM/B.5.FM__006_archetypal-grounding.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "B.5.FM — Construct a First Model for the Working Question"
  - "B.5.FM:5 — Archetypal Grounding"
line_start: 45063
line_end: 45128
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.4"
  - "B.5.MPC.R"
  - "B.5.RR"
  - "C.16"
  - "C.29"
keywords:
---

### B.5.FM:5 - Archetypal Grounding

These constructed cases expose different model choices. Their calculations establish conditional consequences; no apparatus test is reported.

#### B.5.FM:5.1 - Choose the heat path before commissioning a calculation

An engineer asks whether a stronger external fan can bring an overheating component below 65 °C. Inspection finds the component attached to a metal case through a pad; the fan blows over the outside of the case.

Trace the proposed path from component to case and then to the surrounding air. Keep the component, the case at its attachment and the air distinguishable: their temperatures can differ, and the fan acts on one part of that path.

Try a steady account with constant component heating, all generated heat passing through the pad, and an unchanged linear conductance between component and case. Carrying the same heat per second then requires the same temperature difference across that path. Treat outward case-to-air transfer as driven by temperature difference. A steady case receiving positive heat must remain warmer than the air.

Use supplied steady readings of 80 °C at the component, 25 °C at the case attachment and 20 °C in the air. The component-to-case difference is 55 °C. Even ideal external cooling of the case to the air temperature leaves the component at 75 °C under these assumptions. The fan-only proposal cannot reach 65 °C in this model.

The result directs work toward the component-to-case contact, another heat path or reduced heating. Direct airflow onto the component would change the assumed path; temperature-dependent heating or conductance would change the fixed-difference argument. Measurement uncertainty matters to the real-device conclusion.

A useful next request is: “Can this component stay below 65 °C after changing its contact to the case, and which observations distinguish the relevant heat paths?” The model supplies that request before a detailed equation set is commissioned.

#### B.5.FM:5.2 - Include the air when modeling liquid discharge

Consider a rigid vessel with a liquid outlet near its bottom and trapped air above the liquid. The question is whether enlarging the outlet will allow most of the liquid to drain. A model based only on liquid height can miss what changes when liquid leaves.

For a first conditional account, assume that no air enters and the liquid is incompressible. Treat the trapped air as an ideal gas at constant temperature and fixed amount. Consider slow flow whose inertia is negligible and whose motion is dissipated by resistance at the outlet. Include the gas volume and absolute pressure, the liquid height above the outlet and the outside pressure. Liquid leaving increases gas volume and lowers gas pressure.

At the no-flow equilibrium, the internal pressure at the outlet equals the outside pressure. For the following rough calculation take liquid density as 1,000 kg/m³ and gravitational acceleration as 10 m/s². Initial liquid height is 20 cm, trapped gas volume is 100 cm³, vessel cross-section is 100 cm² and initial gas and outside pressures are both 100 kPa.

Let q be the discharged volume in cm³. The gas occupies 100+q cm³; liquid height is 20−q/100 cm. The isothermal gas relation and hydrostatic head give the equilibrium equation:

```text
10000/(100+q) + 0.1*(20−q/100) = 100   [kPa]
```

The positive solution is about 2.039 cm³, with gas pressure about 98.002 kPa and liquid height about 19.980 cm. In this slow-flow account, the discharge approaches a stop after a very small volume. Changing outlet size changes resistance and the approach to equilibrium; this same equilibrium balance applies while air entry and inertial effects remain negligible.

Allowing ambient air to reach the gas space changes the model: gas pressure can remain near outside pressure as liquid leaves. Air entering through the outlet, gas-temperature change, vessel deformation or appreciable capillary pressure requires another account. The immediate useful result is the distinction between an outlet-flow restriction and a gas-replacement restriction. Investigate the air path before treating outlet enlargement as the answer.

#### B.5.FM:5.3 - Construct classes that permit a counting inference

We need counts of binary strings at several lengths under a rule that forbids consecutive 1s. Use length four as a small case. The question supplies symbols and a restriction, but no recurrence.

Start with short valid prefixes and examine their allowed next symbols. A prefix ending in 1 may receive only 0. A prefix ending in 0 may receive either symbol; the empty prefix has the same two permissions. Group prefixes by those extension permissions.

Let r_n count valid length-n prefixes that are empty or end in 0; let b_n count those ending in 1. Every valid prefix can receive 0, while only the r_n prefixes can receive 1:

```text
r_0 = 1, b_0 = 0
r_(n+1) = r_n + b_n
b_(n+1) = r_n
```

The pairs for lengths 1 through 4 are (1,1), (2,1), (3,2), (5,3). There are eight valid strings of length four.

The inference works because each extension produces a distinct string, deleting its final symbol recovers its unique predecessor, and the two resulting classes exhaust the permitted cases. The total alone does not tell how many prefixes permit appending 1; keeping the two classes makes that operation possible.

If the restriction changes to “no three consecutive 1s”, the same grouping loses a needed distinction. Separate prefixes with zero, one or two trailing 1s and reconstruct the permitted transitions. This change identifies what the state must retain; the subsequent recurrence or program is a further computational contribution.

#### B.5.FM:5.4 - Find the limiting relation in a workshop plan

Twelve people have accepted a 60-minute workshop. There are twelve seats and one instructor. The proposed arrangement gives each person a four-minute attempt observed by that instructor, then two minutes of the instructor's feedback before the next attempt begins. The initial plan lists attendance and materials.

Use the relation between attempted action, observation and feedback to ask whether the intended practice can occur in the session. The sequential arrangement requires `12 * (4 + 2) = 72` minutes before any introduction. The next question is which arrangement can supply the intended practice and feedback within the available time. Reducing attendance, increasing duration or changing the learning arrangement have different consequences. Merely pairing learners supplies the required feedback only if they can provide that contribution.

Now suppose twelve independent stations already provide the required task-specific feedback and can be used concurrently. The serial calculation no longer describes the work. Use the concurrent duration and the remaining session activities to decide whether the arrangement fits; this reasoning does not require another instructor. If the intended event is instead a demonstration with no individual practice, the individual-feedback relation does not impose that practice on it. Clarify the event's purpose before treating this scheme as applicable.

The same question-forming move can use a measurement scheme: a shared column label, such as temperature, leaves the relevant quantity, observing conditions and aggregation to be recovered before combining records. If the existing documentation already establishes their suitability, use that answer. The scheme supplies a question, not a compulsory new measurement.

