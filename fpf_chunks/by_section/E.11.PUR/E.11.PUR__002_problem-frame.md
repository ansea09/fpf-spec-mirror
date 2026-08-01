---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__002_problem-frame.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:1 — Problem frame"
line_start: 77047
line_end: 77058
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
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

Use `E.11.PUR` after one or more `CandidatePatternUse@Context` values are available and a person or assisting agent needs to decide whether each use fits, which use to recommend, or how several uses should be coordinated for the current concern.

**Primary EntityOfConcern.** One current PUR-governed value over already inspected candidate pattern uses: a `PatternUseApplicabilityFinding@Context`, a `PatternUseRecommendation@Context`, or a `PatternUseCoordination@Context`. A `PatternUseOrderingRelation@Context` is current only inside the coordination it qualifies.

**What this buys.** Applicability no longer silently becomes recommendation, and presentation order no longer silently becomes workflow order. A project can preserve exact reasons for a consequential recommendation without burdening ordinary bounded use with five separate forms.

**Not this pattern when.** Use `E.11` while public cards are still being compared. Use `E.11.PUA` to apply one selected pattern and obtain its first result. Use A.15 for work planning or performed work, A.21 for a gate decision, and the direct decision or authorization pattern when those claims are current.

