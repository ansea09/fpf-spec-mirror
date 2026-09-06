---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN‑frame (comparability & normalization)"
section_id: "A.19.CN:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__002_context.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.19.CN — CN‑frame (comparability & normalization)"
  - "A.19.CN:1 — Context"
line_start: 31697
line_end: 31711
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CL/loss notes"
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "bridges"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "normalization refs"
  - "registry"
  - "Γ-fold governance"
---

### A.19.CN:1 - Context

A.19 established a substrate‑neutral picture:

* a **CN‑frame** = a selected **CharacteristicSpace (CS)** + **chart** (coordinate patch + units) + a referenced **Normalization mechanism (UNM)** for one named bearer, comparison basis, scope/window, and intended use. A.19.UNM defines the admissibility, invariants, and `≡_UNM` semantics;
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the specification (S) that fixes the bearer, characteristic and scale editions, chart, comparison basis, scope/window, normalization references, comparability rule, aggregation choice, and intended use; *CN‑Description* is the didactic surface (D) with worked examples and anti-patterns. Mechanism-level term cards such as `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, and `IndicatorChoicePolicy` remain defined by the corresponding **A.19.<MechId>** patterns and are only cited here.

**Lexical guard (map/Map, by reference).** Follow the lexical discipline governed by **A.19.UNM**: avoid introducing new normalization tokens that use “map/Map/mapping” (because `…Map` is a Part‑G method‑type kind). In normalization contexts prefer **normalize / transform / re‑parameterize**. Legacy tokens (including retired κ‑notation) are handled via **alias docking** (F.18); A.19.CN applies this rule and does not redefine it.

A.19.CN makes this *operational and auditable*.

