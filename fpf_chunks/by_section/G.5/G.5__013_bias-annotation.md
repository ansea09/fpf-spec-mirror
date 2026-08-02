---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__013_bias-annotation.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:6 — Bias-Annotation"
line_start: 99369
line_end: 99379
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:6 - Bias-Annotation

Potential biases and failure modes this pattern explicitly guards against:

* **Monoculture bias (single Tradition dominance by default).** Mitigation: registry requires explicit eligibility and assurance records; selection is set‑returning under partial orders; method‑specific policies stay explicit pins rather than hard-coded defaults.
* **Hidden scalarisation bias.** Mitigation: set-return semantics is pinned through `G.Core`; dominance regimes are explicit and each default cites one declared governing definition.
* **“Tool equals method” bias.** Mitigation: notation independence and prohibition of tool keywords in core registry and eligibility fields; tool choices are outside the core.
* **Cross‑Context leakage bias.** Mitigation: require exact F.17 endpoint senses, an obtaining F.9 Bridge, a separate C.2.1 bounded-use proposition and the matching A.10 or B.3 reliance branch; keep loss and CL visible where material. Crossing pins and bundles remain audit or publication references and cannot make an implicit crossing admissible.

* **Survivorship bias in refresh.** Mitigation: RSCR triggers are typed and id-based; freshness, decay, and telemetry deltas are first‑class causes with canonical ids.

