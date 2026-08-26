---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:8"
section_title: "Guard anti-patterns and remedies (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__009_guard-anti-patterns-and-remedies-informative.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:8 — Guard anti-patterns and remedies (informative)"
line_start: 44717
line_end: 44728
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

### C.3.A:8 - Guard anti-patterns and remedies (informative)

| Anti-pattern | Why it is wrong | Remedy |
| --- | --- | --- |
| Widening G to repair kind mismatch | applicability is not typed compatibility | repair the order/bridge/adapter or refuse |
| Asking whether an unnamed candidate “counts” | hides candidate identity and signature edition | stay at declaration level or name the exact candidate and four inputs |
| Treating unavailable support as `false` | turns non-settlement into world-side failure | retain `unknown`; let the guard refuse separately |
| Treating a mask label as a kind | hides the declaration and constraints | designate the exact RoleMask edition and evaluate `J_mask` |
| Copying source classification through a bridge | bridge evidence is not target truth | recover the target declaration and evaluate the target candidate afresh |
| Gating on KindAT | the facet is not a guard Characteristic | use the actual declaration, judgment, scope, evidence, and policy predicates |
| Calling a plan, row, or JobSlice “the work” | erases the world/episteme boundary | identify the independently grounded dated Work occurrence when Work is current |

