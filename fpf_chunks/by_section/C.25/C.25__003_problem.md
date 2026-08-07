---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__003_problem.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:2 — Problem"
line_start: 53021
line_end: 53035
dependencies:
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:2 - Problem

Without a normal form for engineering quality families:

1. **Composite families are scalarized illegally.**
   Terms such as *resilience*, *security*, or *maintainability* are treated as if one number exhausted them.
2. **Scope is confused with measurement.**
   A claim's `ClaimScope` / `WorkScope` is spoken of as if it were a magnitude rather than a USM set-valued applicability object.
3. **Mechanism and status are mistaken for evidence or metrics.**
   Presence of redundancy, certification, or audit controls is described as if it were itself a measurement value.
4. **Guards become unstable.**
   Admission checks silently mix scope coverage, numerical thresholds, mechanism presence, and evidence freshness in one phrase.
5. **Evaluative governing-pattern selection remains underspecified.**
   After `C.16.Q` repairs a bare quality term, or `C.16.P` repairs characteristic, scale, score, metric, or proxy wording inside that term, the admissible endpoint is unclear unless FPF distinguishes single-CHR cases from bundle-shaped quality families.

