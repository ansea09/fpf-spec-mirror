---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__002_problem-frame.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:1 — Problem frame"
line_start: 80117
line_end: 80132
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.22.PFR"
  - "C.24"
  - "C.30"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUA"
  - "E.18"
  - "E.18.1"
  - "G.11"
keywords:
---

### E.11.PUR:1 - Problem frame

#### E.11.PUR:1.1 - Use this when

Use `E.11.PUR` after one or more candidate pattern uses have been inspected and a person or assisting agent needs to decide whether each use fits, which use to recommend, how several uses should be coordinated, or whether an earlier result already answers the current concern. The candidates may remain conversational in ordinary bounded use; addressable `CandidatePatternUse@Context` values are required only when a named later reliance needs them.

**Primary EntityOfConcern.** One current applicability, recommendation, or coordination judgement over already inspected candidate pattern uses. When that judgement must remain addressable, it may be represented by `PatternUseApplicabilityFinding@Context`, `PatternUseRecommendation@Context`, or `PatternUseCoordination@Context`; a `PatternUseOrderingRelation@Context` exists only inside the coordination it qualifies.

The `@Context` suffix on these compatibility support names is retrieval wording only. It names no bounded-context entity, generic situation, project container, relation participant, or identity field; every episteme follows C.2.1 identity, and an ordering relation follows its own participant, condition, obtaining, and occurrence rules.

**What this buys.** Applicability no longer silently becomes recommendation, presentation order no longer silently becomes workflow order, and a result that still answers the concern can end a repeated pattern use. A project can preserve exact reasons for a consequential recommendation without burdening ordinary bounded use with five separate forms or copying one result under another stage name.

**Not this pattern when.** Use `E.11` while public entries are still being compared. Use `E.11.PUA` to use one selected pattern and obtain its first result. Use A.15 for work planning or performed work, A.21 for a gate decision, and the direct decision or authorization pattern when those claims are current.

In this pattern, *next move* is Plain shorthand for the currently recommended pattern use or conditional continuation. It is not a shared `Move` identity, `U.Method`, `U.WorkPlan`, performed `U.Work`, or actual `U.Transformation`.

