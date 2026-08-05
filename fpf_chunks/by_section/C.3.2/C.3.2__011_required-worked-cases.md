---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:9"
section_title: "Required Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__011_required-worked-cases.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:9 — Required Worked Cases"
line_start: 44984
line_end: 45009
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
---

### C.3.2:9 - Required Worked Cases

#### C.3.2:9.1 - Physical pump

Within bounded context `Plant-7`, `CoolingPumpKind` is the local kind identified by Plant-7's declared cooling-function distinction. Signature edition `CPS-2` names effective scheme `PS-7`, declares pump candidates, and states a criterion in terms of directly governed flow, heat-transfer, and operating-state features for plant slice `S-14`.

Pump #14 is independently identified as the physical candidate. A calibrated measurement-result episteme supports the assertion that its flow and temperature-difference features meet the criterion; the measurement result is not Pump #14 and does not constitute its cooling performance. With those feature facts settled, `J(Pump #14, CoolingPumpKind, CPS-2, S-14) = true`. An extension used by a maintenance query may represent Pump #14, but the query row does not create its classification.

#### C.3.2:9.2 - Episteme and publication form

The exact maintenance-instruction episteme `MI-22` is evaluated against local kind `DiagnosticInstructionKind` using its claim-bearing content and governed subject. For one bounded maintenance-reading use, the selected page arrangement and notation `MI-22-PDF-Layout` is the publication form that expresses the chosen `MI-22` edition, while exact digital file `MI-22-PDF-File-7` is the `U.PresentationCarrier` that bears that form. Separately, selected arrangement and notation `MI-22-HTML-Layout` is another publication form that expresses the same chosen edition for that bounded use, while exact digital file `MI-22-HTML-File-8` is the `U.PresentationCarrier` that bears the HTML form. This case asserts no C.29 representation because it selects no elements with an explicit correspondence to independently recovered objects and changes no admitted modeling or reasoning operation.

Changing the arrangement, notation, presentation carrier, or file encoding does not by itself change candidate episteme `MI-22`, satisfy the `DiagnosticInstructionKind` criterion, create another kind, or rewrite the classification judgment. If the claim-bearing content, exact signature edition, context slice, and governed candidate facts remain unchanged, the same judgment remains current.

#### C.3.2:9.3 - Non-entity temperature value

The value `87 °C`, interpreted under a declared measurement scale, unit, reference scheme, and time, is evaluated against local kind `HighTemperatureValueKind` whose criterion is a declared interval. The candidate remains that governed non-entity value; no value-shaped entity is fabricated. The classification may stay inside the measurement or diagnostic claim content. The unit and interval must be pinned before a `true` or `false` result is possible.

#### C.3.2:9.4 - Schema label

A database row carries schema label `Customer`, but the receiving claim asks whether account holder #441 is a contractual customer. The label is a cue or supporting source, not the contractual relation that makes the world-side criterion hold. The practitioner must recover the actual candidate and the direct contractual facts. If the candidate were instead the row itself and the local kind concerned row shapes, that different candidate and criterion would have to be stated explicitly.

#### C.3.2:9.5 - Unavailable measurement

At later slice `S-15`, the cooling-pump signature still requires a governed flow measurement, but the measurement dependency is unavailable. The current evaluation returns `unknown`. A safety guard declines reliance on Pump #14 as a cooling pump for that use. The guard does not return `false`, prove that the pump lacks cooling performance, or remove it from a historical extension for `S-14`.

