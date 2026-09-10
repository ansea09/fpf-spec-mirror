---
chunk_kind: "child"
pattern_id: "A.0"
pattern_title: "Onboarding Glossary (NQD & E/E‑LOG)"
section_id: "A.0:QF.1"
section_title: "Early set-result and metric-kind vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.0/A.0__013_early-set-result-and-metric-kind-vocabulary.md"
commit_sha: "ce6fcc3b99b10e42f4b258f84091355b2ee5ab24"
heading_path:
  - "A.0 — Onboarding Glossary (NQD & E/E‑LOG)"
  - "A.0:QF.1 — Early set-result and metric-kind vocabulary"
line_start: 1422
line_end: 1450
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.5"
  - "B.5"
  - "B.5.2.1"
  - "C.17"
  - "C.17-C.19"
  - "C.19"
  - "E.10"
  - "E.2"
  - "E.7"
  - "E.8"
  - "F.17"
  - "G.12"
  - "G.5"
  - "G.9"
  - "G.9-G.12"
keywords:
  - "& queries. novelty"
  - "BLP"
  - "CL^plane"
  - "DeclaredSubstrateInterpretiveView"
  - "OutcomeSpaceRef"
  - "ParetoOnly default"
  - "ReferencePlane"
  - "SearchSpaceRef"
  - "TypedSetViews"
  - "comparability"
  - "declared set result"
  - "explore/exploit (E/E-LOG)"
  - "explore/exploit (E/E‑LOG)"
  - "illumination map (report‑only telemetry)"
  - "novelty"
  - "parity run"
  - "quality-diversity (NQD)"
  - "quality‑diversity (NQD)"
  - "scale-probe"
  - "typed portfolio publication"
---

### A.0:QF.1 - Early set-result and metric-kind vocabulary

- Use `Palette` for a plurality-preserving set with no dominance semantics yet.
- Use `TraditionPalette` only when the members are traditions gathered before later comparison or choice semantics are declared.
- For methods, hypotheses, environment-method pairs, candidate explanations, or other member kinds, use `Palette` plus explicit `SubjectKind` instead of borrowing the `TraditionPalette` head.
- Use `Front` only for a non-dominated set under one declared `DominanceSet`.
- Use `Q-Front` when the declared `DominanceSet` is the declared `Q` components.
- Use `Archive` for a retained set whose purpose is coverage, stepping-stone retention, or frontier expansion rather than current non-domination.
- Use `ExplorationArchive` for the broad retained exploration surface; it is the exploration-specific specialization of `Archive`.
- Use `SteppingStoneSet` only for one narrower retained subset whose stated purpose is future frontier reach rather than the whole archive. It is not part of the ordinary first-pass public-head family for retained exploration.
- Use `Shortlist` for the set chosen from one declared source set by one named lens.
- Use `RankedShortlist` only when that shortlist is explicitly rank-ordered.
- Use `JointUseSet` when every exact member is included for one named use; keep that use, keyed member entries, inclusion conditions, and basis pins under `G.5`.
- Use `ShortlistId` for the stable public token of one emitted shortlist; it is not the shortlist itself.
- Use `ChoiceSet` only when the mathematical set object underlying one shortlist must be named explicitly; do not let it replace the public shortlist head.
- Use `Q-set` for the declared current objective tuple that may ground the current `DominanceSet`.
- For a result or claim used by a pool policy, retain its direct pattern's reference name and kind; for example, `A.2.2` supplies `capabilityInstanceRef` and `capabilityStatementRef`. Use `C.19` for the resulting pool treatment. Citing an input does not add it to `Q` or dominance.
- Use `competenceModelRef` under `C.19` only for one exact model episteme used by the policy; identify the capability and supporting results separately.
- When the pool treatment relies on an evidence-bearing or source-bearing claim, use `a10RelianceRef` for the exact claim and bounded pool-treatment reliance under `A.10`.
- Use `goalSpaceExpansionPolicyRef` under `C.19` when an independently declared archive or curriculum expansion policy governs goal- or task-space growth; that policy does not place a candidate on a front or add a dominance coordinate.
- When future reach depends on a transition or transfer relation, cite its direct rule and supporting result references together with any model episteme actually used. Keep their use in archive/pool policy separate from any explicitly authorized promotion into dominance.
- If one front is meant to be current-`Q` by default, say so as `Q-Front` or as `Front over the declared Q components` rather than leaving the relation between `Q-set` and `DominanceSet` implicit.
- `Use-Value` may be one member of the `Q-set` only when the current Context declares it there; it is not the whole `Q-set` or the default `Q-set` by itself.
- Metric-kind doctrine: the `Q-set` is the candidate/front-facing objective tuple; `Novelty@context` is one context-relative candidate signal; `DeltaDiversity_P` is one set-relative marginal diversity contribution; `IlluminationSummary` is one report-only archive telemetry summary unless one explicit policy promotes it.
- Minimal mathematical lens: the current front lives in one declared comparison or outcome space, while the exploration archive may depend on one declared search, niche, or reachability space. Keep both spaces explicit when they differ.
- Keep `Novelty@context`, `DeltaDiversity_P`, `Surprise`, and `IlluminationSummary` outside the default `Q-set` unless one declared `PromotionPolicy` says otherwise.
- A reader should be able to tell whether one sentence is talking about a `Palette`, a `Front`, an `Archive`, a `SteppingStoneSet`, a `Shortlist`, a `RankedShortlist`, or a `JointUseSet`, and whether one selected set came from one declared source set, before later policy or geometry detail arrives.
- Use `portfolio` only when the portfolio or set-result field is a declared retained set plus a selection/retention rule or a portfolio-publication posture. Do not use bare `portfolio` when `Palette`, `Front`, `Archive`, `SteppingStoneSet`, `Shortlist`, or `RankedShortlist` is already recoverable.

