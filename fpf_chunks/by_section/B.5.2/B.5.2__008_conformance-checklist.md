---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__008_conformance-checklist.md"
commit_sha: "aa10af7e8221518114822d00bb9cf11e6c41f6b2"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:7 — Conformance Checklist"
line_start: 41167
line_end: 41175
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:7 - Conformance Checklist

- `CC-B.5.2-1` Every abductive run **SHALL** begin from a declared `U.AbductivePrompt`; arbitrary prose fragments are not sufficient prompt-entry forms.
- `CC-B.5.2-2` A conforming abductive run **SHALL** record at least one rival candidate alongside any selected prime hypothesis, unless the author explicitly justifies why no rival candidate was available.
- `CC-B.5.2-3` Selection of a prime hypothesis **SHALL** cite at least two explicit plausibility filters.
- `CC-B.5.2-4` The selected prime hypothesis SHALL be published as a hypothesis-bearing `U.Episteme` with its scope, support and limitations. An assurance level, if a receiving use requires one, SHALL follow B.3.3's applicable justified profile rather than the fact that abduction occurred.
- `CC-B.5.2-5` The prime hypothesis record **SHALL** preserve a link to the initiating prompt and to the filtering rationale that justified selection.
- `CC-B.5.2-6` A conforming conjecture SHALL expose an interpretable implication, deduction or possible discriminating contrast. The availability and value of a check SHALL be considered separately before selecting evidence acquisition. An unavailable probe neither creates an observation nor by itself forbids a separately supported present decision.

