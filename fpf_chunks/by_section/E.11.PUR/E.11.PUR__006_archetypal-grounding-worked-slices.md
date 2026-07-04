---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Recommendation and Pattern-Use Sequence"
section_id: "E.11.PUR:5"
section_title: "Archetypal Grounding - Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__006_archetypal-grounding-worked-slices.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "E.11.PUR — Pattern-Use Recommendation and Pattern-Use Sequence"
  - "E.11.PUR:5 — Archetypal Grounding - Worked Slices"
line_start: 70938
line_end: 70977
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.5"
  - "A.16"
  - "A.21"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "E.8"
keywords:
---

### E.11.PUR:5 - Archetypal Grounding - Worked Slices

#### E.11.PUR:5.1 - Architecture Entry

Situation: a team says, "We need the next useful FPF move for our reactor-cooling architecture problem."

Use `PatternUseRecommendation@Context`:

```text
ProjectConcernRef: reactor-cooling architecture uncertainty
BoundedContextRef: concept review before module selection
CandidatePatternUseSet: C.30, C.30.ASV, C.29, A.21
ApplicablePatternUseSet: C.30 and C.30.ASV are applicable
RecommendedPatternUse: C.30 first, then C.30.ASV if selected structure is still unclear
ReasonForRecommendation: the question is about architecture and selected structures before a gate or work plan is current
OutputRefOrOutputShape: ArchitectureQuestionCard@Project
BlockedStrongerUse: no gate passage, no work authorization, no performed work
NextGoverningPatternRef: C.30
```

The ordinary sentence may still say "first useful move", but the FPF record names recommended pattern use.

#### E.11.PUR:5.2 - Agent Repair

Situation: an assisting agent notices vague "process" wording in a technical standard and asks what to do next.

Use `PatternUseRecommendation@Context` when the current question is which FPF pattern to apply. Recommend `E.10` first. If `E.10` recovers transformation-situation wording, use `A.3.4.P`. If it recovers work-entry readiness wording, use `E.10.MOVE` and possibly `A.15.5`. If the agent plans tool calls, use `C.24` for the call plan.

#### E.11.PUR:5.3 - P2W Boundary

Situation: a problem card has accepted problem-side material and the team asks for the next useful FPF use.

Use `E.18.1` for the carry-through relation. `E.18.1` may cite `PatternUseRecommendation@Context` when the next recovered value is a recommended FPF pattern use. P2W remains the relation from accepted problem-side material to the next governed value; `E.11.PUR` does not replace it.

#### E.11.PUR:5.4 - Proxy Failure

Situation: a team keeps recommending `C.30` because it is the familiar architecture pattern, even when the current concern is a work-entry readiness question before a test run.

Do not treat the familiar pattern id as the value. Fill `PatternUseRecommendation@Context` against the current concern and expected practical result. If the needed result is a readiness disposition, recommend `A.15.5`; if the needed result is an architecture question, recommend `C.30`. The visible proxy, "we used the architecture pattern again", gets worse when it hides missing kit, commitment, or launch-gate relations.

