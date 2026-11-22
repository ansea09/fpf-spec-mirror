---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace: Coordinates, State Predicates and Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:0"
section_title: "First use: declare a space and one predicate"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__002_first-use-declare-a-space-and-one-predicate.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "A.19 — CharacteristicSpace: Coordinates, State Predicates and Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:0 — First use: declare a space and one predicate"
line_start: 36199
line_end: 36229
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.ULSAM"
  - "A.19.UNM"
  - "A.2.6"
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
  - "CharacteristicSpacePredicate"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "reusable state conditions"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
  - "system-role–Method–Work assertions stay outside A.19"
---

### A.19:0 - First use: declare a space and one predicate

Begin with the conclusion or action for which someone needs the space. Identify its subject and the conditions under which that conclusion could change. When the question concerns a whole, a part, or their interaction, decide which of those subjects each proposed Characteristic describes. A total can answer a question about the whole while leaving the distribution among its parts undetermined. If the question relates several kinds of holon, choose the relevant span of parts and wholes for each kind. Decide what the model at each scale must distinguish. To explain a relation between scales or a joint result, identify what connects the models and which conditions must hold across them. A model of each part can suffice for a local decision while omitting a condition on their joint operation.

**First move.** For each proposed slot, ask what distinction it retains. Could two configurations that the subject and its operating conditions permit have the same retained coordinates yet require different conclusions or different grounds? If so, identify the missing distinction or relation and revise the space or the claimed use. An applicable rule can also establish directly that the retained coordinates suffice. Specify each chosen Characteristic, its subject or input roles, its Scale and admissible values. Shared constraints can make combinations of individually admissible values unreachable. Add order, topology, distance, a map or a reusable predicate when the use calls for it.

**Applying a declared space.** For example, a pump team has already chosen two slots for `PumpOperatingSpace`.

| Slot | Characteristic and subject | Scale |
| --- | --- | --- |
| `coolantTemperature` | temperature of one Pump | degrees Celsius, `0..120` |
| `dischargePressure` | discharge pressure of one Pump | kilopascals, `0..1000` |

For Pump #37, the available tuple of Coordinates is `(72 °C, 315 kPa)`. The reusable condition is:

> `ready(x) := 60 °C <= x.coolantTemperature <= 80 °C and x.dischargePressure >= 300 kPa`.

For this tuple the predicate is true. This establishes the answer to the stated test in the declared space. Suppose the operating decision also requires a minimum flow and two allowed configurations at those temperatures and pressures give flows on opposite sides of that minimum. The same tuple would then support different operating decisions. The team can retain a flow coordinate or supply a relation that settles the flow condition for this use. The original temperature and pressure test stays usable for the question it answers.

**Add only what the next use needs.**

- If the Characteristic, Scale, or measurement chain is not sound yet, start with A.17, A.18, or C.16.
- Use A.19.UNM for normalization, A.19.UINDM for indicator choice, A.19.USCM for scoring, A.19.ULSAM for scale aggregation, A.19.CPM for comparison, and A.19.SelectorMechanism for selection. Use B.1 for a separate holonic-composition claim. G.0 checks whether the numeric operation is admissible.
- Use A.3.3 when the space types a dynamics model.
- Use A.19.CHR when a characterization task needs shared suite contracts; add A.15.3 for typed planned fillings of independently declared positions, and E.18 when the selected flow structure is needed. Use E.20 when an FPF change introduces or revises mechanism or suite semantics or their governing definitions.
- Use the evaluation, gate, evidence, or assurance pattern for that separate use.

If none of those questions is current, stop with the space and predicate above.

**Boundary.** A.19 defines the space and reusable predicate. A subject binding, partial observation, evaluation, result, comparison, gate, evidence use, view, or publication remains a separate value or occurrence under its pattern.

