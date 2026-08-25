---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:0"
section_title: "First use: declare a space and one predicate"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__002_first-use-declare-a-space-and-one-predicate.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:0 — First use: declare a space and one predicate"
line_start: 28002
line_end: 28032
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UNM"
  - "A.2.6"
  - "A.6.5"
  - "B.1"
  - "C.16"
  - "C.2.1"
  - "E.24"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.4"
  - "U.ClaimScope"
  - "U.ContextSlice"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
  - "system-role–Method–Work assertions stay outside A.19"
---

### A.19:0 - First use: declare a space and one predicate

Use A.19 when you need to say which Characteristics form one state space and what reusable condition can be tested on a state in that space.

**First move.** Name the `CharacteristicSpace` and list its slots. Each slot names one Characteristic, its subject or input roles, and one Scale with its admissible values. Add order, topology, distance, or a mapping only when a real use needs it.

**Smallest complete case.** A pump team declares `PumpOperatingSpace` with two slots:

| Slot | Characteristic and subject | Scale |
| --- | --- | --- |
| `coolantTemperature` | temperature of one Pump | degrees Celsius, `0..120` |
| `dischargePressure` | discharge pressure of one Pump | kilopascals, `0..1000` |

For Pump #37, the available Coordinate tuple is `(72 °C, 315 kPa)`. The reusable condition is:

> `ready(x) := 60 °C <= x.coolantTemperature <= 80 °C and x.dischargePressure >= 300 kPa`.

For this tuple, `ready(x)` is true. That is the practical result: a reader can recover the two meanings, inspect the current input, and repeat the test. The declaration does not by itself claim that the readings are current, authorize work, or pass a gate.

**Add only what the next use needs.**

- If the Characteristic, Scale, or measurement chain is not sound yet, start with A.17, A.18, or C.16.
- For normalization, indicator choice, scoring, aggregation, comparison, or selection, use A.19.UNM, A.19.UINDM, A.19.USCM, A.19.ULSAM or B.1, A.19.CPM, or A.19.SelectorMechanism respectively. G.0 checks whether the numeric operation is admissible.
- Use A.3.3 when the space types a dynamics model.
- Use A.19.CHR with A.15.3 or E.18 only for a planned suite or baseline, and E.20 only for a project specialization.
- Use the direct evaluation, gate, evidence, or assurance pattern for that separate use.

If none of those questions is current, stop with the space and predicate above.

**Boundary.** A.19 defines the space and reusable predicate. A subject binding, partial observation, evaluation, result, comparison, gate, evidence use, view, or publication remains a separate value or occurrence under its direct pattern.

