---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__001_intro.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:intro — Intro"
line_start: 34542
line_end: 34558
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

## B.3.5 - Working-Model Relations & Grounding (CT2R-LOG)
> **Status:** Stable
> **Type:** Pattern

**At a glance.** Use B.3.5 when a human-facing Working-Model relation such as `ut:ComponentOf`, `ut:MemberOf`, `ut:PortionOf`, or `ut:AspectOf` needs an assurance grounding relation without exposing constructive machinery as the public vocabulary.

**Use this when.** Use this pattern when a structural edge must remain readable to engineers and managers while still carrying `validationMode` and, for structural claims, a `tv:groundedBy` link to a reconstructible Compose-CAL trace.

**What goes wrong if missed.** The readable relation layer and the constructive proof layer collapse into each other: either authors lose usable relation names, or reviewers cannot reconstruct why a structural edge should be trusted.

**What this buys.** The alias-plus-grounding split: Working-Model relations stay canonical for communication, while CT2R-LOG carries the grounding channel and validation stance that E.24.UK can cite for structural U-kind admission.

**Not this pattern when.** Not this pattern when the current question is how to construct the trace (`C.13`), which mereology relation kind is intended (`A.14`), whether a new holon exists (`B.2`), or whether a candidate name deserves durable U-kindhood (`E.24.UK`).

> **One‑line summary.**
> CT2R-LOG treats the everyday **Working-Model relations**— **ut:ComponentOf**, **ut:MemberOf**, **ut:PortionOf**, **ut:AspectOf** —as the **public relation layer** for structure, while binding each published edge to a **grounding trace** and a **declared `tv:validationMode`**. Authors keep using a short list of relations; reviewers get reconstructible provenance.

