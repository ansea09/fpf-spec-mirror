---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__007_archetypal-grounding-tell-show-show.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 34960
line_end: 34990
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:5 - Archetypal Grounding (Tell–Show–Show)

**Tell.** UNM is the conceptual “front gate” that turns “raw coordinate values” into “values comparable under declared invariants”, by:
1) choosing an admissible normalization method instance (with evidence and validity window),
2) applying it to produce NCVs,
3) returning only the inverse, equivalence, class-level operation or query result whose additional conditions hold for the receiving use.

**Show (System).** A team compares alternatives using `normalization-based` comparability:
- CN-Spec declares:
  - `comparability.mode = normalization-based`
  - `normalization.invariants = {unit-alignment, polarity}`
  - a method instance `M_unitScale` with validity window `VW_2026Q1` and evidence pins.
- UNM applies `M_unitScale` to each coordinate value, producing NCVs.
- CPM compares the NCV-profiles (not raw profiles).
- If evidence pins are missing for a slice, UNM returns `GuardDecision = abstain`, preventing “fake comparability”.

**Show (Episteme) — a many-to-one LUT.** Let D be `{0,1,2}` and `n(0)=0`, `n(1)=n(2)=1`. Applying n to 2 returns the transformed value 1. Equality of outputs partitions D into `{0}` and `{1,2}`: it is reflexive, symmetric and transitive. The directed edge `2→1` supplies no edge `1→2`.

The query `x>0` is constant on each class and can be answered from the class. The query `x>1` is false at 1 and true at 2, so no function of their common class can recover it. Retain x, split that class with the needed distinction, or return the unresolved answer set `{false,true}` when that set answers the receiving question. Selecting 1 as a representative would answer a question about the representative, not the lost original input.

Now let a partial operation f be defined at 0 and 1 but not at 2, with `f(1)=0`. Because `1 ≡_UNM 2` while availability differs, f cannot descend to a representative-independent operation on these classes. Matching only the outputs that happen to exist would miss the failure. Preserve the distinguishing input or refine the class before applying f.

**Show — reversible conversion and partial normalization.** For exact temperature values in the declared physical domain, Celsius-to-kelvin conversion `n(c)=c+273.15` has inverse `c=k-273.15` on its image. For example, 20 °C maps to 293.15 K and back to 20 °C. Measurement uncertainty remains governed by its measurement result; the exact coordinate law does not remove it. More generally, a strictly monotone encoding has an inverse on its image, not automatically everywhere in the named target.

Restrict the LUT above to D=`{0,1}`. Input 2 is then undefined, has no NCV and belongs to no kernel class of that partial normalizer. A policy's degraded-evidence allowance does not define n(2). Likewise, an idempotence claim needs composability and `n(n(x))=n(x)` on the named domain; a function's fibers do not prove it.

**Show (P2W and transformation flow).** Missing/stale inputs:
- A selector (or comparator) requires comparability under `normalization-based` mode.
- UNM finds that a required coordinate value is missing/stale for the current slice and the instance validity window.
- UNM returns `GuardDecision = abstain` (fail-closed) and identifies the missing current measurement. The receiver may reuse an adequate existing result, choose a justified acquisition, or leave this comparison unresolved; any acquisition has its own planning and enactment basis.

