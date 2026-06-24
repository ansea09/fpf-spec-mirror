---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Recommendation and Pattern-Use Sequence"
section_id: "E.11.PUR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__012_sota-echoing.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "E.11.PUR — Pattern-Use Recommendation and Pattern-Use Sequence"
  - "E.11.PUR:11 — SoTA-Echoing"
line_start: 67604
line_end: 67612
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

### E.11.PUR:11 - SoTA-Echoing

| Source family | Use in this pattern | Local adoption |
| --- | --- | --- |
| Pattern-language practice for problem-situation recognition and pattern composition | Supports the "patterns as words, phrases as composed uses" teaching line. | Adopt the metaphor only as didactic guidance; precise FPF text still names pattern-use relations and direct governing patterns. |
| Current recommender-system and human-centered XAI practice | Separates candidate generation, applicability or ranking, recommendation, explanation, user control, and bias or proxy checks. | Adapt the separation without importing an IT recommender ontology: `CandidatePatternUseSet`, `ApplicablePatternUseSet`, `RecommendedPatternUse`, `ReasonForRecommendation`, expected practical gain, and proxy-failure checks make pattern recommendation reviewable by a practitioner. |
| Human-centered guidance for task-suitable labels and first-use recognition | Supports keeping engineer-facing phrases such as "first useful move" when they help recognition. | Adapt by requiring the durable FPF relation name to remain recoverable after the friendly label. |
| Current FPF `E.11`, `E.8`, and `E.10` governance | Governs entry publication, pattern-local recognition, and wording restoration. | Reuse existing first-entry and authoring law; this child pattern supplies only the pattern-use recommendation relation. |

