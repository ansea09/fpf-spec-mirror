---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:3"
section_title: "Shared outcome model"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__004_shared-outcome-model.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:3 — Shared outcome model"
line_start: 45832
line_end: 45843
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

### C.3.A:3 - Shared outcome model

All guards obey these invariants.

1. **Exact declarations.** A kind designator never substitutes for the exact `KindSignature` edition needed by the use.
2. **Candidate only when current.** A universally quantified claim or proof can be checked for declaration compatibility without inventing a wildcard candidate. Actual application, test attachment, capability input/output use, or other candidate-bearing action pins the candidate and evaluates the four-input judgment.
3. **Three classification values.** `true` means the criterion is known to hold; `false` means it is known to fail; `unknown` means the evaluation cannot settle because evidence or a declared dependency is unavailable or the candidate is outside the evaluation domain.
4. **Separate guard disposition.** A guard returns an action disposition such as allow or refuse. Both `false` and `unknown` normally cause fail-closed refusal, but the guard MUST preserve which classification value it consumed.
5. **Scope separation.** Scope coverage is a USM predicate over a named slice. It does not classify the candidate or repair kind compatibility.
6. **Bridge separation.** An obtaining KindBridge relation connects exact source and target kinds. Its separate bridge assertion supplies mapping, `CL^k`, loss, evidence, definedness, and admitted use; neither object creates a target kind, signature, or judgment.
7. **R-only consequences.** Justified scope- and kind-bridge consequences affect R only. They do not change F, G, or classification truth.

