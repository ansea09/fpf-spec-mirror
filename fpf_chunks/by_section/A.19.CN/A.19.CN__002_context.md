---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__002_context.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:1 — Context"
line_start: 33654
line_end: 33668
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

* a **CN‑frame** = a selected **CharacteristicSpace (CS)** + **chart** (coordinate patch and value basis, with Units where applicable) + a referenced **Normalization mechanism (UNM)** for one named bearer, comparison basis, scope/window, and intended use. A.19.UNM defines directed normalization, its preservation/loss basis and any separately justified `≡_UNM` class use;
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the specification (S) that fixes the bearer, characteristic and scale editions, chart, comparison basis, scope/window, normalization references, comparability rule, aggregation choice, and intended use; *CN‑Description* is the didactic surface (D) with worked examples and anti-patterns. Mechanism-level term cards such as `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, and `IndicatorChoicePolicy` remain defined by the corresponding **A.19.<MechId>** patterns and are only cited here.

**Normalization names.** Use A.19.UNM’s method and instance identifiers to identify the selected normalization. Ordinary mathematical “mapping” describes its function; it does not assert a specialized FPF `Map` kind or an F.9 Bridge. Resolve a legacy identifier through F.18 alias docking when needed.

A.19.CN makes this *operational and auditable*.

