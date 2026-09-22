---
chunk_kind: "child"
pattern_id: "C.16.RM"
pattern_title: "Repair a Measurement Model or Arrangement"
section_id: "C.16.RM:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.RM/C.16.RM__006_archetypal-grounding.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "C.16.RM — Repair a Measurement Model or Arrangement"
  - "C.16.RM:5 — Archetypal Grounding"
line_start: 53781
line_end: 53850
dependencies:
  - "B.5.MPC.R"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.16"
  - "C.16.IR"
  - "C.16.MR"
  - "C.28"
  - "C.29.2"
keywords:
---

### C.16.RM:5 - Archetypal Grounding

#### C.16.RM:5.1 - Separate a beam from background and detector offset

The wanted quantity is the optical power I from a beam at a detector. A supplied linear response model is:

`r = g*(I + A) + b.`

Here A is ambient optical power, g = 2 mV/mW is a known response coefficient and b is an electronic offset. The detector is unsaturated. During the following three observations, g, A and b remain unchanged:

| Condition | Reading |
| --- | --- |
| Beam on, receiver exposed | 12 mV |
| Beam off, receiver exposed to the same ambient light | 6 mV |
| Opaque cap over the receiver, excluding beam and ambient light | 2 mV |

The capped reading gives b = 2 mV. Subtracting only this offset from the beam-on reading and dividing by g gives 5 mW. That is I + A; it leaves the wanted beam contribution mixed with ambient light.

Use the exposed beam-off reading to cancel both unchanged contributions:

`I = (r_on - r_off)/g = (12 - 6) mV / (2 mV/mW) = 3 mW.`

The same observations give A = (6 - 2)/2 = 2 mW. Substitution reconstructs all three readings. The repaired interpretation supplies I using observations already available.

A possible arrangement repair is to shield the receiver from ambient light while preserving the beam at the detector. Under A = 0 and the same g and b, a new beam-on reading of 8 mV would also give I = 3 mW. That value is conditional until the new measurement is performed.

Suppose instead that the shield removes ambient light but transmits a known fraction alpha = 0.9 of the original beam. With the same g and b, a new reading of 7.4 mV gives (7.4 - 2)/2 = 2.7 mW for the transmitted beam. Recover the original beam through the changed relation:

`I = (r - b)/(g*alpha) = (7.4 - 2)/(2*0.9) = 3 mW.`

If the transmission fraction is unknown, this new reading alone leaves the original beam unresolved. The earlier valid on/off observations still support their result of 3 mW. The shield's changed interaction must be included in any conclusion drawn from the new measurement.

For a question I ≤ 3.2 mW, suppose each on/off reading has an arbitrary additive error between -0.1 and 0.1 mV, while g and the shared background remain fixed. The difference gives 2.9 ≤ I ≤ 3.1 mW, so the bound settles the question. Drift in A between on and off would add a further term. Alternating readings reduces that uncertainty only with a supplied account of the drift; the alternation itself is insufficient.

#### C.16.RM:5.2 - Reduce loading enough to settle the question

A source has open-circuit voltage E and internal resistance Rs between 0.8 and 1.2 MΩ. A meter with input resistance Rm reads:

`V = E*Rm/(Rs + Rm), hence E = V*(1 + Rs/Rm).`

With Rm = 1 MΩ and an ideal reading V = 5 V, the compatible bound is 9 ≤ E ≤ 11 V. It leaves the question E ≤ 10.5 V unresolved.

One option is to determine Rs more closely and correct the loaded reading. Another is to reduce loading. The second option is available here: change to a meter with Rm = 100 MΩ. Assume the same passive-source model and resistance range apply to the new measurement. If its ideal reading is 9.9 V, then:

`9.9*(1 + 0.8/100) ≤ E ≤ 9.9*(1 + 1.2/100),`

so 9.9792 ≤ E ≤ 10.0188 V. The bound settles E ≤ 10.5 V while Rs remains unresolved. The repair earned its place by reducing the unknown resistance's influence on this conclusion.

Restore a supplied reading-error bound of ±0.1 V for the new meter. The positive factors give:

`9.8*1.008 ≤ E ≤ 10.0*1.012,`

or 9.8784 ≤ E ≤ 10.12 V. The same decision remains settled. A more demanding threshold could make the error bound consequential again. Meter range, voltage stability and the loading model belong to the physical premises supporting this use.

#### C.16.RM:5.3 - Recompute a rate from retained observations

A flow logger records cumulative pulses and elapsed timestamps in milliseconds. The supplied calibration is one pulse per litre, with no missed pulses or resets in the interval. The receiving question concerns average volume flow over that interval.

Both endpoint timestamps are taken at pulse events. The retained endpoints are 120 pulses at 10,000 ms and 180 pulses at 40,000 ms. A program subtracts the timestamps, divides the count difference by 30,000 and labels its output 0.002 L/s.

The pulse difference represents 60 L. The timestamp difference represents 30 s. Evaluating the intended relation gives:

`average flow = 60 L / 30 s = 2 L/s.`

The program's division obtained 0.002 L/ms and then attached the wrong time unit. Convert milliseconds to seconds before division, or convert the resulting rate afterward. Both repairs give 2 L/s. Recompute other affected intervals from their retained counts and timestamps.

A reference input of 10 pulses over 2,000 ms should give 5 L/s. A program result of 0.005 L/s reproduces the conversion fault; 5 L/s confirms this operation for that input. This calculation checks the implementation. Whether the actual instrument counted every litre and its clock tracked elapsed time requires the relevant calibration and observation when those premises are disputed.

The useful result is a repaired average rate from existing observations. Repeating the physical flow measurement is unnecessary for the identified unit-conversion fault while those observations and their calibration remain usable.

