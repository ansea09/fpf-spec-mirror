---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:11"
section_title: "SoTA alignment (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__012_sota-alignment-informative.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:11 — SoTA alignment (informative)"
line_start: 99350
line_end: 99359
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:11 - SoTA alignment (informative)

Although FPF is conceptual (not a data governance framework), `G.Core` aligns Part‑G authoring with modern best practice patterns seen across post‑2015 work:

* **Selective prediction / abstention** informs tri‑state guard discipline: abstaining or degrading is a first-class outcome, not an error coerced into a scalar.
* **Set-valued / conformal methods** motivate set-return semantics: when comparability is partial or uncertainty is structural, returning sets/regions is often the SoTA-friendly representation.
* **Multiobjective optimization and quality-diversity** reinforce declared set-result and `Archive` semantics instead of forced “best single scalar”.
* **Monotone constrained modelling** (where used) supports “legality-first” scoring/aggregation: constraints and admissibility precede optimization, mirroring CG‑Spec gate discipline.
* **Schema evolution and contract testing** motivate id-stable conformance points and typed trigger catalogues: stable identifiers + regression hooks are the practical mechanism for safe refactoring.

