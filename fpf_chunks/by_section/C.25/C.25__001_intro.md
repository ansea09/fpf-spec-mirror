---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__001_intro.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:intro — Intro"
line_start: 53717
line_end: 53737
dependencies:
  - "A.10"
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

## C.25 - Q-Bundle: Authoring "-ilities" as Structured Quality Bundles

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Quality-bundle normal form.

**Builds on.**
`C.2.1` for the enclosing quality-claim episteme, `A.2.6` for scope algebra, `A.6.1` for exact mechanism references when current, and `C.16` / `A.18` for Characteristic and Scale legality.
**Coordinates with.**
`C.17-C.19` for quality-related measurement families, `C.16.P` when characteristic/scale/score wording is not yet recoverable, `A.15` for method, work-plan, or work-occurrence gating, and `C.16.Q` for quality/evaluative-characterization wording before the endpoint is one explicit characteristic, Q-Bundle-shaped claim content, objective, or another governing pattern.

**Use this pattern when.** Use C.25 when a familiar quality family such as availability, resilience, security, or maintainability may be hiding several differently typed contributors and the reader needs one claim that keeps them distinct.

**First useful move.** Ask: *what would make this quality claim false?* If one measure on one declared Scale answers the question, state that one Characteristic and stop. Use Q-Bundle-shaped claim content only when several differently typed contributors—such as a measure and scope, or measures plus a load-bearing window or mechanism—jointly determine the answer.

**First result.** Write one readable quality claim about one exact bearer and include only the contributors on which its truth or the next receiving action depends. An optional slot is omitted unless changing that slot could change the current claim or receiving action.

**Nearest non-use.** Stay with the direct Characteristic pattern when one measure and Scale carry the claim. Use the direct scope, measurement, evidence, assurance, gate, publication, viability-envelope, or temporal pattern when that neighboring question—not quality-family decomposition—is the current work.

