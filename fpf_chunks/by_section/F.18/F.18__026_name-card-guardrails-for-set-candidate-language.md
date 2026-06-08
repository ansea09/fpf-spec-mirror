---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:24a"
section_title: "Name-card guardrails for set-candidate language"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__026_name-card-guardrails-for-set-candidate-language.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:24a — Name-card guardrails for set-candidate language"
line_start: 75767
line_end: 75787
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:24a - Name-card guardrails for set-candidate language

- Keep `Palette`, `Front`, `Archive`, and `Shortlist` as distinct head families rather than as aliases of one generic `portfolio`.
- Prefer this head family when the local entry load matches it:
  - `TraditionPalette` when `SubjectKind=Tradition`
  - `Q-Front`
  - `ExplorationArchive`
  - `Shortlist`
- The shortlisted family stays internally coherent:
  - `RankedShortlist ⊑ Shortlist`
  - `ShortlistId` is one `Id` specialized to an emitted shortlist
  - `ChoiceSet` may appear only as one mathematical gloss for the shortlist's set object, not as one rival public head
- Reserve `Pareto` for actual non-domination under a declared `DominanceSet`; do not use it for weighted ranking, popularity ordering, or one post-lens shortlist.
- Treat bare `portfolio` as a guarded reject here because current `FPF` already uses `portfolio` as one broader selector/set-return family. When the local set family is recoverable, do not reuse that broader head as the local winner.
- Treat bare `shortlist` as admissible only when the selected-set family is intended and the declared source set kind plus the named lens are already recoverable nearby.
- When one set-family candidate is tied to traditions, methods, hypotheses, or environment-method pairs, say the `SubjectKind` explicitly instead of letting the head noun do the work by implication.
- When one shortlist is emitted from one front or one archive, say the declared source set kind and the named lens instead of letting `Shortlist` drift into one generic selector result.
- If one local explanation still needs `ChoiceSet`, say that it is the mathematical set gloss for the shortlist rather than letting it read like one second public set family.
- Good examples include `TraditionPalette` for a tradition-member palette, `Palette + SubjectKind=MethodFamily`, `Q-Front`, `ExplorationArchive`, `ShortlistFromQFront`, `RankedShortlistFromShortlist`, and `ShortlistId`.
- Bad examples include bare `portfolio`, `SoTA portfolio`, `Pareto shortlist`, `Pareto archive`, and `frontier set` when the declared dominance basis is still missing.

