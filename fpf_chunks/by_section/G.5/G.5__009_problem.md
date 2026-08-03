---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__009_problem.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:2 — Problem"
line_start: 99775
line_end: 99789
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

### G.5:2 - Problem

How to design a **general, auditable dispatcher** that:

* preserves **pluralism** (families from competing Traditions stay disjoint) while remaining **dispatchable** (selection is possible and explainable);
* does **not embed algorithmic dogma** in the core selector kernel;
* respects semantic-context boundaries through the complete current crossing path—exact local senses, an obtaining F.9 Bridge, a separate bounded-use proposition, and the appropriate reliance or assurance branch—while treating pins as audit references rather than as the crossing facts;

* produces **set‑valued outcomes** when only partial orders are admissible;
* cleanly separates:

  * **selector object set and components** (registry, selector boundary, and publication records),
  * **universal Part‑G invariants** (carried by `G.Core`),
  * **method-specific and generator-specific semantics** (carried only through `Extensions` blocks).

