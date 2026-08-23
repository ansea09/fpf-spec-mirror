---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:15"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__017_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:15 — Common Anti-Patterns and How to Avoid Them"
line_start: 73747
line_end: 73755
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.10.MOVE"
  - "E.10.ROLE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.17"
  - "F.18"
  - "F.19"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
---

### E.10:15 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Correction |
| --- | --- | --- |
| Replace one umbrella with another | `support` becomes `basis`, `route` becomes `path`, or `posture` becomes `status` without recovering the kind. | Write the ordinary domain sentence, select one `E.10:0.0a` branch when relation-like, and name only the applicable pattern contribution and admissible use. If no branch or other governed object can be selected, keep ordinary wording or leave the repair blocked. |
| Pattern does the work | A pattern is said to send, route, approve, authorize, or repair a project object. | Name the person or system that acts and the action it performs. If the sentence is instead about a resulting fact, declaration, report, or representation, use the matching `E.10:0.0a` branch and its pattern. The pattern supplies guidance or a rule; it does not act. |
| Description becomes object | A description, diagram, publication face, source span, or dashboard is treated as the in-life object or authority. | Use A.7, C.2.1, E.17, publication patterns, and the pattern for the claim being made. |
| Source label becomes FPF kind | A quoted term, acronym, legacy label, or local handle is kept as a live kind. | Treat it as source wording until the FPF kind or relation is recovered. |

