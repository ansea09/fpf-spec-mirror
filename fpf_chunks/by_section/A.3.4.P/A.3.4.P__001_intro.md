---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Wording Repair: Recover Objects and Claims"
section_id: "A.3.4.P:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__001_intro.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.3.4.P — Transformation Wording Repair: Recover Objects and Claims"
  - "A.3.4.P:intro — Intro"
line_start: 13182
line_end: 13201
dependencies:
  - "A.10"
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
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
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
  - "F.19"
keywords:
  - "actual subject facts"
  - "and continuity rule"
  - "and other neighboring claims through exact governors"
  - "and routing flow structure"
  - "boundary"
  - "distinguishing performed-work or other direct actor-side claims from differently typed influence sources"
  - "evidence"
  - "method"
  - "publication"
  - "representation"
  - "transformation ontic precision restoration. Repairs change-situation wording by grounding any actual U.Transformation in its changed referent"
  - "work"
---

## A.3.4.P - Transformation Wording Repair: Recover Objects and Claims

> **Type:** A.3.4 precision-restoration child pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

**Intent.** Restore precision when wording about change hides the object or claim under concern. Distinguish a bounded transformation and its changed referent from acting-System and influence claims, then identify the neighboring objects and their relations before rewriting.

**Use this when.** Use `A.3.4.P` when source or FPF-governed wording such as "pipeline", "dataflow", "flow", "network", "circuit", "path", "slice", "workflow", "process", "operation", "transformation", or "change" seems to name the thing under concern, but the text has not yet recovered what kind of FPF value is actually current.

**First useful move.** State what the passage claims and about which subject. Recover the meaning of the ambiguous word and the conditions that change its use. Test an actual-change claim under A.3.4; open actor, influence and other neighboring questions only when the passage makes those claims. Then rewrite the affected wording, preserving its useful content. Keep a `TransformationWordingRepair` note only when the receiving use needs inspectable detail.

**Not this pattern when.**

- If one bounded transformation is already identified and only its ordinary use continues, apply `A.3.4` directly.
- If the current claim is already a selected transformation-flow structure, use `E.18`.
- If the current claim is a graph, morphism, category, algebra, path, circuit expression, network expression, or other mathematical description, use `E.18.2` and `C.29`.
- If the current claim is only a semantic way of doing, method description, mechanism, work plan, dated work, evidence relation, publication relation, gate, decision, assurance, result, or temporal claim, use the subject pattern.
- If the word is quoted source wording with no FPF-governed use, keep it quote-only.

