---
chunk_kind: "child"
pattern_id: "C.16.MR"
pattern_title: "Construct a Measurement Relation"
section_id: "C.16.MR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.MR/C.16.MR__006_archetypal-grounding.md"
commit_sha: "368bb772285d22b29eaaf20180500f49f1a2c9d7"
heading_path:
  - "C.16.MR — Construct a Measurement Relation"
  - "C.16.MR:5 — Archetypal Grounding"
line_start: 52736
line_end: 52791
dependencies:
  - "A.3.3"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "B.5.RC"
  - "C.11.DUA"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.16.MR:5 - Archetypal Grounding

#### C.16.MR:5.1 - Recover an open-circuit voltage from a loaded indication

The sought value is a source's open-circuit voltage E. The supplied ideal circuit represents the source by E in series with resistance Rs. Connecting a voltmeter of input resistance Rm completes the circuit. Assume positive resistances, a stable source and a meter whose indication equals its terminal voltage.

The common current I satisfies

    E = I*Rs + I*Rm
    V = I*Rm

Eliminating I gives

    V = E*Rm/(Rs+Rm)
    E = V*(1+Rs/Rm)

For Rs=Rm=1 megohm and V=5 volts, the inferred open-circuit voltage is 10 volts. Substitution returns I=5 microamperes and the original 5-volt indication. The two voltage drops explain both the sign and magnitude of the correction.

If the desired quantity were instead the connected terminal voltage, V would already be the value in this ideal model. The measurement question determines which result is needed.

As Rm becomes large relative to Rs, loading becomes small and V approaches E. For a use that needs only a bound on this effect, E-V=V*Rs/Rm supplies it. If Rs/Rm is at most 0.001 and V is 5 volts, the loading correction is at most 0.005 volts. Whether that is negligible depends on the receiving question and the other uncertainties.

If Rs is unknown, the same relation can expose an unresolved contribution. With V=5 volts, Rm=1 megohm and Rs between 0.8 and 1.2 megohms, E lies between 9 and 11 volts under the ideal assumptions. The interval may be enough. A performed measurement additionally accounts for indication and resistance uncertainty and relevant model inadequacy.

#### C.16.MR:5.2 - Build the relation for an assessment of independent performance

The sought quantity p is the fraction of a stated population able to perform a specified action independently under specified conditions. An applicable assessment account supplies s, the probability of a positive response when that capability is present, and f, the probability when it is absent.

Partition the population by the capability. The probability of a positive response is

    q = s*p + f*(1-p)
      = f + (s-f)*p

For s=0.9 and f=0.1, q=0.1+0.8*p. A sample positive fraction of 0.7 gives the estimate p=0.75 obtained by substituting the sample fraction. Its use also depends on sampling uncertainty, uncertainty in s and f and whether those rates apply to this population and procedure. The formula describes the expected response; the sample proportion estimates it.

If s=f, q is independent of p and the test does not distinguish the two conditions through this response. The failure is visible in the constructed relation. Further estimates of that same marginal positive rate cannot identify p through this relation.

Now change the procedure by offering hints. The earlier rates may cease to apply. Recover rates for the changed procedure or restore independent performance if that remains the target. The subject's capability and assessment Methods establish those conditions; the general construction shows where they enter the inference.

This population estimate does not identify which particular people or agents have the capability. That different question requires an individual assessment account.

#### C.16.MR:5.3 - Interpret a wrapping event counter

A modeled counter increments once for each event and retains a value from 0 to 15, returning to 0 after 15. Readings immediately before and after an interval are r0 and r1. The sought quantity is the number N of intervening events. Assume no reset, no missed increment and readings taken at the stated interval boundaries.

The counter operation gives

    r1 = (r0+N) mod 16
    N = d + 16*k

Here d is the least nonnegative remainder of r1-r0 modulo 16, and k is a nonnegative integer. With r0=14 and r1=3, d=5: the compatible counts are 5,21,37 and so on.

If the interval is known to contain fewer than 16 events, N=5. Without that bound, subtracting the displayed numbers or returning the modular difference loses possible complete wraps. A wider counter, a recorded wrap count or shorter observation intervals can supply the missing information for a later measurement.

To infer elapsed time, another relation is needed: the counter must count timing ticks with an applicable tick-duration account. A counter of arbitrary work events alone measures no duration. This identifies a missing relation rather than inventing one from the numerical display.

