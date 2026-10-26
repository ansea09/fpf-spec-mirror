---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:7"
section_title: "Conformance requirements"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__008_conformance-requirements.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:7 — Conformance requirements"
line_start: 76913
line_end: 76928
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture fitness-function source wording"
  - "architecture-characteristic eval program"
  - "comparison input"
  - "current-architecture evaluation"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "monitoring"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:7 - Conformance requirements

| Requirement | Required result |
|---|---|
| `CC-ACE-1` | Every eval references declared ACS rows or C.25 Q-Bundle slots. |
| `CC-ACE-2` | Every eval names evaluated candidates, bearers, or selected structures. |
| `CC-ACE-3` | Purpose, scope, eval operation, trigger mode, result form and run conditions are recoverable; parity is established when the receiving inference depends on it. |
| `CC-ACE-4` | Measurement claims require `C.16`; composite quality claims require `C.25`. |
| `CC-ACE-5` | Before receiving work relies on an eval result, its missing-data treatment and material proxy risks are understood, with relevant constraints and counter-characteristics protected. |
| `CC-ACE-6` | Source-side "fitness function" wording retains its source meaning; any FPF object or claim is identified by the operation, expression or relation actually meant. |
| `CC-ACE-7` | A check or test is admitted only as one eval operation when an expectation or hard constraint is being inspected. |
| `CC-ACE-8` | The eval result does not select, decide, certify, or carry an architecture-adequacy claim by itself. |
| `CC-ACE-9` | A project-local program names both `projectWorkOccurrenceRef` and `architectureEvalProgramProjectUseRelationRef`; the suffix or either reference alone asserts no locality. |
| `CC-ACE-10` | The record separately identifies any reusable Method, MethodDescription, planned evaluation, dated evaluation Work, actual operation application, and typed result that the use needs; `evalOperation` or `resultForm` supplies none of those occurrences or identities. |
| `CC-ACE-11` | Every actual evaluation use binds one exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, evaluation window, and input projections; `evalScope`, `runContext`, and `parityFrameRef` do not replace them. |

