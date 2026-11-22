---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:9"
section_title: "Required Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__011_required-worked-cases.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:9 — Required Worked Cases"
line_start: 58128
line_end: 58157
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
  - "E.24.UK"
keywords:
---

### C.3.2:9 - Required Worked Cases

#### C.3.2:9.1 - Physical pump

`CoolingPumpSignature-2` admits physical pump candidates and applies in plant slice `S-14`. Pump #14 is independently identified as a physical pump, so the request is admissible. Governed flow, heat-transfer, and operating-state conditions satisfy the criterion; a calibrated measurement result supports that claim without becoming the pump or its performance. The result is `true`. A maintenance-query extension may represent Pump #14 but does not create its classification.

#### C.3.2:9.2 - Episteme and publication form

Maintenance-instruction episteme `MI-22` is admissible for `DiagnosticInstructionKind` and is evaluated through its claim-bearing content and governed subject. `MI-22-PDF-Layout` and `MI-22-HTML-Layout` are different publication forms for the chosen episteme edition; files that bear them are presentation carriers. Arrangement, form, carrier, or encoding alone changes neither the episteme, criterion satisfaction, kind, nor judgment.

#### C.3.2:9.3 - Non-entity temperature value

Value `87 °C`, with declared scale, unit, interpretation, and time, is admissible for `HighTemperatureValueKind` when the signature's ValueKind accepts that quantity. It can then be judged against the declared interval without fabricating a value-shaped entity.

#### C.3.2:9.4 - Schema label

A row carries label `Customer`, but the claim asks whether account holder #441 is a contractual customer. If the kind admits account-holder Systems or persons rather than database rows, the row itself is not an admissible candidate. For the account holder, the label may support recovery of the governed contractual relation but does not make that relation obtain. A different row-shape kind could make the row admissible under its own criterion.

#### C.3.2:9.5 - Unavailable measurement

For `S-15`, the maintenance team verifies that the edition of `CoolingPumpSignature-2` in use also applies to that slice and that Pump #14 is an admissible candidate. The required flow reading is missing and the remaining evidence leaves the criterion unsettled. The judgement is `unknown`. The safety guard may decline reliance. The result recorded for `S-14` retains its own basis.

#### C.3.2:9.6 - Not-applicable request

The value `87 °C` is submitted to `CoolingPumpSignature-2`, whose candidate ValueKind is physical pump. The request is `not-applicable`; no cooling-pump judgment is formed. Lack of a pump judgment says nothing about whether the temperature value is known.

#### C.3.2:9.7 - Registration-defined membership

A `KindSignature` for `RegisteredSupplierKind` declares supplier candidates and requires an exact obtaining registration-status relation under the current register rule. Supplier #27 is admissible. If that governed relation obtains, it is part of the membership condition even though a registration episteme may also be used as evidence. A copied row or certificate image alone does not create the relation. This preserves legitimate institutional kinds without treating every record as a world-side fact.

