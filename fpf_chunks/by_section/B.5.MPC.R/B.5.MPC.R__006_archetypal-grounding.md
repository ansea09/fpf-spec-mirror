---
chunk_kind: "child"
pattern_id: "B.5.MPC.R"
pattern_title: "Repair a Physical-Mathematical-Computational Connection"
section_id: "B.5.MPC.R:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC.R/B.5.MPC.R__006_archetypal-grounding.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "B.5.MPC.R — Repair a Physical-Mathematical-Computational Connection"
  - "B.5.MPC.R:5 — Archetypal Grounding"
line_start: 43486
line_end: 43561
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.16"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
keywords:
---

### B.5.MPC.R:5 - Archetypal Grounding

These are constructed cases under stated models. They demonstrate different repair locations and the contributions that follow from them.

#### B.5.MPC.R:5.1 - A robot receives a new deadline, then keeps moving during a pause

A robot must travel d=1 m along a straight guide. In the stipulated regime, constant speed obeys v=k*u, where u is a dimensionless command and k=0.2 m/s. The model initially idealizes starting and stopping as immediate. The available command range is 0<u<=0.8.

With u=0.5, the relation d=v*T gives T=d/(k*u)=10 s. The question then changes: find the command for T=5 s. Keep the relations but choose u as the unknown:

u=d/(k*T)=1/(0.2*5)=1.

The algebra supplies a value outside the available range. The corresponding lower bound on duration is T>=1/(0.2*0.8)=6.25 s. This answers the feasibility question before another controller is written. Changing the deadline or the available motion capability is now a meaningful choice.

Suppose the requester chooses T=8 s. The required command is u=0.625, giving v=0.125 m/s. A controller applies that command, counts eight seconds of active program execution and then issues stop.

During a diagnostic run, a debugger freezes the program and its timer for three seconds. In this example the output retains u=0.625 and the motor continues to run. The stop is therefore issued after eleven seconds of physical operation, giving d=0.125*11=1.375 m under the model.

The disagreement concerns execution timing. The equation and chosen command remain appropriate to eight seconds of motion. If the question concerns an uninterrupted run, observe that run under its intended timing. If such pauses can occur in the required operation, provide a stopping mechanism whose elapsed-time behavior survives the pause, or revise the control arrangement accordingly. Test its physical completion at the condition the use needs.

For example, suppose an independent timer can remove the motor command and continues to run while the controller is paused. Start it with the command and set it to remove the command after eight physical seconds. Under the example's immediate-start/stop model, motion then lasts eight seconds and covers 0.125*8=1 m, including a run with the three-second program pause. Compare the timer's actual behavior with those conditions before relying on that performance. If no such mechanism is available, the next contribution is a way to stop motion with that timing or a revised operating requirement.

A real stopping delay or speed transient would be another changed premise. Incorporate it when predicting final displacement; acknowledging stop does not measure that displacement. The example's next useful result is a duration bound or a repaired timing design with an identified performance question.

#### B.5.MPC.R:5.2 - A correct spectrum calculation answers an ambiguous physical question

A measurement uses uniformly spaced samples at f_s=100 samples/s. The earlier physical account admits a single sinusoidal signal with frequency below 50 Hz. A spectrum calculation returns a 10 Hz component, interpreted under that restriction.

The apparatus is changed and the admitted frequency range becomes 0 to 120 Hz. The same interpretation is now in question. For ideal samples of a unit-amplitude cosine at times n/100 seconds:

cos(2π*90*n/100)=cos(2π*10*n/100)

for every integer n. This follows because 90/100=1−10/100 and cosine is periodic and even. A 110 Hz cosine gives the same samples as well.

Consequently, the sampled sequence fits physical frequencies 10, 90 and 110 Hz in the new range. The spectrum calculation can remain correct for its input. Increasing its arithmetic precision or merely collecting more samples at the same times leaves this ambiguity.

To determine which frequency is present, change a contribution that distinguishes those cases. For the stipulated single-tone model, sampling at 300 samples/s places the whole admitted range below half the sampling rate. A three-second record of a 90 Hz signal then contains 270 cycles; the spectrum can return 90 Hz under the stated ideal timing and signal assumptions.

For a physical measurement, obtain the needed sampling and input-conditioning behavior from the instrument account. Frequencies outside the admitted band, timing error and an unsuitable analog input path can reopen the interpretation. A filter that removes the signal of interest changes the measurement question rather than recovering its frequency.

The repair is a changed acquisition and interpretation, with a recomputation on the new data. The receiving user can now distinguish a physical-frequency estimate from an unresolved alias. If the old record is all that is available, return the remaining alternatives instead of selecting one without further grounds.

#### B.5.MPC.R:5.3 - The voltmeter changes the circuit being inferred

An ideal 10 V source drives two 1 MΩ resistors in series. The wanted quantity is the midpoint voltage before a meter is connected. The divider relation gives 5 V.

A voltmeter with 1 MΩ input resistance is connected between the midpoint and the lower terminal. In the connected circuit it lies in parallel with the lower resistor, whose combined resistance becomes 0.5 MΩ. The same divider construction now gives:

V_mid=10*0.5/(1+0.5)=10/3 V.

The indicated value can agree with the connected-circuit model. Comparing it directly with the unloaded prediction had omitted the meter's interaction.

One repair is inferential: with these resistor, source and meter models, recover the unloaded value from the model, keeping its conditional status. Another is experimental: choose a measurement arrangement whose loading is small enough for the wanted use and account for its remaining effect. Repeating the same connection alone preserves the load.

The result tells the practitioner which voltage was observed and how the wanted voltage can be obtained. A different observed value may require revisiting the assumed source, resistor or instrument behavior through their subject methods.

#### B.5.MPC.R:5.4 - A motion command changes its unit and starting point

In C.29.3's robot case, the effective wheel radius is 0.05 m, ten motor revolutions turn the wheel once, and the interface counts 1,000 increments per motor revolution. A two-metre displacement requires a total of 63,662 motor increments after rounding. C.29.3 handles sending that total through the available command field.

Now change the radius to 0.06 m and the interface to an absolute wheel-position target. It counts 1,000 units per wheel revolution, currently reads 3,000 and admits targets from 0 to 65,535. The requested forward displacement remains 2 m. Assume rolling without slip and completion at the commanded count.

Recover the count's new meaning before reusing the calculation. If q is the target, the wheel travels (q−3,000)/1,000 revolutions, so the model gives:

d=(q−3,000)/1,000 * 2π * 0.06 m.

The new scale already counts wheel revolutions; use that scale to obtain the needed increment:

Δq=2/(2π*0.06) * 1,000 ≈ 5,305.16477.

Round to 5,305 and add the initial count, giving target q=8,305. This target is admitted. Its modeled displacement is approximately 1.99993788 m. Nearest-integer rounding contributes at most half a count, corresponding to π*0.06/1,000 m ≈ 0.00018850 m; compare that contribution with the receiving accuracy requirement.

Reusing the former total 63,662 as the absolute target would pass the new range check but give approximately 22.8690 m under this model. The value has changed from a relative motor increment to an absolute wheel position. The repair therefore changes the physical parameter, the count-to-motion correspondence and the computational use of initial state together.

The useful return is the new command with its displacement and rounding consequence. A changed starting count requires recomputing the target; a changed radius or count scale reopens their correspondence. A slip or incomplete motion requires the relevant physical or execution repair. C.29.3's preparation and completion comparison can then use this revised command.

