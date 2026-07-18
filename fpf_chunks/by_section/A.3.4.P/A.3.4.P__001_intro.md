---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Ontic Precision Restoration"
section_id: "A.3.4.P:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__001_intro.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.3.4.P — Transformation Ontic Precision Restoration"
  - "A.3.4.P:intro — Intro"
line_start: 7822
line_end: 7847
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.20"
  - "E.24"
  - "E.8"
  - "F.18"
  - "F.19"
keywords:
---

## A.3.4.P - Transformation Ontic Precision Restoration

> **Type:** A.3.4 precision-restoration child pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

**Plain-name.** Transformation wording repair.

**Intent.** Restore precision when wording about a situation of change hides whether the current FPF object is one bounded `U.Transformation`, a transformed object, a transformer-side system or holon, a method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence relation, publication relation, gate, decision, result, or source label.

**Use this when.** Use `A.3.4.P` when source or FPF-governed wording such as "pipeline", "dataflow", "flow", "network", "circuit", "path", "slice", "workflow", "process", "operation", "transformation", or "change" seems to name the thing under concern, but the text has not yet recovered what kind of FPF value is actually current.

**First useful restoration output.** Fill a compact `TransformationWordingRepair` note: encountered wording, working concern, recovered transformation or non-transformation object, recovered slot or neighboring pattern, retained use, blocked overread, and remaining reader use. Then rewrite only the wording that depends on the recovered kind.

**What goes wrong if missed.** The text silently creates a local ontology from a convenient source label: "process" becomes method in one paragraph, dated work in another, and transformation-flow structure in a third; "path" becomes evidence sufficiency, assurance, gate passage, deontic permission, work authorization, or release authorization; "function" becomes behavior, bearer, mathematical function, and software routine at once.

**What this buys.** The reader gets one small restoration use that keeps bounded transformations, compound transformation-flow structures, formal descriptions, methods, mechanisms, work, evidence, publications, and functional structures in their governing places before any wording is changed.

**Not this pattern when.**

- If one bounded transformation is already identified and only its ordinary use continues, apply `A.3.4` directly.
- If the current claim is already a selected transformation-flow structure, use `E.18`.
- If the current claim is a graph, morphism, category, algebra, path, circuit expression, network expression, or other mathematical description, use `E.18.2` and `C.29`.
- If the current claim is only a semantic way of doing, method description, mechanism, work plan, dated work, evidence relation, publication relation, gate, decision, assurance, result, or temporal claim, use the direct governing pattern.
- If the word is quoted source wording with no FPF-governed use, keep it quote-only.

