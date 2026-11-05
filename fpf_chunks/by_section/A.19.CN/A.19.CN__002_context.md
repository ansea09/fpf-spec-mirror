---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__002_context.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:1 — Context"
line_start: 36424
line_end: 36438
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "loss evidence"
  - "maintained editions"
  - "normalization refs"
  - "optional CL"
  - "semantic relations"
  - "separate use claims"
  - "Γ-fold governance"
---

### A.19.CN:1 - Context

A.19 established a substrate‑neutral picture:

* a **CN‑frame** = a selected **CharacteristicSpace (CS)** + **chart** (coordinate patch and value basis, with Units where applicable) + a referenced **Normalization mechanism (UNM)** when the use needs normalization, for one named bearer, comparison basis, intended use, and any scope/window that qualifies it. A.19.UNM defines directed normalization, its preservation/loss basis and any separately justified `≡_UNM` class use;
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch-points**: state predicates use observable characteristics; an evaluation establishes whether their conditions hold for the named bearer and window;
* **entity/relational mixtures** across CN‑frames, represented by the schemas in §8.4, with each required correspondence grounded under its own rule.

**Frame, specification and explanation.** A *CN‑frame* is the selected basis for interpreting and comparing the readings. Its *CN‑Spec* fixes the bearer, characteristic and scale editions, chart, comparison basis, comparability rule, intended use and qualifying scope/window, with normalization and aggregation choices when used. A *CN‑Description* explains that basis through worked examples and anti-patterns. Mechanism-level terms such as `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, and `IndicatorChoicePolicy` retain the definitions supplied by the corresponding `A.19.<MechId>` patterns.

**Normalization names.** Use A.19.UNM’s method and instance identifiers to identify the selected normalization. Ordinary mathematical “mapping” describes its function; it does not assert a specialized FPF `Map` kind or an F.9 Bridge. Resolve a legacy identifier through F.18 alias docking when needed.

The practitioner can compare values within this declared basis and identify which conclusions need reconsideration when it changes.

