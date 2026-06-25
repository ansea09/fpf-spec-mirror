---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:11.4"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__018_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:11.4 — Common Anti-Patterns and How to Avoid Them"
line_start: 67401
line_end: 67409
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
keywords:
---

### E.10:11.4 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Correction |
| --- | --- | --- |
| Replace one umbrella with another | `support` becomes `basis`, `route` becomes `path`, or `posture` becomes `status` without recovering the kind. | Recover EntityOfConcern, relation position, governing pattern, admissible use, and blocked overread before choosing wording. |
| Pattern does the work | A pattern is said to send, route, approve, authorize, or repair a project object. | Say the user applies the governing pattern, or name the resulting relation, record, or admissible use. |
| Description becomes object | A description, diagram, publication face, source span, or dashboard is treated as the in-life object or authority. | Use A.7, C.2.1, E.17, publication patterns, and the direct governing pattern for the claim being made. |
| Source label becomes FPF kind | A quoted term, acronym, legacy label, or local handle is kept as a live kind. | Treat it as source wording until the governing FPF kind or relation is recovered. |

