---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__009_problem.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:2 — Problem"
line_start: 102764
line_end: 102778
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
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
* when expressions carry distinct F.17 source-local meanings, requires the complete crossing path—exact local senses, an obtaining F.9 Bridge, a separate bounded-use proposition, and the appropriate reliance or assurance branch—while treating pins as audit references rather than as the crossing facts;

* produces **set-valued outcomes** when only partial orders are admissible or when every named member is included for one bounded use, without confusing those meanings; when exact non-Method members already have a current inclusion basis, it declares that result without routing them through method-family selection;
* cleanly separates:

  * **selector object set and components** (registry, selector boundary, and result-declaration records),
  * **universal Part‑G invariants** (carried by `G.Core`),
  * **method-specific and generator-specific semantics** (carried only through `Extensions` blocks).

