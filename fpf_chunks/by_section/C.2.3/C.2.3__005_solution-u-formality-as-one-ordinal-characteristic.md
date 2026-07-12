---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:4"
section_title: "Solution - U.Formality as one ordinal characteristic"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__005_solution-u-formality-as-one-ordinal-characteristic.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:4 — Solution - U.Formality as one ordinal characteristic"
line_start: 39927
line_end: 39965
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
keywords:
  - "F-scale"
  - "F0-F9"
  - "Formality"
  - "language-state separation"
  - "proof"
  - "rigor"
  - "specification"
---

### C.2.3:4 - Solution - `U.Formality` as one ordinal characteristic

`C.2.3` defines `U.Formality` as the single governing characteristic for rigor of expression in FPF.

#### C.2.3:4.1 - Identity and typing

- **Name:** `U.Formality` (abbreviated `F` in the assurance tuple)
- **Type:** `U.Characteristic`
- **Scale kind:** ordinal
- **Polarity:** `up`
- **Carrier:** any `U.Episteme`
- **Default value family:** `F0...F9`

`F` states **how strictly the content is expressed**. It does not state whether the content is true, well evidenced, widely applicable, or organizationally accepted.

#### C.2.3:4.2 - Role in the typed `F-G-R` tuple

`F` is the formality coordinate in the assurance tuple. Its interaction rules are strict:

- `F` is **not** `G`; scope remains governed by `U.ClaimScope` and other USM structures.
- `F` is **not** `R`; evidence, warrant strength, and decay remain assurance concerns.
- `CL` and bridge losses affect **`R`**, not `F`.
- Changes in notation, carrier, or rendering form do not change `F` if the formal content is preserved.

#### C.2.3:4.3 - Extensibility and local anchors

FPF provides the default anchor ladder `F0...F9`. A context may define sub-anchors or intermediate anchors such as `F4[OCL]` or `F6.5`, but only if:

- global order is preserved,
- the local anchor is explicitly docked to a parent anchor,
- the context does not invent a rival ladder or proxy scale.

#### C.2.3:4.4 - Usage obligations

- Every normative episteme shall declare one `F` value.
- Thresholds that depend on rigor should be written explicitly as `F >= Fk` conditions.
- Any raise or lowering of `F` is a content change, not a status-only change.
- `F` remains declaration and reasoning infrastructure; it is not itself a governance process.

