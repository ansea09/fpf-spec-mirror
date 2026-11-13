---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:intro — Intro"
line_start: 47275
line_end: 47291
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

## B.3.5 - Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)
> **Status:** Stable
> **Type:** Pattern

**At a glance.** Use B.3.5 when a human-facing structural relation or a collection's own belongs-to relation has been selected for an additional assurance account without exposing constructive machinery as the public vocabulary.

**Use this when.** Use this assurance profile only when a publication choice or named requirement elects it for a relation claim. State the readable relation first. After election, structural parthood and collection belonging follow separate trace and `validationMode` obligations. The trace reports the relation facts and their grounds for inspection.

**What goes wrong if missed.** The readable relation and its assurance account collapse: authors either lose usable relation sentences, treat collection belonging as parthood, prohibit separately grounded parthood by label, or make a trace look like the cause of the claim.

**What this buys.** Working-Model relations stay readable, while an elected assurance branch supplies the right inspectable account without changing the relation kind.

**Not this pattern when.** Not this pattern when a relation claim is sufficient and no publication choice or requirement elects this assurance profile. Also not this pattern when the question is how to construct the trace (`C.13`), which mereology relation kind is intended (`A.14`), whether a whole must be reidentified (`B.2`), or whether a candidate name deserves durable U-kindhood (`E.24.UK`).

> **One‑line summary.**
> CT2R-LOG keeps **ComponentOf**, ordinary belongs-to sentences, **PortionOf**, and **AspectOf** readable while respecting their different relation kinds. When this assurance profile is elected, structural parthood uses its applicable construction account; collection belonging uses a current `C.13 set` trace. The relation pattern supplies the conditions for each relation, including any separately claimed parthood.

