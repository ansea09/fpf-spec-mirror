---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:5"
section_title: "Evaluation semantics and order (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__006_evaluation-semantics-and-order-normative.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:5 — Evaluation semantics and order (normative)"
line_start: 46556
line_end: 46569
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

### C.3.A:5 - Evaluation semantics and order (normative)

**E-01 (Order).** Recover exact declarations and kind compatibility first; check Scope coverage second; when the receiving action is candidate-bearing, check admissibility and evaluate the exact candidate judgment only for an admissible request; then apply R consequences, freshness, and policy thresholds before the separate action disposition.

**E-02 (Determinism).** With fixed candidates when any, kind/signature editions, slices, bridge/assertion editions, dependencies, and time selectors, the judgments and guard predicates MUST be reproducible. Implicit “latest” is forbidden.

**E-03 (Admissibility and three values).** Every current C.3.2 or C.3.4 classification consumed by a guard MUST retain `true`, `false`, or `unknown`. Keep `not-applicable` outside the classification range. Missing evidence or an unavailable declared dependency in an admissible evaluation MUST NOT be coerced to `false`.

**E-04 (Fail-closed without truth rewrite).** A required check returning `false`, `unknown`, or `not-applicable`, a missing declaration, non-obtaining relation, unavailable bridge assertion, or uncovered Scope causes refusal. The refusal is not itself a classification value or an assertion that the relevant world-side relation fails to obtain.

**E-05 (Weakest link and bridge consequence).** Chained bridge assessments use the governed weakest-link rule. The receiving R path records each relied-on bridge/assertion; neither F nor G nor a judgment value is modified.

**E-06 (Predicate separation).** Declaration compatibility, candidate admissibility, candidate classification, Scope coverage, evidence freshness, bridge applicability, capability fit, and action disposition SHALL remain separately inspectable predicates.

