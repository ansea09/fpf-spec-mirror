---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher & MethodFamily Registry"
section_id: "G.5:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__012_bias-annotation.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "G.5 — Multi‑Method Dispatcher & MethodFamily Registry"
  - "G.5:6 — Bias-Annotation"
line_start: 79214
line_end: 79223
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
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
  - "in core registry/eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:6 - Bias-Annotation

Potential biases and failure modes this pattern explicitly guards against:

* **Monoculture bias (single Tradition dominance by default).** Mitigation: registry requires explicit eligibility/assurance records; selection is set‑returning under partial orders; method‑specific policies stay explicit pins rather than hard-coded defaults.
* **Hidden scalarisation bias.** Mitigation: set‑return semantics is core‑routed; dominance regimes are explicit and each default cites one declared governing definition.
* **“Tool equals method” bias.** Mitigation: notation independence + prohibition of tool keywords in core registry/eligibility fields; tool choices are outside the core.
* **Cross‑Context leakage bias.** Mitigation: explicit crossing pins only; Bridges + CL are required when crossings occur; no implicit crossings.
* **Survivorship bias in refresh.** Mitigation: RSCR triggers are typed/id‑based; freshness/decay and telemetry deltas are first‑class causes with canonical ids.

