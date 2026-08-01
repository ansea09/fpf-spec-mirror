---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:9"
section_title: "Required Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__011_required-worked-cases.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:9 — Required Worked Cases"
line_start: 45060
line_end: 45083
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
  - "KindExtension representation"
  - "KindSignature declaration episteme"
  - "candidate classification"
  - "local kind"
  - "true/false/unknown"
---

### C.3.2:9 - Required Worked Cases

#### C.3.2:9.1 - Physical pump

Plant scheme `PS-7` uses local kind `CoolingPumpKind`. Signature edition `CPS-2` declares pump candidates and a criterion in terms of directly governed flow, heat-transfer, and operating-state features for plant slice `S-14`.

Pump #14 is independently identified as the physical candidate. A calibrated measurement-result episteme supports the assertion that its flow and temperature-difference features meet the criterion; the measurement result is not Pump #14 and does not constitute its cooling performance. With those feature facts settled, `J(Pump #14, CoolingPumpKind, CPS-2, S-14) = true`. An extension used by a maintenance query may represent Pump #14, but the query row does not create its classification.

#### C.3.2:9.2 - Episteme and publication form

The exact maintenance-instruction episteme `MI-22` is evaluated against local kind `DiagnosticInstructionKind` using its claim-bearing content and governed subject. Its PDF and HTML manifestations are publication forms or representations. Converting the PDF to HTML does not change the candidate episteme, satisfy the criterion, or create another kind. If the content is unchanged, the same candidate judgment can remain current under the same edition and slice.

#### C.3.2:9.3 - Non-entity temperature value

The value `87 °C`, interpreted under a declared measurement scale, unit, reference scheme, and time, is evaluated against local kind `HighTemperatureValueKind` whose criterion is a declared interval. The candidate remains that governed non-entity value; no value-shaped entity is fabricated. The classification may stay inside the measurement or diagnostic claim content. The unit and interval must be pinned before a `true` or `false` result is possible.

#### C.3.2:9.4 - Schema label

A database row carries schema label `Customer`, but the receiving claim asks whether account holder #441 is a contractual customer. The label is a cue or supporting source, not the contractual relation that makes the world-side criterion hold. The practitioner must recover the actual candidate and the direct contractual facts. If the candidate were instead the row itself and the local kind concerned row shapes, that different candidate and criterion would have to be stated explicitly.

#### C.3.2:9.5 - Unavailable measurement

At later slice `S-15`, the cooling-pump signature still requires a governed flow measurement, but the measurement dependency is unavailable. The current evaluation returns `unknown`. A safety guard declines reliance on Pump #14 as a cooling pump for that use. The guard does not return `false`, prove that the pump lacks cooling performance, or remove it from a historical extension for `S-14`.

