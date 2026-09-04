---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:1"
section_title: "Purpose and audience"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__002_purpose-and-audience.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:1 — Purpose and audience"
line_start: 46437
line_end: 46449
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

### C.3.A:1 - Purpose and audience

Use this Annex when a receiving action must check one or more of these without blending them:

1. the declaration-level compatibility of a claim's quantified kind with a consumer's expected kind;
2. the classification of one exact candidate under one exact signature edition and slice;
3. Claim or Work scope coverage;
4. cross-context kind and scope bridges and their R consequences;
5. a RoleMask declaration and exact masked judgment; or
6. an actual capability use or Work occurrence whose input/output candidates are typed.

The practical gain is a readable refusal reason. “The kinds are incompatible”, “the candidate is known not to satisfy the criterion”, “classification is unknown”, “scope does not cover”, “a bridge is unavailable”, and “the guard refuses use” remain different outcomes.

