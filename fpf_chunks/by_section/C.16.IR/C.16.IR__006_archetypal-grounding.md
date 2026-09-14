---
chunk_kind: "child"
pattern_id: "C.16.IR"
pattern_title: "Determine What an Indication Can Resolve"
section_id: "C.16.IR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.IR/C.16.IR__006_archetypal-grounding.md"
commit_sha: "0caf9a10acfc0ee17c32fc71f6173b542393f0a4"
heading_path:
  - "C.16.IR — Determine What an Indication Can Resolve"
  - "C.16.IR:5 — Archetypal Grounding"
line_start: 52974
line_end: 53025
dependencies:
  - "A.3.3.PI"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.16.MR"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### C.16.IR:5 - Archetypal Grounding

#### C.16.IR:5.1 - One source, two loads and an unidentified influence

Suppose a source has unknown open-circuit voltage E ≥ 0 and finite internal resistance Rs ≥ 0. An ideal meter of known input resistance Rm > 0 reads the connected voltage:

`V = E*Rm/(Rs + Rm).`

The relation and passive-source assumptions are supplied. The question is whether E is at most 8 V.

A reading of 5 V with Rm = 1 MΩ gives:

`E = 5 V*(1 + Rs/(1 MΩ)).`

Rs = 0 and E = 5 V fit the reading; Rs = 1 MΩ and E = 10 V also fit it. The threshold question is unresolved. The reading does establish E ≥ 5 V under the stated domain.

Now a meter with Rm = 3 MΩ reads 7.5 V. Assume E and Rs stayed unchanged between the readings and both meters obey the given model. The two equations share those two unknowns. Express E from each equation and equate:

`V1*(1 + Rs/R1) = V2*(1 + Rs/R2).`

Hence, when the denominator is nonzero,

`Rs = (V2 - V1)/(V1/R1 - V2/R2).`

The supplied readings give Rs = 1 MΩ and E = 10 V. Substitution recovers both 5 V and 7.5 V. The answer to E ≤ 8 V is now no.

The shared-source condition does work here. If E changes between readings, replacing it with E1 and E2 leaves the original inference unsupported. A second number is useful through the relation connecting its measurement to the first.

For two zero readings under the same model, E = 0 follows while Rs can be any finite nonnegative value. A zero denominator in the derived formula is a reason to return to the original equations. Full recovery of Rs is unnecessary for this voltage result.

#### C.16.IR:5.2 - A saturated reading can settle one threshold

An ideal instrument reports r = min(y,10), where y ≥ 0 is a quantity expressed on the instrument's stated scale. For r = 10, every y ≥ 10 is compatible.

If the working question is y ≥ 8, the reading settles it. If the question is y ≥ 12, y = 10 and y = 13 are compatible cases with different answers. Reporting y = 10 as the determined quantity would lose that distinction.

Now suppose the reported reading follows `r = min(y,10) + e`, with -0.2 ≤ e ≤ 0.2. This error is applied after the clipping operation. For the same r = 10, the ideal clipped value can lie from 9.8 to 10. The compatible set becomes y ≥ 9.8: y = 9.8 with e = 0.2 is a feasible endpoint, and every y ≥ 10 fits with e = 0.

The reading still settles y ≥ 8. It no longer settles y ≥ 10, since y = 9.8 and y = 10 are both compatible. This is a bound-based result; no probability was assigned to the error. Repeated readings do not narrow that bound merely by being repeated. A narrower result needs a relation that supports the reduction, such as a justified stochastic error model or a smaller error bound.

#### C.16.IR:5.3 - Combining counter remainders

A device starts at zero, increments once per event and stores N modulo 16. No reset or missed event occurs. A supplied count bound is 0 ≤ N < 100. The stored value 5 permits:

`N in {5,21,37,53,69,85}.`

These six values come from `N = 5 + 16*k` with an integer k in the range allowed by the bound. They all satisfy the original operation. The reading settles N < 90, while N < 30 remains unresolved; 21 and 37 are witnesses.

Suppose a second counter starts at the same event boundary, sees every same event, and stores N modulo 17. It reports 4. Test the six candidates against this second relation: only N = 21 remains. The physical event correspondence and initialization make the mathematical intersection appropriate.

If the supplied bound is relaxed to N < 300, both 21 and 293 satisfy the two remainders. The earlier uniqueness conclusion therefore depended on the bound. If the counters cover different event intervals, use separate counts and recover the relation between them before combining their readings.

