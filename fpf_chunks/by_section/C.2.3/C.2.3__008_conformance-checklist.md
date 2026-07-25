---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__008_conformance-checklist.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:7 — Conformance Checklist"
line_start: 42290
line_end: 42307
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
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

### C.2.3:7 - Conformance Checklist

- `CC-F-1` Every normative `U.Episteme` **SHALL** declare exactly one `U.Formality` value, either a default anchor or a local sub-anchor explicitly docked to one.
- `CC-F-2` `F` **SHALL** be treated as an ordinal characteristic; arithmetic over `F` values is invalid.
- `CC-F-3` Higher `F` **SHALL** mean greater or equal strictness of expression, not greater truth, trust, or scope.
- `CC-F-4` Contexts **MUST NOT** publish alternative "formality modes" or "tiers" as surrogates for `F`.
- `CC-F-5` Local sub-anchors **SHALL** preserve the global ordering and the parent anchor meaning.
- `CC-F-6` The episteme-level `F` of a composite episteme **SHALL** be bounded by the least-formal essential support on the relevant support path.
- `CC-F-7` Implementations **MUST NOT** average `F` values numerically.
- `CC-F-8` Changes in `G`, `R`, or `CL` **SHALL NOT** change `F` unless the expression form itself changes.
- `CC-F-9` Cross-context transport **SHALL** preserve the attributed `F`; if the receiving context rewrites the claim materially, it becomes a new episteme with its own `F`.
- `CC-F-10` Translation loss, bridge loss, and plane crossings **SHALL** affect `R` rather than being hidden as `F` changes.
- `CC-F-11` Assigned `F` values **SHALL** be justifiable by observable content such as explicit predicates, executable semantics, or machine-checked proofs.
- `CC-F-12` Declaring a tool or notation **SHALL NOT** by itself justify a higher `F` unless the content satisfies the target anchor semantics.
- `CC-F-13` Status labels such as `Draft`, `Approved`, or `Published` **MUST NOT** substitute for `F`.
- `CC-F-14` A context that uses `F` in gates or policies **SHALL** write those thresholds explicitly.
- `CC-F-15` Language-state facets such as articulation or closure **MUST NOT** be hidden as pseudo-levels of `F`.

