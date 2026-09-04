---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__018_sota-echoing.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:11 — SoTA-Echoing"
line_start: 104192
line_end: 104209
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

### G.5:11 - SoTA-Echoing

This pattern is designed to carry extension declarations for, not redefine, post-2015 SoTA families through `Uses` plus edition and policy pins:

* **Quality-Diversity survey currentness (2026 DOI `10.1016/j.swevo.2025.102240`, ScienceDirect `S2210650225003979`).** Survey support keeps, for example, approaches, applications, archives, diversity use, and challenges visible, but it does not replace FPF rules. If the current result is the archive or front relation itself, stop at `C.18`. If a later selector consumes that archive or front and uses G.5 to declare its result, keep the archive or front as the source set and emit only an admitted `SelectorOutcomeKind`, with an admitted `SetResultFamily` for a set result; state the ordering and basis pins directly instead of letting survey taxonomy rename the result.
* **QD-as-MOO and archive-centric QD lines.** Current QD work can produce fronts and archives under declared descriptor, distance, dominance, and comparator editions. `C.18` and `A.19.CPM` carry those meanings. Use G.5 only when a later selector-facing declaration is current. The G.5 record cites the front or archive as its source and states one admitted selector outcome.
* **Complementary portfolio and ensemble construction (Kostovska et al., 2023, PMLR 224:11/1–17; Chen et al., 2024, PMLR 235:7568–7585).** Current algorithm-portfolio work selects a diverse, representative, non-redundant portfolio for a named downstream selection task, while submodels in a complementary ensemble have different contributions in combined use. G.5 adopts only the result distinction: a `JointUseSet` states the named use, keyed members, inclusion conditions, and sufficient top-level basis pins. It does not import portfolio or ensemble semantics, imply that members are Methods, or establish compatibility, contribution, co-enactment, or actual selection Work.
* **Cultural and style selected-set labels.** Music, dance, and cultural-market source rows motivate labels such as `StyleShortlist` or `TraditionShortlist` only after term bridges and cultural-evolution case meaning are clear. Such a label remains a recoverable public label over an admitted `SetResultFamily`; it is not another outcome family. Keep `DerivedViewKind`, `BasePaletteRef`, and `SourceSetFamily` visible. G.5 does not define style, tradition, canon, or platform semantics.
* **Quality-Diversity and illumination (post-2015 refinements).** Archive-centric QD families fit naturally as `G.5:Ext.NQD` extension declarations with explicit descriptor, distance, and insertion pins. The practical implication is to emit one admitted selector outcome and, for a set result, to say whether its family is `Shortlist`, `RankedShortlist`, or `JointUseSet`.
* **Open-Endedness (post-2015 line; POET `arXiv:1901.01753`, AlphaEvolve `arXiv:2506.13131`).** POET-class and later open-ended or co-evolutionary families use generator registries plus `TransferRulesRef.edition` pins. The practical implication is to keep pair-valued or retained members explicit inside the applicable admitted set-result family rather than silently squeezing them into one false single-family winner.

* **Algorithm selection and meta-selection (Thompson sampling tutorial `arXiv:1707.02038`; Bayesian optimization tutorial `arXiv:1807.02811`).** Modern selection under uncertainty, robust evaluation, and policy-driven probing use explicit policy records and typed telemetry pins, rather than hard-coded scoring rules. The practical safeguard is that the result label and basis pins must still remain explicit after those policies have acted.
* **Budgeted specialist acquisition (current agentic-search source-pack pressure via `G.2`).** Current agentic search lines compete on time or budget to threshold plus truthful selected-set return when heterogeneous specialists remain non-dominated. Treat those rows as source-pack pressure until cited by `G.2`; `G.5` keeps specialization profiles and set-return semantics explicit instead of forcing one static breadth winner.
* **Preference-learning comparators.** Interactive and learned-preference regimes are treated as comparator or policy records with explicit editions when they are actually declared.

SoTA here is treated as **best-known practice for a declared goal and constraint regime**, not whatever is currently popular.
Evidence-source clarification: peer-reviewed source references carry the most direct citation strength for typed comparison, budget-to-threshold, and truthful selected-set return. Faster-moving workshop, poster, or frontier-exploration lines remain explicit source references for specialization-entry or open-ended pressure, not silently equal evidence for every selector claim.

