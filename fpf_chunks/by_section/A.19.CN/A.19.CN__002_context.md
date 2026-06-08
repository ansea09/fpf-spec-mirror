---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN‑frame (comparability & normalization)"
section_id: "A.19.CN:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__002_context.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.19.CN — CN‑frame (comparability & normalization)"
  - "A.19.CN:1 — Context"
line_start: 24744
line_end: 24758
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

* a **CN‑frame** = *(Context‑local)* **CharacteristicSpace (CS)** + **chart** (coordinate patch + units) + a referenced **Normalization mechanism (UNM)** pinned from `CN‑Spec.normalization`. Any semantics of admissibility, invariants, and `≡_UNM` is governed by the A.19.UNM governing pattern (see **A.19.UNM**);
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the **governance card** (S) that fixes admissible charts/normalization *references*/comparability/Γ‑fold for that lens **in one `U.BoundedContext`**; *CN‑Description* is the didactic surface (D) with worked examples and anti‑patterns. Mechanism‑level term cards (e.g., `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, `IndicatorChoicePolicy`) are governed by the corresponding **A.19.<MechId>** patterns and are only **cited** here.

**Lexical guard (map/Map, by reference).** Follow the lexical discipline governed by **A.19.UNM**: avoid introducing new normalization tokens that use “map/Map/mapping” (because `…Map` is a Part‑G method‑type kind). In normalization contexts prefer **normalize / transform / re‑parameterize**. Legacy tokens (including retired κ‑notation) are handled via **alias docking** (F.18); A.19.CN applies this rule and does not redefine it.

A.19.CN makes this *operational and auditable*.

