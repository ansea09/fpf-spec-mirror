---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Generate and Compare Candidate Explanations (Abductive Loop)"
section_id: "B.5.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__008_conformance-checklist.md"
commit_sha: "d73588bdcb52ed173d7b4c1552b2ce199a548c64"
heading_path:
  - "B.5.2 — Generate and Compare Candidate Explanations (Abductive Loop)"
  - "B.5.2:7 — Conformance Checklist"
line_start: 49703
line_end: 49711
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
  - "C.28.CM"
keywords:
---

### B.5.2:7 - Conformance Checklist

- `CC-B.5.2-1` Every abductive run **SHALL** begin from a question account whose content and grounds meet `B.5.2.0`'s `U.AbductivePrompt` entry conditions.
- `CC-B.5.2-2` A conforming abductive run **SHALL** make the serious candidates actually considered recoverable. When no serious rival has been identified, state that limit and qualify any preference claim by the available comparison.
- `CC-B.5.2-3` Selection of a prime hypothesis **SHALL** state the applicable plausibility criteria and grounds sufficient to justify its preference for the declared prompt and intended use.
- `CC-B.5.2-4` The selected prime hypothesis SHALL be published as a hypothesis-bearing `U.Episteme` with its scope, support and limitations. An assurance level, if a receiving use requires one, SHALL follow B.3.3's applicable justified profile rather than the fact that abduction occurred.
- `CC-B.5.2-5` The prime hypothesis record **SHALL** preserve a link to the initiating prompt and to the filtering rationale that justified selection.
- `CC-B.5.2-6` A conforming conjecture SHALL expose an interpretable implication, deduction or possible discriminating contrast. The availability and value of a check SHALL be considered separately before selecting evidence acquisition. An unavailable probe neither creates an observation nor by itself forbids a separately supported present decision.

